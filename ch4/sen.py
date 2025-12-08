 credit_Card = "Card: 1234-5678-9012-3456"
 masked_Card = re.sub(r"\d(?=[\d-]*\d{4})", "*",credit_Card)
 print(masked_Card)
