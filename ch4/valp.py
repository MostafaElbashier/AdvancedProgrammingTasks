phones = ["+1-555-1234", "5551234", "123-456-7890"]
 pattern = r"^\+?\d{1,3}[-]?\d{3}[-]?\d{4}$"
 for p in phones:
    print(f"{p}: {bool(re.match(pattern, p))}")
