---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-implemt-common-inferfunc
title: IMPLEMT_COMMON_INFERFUNC
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > IMPLEMT_COMMON_INFERFUNC
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c4e6520cd141e9e348edcccf5954393ce3e052d46e0b6d96f13bd829022b02f5
---

## 函数功能

封装算子的Common\_InferShape函数。

与[IMPLEMT\_INFERFUNC](cannkit-implemt-inferfunc.md)的区别是，此函数自动生成的一个类型为Operator类的对象op，可直接调用[Operator](cannkit-operator-construction-and-destructor.md)接口进行InferShape的实现。若InferShape方法具有通用性，可被多个算子的原型实现调用，可选择此接口实现。

## 函数原型

```
1. IMPLEMT_COMMON_INFERFUNC(func_name)
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| func\_name | 输入 | InferShape函数名，开发者自定义。 |

## 返回值

无
