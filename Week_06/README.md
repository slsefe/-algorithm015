# 第六周学习笔记

## 递归 recursion

```python
# 1. recursion terminator
# 2. process current logic
# 3. drill down
# 4. restore current status if needed
```

## 分治 divide & conquer

```python
# 1. recursion terminator
# 2. split current problem into several sub-problems
# 3. drill down: conquer sub-problems, merge sub-problems results
# 4. revert current level status if needed
```

## 动态规划 dynamic programming

- 本质是要解决一个分治或者递归问题，可以理解为动态递推

simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner.
dynamic programming = divide & conquer + optimal substructure
动态规划 = 分治 + 最优子结构

- 关键点
    - 动态规划和递归、分治没有根本的区别，关键是看问题有无最优的子结构。如果没有最优子结构，需要把所有子问题都进行计算，即为分治；如果存在最优子结构，中间过程只需保存最优子问题的解，即为动态规划。
    - 共性：找到重复子问题
    - 差异性：最优子结构、中途可以淘汰次优解

## 思维

- 寻找重复性，将复杂问题拆解为简单子问题
- 利用数学归纳法
- MIT 5 steps to DP, MIT五步DP法
    1. define sub-problems, 定义子问题
    2. guess part of solution, 递推公式
    3. merge sub-problem solutions, 合并子问题的解
    4. recurse & memorize or build DP table bottom-up, 自顶向下的递归+记忆化搜索 或者 自底向上的状态转移表
    5. solve original problem

## 题目

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
