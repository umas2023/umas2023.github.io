# 在style中使用v-bind

- style中引用script变量：
```scss
<script setup>
const theme = {
    color: "red",
};
</script>
    
<template>
    <p>hello</p>
</template>
    
<style scoped>
p {
    color: v-bind("theme.color");
}
</style>
```

- 加上"px"后缀，除了computed添加之外，还可以：
```scss
<style scoped>
p {
 font-size: calc(1px * v-bind(size));
}
</style>
```

- 也可以设置多个style组
```scss
<template>
 <p :class="classes1.red">This should be red</p>
</template>

<style module="classes1">
.red {
 color: red;
}
</style>

<style module="classes2">
.red {
 color: green;
}
</style>
```

