sentences = 
["I love python" , "coding is fun" , "painting is cool"] 
res = list( 
map( 
lambda sentence: list( 
map(lambda word: len(word), sentence.split()) 
), 
sentences 
) 
) 
print(res)
