# coding=utf-8
import re
import time

def partition(data, left, right): # 左右分别指向两端的元素
    tmp = data[left]                # 把左边第一个元素赋值给tmp,此时left指向空
    while left < right:             # 左右两个指针不重合，就继续
        while left < right and data[right] >= tmp:  # right指向的元素大于tmp,则不交换
            right -= 1                      # right 向左移动一位
        data[left] = data[right]            # 如果right指向的元素小于tmp，就放到左边现在为空的位置
        while left < right and data[left] <= tmp:   # 如果left指向的元素小于tmp,则不交换
            left += 1                       # left向右移动一位
        data[right] = data[left]            # 如果left指向的元素大于tmp,就交换到右边
    data[left] = tmp            # 最后把最开始拿出来的那个值，放到左右重合的那个位置
    return left                 # 最后返回这个位置
#  写好归位函数后，就可以递归调用这个函数，实现排序
def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)  # 找到指定元素的位置
        quick_sort(data, left, mid - 1)     # 对左边元素排序
        quick_sort(data, mid + 1, right)    # 对右边元素排序
    return data

if __name__ == "__main__":
    num = {'a':1, 'b':2}
    print num.get('aa',0)
    print num