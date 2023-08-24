// Problem 10 : How to print Floyd’s triangle?

for(var i=0;i<3;i++){
    for(var j=0;j<3;j++){
        if(i==j || i>j){
            console.log("*")
        }
    }
    console.log()
}