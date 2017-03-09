# Knuckle Tattoos with Crossed Fingers
*which word combinations scramble to make other valid word combinations?*

scramble? like if you got a knuckle tattoo and then interweave your fingers

*wouldn't it be cool if your knuckle tattoo said something else when you interweave your fingers?*

right now it checks 8-letter 2-word combos. Can be used to check other types of 8-letter input strings

## !!! WARNING !!!!
this program deals with a LOT of data (there are millions of combinations of words to try), and is probably not as optimized as it could/should be.  a cache it creates can use up several GB of memory.  running this program might overwhelm your machine.  use at your own risk.

the amount of processing the program does can lead to running times of several minutes on a fairly powerful machine.  

## usage
- see WARNING above
- install pip requirements "pip install -r requirements.txt"
- if desired, edit the word lists in wordlists/, adding words that are meaningful to you, deleting words that aren't.  
- run the scramble finder "python scramble_finder.py" *this just prints the result to the console.  if you want to save to a file, you can redirect the output to a file: "python scramble_finder.py >> results.txt"*
- if you want, once you have a txt file of results you can use the code in /flask_app to populate a database and serve/query the results via a simple web app. *see the readme in /flask_app*


