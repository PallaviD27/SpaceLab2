import numpy as np
import matplotlib.pyplot as plt

""" Parameters:
    b:vector of transmitted information bits
    b_hat:vector of estimated information bits  
    c: vector of transmitted code bits
    c_hat:vector of estimated codebits
    output:
    BE:Number of incorrectly received bits with coding
    BEuc: Number of incorrectly received bits without coding """

def count_errors(b,b_hat,c,c_hat):
    BE=0
    BEuc=0
    # Check if the lengths of b, b_hat, c and c_hat matches

    if len(b)!=len(b_hat):
        print("Error in length in b and b_hat")
        return None,None
    if len(c)!=len(c_hat):
        print("Error in length in c and c_hat")
        return None,None

    # Add the errors in BE and BEuc if the bits don't match

    for i in range (len(b)):
        if b[i]!=b_hat[i]:
            BE+=1

    for i in range (len(c)):
        if c[i]!=c_hat[i]:
            BEuc+=1

    print(f'BE: {BE}, BEuc: {BEuc}')

    return BE,BEuc







