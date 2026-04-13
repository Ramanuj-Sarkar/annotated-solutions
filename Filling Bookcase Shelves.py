'''
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

    For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
'''
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # the width and height of zero books is [[0,0]]
        indexed_books = [[0,0]]+books
        n = len(indexed_books)

        # collection of minimum total heights given (index #) books
        # again, height of one book is zero
        heights = [0] + [float('inf')]*(n-1)

        for i in range(1, n):
            j = i-1
            # find the i-th book
            curWidth, curHeight = indexed_books[i]
            while j > -1:
                # decreases the height from infinity the first time
                # then sort of moves tall books down if they fit there
                heights[i] = min(heights[i], heights[j]+curHeight)
                
                curWidth += indexed_books[j][0]

                # maybe the new book was taller than the previous ones
                curHeight = max(curHeight, indexed_books[j][1])
                j -= 1
                # 
                if curWidth > shelfWidth:
                    break
        
        # it's the final height that's the answer
        return heights[-1]
