
def sum_distance(one_number, two_number)->int:
    if one_number > two_number:
        one_number, two_number = two_number, one_number
        print (sum(range(one_number, two_number + 1)))
    


def main()->None:
    start_number = input("Введите начальное число: ")
    end_number = input("Введите конечное число")
    sum_distance(start_number, end_number)



if __name__ == "__main__":
    main()