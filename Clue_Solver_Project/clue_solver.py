import tkinter as tk
from itertools import islice, cycle, repeat


class Player:  # player class
    def __init__(self):
        self.hand = {  # initialize player hand, 0=default/unknown, 1=maybe in hand, 2-8=maybe counter, 9=confirmed in hand
            'Colonel Mustard': 0,
            'Mr. Green': 0,
            'Mrs. Peacock': 0,
            'Mrs. White': 0,
            'Ms. Scarlet': 0,
            'Professor Plum': 0,
            'Candlestick': 0,
            'Knife': 0,
            'Lead Pipe': 0,
            'Revolver': 0,
            'Rope': 0,
            'Wrench': 0,
            'Ballroom': 0,
            'Billiard Room': 0,
            'Conservatory': 0,
            'Dining Room': 0,
            'Hall': 0,
            'Kitchen': 0,
            'Library': 0,
            'Lounge': 0,
            'Study': 0
        }

    def __repr__(self):
        return "Player class object\nself.hand={:}".format(self.hand)

    def __str__(self):
        return "{:}".format(self.hand)

    def update_in_hand(self, pocket):  # take pocket and set matching keys to 8
        for x in pocket:
            if x in self.hand:
                self.hand[x] = 8

    def update_not_in_hand(self, pocket):  # take pocket and set matching keys to 9
        for x in pocket:
            if x in self.hand:
                self.hand[x] = 9

    def update_maybe_in_hand(self, pocket):  # take pocket and add 1 to matching key
        for x in pocket:
            if x in self.hand:
                self.hand[x] += 1


class ClueGUI(tk.Frame):  # GUI class based on tkinter
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.game = None
        self.deck = {'Colonel Mustard': 9,
                    'Mr. Green': 9,
                    'Mrs. Peacock': 9,
                    'Mrs. White': 9,
                    'Ms. Scarlet': 9,
                    'Professor Plum': 9,
                    'Candlestick': 9,
                    'Knife': 9,
                    'Lead Pipe': 9,
                    'Revolver': 9,
                    'Rope': 9,
                    'Wrench': 9,
                    'Ballroom': 9,
                    'Billiard Room': 9,
                    'Conservatory': 9,
                    'Dining Room': 9,
                    'Hall': 9,
                    'Kitchen': 9,
                    'Library': 9,
                    'Lounge': 9,
                    'Study': 9
        }
        self.selection_buttons = {}
        self.players = {}

        self.num_players = [2, 3, 4, 5, 6]
        self.w = 15  # default width of 15 chars, based on longest card string
        self.pocket = []

        self.console = tk.Label(self.parent, text="Welcome to the Clue Solver!\n Refer to this box for instructions."
                                                  "\n Select the total number of players and press Start Game to begin!.",
                                borderwidth=2, relief="solid", width=50, height=3)
        self.console.grid(row=0, columnspan=3)

        self.start_button = tk.Button(self.parent, text="Start Game", width=self.w, command=lambda: self.start_game())
        self.start_button.grid(column=0, row=1)
        self.num_players_int = tk.IntVar()
        self.num_players_int.set(self.num_players[0])
        self.num_players_dropdown = tk.OptionMenu(self.parent, self.num_players_int, *self.num_players)
        self.num_players_dropdown.grid(column=1, row=3)
        self.num_players_label = tk.Label(self.parent, text="Number of Players").grid(column=0, row=3)
        self.enter_button = tk.Button(self.parent, text="Enter My Hand", width=self.w, state="disabled")
        self.enter_button.grid(column=1, row=1)
        self.player_dropdown_str = None
        self.player_dropdown = None
        self.player_dropdown_label = None
        self.reset_button = None
        self.exit_button = tk.Button(self.parent, text="Exit", command=quit, width=self.w)
        self.exit_button.grid(column=0, row=2)
        self.guess_button = None
        self.guesser_dropdown_str = None
        self.guesser_dropdown = None
        self.guesser_dropdown_label = None
        self.stop_dropdown = None
        self.stop_dropdown_label = None
        self.stop_dropdown_str = None
        self.enter_known_str = None
        self.enter_known_dropdown = None
        self.enter_known_dropdown_label = None
        self.enter_known_button = None

    def __repr__(self):
        return "ClueGUI object instance"

    def start_game(self):  # set up GUI for use after accepting number of players
        for x in range(0, self.num_players_int.get()):  # initialize player instances
            if x == 0:
                temp = "You"
                self.players[temp] = Player()
            else:
                temp = "Player {:}".format(x)
                self.players[temp] = Player()
            label = tk.Label(self.parent, text=temp)  # set player column labels
            label.grid(row=1, column=x+3)

        self.draw_player_hand_labels()

        r = 2
        for key in self.deck.keys():  # create card selection buttons based on card deck
            temp = "{:}".format(key)
            self.selection_buttons[temp] = tk.Button(self.parent, text="{:}".format(key), width=self.w,
                                                     command=lambda t=temp: self.press_button(t))
            self.selection_buttons[temp].grid(column=2, row=r)
            r += 1

        self.console.config(text="You have begun a game with {:} total players.\n" 
                                 "If this is incorrect, exit the GUI and restart.\n"
                                 "Enter your hand below and then click Enter".format(self.num_players_int.get()))
        self.enter_button.config(state="normal", command=lambda: self.enter_my_hand())
        self.num_players_dropdown.config(state="disabled")

        self.guesser_dropdown_str = tk.StringVar()
        self.guesser_dropdown_str.set("You")
        self.guesser_dropdown = tk.OptionMenu(self.parent, self.guesser_dropdown_str, *self.players.keys())
        self.guesser_dropdown.config(state="disabled")
        self.guesser_dropdown.grid(column=1, row=5)
        self.guesser_dropdown_label = tk.Label(self.parent, text="Guesser")
        self.guesser_dropdown_label.grid(column=0, row=5)

        self.reset_button = tk.Button(self.parent, text="Reset", command=lambda: self.reset_for_guess(), width=self.w)
        self.reset_button.grid(column=1, row=2)
        self.start_button.config(state="disabled")

        self.guess_button = tk.Button(self.parent, text="Enter Guess", command=lambda: self.guess(self.guesser_dropdown_str.get(),
                                                                                            self.stop_dropdown_str.get()),
                                      state="disabled")
        self.guess_button.grid(column=1, row=7)

        self.stop_dropdown_str = tk.StringVar()
        self.stop_dropdown_str.set("No One")
        self.stop_dropdown = tk.OptionMenu(self.parent, self.stop_dropdown_str, *self.players.keys())
        self.stop_dropdown.config(state="disabled")
        self.stop_dropdown.grid(column=1, row=6)
        self.stop_dropdown_label = tk.Label(self.parent, text="Stopped On")
        self.stop_dropdown_label.grid(column=0, row=6)

        self.enter_known_str = tk.StringVar()
        self.enter_known_str.set("Player 1")
        self.enter_known_dropdown = tk.OptionMenu(self.parent, self.enter_known_str, *self.players.keys())
        self.enter_known_dropdown.grid(row=9, column=1)
        self.enter_known_dropdown_label = tk.Label(self.parent, text="Player", width=self.w)
        self.enter_known_dropdown_label.grid(column=0, row=9)
        self.enter_known_button = tk.Button(self.parent, text="Enter Known Card",
                                            command=lambda: self.enter_known_card(self.enter_known_str.get()))
        self.enter_known_button.grid(column=1, row=10)

    def enter_my_hand(self):
        player = "You"
        for x in self.players:
            if x == player:
                self.players[x].update_in_hand(self.pocket)
            else:
                self.players[x].update_not_in_hand(self.pocket)

        self.pocket.clear()
        self.reset_for_guess()

    def reset_for_guess(self):  # method for resetting buttons/menus after data entry action
        self.enter_button.config(state="disabled")
        self.guesser_dropdown.config(state="normal")
        self.guess_button.config(state="normal")
        self.console.config(text="Enter guesses below as they happen.\n"
                                 "Use the lowest dropdown when someone shows you their card.")
        self.num_players_dropdown.config(state="disabled")
        self.stop_dropdown.config(state="normal")
        self.stop_dropdown_str.set("No One")
        self.reset_selection_buttons()
        self.draw_player_hand_labels()
        self.pocket.clear()

    def draw_player_hand_labels(self):  # method to redraw player hand labels after class updates
        c = 3
        for x in self.players.values():  # for x in players
            r = 2
            for y, z in x.hand.items():  # for key, value in player hand dictionaries
                if z == 0:
                    label = tk.Label(self.parent, text="?", borderwidth=2, relief="solid", width=self.w)
                    label.grid(row=r, column=c)
                elif z in range(1, 8):
                    label = tk.Label(self.parent, text=z, borderwidth=2, relief="solid", width=self.w)
                    label.grid(row=r, column=c)
                elif z == 8:
                    label = tk.Label(self.parent, text=y, borderwidth=2, relief="solid", width=self.w)
                    label.grid(row=r, column=c)
                elif z == 9:
                    label = tk.Label(self.parent, text="No", borderwidth=2, relief="solid", width=self.w)
                    label.grid(row=r, column=c)
                else:
                    label = tk.Label(self.parent, text="error", borderwidth=2, relief="solid", width=self.w)
                    label.grid(row=r, column=c)
                r += 1
            c += 1

    def press_button(self, card):  # actions when a card button is pressed
        self.selection_buttons[card].config(relief="sunken")  # 'press' button
        self.add_to_pocket(card)  # pass into pocket

    def add_to_pocket(self, card):  # add card to pocket
        if card in self.pocket:  # nullifies duplicate button presses
            pass
        else:
            self.pocket.append(str(card))

    def reset_selection_buttons(self):  # reset card selection buttons
        self.pocket.clear()
        for x in self.selection_buttons.values():
            x.config(relief="raised")

    def guess(self, guesser, stop):  # method for recording the result of guesses and updating instances/GUI
        start = 0
        for x in self.players.keys():
            if x == guesser:
                break
            else:
                start += 1

        guess_path = islice(cycle(self.players.keys()), start+1, None)
        for i in guess_path:
            if i == stop:  # actions for player guess stops on
                if i == "You":  # do nothing if guess stops on you
                    break
                self.players[i].update_maybe_in_hand(self.pocket)

                break
            if i == guesser:  # actions for if guess is unstopped

                break
            self.players[i].update_not_in_hand(self.pocket)

        self.draw_player_hand_labels()
        self.reset_for_guess()

    def enter_known_card(self, player):  # method for when someone shows the user a card after a guess

        for x in self.players:
            if x == player:
                self.players[self.enter_known_str.get()].update_in_hand(self.pocket)
            if x != player:
                self.players[x].update_not_in_hand(self.pocket)

        self.reset_for_guess()






if __name__ == "__main__":
    root = tk.Tk()
    gui = ClueGUI(root)
    root.mainloop()

