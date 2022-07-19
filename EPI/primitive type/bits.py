# time: o(1)/bits,  total: o(n), number of bits need to represent the integer
# e.g: 12 = 1100 (4 bits)
import math
import random
import sys


# bitwise operation https://www.w3schools.com/python/python_operators.asp
# bit converter: https://www.rapidtables.com/convert/number/binary-to-ascii.html
# python bitwise 细节: https://realpython.com/python-bitwise-operators/#overview-of-pythons-bitwise-operators
def bitwise_operation():
    # << vs <<= 都是同一个意思, << 直接给数字用来移动， <<=用于给variable
    print(2 << 2)
    x = 2
    x <<= 2
    print(x)
    # right shift 1 bits, 最左边那一位减少，不加0 or 1
    8 >> 1
    # left shift 10 bits, 新多出来的那10个bits是0
    1 << 10
    # -16>>2,

    # And &: =1 if both bits are 1
    print(6 & 4)

    # OR |: =1 if one of two bits is 1
    1 | 2

    # XOR ^: =1 if only one of two bits is 1
    15 ^ x

    # NOT ~: inverts all bits
    ~0


# count how many bit is 1
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        # >>= left shift 1 bit
        x >>= 1
    return num_bits


# 4.1 check word's 奇偶性
# method: check every bits
# time: o(n), n is the word size
def parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# improve easing/unsetting the lowest set-bit(1 bit) in a word in a single operation
# time o(k), k is number of 1 bit in number e.g:10001010, k  =3
def party_shift_improve(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1

    return result

# improve using cache, time:o(log n), n is the word size
# todo: come back study p28

# 4.2 Swap bits


def import_func_integer():
    # max value Integer of memory
    # print(sys.maxsize)
    # print(count_bits(12))

    # important function of integer
    abs(-34.5)  # 34.5
    math.ceil(2.17)  # 3
    math.floor(3.14)  # 3
    min(1, -4)
    max(3.14, 5)
    pow(2, 3)  # 2^3 = 8
    2 ** 3  # 2^3 = 8
    math.sqrt(4)  # square root(4) = 2


def convert():
    # integers <-> string
    str(42)
    int('42')

    # floats <-> string
    str(3.14)
    float('3.14')

    # floats
    print(float('inf'))
    print(float('-inf'))


def random_func():
    # random
    random.randrange(28)
    random.randint(8, 16)
    random.random()
    # random.shuffle(A)
    # random.choice(A)


if __name__ == "__main__":
    # print(count_bits(0))
    # print(count_bits(1))
    # print(count_bits(2))
    # print(count_bits(3))
    # print(count_bits(4))
    for x in range(100):
        print("number %s is: %s" % (x, parity(x)))
