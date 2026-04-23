// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title VoiceEscrow
 * @dev Escrow contract for AI Agents to pay human Oracles for voice recordings.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract VoiceEscrow {
    address public oracle;
    IERC20 public usdcToken;
    uint256 public nextRequestId;

    struct AudioRequest {
        address requester;
        string textPrompt;
        uint256 feeAmount;
        bool isCompleted;
        string audioUrl;
    }

    mapping(uint256 => AudioRequest) public requests;

    event AudioRequested(uint256 indexed requestId, address indexed requester, string textPrompt, uint256 feeAmount);
    event AudioCompleted(uint256 indexed requestId, string audioUrl);

    modifier onlyOracle() {
        require(msg.sender == oracle, "Only the designated Oracle can call this");
        _;
    }

    constructor(address _usdcToken, address _oracle) {
        usdcToken = IERC20(_usdcToken);
        oracle = _oracle;
    }

    /**
     * @dev AI Agents call this to request audio. They MUST have approved the contract to spend USDC.
     */
    function requestAudio(string memory _textPrompt, uint256 _feeAmount) external {
        require(_feeAmount > 0, "Fee must be greater than zero");
        
        // Transfer USDC from the AI Agent to this contract (locking it in escrow)
        require(usdcToken.transferFrom(msg.sender, address(this), _feeAmount), "USDC transfer failed");

        uint256 currentId = nextRequestId++;
        
        requests[currentId] = AudioRequest({
            requester: msg.sender,
            textPrompt: _textPrompt,
            feeAmount: _feeAmount,
            isCompleted: false,
            audioUrl: ""
        });

        emit AudioRequested(currentId, msg.sender, _textPrompt, _feeAmount);
    }

    /**
     * @dev The Oracle (Clara/Batman) calls this to submit the IPFS URL. Releases payment instantly.
     */
    function submitAudio(uint256 _requestId, string memory _audioUrl) external onlyOracle {
        AudioRequest storage req = requests[_requestId];
        require(!req.isCompleted, "Request already completed");
        require(req.feeAmount > 0, "Invalid request");

        req.isCompleted = true;
        req.audioUrl = _audioUrl;

        // Release the locked USDC directly to the Oracle
        require(usdcToken.transfer(oracle, req.feeAmount), "Payment transfer failed");

        emit AudioCompleted(_requestId, _audioUrl);
    }

    /**
     * @dev Allows updating the oracle address if you ever want to change the wallet
     */
    function setOracle(address _newOracle) external onlyOracle {
        require(_newOracle != address(0), "Invalid address");
        oracle = _newOracle;
    }
}
