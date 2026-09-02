---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getprimaryformat
title: GetPrimaryFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetPrimaryFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7dab202a2bc7c86354c4f40961508d23e1e7204eabec20f5d3717b49de3fc0f9
---

## 函数功能

从实际format中解析出主format信息。

## 函数原型

```cpp
inline int32_t GetPrimaryFormat(int32_t format)
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
