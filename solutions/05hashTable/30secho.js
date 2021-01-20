/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let obj = {};
  let result = 0;
  let start = 0;
  for (let index = 0; index < s.length; index++){
    //같을 때
    if (s[index] in obj && start <= obj[s[index]]){
      start = obj[s[index]] + 1;
    }
    //다를 때
    else{
      result = Math.max(result, index - start + 1);
    }
    obj[s[index]] = index;

  }
  return result
};
console.log(lengthOfLongestSubstring("dvdf"));