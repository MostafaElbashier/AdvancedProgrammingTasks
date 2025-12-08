 Str = "This is is a test test"
 duplicates = re.findall(r"\b(\w+)\s+\1\b", Str)
 print([f"{w} {w}" for w in duplicates])
