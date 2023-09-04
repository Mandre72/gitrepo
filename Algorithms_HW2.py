#Level 1
#Task1
def reverse_integer(n: int) -> int:

    num_str = str(n)

    if num_str[0] == '-':

        reversed_str = '-' + num_str[1:][::-1]
    else:

        reversed_str = num_str[::-1]

    reversed_int = int(reversed_str)

    return reversed_int


original_num = -189
reversed_num = reverse_integer(original_num)
print(f"Original: {original_num}, Reversed: {reversed_num}")


#Task2
def are_anagrams(s1: str, s2: str) -> bool:

    s1 = s1.lower()
    s2 = s2.lower()

    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    return sorted_s1 == sorted_s2


word1 = "race"
word2 = "care"
print(are_anagrams(word1, word2))  # Should return True

word1 = "hEArt"
word2 = "earth"
print(are_anagrams(word1, word2))  # Should return True

word1 = "rattle"
word2 = "battle"
print(are_anagrams(word1, word2))  # Should return False


#Level2
#Task3
def reverse_words(sentence: str) -> str:

    words = sentence.split()

    reversed_words = []

    for word in words:

        reversed_word = word[::-1]

        reversed_words.append(reversed_word)

    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence


sentence1 = "Hello World"
print(reverse_words(sentence1))  # Should return "olleH dlroW"

sentence2 = "mistertwister"
print(reverse_words(sentence2))  # Should return "retsiwtretsim"


#Task4
def repeat_digits(s: str) -> str:
    result = ""

    for char in s:
        current_num = int(char)
        repeated_char = char * current_num
        result += repeated_char

    return result  #


string1 = "312"
print(repeat_digits(string1))  # Should return "333122"

string2 = "102"
print(repeat_digits(string2))  # Should return "122"


#Task5
def shortcut(s: str) -> str:

    result = ""

    vowels = set("aeiou")

    for char in s:

        if char not in vowels:

            result += char

    return result


string1 = "hello"
print(shortcut(string1))  # Should return "hll"

string2 = "goodbye"
print(shortcut(string2))  # Should return "gdby"
