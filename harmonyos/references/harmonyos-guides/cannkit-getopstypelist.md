---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getopstypelist
title: GetOpsTypeList
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OperatorFactory > GetOpsTypeList
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d28ecdf8f40fef7d0c6fad784bb4f609e85f6e490a7969870bb3d983cce7d98b
---

## 函数功能

获取系统支持的所有算子类型列表。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. static graphStatus GetOpsTypeList(std::vector<std::string> &all_ops);
2. static graphStatus GetOpsTypeList(std::vector<AscendString> &all_ops);
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
