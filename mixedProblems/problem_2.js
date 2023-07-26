// Problem 2: How do you calculate the number of vowels and consonants in a String

myString = "Auntor"
noOfVowel = 0
noOfCons = 0
var arrayOfString = myString.toLowerCase().split("")
arrayOfString.forEach(element=>{
    if(element=='a' || element=='e' || element=='i'|| element=='o' || element=='u'){
        noOfVowel++
    }else{
        noOfCons++
    }
})

console.log(`No of Vowel is ${noOfVowel} and No of Consonent is ${noOfCons}`)

