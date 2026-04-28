---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getname
title: GetName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetName
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b83036b58c3fbcef6c66696aca5545999742b9e111ab676d8b9df63e60d590fc
---

## 函数功能

获取算子名称。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. std::string GetName() const;
2. graphStatus GetName(AscendString &name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输出 | 算子名称。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
