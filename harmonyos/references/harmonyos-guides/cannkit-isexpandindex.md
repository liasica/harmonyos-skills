---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isexpandindex
title: IsExpandIndex
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > IsExpandIndex
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d95a08e67921be7070ea575f6472ec1c4e24061f995097f4ca465e1bbfe0a400
---

## 函数功能

基于补维后的shape，判断指定的index轴是否为补维轴。

## 函数原型

```
1. bool IsExpandIndex(const AxisIndex index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 指定轴的索引。 |

## 返回值

* true代表指定的轴为补维轴。
* false代表指定的轴为原始轴。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType type1("1001");
2. bool is_expand_index0 = type1.IsExpandIndex(0); // true
3. bool is_expand_index1 = type1.IsExpandIndex(1); // false
```
