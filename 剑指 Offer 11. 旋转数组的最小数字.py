#把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers)-1
        
        while left <= right:
            mid = (left + right)//2
            if numbers[right] > numbers[mid]:
                right = mid
            if numbers[right] < numbers[mid]:
                left = mid
            if left == mid:
                if numbers[left] <= numbers[right]:
                    return numbers[left]
                if numbers[left] > numbers[right]:
                    return numbers[right]
        
