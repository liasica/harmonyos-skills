---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opimpiregisterv2-construction
title: 构造和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > 构造和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c23ca05e6bce292538fc0dcd3e95d79f022d184737d82fe9f0533f2e44a4aed6
---

## 函数功能

OpImplRegisterV2类作为注册接口类，提供了一系列算子原型注册接口，供开发者注册指定算子类型的Tiling函数、Infershape函数、私有属性等信息。开发者调用算子原型注册接口进行注册时会间接使用到该类。

## 函数原型

```cpp
// 指定算子类型为op_type，构造一个用于算子注册的OpImplRegisterV2对象，并对其注册数据进行默认初始化。
explicit OpImplRegisterV2(const ge::char_t *op_type);
// 移动构造和拷贝构造函数，二者功能均能将另一个OpImplRegisterV2对象register_data的OpImplFunctions数据注册到OpImplRegistry单例所管理的map中，并且生成一个新的默认初始化的OpImplRegisterV2对象。
OpImplRegisterV2(OpImplRegisterV2 &&register_data) noexcept;
OpImplRegisterV2(const OpImplRegisterV2 &register_data);
OpImplRegisterV2 &operator=(const OpImplRegisterV2 &) = delete;
OpImplRegisterV2 &operator=(OpImplRegisterV2 &&) = delete;
~OpImplRegisterV2();
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_type | 输入 | 指定的算子类型。 |
| register\_data | 输入 | 另一个注册对象，类型为OpImplRegisterV2的引用。 |

## 返回值

一个用于算子注册的OpImplRegisterV2对象。

## 约束说明

无
