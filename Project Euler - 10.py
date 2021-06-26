import eulerlib

def prime():
    ans = sum(eulerlib.primes(1999999))
    return str(ans)

if __name__ == "__main__":
    print(prime())
