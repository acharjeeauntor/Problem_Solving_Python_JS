// Problem 5 - Can you remove duplicates from an array?

var array =[2,5,7,8,3,2,8,9,3,2]
var newArray=[]


for(var i=0;i<array.length;i++){
    var count =0
    for(var j=i+1;j<array.length;j++){
        if(array[i]==array[j]){
            count++
        }
    }
    if(count==0){
        newArray.push(array[i])
    }
}
console.log(newArray)