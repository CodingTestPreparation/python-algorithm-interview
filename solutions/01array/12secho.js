/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min = 100000;
    let profit = 0;
    for (let price of prices){
        min = Math.min(price, min);
        profit = Math.max(profit, price - min);
    }
    return  profit;
};

maxProfit([7,1,5,3,6,4])