
def get_num_words(input: str) -> list:
    return input.split()

def letter_counts(input: str) -> list:
    letter_count = {}
    for _char in input:
        char = _char.lower()

        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
            
    arr = []
    
    for char in letter_count:
        arr.append({"char": char, "num": letter_count[char]})
    
    return arr