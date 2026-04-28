---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmarks
title: GetMarks
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > GetMarks
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:32e7883df25511ff1372dea30d93b08ba49ae5b5e79736ed6bfbafe4ecef0056
---

## 函数功能

在资源类算子推理的上下文中，获取成对资源算子的标记。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. const std::vector<std::string> &GetMarks() const
2. void GetMarks(std::vector<AscendString> &marks) const
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| const std::vector<std::string> | 资源类算子的标记。 |

## 异常处理

无

## 约束说明

无
