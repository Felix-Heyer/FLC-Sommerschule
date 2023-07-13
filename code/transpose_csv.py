import pandas as pd

def csvToMat (data, separator = ", "):
    tmp = []
    for line in data:
        line = line.rstrip()
        mat_row = line.split(separator)
        tmp.append(mat_row)

    matrix = pd.DataFrame(tmp)
    matrix = matrix.T

    return matrix.to_records(index = False)

if (__name__ == "__main__"):
    transposed_data = []
    with open("transpose_test.csv", "r", encoding="utf-8") as f1:
        transposed_data = (csvToMat(f1))

    with open("test_transposed.csv", "w", encoding="utf-8") as f2:
        for i in transposed_data:
            for j in i:
                f2.write(j + "\t")
            f2.write("\n")
