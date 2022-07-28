numberShuffle = 0
numberCard = 0
cardCheck = 96

deck = []
deckCopy = []
while numberCard != cardCheck:
    numberCard = numberCard + 1
    deck.append(numberCard)
    deckCopy.append(numberCard)

print(deck)
def shuffleCards (deck):
    midDeck = int(len(deck) / 2)
    halfDeck = int(midDeck-1)
    deckB = deck[0:midDeck]
    deckA = deck[midDeck:len(deck)]
    deck = []
    while deckB != []:
        deck.append(deckA[halfDeck])

        del deckA[halfDeck]
        deck.append(deckB[halfDeck])
        del deckB[halfDeck]
        halfDeck = halfDeck - 1
    deck.reverse()
    return deck

deck=shuffleCards (deck)
numberShuffle = numberShuffle+1

print(deck)
while (deck != deckCopy):
    deck=shuffleCards (deck)
    numberShuffle = numberShuffle+1
    print(deck)
print(numberShuffle)
