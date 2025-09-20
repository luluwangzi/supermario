"""
Streamlit app for Super Mario Bros Online Game
A fully playable Super Mario Bros game in the browser using Construct 2
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Super Mario Bros Online - Play Now",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #FF0000;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .game-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .controls-info {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #007bff;
    }
    .game-info {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
    }
    .feature-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #ffc107;
    }
    .warning-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #dc3545;
    }
</style>
""", unsafe_allow_html=True)

def load_html_game():
    """Load the HTML5 Super Mario Bros game"""
    try:
        with open('file/index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        st.error("Game file not found. Please ensure file/index.html exists.")
        return None

def main():
    """Main Streamlit app"""
    # Header
    st.markdown('<h1 class="main-header">🍄 Super Mario Bros Online 🍄</h1>', unsafe_allow_html=True)
    
    # Success message
    st.success("🎮 **Fully Playable Game**: This is a complete Super Mario Bros game built with Construct 2 that you can play directly in your browser!")
    
    # Sidebar with game info
    with st.sidebar:
        st.header("🎮 Game Information")
        st.markdown("""
        **Welcome to Super Mario Bros Online!**
        
        This is a fully playable HTML5 version featuring:
        - Classic Super Mario Bros gameplay
        - Multiple levels and worlds
        - Power-ups and collectibles
        - Enemies and obstacles
        - Authentic sound effects
        - Smooth animations
        """)
        
        st.header("🎯 How to Play")
        st.markdown("""
        **Controls:**
        - ⬅️ **Left Arrow**: Move left
        - ➡️ **Right Arrow**: Move right  
        - ⬆️ **Up Arrow**: Jump
        - **Space**: Jump (alternative)
        - **Touch Controls**: Available on mobile devices
        
        **Objective:**
        - Navigate through levels
        - Collect coins and power-ups
        - Defeat enemies
        - Reach the flag at the end of each level
        - Save Princess Peach!
        """)
        
        st.header("🏆 Game Features")
        st.markdown("""
        - **Authentic Gameplay**: Faithful recreation of the original
        - **Multiple Worlds**: Explore different themed levels
        - **Power-ups**: Mushrooms, Fire Flowers, and more
        - **Enemies**: Classic foes like Goombas and Koopas
        - **Sound Effects**: Original game audio
        - **Mobile Support**: Touch controls for mobile devices
        """)
        
        st.header("🔧 Technical Info")
        st.markdown("""
        **Built With:**
        - Construct 2 Engine
        - HTML5 Canvas
        - JavaScript
        - Web Audio API
        
        **Features:**
        - Offline support
        - Service Worker caching
        - Responsive design
        - Cross-platform compatibility
        """)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Load and display the HTML5 game
        html_content = load_html_game()
        if html_content:
            st.subheader("🎮 Play Super Mario Bros Online")
            
            # Display the game using components.iframe
            components.html(html_content, height=600, scrolling=True)
            
            st.markdown("""
            <div class="feature-box">
            <h4>🎯 Game Instructions</h4>
            <p><strong>Goal:</strong> Navigate through levels, collect coins, defeat enemies, and save Princess Peach!</p>
            <p><strong>Controls:</strong> Use arrow keys or touch controls to move and jump.</p>
            <p><strong>Tip:</strong> Collect power-ups to gain special abilities and extra lives!</p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("Unable to load the game. Please check the file structure.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Game features section
    st.markdown("---")
    st.subheader("🌟 Game Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="game-info">
        <h4>🎮 Classic Gameplay</h4>
        <p>Experience the authentic Super Mario Bros gameplay with modern web technology. Jump, run, and collect coins just like the original NES classic!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="game-info">
        <h4>🌐 Browser-Based</h4>
        <p>No downloads or installations required! Play directly in your browser on any device. Works on desktop, tablet, and mobile with touch controls.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="game-info">
        <h4>🎯 Multiple Levels</h4>
        <p>Explore multiple worlds with different themes, enemies, and challenges. Each level offers unique obstacles and secrets to discover!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Technical information
    st.markdown("---")
    st.subheader("🔧 Technical Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Built With:**
        - Construct 2 Game Engine
        - HTML5 Canvas
        - JavaScript Game Logic
        - Web Audio API
        - Service Workers
        
        **Features:**
        - Real-time physics engine
        - Smooth 60 FPS animations
        - Offline support
        - Mobile touch controls
        - Cross-platform compatibility
        """)
    
    with col2:
        st.markdown("""
        **Game Elements:**
        - Mario character with physics
        - Classic enemies (Goombas, Koopas)
        - Power-ups and collectibles
        - Multiple themed worlds
        - Authentic sound effects
        - Progressive difficulty
        """)
    
    # Browser compatibility
    st.markdown("---")
    st.subheader("🌐 Browser Compatibility")
    
    st.markdown("""
    <div class="controls-info">
    <h4>✅ Supported Browsers</h4>
    <p><strong>Desktop:</strong> Chrome, Firefox, Safari, Edge (latest versions)</p>
    <p><strong>Mobile:</strong> Chrome Mobile, Safari Mobile, Firefox Mobile</p>
    <p><strong>Requirements:</strong> HTML5 Canvas support, JavaScript enabled</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🍄 Super Mario Bros Online - Construct 2 Version 🍄</p>
        <p>Play the classic game directly in your browser!</p>
        <p><strong>Controls:</strong> Arrow Keys or Touch | <strong>Goal:</strong> Save Princess Peach!</p>
        <p><em>This is a fan-made recreation for educational purposes.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
