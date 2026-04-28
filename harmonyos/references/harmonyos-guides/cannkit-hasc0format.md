---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hasc0format
title: HasC0Format
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > HasC0Format
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d2b52504aa1a6dc53bbc08f130c6715e3395836ea4ced895c9c1aaf442e0cd4
---

## 函数功能

判断实际format中是否包含C0 format。

## 函数原型

```
1. inline bool HasC0Format(int32_t format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。 |

## 返回值

* true：实际format中包含c0 format。
* false：实际format中不包含c0 format。

## 异常处理

无

## 约束说明

无
