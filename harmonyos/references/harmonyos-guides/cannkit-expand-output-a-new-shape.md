---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expand-output-a-new-shape
title: Expand（输出新shape）
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > Expand（输出新shape）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a24ad78ae14a69bdcaec332c2ae0ccb063b0518c3b22d0a231250f6f5f0b1fb6
---

## 函数功能

对shape做补维，并将补维后的结果写入指定的输出shape对象。

## 函数原型

```cpp
ge::graphStatus Expand(const Shape &shape, Shape &out_shape) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| shape | 输入 | 输入shape，补维前shape。 |
| out\_shape | 输出 | 输出shape，补维后shape。 |

## 返回值

补维成功返回ge::GRAPH\_SUCCESS。

失败则返回ge::GRAPH\_FAILED。

关于ge::graphStatus类型的定义，请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

## 约束说明

无

## 调用示例

```cpp
Shape origin_shape({3, 256, 256}); // 设置原始shape 3x256x256
Shape out_shape;
ExpandDimsType type1("1000");
ExpandDimsType type2("10000");
ExpandDimsType type3("1001");
auto ret = type1.Expand(origin_shape, out_shape); // ret = ge::GRAPH_SUCCESS, out_shape = 1,3,256,256
ret = type2.Expand(origin_shape, out_shape); // ret = ge::GRAPH_FAILED
ret = type3.Expand(origin_shape, out_shape); // ret = ge::GRAPH_SUCCESS, out_shape = 1,3,256,1,256
```
