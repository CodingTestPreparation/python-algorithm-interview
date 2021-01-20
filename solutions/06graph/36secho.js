/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  let result = [];
  const dfs = (element, callSize) => {
    let total = element.reduce((sum, curr) => sum + curr, 0);
    if (total > target) {
      element.pop();
      return;
    }
    if (total == target) {
      result.push(element);
      return;
    }
    for (let i of candidates) {
      element.push(i);
      dfs(element, callSize + 1);
    }
  };
  for (let i of candidates) {
    dfs([i], 0);
  }
  return result;
};

console.log(combinationSum([2, 3, 5], 8));
