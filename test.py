def main():
    numbers = [1,2,3]
    total = calc_total(numbers)
    print(total)
def calc_total(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total
if __name__ == "__main__":
  main()
