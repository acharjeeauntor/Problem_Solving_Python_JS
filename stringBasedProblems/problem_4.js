// Problem 4 : How do you find the maximum occurring character in a given string?

function myFunc(text){
    index = 0
    count=0
    lastHeighestValue=0

var arrayOfChar = text.split('')
for(var i=0;i<arrayOfChar.length;i++){
    for(var j=i+1;j<arrayOfChar.length;j++){
        if(arrayOfChar[i]==arrayOfChar[j]){
            count++
        }
    }
    if(count>lastHeighestValue){
        lastHeighestValue = count
        index = i
    }
    count = 0
}
if(lastHeighestValue==0){
    console.log(("There are no maximum occurring character in the given string"))
}else{
    console.log((`There is ${lastHeighestValue+1} ${arrayOfChar[index]} char in the given string`))
}
}

myFunc("auntorttt")