# Problem 1 : Can you write a method that will erase any character from a string?


def erase_character(text,char):
    newText=""
    for ch in text:
        if(ch!=char):
            newText+=ch
    return newText


print(erase_character("AuntorA","A"))



def erase_character_from_string(text,char):
    newText = text.replace(char,"")
    return newText

print(erase_character_from_string("auntora","a"))



