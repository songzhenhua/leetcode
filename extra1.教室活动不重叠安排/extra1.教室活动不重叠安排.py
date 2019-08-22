# coding=utf-8
"""
这是《算法导论》上的例子，也是一个非常经典的问题。
有n个需要在同一天使用同一个教室的活动a1,a2,…,an，教室同一时刻只能由一个活动使用。
每个活动ai都有一个开始时间si和结束时间fi 。一旦被选择后，活动ai就占据半开时间区间[si,fi)。
如果[si,fi]和[sj,fj]互不重叠，ai和aj两个活动就可以被安排在这一天。
该问题就是要安排这些活动使得尽量多的活动能不冲突的举行。
"""


def max_actives(li):
    """
    用贪心法的话思想很简单：活动越早结束，剩余的时间越多，能安排的活动就越多。
    找最早结束的那个活动，找到后在剩下的活动中再找最早结束的，如图1。
    :param li: 活动的开始结束时间列表
    :return actives: 最终安排活动列表
    """
    li.sort(key=lambda x: x[1])  # 先按每个活动的结束时间排序
    actives = [li[0]]
    start_time = li[0][1]
    for i in range(1, len(li)):
        if li[i][0] >= start_time:
            actives.append(li[i])
            start_time = li[i][1]

    return actives


if __name__ == "__main__":
    a = [(5, 9),(3, 5),(5, 7),(3, 8),(1, 4),(6, 10),(8, 11),(8, 12),(2, 13),(0, 6),(12, 14)]
    actives = max_actives(a)
    for i in actives:
        print i
