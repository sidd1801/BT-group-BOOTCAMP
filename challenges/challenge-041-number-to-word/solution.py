# solution.py

def number_to_words(num):
    """
    Converts each digit of the number into words.
    Example:
    Input: 270176
    Output: Two Seven Zero One Seven Six
    """

    words = ["Zero", "One", "Two", "Three", "Four",
             "Five", "Six", "Seven", "Eight", "Nine"]

    result = [words[int(digit)] for digit in str(num)]
    return " ".join(result)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(number_to_words(num))
