import unittest

class CardGame:
    def __init__(self,data):
        self.data = data

# Run through round of game
    def round(self,deck):
        table = []
        while len(deck) > 0:
            table.append(deck.pop(0))
            if len(deck) != 0:
                deck.append(deck.pop(0))
        table.reverse()
        return table                                                            

    # Run through game
    def game(self,noofCards):
        if noofCards >0:    
            deck = []
            origDeck = []
            rounds = 1

            # Generate deck and copy
            for j in range(1, noofCards + 1):
                deck.append(j)
                origDeck.append(j)

            # Run through one round
            deck = self.round(deck)

            # Loop through until deck is life first
            while deck != origDeck:
                deck = self.round(deck)
                rounds += 1

            print (f"No of rounds needed for {noofCards} is {rounds}")      
            return rounds

        else:
            print ("The input should be greater than zero for card value")
            return False

if __name__=='__main__':
    numOfCards = int(input('Enter number of cards:'))
    cardGame = CardGame(None)
    cardGame.game(numOfCards)

class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        #Test the results for positive input values
        cardgame = CardGame(None)
        result = cardgame.game(5)
        self.assertEqual(result,5)
        
        result = cardgame.game(32)
        self.assertEqual(result,12)
        

        #Test the results for negative input value
        result = cardgame.game(-1)
        self.assertEqual(result,False)
 
# run the test
unittest.main()