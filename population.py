'''
Given a mathematical function regarding population growth. 
Was asked to provide a few answer to questions in the formats implemented in the code
'''

import math

B = 50000
k = 0.2

# a) Svaret er:

def populasjonsvekst(t):
    return B / (1+ 9 * math.exp(-k*t))

print(populasjonsvekst(0)) # N = 5000 når C er 9, ved t0


# b) Svaret er:
    
print(round(populasjonsvekst(24))) #N = 46552 rundet opp fra 46551.99938399246


# c) Svaret er:
    
print(math.floor(populasjonsvekst(22))) #N = 45024

