// Problm 6: How would you find the second largest number in an array?

// 1st way
// array = [2,54,7,98,3,8,64,4,3]
// array.sort((a,b)=>b-a)
// console.log(array)
// console.log(`Second largest number is ${array[1]}`)


//2nd way
array = [2,54,7,98,3,8,64,4,3]
for(var i=0;i<array.length-1;i++){
    for(var j=i+1;j<array.length;j++){
        if(array[i]<array[j]){
            temp=array[j]
            array[j]=array[i]
            array[i]=temp
        }
    }
}
console.log(`Second largest number is ${array[1]}`)