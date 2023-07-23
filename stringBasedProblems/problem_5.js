// Problem 5 : How do you find the first unrepeated character of a given string?

var text = "auntoraunto"
count = 0
var charOfString = text.split('')
for (var i=0;i<charOfString.length;i++){
    for (var j=i+1;j<charOfString.length;j++){
      if(charOfString[i]==charOfString[j]){
        count++
      }
    }
    
    if(count==0){                                                                                                                                                                       
        console.log(charOfString[i])
        break
    }
    count = 0
}
