"""
Streamlit app for Super Mario Bros HTML5 Game
A fully playable Super Mario Bros game in the browser
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Super Mario Bros - Play Online",
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
    }
    .controls-info {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .game-info {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .feature-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

def load_html_game():
    """Load the HTML5 Super Mario Bros game"""
    try:
        with open('mario_game.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        try:
            with open('index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            return html_content
        except FileNotFoundError:
            st.error("Game file not found. Please ensure mario_game.html or index.html exists.")
            return None

def main():
    """Main Streamlit app"""
    # Header
    st.markdown('<h1 class="main-header">🍄 Super Mario Bros - Play Online 🍄</h1>', unsafe_allow_html=True)
    
    # Success message
    st.success("🎮 **Fully Playable Game**: This is a complete Super Mario Bros game that you can play directly in your browser!")
    
    # Sidebar with game info
    with st.sidebar:
        st.header("🎮 Game Information")
        st.markdown("""
        **Welcome to Super Mario Bros!**
        
        This is a fully playable HTML5 version featuring:
        - Classic Mario gameplay with jumping and running
        - Moving enemies (Goombas) to avoid or jump on
        - Collectible coins for points
        - Multiple platforms to jump on
        - Score system and lives
        - Level progression
        """)
        
        st.header("🎯 How to Play")
        st.markdown("""
        **Controls:**
        - ⬅️ **Left Arrow**: Move left
        - ➡️ **Right Arrow**: Move right  
        - ⬆️ **Space**: Jump
        - **Click Buttons**: Use the control buttons below the game
        
        **Objective:**
        - Collect all coins to advance to the next level
        - Avoid enemies or jump on them
        - Don't fall off the platforms!
        - Get the highest score possible
        """)
        
        st.header("🏆 Scoring System")
        st.markdown("""
        - **Collect Coin**: 100 points
        - **Complete Level**: 500 points
        - **Lives**: Start with 3 lives
        - **Game Over**: When all lives are lost
        """)
        
        st.header("🎮 Game Features")
        st.markdown("""
        - **Real-time Gameplay**: Smooth animations and physics
        - **Responsive Controls**: Keyboard and button controls
        - **Progressive Difficulty**: Multiple levels
        - **Classic Mario Elements**: Pipes, platforms, enemies
        - **No Downloads Required**: Play directly in browser
        """)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Load and display the HTML5 game
        html_content = load_html_game()
        if html_content:
            st.subheader("🎮 Play Super Mario Bros")
            
            # Display the game using components.iframe
            components.html(html_content, height=650, scrolling=True)
            
            st.markdown("""
            <div class="feature-box">
            <h4>🎯 Game Instructions</h4>
            <p><strong>Goal:</strong> Collect all coins while avoiding enemies to advance through levels!</p>
            <p><strong>Controls:</strong> Use arrow keys or the buttons below the game to control Mario.</p>
            <p><strong>Tip:</strong> Jump on enemies to defeat them, but be careful not to touch them from the side!</p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("Unable to load the game. Please check the file.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Game features section
    st.markdown("---")
    st.subheader("🌟 Game Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="game-info">
        <h4>🎮 Classic Gameplay</h4>
        <p>Experience the classic Super Mario Bros gameplay with modern web technology. Jump, run, and collect coins just like the original!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="game-info">
        <h4>🌐 Browser-Based</h4>
        <p>No downloads or installations required! Play directly in your browser on any device. Works on desktop, tablet, and mobile.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="game-info">
        <h4>🎯 Interactive Controls</h4>
        <p>Use keyboard arrow keys or click the control buttons. Responsive controls make the game easy to play for everyone.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Technical information
    st.markdown("---")
    st.subheader("🔧 Technical Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Built With:**
        - HTML5 Canvas
        - CSS3 Animations
        - JavaScript Game Logic
        - Streamlit Web Framework
        
        **Features:**
        - Real-time collision detection
        - Smooth animations
        - Responsive design
        - Cross-platform compatibility
        """)
    
    with col2:
        st.markdown("""
        **Game Elements:**
        - Mario character with physics
        - Moving enemies (Goombas)
        - Collectible coins
        - Multiple platforms
        - Pipes and obstacles
        - Score and lives system
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🍄 Super Mario Bros - HTML5 Version 🍄</p>
        <p>Play the classic game directly in your browser!</p>
        <p><strong>Controls:</strong> Arrow Keys or Click Buttons | <strong>Goal:</strong> Collect Coins & Avoid Enemies</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()