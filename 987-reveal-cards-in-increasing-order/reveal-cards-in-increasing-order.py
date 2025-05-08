from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Empty double ended queue
        dequeCards = deque()

        # reverse sorted array
        for card in sorted(deck, reverse=True):

            # check queue elements
            if dequeCards:

                # not empty, move last element to front 
                dequeCards.appendleft(dequeCards.pop())

            # Insert current card to front of deque
            dequeCards.appendleft(card)

        return list(dequeCards)

          