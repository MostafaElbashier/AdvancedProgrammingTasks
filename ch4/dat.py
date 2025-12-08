 event = "The events are on 2023-05-12 and 2024-01-01."
 pattern = r"\d{4}-\d{2}-\d{2}"
 event_dates = re.findall(pattern, event)
 print(event_dates)
