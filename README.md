# LeetCode
[TOC]

## 算法

### 1. Two Sum

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
```

创建一个字典`dic：target - nums[i] : i`，对列表进行遍历，如果`nums[i]`在`dic`中，则搜索成功。

```python
dic = {}
for i in range(len(nums)):
	if nums[i] in dic:
		return [dic[nums[i]], i]
	else:
		dic[target - nums[i]] = i
```

###2.Add Two Numbers

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```

```python
carry = 0
ans = cur = ListNode(0)
while l1 or l2 or carry:
	if l1:
    	carry += l1.val
    	l1 = l1.next
	if l2:
    	carry += l2.val
    	l2 = l2.next
	carry, val = divmod(carry, 10)
    cur.next = ListNode(val)
    cur = cur.next
    return ans.next
```

### 39. Combination Sum

```python
def dfs(nums, target, index, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return 
            for i in xrange(index, len(nums)):
                dfs(nums, target - nums[i], i, path + [nums[i]], res)
```

### 53. Maximum Subarray
https://en.wikipedia.org/wiki/Maximum_subarray_problem
以i为结束位置的最大子数组之和：$B_{i}$
索引为i的数组值：$A_{i+1}$
$ {\displaystyle B_{i+1}=max(A_{i+1},A_{i+1}+B_{i})} $

### 69
牛顿法开平方
牛顿迭代法：$ x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}\,$
求平方根可变为如下方程：$ y=x^{{2}}-n $
迭代公式为：$ {x}_{{k+1}}={\frac  {1}{2}}\left(x_{k}+{\frac  {n}{x_{k}}}\right),\quad k\geq 0,\quad x_{0}>0. $

### 160. Intersection of Two Linked Lists
`l1`,`l2`第二遍遍历时，如果有交点，则会相遇

### 169
majority element的个数超过半数，则排序后，中间值为所求。

### 174. Dungeon Game
从矩阵的最后一行开始求到该元素所需的hp，在一行中遍历时，继续逆序。
`need[j:j + 2]`中`need[j]`为当前元素下一行所需的hp，`need[j + 1]`为当前元素下一列所需的hp。

### 204

### 231
数为2的幂时，二进制时只有一位1，`n & n - 1`为零。

### 264


### 287
`O(1)`space and `O(n)`time的解：
`nums[a] = b`当做`a.next = b`，则数组长度为n+1且数组的值在1到n时，数组出现重复的数等效于链表出现环（第二次出现重复的数时，链表指针又指向该数的结点）。
选取两个指针，slow步长为1，fast步长为2。假设两个指针第一次相遇在第k步，环的长度为r，则`2k - k = nr,k = nr`。设链表的起始结点到环的起始结点距离为s，链表的起始结点到第一次相遇的结点距离为k。环的起始结点到第一次相遇的结点距离为m。则`s = k - m`。`s = nr - m = (n - 1)r + (r - m)`，`n = 1`时，一个指针从链表的起始结点出发，另一个结点从相遇的结点出发，步长都为1，第一次相遇的结点即为环的起始结点。

### 326
32位为3的幂，则是`3^19`的因子。`(3 ** 19) % n == 0`

### 342
1010101010101010101010101010101 (1431655765)
`num & num -1 == 0 and num & 1431655765 == num`

### 337. House Robber III
`f1(node)` 为以node为根结点的子树中可以抢的最大钱数（包含根结点）。
`f0(node)` 为以node为根结点的子树中可以抢的最大钱数（不包含根结点）。
则：
`f0(node) = f1(node.left) + f1(node.right)` 
`f1(node) = max( f0(node.left)+f0(node.right)+node.value, f0(node) )`.

### 338

### 345

### 406

### 442
`1 ≤ a[i] ≤ n`（n：数组长度），将`array[a[i]]`的值乘-1，~~数组出现正数，则该正数的索引出现两次~~（有些数组中有些数可能一次也没出现，也为正数）。判断`array[a[i]]`的值，为负，则是第二次检测到该索引，因此该索引出现两次。

### 448
`1 ≤ a[i] ≤ n`（n：数组长度），将`array[a[i]]`的值变为`-abs(array[a[i]])`，最后数组中值为正数的，说明该索引没有出现，即该索引对应的值没有出现。

### 453. Minimum Moves to Equal Array Elements
sum：列表之和；minNum：列表最小元素；n：列表长度
m：m次move；x：最终相同时的数

`sum + m * (n - 1) = x * n`；`x = minNum + m`
则`sum - minNum * n = m`

### 463
相邻两格不同，则含有一条边，周长加一。遍历将行的结果与列的相加。

### 496

### 540. Single Element in a Sorted Array
二分法判断的标准：先计算`mid`，`mid`与`mid ^ 1`为连续的（偶数位，奇数位）。当`mid`与`mid ^ 1`相等时，说明只出现一次的数出现在后部分，在`mid + 1`与`right`中继续搜索反之。

### 561
给定数组之和为定值，每个数对之间的相差越小，则每个数对中较小值之和最大。将数组排序之后，求和以2为步长，即为结果。

### 566

## 数据结构
### 栈

#### 20

### 树

#### 102:Binary Tree Level Order Traversal

```
def levelOrder(self, root):
   ans, level = [], [root]
   while root and level:
       ans.append([node.val for node in level])
       level = [kid for n in level for kid in (n.left, n.right) if kid]
   return ans
```

#### 637


