def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reverse: {fruit_list}")

    fruit_list.append("orange")
    print(f"append orange : {fruit_list}")

    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(f"add cherry before apple: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    removed = fruit_list.pop()
    print(f"removed: {removed}")
    print(f"popped: {fruit_list}")

    fruit_list.sort()
    print(f"sort: {fruit_list}")

    fruit_list.clear()
    print(f"clear: {fruit_list}")

main()