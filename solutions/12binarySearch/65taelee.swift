class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {

        var start: Int = 0
        var end: Int = nums.count - 1
        while start < end {
            var middle: Int = (start + end) / 2
            print(start, middle, end)
            if nums[middle] == target {
                print(nums[middle], target)
                print("success", start, middle, end)
                return middle
            } else if nums[middle] < target {
                start = middle + 1
            } else {
                end = middle - 1
            }
        }
        return -1
    }
}
