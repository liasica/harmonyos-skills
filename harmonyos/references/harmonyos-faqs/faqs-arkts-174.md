---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-174
title: ArkTS是否支持Partial类型
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持Partial类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b72a0f62c703c43f8a673f1064e5410791743142e33a92344d04d1804e4c7fd
---

## 问题现象

ArkTS是否支持Partial类型，如何使用？

## 背景知识

Partial是TypeScript（简称TS）一个内置的泛型工具类型，作用是将目标类型的所有属性变为可选属性，即给每个属性添加?修饰符。

ArkTS是HarmonyOS应用的默认开发语言，在TS生态基础上做了扩展，是兼容TS/JavaScript（简称JS）生态的，因此也支持Partial。

HarmonyOS系统对TS/JS支持的详细情况见[兼容TS/JS的约束](../harmonyos-guides/arkts-migration-background.md#方舟运行时兼容tsjs)。

## 解决方案

假设声明了一个表示用户信息的接口User：

```ts
interface User {
  name: string;
  age: number;
  email: string;
}
```

在默认情况下，User类型的变量必须包含name、age、email三个属性，缺一不可，否则编辑器就会出现"Property 'xxx' is missing in type..."的报错提示。而使用Partial后，得到的新类型中的所有属性都会变为可选，此时PartialUser类型的变量可以只包含部分属性，甚至为空：

```ts
type PartialUser = Partial<User>;
let pUser: PartialUser = {
  name: 'Alice'
};
```

完整示例参考如下：

```ts
interface User {
  name: string;
  age: number;
  email: string;
}

@Entry
@Component
struct PartialDemo {
  build() {
    Column() {
      Button('Partial类型')
        .onClick(() => {
          type PartialUser = Partial<User>;
          let pUser: PartialUser = {
            name: 'Alice'
          };
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
