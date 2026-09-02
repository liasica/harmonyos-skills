---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalargetcountofvalue
title: ScalarGetCountOfValue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 标量计算 > ScalarGetCountOfValue
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:655fdc45ca53290b629d191a1b0bfe0ae08eb73d160f2758c9c544566ff9f8fa
---

## 功能说明

获取一个uint64\_t类型数字的二进制中0或者1的个数。

## 函数原型

```cpp
template <int countValue>  
__aicore__ inline int64_t ScalarGetCountOfValue(uint64_t valueIn)
```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| valueIn | 输入 | 被统计的二进制数字。  数据类型是uint64\_t。 |
| countValue | 输入 | 指定统计0还是统计1的个数。  数据类型是int，只能输入0或1。 |

## 返回值

valueIn中0或者1的个数。

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

无

## 调用示例

```cpp
uint64_t valueIn = 0xffff;
// 输出数据(oneCount): 16
int64_t oneCount = AscendC::ScalarGetCountOfValue<1>(valueIn);
```
