---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setformat
title: SetFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:069143dff0a8a05809dc35024b3b356b0030dd66b83072e064023fe112cf7848
---

## 函数功能

设置Tensor的Format。

## 函数原型

```cpp
graphStatus SetFormat(const ge::Format &format);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| format | 输入 | 需设置的Format值。  关于Format类型，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
