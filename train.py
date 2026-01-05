""" 
Input File

Currently, we are using the tiny shakespeare dataset, which is a text file containing the works of Shakespeare. 

"""
with open('input.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

# Some limited data analysis to understand the dataset.

print("length of dataset in characters: ", len(text))
print(text[:1000])

chars = sorted(list(set(text)))
vocab_size = len(chars)
print("all the unique characters: ", ''.join(chars))
print("vocab size: ", vocab_size)

# mapping from characters to integers and vice versa
stoi = { ch:i for i, ch in enumerate(chars) }
itos = { i:ch for i, ch in enumerate(chars) }
def encode(s):
    return [stoi[c] for c in s]
def decode(l):
    return ''.join([itos[i] for i in l])

print("encode: ", encode("hii there"))
print("decode: ", decode(encode("hii there")))


