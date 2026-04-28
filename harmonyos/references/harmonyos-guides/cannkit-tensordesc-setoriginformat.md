---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-setoriginformat
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24a6c3a86797b6cfa5ff51e625c901acc10ec6ede4b3ea330765fcea136794e0
---

## 函数功能

向TensorDesc中设置Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```
1. void SetOriginFormat(Format origin_format);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| origin\_format | 输入 | 需设置的原始Format信息。  关于Format数据类型的定义，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
