---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicinputnum
title: GetDynamicInputNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetDynamicInputNum
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:11+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:4c51e31daa528183dd3c28d613c2259cb7810e942459f892fefc530ecc7f254c
---

## 函数功能

获取算子的动态Input的实际个数。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
int32_t GetDynamicInputNum(const std::string &name) const;
int32_t GetDynamicInputNum(const char_t *name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的动态Input名。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| int | 实际动态Input的个数。  当name非法，或者算子无动态Input时，返回0。 |

## 约束说明

无
