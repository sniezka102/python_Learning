names = ["Jeffrey", "Nicholas", "Wilfred", "Ashley","Dorothy", "Cynthia", "Jerad", "Alice"]

vowel_name = []
for name in names:
	if name[0].lower() in "aeiou":
		vowel_name.append(name)
		

#below will be created as the comprehensions list - we don't need to split the values in the separatere lines. We do it because  it is possible, we can write it in 
# one line
vowel_name = [
  name 
  for name in names 
  if name[0].lower() in "aeiou"
  ]
print (vowel_name)