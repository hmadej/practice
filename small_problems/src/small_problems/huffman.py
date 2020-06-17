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

    def decode(self, emitter):
        if self.char:
            return self.char
        
        bit = next(emitter)
        if bit == '0':
            return self.right.decode()
        elif bit == '1':
            return self.left.decode()
        else:
            raise ValueError(f"Not a bit value! ={bit}")


class HuffmanTree:
    def __init__(self, s: str, f: Dict[str, int]=None):
        self.freq = f
        self.tree, self.msg = self._encode(s)
        

    def _encode(self, s: str):
        if self.freq:
            freq = self.freq
        else:
            freq = dict(Counter(s).most_common())
            
        h = []
        for k, v in freq.items():
            heapq.heappush(h, Node(v, k))
            
        while len(h) != 1:
            left = heapq.heappop(h)
            right = heapq.heappop(h)
            combined_freq = left.frequency + right.frequency
            heapq.heappush(h, Node(combined_freq, None, left, right))
        
        return h[0]
    
    def decode(self, bit_string: str):
        def emit(bit_string: str):
            for bit in bit_string:
                yield bit

        decoded_string = ''
        while True:
            try:
                decoded_string += self.tree.decode(emit(bit_string))
            except StopIteration:
                break

        return decoded_string


