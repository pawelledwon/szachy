# ChessGame

ChessGame is a Python-based program that brings the classic game of chess to your computer. It provides the flexibility to play chess either offline against another player locally or online against other players through a Local Area Network (LAN). There is available only polish langugae in the game.

## Requirements

To use the program, ensure that you have the following installed on your computer:

- **Python** 
- **Tkinter** 
- **Pygame** 

## Installation

1. **Clone the repository**: Clone this repository to your local machine using the following command:
     git clone https://github.com/pawelledwon/szachy.git
2. **Install python**: Install python (version at least 3.8)
     https://www.python.org/downloads/
3. **Install dependencies**: Install the required dependencies using pip:\
     pip install pygame\
     pip install tk

## Usage

### Offline Mode

To play chess offline against another player locally, simply run the `chessgame.py` script:\
     python -m chessgame.py
     
### Online Mode (LAN)

To play chess online against other players through LAN, follow these steps:
1. **Launch game as if you wanted to play offline**
2. **Choose 'GRA ONLINE'**
3. **Choose if you want to be a host or to connect to other player**
4. **As a host you have to just press 'WYSLIJ' button and then 'Rozpocznij' button**
5. **As a connecting player you have to put the ip address of host and then press 'WYSLIJ' button and then 'Rozpocznij' button**
6. **Enjoy the game**

## Controls

**Mouse Interaction**: Use the mouse to interact with the chessboard. Click on a piece to select it, then click on the destination square to make a move.

## Contributing
Contributions to ChessGame are welcome! If you find any bugs or have suggestions for improvements, please submit an issue or a pull request. Your contributions will help make the game even better for everyone.

