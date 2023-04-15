/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let newArr =[];
    let sum = 0;

    nums.forEach((num) => {
        sum += num;
        newArr.push(sum);
    });
    return newArr;
};