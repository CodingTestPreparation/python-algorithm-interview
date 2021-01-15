class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        var leftProduct = Array(repeating: 1, count: nums.count)
        var rightProduct = Array(repeating: 1, count: nums.count)
        for i in 1..<nums.count {
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
        }
        for j in (0...nums.count-2).reversed() {
            rightProduct[j] = rightProduct[j + 1] * nums[j + 1]
        }

        print(leftProduct)
        print(rightProduct)
        var resultArray: [Int] = []

        for i in 0..<nums.count {
            resultArray.append(leftProduct[i] * rightProduct[i])
        }
        return resultArray

    }
}

let solution: Solution = Solution()

print(solution.productExceptSelf([1, 2, 3, 4]))











