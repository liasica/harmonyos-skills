---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang
title: @arkts.lang (ArkTS语言基础能力)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.lang (ArkTS语言基础能力)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:56+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:028ca2b0165ededf4b0955ac1a72d8848b74fc46bf72190362127e840177a0ed
---

本模块提供的ArkTS语言的基础类型定义。当前提供ISendable接口。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { lang } from '@kit.ArkTS';
```

## lang.ISendable

PhonePC/2in1TabletTVWearable

是所有[Sendable](../harmonyos-guides/arkts-sendable.md#基础概念)类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

ArkTS中，ISendable类型的对象是Object类型的实例，遵循其基本特征，同时支持跨线程传递。

ISendable主要用在开发者自定义Sendable数据结构的场景中，ArkTS语言标准库中的容器类型（如[Array](arkts-apis-arkts-collections-array.md)、[Map](arkts-apis-arkts-collections-map.md)、[Set](arkts-apis-arkts-collections-set.md)等）隐式地继承并实现了ISendable。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**示例：**

```
1. // 构造一个用户自定义的Sendable数据结构
2. @Sendable
3. class CustomData implements lang.ISendable {
4. data1: number;
5. data2: string;
6. constructor(data1: number, data2: string) {
7. this.data1 = data1;
8. this.data2 = data2;
9. }
10. }
```
