numberShuffle = 0 #counter for the period of deck
numberCard = 0 #variable to created numbered list
cardCheck = 96 #number of cards in a deck

deck = [] #list to represent deck
deckCopy = [] #list to check if deck is in original order after each shuffle
while numberCard != cardCheck: #creates numbered list to represent deck
    numberCard = numberCard + 1
    deck.append(numberCard)
    deckCopy.append(numberCard)

print(deck) 
def shuffleCards (deck): #perfect shuffle function!!!!! 
    midDeck = int(len(deck) / 2)
    halfDeck = int(midDeck-1)
    deckB = deck[0:midDeck]
    deckA = deck[midDeck:len(deck)] #cuts deck in half
    deck = []
    while deckB != []: #the order of this segment of code within the while loop determines the type of shuffle; thus this is how each file differs in code
        deck.append(deckA[halfDeck])

        del deckA[halfDeck]
        deck.append(deckB[halfDeck])
        del deckB[halfDeck]
        halfDeck = halfDeck - 1
    deck.reverse()
    return deck

deck=shuffleCards (deck)
numberShuffle = numberShuffle+1

print(deck) #prints each step of the shuffle
while (deck != deckCopy): #checks if deck has reverted to original
    deck=shuffleCards (deck)
    numberShuffle = numberShuffle+1
    print(deck)
print(numberShuffle)
