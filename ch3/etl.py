 def etl_pipeline(texts):
     stopwords = {"the", "a", "is", "in", "at", "of", "on", "and", "to", "for"}
     all_Words = [word.lower() for text in texts for word in text.split()]
     filtered_Words = filter(lambda word: word and word not in stopwords, all_Words)    
     word_Frequencies  = {}
     for word in filtered_Words:
         word_Frequencies[word] = word_Frequencies.get(word, 0) + 1
     return word_Frequencies
