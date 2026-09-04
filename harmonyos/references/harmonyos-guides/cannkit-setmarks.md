---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmarks
title: SetMarks
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > SetMarks
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8aa5af615f8ae85e45f088f8b075e0d643be063b9819daaf1888ef2b9801d7ed
---

## 函数功能

在资源类算子推理的上下文中，设置成对资源算子的标记。

## 函数原型

![](https://media:401788444108886906) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
void SetMarks(const std::vector<std::string> &marks)
void SetMarks(const std::vector<AscendString> &marks)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| marks | 输入 | 资源类算子的标记。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
