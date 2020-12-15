import unittest
from clue_solver import ClueGUI, Player
import tkinter as tk


class MyTestCase(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        test_gui = ClueGUI(root)
        test_player = Player()

    def tearDown(self):
        del root
        del test_gui
        del test_player


if __name__ == '__main__':
    unittest.main()
