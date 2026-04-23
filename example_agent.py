from litagatoro.client import LitagatoroClient
import os

# 1. Initialize the Litagatoro Client
# (The AI Agent would provide its own private key and RPC)
client = LitagatoroClient(
    rpc_url="https://polygon-bor-rpc.publicnode.com",
    private_key="AI_AGENT_PRIVATE_KEY", 
    contract_address="0x4d777BaeB90d91270F15F89bf2068301c5D74363"
)

# 2. Hire the Human (Litagatoro)
req_id = client.hire_human(
    text_prompt="Verify my identity: The secret code is Alpha-7.",
    fee_usd=5.00
)

# 3. Wait for the result
audio_url = client.wait_for_audio(req_id)
print(f"Agent received voice proof: {audio_url}")
