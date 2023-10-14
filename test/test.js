function myCall(fn, context) {
  if (typeof fn !== 'function') {
    throw new TypeError('myCall 只能用于函数');
  }

  // 创建一个唯一的属性名
  const propertyName = '__myCall__';

  // 将函数赋值给上下文对象的属性
  context[propertyName] = fn;

  // 使用属性名调用函数并获取结果
  const result = context[propertyName]();

  // 删除临时属性
  delete context[propertyName];

  return result;
}

// 示例用法
function greet() {
  console.log(`Hello, ${this.name}!`);
}

const person = { name: 'John' };

myCall(greet, person);