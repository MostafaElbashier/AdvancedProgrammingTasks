Str = "Python, Python! AI is great; Python AI."
 words = re.findall(r"\w+", Str)
freq = dict(Counter(words))
print(freq)
