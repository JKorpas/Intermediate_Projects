import random


class Machine:
    def __init__(self):
        self.score = 0

    def get_spin(self, rows, cols, symbols: dict) -> list:
        all_symbols = [symbol for symbol, symbol_count in symbols.items()
                       for _ in range(symbol_count)]
        #print(all_symbols, rows, cols)
        matrix = []
        for _ in range(rows):
            wheel = []
            copy_of_symbols = all_symbols.copy()
            for _ in range(cols):
                value = random.choice(copy_of_symbols)
                copy_of_symbols.remove(value)
                wheel.append(value)
            matrix.append(wheel)
        # print(matrix)
        self.show_result(matrix)
        self.check_primary_diagonal(matrix)
        self.check_row(matrix)
        self.check_wheel(matrix)
        self.check_secondary_diagonal(matrix)
        self.show_score()

    def show_result(self, matrix):
        for col in range(len(matrix)):
            for number in matrix[col]:
                print(f"|{number}| ", end="")
            print()

    def check_row(self,matrix):
        for rows in matrix:
            if len(set(rows)) == 1:
                self.score += 1
                #print(f"check_row")

    def check_wheel(self, matrix):
        for i in range(len(matrix)):
            if len(set([symbol[i] for symbol in matrix])) == 1:
                self.score += 1
                #print(f"check_wheel")

    def check_primary_diagonal(self, matrix):
        primary_diagonal = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # Condition for principal diagonal
                if (i == j):
                    print(i,j,len(matrix))
                    primary_diagonal.add(matrix[i][j])
        if len(primary_diagonal) == 1:
            self.score += 1
            #print(f"check_primary_diagonal")

    def check_secondary_diagonal(self, matrix):
        secondary_diagonal = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1,0,-1):
                # Condition for secondary diagonal
                if ((i + j) == (len(matrix)-1)):
                    print(i,j,len(matrix))
                    secondary_diagonal.add(matrix[i][j])
        if len(secondary_diagonal) == 1:
            self.score += 1
            #print(f"check_secondary_diagonal")

    def show_score(self):
        print(f"{self.score} lines")

    