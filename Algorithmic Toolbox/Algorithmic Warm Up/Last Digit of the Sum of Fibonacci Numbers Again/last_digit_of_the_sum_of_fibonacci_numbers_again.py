# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]



    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_dig_of_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        n = n % 60
        if n == 0:
            return 0
        prev, curr, = 0, 1
        count = 1
        for i in range(2, n + 1):
            prev, curr = curr, (prev + curr) % 10
            count += curr
            count %= 10
        return count

def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    return (last_dig_of_sum(to_index) - last_dig_of_sum(from_index - 1)) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
