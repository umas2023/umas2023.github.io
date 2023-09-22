---
layout: post
title: 'css: fontawesome安装'
info: '在vue中使用有些麻烦，官网介绍不够详细，特此记录'
date: 2023-09-22 11:51:15  +0800
categories: ['css', 'vue']
toc: True
---

- 在vue中引入
  - https://fontawesome.com/docs/web/use-with/vue/add-icons


- npm
```bash
# core
npm i --save @fortawesome/fontawesome-svg-core

# Free icons styles
npm i --save @fortawesome/free-solid-svg-icons
npm i --save @fortawesome/free-regular-svg-icons
npm i --save @fortawesome/free-brands-svg-icons
```

- main.ts


```js
/* Set up using Vue 3 */
import { createApp } from 'vue'
import App from './App.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')

```

- vue
 
```js
/* add fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* add some free styles */
import { faTwitter } from '@fortawesome/free-brands-svg-icons'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faEnvelope } from '@fortawesome/free-regular-svg-icons'

/* add each imported icon to the library */
library.add(faTwitter, faUserSceret,faEnvelope)

// 注意每个icon都有solid/regular/light/duotone/thin的区别，引入时需要区分

```



<!-- ![引入图片]({{site.url}}/image/css/2023-09-20-bg_img/image_1.jpg) -->

{% raw %}
```
```
{% endraw %}
