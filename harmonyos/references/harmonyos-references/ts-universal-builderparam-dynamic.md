---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-builderparam-dynamic
title: "@BuilderParam装饰器：引用@Builder函数"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > @BuilderParam装饰器：引用@Builder函数
category: harmonyos-references
scraped_at: 2026-09-02T15:01:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3ceeef61b15a25d3b4ebbaab53c9d7a1a992d1a6d82bb4b1de5257f817051f0a
---

@BuilderParam用于装饰指向[@Builder](ts-universal-builder-dynamic.md)函数的变量，使自定义组件能够接收外部传入的@Builder函数，实现UI内容的自定义渲染。适用于需要将父组件的UI构建逻辑传递给子组件、实现组件内容动态定制的场景。

开发指南参考：[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)。

**说明** 

* 该装饰器从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @BuilderParam

const BuilderParam: PropertyDecorator

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ts
@Component
struct Child {
  @Builder
  customBuilder() {
  }

  // 使用@BuilderParam装饰器声明一个指向@Builder函数的变量
  // 类型为无参无返回值的函数，默认值为子组件内部的customBuilder
  @BuilderParam customBuilderParam: () => void = this.customBuilder;

  build() {
    Column() {
      // 调用@BuilderParam引用的构建函数来渲染UI
      this.customBuilderParam()
    }
  }
}

@Entry
@Component
struct Parent {
  @Builder
  componentBuilder() {
    Text(`Parent builder`)
  }

  build() {
    Column() {
      // 创建子组件Child，将父组件的componentBuilder传入customBuilderParam
      Child({ customBuilderParam: this.componentBuilder })
    }
  }
}
```
