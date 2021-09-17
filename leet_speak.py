text = input("please Enter a text: ")
leet_speak_mapper= {
    "a":"4",
    'b':'8',
    'e':'3',
    'l':'1',
    'o':'0',
    's':'5',
    't':'7'

}

for key, value in leet_speak_mapper.items():
    if key in text.lower():
        text=text.replace(key,value)



print("leetSpeak output: ",text)