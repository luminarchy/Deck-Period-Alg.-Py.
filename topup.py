numberShuffle = 0
numberCard = 0
cardCheck = 64

deck = []
deckCopy = []
while numberCard != cardCheck:
    numberCard = numberCard + 1
    deck.append(numberCard)
    deckCopy.append(numberCard)

print(deck)
def shuffleCards (deck):
    midDeck = int(len(deck)/2)
    deckA = deck[0:midDeck]
    deckB = deck[midDeck:len(deck)]
    deck = []
    while deckB != []:
        deck.append(deckA[0])

        del deckA[0]
        deck.append(deckB[0])
        del deckB[0]
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
