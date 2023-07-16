// Problem 1 : Can you write a method that will erase any character from a string?

function myFunc(text,char){
    var newString = text.replace(char,'')
    return newString
}

console.log(myFunc("auntor","t"))