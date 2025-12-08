pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.(com|org|edu)$"
 emails = ["user@example.com", "bad-email", "test@domain.org"]
 valid = [email for email in emails if re.match(pattern, email)]
 print(valid)
