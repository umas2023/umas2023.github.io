const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  pages: {
    home: {
      entry: 'src/main.ts',
      template: 'public/index.html',
      filename: 'c99_inner.html'
    }
  }
})
