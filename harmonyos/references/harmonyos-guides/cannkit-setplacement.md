---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setplacement
title: SetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > SetPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2491b2a71a1217ba4d4250da67a2ce37e26b61b8ec78df117ccd84e60d11b1cb
---

## 函数功能

设置tensor的placement。

## 函数原型

```cpp
void SetPlacement(const TensorPlacement placement)
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

```cpp
auto addr = reinterpret_cast<void *>(0x10);
TensorData td(addr, nullptr);
auto td_place = td.SetPlacement(kOnHost);
```
