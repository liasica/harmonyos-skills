---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getprimaryformat
title: GetPrimaryFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetPrimaryFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:01b75190dd4bd1aea38fcbda854946abf6d6bbc5a527f4d460c50a26381d12bd
---

## 函数功能

从实际format中解析出主format信息。

## 函数原型

```
1. inline int32_t GetPrimaryFormat(int32_t format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。 |

## 返回值

实际format中包含的主format。

## 异常处理

无

## 约束说明

无
