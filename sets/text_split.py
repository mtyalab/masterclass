text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Split the text to create a list of words from the text
text_split = text.split()

# Create an intersection
preps_used = prepositions.intersection(text_split)
print(f"{preps_used}")