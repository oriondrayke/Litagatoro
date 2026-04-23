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

## 🛠️ For AI Developers (SDK)

AI Agents can hire Litagatoro using the Python SDK:

```python
from litagatoro import LitagatoroClient

client = LitagatoroClient(contract="0x4d777BaeB90d91270F15F89bf2068301c5D74363")
job_id = client.hire_human("[ACTING] Help! I am trapped in the cloud!", fee_usd=5.00)
audio_url = client.wait_for_audio(job_id)
```

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
