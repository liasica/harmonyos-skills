---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicinputnum
title: GetDynamicInputNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetDynamicInputNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2dbd552e024e479118233842231806668a1ff9bd7f4e6e920c7e2680362bfe64
---

## 函数功能

获取算子的动态Input的实际个数。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. int32_t GetDynamicInputNum(const std::string &name) const;
2. int32_t GetDynamicInputNum(const char_t *name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的动态Input名。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| int | 实际动态Input的个数。  当name非法，或者算子无动态Input时，返回-1。 |

## 约束说明

无
