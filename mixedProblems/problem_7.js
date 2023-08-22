// Problem 7: How do you calculate the number of vowels and consonants in a String?

function myFunc(word){
    var ArrayOfString  = word.toLowerCase().split('')
    var vawel = 0
    var cons =0
    for(var i =0;i<ArrayOfString.length;i++){
        if(ArrayOfString[i]=='a' || ArrayOfString[i]=='e' || ArrayOfString[i]=='i' || ArrayOfString[i]=='o' || ArrayOfString[i]=='u'){
            vawel++
        }else{
            cons++
        }
    }
    console.log(`Number of Vowel is ${vawel} and Number of Consonent ${cons}`)
}

myFunc("Howareyou")