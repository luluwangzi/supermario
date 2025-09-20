# 🍄 Super Mario Bros - Streamlit Web Version

This is a web-enabled version of the classic Super Mario Bros Python clone, now accessible through Streamlit for easy deployment and play.

## 🎮 Original Game

Based on the original Super Mario Bros Python clone by [m0rniac](https://github.com/m0rniac/supermario), this version adds Streamlit web interface for easy access and deployment.

**Original Repository**: [https://github.com/luluwangzi/supermario](https://github.com/luluwangzi/supermario)

## 🚀 Quick Start

### Option 1: Run with Streamlit (Recommended)

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the Streamlit app:**
```bash
streamlit run streamlit_app.py
```

3. **Open your browser:**
   - Go to `http://localhost:8501`
   - Click "Start Game" to launch Super Mario Bros

### Option 2: Run Original Game

1. **Install pygame:**
```bash
pip install pygame==2.4.0
```

2. **Run the original game:**
```bash
python main.py
```

## 🎯 Game Features

- **Classic Mario Gameplay**: Jump, run, and defeat enemies
- **Multiple Levels**: 4 different levels to explore
- **Power-ups**: Mushrooms, Fire Flowers, Stars
- **Enemies**: Goombas, Koopas, Flying Koopas, Piranhas
- **Original Physics**: Faithful recreation of classic mechanics
- **Score System**: Collect coins and defeat enemies

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| Space | Jump |
| S | Sprint/Run |

## 🌐 Web Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub:**
```bash
git add .
git commit -m "Add Streamlit web interface"
git push origin main
```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Deploy!

### Deploy to Heroku

1. **Create Heroku app:**
```bash
heroku create your-supermario-app
```

2. **Deploy:**
```bash
git push heroku main
```

## 📁 Project Structure

```
supermario/
├── streamlit_app.py          # Streamlit web interface
├── main.py                   # Original game entry point
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku deployment config
├── .streamlit/config.toml    # Streamlit configuration
├── README_STREAMLIT.md       # This file
├── source/                   # Original game source code
│   ├── main.py              # Game engine
│   ├── constants.py         # Game constants
│   ├── components/          # Game components
│   ├── states/              # Game states
│   └── data/                # Game data and maps
├── images/                   # Game images
└── resources/                # Game resources
```

## 🛠️ Development

### Adding New Features

1. **Game Logic**: Modify files in `source/` directory
2. **Web Interface**: Update `streamlit_app.py`
3. **Dependencies**: Update `requirements.txt`

### Testing

1. **Test Streamlit app:**
```bash
streamlit run streamlit_app.py
```

2. **Test original game:**
```bash
python main.py
```

## 📋 Requirements

- Python 3.7+
- pygame 2.4.0
- streamlit 1.28.0+

## 🎉 Features Added for Web Version

- **Web Interface**: Easy-to-use Streamlit interface
- **Installation Check**: Automatic pygame installation detection
- **Game Launch**: One-click game launching
- **Controls Guide**: Built-in controls reference
- **Deployment Ready**: Ready for Streamlit Cloud and Heroku
- **Responsive Design**: Works on desktop and mobile

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🎮 Have Fun!

Enjoy playing Super Mario Bros in your browser! The game maintains all the original gameplay mechanics while providing an easy web interface for access and deployment.

---

**Original Game**: [m0rniac/supermario](https://github.com/m0rniac/supermario)  
**Web Version**: Enhanced with Streamlit for easy deployment and access
