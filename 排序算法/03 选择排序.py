# coding:utf-8
# 选择排序：首先在未排序序列中找到最小元素,存放到排序序列的起始位置,然后,再从剩余未排序元素中继续寻找最小元素,然后放到已排序序列的末尾。以此类推,直到所有元素均排序完毕
"""
时间复杂度：O(N^2)
空间复杂度：O(1)
不稳定排序：比如说 5,8,5,2,9 这样一组数据,使用选择排序算法来排序的话,第一次找到最小元素2,与第一个5 交换位置,那第一个5 和中间的5 顺序就变了
原地排序
"""


# 以下标序号为标准
def Selectionsort1(arr):
    len_arr = len(arr)

    for i in range(len_arr):
        min = i  # 假定最小值的下标为第一个

        for j in range(i + 1, len_arr):  # 上一个值右边的数组
            if arr[min] > arr[j]:  # 使min为最小值,遇到比min小的值就把下标进行替换
                min = j

        arr[i], arr[min] = arr[min], arr[i]  # 交换最小值到左边
    return arr

