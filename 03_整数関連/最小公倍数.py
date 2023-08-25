import math

#x × yを最大公約数で割ったものが最小公倍数となる
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(my_lcm(6, 4))

