---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-decorator-extend
title: "@Extend：扩展组件样式"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > @Extend：扩展组件样式
category: harmonyos-references
scraped_at: 2026-09-02T15:01:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6881f1b2a1509675f50c55d3ed21cdd1d6f22fd16737ff1c55e6131ea6c74a5c
---

@Extend装饰器用于扩展指定组件的样式，支持在装饰的函数中统一定义多个样式属性，并可通过参数传递实现样式的灵活复用，适用于需要将相同样式应用到多个组件、减少样式代码重复的场景。

开发指南参考：[@Extend装饰器：定义扩展组件样式](../harmonyos-guides/arkts-extend.md)。

**说明** 

* 本装饰器首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @Extend

const Extend: MethodDecorator & ((value: any) => MethodDecorator)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | any | 是 | 指定要扩展样式的目标内置UI组件类型（如Text、Column），传入组件的类型而非组件实例，不支持自定义组件。@Extend装饰器内定义的样式属性将绑定到该组件类型，使其可在该组件上以链式方式调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MethodDecorator | 方法装饰器，开发者无需关注该返回值。 |

**示例：**

```ts
@Extend(Text)
function fancy(fontSize: number) {
  .fontColor(Color.Red)
  .fontSize(fontSize)
}

@Entry
@Component
struct FancyUse {
  build() {
    Row({ space: 10 }) {
      Text('Fancy')
        .fancy(16)
      Text('Fancy')
        .fancy(24)
    }
  }
}
```
