---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-countbitscntsameassignbit
title: CountBitsCntSameAsSignBit
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 标量计算 > CountBitsCntSameAsSignBit
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:23+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:267c3037c4ee1aab8756c74fee2df4f85bcd68d8c4f32e274181744e3855bf85
---

## 功能说明

计算一个int64\_t类型数字的二进制中，从最高数值位开始与符号位相同的连续比特位的个数。

当输入是-1（比特位全1）或者0（比特位全0）时，返回-1。

## 函数原型

```
1. __aicore__ inline int64_t CountBitsCntSameAsSignBit(int64_t valueIn)
```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| valueIn | 输入 | 输入数据，数据类型int64\_t。 |

## 返回值

返回从最高数值位开始和符号位相同的连续比特位的个数。

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

无

## 调用示例

```
1. int64_t valueIn = 0x0f00000000000000;
2. // 输出数据(ans): 3
3. int64_t ans = AscendC::CountBitsCntSameAsSignBit(valueIn);
```
