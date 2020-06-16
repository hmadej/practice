from collections import Counter
from typing import Tuple, Dict
import heapq


class Node:
    def __init__(self, frequency: int, char: str = None, left = None, right = None):
        self.frequency = frequency
        self.character = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency
    

class HuffmanTree:
    def __init__(self, s: str, f: Dict[str, int]=None):
        self.tree = self._encode(s)
        self.freq = f

    def _encode(self, s: str):
        freq = self.freq if self.freq else dict(Counter(s).most_common())
        
        h = []
        for k, v in freq.items():
            heapq.heappush(h, Node(v, k))
            
        while len(h) != 1:
            left = heapq.heappop(h)
            right = heapq.heappop(h)
            combined_freq = left.frequency + right.frequency
            heapq.heappush(h, Node(combined_freq, None, left, right))
        
        return h[0]

    def _decode(self, bit_string: str):
        pass
