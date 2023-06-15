"""r_gcd is a tail recursion version gcd solution"""
def r_gcd(a: int, b: int) -> int:
    print(f"a: {a}")
    print(f"b: {b}")
    if (b == 0):
        return a
    return r_gcd(b, a % b)

def gcd(a: int, b: int) -> int:
    while b!= 0:
        print(f"a: {a}")
        print(f"b: {b}")
        temp = a
        a = b
        b = temp % b
    return a

