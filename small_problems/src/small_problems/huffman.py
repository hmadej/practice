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

    def decode(self, index: int, bit_string: str):
        if self.character:
            return index, self.character
        
        bit = bit_string[index]
        if bit == '1':
            return self.right.decode(index+1, bit_string)
        elif bit == '0':
            return self.left.decode(index+1, bit_string)
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
        index = 0
        decoded_string = ''
        while index < len(bit_string):
            index, char = self.tree.decode(index, bit_string)
            decoded_string += char
        return decoded_string


