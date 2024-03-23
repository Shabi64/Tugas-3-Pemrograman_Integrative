def main():
    # Read integers from the file
    with open("indata.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    # Calculate the sum
    total = sum(numbers)

    # Format the sum with comma separators and two decimal places
    formatted_total = "{:,.2f}".format(total)

    # Print the formatted sum
    print(formatted_total)


if __name__ == "__main__":
    main()
