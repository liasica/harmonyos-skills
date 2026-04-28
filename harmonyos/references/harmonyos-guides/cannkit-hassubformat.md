---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hassubformat
title: HasSubFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > HasSubFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87b646276842541e2bd35fe5c6b40547d2817e83aa661002a45ef3bddd62f05a
---

## 函数功能

判断实际format中是否包含子format。

## 函数原型

```
1. inline bool HasSubFormat(int32_t format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。 |

## 返回值

* true：实际format中包含子format。
* false：实际format中不包含子format。

## 异常处理

无

## 约束说明

无
