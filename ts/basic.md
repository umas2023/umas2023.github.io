# typescript基础语法

### 类型定义

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