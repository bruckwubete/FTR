if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most problems.
    t = int(input())  # read a line with a single integer
    for c in range(1, t + 1):
        times = int(input())
        names = []
        for _ in range(times):
            names.append(input())
        cost = 0
        for i in range(1, len(names)):
            if names[i - 1] > names[i]:
                for j in range(i - 1, -1, -1):
                    if names[j] > names[i]:
                        cost += 1
                        tmp = names[j]
                        names[j] = names[i]
                        names[i] = tmp

        print(f"Case #{c}: {cost}")
