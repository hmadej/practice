from collections import Counter
from typing import Tuple, Dict
import heapq


class Node:
    def __init__(self, frequency: int, char: str = None, left = None, right = None):
        self.frequency = frequency
        self.character = char
        self.left = left
        self.right = right
        self.visited = False

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def decode(self, emitter):
        if self.character:
            return self.character
        
        bit = next(emitter)
        if bit == '1':
            return self.right.decode(emitter)
        elif bit == '0':
            return self.left.decode(emitter)
        else:
            raise ValueError(f"Not a bit value! ={bit}")

    def populate_encoder(self, bit_string: str, d: Dict[str, str]):
        if self.character:
            d[self.character] = bit_string
        else:
            if self.left:
                self.left.populate_encoder(bit_string + "0", d)
            if self.right:
                self.right.populate_encoder(bit_string + "1", d)

class HuffmanTree:
    def __init__(self, s: str, f: Dict[str, int]=None):
        self.freq = f
        self.tree = self._generate(s)
        self.encode_dictionary = dict()
        self.tree.populate_encoder("", self.encode_dictionary)
        self.msg = self.encode(s)


    def _generate(self, s: str):
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

    def encode(self, s: str):
        encoded = ""
        for char in s:
            encoded += self.encode_dictionary[char]
        return encoded

    def decode(self, bit_string: str): 
        # doesn't work need to fix how bit_string is feed, through 
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


