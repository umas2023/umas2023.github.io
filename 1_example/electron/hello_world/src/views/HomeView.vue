<template>
  <div class="home">
    <h1>hello world</h1>
    <el-button type="danger" @click=testbutton>click</el-button>
  </div>
</template>

<script setup lang="ts">
const path = window.require("path");
const fs = window.require("fs");

const local_file = path.join(process.cwd(), "public/static/test.txt")
fs.readFile(local_file, 'utf-8',
  (err: any, data: any) => {
    if (err) {
      console.log("load config err:", err);
    } else {
      console.log(data)
    }
  }
);

const testbutton = () => {
  try {
    fs.writeFileSync(local_file, "文件被写入了");
  } catch (err) {
    console.error("config write error : " + err);
  }
}


</script>
