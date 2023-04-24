def recursive_nth_fibo(n):
    """
    snazime se najit konkretni cislo (poradi cisla) ve Fibonacciho rade
    = soucet dvou predchozich cisel - 0, 1, 1, 2, 3, 5, 8 atd
    """
    if n <= 1:
        return n
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    print(recursive_nth_fibo(30))


if __name__ == "__main__":
    main()
