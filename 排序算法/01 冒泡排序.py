# coding:utf-8
# Py3
"""

冒泡的Python实现
-------------------------
稳定排序、原地排序
时间复杂度：O(n^2)
空间复杂度：O(1)
-------------------------

"""

print(111)

def sort_by_bubble(arr):
    """冒泡排序"""
    len_arr = len(arr)
    for i in range(len_arr):  # 遍历数组元素
        for j in range(0, len_arr-i-1):  # 遍历数组元素，末尾已排序的无需遍历
            if arr[j] > arr[j+1]:  # 如果左边大于右边，交换数值
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


