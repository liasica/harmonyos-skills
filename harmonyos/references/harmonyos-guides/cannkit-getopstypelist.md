---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getopstypelist
title: GetOpsTypeList
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OperatorFactory > GetOpsTypeList
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a805f3e701be55abab9e6818b59f3645fe75a0dd13d425ae2254f87795c6591a
---

## 函数功能

获取系统支持的所有算子类型列表。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
static graphStatus GetOpsTypeList(std::vector<std::string> &all_ops);
static graphStatus GetOpsTypeList(std::vector<AscendString> &all_ops);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| all\_ops | 输出 | 算子类型列表。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | - SUCCESS：执行成功。  - FAILED：执行失败。 |

## 约束说明

无
