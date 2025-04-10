import numpy as np
import galois
def primitive_elements(m):
    GF = galois.GF(2**m)
    return GF.primitive_element
def generator_poly(k,n,m):
    """Computes the generator polynomial of reed solomon code"""
    GF = galois.GF(2**m)
    alpha = GF.primitive_element
    roots = []
    for i in range(n-k,n):
        roots.append(alpha**i)
    return galois.Poly(roots,GF)
def reed_solomon_encoding(m,n,k,input_words):
    """Trying to figure out how to write the encoder"""
    """Planning to implement the systematic version of the reed solomon encoding algorithm"""
    """Systematic version means that the encoding input words are part of the final message word"""
    """what's the n and k to use """
    """m is the number of bits per message symbol, n is the total number of symbol, k is the number of input message symbols
    input words is of length k message symbols"""
    if len(input_words) != k:
        raise ValueError("Input words length must be equal to k")
    #To construct the final output, take the input polynomial , 
    # scale it by x^(n-k)
    # find the remainder of the division by th generator polynomial 
    # construct the message by concatenating the input words and the remainder 
    # return the message 
    GF = galois.GF(2**m)
    message_word = galois.Poly([input_words[i] for i in range(k)],GF)
    append_zeros = galois.Poly([0 for i in range(n-k)],GF)
    message_word = message_word + append_zeros
    gen_poly = generator_poly(k,n,m)
    remainder = message_word % gen_poly
    message_word = message_word + remainder
    return message_word
