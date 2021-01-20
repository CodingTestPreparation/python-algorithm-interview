/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let rowLength = grid.length;
  let colLength = grid[0].length;
  let result = 0;
  const dfs = (x, y) => {
    if(x < 0 || y < 0 || x >= rowLength || y >= colLength || grid[x][y] == "0"){
      return;
    }
    if (grid[x][y] == "1") {
      grid[x][y] = "0";
      dfs(x - 1, y);
      dfs(x, y - 1);
      dfs(x + 1, y);
      dfs(x, y + 1);
    }
  };
  for (let i = 0; i < rowLength; i++) {
    for (let j = 0; j < colLength; j++) {
      if (grid[i][j] == "1") {
        dfs(i, j);
        result++;
      }
    }
  }
  return result;
};

console.log(
  numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
  ])
);
