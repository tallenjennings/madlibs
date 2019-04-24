"This is a madlibs game"


#intro
print('Hi You')
print('We are going to play a wacky word game')
print('It is going to ask you for some words')
print('Then use those words to fill in some blanks')

input('Are you ready?')

#banter
print('It goes a little something like this!')
print('There was a ______ that _____ a _____')
print('It is your job to fill in those words')
print('What words would you like to put in there?')

#banter words
bantOne = input('1st word: ')
bantTwo = input('2nd word: ')
bantThree = input('3rd word: ')

#banter concatination
print('There was a ' + bantOne + ' that ' + bantTwo + ' a ' + bantThree)
print('and it licked a knife and rolled on the floor')
print('Wasnt that a great story!?!')

#now for the madlib 
print('I will ask you for a few words. Either a verb, adverb or adjective') 

#answers
ad1 = input('adjective: ')
noun1 = input('noun: ')
verb1 = input('verb: past tense: ')
adverb1 = input('adverb: ')
ad2 = input('adjective: ')
noun2 = input('noun: ')
noun3 = input('noun: ')
ad3 = input('adjective: ')
verb2 = input('verb: ')
adverb2 = input('adverb: ')
verb3 = input('verb: past tense: ')
ad4 = input('adjective: ')

#story
print('Today I went to the zoo. I saw a ' + ad1 + noun1 + ' jumping up and down in its tree. He ' + verb1 + adverb1 + ' through the large tunnel that led to its ' + ad2 + noun2 + '. I got some peanuts and passed them through the cage to a gigantic gray ' + noun3 + ' towering above my head. Feeding that animal made me hungry. I went to get a ' + ad3 + ' scoop of ice cream. It filled my stomach. Afterwards I had to ' + verb2 + adverb2 + ' to catch our bus. When I got home I ' + verb3 + ' my mom for a ' + ad4 + ' day at the zoo.')
