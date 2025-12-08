Str = "I know Python, Java, and C++ but not Ruby."
pattern = r"(?<!\w)(Python|Java|C\+\+|C#|Ruby|JavaScript|Go|Rust|Swift|Kotlin)(?!\w)"
langs = re.findall(pattern,Str,re.IGNORECASE)

print(langs)
