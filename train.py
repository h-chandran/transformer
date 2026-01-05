""" 
Input File

Currently, we are using the tiny shakespeare dataset, which is a text file containing the works of Shakespeare. 

"""
with open('input.txt', 'r', encoding = 'utf-8') as f:
    data = f.read()

# Some limited data analysis to understand the dataset.

print("length of dataset in characters: ", len(data))
print(data[:1000])

chars = sorted(list(set(data)))
vocab_size = len(chars)
print("all the unique characters: ", ''.join(chars))
print("vocab size: ", vocab_size)