from check import *

def main():
    while True:
        run_currency_conversion()
        if not check_restart():
            break

if __name__ == "__main__":
    main()
