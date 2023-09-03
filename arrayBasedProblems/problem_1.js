// Problem 1 : How do you find the largest and smallest number in an array of 1-100?
var array = [4,8,6,9,1,2,5,6,8,7,1,3,858,-8,0,699,1452]
for(var i=0;i<array.length;i++){
    for(j=i;j<array.length;j++){
        if(array[i]>array[j]){
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        }
    }
}
console.log(`The smallest value is: ${array[0]}`)
console.log(`The latgest value is: ${array[array.length-1]}`)
