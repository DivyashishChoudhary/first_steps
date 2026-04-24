def main():
    hello()
    name = input("What's your name? ").strip()
    hello(name)

def hello(to="world"):
    print("hello,", to)


main()