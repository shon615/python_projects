favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

if 'erin' not in favorite_languages.keys():
	print("Erin please take the poll!")
	

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking our poll!")
	
print("\n\n")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

print("\n\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print (name.title())
	
	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " + 
			favorite_languages[name].title() + "!")
