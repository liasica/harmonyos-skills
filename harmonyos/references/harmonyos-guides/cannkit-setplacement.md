---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setplacement
title: SetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > SetPlacement
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:deb0e72abcbe3b9561aad0c1a1014db11eaad5cde2d26876dc1b303cc1d6a941
---

## 函数功能

设置tensor的placement。

## 函数原型

```
1. void SetPlacement(const TensorPlacement placement)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| placement | 输入 | tensor的placement。  关于TensorPlacement类型的定义，请参见[TensorPlacement](cannkit-tensorplacement.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. auto addr = reinterpret_cast<void *>(0x10);
2. TensorData td(addr, nullptr);
3. auto td_place = td.SetPlacement(kOnHost);
```
