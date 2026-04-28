---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getformatfromsubandc0
title: GetFormatFromSubAndC0
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetFormatFromSubAndC0
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9fa2d7864f50031e87350ade574d89d7cdfa85b5ce5cdf6dca17af8e5e704fd1
---

## 函数功能

根据传入的主format，子format和c0format信息得到实际的format。

实际format为4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息，如下。

/\*

\* ---------------------------------------------------

\* | 4 bits | 4bits | 2 bytes | 1 byte |

\* |------------|-------------|----------------|--------|

\* | reserved | c0 -format | sub-format | format |

\* ---------------------------------------------------

\*/

## 函数原型

```
1. inline int32_t GetFormatFromSubAndC0(int32_t primary_format, int32_t sub_format, int32_t c0_format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| primary\_format | 输入 | 主format信息，值不超过0xffU。 |
| sub\_format | 输入 | sub-format信息，值不超过0xffffU。 |
| c0\_format | 输入 | c0-format信息，值不超过0xfU。 |

## 返回值

指定的primary\_format、sub\_format和c0\_format对应的实际format。

## 异常处理

无

## 约束说明

无
