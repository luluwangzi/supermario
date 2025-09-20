# 🍄 Super Mario Bros Online - Streamlit Edition

A fully playable Super Mario Bros game built with Construct 2 and deployed via Streamlit. Experience the classic NES game directly in your browser!

## 🎮 Play Online

**Streamlit Version**: Run `streamlit run streamlit_app.py` and open your browser to play!

**Direct HTML**: Open `index.html` in any modern web browser to play directly.

## 🚀 Quick Start

### Option 1: Streamlit Web App (Recommended)

1. **Install Streamlit:**
```bash
pip install streamlit
```

2. **Run the app:**
```bash
streamlit run streamlit_app.py
```

3. **Open your browser:**
   - Go to `http://localhost:8501`
   - Start playing immediately!

### Option 2: Direct HTML Play

1. **Open the game:**
   - Double-click `index.html`
   - Or drag it into your browser
   - Start playing instantly!

## 🎯 Game Features

### 🎮 Core Gameplay
- **Classic Mario Controls**: Arrow keys for movement, Up/Space to jump
- **Touch Controls**: Full mobile support with touch gestures
- **Real-time Physics**: Smooth jumping and movement with Construct 2 engine
- **Collision Detection**: Precise enemy and object interactions

### 🏆 Game Elements
- **Mario Character**: Classic red plumber with authentic animations
- **Classic Enemies**: Goombas, Koopas, and other familiar foes
- **Power-ups**: Mushrooms, Fire Flowers, and special items
- **Multiple Worlds**: Different themed levels to explore
- **Collectibles**: Coins, 1-Up mushrooms, and hidden secrets
- **Authentic Sound**: Original game audio and sound effects

### 🌟 Technical Features
- **Construct 2 Engine**: Professional game development platform
- **HTML5 Canvas**: Modern web technology for smooth gameplay
- **Service Workers**: Offline support and caching
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Cross-Platform**: Compatible with all modern browsers

## 🎮 How to Play

### Controls
- **⬅️ Left Arrow**: Move Mario left
- **➡️ Right Arrow**: Move Mario right
- **⬆️ Up Arrow**: Make Mario jump
- **Space**: Alternative jump button
- **Touch**: Tap and swipe on mobile devices

### Objective
1. **Navigate Levels**: Move through each level from left to right
2. **Collect Coins**: Gather coins for points and extra lives
3. **Defeat Enemies**: Jump on enemies or use power-ups
4. **Find Power-ups**: Collect mushrooms and fire flowers
5. **Reach the Flag**: Complete each level by reaching the flagpole
6. **Save Princess Peach**: Progress through all worlds to rescue the princess

### Scoring
- **Coin**: 200 points
- **Enemy Defeat**: 100-1000 points (varies by enemy)
- **Power-up**: Various bonuses
- **Level Complete**: 500 points
- **Lives**: Start with 3 lives, gain more with 1-Up mushrooms

## 🌐 Deployment Options

### Streamlit Cloud
1. Push to GitHub
2. Connect to [share.streamlit.io](https://share.streamlit.io)
3. Deploy automatically

### GitHub Pages
1. Push to GitHub
2. Enable GitHub Pages in repository settings
3. Access via `https://yourusername.github.io/supermario`

### Netlify/Vercel
1. Connect your GitHub repository
2. Deploy with one click
3. Get a live URL instantly

## 📁 Project Structure

```
supermario/
├── index.html              # 🎮 Main HTML5 game file
├── streamlit_app.py        # 🌐 Streamlit web interface
├── requirements.txt        # 📦 Python dependencies
├── README.md              # 📖 This file
├── file/                  # 🎮 Game files directory
│   ├── index.html         # 🎮 Construct 2 game
│   ├── c2runtime.js       # 🎮 Game engine
│   ├── data.js            # 🎮 Game data
│   ├── media/             # 🎵 Audio files
│   └── images/            # 🖼️ Game assets
├── css/                   # 🎨 Stylesheets
├── js/                    # 📜 JavaScript files
└── images/                # 🖼️ Website images
```

## 🛠️ Development

### Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/supermario.git
cd supermario

# Run Streamlit version
streamlit run streamlit_app.py

# Or open HTML directly
open index.html
```

### Customization
- **Game Speed**: Modify physics settings in Construct 2
- **Level Design**: Edit level layouts and enemy placement
- **Scoring**: Change point values in game data
- **Graphics**: Update sprites and animations
- **Audio**: Replace sound effects and music

## 🎨 Game Design

### Visual Elements
- **Mario**: Classic red plumber with authentic sprite animations
- **Enemies**: Faithful recreations of original NES enemies
- **Power-ups**: Mushrooms, Fire Flowers, and special items
- **Levels**: Multiple themed worlds with unique challenges
- **Backgrounds**: Classic Mario environments and scenery

### Audio Features
- **Jump Sound Effects**: Authentic Mario jump sounds
- **Coin Collection**: Classic coin pickup audio
- **Background Music**: Original Mario theme music
- **Power-up Sounds**: Special audio for power-ups
- **Enemy Defeat**: Sound effects for defeating enemies

## 🚀 Performance

- **Lightweight**: Optimized Construct 2 export
- **Fast Loading**: Efficient asset loading and caching
- **Smooth Gameplay**: 60 FPS animations and physics
- **Cross-Platform**: Works on all modern browsers
- **Mobile Optimized**: Touch controls and responsive design

## 📱 Browser Compatibility

- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS/Android)

## 🎉 Features vs Original

| Feature | Online Version | Original NES |
|---------|---------------|--------------|
| Play in Browser | ✅ | ❌ |
| No Installation | ✅ | ❌ |
| Cross-Platform | ✅ | ❌ |
| Touch Controls | ✅ | ❌ |
| Classic Gameplay | ✅ | ✅ |
| Multiple Worlds | ✅ | ✅ |
| Power-ups | ✅ | ✅ |
| Sound Effects | ✅ | ✅ |
| Offline Support | ✅ | ❌ |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

MIT License - Feel free to use and modify!

## 🎮 Have Fun!

Enjoy playing Super Mario Bros directly in your browser! This version captures the classic gameplay while being accessible to everyone, everywhere.

---

**🎮 Play Now**: Open `index.html` or run `streamlit run streamlit_app.py` to start playing immediately!
