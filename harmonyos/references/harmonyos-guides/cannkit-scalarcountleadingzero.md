---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalarcountleadingzero
title: ScalarCountLeadingZero
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 标量计算 > ScalarCountLeadingZero
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:1af28daf4731e2d667d50740bd2915deb886548ad14d7557776178a389c9cfab
---

## 功能说明

计算一个uint64\_t类型数字前导0的个数（二进制从最高位到第一个1一共有多少个0）。

## 函数原型

```cpp
__aicore__ inline int64_t ScalarCountLeadingZero(uint64_t valueIn)
```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| valueIn | 输入 | 被统计的二进制数字。  数据类型为uint64\_t。 |

## 返回值

返回valueIn的前导0的个数。

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

无

## 调用示例

```cpp
uint64_t valueIn = 0x0ffffffffffffffff;
// 输出数据(ans): 4
int64_t ans = AscendC::ScalarCountLeadingZero(valueIn);
```
