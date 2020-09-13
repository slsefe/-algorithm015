# 第三周学习笔记

## 1.递归

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

- leetcode题目：
    - 二叉树的前中后序遍历
    - 将有序数组转化为二叉搜索树
    - 爬楼梯
    - 括号生成
    - 翻转二叉树
    - 二叉树最大深度和最小深度
    - 二叉树序列化和反序列化
    - 二叉树的最近公共祖先
    - 从前序遍历和中序遍历序列构造二叉树

## 2.分治

- leetcode题目
    - pow(x,n)
    
## 3.回溯

- leetcode题目
    - 括号生成
    - 组合
    - 组合总和
    - 全排列
    - 全排列II
    - 子集
    - 电话号码的字母组合
    - N皇后