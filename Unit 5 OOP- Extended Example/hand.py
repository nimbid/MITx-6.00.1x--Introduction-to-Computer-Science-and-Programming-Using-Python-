import random

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3

        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.

        word: string
        returns: Boolean (if the word was or was not made)
        """
        word_letter_list = list(word)
        hand_letter_list = []
        # Fill up hand_letter_list with all the letters in the hand.
        for i in self.hand.keys():
            for j in range(self.hand[i]):
                hand_letter_list.append(i)

        def isValidWord(word):
            """
            Returns True if word is made of letters only in the hand;
            returns False otherwise.

            Does not mutate hand or word list.

            word: strings
            """
            hand_copy = self.hand.copy()
            valid_letters = 0
            check_for_letters = set(list(word)) <= set(hand_copy.keys())
            # For every letter in the word, if it is present in the hand,
            # decrement its count by 1.
            for letter in word:
                if letter in hand_copy.keys():
                    valid_letters += 1
            if valid_letters == len(word) and check_for_letters == True:
                return True
            else:
                return False

        if isValidWord(word) == True:
            hand_copy = self.hand.copy()
            for letter in word:
                if letter in hand_copy:
                    hand_copy[letter] -= 1
            # Use dictionary comprehension to copy non-zero values to hand.
            # Non-zero values represent those letters that are still present in
            # the hand.
            self.hand = {k:hand_copy[k] for k in hand_copy if hand_copy[k] != 0}
            return True
        else:
            return False





myHand = Hand(7)
print(myHand)
print(myHand.calculateLen())

myHand.setDummyHand('aazzmsp')
print(myHand)
print(myHand.calculateLen())

myHand.update('za')
print(myHand)
