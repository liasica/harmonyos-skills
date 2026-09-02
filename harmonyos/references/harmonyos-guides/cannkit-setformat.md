---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setformat
title: SetFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc392c3996401d47670dd0f13ce1fd9b3114b4bb79e962496395b630ee2e99f2
---

## 函数功能

向TensorDesc中设置Tensor的Format。

## 函数原型

```cpp
void SetFormat(Format format);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| format | 输入 | 需设置的format信息。  关于Format类型，请参见[Format](cannkit-ge-format.md)。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
