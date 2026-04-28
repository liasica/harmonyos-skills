---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getc0value
title: GetC0Value
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetC0Value
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:245ea7251b0ac3358cb6f02ce9cf288099347f8b898c75383ef7db9d3d04eaac
---

## 函数功能

从实际format中解析出c0 format信息。

## 函数原型

```
1. inline int64_t GetC0Value(int32_t format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。 |

## 返回值

* 如果包含c0 format，返回实际format中包含的c0 format。
* 如果不包含c0 format，返回-1。

## 异常处理

无

## 约束说明

设置实际format格式时，第一个字节低四位的c0 format的范围只支持x=(0001~1111)，实际获取的c0 value为2^x-1。
