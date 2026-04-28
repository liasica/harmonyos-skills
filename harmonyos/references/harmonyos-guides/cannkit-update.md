---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-update
title: Update
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > Update
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:080d3ce297cb74ed8af0834e81af0763dae5a7a080b89f48a0ddb651f256ab12
---

## 函数功能

更新TensorDesc的shape、format、datatype属性。

## 函数原型

```
1. void Update(const Shape &shape, Format format = FORMAT_ND, DataType dt = DT_FLOAT);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| shape | 输入 | 需刷新的shape对象。 |
| format | 输入 | 需刷新的format对象，默认取值FORMAT\_ND。 |
| dt | 输入 | 需刷新的datatype对象，默认取值DT\_FLOAT。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
