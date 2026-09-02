---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicoutputnum
title: GetDynamicOutputNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetDynamicOutputNum
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2212c67f208d07b679e4c82fa0da05736a47925c4740e0c201ac09af70a1126c
---

## 函数功能

获取算子的动态Output的实际个数。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
int32_t GetDynamicOutputNum(const std::string &name) const;
int32_t GetDynamicOutputNum(const char_t *name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的动态Output名。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| int | 实际动态Output的个数。  当name非法，或者算子无动态Output时，返回0。 |

## 约束说明

无
