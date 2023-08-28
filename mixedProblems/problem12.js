// Problem 12: How to check if a given year is a leap year
var year = 2012
if(year%400==0){
    console.log("The year is Leap year")
}else if(year%4==0 && year%100!=0){
    console.log("The year is Leap year")
}else{
    console.log("The year is not Leap year")
}