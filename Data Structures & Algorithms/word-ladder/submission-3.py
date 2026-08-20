from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        word_set.add(beginWord)

        graph = {word: [] for word in word_set}
        
        for word in word_set:
            for idx, og_letter in enumerate(word):
                for i in range(26):
                    new_letter = chr(ord("a") + i)
                    if og_letter == new_letter:
                        continue
                    new_word = word[:idx] + new_letter + word[idx + 1:]
                    if new_word in word_set:
                        graph[word].append(new_word)


        def bfs(beginWord):
            queue = deque([(beginWord, 1)])
            visited = {beginWord}

            while queue:

                node, dist = queue.popleft()

                if node == endWord:
                    return dist

                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

            return 0 

        return bfs(beginWord)
        