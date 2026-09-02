---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-wrapbuilder
title: wrapBuilder
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > wrapBuilder
category: harmonyos-references
scraped_at: 2026-09-02T15:01:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a698c6d1da05b98ee4fa806978837a88c3299e91bbb35fde71c06987f980930c
---

wrapBuilder用于封装全局[@Builder](ts-universal-builder-dynamic.md#builder)，可以将全局@Builder函数作为参数传递，实现按引用传递和动态调用，提升代码复用性。

开发指南见：[wrapBuilder：封装全局@Builder](../harmonyos-guides/arkts-wrapbuilder.md)。

**说明** 

* 本模块首批接口从API version 11开始支持。
* 本模块接口仅可在Stage模型下使用。
* 后续版本的新增接口，采用上角标单独标记接口的起始版本。

## wrapBuilder

wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>

wrapBuilder是一个模板函数，返回一个WrappedBuilder对象。模板参数Args extends Object[]是需要封装的@Builder函数的参数列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | (...args: Args) => void | 是 | @Builder装饰的全局函数，传入后将被封装为WrappedBuilder对象。函数参数args为该@Builder函数所需的参数列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WrappedBuilder<Args>](ts-universal-wrapbuilder.md#wrappedbuilder) | @Builder函数的包装类对象，用于将全局@Builder函数及其参数封装为可按引用传递、支持动态调用的对象。 |

**示例：**

```ts
@Builder
function myBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}

// 使用wrapBuilder封装myBuilder
let builderVar: WrappedBuilder<[string, number]> = wrapBuilder(myBuilder);
```

## WrappedBuilder

WrappedBuilder是@Builder函数的包装类，用于封装全局@Builder函数及其参数，实现按引用传递和动态调用。模板参数Args extends Object[]应传入@Builder函数的参数类型列表。

### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | (...args: Args) => void | 否 | 否 | @Builder装饰的全局函数。 |

### constructor

constructor(builder: (...args: Args) => void)

WrappedBuilder的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | (...args: Args) => void | 是 | @Builder装饰的全局函数，作为构造参数用于初始化WrappedBuilder实例。函数参数args为该@Builder函数所需的参数列表。 |

**示例：**

```ts
@Builder
function myBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}

// 使用WrappedBuilder封装myBuilder
let builderVar: WrappedBuilder<[string, number]> = new WrappedBuilder<[string, number]>(myBuilder);
```
