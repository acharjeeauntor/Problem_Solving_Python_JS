// Problem 2: How do you find a missing number in an array of 1-100?
var array = [3,8,5,7]
var count = 0
var newArray = []

for(var i=1;i<=100;i++){
  for(var j = 0;j<array.length;j++){
    if(i==array[j]){
      count++
    }
  }
  if(count==0){
    newArray.push(i)
  }else{
    count = 0
  }
}

console.log(newArray)