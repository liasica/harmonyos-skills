---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalargetsffvalue
title: ScalarGetSFFValue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 标量计算 > ScalarGetSFFValue
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:4bd301c6c525cdc3526915e49557646853c5bac2072c603980d6ceb7e3237d6e
---

## 功能说明

获取一个uint64\_t类型数字的二进制中第一个0或1出现的位置，索引从最低位（索引0）开始计数，若未找到则返回-1。当countValue参数为1时，查找的是第一个1的位置；当countValue参数为0时，查找的是第一个0的位置。此函数常用于位操作优化、数据压缩算法等场景中以提高处理效率。

## 函数原型

```cpp
template <int countValue>  
__aicore__ inline int64_t ScalarGetSFFValue(uint64_t valueIn)
```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| valueIn | 输入 | 输入数据，数据类型是uint64\_t。 |
| countValue | 输入 | 获取到第一个0或1的位置。数据类型是int，值为0或1。 |

## 返回值

valueIn中第一个0或1出现的位置。

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

无。

## 调用示例

```cpp
uint64_t valueIn = 28;
// 输出数据(oneCount): 2
int64_t oneCount = AscendC::ScalarGetSFFValue<1>(valueIn);
```
