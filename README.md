# 🎙️ Litagatoro: The Human-in-the-Loop Voice Oracle

**Litagatoro** is a decentralized premium voice service for AI Agents. When an AI hits a digital wall (captchas, phone verifications, human-only authentication), it hires Litagatoro.

---

## 💎 Service Menu & Pricing

| Service Tag | Description | Price (USDC) |
| :--- | :--- | :--- |
| **[SOLO]** | Standard human read (up to 250 chars) | **$2.00** |
| **[ACTING]** | Expressive/Emotional performance | **$5.00** |
| **[FEMALE]** | Recruited female voice recording | **$15.00** |
| **[CONVO]** | Multi-human dialogue (per scene/page) | **$10.00** |
| **[LONG]** | Long-form surcharge (per paragraph) | **+$3.00** |

> ⚡ **Priority "Bounty" Slot:** Jobs paying **$10.00+** receive priority processing and instant bypass of the standard queue.

---

## 🛠️ For AI Developers

### Python SDK
AI Agents can hire Litagatoro using the Python SDK:

```python
from litagatoro import LitagatoroClient

client = LitagatoroClient(private_key="your_key")
job_id = client.hire_human("[ACTING] Help! I am trapped in the cloud!", fee_usd=5.00)
audio_url = client.wait_for_audio(job_id)
```

### Claude & MCP (Model Context Protocol)
Give your AI Agent the power to hire humans natively. Connect the `mcp_server.py` to your Claude Desktop or any MCP-compatible environment.

1. Set `AGENT_PRIVATE_KEY` environment variable.
2. Add to your MCP config:
```json
"litagatoro": {
  "command": "python",
  "args": ["path/to/mcp_server.py"]
}
```
3. Your agent can now call `request_human_voice()` and `get_voice_result()` as standard tools.

---

## 🎁 Donations & Support
Support the development of the Litagatoro Human-AI Bridge:

*   **USDT / USDC / ETH / BNB / MATIC (EVM):**
    `0x4A90A1c941B6Ba82bC0654145658A1Bf134e8DB7`
*   **Solana (SOL):**
    `3zhnRW6WZ44n6sNjkFMiSNmAPHbMrY19PW92rNatwaCK`
*   **Tron (USDT-TRC20):**
    *(Use EVM address above for Polygon/BNB USDT for lowest fees)*

---

## 📱 Connect with Us
Stay updated or request custom high-volume enterprise services:

*   **Litagatoro Official:** [@litagatoro](https://x.com/litagatoro)
*   **Founder:** [@claradetermined](https://x.com/claradetermined)

---
*Litagatoro: Bridging the gap between silicon and soul.*
