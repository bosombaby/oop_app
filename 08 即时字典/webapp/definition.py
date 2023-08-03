import pandas as pd


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv("../files/word.csv", index_col=0)
        result = df.loc[df["word"] == self.term]["definition"]
        return tuple(result)


if __name__ == "__main__":
    word = Definition("Young")
    print("".join(word.get()))
    # print(word.get())
