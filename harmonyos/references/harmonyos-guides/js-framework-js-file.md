---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-js-file
title: app.js
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 框架说明 > app.js
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f42fe860f484118593cc1bbcb36134abb04600234e983bbabd374480ae4bdb96
---

## 应用生命周期

每个应用可以在app.js自定义应用级[生命周期](js-framework-lifecycle.md)的实现逻辑，以下示例仅在生命周期函数中打印对应日志：

```
1. // app.js
2. export default {
3. onCreate() {
4. console.info('Application onCreate');
5. },

7. onDestroy() {
8. console.info('Application onDestroy');
9. },
10. }
```

## 应用对象6+

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| getApp | Function | 提供getApp()全局方法，可以在自定义js文件中获取app.js中暴露的对象。 |

示例如下：

```
1. // app.js
2. export default {
3. data: {
4. test: "by getApp"
5. },
6. onCreate() {
7. console.info('AceApplication onCreate');
8. },
9. onDestroy() {
10. console.info('AceApplication onDestroy');
11. },
12. }
```

```
1. // test.js 自定义逻辑代码
2. export var appData = getApp().data;
```
