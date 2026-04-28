---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setoriginformat1
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec5bf68214cd5166c69611fd5f3e5e029c50940d4b9d0d219595b5b656ca43bb
---

## 函数功能

设置Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```
1. graphStatus SetOriginFormat(const ge::Format &format);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| format | 输入 | 需设置的原始Format值。  关于Format类型，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
