---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-wrapbuilder
title: wrapBuilder
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > wrapBuilder
category: harmonyos-references
scraped_at: 2026-04-29T13:52:56+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2ea6b0e510659c2336f38ac5d4289fde3e1e9f85a6204dacc54a2eb208e36882
---

使用wrapBuilder封装全局@Builder，可以帮助维护代码。开发指南见[wrapBuilder：封装全局@Builder](../harmonyos-guides/arkts-wrapbuilder.md)。

说明

本模块首批接口从API version 11开始支持。

后续版本的新增接口，采用上角标单独标记接口的起始版本。

## wrapBuilder

PhonePC/2in1TabletTVWearable

wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>

wrapBuilder是一个模板函数，返回一个WrappedBuilder对象。模板参数Args extends Object[]是需要包装的builder函数的参数列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | (...args: Args) => void | 是 | @Builder装饰的全局函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WrappedBuilder<Args>](ts-universal-wrapbuilder.md#wrappedbuilder) | WrappedBuilder对象。 |

**示例：**

```
1. @Builder
2. function MyBuilder(value: string, size: number) {
3. Text(value)
4. .fontSize(size)
5. }
6. // 使用wrapBuilder封装MyBuilder
7. let builderVar: WrappedBuilder<[string, number]> = wrapBuilder(MyBuilder);
```

## WrappedBuilder

PhonePC/2in1TabletTVWearable

@Builder函数的包装类。模板参数Args extends Object[]应传入@Builder函数的参数类型列表。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| builder | (...args: Args) => void | 否 | 否 | @Builder修饰的全局函数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(builder: (...args: Args) => void)

WrappedBuilder的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | (...args: Args) => void | 是 | @Builder装饰的全局函数。 |

**示例：**

```
1. @Builder
2. function MyBuilder(value: string, size: number) {
3. Text(value)
4. .fontSize(size)
5. }
6. // 使用WrappedBuilder封装MyBuilder
7. let builderVar: WrappedBuilder<[string, number]> = new WrappedBuilder<[string, number]>(MyBuilder);
```
