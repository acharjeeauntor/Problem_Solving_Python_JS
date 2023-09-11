// Problem 4 : Can you find duplicate numbers in an array?

var array = [3,6,8,8,3,10,10,0,4,2,7]
var duplicateArray=[]
var count=0
for(var i =0;i<array.length;i++){
    for(var j=i+1;j<array.length;j++){
        if(array[i]==array[j]){
            duplicateArray.push(array[j])
        }
    }

}

console.log(duplicateArray)