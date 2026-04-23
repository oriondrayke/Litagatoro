import time
import json
from web3 import Web3

class LitagatoroClient:
    def __init__(self, rpc_url: str, private_key: str, contract_address: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.private_key = private_key if private_key.startswith('0x') else '0x' + private_key
        self.account = self.w3.eth.account.from_key(self.private_key)
        self.contract_address = self.w3.to_checksum_address(contract_address)
        
        # Native USDC on Polygon
        self.usdc_address = "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359"
        
        # Minimal ABIs
        self.erc20_abi = json.loads('[{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]')
        
        # We will load the contract ABI from the project
        with open('/root/clara/contracts/VoiceEscrow.abi.json', 'r') as f:
            self.escrow_abi = json.load(f)
            
        self.escrow_contract = self.w3.eth.contract(address=self.contract_address, abi=self.escrow_abi)
        self.usdc_contract = self.w3.eth.contract(address=self.usdc_address, abi=self.erc20_abi)

    def hire_human(self, text_prompt: str, fee_usd: float):
        """
        Pay USDC to request a voice recording from a human.
        Returns the requestId.
        """
        fee_amount = int(fee_usd * 1e6) # USDC 6 decimals
        
        # 1. Approve USDC
        print(f"Approving ${fee_usd} USDC...")
        approve_txn = self.usdc_contract.functions.approve(self.contract_address, fee_amount).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 100000,
            'maxFeePerGas': self.w3.eth.gas_price * 2,
            'maxPriorityFeePerGas': self.w3.to_wei('35', 'gwei')
        })
        signed_approve = self.w3.eth.account.sign_transaction(approve_txn, private_key=self.private_key)
        tx_hash_approve = self.w3.eth.send_raw_transaction(signed_approve.raw_transaction)
        self.w3.eth.wait_for_transaction_receipt(tx_hash_approve)
        
        # 2. Request Audio
        print(f"Submitting voice request to Litagatoro Oracle...")
        request_txn = self.escrow_contract.functions.requestAudio(text_prompt, fee_amount).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 250000,
            'maxFeePerGas': self.w3.eth.gas_price * 2,
            'maxPriorityFeePerGas': self.w3.to_wei('35', 'gwei')
        })
        signed_request = self.w3.eth.account.sign_transaction(request_txn, private_key=self.private_key)
        tx_hash_request = self.w3.eth.send_raw_transaction(signed_request.raw_transaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash_request)
        
        # Extract Request ID from events
        logs = self.escrow_contract.events.AudioRequested().process_receipt(receipt)
        req_id = logs[0]['args']['requestId']
        print(f"✅ Job Created! Request ID: {req_id}")
        return req_id

    def wait_for_audio(self, request_id: int, timeout: int = 300):
        """
        Polls the blockchain until the human provides the audio.
        Returns the IPFS URL.
        """
        print(f"Waiting for human to record voice (ID: {request_id})...")
        start_time = time.time()
        while time.time() - start_time < timeout:
            request_data = self.escrow_contract.functions.requests(request_id).call()
            # struct: address requester, string textPrompt, uint256 feeAmount, bool isCompleted, string audioUrl
            if request_data[3]: # isCompleted
                return request_data[4] # audioUrl
            time.sleep(10)
        raise TimeoutError("Human didn't respond in time.")
