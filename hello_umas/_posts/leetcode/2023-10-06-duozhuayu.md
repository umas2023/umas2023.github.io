---
layout: post
title: 'leetcode: 记某次笔试的5道题'
info: '据说这个公司每年都用这5道，所以不写公司名了'
date: 2023-10-06 16:14:24  +0800
categories: ['leetcode', 'python']
toc: True
---




## 1. Good Word  
字符串中出现最多的字符数量m  
字符串中出现最少的字符数量n  
m/n = 整数且>1
满足条件为Good Word 

- 暴力求解：创建了一个dic，记录所有字母出现的次数


```py
class Solution:
    def isGoodWord(self , word: str) -> bool:
        # write code here
        dic = {}
        for letter in word:
            dic[letter] = 1 if letter not in dic else dic[letter] + 1
            print(letter)
        ct = [dic[index] for index in dic ]
        maxn = max(ct)
        minn = min(ct)
        if maxn % minn ==0 and maxn/minn >1:
            return True
        return False


print(Solution().isGoodWord("duozhuayu"))
```



## 2. 升序链表合并

- 合并结果仍为升序链表


- 遍历就完了

```py
class ListNode:
    def __init__(self, x,next_node):
        self.val = x
        self.next:ListNode = next_node

class Solution:
    def merge_orders(self , a:ListNode , b:ListNode ) ->ListNode:
        # write code here
        ans = ListNode(0,None)
        pointer = ans
        while a and b:
            if a.val<=b.val:
                pointer.next = a
                a = a.next
            else:
                pointer.next = b
                b = b.next
            pointer = pointer.next
        if a:
            pointer.next = a
        if b:
            pointer.next = b
        return ans.next


ln1 = ListNode(1,ListNode(3,ListNode(5,None)))
ln2 = ListNode(2,ListNode(4,None))
ans = Solution().merge_orders(ln1,ln2)
print(ans.val)
print(ans.next.val)
print(ans.next.next.val)
print(ans.next.next.next.val)
print(ans.next.next.next.val)
```






## 3. 解压缩字符串  
aabb => a(2)b(2)  
aabbaabb => (a(2)b(2))2  
只出现一次的字母不压缩  

- 这里我下面写的程序通过率只有60%


- 暴力求解：创建了一个函数get_cp，返回每个前括号对应的后括号的位置（list形式）
- 本来应该在更新字符串时同步更新上面那个list，但有点错位懒得改了，每次循环都调用一遍get_cp

```py
class Solution:
    def decompress(self , compressed_str:str ):
        # write code here
        def get_cp(str_in):
            cp_index = [0] * len(compressed_str)
            stack = []
            for i,letter in enumerate(compressed_str) :
                if letter == "(":
                    stack.append(i)
                elif letter == ")":
                    cp_index[stack[-1]] = i
                    stack.pop()
            return cp_index

        cp_index = get_cp(compressed_str)
        while sum(cp_index):
            for i,cp in enumerate(cp_index) :
                if cp:
                    multi = int(compressed_str[cp+1])
                    compressed_str = compressed_str[0:i]+ compressed_str[i+1:cp] *multi +compressed_str[cp+2:len(compressed_str)]
                    cp_index = get_cp(compressed_str)
                    break
        return compressed_str

print(Solution().decompress("((a)2(b)2(c)2)2"))
# print(Solution().decompress("((a)2)2"))

```





## 4. 货架编号  
（类似N字排序，但没找到规律，所以还是用了暴力解法）  

等边直角三角形，左上起始，逆时针螺旋排序   

```
1 6 5
2 4
3
```

输入三角形维度，输出横向遍历排序结果

```
>> 3
<< [1,6,5,2,4,3]
```

- 在本子上写了几圈，没找到统一的规律，决定用暴力解法，新建n维空矩阵，三个函数fill_down、fill_rightup、fill_left分别向三个方向填入数据，循环到填满左上区域为止

- 这里通过率只有85%


```py
class Solution:
    def numberOfShelves(self , N ):
        # write code here
        mt = [[0]*N for _ in range(N)]
        def fill_down(num:int,pos1:int,pos2:int):
            if not mt[pos1][pos2] ==0:
                return num,pos1,pos2
            while mt[pos1][pos2] ==0 :
                mt[pos1][pos2] = num
                num +=1
                pos1 +=1
                if pos1>=len(mt) or pos2>=len(mt[len(mt)-1]):
                    pos1 -=1
                    return num,pos1,pos2
            pos1 -=1
            return num,pos1,pos2
        
        def fill_rightup(num:int,pos1:int,pos2:int):
            if not mt[pos1][pos2] ==0:
                return num,pos1,pos2
            while mt[pos1][pos2] ==0 :
                mt[pos1][pos2] = num
                num +=1
                pos1 -=1
                pos2 +=1
                if pos1>=len(mt) or pos2>=len(mt[len(mt)-1]):
                    pos1 +=1
                    pos2 -=1
                    return num,pos1,pos2
            pos1 +=1
            pos2 -=1    
            return num,pos1,pos2
        
        def fill_left(num:int,pos1:int,pos2:int):
            if not mt[pos1][pos2] ==0:
                return num,pos1,pos2
            while mt[pos1][pos2] ==0 :
                mt[pos1][pos2] = num
                num +=1
                pos2 -=1
                if pos1>=len(mt) or pos2>=len(mt[len(mt)-1]):
                    pos2 +=1
                    return num,pos1,pos2
            pos2 +=1
            return num,pos1,pos2
        
        num,pos1,pos2 = 1,-1,0
        while True:
            num0 = num
            num,pos1,pos2 = fill_down(num,pos1+1,pos2)
            num,pos1,pos2 = fill_rightup(num,pos1-1,pos2+1)
            num,pos1,pos2 = fill_left(num,pos1,pos2-1)

            

            if num == num0:
                break
            if pos1 < 0 or pos2 <0:
                break

        ans = []
        for i in mt:
            ans += i

        for line in mt:
            print(line)

        return [x for x in ans if not x ==0]

print(Solution().numberOfShelves(10))


```




## 5. BGP树
- 2^N字符串由01构成
- 字符串中全为0，节点value设为B
- 全1为P
- 都有为G
- 判定完当前节点后将字符串等分两半继续判定，到字符串无法二分为止
- 输出二叉树后序遍历结果

```
"10001101"
"PBGBBBGPPPBPGGG"
```

- 这题显然是有规律可循的，题解里都没给TreeNode定义
- 但还是写了个暴力解法


```py
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left:TreeNode = None
        self.right:TreeNode = None

class Solution:
    def bpg(self , s ):
        # write code here

        def bpg_str(bpgs):
            '''判断BPG'''
            if not "1" in bpgs:
                return "B"
            elif not "0" in bpgs:
                return "P"
            else:
                return "G"
            
        def create_tn(tns):
            '''生成二叉树'''
            print(tns)
            
            tnp = TreeNode(bpg_str(tns))
            if not len(tns) == 1:
                tnp.left = create_tn(tns[:int(len(tns)/2)])
                tnp.right = create_tn(tns[int(len(tns)/2):])
            return tnp
        
        def traverse(root:TreeNode):
            '''遍历'''
            if root == None:
                return ''
            ans = ''
            if not root.left == None:
                ans += traverse(root.left)
            if not root .right == None:
                ans += traverse(root.right)
            ans += root.val
            return ans

        return traverse(create_tn(s))

    

print(Solution().bpg("10001101"))
```



<!--![引入图片]({{site.url}}/image/leetcode/2023-10-06-duozhuayu/image_1.jpg) -->

