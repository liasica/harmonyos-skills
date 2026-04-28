---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdim
title: SetDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > SetDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9a22596eae18b685d3f5846a68259dd09f75539dc64095f925a782b470cc5cd5
---

## 函数功能

设置dim值。

## 函数原型

```
1. void SetDim(size_t idx, const int64_t dim_value)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| idx | 输入 | dim的index，调用者需要保证index合法。 |
| dim\_value | 输入 | 对idx轴设置的维度值。 |

## 返回值

无

## 约束说明

调用者需要保证index合法。

## 调用示例

```
1. Shape shape0({3, 256, 256});
2. shape0.SetDim(0U, 1); // 1,256,256
```
