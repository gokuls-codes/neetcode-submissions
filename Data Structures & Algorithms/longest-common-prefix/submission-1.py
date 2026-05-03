class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = [None for _ in range(26)]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        trie = TrieNode()

        for word in strs:
            currNode = trie
            for ch in word:
                currVal = ord(ch) - ord('a')
                if not currNode.children[currVal]:
                    currNode.children[currVal] = TrieNode()

                currNode = currNode.children[currVal]
                currNode.count += 1

        currPrefix = ""
        currNode = trie

        while True:
            foundNext = False
            for i in range(26):
                if currNode.children[i] is not None:
                    if currNode.children[i].count == n:
                        currPrefix += chr(ord('a') + i)
                        currNode = currNode.children[i]
                        foundNext = True
                        break
            if not foundNext: return currPrefix