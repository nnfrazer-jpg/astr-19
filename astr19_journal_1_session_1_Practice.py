Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Write a Python program to print out your full name, your preferred pronouns (optional), and two sentences about your favorite movie and your favorite food.
>>> 
>>> full_name = 'Nate Frazer'
>>> pronouns = 'he/him/his'
>>> print(type(pronouns))
<class 'str'>
>>> sentence_one = 'My favorite movie growing up was Speed Racer but now I like a lot of movies. '
>>> sentence_two = 'My favorite food is street tacos.'
>>> print(full_name + pronouns + sentence_one + sentence_two)
Nate Frazerhe/him/hisMy favorite movie growing up was Speed Racer but now I like a lot of movies. My favorite food is street tacos.
>>> print(full_name + \npronouns + \nsentence_one + \nsentence_two)
SyntaxError: unexpected character after line continuation character
>>> print(full_name + n/pronouns + n\sentence_one + n\sentence_two)
SyntaxError: unexpected character after line continuation character
>>> print(full_name +\n+ pronouns +\n+ sentence_one +\n+\ sentence_two)
SyntaxError: unexpected character after line continuation character
>>> print(full_name + \n + pronouns + \n + sentence_one + \n + sentence_two)
SyntaxError: unexpected character after line continuation character
>>> 
>>> full_name = 'Nate Frazer\n'
>>> pronouns = 'he/him/his\n'
>>> print(full_name + pronouns)
Nate Frazer
he/him/his

>>> sentence_one = 'My favorite movie growing up was Speed Racer but now I like a lot of movies.\n'
>>> sentence_two = 'My favorite food is street tacos.'
>>> print(full_name + pronouns + sentence_one + sentence_two)
Nate Frazer
he/him/his
My favorite movie growing up was Speed Racer but now I like a lot of movies.
My favorite food is street tacos.
>>> 
>>> 
