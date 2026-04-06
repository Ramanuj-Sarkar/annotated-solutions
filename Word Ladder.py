# The goal is to transform beginWord into endWord using the words in wordList.
# You can only transform one letter at a time, but all the words are the same length.
# You return how many words were used, and if it is impossible, you return 0.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not all([endWord in wordList, endWord, beginWord, wordList]):
            return 0

        # all words are the same length, so beginWord is chosen arbitrarily
        length = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure the same word isn't processed repeatedly
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(length):
                # Intermediate words for current word
                intermediate_word = (current_word[:i] + "*" + current_word[i + 1 :])

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If we find the end word, we can return the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                
                # now you take all the words out of this list
                all_combo_dict[intermediate_word] = []
        
        # no such sequence exists
        return 0
