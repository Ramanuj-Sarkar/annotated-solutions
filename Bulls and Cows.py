# It's like a Wordle row but for numbers.
# Bulls are when the digit and placement are the same.
# Cows are when the digit is the same but the placement is different.
# Returns it like {# bulls}A{# cows}B.
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # characters in secret are associated with positive values
        # while characters in guess are associated with negative values
        # since they are supposed to cancel one another out
        h = defaultdict(int)
        bulls = cows = 0

        for g, s in zip(guess, secret):
            if s == g: 
                bulls += 1
            else:
                # h[s] < 0 if the GUESS contained more s characters
                # h[g] > 0 if the SECRET contained more g characters
                # it basically compares with the other one
                cows += int(h[s] < 0) + int(h[g] > 0)

                # this is where the positive/negative association happens
                h[s] += 1
                h[g] -= 1
                
        return "{}A{}B".format(bulls, cows)
        
