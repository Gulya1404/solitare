class CardweeperCell:
    # Possible state of game cards:
    # Closed-закрытая
    # Opened-открытая
    # Completed-завершенная
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.state = 'closed'
        self.card = False
        self.counter = 0

    CardMoves = ['closed', 'opened', 'completed']

    def nextcard(self):
        if self.state in self.CardMoves:
            stateIndex = [self.CardMoves.index(self.state)]

            self.state= self.CardMoves [(stateIndex+1)] % len (self.CardMoves)
    def open (self):
        if self.state != 'Completed':
            self.state = 'Opened'

import random


class CardweeperModel:
    def __init__(self):
        self.list = ['в™*', 'в™Ј', 'в™Ґ', 'в™¦']
        self.cards = []
        self.cart = []
        for card_num in range(0, 52):
            r = str(card_num % 13)
            if r == '0':
                r = 'K'
            if r == '1':
                r = 'A'
            if r == '12':
                r = 'Q'
            if r == '11':
                r = 'J'
            index = int((card_num / 13) % 13)
            self.cards.append((r, self.list[index]))

    def draw(self):
        next = self.cards.pop(random.randint(0, len(self.cards) - 1))
        return next

    def deck(self):
        c = CardweeperModel()
        for i in range(0, 52):
            self.cards.append(c.draw())


        def show (self,c):
            for c in self.cart:
              c=(30 * ' ', self.cart[0])
              c=(25 * ' ', self.cart[1:3])
              c=(20 * ' ', self.cart[4:7])
              c=(15 * ' ', self.cart[7:11])
              c=(10 * ' ', self.cart[11:16])
              c=(5 * ' ', self.cart[16:22])
              c=(self.cart[23:30])
              c=(30 *'')



c = CardweeperModel()
c.deck()
