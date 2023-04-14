/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
 
    let mapArr = nums.map(num => num * num).sort((a, b) => a - b);
   
    return mapArr;
};