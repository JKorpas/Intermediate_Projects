import pandas


def tranform_to_nato(name):
    return " ".join([nato_dict[char] for char in name])


df = pandas.read_csv("nato_phonetic_alphabet.csv")
'''keys = df.iloc[:, 0]
values = df.iloc[:, 1]'''
nato_dict = {key: value for key, value in zip(df.iloc[:, 0], df.iloc[:, 1])}
name = str(input("Tell me your name so i can do my shit: ").upper())
print(tranform_to_nato(name))
