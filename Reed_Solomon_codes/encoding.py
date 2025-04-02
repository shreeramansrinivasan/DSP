import numpy as np
def reed_solomon_encoding(m,n,k,input_words):
    """Trying to figure out how to write the encoder"""
    """Planning to implement the systematic version of the reed solomon encoding algorithm"""
    """Systematic version means that the encoding input words are part of the final message word"""
    """what's the n and k to use """
    """m is the number of bits per message symbol, n is the total number of symbol, k is the number of input message symbols
    input words is of length k message symbols"""
    if len(input_words) != k:
        raise ValueError("Input words length must be equal to k")
    