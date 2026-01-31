# String -> Immutable
owner_name = "Masum"
print(f"Owner Name: {owner_name}")

# String Slicing
honey_description ="Honey is too much Healthy"
# Last Index in python always not inclusive / is Exclusive
print(f"First Word: {honey_description[:5]}")
print(f"last Word: {honey_description[18:]}") 
# [starting Index : Stoping Index : Step amount]
print(f"Reverse : {honey_description[::-1]}")

#Encoding & Decoding
word ="Ohayō gozaimasu"
encoded_word = word.encode("utf-8")
print(f"Encoded Word: {encoded_word}")

decoded_word = encoded_word.decode("utf-8")
print(f"Decoded word: {decoded_word}")

