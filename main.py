## Card class
## Class dirrector
import random

class Dirrector:

    def __init__(self):
        
        self.card_value = []
        self.is_playing = True

    def display_card(self):
        print(card_value)

    def start_game(self):
        while self.is_playing:
            self.dislpay_card

            self.display_card


class Card:

    def __init__(self):
        self.previous_value = 0
        self.value = 0
        self.points = 300


    def current_card(self):
        self.value = random.randint(1, 14)

    def previous_card(self):
        self.previous_value = self.value
        

    def guess(self):

        self.previous_card()
        self.current_card()

        user_input = input('Higher or Lower? [h/l]: ')

        if user_input == 'h':
            if self.previous_value < self.value:
                self.points += 100


    


