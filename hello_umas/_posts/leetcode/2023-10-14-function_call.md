---
layout: post
title: 'leetcode: 58笔试'
info: '字符查找、斐波那契、中文数字转换'
date: 2023-10-14 21:00:04  +0800
categories: ['leetcode', 'js']
toc: True
---

- 依旧是算法题不难，选择题逆天
- 因为是第一次用js写算法题，所以记录一下



## 知识总结

- 哈希表，动态规划


## 查找出现次数最多的字符

{% raw %}
```js



// 查找字符串中出现次数最多的字符
// 可能有多个重复字符

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 返回给定字符串中出现频率最高的字符
 * @param str string字符串 给定的字符串
 * @return string字符串一维数组
 */
function findChar(str) {
    // write code here
    let charCount = {}
    for (let chr of str) {
        if(charCount[chr]){
            charCount[chr] += 1
        } else{
            charCount[chr] = 1
        }

    }
    maxList = [str[0]]
    for(let chr in charCount){
        if (charCount[chr] > charCount[maxList[0]] ){
            maxList = [chr]
        } 
        else if((charCount[chr] == charCount[maxList[0]]) && chr!=maxList[0] ){
            maxList.push(chr)
        }
    }
    return maxList
}
module.exports = {
    findChar: findChar
};


findChar("asdfghjklaqwertyuiopiaia135")


```
{% endraw %}



## 斐波那契数列

- 使用递归法超时了，改用迭代（动态规划）


{% raw %}
```js


// 斐波那契数列


/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 返回斐波那契数列第n项的数字
 * @param n long长整型 数列中的第n项
 * @return long长整型
 */
function fib(n) {

    // 递归法超时
    // if(n<=1){
    //     return 1
    // }
    // return fib(n-1) + fib(n-2)


    // 试试迭代
    if (n <= 1) {
        return 1
    }

    let pre = 1;
    let cur = 1;
    for(let i = 2;i<=n;i++){
        let next = pre + cur
        pre = cur
        cur = next
    }
    return cur


}
module.exports = {
    fib: fib
};


console.log(fib(5))

```
{% endraw %}


<!--![引入图片]({{site.url}}/image/leetcode/2023-10-14-function_call/image_1.jpg) -->



## 中文转数字

- 这题比较有意思
- 关键在于对零的判断

```
输入 "二百零五万三千三百三十三"
输出 2053333
```

- 通过率只有85%，没有找到问题

```js


// 中文转数字

// "二百零五万三千三百三十三"
// 2053333

// 通过率85%



/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 请实现一个将中文数字转换为阿拉伯数字的方法
 * @param chineseNumber string字符串 中文数字字符串
 * @return int整型
 */
function chineseToNumber(chineseNumber) {
    // write code here
    const numberMap = {
        零: 0,
        一: 1,
        二: 2,
        三: 3,
        四: 4,
        五: 5,
        六: 6,
        七: 7,
        八: 8,
        九: 9,
        十: 10,
        百: 100,
        千: 1000,
        万: 10000
    }
    let ansNumber = 0
    let curNumber = 0
    let lastNumber = 0
    for (let cnNum of chineseNumber) {
        let intNum = numberMap[cnNum]
        if (intNum < 10) {
            curNumber += intNum
            // 一万零二这种情况
            if (intNum === 0) {
                curNumber = ansNumber
                ansNumber = 0
            }
            // 一万零二十这种情况要记住二，再在下面处理十
            if (curNumber > 10) {
                lastNumber = intNum
            }
        }
        else {
            if (curNumber == 0) {
                // "十七"这种情况
                if (intNum == 10) {
                    curNumber = 10
                }
                // 一千万这种情况
                else if (intNum == 10000){
                    ansNumber *= 10000
                }

            }
            // 处理一万零二十的十
            else if ((lastNumber != 0) && intNum <= 1000) {
                ansNumber = curNumber - lastNumber
                curNumber = lastNumber * intNum
                ansNumber += curNumber
                curNumber = 0
                lastNumber = 0
            }
            else {
                curNumber *= intNum
                ansNumber += curNumber
                curNumber = 0
                lastNumber = 0
            }
        }
        console.log(cnNum, curNumber, ansNumber)
    }
    return curNumber + ansNumber
}
module.exports = {
    chineseToNumber: chineseToNumber
};


// console.log(chineseToNumber("二百零五万三千三百三十三"))
// console.log(chineseToNumber("一万零二"))
// console.log(chineseToNumber("一万零二十"))
// console.log(chineseToNumber("一千万"))
// console.log(chineseToNumber("一千万零一百"))
console.log(chineseToNumber("一千零一万零一十一"))


```