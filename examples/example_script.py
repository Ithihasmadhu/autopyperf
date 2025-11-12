from autopyperf import profile_function


@profile_function
def calculate():
    data = []
    for i in range(100000):
        data.append(i ** 2)
    return sum(data)


if __name__ == "__main__":
    total = calculate()
    print(f"Sum of squares: {total}")
