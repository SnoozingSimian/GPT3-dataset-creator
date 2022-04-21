# Built ins
import sys
import argparse

# Local imports
from src.window import MainWindow

# Third party imports
from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple GUI tool to create OpenAI datasets.")

    parser.add_argument("data_dir", type=str, default="data" help="Path to store created dataset.")

    args = parser.parse_args()
    app = QApplication(sys.argv)

    window =  MainWindow()
    window.show()

    app.exec()