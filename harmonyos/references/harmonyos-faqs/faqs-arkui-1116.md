---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1116
title: 自定义装饰器实现示例
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义装饰器实现示例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:603673c5ca89d8837b879efc70e5da176825db5be9ba3ee0716628cf6701ec91
---

## 问题现象

如何在HarmonyOS中实现自定义装饰器？

## 背景知识

ArkTS本身没有自定义装饰器相关的内容，可以使用TS的自定义装饰器。

## 解决方案

以下是类装饰器、属性装饰器、方法装饰器、参数装饰器的简单示例：

```ts
@Entry
@Component
struct DecoratorDemo {
  @State address: string = '点我探索世界';

  build() {
    RelativeContainer() {
      Text(this.address)
        .fontSize(15)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.address = new ExploringWorld().TestFun('中国');
        });
    }
    .height('100%')
    .width('100%');
  }
}

// 类装饰器
function TestClassDecorator(target: Function) {
  if (target) {
  }
}

// 属性装饰器
function TestMemberDecorator(target: ExploringWorld, memberName: String) {
  if (target && memberName) {
  }
}

// 方法装饰器
function TestFunDecorator(target: ExploringWorld, propertyName: String, descriptor: PropertyDescriptor) {
  if (target && propertyName && descriptor) {
  }
}

// 参数装饰器
function TestArgDecorator(target: Function, methodName: String, paramIndex: Number) {
  if (target && methodName && paramIndex) {
  }
}

@TestClassDecorator
class ExploringWorld {
  @TestMemberDecorator
  count: number = 123;

  @TestFunDecorator
  TestFun(@TestArgDecorator param: string): string {
    if (param) {
      return '欢迎来到大美中国';
    } else {
      return '未知地点';
    }
  }
}
```

## 总结

ArkTS在TS基本语法风格的基础上，进一步通过规范强化静态检查和分析，使得在程序运行之前的开发期能检测出更多错误，提升代码的健壮性，并实现更好的性能，因此从TS迁移过来的代码需要进行人工检测修复，无法直接复用。

## 常见FAQ

Q：在自定义装饰器修饰的方法中访问状态变量，会报错Error message:Cannot read property get of undefined。

A：状态变量是组件内私有状态，仅能在所属组件内部访问，自定义装饰器无法绕过这一访问限制。
