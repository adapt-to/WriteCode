# coding:utf-8
# 插入排序:原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
"""
时间复杂度：O(n^2)
空间复杂度：O(1)
稳定排序
原地排序
"""


def insertion_Sort(arr):
    #从要排序的列表第二个元素开始比较
    for i in range(1,len(arr)):  # 循环数组
        j = i

        while j > 0:  #从右到左比较，直到比较到第一个元素
            if arr[j] < arr[j-1]:  # 当左边大于右边时，交换位置
                arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1

    return arr