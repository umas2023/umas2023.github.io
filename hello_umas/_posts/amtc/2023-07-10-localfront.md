---
layout: post
title: 'amtc: localfront本地前端开发记录'
info: '学习工厂上班，记录开发中遇到的问题和解决（持续更新）'
date: 2023-07-10 14:48:43  +0800
categories: ['amtc','vue','raspberry_pi']
toc: True
---




## tableData类型定义

- 在导入网络设备的表格时，除了json中定义好的静态参数外，设备状态是由函数实时更新的，这时需要给tableData添加新的属性"status"

{% raw %}
```js
const tableData= ref(assets_json["network"])
tableData.value[id]["status"] = "offline"
```
{% endraw %}

- 但因为tableData在赋值时assets_json["network"]中并没有"status"属性，所以会报错：元素隐式具有 "any" 类型，因为类型为 ""status"" 的表达式不能用于索引类型
- 需要给tableData添加类型定义

{% raw %}
```js
interface TableDataItem {
        id:string;
        name:string;
        description:string;
        mac:string;
        ip:string;
        port:string
        status: string;
}
type TableData = TableDataItem[];
const tableData: Ref<TableData> = ref(assets_json["network"] as TableData)
```
{% endraw %}



## 获取网络设备状态

- 前端没有找到合适的ping函数，所以给后端添加了一个新的test接口，直接返回hello
- 前端用一个定时器来循环获取延时

{% raw %}
```js
// 后端连通性检查
const check_status = () => {
    console.log("refresh status ...")
    for (let id in tableData.value) {

        let start_time = Date.now()
        const res = (msg: string) => {
            tableData.value[id]["status"] = JSON.stringify(Date.now() - start_time) + "ms"
        }
        const err = (msg: string) => {
            console.log(msg)
            tableData.value[id]["status"] = "error"
        }

        let asset = tableData.value[id]
        // let ip = "http://"+asset["ip"]+":4090/"
        let ip = "http://localhost:4090/"
        opc_connect(ip, "test", res, err)
    }
}
```
{% endraw %}


{% raw %}
```js
onMounted(() => {
    for (let id in tableData.value) {
        (tableData.value[id] as { status: string }).status = 'offline';
        tableData.value[id]["status"] = "offline"
    }
    // 设置定时器检查后端连通状态
    let time_interval = 3000
    let set_id = setInterval(check_status, time_interval)
})
```
{% endraw %}



## 表格文本颜色

- 想给offline红色，online绿色，但是element ui提供的表格方法中没有对单个单元格的操作，默认格式是这样的：

{% raw %}
```html
<el-table-column prop="status" label="Status" />
```
{% endraw %}

- 经过查找，有插槽可以调用

{% raw %}
```html
<el-table-column prop="status" label="Status">
    <template #default="scope">
        <span :class="scope.row.status == 'offline' ? 'red' : 'green'">{{ scope.row.status }}</span>
    </template>
</el-table-column>
```
{% endraw %}

{% raw %}
```scss
// 表格属性
span.red{
    color: red;
}
span.green{
    color: green;
}
```
{% endraw %}


## 全部资产列表

- 拼接network和factory分类，js拼接数组有很多方法，这里使用扩展运算符

{% raw %}
```js
interface TableDataItem {
    id: string;
    name: string;
    description: string;
}
type TableData = TableDataItem[];
const tableData: Ref<TableData> = ref([...assets_json["network"],...assets_json["factory"]] as TableData)
```
{% endraw %}












![引入图片]({{site.url}}/image/amtc/2023-07-10-localfront/image_1.jpg)

{% raw %}
```js
```
{% endraw %}
