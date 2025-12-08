def remove_vowels(str):
vowels = "aeiouAEIOU"
return "".join([char for char in str if char not in vowels])
