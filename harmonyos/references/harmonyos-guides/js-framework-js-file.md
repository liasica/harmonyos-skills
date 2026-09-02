---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-js-file
title: app.js
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 框架说明 > app.js
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d57817df81d5671964c893d5ebeac25c02ad1495722058a01590303138f034a1
---

## 应用生命周期

每个应用可以在app.js自定义应用级[生命周期](js-framework-lifecycle.md)的实现逻辑，以下示例仅在生命周期函数中打印对应日志：

```js
// app.js
export default {
    onCreate() {
        console.info('Application onCreate');
    },

    onDestroy() {
        console.info('Application onDestroy');
    },
}
```

## 应用对象6+

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| getApp | Function | 提供getApp()全局方法，可以在自定义js文件中获取app.js中暴露的对象。 |

示例如下：

```js
// app.js
export default {
    data: {
        test: "by getApp"
    },
    onCreate() {
        console.info('AceApplication onCreate');
    },
    onDestroy() {
        console.info('AceApplication onDestroy');
    },
}
```

```js
// test.js 自定义逻辑代码
export var appData = getApp().data;
```
