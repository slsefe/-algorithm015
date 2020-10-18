# 第七周学习笔记

## 1. 字典树、前缀树 Trie

### 1.1 树的基本概念回顾
- 树的BFS和DFS
- 二叉搜索树

### 1.2 数据结构
字典树、Trie树，是一种树形结构，典型应用是用于统计和排序大量的字符串，经常被搜索引擎用于文本词频统计。
优点：最大限度减少无谓的字符串比较，查询效率比哈希表高。

### 1.3 基本性质
1. 结点本身不存完整单词
2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串
3. 每个结点的所有子结点路径代表的字符都不相同

### 1.4 核心思想
1. 用空间换时间
2. 利用字符串的公共前缀来降低查询时间

### 1.5 leetcode题目

- 208 中等 实现Trie
- 212 困难 单词搜索II Trie+回溯DFS

## 2. 并查集 disjoint set

### 2.1 适用场景

组合问题，快速判断两个对象是否在同一个集合中

### 2.2 基本操作

- makeSet(s)：建立一个新的并查集，其中包含s个单元素集合
- unionSet(x, y)：将元素x和元素y所在的集合进行合并，要求x和y所在的集合不相交，如果相交则不合并
- find(x)：找到元素x所在集合的代表，也用于判断两个元素是否位于同一个集合（两个元素位于同一个集合<==>两个元素所在集合的代表相同）

### 2.3 实现

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

### 2.4 leetcode题目

- 547 朋友圈 中等 DFS/BFS/并查集
- 200 岛屿数量 中等 BFS/DFS/并查集
- 130 被围绕的区域 中等

## 3. 高级搜索

### 3.1 基础搜索

1. 朴素搜索
2. 优化方向：去掉重复计算的过程（Fibonacci）、剪枝掉不合理的情况（生成括号问题）
3. 搜索方向
    - DFS
    - BFS
    - 双向搜索：从起点和终点同时BFS
    - 启发式搜索，A*算法：基于优先级队列按照优先级搜索

### 3.2 剪枝

- 爬楼梯
- 括号生成
- N皇后
- 有效的数独
- 解数独

### 3.3 双向BFS

- 单词接龙
- 最小基因变化

### 3.4 启发式搜索

- 二进制矩阵中的最短路径
- 滑动谜题
- 解数独

## 4. AVL树与红黑树

### 4.1 树

- 树
- 二叉树
- 二叉树的BFS和DFS
- 二叉搜索树的查找、插入和删除操作
- 平衡二叉树
    - 2-3树
    - AVL树
    - B+树
    - 红黑树

### 4.2 AVL树

1. 自平衡二叉搜索树
2. 引入平衡因子：左子树与右子树的高度之差，取值为{-1，0，1}，所有叶子节点的平衡因子为0，保证所有结点的平衡因子都在{-1,0,1}中

- 旋转操作：
    1. 左旋：右右子树->左旋
    2. 右旋：左左子树->右旋
    3. 左右旋：左右子树->左右旋 等价于 左右子树左旋得到左左子树，再右旋
    4. 右左旋：右左子树->右左旋

- 带有子树的旋转
- 不足：每个结点需要存储平衡因子，调整次数频繁

### 4.3 红黑树

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
