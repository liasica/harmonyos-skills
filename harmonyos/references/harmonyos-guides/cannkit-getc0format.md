---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getc0format
title: GetC0Format
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetC0Format
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ccff4ae49aec0a246898be350f14d8b0ffae769ea49ed957503bb5e3cf167f5
---

## 函数功能

根据实际format获取C0 format的值。C0值是AI处理器特有数据格式所需要的参数。例如NC1HWC0，最后一维即表示C0值，C0值在不同的AI处理器中数值不同，通过C0 format来承载。

实际format为4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息，如下所示：

/\*

\* ---------------------------------------------------

\* | 4 bits | 4bits | 2 bytes | 1 byte |

\* |------------|-------------|----------------|--------|

\* | reserved | c0 -format | sub-format | format |

\* ---------------------------------------------------

\*/

## 函数原型

```
1. inline int32_t GetC0Format(int32_t format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format段，第2-3字节为子format信息，第4字节为主format信息）。 |

## 返回值

* 如果包含c0 format，返回c0 format的值。
* 如果不包含c0 format，返回0。

## 异常处理

无

## 约束说明

无
