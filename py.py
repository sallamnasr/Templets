def gcd(x, y):
    while x and y:
        if (x > y):
            x %= y
        else:
            y %= x
    return x if x else y


def divisors(num):
    arr = []
    i = 1
    while i*i <= num:
        if num % i == 0:
            arr.append(i)
            if i != num//i:
                arr.append(num//i)
        i += 1
    return arr
