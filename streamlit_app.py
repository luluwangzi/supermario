"""
Streamlit app for Super Mario Bros game
Based on the original game from https://github.com/luluwangzi/supermario
"""

import streamlit as st
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
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

def create_game_simulation():
    """Create a visual simulation of the Super Mario Bros game"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    
    # Draw ground
    ground = patches.Rectangle((0, 0), 20, 1, linewidth=1, edgecolor='brown', facecolor='#8B4513')
    ax.add_patch(ground)
    
    # Draw platforms
    platform1 = patches.Rectangle((3, 3), 2, 0.5, linewidth=1, edgecolor='brown', facecolor='#8B4513')
    platform2 = patches.Rectangle((8, 4), 2, 0.5, linewidth=1, edgecolor='brown', facecolor='#8B4513')
    platform3 = patches.Rectangle((13, 2), 2, 0.5, linewidth=1, edgecolor='brown', facecolor='#8B4513')
    platform4 = patches.Rectangle((16, 5), 2, 0.5, linewidth=1, edgecolor='brown', facecolor='#8B4513')
    ax.add_patch(platform1)
    ax.add_patch(platform2)
    ax.add_patch(platform3)
    ax.add_patch(platform4)
    
    # Draw Mario (red circle with hat)
    mario_body = patches.Circle((2, 1.5), 0.3, color='red')
    mario_hat = patches.Rectangle((1.7, 1.7), 0.6, 0.2, color='red')
    ax.add_patch(mario_body)
    ax.add_patch(mario_hat)
    
    # Draw enemies (brown circles)
    goomba1 = patches.Circle((6, 1.5), 0.2, color='brown')
    goomba2 = patches.Circle((11, 1.5), 0.2, color='brown')
    goomba3 = patches.Circle((15, 1.5), 0.2, color='brown')
    ax.add_patch(goomba1)
    ax.add_patch(goomba2)
    ax.add_patch(goomba3)
    
    # Draw coins (yellow circles)
    coin1 = patches.Circle((4, 3.5), 0.15, color='yellow')
    coin2 = patches.Circle((9, 4.5), 0.15, color='yellow')
    coin3 = patches.Circle((14, 2.5), 0.15, color='yellow')
    coin4 = patches.Circle((17, 5.5), 0.15, color='yellow')
    ax.add_patch(coin1)
    ax.add_patch(coin2)
    ax.add_patch(coin3)
    ax.add_patch(coin4)
    
    # Draw pipes (green rectangles)
    pipe1 = patches.Rectangle((7, 1), 1, 3, color='green')
    pipe2 = patches.Rectangle((18, 1), 1, 4, color='green')
    ax.add_patch(pipe1)
    ax.add_patch(pipe2)
    
    # Draw flagpole
    flagpole = patches.Rectangle((19.5, 1), 0.1, 6, color='gray')
    flag = patches.Polygon([(19.5, 7), (20, 7), (20, 6.5), (19.5, 6.5)], color='red')
    ax.add_patch(flagpole)
    ax.add_patch(flag)
    
    # Add labels
    ax.text(2, 0.5, 'Mario', ha='center', fontsize=8, fontweight='bold')
    ax.text(6, 0.5, 'Goomba', ha='center', fontsize=8)
    ax.text(11, 0.5, 'Goomba', ha='center', fontsize=8)
    ax.text(15, 0.5, 'Goomba', ha='center', fontsize=8)
    ax.text(4, 2.5, 'Coin', ha='center', fontsize=8)
    ax.text(9, 3.5, 'Coin', ha='center', fontsize=8)
    ax.text(14, 1.5, 'Coin', ha='center', fontsize=8)
    ax.text(17, 4.5, 'Coin', ha='center', fontsize=8)
    ax.text(7.5, 4.5, 'Pipe', ha='center', fontsize=8)
    ax.text(18.5, 5.5, 'Pipe', ha='center', fontsize=8)
    ax.text(19.5, 8, 'Flag', ha='center', fontsize=8, fontweight='bold')
    
    ax.set_title("Super Mario Bros - Level 1 Simulation", fontsize=16, fontweight='bold')
    ax.set_xlabel("Move with arrow keys or buttons below!")
    ax.set_facecolor('#87CEEB')  # Sky blue
    ax.grid(True, alpha=0.3)
    
    # Remove axis ticks for cleaner look
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig

def download_game_files():
    """Create download links for the game files"""
    st.markdown("### 📥 Download Game Files")
    st.markdown("""
    To play the full Super Mario Bros game on your local machine:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Option 1: Clone from GitHub**
        ```bash
        git clone https://github.com/luluwangzi/supermario.git
        cd supermario
        pip install pygame==2.4.0
        python main.py
        ```
        """)
    
    with col2:
        st.markdown("""
        **Option 2: Direct Download**
        - Download the repository as ZIP
        - Extract and install pygame
        - Run the game locally
        """)
    
    st.markdown("""
    **System Requirements:**
    - Python 3.7+
    - pygame 2.4.0
    - SDL2 libraries (for pygame compilation)
    """)

def main():
    """Main Streamlit app"""
    # Header
    st.markdown('<h1 class="main-header">🍄 Super Mario Bros 🍄</h1>', unsafe_allow_html=True)
    
    # Show web version info
    st.info("🌐 **Web Version**: This is a browser-based simulation of Super Mario Bros. For the full game experience, download and run locally!")
    
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
        
        st.header("📋 Local Installation")
        st.markdown("""
        To play the full game locally:
        ```bash
        git clone https://github.com/luluwangzi/supermario.git
        cd supermario
        pip install pygame==2.4.0
        python main.py
        ```
        """)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Game simulation section
        st.subheader("🎮 Game Simulation")
        
        # Create and display game simulation
        fig = create_game_simulation()
        st.pyplot(fig)
        
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
        
        # Interactive buttons
        st.subheader("🎯 Interactive Demo")
        col_move, col_action = st.columns(2)
        
        with col_move:
            if st.button("⬅️ Move Left", key="move_left"):
                st.success("Mario moved left!")
            if st.button("➡️ Move Right", key="move_right"):
                st.success("Mario moved right!")
        
        with col_action:
            if st.button("⬆️ Jump", key="jump"):
                st.success("Mario jumped!")
            if st.button("🏃 Sprint", key="sprint"):
                st.success("Mario is sprinting!")
        
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
        
        # Download section
        download_game_files()
        
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
