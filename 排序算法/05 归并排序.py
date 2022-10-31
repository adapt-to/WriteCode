# coding:utf-8

"""
时间复杂度：O(nlogn)
空间复杂度：O(n)
为稳定排序
非原地排序
"""

def merge_sort(lst):
    """递归+分治 完成归并排序"""
    if len(lst) <= 1:
        return lst
    middle = int (len(lst)/2)  # 取中间值

    left = merge_sort(lst[ :middle])  # 递归获取左边
    right = merge_sort(lst[middle: ])  # 递归获取右边

    merged = []  # 新创建了空间

    while left and right:  # 直到一方为空
        merged.append(left.pop(0) if left [0] <= right[0] else right.pop(0))

    merged.extend(right if right else left)  #该方法没有返回值,但会在已存在的列表中添加新的列表内容

    return merged