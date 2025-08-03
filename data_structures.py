def display_list(message, lst):
    print(f"{message}: {lst}")

def main():
    my_list = []
    display_list("empty list", my_list)

    my_list += [10, 20, 30, 40]
    display_list("appends",my_list)

    my_list.insert(1, 15)
    display_list("15 inserted at index 1", my_list)

    my_list.extend([50, 60, 70])
    display_list("Extended", my_list)

    removed = my_list.pop()
    display_list(f"last element removed ({removed})", my_list)

    my_list.sort()
    display_list("Sorting in ascending order", my_list)

    try:
        index_30 = my_list.index(30)
        print(f"Index of value 30: {index_30}")
    except ValueError:
        print("Value 30 not found in the list.")

if __name__ == "__main__":
    main()
