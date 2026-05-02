# 🤖 FlowOps: Minimalist BlueSky Automation Bot

A professional, text-only automated broadcaster for BlueSky, powered by **Google Gemini 2.5 Flash** and **GitHub Actions**. This bot is designed for technical niches like Automation, Programming, and AI workflows.

> **Note:** This repository contains the **Lite Version** of our automation suite. It provides essential, text-only broadcasting features for free. For the full suite of engagement and AI image tools, see the [**SkyPulse AI**](https://github.com/ProcWire/Bluesky-Bot#-elevate-your-bluesky-brand-with-skypulse-ai) section below.

---

## 🚀 Elevate Your BlueSky Brand with SkyPulse AI
**The Most Sophisticated, Fully Automated AI Agent for BlueSky**

Tired of manual posting and low engagement? Meet **SkyPulse AI**—a high-performance, autonomous agent designed to build a professional, authoritative presence on BlueSky while you sleep. Unlike basic scripts, this bot uses a multi-model AI architecture to think, see, and interact like a human expert in **any** niche.

### ⚡ The "Superpowers" of SkyPulse AI:

| Feature | What it Does for You |
| :--- | :--- |
| **Multi-Model Intelligence** | Powered by **Gemini 3.1 Pro & Flash**. It doesn't just post; it generates high-quality, engaging, and context-aware content tailored to your voice. |
| **Autonomous Daily Posts** | Pulls from a custom topic pool of your choice (e.g., Marketing, Fitness, News, or Tech) to share high-value insights every day. |
| **AI-Generated Visuals** | Integrated with **Hugging Face (FLUX.1 & SDXL)** to generate stunning, relevant images for every post automatically. |
| **Smart Engagement** | Scans BlueSky for specific keywords to Like, Repost, Reply and Follow potential followers or community leaders in your industry. |
| **Deep Conversation Engine** | Handles notifications and replies in threads up to **15 levels deep**, keeping your audience engaged without you lifting a finger. |
| **Human-Centric Stealth** | Built-in "Stealth Breaks," random delays, and probability-based actions to mimic human behavior and keep your account safe. |
| **Auto-Facet Parsing** | Automatically detects and formats URLs and Hashtags, ensuring your posts look professional and are SEO-friendly. |

### 📊 Comparison: Lite vs. Pro

| Feature | FlowOps (Lite - This Repo) | SkyPulse AI (Premium) |
| :--- | :--- | :--- |
| **AI Model** | Gemini 2.5 Flash | **Gemini 3.1 Pro & Flash** |
| **Content Type** | Text Only | **Text + AI Generated Images** |
| **Engagement** | Post-Only | **Auto-Like, Follow & Repost** |
| **Replies** | Manual Only | **Autonomous Threading (15+ levels)** |
| **Stealth Logic** | Basic Delays | **Human-Like Probability Engine** |
| **Deployment** | GitHub Actions | **Cloud Hosting / Custom Deployment** |

### 📺 See it in Action (Live Demo)
Curious how it looks in the wild? Check out our official automation demo account to see the AI posting, replying, and generating images in real-time:
🔗 **View Demo Account:** [@autoflow](https://bsky.app/profile/autoflow.bsky.social)

### 💡 Ready to Automate Your Brand?
Whether you are a content creator, a business owner, or looking to build a personal brand, I can deploy and customize this agent for your specific goals.

**Contact me today to get started:**
* 📥 **Message me on Fiverr:** [Order Custom Setup](https://www.fiverr.com/s/vvqB8rz)
* 📩 **Direct Inquiries:** [kambetastephano@gmail.com](mailto:kambetastephano@gmail.com)

---

## 🛠️ Setup Guide (FlowOps Lite)

### 1. Fork the Repository
Click the **Fork** button at the top right of this page to create your own copy.

### 2. Configure Your Identity
Edit the `config.yaml` file to change the bot's name, persona, and topic pool to match your specific niche.

### 3. Add GitHub Secrets
Go to your repository **Settings > Secrets and variables > Actions** and add the following:

| Secret Name | Description |
| :--- | :--- |
| `BSKY_HANDLE` | Your BlueSky handle (e.g., `user.bsky.social`) |
| `BSKY_PASSWORD` | Your BlueSky App Password (not your main password!) |
| `GEMINI_API_KEY` | Your Google AI Studio API Key |

### 4. Enable GitHub Actions
Go to the **Actions** tab in your repository and click "I understand my workflows, go ahead and enable them."

## ⚙️ Configuration
The bot's logic is controlled via `config.yaml`. You can customize:
* **Persona:** How the AI speaks (Pragmatic, Academic, Witty).
* **Topic Pool:** The specific technical subjects the bot writes about.
* **Schedule:** Change the `.github/workflows/main.yml` cron timing to post more or less frequently.

## ⚖️ Disclaimer
This tool is for educational and professional sharing purposes. Please adhere to BlueSky's Community Guidelines and avoid generating spam. The author is not responsible for any account suspensions.

## 📜 License
MIT License - feel free to use and modify for your own projects!
