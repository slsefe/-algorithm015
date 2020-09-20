# 第四周学习笔记

## 1. 深度优先搜索和广度优先搜索

- 遍历or搜索：每个节点访问且仅访问一次
- 按照节点访问顺序不同分为：
    - 深度优先：depth first search
    - 广度优先：breadth first search
    - 优先级优先，启发式算法

```python
def dfs(node):
    # terminator
    if node in visited:
        return
    visited.add(node)
    # process
    # drill down
    dfs(node.left)
    dfs(node.right)
    # reverse state

def bfs(node):
    queue = []
    queue.append(node)
    visited.add(node)
    while queue:
        node = queue.pop()
        process(node)
        nodes = generate_related_nodes(node)
        for node in nodes:
            if node not in visited:
                visited.add(node)
                queue.append(nodes)
```

## 2. 贪心算法

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优的选择，从而希望导致结果是全局最好或最优的算法


- 贪心：局部最优，不能回退
- 回溯：可以回退
- 动态规划：最优判断+回退

贪心法可以解决一些最优化问题，如：最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们要求的答案。

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别准确的问题。

如果要用贪心法，第一问题需要比较特殊，第二需要证明贪心法得到的结果是全局最优解。

- 贪心法适用条件
    - 问题能够分解为子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。
    - 贪心算法与动态规划的不同在于：贪心算法对每个子问题的解决方案都做出选择，不能回退，而动态规划则会保存以前的运算结果，并根据之前的记过可以对当前结果进行选择，有回退功能。

## 3. 二分查找

- 三个前提条件
    1. 目标函数单调性
    2. 存在上下界
    3. 能够通过索引访问
   
- 代码模板

```python
left, right = 0, len(nums)-1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```