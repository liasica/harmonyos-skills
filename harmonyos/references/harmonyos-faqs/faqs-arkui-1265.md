---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1265
title: 如何解决LocalStorage存储function报错问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决LocalStorage存储function报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:11db424d6be5175afc638ea2683a3c59c69d3713fcf8f5f53d8e389831e89d7c
---

## 问题现象

使用LocalStorage传递function报错：

```screen
Error message:@Component 'owning @Component UNKNOWN': Illegal variable value error with decorated variable undefined 'clickSend': failed validation: 'undefined, null, number, boolean, string, or Object but not function, not V2 @ObservedV2 / @Trace class, and makeObserved return value either, attempt to assign value type: 'function', value: 'undefined'!
```

关键问题参考如下：

```screen
function openCommentsInput(title: string, hintMsg: string, clickSend: Function = (content: string) => {}) {
  let storage: LocalStorage = new LocalStorage();
  storage.setOrCreate('title', title)
  storage.setOrCreate('hintMsg', hintMsg)
  storage.setOrCreate('clickSend', clickSend) // 程序崩溃，报错
}
```

## 背景知识

[LocalStorage](../harmonyos-guides/arkts-localstorage.md)是页面级的UI状态存储，存储的类型有所限制。

## 问题定位

查看以下报错日志的关键信息可知，clickSend是非法变量值，支持undefined、null、number、boolean、string、Object等类型，但不支持function函数类型变量。

```screen
Illegal variable value error with decorated variable undefined 'clickSend': failed validation: 'undefined, null, number, boolean, string, or Object but not function ...'
```

## 分析结论

LocalStorage不支持存储function函数类型变量。

## 修改建议

使用类class将函数function进行封装为Object对象，LocalStorage支持存储Object对象。

```screen
let storage: LocalStorage = new LocalStorage();

function openCommentsInput(title: string, hintMsg: string, clickSend: object) {
  storage.setOrCreate('title', title);
  storage.setOrCreate('hintMsg', hintMsg);
  storage.setOrCreate('clickSend', clickSend);
}

// 使用class对function进行一层封装
class MyFunc {
  clickSend: Function = () => {
  };
}

// 需要保存至LocalStorage的函数
function clickSend(ctx: string) {
  console.info(ctx);
}

@Entry(storage)
@Component
export struct LocalStorageDemo {
  @LocalStorageLink('clickSend') myFunc: object = []; // 获取LocalStorage中存储的clickSend对象

  build() {
    Column({ space: 20 }) {
      Button('向storage保存数据')
        .onClick(() => {
          let myFunc: MyFunc = new MyFunc();
          myFunc.clickSend = clickSend; // 将要保存的函数封装在class对象中
          openCommentsInput('title', 'hintMsg', myFunc); // 将class对象保存至LocalStorage
        });
      Button('读取storage的数据')
        .onClick(() => {
          let tmp = this.myFunc as MyFunc; // 将Object对象转为MyFunc类
          tmp.clickSend('读取storage的数据成功'); // 调用MyFunc中的clickSend函数
        });
    };
  }
}
```

运行截图如下：成功调用LocalStorage中存储的类对象的函数来打印数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Rnc9X2JTSiqZceAQrXHGoQ/zh-cn_image_0000002658835373.png "点击放大")
