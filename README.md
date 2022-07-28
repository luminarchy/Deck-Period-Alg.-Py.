# Deck-Period-Alg.-Py.
###### Finding the period of any even numbered deck
A Python project that I coded for my 2019 ProMYS first-year mathematical project. 

### .The Card Lore. 
A well-known (but practically impossible to replicate) magic trick is to take a standard deck of 52 cards organized perfectly by suit and number and perfectly shuffle it 8 times. After such the card deck seems to not have gone through any change at all, with its order completely undisturbed. 

We first define a 'perfect' shuffle as the following: Take a stack of m playing cards, with m even, cut it into two equal stacks, and place one on the left and one on the right alternately select the top card from each stack of m/2 cards, left then right then left then right and so on, and place in turn each newly selected card below those selected previously till you end up with a reordered stack of cards of the original stack. In simpler terms it is quite literally a *perfect* ruffle shuffle. 
Thus the period of a deck is defined as the number of perfect shuffles it takes for the deck to revert back to its original position. 

There are a few different ways to shuffle a deck, which will affect the period of the deck. 
A shuffle is defined with two attributes (top/bottom) and (up/down). 
**Top Shuffle:** During a shuffle, after cutting the deck into two equal stacks, if we take the first card from the top half of the deck first, then it is called top shuffle.
**Bottom Shuffle:** During a shuffle, after cutting the deck into two equal stacks, if we take the first card from the bottom half of the deck first, then it is called bottom shuffle.
**Up Shuffle:** During a shuffle, after cutting the deck into two equal stacks, we can either take a card from the top or bottom of each stack. The shuffle is considered a ‘up’ shuffle if every time we select a new card, we take it from the top of the deck. 
**Down Shuffle:** During a shuffle, after cutting the deck into two equal stacks, we can either take a card from the top or bottom of each stack. The shuffle is considered a ‘down’ shuffle if every time we select a new card, we take it from the bottom of the deck. 
Thus there are 4 different shuffles to consider when finding the period of a deck. 

### .How the Code Works.
For our convenience and simplicity, we are numbering each card rather than considering suits. So a deck of 52 cards would have numbers from 1 to 52. Each deck starts in numerical order. 

The variable labeled *cardCheck* will denote the number of cards in the deck. The code will print the order of the cards after each perfect shuffle, and once the deck has reverted back to original position, the period will be printed. 

Comments on the code are shown on the bottomdown.py file

### .Further Implications and Project results. 
There may not be any implications of such a niche project; however, I find it quite interesting that if the period of card decks were to be graphed it looks eerily similar to the graph of the Euler's Totient Formula. The mathematical equations to find the period is also included alongside the progam files if any further interest might be piqued. 

### .Credits. 
The project was coded by me (Amy Suo) as a component of the Shuffling Cards mathematical research project conducted by Senjuti Dutta (senjutid58@gmail.com), Alex Arnell (alexandergarnell@gmail.com), and Amy Suo (amysuwoah@gmail.com) under the mentorship of Natalie Merson 

