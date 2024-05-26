#! /usr/bin/python3

def fizz_buzz(r):
    for i in range(1, r+1):
        x = str(i)
        y = ""
        z = ""
        if (i) % 3 == 0:
            y = "fizz"
            x = ""
        if (i) % 5 == 0:
            z = "buzz"
            x = ""
        print(x+y+z)


if __name__ == "__main__":
    fizz_buzz(15)
