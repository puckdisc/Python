class Player:
    def __init__(self):
        self.hand = {  # initialize player hand, 0=default/unknown, 1=not in hand, 2=maybe in hand, 3=confirmed in hand
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
        self.not_in_hand = None
        self.might_have = None

    def update_in_hand(self, pocket):
        for x in pocket:
            if x in self.hand:
                self.hand[x] = 8


    def update_not_in_hand(self, pocket):
        for x in pocket:
            if x in self.hand:
                self.hand[x] = 9

    def update_maybe_in_hand(self, pocket):
        for x in pocket:
            if x in self.hand:
                self.hand[x] += 1
