---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expand-change-the-original-shape
title: Expand(更改原shape)
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > Expand(更改原shape)
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f10cd38ca9fa228a945ea0507a60b5fa0f99343963138d7e27fb41b9d3c87855
---

## 函数功能

对shape做补维，并将补维后的结果直接更新到原shape对象。

## 函数原型

```
1. ge::graphStatus Expand(Shape &shape) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| shape | 既是输入，又是输出 | 需要进行补维操作的shape对象。 |

## 返回值

补维成功返回ge::GRAPH\_SUCCESS。

关于ge::graphStatus类型的定义，请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

## 约束说明

无

## 调用示例

```
1. Shape shape({3, 256, 256}); // 设置原始shape 3,256,256
2. ExpandDimsType type1("1000");
3. auto ret = type1.Expand(shape); // ret = ge::GRAPH_SUCCESS, shape = 1,3,256,256
```
