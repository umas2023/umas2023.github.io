function Person() {
  //构造函数体内的属性
  this.name = 'Jack'
}
// Person.prototype 原型 上的方法
Person.prototype = {
  a: function () {
    console.log('我是一个a方法')
  },
  b: function () { },
  // ...
}

var p = new Person()
console.log(p)
console.log(p.name)// Jack
p.a()// 我是一个a方法