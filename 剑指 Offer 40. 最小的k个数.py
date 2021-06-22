#输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#示例 1：
#输入：arr = [3,2,1], k = 2
#输出：[1,2] 或者 [2,1]
#示例 2：
#输入：arr = [0,1,2,1], k = 1
#输出：[0]
##########################solution1##########################
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        sort_arr = sorted(arr)
        return sort_arr[:k]
    
##########################solution2##########################    
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, l, r):
            if r <= l:
                return
            i = l
            j = r
            while i < j:   
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            quick_sort(arr, l, i-1)
            quick_sort(arr, i+1, r)
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]
