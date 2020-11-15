# 学习笔记

- 数据结构与算法
    - 复杂度分析
    - 存储结构
        - 顺序存储
        - 链式存储
    - 逻辑结构
        - 线性结构
            - 栈
            - 队列
        - 非线性结构
            - 散列表
            - 树
                - 二叉树
                - 多路查找树
                - 堆
            - 图
    - 二分查找
    - 排序
    - 字符串匹配
    - 搜索
    - 查找
    - 算法思想
        - 枚举
        - 贪心
        - 分治
        - 回溯
        - 动态规划
    - 其他
        - 跳表
        - Trie树
        - 布隆过滤器
        - 并查集
        - 位运算
        - LRU Cache

## 1. 数组、链表、跳表

### 1.1 数组array

1. 定义：数组是一种线性表数据结构.它用一组连续的内存空间, 来存储一组具有相同类型的数据.
2. 操作
    - 查找: 在数组中查找元素的时间复杂度为`O(n)`, 在有序数组中使用二分查找的时间复杂度为`O(logn)`.
    - 随机访问:
      - 连续的内存空间和相同类型的数据使得数组具有**随机访问**的特性. 以长度为`n`的`int`类型数组为例, 假设首地址为`base_address`, 则第i个元素的内存地址为`base_address + i * data_type_size`, 其中`data_type_size`为数组类型的字节大小.
      - 数组支持随机访问, 根据下标随机访问的时间复杂度为`O(1)`.
    - 插入:
      - 有序数组的插入操作根据插入位置的不同最好时间复杂度为`O(1)`, 最坏时间复杂度为`O(n)`, 平均时间复杂度为`O(n)`.
      - 无序数组的插入操作可以将要插入位置的元素搬移到数组元素的末尾, 同时插入新的元素, 避免了大量的数据搬移, 时间复杂度为`O(1)`, 快排中使用了这种技巧.
    - 删除:
      - 为了保持数组元素的连续性, 删除操作需要进行数据搬移, 最好时间复杂度为`O(1)`, 最坏时间复杂度为`O(n)`, 平均情况时间复杂度为`O(n)`.
      - 有些特殊情境下, 为了避免进行多次数据搬移, 可以先记录下要删除的数据, 当数组中没有更多存储空间时, 再触发一次真正的删除操作.
3. 实现
    - 针对数组类型, `Java`提供了`ArrayList`, `C++`提供了`vector`. 以`Java`语言为例, `ArrayList`最大的优势是可以将很多数组操作的细节封装起来, 并且支持动态扩容. 如果事先能够确定存储的数据大小, 最好在创建`ArrayList`的时候指定数据大小.
    - 在Python中, 列表list和元组tuple都是一个可以存储任意数据类型的有序集合. 列表是动态的, 长度可变, 可以随意增加/删除/改变元素, 列表的存储空间略大于元组, 性能略逊于元组; 元组是静态的, 长度大小固定, 无法增加/删除/改变, 元组相对于列表更加轻量级, 性能稍优. 两者可以通过`list()`和`tuple()`方法相互转换, 常用的内置函数有: count(item)统计item出现的次数, index(item)返回item第一次出现的索引, reverse()原地反转, sort()进行排序. 元组适合用来存储不变的数据, 列表适合用来存储需要变化的数据. list和tuple的内部都是通过数组array实现的, list因为长度可变是一个over-allocate的array, 而元组是一个长度不变的array.
4. leetcode相关题目
    - 283移动零（双指针）
    - 11盛最多水的容器（首尾指针）
    - 15三数之和（三指针）
    - 88合并两个有序数组（三指针）
    - 26删除排序数组中的重复项（双指针）
    - 80删除排序数组中的重复项二（双指针）

### 1.2 链表linked list

1. 定义：链表是一种线性表数据结构，它用一组任意的存储单元来存储数据，同时存储当前数据元素的直接后继元素所存放的内存地址。
2. 操作
    - 插入和删除操作时间复杂度为`O(n)`
    - 查找某个结点或元素的时间复杂度为`O(n)`
3. 形态
    - 单链表：数据data和后继指针next
    - 双向链表：在单链表的基础上增加了前驱指针prev，支持O(1)找到前驱结点
    - 循环链表：在单链表的基础上将尾结点指向了头结点，支持O(1)找到尾结点
4. leetcode相关题目
    - 19删除链表倒数第N个结点（快慢指针）
    - 876链表中间节点（快慢指针）
    - 141环形链表（快慢指针）
    - 142环形链表二（快慢指针）
    - 206反转链表（迭代、递归）
    - 24两两交换链表节点（迭代、递归）
    - 25K个一组反转链表
    - 21合并两个有序链表（双指针、递归）
    - 23合并K个有序链表（归并、优先级队列）
    - 83删除排序链表中的重复项（双指针）
    - 82删除排序链表中的重复项二（双指针）

### 1.3 数组和链表的比较

1. 时间复杂度
    - 数组随机访问O(1)，链表随机访问O(n)
    - 数组插入删除O(n)，链表插入删除O(1)
2. 访问效率
    - 数组内存空间连续，可使用CPU缓存预读，访问效率更高
    - 链表在内存中非连续存储，对CPU缓存不友好
3. 空间
    - 数组空间固定，可能出现内存不足或者空间浪费
    - 链表天然支持动态扩容，没有空间浪费情况
4. 应用场景
    - 对于查找操作频繁、插入删除操作很少的需求使用数组实现，对于查询操作很少、插入删除操作频繁的需求使用链表实现
    - 对于空间固定的场景使用数组，对于空间不确定的情况使用链表

### 1.4 跳表skip list

1. 定义：有序链表+多级索引
2. 操作：插入、删除、查找O(logn)
3. 应用
    - Redis中的有序集合zset
    - LevelDB

## 2. 栈、队列、双端队列、优先级队列

### 2.1 栈stack

1. 定义：栈是一种操作受限的线性表，只能在表尾进行插入和删除操作。
2. 操作
    - 在栈顶插入元素，入栈push，O(1)
    - 删除栈顶元素并弹出，出栈pop，O（1）
3. 实现
    - 用数组实现：顺序栈
    - 用链表实现：链式栈
4. 应用场景
    - 函数调用
    - 四则表达式求值
    - 括号匹配
    - 浏览器前进后退功能
5. 存在性思考：栈是一种操作受限的线性表，功能不如数组和链表强大，凡是可以使用栈和队列的场景，都可以使用数组和链表来实现。但是，特定的数据结构是对特定场景的抽象，当某个数据集合只需要在一端插入和删除数据，并且满足先进后出的特性，就应该使用栈这种数据结构。
6. leetcode相关题目
    - 20有效的括号（基本操作）
    - 155最小栈（两个栈实现）
    - 730每日温度（单调栈）
    - 84柱状图中最大的矩形（单调栈）
    - 42接雨水（单调栈）

### 2.2 队列 queue

1. 定义：一种操作受限的线性表，满足先进先出，在表头进行删除操作、表尾进行插入操作
2. 操作
    - 入队enqueue O(1)
    - 出队dequeue O(1)
3. 实现：使用head和tail指针分别指向表头和表尾
    - 用数组实现：顺序队列
    - 用链表实现：链式队列
4.应用场景
    - 循环队列：避免顺序队列出队操作时频繁的数据搬移
5. leetcode相关题目

### 2.3 双端队列deque

1. 定义：在线性表两端都可以进行插入和删除操作
2. 操作
    - 表头出队popleft O(1)
    - 表尾入队push O(1)
    - 表尾出队pop O(1)
    - 表头入队pushleft O(1)
3. 实现
4. leetcode
    - 622设计循环队列
    - 641设计循环双端队列
    - 239滑动窗口最大值（双端单调队列）

### 2.4 优先级队列priority queue

1. 定义：元素出队时不再按照先进先出，而是按照优先级出队
2. 操作
    - 入队：O(logn)
    - 出队：O(logn)
3. 实现
    - python中使用二叉堆heap实现，heap底层是一个数组，元素入队时和出队后要调整元素位置。
4. leetcode相关题目
    - 23合并K个有序链表（归并、优先级队列）
    - 剑指offer40最小的k个数
    - 347前K个高频元素

## 3. 哈希表、映射、集合

### 3.1 哈希表hash table

1. 定义：key-value对，其中key不重复
2. 操作
    - 查找：判断某个key是否在哈希表中，若在取出其对应的value值，否则返回默认值或者抛出异常O(1)
    - 更新：更新哈希表中某个key的value值
    - 删除：删除哈希表中某个key
3. 实现：python中的dict，底层使用数组实现，利用了**数组支持按照下标随机访问数据**的特性，通过**散列函数**把元素的键值映射为下标, 然后将数据存储在数组中对应下标的位置.当我们按照键值查询元素时, 我们用同样的散列函数, 将键值转换为数组下标, 从对应的下标中取出数据.
4. leetcode相关题目
    - 1两数之和（哈希表）
    - 242有效的字母异位词
    - 49字母异位词分组

### 3.2 集合set

1. 定义：不重复元素的集合
2. 操作
    - 查找：某个元素是否在集合中
    - 添加：添加某个元素到集合中
    - 删除：从集合中删除某个元素
3. 实现：python中的set

## 4. 树

### 4.1 二叉树 binary tree

1. 定义：每个节点最多只有两个节点，称为left左节点和right右节点
2. 操作
    - 遍历
        - DFS O(n)
            - 前序遍历：根->左->右
            - 中序遍历：左->根->右
            - 后序遍历：左->右->根
        - BFS O(n)

### 4.2 二叉搜索树 binary search tree

1. 定义：空树或者具有下列性质的二叉树
    1. 左子树上所有节点的值小于根结点的值
    2. 右子树上所有节点的值大于根结点的值
    3. 左、右子树也是二叉搜索树
2. 性质：中序遍历为升序排序
3. 操作
    - 查询：O(logn)
    - 插入：O(logn)
    - 删除：O(logn)

### 4.3 AVL树

1. 自平衡二叉搜索树
2. 引入平衡因子：左子树与右子树的高度之差，取值为{-1，0，1}，所有叶子节点的平衡因子为0，保证所有结点的平衡因子都在{-1,0,1}中

- 旋转操作：
    1. 左旋：右右子树->左旋
    2. 右旋：左左子树->右旋
    3. 左右旋：左右子树->左右旋 等价于 左右子树左旋得到左左子树，再右旋
    4. 右左旋：右左子树->右左旋

- 带有子树的旋转
- 不足：每个结点需要存储平衡因子，调整次数频繁

### 4.4 红黑树

- 定义：近似平衡的二叉搜索树，任何一个结点的左右子树的高度差小于两倍。
- 特点：
    - 每个结点要么是红色，要么是黑色
    - 根节点是黑色
    - 每个叶子结点都是空结点，是黑色
    - 不能有相邻的两个红色结点
    - 从任意结点到其每个叶子的所有路径都包含相同数目的黑色结点
- AVL tree & Red Black Tree
    - AVL trees provide faster lookups than Red Black Trees because they are more strictly balanced.
    - Red Black Trees provide faster insertion and removal operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
    - AVL trees store balance factors heights with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
    - Red Black Tree are used in most of language libraries like map, multimap, multiset in C++ whereas AVL trees are used in databases where faster retrievals are required.


## 5. 堆、二叉堆、图

### 5.1 堆heap

1. 定义：可以迅速找到一堆数中的最大或者最小值的数据结构
2. 实现：
    - 二叉堆
        - 实现：数组
        - 性质：
            - 完全二叉树
            - 树中任意节点的值>=其子节点的值
3. 操作（二叉堆）：
    - 找到最大值/最小值：返回根结点O(1)
    - 插入元素：新元素插入到尾部，从下至上调整堆，O(logN)
    - 删除元素：使用堆尾元素替代堆顶元素，从上至下调整堆O(logN)

### 5.2 图graph

## 6.递归 recursion

1. 思想：将复杂问题分解为重复子问题，
2. 步骤：
    1. recursion terminator
    2. process current logic
    3. drill down
    4. restore current status if needed
3. 代码模板

    ```
    def recursion(level, param1, param2):
        # 1. recursion terminator
        if level > MAX_LEVEL:
            process_result
            return
        # 2. process logic in current level
        process(level, data, ...)
        # 3. drill down
        self.recursion(level+1, p1, p2)
        # 4. reverse status if needed
    ```
4. leetcode题目：
    - 二叉树的前中后序遍历
    - 将有序数组转化为二叉搜索树
    - 爬楼梯
    - 括号生成
    - 翻转二叉树
    - 二叉树最大深度和最小深度
    - 二叉树序列化和反序列化
    - 二叉树的最近公共祖先
    - 从前序遍历和中序遍历序列构造二叉树

## 7. 分治 divide & conquer

1. 思想：将复杂问题分解为简单子问题，分而治之。
2. 步骤
    1. recursion terminator
    2. split current problem into several sub-problems
    3. drill down: conquer sub-problems, merge sub-problems results
    4. revert current level status if needed
3. 代码模板
4. leetcode题目
    - pow(x,n)
    
## 8.回溯

1. 思想：
2. 步骤：
3. 代码模板
4. leetcode题目
    - 括号生成
    - 组合
    - 组合总和
    - 全排列
    - 全排列II
    - 子集
    - 电话号码的字母组合
    - N皇后
    
## 9. 搜索算法

- 遍历or搜索：每个节点访问且仅访问一次
- 按照节点访问顺序不同分为：
    - 深度优先：depth first search
    - 广度优先：breadth first search
    - 优先级优先，启发式算法

### 9.1 深度优先搜索

```
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
```
### 9.2 广度优先搜索
```
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
### 9.3 基础搜索

1. 朴素搜索
2. 优化方向：去掉重复计算的过程（Fibonacci）、剪枝掉不合理的情况（生成括号问题）
3. 搜索方向
    - DFS
    - BFS
    - 双向搜索：从起点和终点同时BFS
    - 启发式搜索，A*算法：基于优先级队列按照优先级搜索

### 9.4 剪枝

- 爬楼梯
- 括号生成
- N皇后
- 有效的数独
- 解数独

### 9.5 双向BFS

- 单词接龙
- 最小基因变化

### 9.6 启发式搜索

- 二进制矩阵中的最短路径
- 滑动谜题
- 解数独

## 10. 贪心算法

1. 思想：贪心算法是一种在每一步选择中都采取在当前状态下最好或最优的选择，从而希望导致结果是全局最好或最优的算法
2. 贪心&回溯&动态规划
    - 贪心：局部最优，不能回退
    - 回溯：可以回退
    - 动态规划：最优判断+回退
3. 注意点
    - 贪心法可以解决一些最优化问题，如：最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们要求的答案。
    - 一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别准确的问题。
    - 如果要用贪心法，第一问题需要比较特殊，第二需要证明贪心法得到的结果是全局最优解。
4. 贪心法适用条件
    - 问题能够分解为子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。
    - 贪心算法与动态规划的不同在于：贪心算法对每个子问题的解决方案都做出选择，不能回退，而动态规划则会保存以前的运算结果，并根据之前的记过可以对当前结果进行选择，有回退功能。

## 11. 二分查找

1. 三个前提条件
    1. 目标函数单调性
    2. 存在上下界
    3. 能够通过索引访问
   
2. 代码模板

```
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

## 12. 动态规划 dynamic programming

1. 思想
    - 本质是要解决一个分治或者递归问题，可以理解为动态递推
    - simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner.
    - dynamic programming = divide & conquer + optimal substructure
    - 动态规划 = 分治 + 最优子结构
2. 关键点
    - 动态规划和递归、分治没有根本的区别，关键是看问题有无最优的子结构。如果没有最优子结构，需要把所有子问题都进行计算，即为分治；如果存在最优子结构，中间过程只需保存最优子问题的解，即为动态规划。
    - 共性：找到重复子问题
    - 差异性：最优子结构、中途可以淘汰次优解
3. 步骤
    - 寻找重复性，将复杂问题拆解为简单子问题
    - 利用数学归纳法
    - MIT 5 steps to DP, MIT五步DP法
        1. define sub-problems, 定义子问题
        2. guess part of solution, 递推公式
        3. merge sub-problem solutions, 合并子问题的解
        4. recurse & memorize or build DP table bottom-up, 自顶向下的递归+记忆化搜索 或者 自底向上的状态转移表
        5. solve original problem

4. leetcode题目
    - 70, 爬楼梯，简单
    - 62，不同路径，中等
    - 63，不同路径II，中等
    - 1143，最长公共子序列，中等
    - 120，三角形最小路径和，中等
    - 53，最大子序和，简单
    - 152，乘积最大子数组，中等
    - 322，零钱兑换，中等
    - 198，打家劫舍，简单
    - 213，打家劫舍II，中等

## 13. 字典树、前缀树 Trie

### 13.1 树的基本概念回顾
- 树的BFS和DFS
- 二叉搜索树

### 13.2 数据结构
字典树、Trie树，是一种树形结构，典型应用是用于统计和排序大量的字符串，经常被搜索引擎用于文本词频统计。
优点：最大限度减少无谓的字符串比较，查询效率比哈希表高。

### 13.3 基本性质
1. 结点本身不存完整单词
2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串
3. 每个结点的所有子结点路径代表的字符都不相同

### 13.4 核心思想
1. 用空间换时间
2. 利用字符串的公共前缀来降低查询时间

### 13.5 leetcode题目

- 208 中等 实现Trie
- 212 困难 单词搜索II Trie+回溯DFS

## 14. 并查集 disjoint set

### 14.1 适用场景

组合问题，快速判断两个对象是否在同一个集合中

### 14.2 基本操作

- makeSet(s)：建立一个新的并查集，其中包含s个单元素集合
- unionSet(x, y)：将元素x和元素y所在的集合进行合并，要求x和y所在的集合不相交，如果相交则不合并
- find(x)：找到元素x所在集合的代表，也用于判断两个元素是否位于同一个集合（两个元素位于同一个集合<==>两个元素所在集合的代表相同）

### 14.3 实现

```python
class DisjointSet:
    def __init__(self, n: int):
        """初始化n个并查集，每个集合只有一个元素，且代表元素指向自身"""
        self.p = [i for i in range(n)]

    def union(self, i: int, j: int):
        """合并元素i和j所在的集合"""
        p1 = self.parent(i)
        p2 = self.parent(j)
        self.p[p1] = p2

    def parent(self, i: int):
        """找到元素i所在集合的代表元素 """
        root = i
        while self.p[root] != root:
            root = p[root]
        while p[i] != i:  # 路径压缩
            x = i
            i = p[i]
            p[x] = root
        return root
```

### 14.4 leetcode题目

- 547 朋友圈 中等 DFS/BFS/并查集
- 200 岛屿数量 中等 BFS/DFS/并查集
- 130 被围绕的区域 中等

## 15. 位运算

### 1. 数制

- 定义：数制是一种计算数量大小的制度，也叫做计数法。数制中，最重要的因素是基数。如果基数是10，就是十进制计数法；如果基数是2，就是二进制计数法。
- 数制的表示方式：

|数制|英文单词|用到的符号|表示方法(以十进制下的19为例)|
|:-:|:-:|:-:|:-:|
|十进制|decimal|0,1,2,3,4,5,5,6,7,8,9|19|
|二进制|binary|0,1|0b10011|
|八进制|octonary|0,1,2,3,4,5,6,7|0o23|
|十六进制|hexadecimal|0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F|0x13|

### 2. 数制转换的方式

- 其他进制转十进制：换基法，X=sum(X_m*N^(m-1))，N表示数制，X_m表示X从右边向左的第m位
- 十进制转其他进制：除余法，用N作为除数不断做除法，将最后的商和之前的余数逆序串联
- 二进制和八进制互转：按位拆分和按位合并，八进制的一位对应二进制的三位
- 二进制和十六进制互转：按位拆分和按位合并，十六进制的一位对应二进制的四位

### 3. 位运算符
- 按位与&：
    - 定义：两个位都为1时结果才为1，否则为0，0&0=0，0&1=0，1&1=1
    - 用途：
        - 清零：与0进行位与运算
        - 取一个数的指定位：将要取的位数设为1，与原数做位与运算
        - 判断奇偶数：判断最末位是0还是1，a&1=0则为偶数，a&1=1则为奇数
- 按位或|：
    - 定义：两个位都为0时结果才为0，否则为1，0|0=0，0|1=1，1|1=1
    - 用途：
        - 用于对某些位置1：将要置1的位数设为1，与原数做位或运算
- 按位异或^：
    - 定义：两个位相同为0，不同为1，0^0=0，0^1=1，1^1=0
    - 性质：
        - 交换律
        - 结合律：(a^b)^c=a^(b^c)
        - 与自身的异或为0，a^a=0
        - 与0的异或为自身
        - 与全1的异或翻转自身
    - 用途：
        - 翻转指定位：指定位为1，其余位为0，与原数做位异或运算
        - 交换两个数：a ^= b, b ^= a, a ^= b
        - 找出出现次数为1的数：对集合中的所有数做异或运算
- 按位取反~：
    - 定义：0变1，1变0，~0=1，~1=0
    - 用途：
        - 最低位置0：a&~1，~1的值为1111 1111 1111 1110
- 左移<<：
    - 定义：各二进位全部左移若干位，高位舍弃，低位补0。
    - 用途：设a=1010 1110，a=a<<2将a的二进制位左移2位，右边补0，得到a=1011 1000。若左移时舍弃的高位不包含1，则每左移一位，相当于该数乘以2。
- 右移>>，
    - 定义：各二进位全部右移若干位，对无符号数，低位舍弃，高位补0；对有符号数，有的编译器补符号位（算术右移），有的编译器补0（逻辑右移）。
    - 用途：操作数每右移一位，相当于该数除以2.

### 4. 位运算常用技巧
- n & (n-1) 将n的最后一个1置0，清零最低位的1
- n & (-n) 将获取最后一个1

### 5. leetcode题目

- 191 位1的个数
- 231 2的幂
- 190 颠倒二进制位
- 51 N皇后
- 52 N皇后II
- 338 比特位计数

## 16. 布隆过滤器 bloom filter

### 1. 哈希表

- 定义：使用哈希函数将元素映射为索引，将元素存放到对应索引的位置中去。
- 哈希冲突：当多个元素对应同一个索引的时候，称为哈希冲突。
- 拉链法：当遇到哈希冲突的时候，有多种解决方法，最常用的是拉链法。拉链法将冲突的元素以链表的形式保存，将哈希表从一维结构升级为二维结构。
- 哈希表适合于存储一种映射关系，常见操作有添加删除一个元素、判断元素是否存在、获取元素的值。
- 在其它一些场景，不需要存储元素的值和额外信息，只需要判断元素是否存在，这时哈希表就有些大材小用了。

### 2. 布隆过滤器

- 定义：布隆过滤器由一系列随机映射函数和一个二进制向量构成，用于快速检查一个元素是否在一个集合中。
- 操作：
    - 插入操作：将元素哈希取模之后对应的向量下标置为1
    - 查询元素是否存在：查询元素哈希取模之后对应的向量下标，如果有0则不存在，否则有可能存在
- 优缺点
    - 优点：时间复杂度：只需要做映射函数个数的位运算；空间复杂度：二进制向量bit数
    - 缺点：有一定的误识别率，元素删除操作困难
- 实现
    - 基础实现：
```python
from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, size, hash_sum):
        """
        :param size: the length of bit array
        :param hash_sum: the number of hash functions
        """
        self.size = size
        self.hash_sum = hash_sum
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_sum):
            index = mmh3.hash(s, seed) % self.size
            self.bit_array[index] = 1

    def lookup(self, s):
        for seed in range(self.hash_sum):
            index = mmh3.hash(s, seed) % self.size
            if self.bit_array[index] == 0:
                return "Nope"
        return "Probably"
```
    
    - 实现2：https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
    - 高性能实现：https://github.com/jhgg/pybloof

- 应用
    - 账号注册检查：手机号检查、昵称检查

## 17. LRU cache

### leetcode题目

- leetcode146 LRU cache （哈希表+双向链表）

## 18. 排序算法

### 1. 分类
- 排序算法根据是否对元素进行比较可以分为基于比较的排序算法和不基于比较的排序算法。
- 基于比较的排序算法不能突破O(NlogN)的时间复杂度下界，可以比较所有定义好大小关系的数据类型；非基于比较的排序算法一般是O(n)的线性时间复杂度，但只能排序整数数据类型。

### 2. 算法原理

#### 0. 分析角度

- 执行效率（时间复杂度）
    - 最好情况、最坏情况、平均情况的时间复杂度及其对应的输入数据
    - 比较同一阶时间复杂度的排序算法时，考虑系数、常量、低阶
    - 对于基于比较的排序算法，考虑比较次数和交换（移动）次数
- 内存消耗（空间复杂度）
    - 原地排序（sorted inplace）：空间复杂度为O(1)的排序算法
- 稳定性
    - 如果待排序序列中存在值相等的元素，排序后相等元素之间原有的先后顺序不变，则排序算法是稳定的
    - 举例：对于电商交易中的订单排序，订单有下单时间和金额两个属性，需要按金额从小到大排序，对于金额相等的订单按照下单时间从早到晚排序。做法：先按照下单时间排序，再使用稳定排序算法按照金额排序。

#### 1. 选择排序

- 原理：将原始待排序序列分为已排序区间和未排序区间。已排序区间初始为空，每次遍历未排序区间选择最小值插入到已排序区间的末尾，具体做法为：将未排序区间的最小值与未排序区间的第一个元素交换位置，并将此位置划分给已排序区间。
- 时间复杂度分析：O(n^2)
- 空间复杂度：O(1)，原地排序
- 稳定性分析：涉及元素交换，不稳定
- 应用场景：数据量不大且对稳定性没有要求时
- 实现
```python
def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
```

#### 2. 插入排序

- 原理：将原始待排序序列的第一个元素划分为已排序区间，剩余元素为未排序区间。每一轮从未排序区间取首个元素，在已排序区间寻找合适的位置将其插入，直到未排序区间为空。
- 时间复杂度分析：O(n^2)
- 空间复杂度：O(1)，原地排序。
- 稳定性分析：对于值相同的元素，我们可以将后出现的元素插入到前面元素的后面来保证稳定性。
- 应用场景：数据量不大
- 实现
```python
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        flag = False
        for j in range(i, 0, -1):  # 从后往前比较
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                flag = True
            if not flag:
                break
```

#### 3. 冒泡排序

- 原理：从前到后依次比较相邻两个元素的值，若前面元素大于后面元素的值，则交换两个元素的位置。每一轮比较都会至少确定一个元素的最终位置，在每一轮比较完成之后检查当前轮是否发生元素交换，若无则说明序列已排好序，无需后续操作。
- 时间复杂度分析：最好时间复杂度O(n)，对应原始序列有序；平均和最差时间复杂度O(n^2)。
- 空间复杂度：O(1)，原地排序。
- 稳定性分析：当相邻两个元素的值相等时不交换位置，保证稳定性。
- 应用场景：数据量不大
- 实现
```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break
```

#### 4. 快速排序

- 原理：对于待排序序列中下标为p:r的一段数据，选择任意一个数据作为分区点pivot。遍历p:r之间的数据，小于pivot的放在左边，大于pivot的放在右边，pivot放在中间。再对p:q-1和q+1:r分别重复这个过程。对于将数组按照分区点左右划分的过程，可以使用两个数组分别存储小于pivot和大于pivot的数据，空间复杂度为O(n)。一种更加巧妙的做法是：遍历数组中的元素，若小于分区点则将其与数组的第i个元素交换（i初始化为0），i++，遍历完成后将a[i]与pivot交换（pivot一般取区间最后一个元素）。
- 时间复杂度分析：
    - 最好情况：每次分区极其平衡，时间复杂度为O(nlogn)
    - 最坏情况：原始序列正序或者逆序，选取最后一个元素为分区点，每次分区极其不平衡，时间复杂度为O(n^2)
    - 平均情况：时间复杂度为O(nlogn)
- 空间复杂度分析：O(1)，原地排序
- 稳定性分析：分区涉及元素交换，不稳定
- 应用场景：大数据量，对稳定性没有要求
- 实现
```python
def quick_sort(nums):
    _quick_sort(nums, 0, len(nums)-1)
def _quick_sort(nums, start, end):
    """对nums[start: end+1]进行快速排序"""
    if start < end:
        mid = _partition(nums, start, end)
        _quick_sort(nums, start, mid-1)
        _quick_sort(nums, mid+1, end)
def _partition(nums, start, end):
    """对nums[start: end+1]，以nums[end]为分界点，返回分界点所在索引"""
    pivot = nums[end]
    i = start
    for j in range(start, end):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[end] = nums[end], nums[i]
    return i
```
- O(n)时间复杂度内求无序数组的第K大元素
    - 算法：
        - 对无序数组nums选择最后一个元素nums[n-1]作为分区点，将大于分区点的数据划分到左边，小于分区点的数据划分到右边，分区点所在的下标为p。
        - 若p+1=k，则分区点为第K大元素；
        - 若p+1<k，则转换为在右边无序区间nums[p+1:]继续查找第(k-p-1)大元素；
        - 若p+1>k，则转换为在左边无序区间nums[:p]查找第k大元素
    - 时间复杂度分析：分区遍历次数分别为：n,n/2,n/4,...,1，和为2n-1，即为O(n)
    - 实现
```python
def get_Kth_largest(nums, k):
    return _get_Kth_largest(nums, 0, len(nums)-1, k)
def _get_Kth_largest(nums, start, end, k):
    if start < end:
        mid = _partition(nums, start, end)
        if mid+1 == k:
            return nums[mid]

        elif mid+1 > k:
            _get_Kth_largest(nums, start, mid-1, k)
        else:
            _get_Kth_largest(nums, mid+1, end, k)
def _partition(nums, start, end):
    """以nums最后一个元素为分区点，大于分区点的在左边，小于分区点的在右边"""
    pivot = nums[end]
    i = start
    for j in range(start, end):
        if nums[j] > pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[pivot] = nums[pivot], nums[i]
    return i
```

#### 5. 归并排序

- 原理：采用分治思想，将待排序序列平均分为两个子序列，分别对其进行排序，排序完成后再合并两个有序子数组，分为子序列排序和有序子序列合并两步。
- 时间复杂度分析：最好、最坏、平均情况下都为O(nlogn)
    - 假设对n个元素进行归并排序需要T(n)，对两个子序列进行归并排序需要2*T(n/2)，合并两个长度为n/2的有序数组花费O(n)
    - T(n)=2*T(n/2)+O(n)=2*(2*T(n/4)+O(n/2))+O(n)=4*T(n/4)+2n=8*T(n/8)+3n=(2^k)*T(n/(2^k))+kn
    - 当2^k=n时，k=logn，则T(n)=n+nlogn=O(nlogn)
- 空间复杂度分析：合并数组时需要临时数组，O(n)，不是原地排序算法。
- 稳定性分析：合并两个有序数组时，当其中有相同元素时，通过先将前面的元素复制到临时数组中，保证稳定性。
- 应用场景：大数据量排序，对存储空间没有要求
- 实现：
```python
def merge_sort(nums):
    """将待排序序列平均划分为两个子序列，分别排序后，再合并"""
    if len(nums) <= 1:
        return nums
    mid = len(nums)>>1
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)
def _merge(nums1, nums2):
    """合并两个有序数组"""
    nums = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    # 将剩下的数组添加到结果末尾
    nums.extend(nums1[i:])
    nums.extend(nums2[j:])
    return nums
```

#### 6. 堆排序

- 堆
    - 定义：堆是一个完全二叉树，堆中每一个节点的值，都必须大于等于或者小于等于其子树中每个节点的值。
    - 分类：每个节点的值都大于等于子树中节点值的堆叫做大顶堆，每个节点的值都小于等于子树中节点值的堆叫做小顶堆。大顶堆的堆顶元素为最大值，小顶堆的堆顶元素为最小值。
    - 存储：堆可以使用数组来存储，对于堆的操作就是对于数组中元素的操作。一般将根节点存储在下标为1的位置，则下标为i的节点的子节点为2i和2i+1，父节点为i//2。若堆顶元素存储在下标为0的位置，则第i个节点的子节点为2i+1和2i+2，父节点为(i-1)//2。
    - 操作：
        - 插入元素：O(logn)，将元素插入到数组尾部，堆中元素数量加一，对堆尾元素进行自下而上的堆化。
        - 删除堆顶元素：O(logn)，用数组末尾元素替换堆顶元素，堆中元素数量减一，对堆顶元素进行自上而下的堆化。
        - 获取堆顶元素：O(1)，返回堆顶元素即可
    - 应用场景：实现优先级队列、获取无序数组中的top-K，求无序数组的中位数和任意百分位数。
- 原理：（1）使用数组元素建立小顶堆，（2）依次取堆顶元素，并删除。
- 时间复杂度分析：建堆需要堆所有非叶子节点元素做自上而下的堆化，花费O(nlogn)，删除堆顶元素花费O(nlogn)，总时间复杂度为O(nlogn)
- 空间复杂度分析：O(1)，原地排序。
- 稳定性分析：堆化过程中涉及不相邻元素的交换，不稳定。
- 应用场景：
- 实现：
```python
def heap_sort(nums):
    n = len(nums)
    # 堆化非叶子节点，O(nlogn)
    for i in range((n-1)//2, -1, -1):
        heapify(nums, n, i)
    # 返回并删除堆顶元素，O(nlogn)
    for j in range(n-1, -1, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(nums, j, 0)
def heapify(nums, len, i):
    """从上往下堆化指定元素，O(logn)
    :param nums: 要堆化的堆
    :param len: 堆化时考虑的元素个数
    :param i: 要堆化的元素下标    
    """
    while True:
        max_index = i
        left_child, right_child = 2*i+1, 2*i+2
        if left_child <= len and nums[left_child] > nums[max_index]:
            max_index = left_child
        if right_child <= len and nums[right_child] > nums[max_index]:
            max_index = right_child
        if max_index == i:
            break
        nums[i], nums[max_index] = nums[max_index], nums[i]
        i = max_index
```

### 7. 计数排序 Counting Sort

- 原理思想：将待排序序列的元素转化为键存储在额外开辟的数组空间中，统计元素出现次数。
- 应用场景：输入数据为有确定范围的整数
    - 数据数量大，但是取值范围不大，存在相同元素。
    - 非负整数：对于其他类型数据，需要在不改变其相对大小的情况下，转换为非负整数。
- 步骤：
    1. 确定数据范围（最大值和最小值）
    2. 构造临时数组存储每个数据元素出现的次数
    3. 从前到后依次累加每个数据出现的次数
    4. 从后往前遍历原始数组，将其在临时数组中对应的值减1后作为下标存在一个新的临时数组中，同时原临时数组中相应的count值减1
    5. 将新的临时数组拷贝到原始数组
- 实现：
```python
def count_sort(nums):
    """计数排序
    适用于元素取值范围有限的输入数组。
    时间复杂度O(n)，空间复杂度O(n)
    按照元素取值范围划分，统计每个值的数量，拼接为最终结果。
    """
    # 确定数组范围
    num_max, num_min = max(nums), min(nums)
    # 统计元素个数
    count = [0] * (num_max - num_min + 1)
    for num in nums:
        count[num-num_min] += 1
    # 拼接结果
    res = []
    for i in range(len(count)):
        if count[i] != 0:
            res.extend([num_min+i] * count[i])
    return res
```
- 时间复杂度分析：假设输入元素数量为n，范围为k，统计元素数量O(n)，拼接结果O(k)，总时间复杂度为O(n+k)
- 空间复杂度分析：存储元素个数数组为O(k)，存储拼接结果数组为O(n)，总空间复杂度为O(n+k)，非原地排序
- 稳定性分析：稳定排序算法

### 8. 桶排序 Bucket Sort

- 原理：假设输入数据服从均匀分布，将输入数据区间划分为n个相同大小的子区间，再把输入数据划分到相应的桶里，每个桶内部单独排序。桶内排完序后，再把每个桶里面的数据按照顺序依次取出，组成序列。
- 步骤：
    1. 确定输入数据范围，根据桶数量划分桶区间；
    2. 将输入数据划分到相应的桶里面；
    3. 对每个桶单独排序；
    4. 拼接每个桶的排序结果。
- 实现：
```python
def bucket_sort(nums, bins=10):
    """桶排序，每个桶内部使用快速排序"""
    num_max, num_min = max(nums), min(nums)
    step = (num_max - num_min)//bins
    ans = [] * bins
    # 将元素划分到桶里面
    for i in range(len(nums)):
        bucket_index = (nums[i] - num_min) // step
        ans[bucket_index].append(nums[i])
    # 对每个桶做快排
    res = []
    for j in range(bins):
        quick_sort(ans[j])
        res.extend(ans[j])
    return res
```
- 时间复杂度分析：将要排序的n个数据均匀地划分到m个桶里面，每个桶里面有k=n/m个元素。每个桶内使用快速排序，时间复杂度为O(klogk)，m个桶的时间复杂度为O(mklogk)，即O(nlogk)，当m接近n时，将logk看作非常小的常量，这时桶排序的时间复杂度接近O(n)。
- 空间复杂度分析：当输入数据均匀分布时，m个桶的总的空间复杂度为O(n)，非原地排序
- 稳定性分析：稳定
- 应用场景：
    - 要排序的数据能够比较容易地划分为m个桶，而且桶之间存在天然的大小关系，如年龄、考试成绩、订单金额等。
    - 数据在各个桶之间的分布比较均匀。如果各个桶之间的分布非常不均匀，那桶内数据排序的时间复杂度就不再是常量级的了。而如果全部数据划分到一个桶内这种极端情况下，桶排序就退化为O(nlogn)的排序算法了。
    - 桶排序适合应用在外部排序中：数据量大，无法一次性加载到内存中的情况。


### 9. 基数排序 Radix Sort

- 应用场景：
    - 排序数据可以分割出独立的“位”进行比较，而且位之间有递进的关系，比如字符串、手机号码、单词
    - 每一位的数据范围不能过大，要可以使用线性排序算法来排序
- 实现方法：
    1. 对于不等长的排序数据，需要补齐到相同长度，如英文单词后面补0
    2. 将要排序的数据先按照最后一位来排序，再按照倒数第二位来排序，依此类推，最后按照第一位来排序
    3. 可以使用桶排序、计数排序等线性稳定性排序算法对每一位进行排序
- 时间复杂度分析：假设一共有k位，每位最多有n个元素取值，时间复杂度为O(kn)
- 空间复杂度分析：O(n+k)
- 稳定性分析：稳定

### 10. leetcode 题目

- 剑指offer 51 数组中的逆序对 （两重循环、merge sort、树状数组）
- 493 翻转对 （merge sort）
- 1122 数组的相对排序 （计数排序）
- 242 有效的字母异位词（哈希表）
- 56 合并区间（排序）
