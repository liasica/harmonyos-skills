---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-31
title: 如何实现类似插槽的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现类似插槽的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd6a04478a5c259eb4b839d9e8ec2b39413924cd253625b53cec5b2edd7fcccd
---

* ArkUI 提供了一种轻量的 UI 元素复用机制 @Builder。使用 @Builder装饰的函数需遵循 build()函数的语法规则。开发者可以将重复使用的 UI 元素抽象成一个方法，并在build方法中调用。
* ArkUI 引入了 @BuilderParam 装饰器，用于装饰指向 @Builder 方法的变量。开发者在初始化自定义组件时，可以对此属性进行赋值，为自定义组件增加特定功能。该装饰器用于声明任意 UI 描述的元素，类似于 slot 占位符。具体代码示例如下：

  ```typescript
  @Component
  struct Child {
    @Builder funABuilder0() {}
    @BuilderParam aBuilder0: () => void = this.funABuilder0;

    build() {
      Column() {
        this.aBuilder0()
      }
    }
  }

  @Entry
  @Component
  struct Parent {
    @Builder componentBuilder() {
      Text(`Parent builder `)
    }

    build() {
      Column() {
        Child({ aBuilder0: this.componentBuilder })
      }
    }
  }
  ```

**参考链接**

[@Builder装饰器：自定义构建函数](../harmonyos-guides/arkts-builder.md)

[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)
