/**
 * Created by DV on 24/02/2017.
 */
function cutTheRopes(a){
    var myCounter = [a.length];
    var myMinValue = Math.min.apply(null,a);
    var myOutputArr = [];

    for(var myIter = 0; myIter < a.length; myIter++){
        myMinValue = Math.min.apply(null,a);
        console.log(myMinValue);
        a = a.map(function(myInput) {
            return myInput - myMinValue <= 0 ? 0 : myInput - myMinValue
        });

    }

    console.log(a);
    // console.log(myOutputArr);
    
    return myCounter


}

console.log(cutTheRopes([3, 3, 2, 9, 7]))
