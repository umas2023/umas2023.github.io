


let str = 'xx2020-01-01yy';
let res = str.replace(/(\d{4})-(\d{2})-(\d{2})/,
  (match, p1, p2, p3) => { return p1 + '年' + p2 + '月' + p3 + '日'; });

console.log(res)