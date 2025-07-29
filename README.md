# 🎭 DiscoMaster7 (ディスコマスター7) 🎶

<div align="center">

![DiscoMaster7 Banner](https://images.unsplash.com/photo-1576525865260-9f0e7cfb02b3?auto=format&fit=crop&w=800&q=80)

![License](https://img.shields.io/badge/license-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![discord.py](https://img.shields.io/badge/discord.py-2.3.2-7289DA?style=for-the-badge&logo=discord&logoColor=white)

*ディスコの魂を持つボット！* (A Bot with the Soul of Disco!)

</div>

---

## 🌟 特徴 (Features)

Our bot embodies the essence of Japanese disco culture with these groovy features:

- **音楽** (Music)
  - Sing Module for dropping those beats
  - High-quality music streaming
  - Queue management and playlist support

- **会話** (Communication)
  - Talk Module for voice interactions
  - Natural conversation flow
  - Multi-channel support

- **パーティー** (Party)
  - `/dm7` command for instant party mode
  - Real-time voice effects
  - Interactive DJ features

## 🚀 クイックスタート (Quick Start)

### Installation from Source

1. Clone the repository
```bash
git clone https://github.com/debaditya99/DiscoMaster7.git
cd DiscoMaster7
```

2. Create and activate virtual environment
```bash
python -m venv .venv
# For Windows
.\.venv\Scripts\activate
# For Unix/MacOS
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the bot
```bash
# Create .env file and add your Discord token
echo "DISCORD_TOKEN=your_bot_token_here" > .env
```

5. Start the party!
```bash
python bot.py
```

## 💫 使用方法 (Usage)

### Basic Operations

1. **Bot Setup**
   - Invite the bot to your server
   - Configure permissions
   - Use `/dm7` to verify connection

2. **Music Commands**
   - `/play` - Start the music
   - `/queue` - Manage playlist
   - `/skip` - Next track
   - `/stop` - Stop the party (but why would you?)

3. **Voice Features**
   - `/join` - Bot joins your channel
   - `/leave` - Bot leaves channel
   - `/effect` - Apply voice effects

## 🎯 プロジェクト構造 (Project Structure)

```
DiscoMaster7/
├── bot.py              # Main bot entry
├── features/
│   ├── Talk/          # Voice interaction module
│   │   └── Talk.py    # Voice commands implementation
│   └── Sing/          # Music module
│       └── Sing.py    # Music playback handling
├── requirements.txt    # Project dependencies
└── .env               # Configuration file
```

## � 技術詳細 (Technical Details)

### Dependencies

- **discord.py**: Discord API wrapper (v2.3.2)
- **python-dotenv**: Environment management
- **FFmpeg**: Audio processing
- **PyNaCl**: Voice support

### Key Components

- **DiscoMaster7Bot**: Main bot class with event handling
- **Talk Module**: Voice channel management
- **Sing Module**: Music playback and queue system
- **Command Tree**: Slash command implementation

## 🎨 設計哲学 (Design Philosophy)

Our bot embraces the spirit of Japanese disco:

- Energetic and engaging interactions
- Seamless music integration
- Community-focused features
- Reliable performance

## 🌈 開発予定 (Coming Soon...)

- 🎶 Advanced playlist management
- 🎤 Custom voice effect filters
- 🎮 Interactive DJ commands
- 🎭 Event notifications with style
- 🌟 Multi-language support

## 🤝 コントリビューション (Contributing)

Let's make this disco party even better! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 ライセンス (License)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with 💖 and 🎶 by Debaditya M.

*Keep the disco spirit alive!* ✨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>
