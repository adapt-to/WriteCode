# coding:utf-8
"""
快速排序:快速排序使用分治法策略来把一个序列分为较小和较大的2个子序列,然后递归地排序两个子序列。

是否稳定排序：不稳定排序 
是否原地排序：原地排序
时间复杂度：O(nlog^n) 【随机选取基准值的方法】
空间复杂度：O(log^n) 

"""

def quick_sort(arr):
    """使用分治+递归的方式"""
    if len(arr) <= 1:
        return arr   
     
    pivot = arr[len(arr) // 2]    # 挑选基准值，选择中间的元素

    left = [x for x in arr if x < pivot]    # 小于基准值的序列，列表推导式
    
    middle = [x for x in arr if x == pivot]    # 等于基准值的序列
    
    right = [x for x in arr if x > pivot]    # 大于基准值的序列

    return quicksort(left) + middle + quicksort(right)  # 递归返回


