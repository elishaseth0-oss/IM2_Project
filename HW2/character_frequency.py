

def char_frequency(text):
    freq = {} 
    for char in text:
        if char.isalpha(): 
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq



string = input("Enter string: ")


parts = string.split(",")

for part in parts:
    part = part.strip()
    result = char_frequency(part)

    output = ", ".join([f"{k}={v}" for k, v in result.items()])
    print(output)

