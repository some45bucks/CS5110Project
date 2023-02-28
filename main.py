import sys

def main():
    if len(sys.argv) >= 2:
        DeltaLength = int(sys.argv[1])
    else:
        DeltaLength = 5

if __name__ == "__main__":
    main()