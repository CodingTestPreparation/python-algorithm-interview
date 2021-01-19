/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let datas = s.split('');
  let stack = [];
  for(let data of datas){
    if (data == '(' || data == '{' || data == '[')
      stack.push(data);
    else{
      if (data == ')' && stack[stack.length - 1] == '(') stack.pop();
      else if (data == ']' && stack[stack.length - 1] == '[') stack.pop();
      else if (data == '}' && stack[stack.length - 1] == '{') stack.pop();
      else return false;
    }
  }
  return stack.length > 0 ? false : true;
};

console.log(isValid("[][]"))