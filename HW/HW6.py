def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


n = 123456
print(f"Количество цифр в числе: {count_digits(n)}")