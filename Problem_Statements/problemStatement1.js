//Initialise a variable res to 0, to store the final answer.
var res = 0;
var arr = [0,1,0,2,1,0,1,3,2,1,2,1];

//Traverse the array A[] from 1 to N and for each element
for(let i =0; i <arr.length;i++){
    var left_max=arr[i];

    //Traverse from A[i] till the beginning and update
    for(let j = i-1; j >= 0; j--){
        left_max =Math.max(left_max,arr[j]);
}

//traverse from A[i] till the end of the array and update
    var right_max=arr[i];
    for(let k =i+1; k < arr.length;k++){
        right_max =Math.max(right_max,arr[k]);
}
max_val=Math.min(left_max,right_max);

//final result
res+=max_val-arr[i];
}
console.log(res);