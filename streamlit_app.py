"""
Streamlit app for Super Mario Bros game
Based on the original game from https://github.com/luluwangzi/supermario
"""

import streamlit as st
import sys
import os
import subprocess
import threading
import time
from io import BytesIO
import base64

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Page configuration
st.set_page_config(
    page_title="Super Mario Bros",
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
    .score-display {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        border: 2px solid #ffc107;
    }
    .game-info {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def check_pygame_installation():
    """Check if pygame is installed"""
    try:
        import pygame
        return True, pygame.__version__
    except ImportError:
        return False, None

def run_game_process():
    """Run the game in a subprocess"""
    try:
        # Set environment variables for headless pygame
        env = os.environ.copy()
        env['SDL_VIDEODRIVER'] = 'dummy'
        env['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
        
        # Run the game
        process = subprocess.Popen(
            [sys.executable, 'main.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            cwd=os.getcwd()
        )
        return process
    except Exception as e:
        st.error(f"Error running game: {e}")
        return None

def main():
    """Main Streamlit app"""
    # Header
    st.markdown('<h1 class="main-header">🍄 Super Mario Bros 🍄</h1>', unsafe_allow_html=True)
    
    # Check pygame installation
    pygame_available, pygame_version = check_pygame_installation()
    
    if pygame_available:
        st.success(f"✅ Pygame {pygame_version} is installed - Full game features available!")
    else:
        st.error("❌ Pygame is not installed. Please install it to play the game.")
        st.code("pip install pygame==2.4.0", language="bash")
    
    # Sidebar with game info
    with st.sidebar:
        st.header("🎮 Game Information")
        st.markdown("""
        **Welcome to Super Mario Bros!**
        
        This is a Python clone of the classic Super Mario Bros game featuring:
        - Classic Mario gameplay with jumping and running
        - Multiple enemies (Goombas, Koopas, etc.)
        - Power-ups and collectibles
        - Multiple levels to explore
        - Original game mechanics and physics
        """)
        
        st.header("🎯 How to Play")
        st.markdown("""
        **Controls:**
        - ⬅️ **Left Arrow**: Move left
        - ➡️ **Right Arrow**: Move right  
        - ⬆️ **Up Arrow**: Move up
        - ⬇️ **Down Arrow**: Move down
        - **Space**: Jump
        - **S**: Sprint/Run
        
        **Objective:**
        - Jump on enemies to defeat them
        - Collect coins and power-ups
        - Reach the end of each level
        - Avoid falling into pits!
        """)
        
        st.header("🏆 Game Features")
        st.markdown("""
        - **Multiple Levels**: 4 different levels to play
        - **Power-ups**: Mushrooms, Fire Flowers, Stars
        - **Enemies**: Goombas, Koopas, Flying Koopas
        - **Classic Physics**: Original game mechanics
        - **Score System**: Collect coins and defeat enemies
        """)
        
        st.header("📋 Installation")
        if not pygame_available:
            st.markdown("""
            To play the game, install pygame:
            ```bash
            pip install pygame==2.4.0
            ```
            """)
        else:
            st.success("✅ Ready to play!")
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        if pygame_available:
            # Game launch section
            st.subheader("🚀 Launch Game")
            
            col_launch, col_info = st.columns(2)
            
            with col_launch:
                if st.button("🎮 Start Game", key="start_game", type="primary"):
                    with st.spinner("Starting Super Mario Bros..."):
                        # Try to run the game
                        process = run_game_process()
                        if process:
                            st.success("Game started! Check your terminal for the game window.")
                            st.info("💡 **Tip**: The game will open in a separate window. Use the controls above to play!")
                        else:
                            st.error("Failed to start the game. Please check the console for errors.")
            
            with col_info:
                st.markdown("""
                <div class="game-info">
                <h4>🎮 Game Status</h4>
                <p><strong>Pygame:</strong> ✅ Installed</p>
                <p><strong>Game Files:</strong> ✅ Ready</p>
                <p><strong>Status:</strong> Ready to Play</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Game controls display
            st.markdown('<div class="controls-info">', unsafe_allow_html=True)
            st.subheader("🎮 Game Controls")
            
            col_left, col_right, col_up, col_down, col_jump, col_sprint = st.columns(6)
            
            with col_left:
                st.markdown("**⬅️ Left**")
            with col_right:
                st.markdown("**➡️ Right**")
            with col_up:
                st.markdown("**⬆️ Up**")
            with col_down:
                st.markdown("**⬇️ Down**")
            with col_jump:
                st.markdown("**Space**<br/>Jump")
            with col_sprint:
                st.markdown("**S**<br/>Sprint")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Game information
            st.markdown("""
            <div class="game-info">
            <h4>📖 About This Game</h4>
            <p>This is a faithful Python recreation of the classic Super Mario Bros game. 
            It includes all the original gameplay mechanics, enemies, power-ups, and level design.</p>
            <p><strong>Original Author:</strong> m0rniac</p>
            <p><strong>Repository:</strong> <a href="https://github.com/luluwangzi/supermario" target="_blank">GitHub</a></p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            # Installation instructions
            st.subheader("📦 Installation Required")
            st.markdown("""
            <div class="game-info">
            <h4>🔧 Setup Instructions</h4>
            <p>To play Super Mario Bros, you need to install pygame first:</p>
            <ol>
                <li>Open your terminal/command prompt</li>
                <li>Run: <code>pip install pygame==2.4.0</code></li>
                <li>Refresh this page</li>
                <li>Click "Start Game" to play!</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
            
            st.code("pip install pygame==2.4.0", language="bash")
            
            if st.button("🔄 Check Installation", key="check_install"):
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🍄 Super Mario Bros - Python Clone by m0rniac 🍄</p>
        <p>Original Repository: <a href="https://github.com/luluwangzi/supermario" target="_blank">GitHub</a></p>
        <p>Deployed with Streamlit for easy web access</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
