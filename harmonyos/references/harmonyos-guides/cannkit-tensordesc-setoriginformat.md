---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-setoriginformat
title: SetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c26509f68e2391134a8ced40d37e8ad8ad1ec3e00bd58d4a03bcb1ddd6568dc5
---

## 函数功能

向TensorDesc中设置Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```cpp
void SetOriginFormat(Format origin_format);
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
