// Problem 1 - How do you write a program that sorts numbers?

array = [2,4,5,1,6,8,0,3,7]

for(var i=0;i<array.length;i++)
{
    for (var j=i+1;j<array.length;j++){
        if(array[i]>array[j]){
            temp = array[i]
            array[i]=array[j]
            array[j]=temp
        }
    }
}
console.log(array)