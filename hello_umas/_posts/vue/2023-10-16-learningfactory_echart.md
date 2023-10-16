---
layout: post
title: 'vue: 学习工厂项目echart图表加载错误'
info: 'init函数重复调用会报错，图表无法加载'
date: 2023-10-16 13:43:44  +0800
categories: ['vue', 'amtc']
toc: True
---


- 学习工厂首页在搜索栏下面用onMounted加入了一张饼图


{% raw %}
```js
onMounted(() => {
    var chartDom = document.getElementById('chart-demo')!;
    var myChart = echarts.init(chartDom);
    ...
```
{% endraw %}


- 使用流程是展示搜索结果时隐藏饼图并在原位置展示搜索结果（把display设置为none），发现切换路由再返回后display保持为none
- 两种方法：进入子页面时 / 离开子页面时 把display重置为flex
- 查阅资料，对标onMounted有onBeforeUnmount可以处理离开当前子页面的操作
- 重新显示饼图后出现了新的问题，报警[ECharts] There is a chart instance already initialized on the dom.饼图不能显示，排查发现问题来自```var myChart = echarts.init(chartDom);```，init函数重复调用就会报错
- 查阅资料得到另一个函数echarts.getInstanceByDom，如果当前dom已经存在echart对象，应该用它来替代echats.init，所以这里也有两种处理方法：首先判断图表是否已经存在 / 或是在离开页面时销毁当前图表
- ↑选择了后者：



{% raw %}
```js
onBeforeUnmount(() => {
    console.log("unmount.......")
    // 初始化输入参数
    res_text.value = ""
    res_json.value = {}
    // 初始化图表显示
    let init_box = document.querySelector<HTMLElement>(".init-box")
    init_box!.style.display = "flex"
    // 销毁图表实例
    var chartDom = document.getElementById('chart-demo')!;
    var myChart = echarts.getInstanceByDom(chartDom);
    if (myChart) {
        myChart.dispose();
    }
})
```
{% endraw %}


{% raw %}
```
```
{% endraw %}

<!--![引入图片]({{site.url}}/image/vue/2023-10-16-learningfactory_echart/image_1.jpg) -->