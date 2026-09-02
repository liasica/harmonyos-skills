---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-setplacement
title: SetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7d5d37b055bed64bc13e5e141cca3d87b81ba4f8278393aa1ab961741a0fd3a
---

## 函数功能

设置Tensor的数据存放的位置。

## 函数原型

```cpp
void SetPlacement(Placement placement);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| placement | 输入 | 需设置的数据地址的值。  枚举值如下：kPlacementHost、kPlacementDevice。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
