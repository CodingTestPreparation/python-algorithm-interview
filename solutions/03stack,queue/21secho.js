/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function (s) {
  let result = [];
  let obj = {};
  let lettersArray = s.split("");
  for (let letter of s) {
    if (!obj.hasOwnProperty(letter)) {
      obj[letter] = 1;
    } else {
      obj[letter] += 1;
    }
  }
  lettersArray.forEach((value, index) => {
    obj[value] -= 1;
    if (result.indexOf(value) == -1) {
      while (
        result.length > 0 &&
        obj[value] >= 0 &&
        result[result.length - 1] > value &&
        obj[result[result.length - 1]] != 0
      ) {
        result.pop();
      }
      result.push(value);
    }
  });
  return result.join("");
};

console.log(removeDuplicateLetters("abacb"));
