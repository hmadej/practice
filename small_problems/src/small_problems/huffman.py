from collections import Counter
from typing import Tuple, Dict
import heapq


def generate_binary(n: int) -> int:
    for i in range(n.bit_length()):
        yield 0b1 & (n >> i)


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

    def decode(self, num: int):
        if self.character:
            return num >> 1, self.character
        
        bit = 0b1 & (num)
        if bit == 1:
            return self.right.decode(num >> 1)
        elif bit == 0:
            return self.left.decode(num >> 1)
        else:
            raise ValueError(f"Not a bit value! ={bit}")

    def populate_encoder(self, num: int, d: Dict[str, int]):
        if self.character:
            d[self.character] = num
        else:
            if self.left:
                self.left.populate_encoder((num << 1), d)
            if self.right:
                self.right.populate_encoder((num << 1) | 0b1, d)

# TODO leading zeros are not perserved in integers, use different representation!
class HuffmanTree:
    def __init__(self, s: str, f: Dict[str, int]=None):
        self.freq = f
        self.tree = self._generate(s)
        self.encode_dictionary = dict()
        self.tree.populate_encoder(0, self.encode_dictionary)
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
        encoded = 0
        for char in s:
            num = self.encode_dictionary[char]
            for bit in generate_binary(num):
                encoded = (encoded | bit) << 1
        return encoded

    def decode(self, num: int): 
        decoded_string = ''
        remaining_num = num
        while remaining_num > 0:
            remaining_num, char = self.tree.decode(remaining_num)
            decoded_string += char
        return decoded_string


