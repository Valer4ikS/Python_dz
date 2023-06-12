import random


class Card:
    card_score = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.score = Card.card_score.get(self.rank)

    def __repr__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    suit = ['♣', '♥', '♦', '♠']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in Deck.suit for rank in Deck.rank]

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def take(self) -> Card:
        return self.deck.pop(0)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []

    def score(self):
        if self.hand:
            return sum([card.score for card in self.hand])
        return 0

    def draw(self, card: Card):
        self.hand.append(card)

    def show(self):
        return f'Игрок {self.name}: {self.hand} ({self.score()})'


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
print(my_deck)

stone = Player('STONE')
alex = Player('Сергей Рябков')

stone.draw(my_deck.take())
stone.draw(my_deck.take())

alex.draw(my_deck.take())
alex.draw(my_deck.take())

print(stone.show())
print(alex.show())
print('Выиграл: ')
print(stone.name if stone.score() > alex.score() else alex.name)

print(my_deck)