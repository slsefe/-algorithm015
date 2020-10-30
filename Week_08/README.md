# 第八周学习笔记

## 一、位运算

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

## 二、布隆过滤器 bloom filter

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

## 三、LRU cache

### leetcode题目

- leetcode146 LRU cache （哈希表+双向链表）

## 四、排序算法

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
