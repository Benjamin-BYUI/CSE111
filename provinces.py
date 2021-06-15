def main():
    read_clean_file("provinces.txt")

def read_clean_file(filename):
    with open(filename, "rt") as readfile:
        provinces = []
        alberta_count = 0
        next(readfile)
        for line in readfile:
            line = line.strip()
            if line == "AB": line = "Alberta"
            if line == "Alberta":
                alberta_count += 1
            provinces.append(line)
        if provinces.pop() == "Alberta": alberta_count -= 1
        print(provinces)
        print()
        print(f"Alberta occurs {alberta_count} times in the modified list.")



if __name__ == "__main__":
    main()