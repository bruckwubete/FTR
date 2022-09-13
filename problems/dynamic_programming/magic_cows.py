import math

if __name__ == '__main__':
    init_farms = [1, 3, 2, 1]
    capacity = 8
    visiting_days = [0, 1, 2]

    remainder_farms = []
    num_init_full = 0
    for i in init_farms:
        if i <= math.ceil(capacity / 2):
            remainder_farms.append(i)
        elif i == capacity:
            num_init_full += 1

    full_farms = [num_init_full]
    print(full_farms)

    for i in range(1, max(visiting_days) + 1):
        updated_remainder_farms = []
        num_filled_farms = 0
        for j in remainder_farms:
            if j * 2 <= math.ceil(j * 2 / capacity):
                updated_remainder_farms.append(j)
            else:
                num_filled_farms += 1
        remainder_farms = updated_remainder_farms
        full_farms.append((full_farms[i - 1] * 2) + num_filled_farms)

    print([full_farms[i] for i in visiting_days])
