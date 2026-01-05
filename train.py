""" 
Input File

Currently, we are using the tiny shakespeare dataset, which is a text file containing the works of Shakespeare. 

"""
with open('input.txt', 'r', encoding = 'utf-8') as f:
    data = f.read()

