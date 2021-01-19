/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
  nums = nums.sort((a, b) => a - b);
  let result = 0;
  let pair = [];
  nums.forEach((value, index) => {
    pair.push(value);
    if (index % 2 == 1){
      result += Math.min.apply(null, pair);
      pair = [];
    }
  });  
  return result;
};