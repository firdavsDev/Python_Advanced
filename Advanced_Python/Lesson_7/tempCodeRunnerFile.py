import time

def sum_numbers():
    return sum(range(1, 100))

def main():
    task1 = sum_numbers()
    task2 = sum_numbers()
    return task1 + task2

if __name__ == '__main__':
    start = time.time()
    result = main()
    print(result)
    print(time.time() - start)
