
def trim_and_repeat(defaul_string, offset=0, repetitions=1)->str:
    return defaul_string[offset:] * repetitions
    


def main()->None:
    string = input("Введите строку: ")
    offset = int(input("Введите число символов для обрезки"))
    repetitions = int(input("Введите число символов для обрезки"))
    trim_and_repeat(string, offset, repetitions)



if __name__ == "__main__":
    main()