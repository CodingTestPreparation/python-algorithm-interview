/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  nums = nums.sort((a, b) => a - b);
  let numsLength = nums.length;
  let result = [];
  console.log(nums);
  
  for (let i = 0; i < numsLength - 2; i++){
    if (i > 0 && nums[i] == nums[i - 1])
      continue;
    let [left, right] = [i + 1, numsLength - 1];
    while (left < right){
      let sum = nums[i] + nums[left] + nums[right];
      if (sum < 0) { left += 1; }
      else if (sum > 0) { right -= 1; }
      else {
        result.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] == nums[left + 1])
          left += 1;
        while (left < right && nums[right] == nums[right - 1])
          right -= 1;
        left += 1;
        right -= 1;
      }
    }
  }
  return result;
};

console.log(threeSum([-1,0,1,2,-1,-4]))