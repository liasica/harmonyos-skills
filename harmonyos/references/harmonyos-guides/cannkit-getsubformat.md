---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubformat
title: GetSubFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetSubFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc5f381d1fe52092f6e916578aa43e1547205a55352b64ef8042ca2c0c424d54
---

## 函数功能

从实际format中解析出子format信息。

## 函数原型

```
1. inline int32_t GetSubFormat(int32_t format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format段，第2-3字节为子format信息，第4字节为主format信息）。 |

## 返回值

实际format中包含的子format。

## 异常处理

无

## 约束说明

无
