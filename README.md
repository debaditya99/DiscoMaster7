# 🎭 DiscoMaster7 (ディスコマスター7) 🎶

![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

> *踊れ、歌え、楽しめ！* (Dance, Sing, Enjoy!)

A groovy Discord bot that brings the vibes of a Japanese disco to your server! ✨

## 🌟 特徴 (Features)

Currently featuring these disco-tastic modules:

### 🎤 Talk Module (トークモジュール)
```
Bring the party to life with voice interactions!
Located in: features/Talk/Talk.py
```

### 🎵 Sing Module (シングモジュール)
```
Drop the beat with music capabilities!
Located in: features/Sing/Sing.py
```

### 🤖 Core Commands
- `/dm7` - Check if DiscoMaster7 is ready to party! 

## 🎪 セットアップ (Setup)

### 1️⃣ Environmental Preparation
```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # For Windows
```

### 2️⃣ Configuration
Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_bot_token_here
```

### 3️⃣ Dependencies
```bash
pip install discord.py python-dotenv
```

### 4️⃣ Start the Party!
```bash
python bot.py
```

## 🎨 モジュラー設計 (Modular Design)

DiscoMaster7 features a plug-and-play modular system:

```
features/
├── Talk/           # Voice interaction module
└── Sing/           # Music playback module
```

## 🎯 新機能の追加 (Adding New Features)

1. Create a new directory in `features/`
2. Add your module files
3. Implement `setup()` function
4. The bot automatically loads your groovy new feature! ✨

## 🔐 パーミッション (Permissions)

DiscoMaster7 adapts to the permissions granted in your server. Grant only what you need!

## 🌈 Coming Soon... 

- 🎶 Music playlist management
- 🎤 Voice effect filters
- 🎮 Interactive DJ commands
- 🎭 Custom event notifications

## 🌟 Contributing

Feel free to join the party! PRs welcome! 

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

🎶 Made with love by your neighborhood disco enthusiasts 🎶

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>
