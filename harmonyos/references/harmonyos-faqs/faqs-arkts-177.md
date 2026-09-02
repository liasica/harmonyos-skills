---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-177
title: 如何解决ArkUI.Lite开发穿戴应用时异步任务不生效问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何解决ArkUI.Lite开发穿戴应用时异步任务不生效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:791129920aaacb542295ae6df56689fbf07378c4550e24fc96de7f2fb6475538
---

## 问题现象

采用兼容JS的类Web开发范式（ArkUI.Lite）开发穿戴应用时，在app.js的onCreate()中调用异步函数向服务器请求数据，发现异步函数不生效。

问题代码示例参考如下：

```java
// app.js
export default {
  data: {
    mockData: {},
    isDataReady: false
  },
  onCreate() {
    console.info('app.js -> AceApplication onCreate');
    this.fetchDataAsync().then((data) => {
      console.info('app.js -> 同步数据完成');
      this.data.mockData = data;
      this.data.isDataReady = true;
    })
  },
  onDestroy() {
    console.info('app.js -> AceApplication onDestroy');
  },
  fetchDataAsync() {
    return new Promise((resolve, reject) => {
      console.info('app.js -> 开始同步数据');
      // 用setTimeout模拟网络延迟（1.5秒后完成）
      setTimeout(() => {
        const mockData = {
          value: '123'
        };
        resolve(mockData);
      }, 1500);
    })
  }
}
```

控制台只输出了“开始同步数据”的日志，then()中的代码并没有执行：

```log
I     app.js -> AceApplication onCreate
I     app.js -> 开始同步数据
```

## 背景知识

[JS语法参考](../harmonyos-references/js-lite-framework-syntax-js.md)：JS文件用来定义HML页面的业务逻辑，支持ECMA规范的JavaScript语言。

## 问题定位

查看官网文档确认是否系统能力是否支持。根据官网文档描述轻量级智能穿戴支持的ES6语法有限，而Promise/async/await不在支持范围内，因此无法使用。

## 分析结论

轻量级智能穿戴支持的ES6语法有限，不支持Promise/async/await等ES6语法。

## 修改建议

使用callback的方式实现异步操作。

```java
// app.js
export default {
  data: {
    mockData: {},
    isDataReady: false
  },
  onCreate() {
    console.info('app.js -> AceApplication onCreate');
    this.fetchData((result, error) => {
      if (result) {
        console.info('app.js -> callback方式同步数据完成');
        console.info(`index.js -> ${JSON.stringify(this.data.mockData)}`);
        console.info(`index.js -> ${this.data.isDataReady}`);
      }
    })
  },
  onDestroy() {
    console.info('app.js -> AceApplication onDestroy');
  },
  fetchData(callback) {
    console.info('app.js -> 开始同步数据');
    // 用setTimeout模拟网络延迟（1.5秒后完成）
    setTimeout(() => {
      const mockData = {
        value: '123'
      };
      this.data.mockData = mockData;
      this.data.isDataReady = true;
      callback(mockData, null);
    }, 1500);
  }
}
```
