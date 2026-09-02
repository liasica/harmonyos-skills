---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-localbuilder
title: "@LocalBuilder装饰器：维持组件关系"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > @LocalBuilder装饰器：维持组件关系
category: harmonyos-references
scraped_at: 2026-09-02T15:01:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e90d716c086af37b7df5c040fe7e62ed0cf321d02fac08a1c4c38fa969973bc6
---

@LocalBuilder拥有和局部[@Builder](ts-universal-builder-dynamic.md)相同的功能，且比局部@Builder能够更好地确定组件的父子关系和状态管理的父子关系。

开发指南见[@LocalBuilder装饰器：维持组件关系](../harmonyos-guides/arkts-localbuilder.md)。

**说明** 

* 本装饰器首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @LocalBuilder

const LocalBuilder: MethodDecorator

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
class ReferenceType {
  paramString: string = '';
}

@Entry
@Component
struct Parent {
  @State variableValue: string = 'Hello World';

  // 使用@LocalBuilder装饰器定义构建函数，维持组件的父子关系和状态管理的父子关系
  // 通过引用类型参数传递，可以监听到状态变量的变化
  @LocalBuilder
  citeLocalBuilder(params: ReferenceType) {
    Row() {
      Text(`UseStateVarByReference: ${params.paramString}`)
    }
  }

  build() {
    Column() {
      // 调用@LocalBuilder定义的构建函数，传入包含状态变量的引用类型参数
      this.citeLocalBuilder({ paramString: this.variableValue })
      Button('Click me')
        .onClick(() => {
          // 点击后修改状态变量的值，UI会自动刷新
          this.variableValue = 'Hi World';
        })
    }
  }
}
```
