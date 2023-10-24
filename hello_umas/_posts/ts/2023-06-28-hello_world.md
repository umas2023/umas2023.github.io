---
layout: post
title:  "ts: hello_world TypeScript基本语法"
info: "TypeScript基本语法之类型定义"
date:   2023-06-28 09:50:00 +0800
categories: ts
toc: true
---



## 类型定义

- 基本类型定义

{% raw %}
```ts
let title:string = '张三'
let total:undefined = undefined
let arr:number = [1, 2, 3]
let arr:Array<number> = [1, 2, 3]
let arr: [string, number] = ['张三', 18]

type Gender = 1 | 2;
let boy:Gender = 1;
let girl:Gender = 2;

interface Props {
  name: string,
  age: number
}
let obj: Props = {
  name: '张三',
  age: 18
}
```
{% endraw %}



- 函数类型

```js
// 一个inject的例子
const body_box_init: () => void = inject("body_box_init")!
```


- vue的ref类型
{% raw %}
```ts
import type {Ref} from "vue"
flag: Ref<boolean>
```
{% endraw %}


- 定义函数返回值
{% raw %}
```ts
function todo(a: number): number {
  return a
}
function todo(a: number): void {
  console.log(a)
}
function demo(): never {
  throw new Error('出错了')
}
```
{% endraw %}


- 类型断言
{% raw %}
```ts
let a:number|string;
console.log((a as number).toFixed(2))
console.log((<number>a).toFixed(2))
```
{% endraw %}


- 键值对类型定义
- 元素隐式具有 "any" 类型，因为类型为 "string" 的表达式不能用于索引类型 "{}"。
```js
const store_config = ref({})
store_config.value[key] = ... // 这里报错
// 修改后:
const store_config: { [key: string]: any } = ref({})
```
```js
var state: {    config: {}  }
state.config[key] = ... // 这里报错
// 修改后:
var state: {    config: {} as { [key: string]: any }   }
```


## 报错及解决

---
> 元素隐式具有 "any" 类型，因为类型为 "string" 的表达式不能用于索引类型 "{}"。

- 直接定义一个对象，[item]索引具有any属性
{% raw %}
```js
const store_config = ref({})

for (let item in data) {
    store_config.value[item] = data[item]["value"]
}
```
{% endraw %}

- 添加这样的定义
{% raw %}
```ts
const store_config: { [key: string]: any } = ref({})
```
{% endraw %}

---
> TS 对象可能为“未定义”，不能将类型“ XXXX \| undefined “分配给类型{ xxxx }

- 使用感叹号表示这个元素不会为undefined

{% raw %}
```js
props.setting_index!.classList.add("animate__backOutRight")
```
{% endraw %}

- 父组件定义是这样的

{% raw %}
```js
const main_index = ref<HTMLDivElement>()
```
{% endraw %}

- 使用问号表示是可选属性，也可能为undefined

{% raw %}
```js
const props = defineProps<{
    main_index?: HTMLDivElement,
    setting_index?: HTMLDivElement
}>();
```
{% endraw %}


---
> 类型为 "string" 的表达式不能用于索引类型xxx

- 报错在page_list[label_select.value]
{% raw %}
```js
const page_list = {
    BrowserIndex: defineAsyncComponent(() => import("./components/app_img_browser/BrowserIndex.vue")),
    AutoIndex: defineAsyncComponent(() => import("./components/app_auto_click/AutoIndex.vue"))
}

const go_page = () => {
    page_select.value = page_list[label_select.value]
}
```
{% endraw %}


- 修改为
{% raw %}
```js
const go_page = () => {
    console.log(label_select.value)
    page_select.value = page_list[label_select.value as keyof typeof page_list]
}
```
{% endraw %}

---
> 类型“Element”上不存在属性“style

- 问题出现
{% raw %}
```js
document.querySelector(".show-log-body")!.style.cssText += " transition: 0s"
```
{% endraw %}

- 因为querySelector返回值类型是Element，应该改成HTMLElement

{% raw %}
```js
const body_div = document.querySelector<HTMLElement>(".show-log-body")!
```
{% endraw %}





