// Problem 3: How do you get the matching elements in an integer array?

myIntArray = [0,1,3,4,6,7,1,7,3,4,9,0,1]
machingElement = []
for(var i =0;i<myIntArray.length;i++){
for(var j=i+1;j<myIntArray.length;j++){
if(myIntArray[i]==myIntArray[j]){
    if(machingElement.includes(myIntArray[i])==false){
        machingElement.push(myIntArray[i])
    }
}
}
}
console.log(machingElement)
