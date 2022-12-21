a: int = 5
b: int = 6
h: list[int] = [1]
i: list[int] = [4]

def test(d: int, e: int) -> None:
    temp: int = d
    d = e
    e = temp

def test2(f: list[int], g: list[int]) -> None:
    temp: list[int] = f[0]
    f[0] = g[0]
    g[0] = temp


def main() -> None:
    test(a, b)
    print(a)
    print(b)
    test2(h, i)
    print(h)
    print(i)
   
main()