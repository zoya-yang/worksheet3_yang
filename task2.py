def recaman_sequence(n):
    sequence = [0]
    seen = {0}

    for k in range(1, n):
        prev = sequence[k - 1]
        candidate = prev - k

        if candidate > 0 and candudate not in seen:
            sequence.append(candidate)
            seen.add(candidate)
        else:
            next_value = prev + k
            sequence.append(next_value)
            seen.add(next_value)

    return sequence

length = int(input("enter the lengh of the Recaman Sequence: "))

print(recaman_sequence(length))