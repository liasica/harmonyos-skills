---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setexpandindex
title: SetExpandIndex
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > SetExpandIndex
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:489a52fcf13e0e18bb8d96a203e9103d09468cea7dd890471ca6a79a31ad4120
---

## 函数功能

将第index轴设置为补维轴。

## 函数原型

```cpp
void SetExpandIndex(const AxisIndex index)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 第index根轴为补维轴。  using AxisIndex = uint64\_t; |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType type1("1001");
type1.SetExpandIndex(1); // 补维规则mask_=1101
```
