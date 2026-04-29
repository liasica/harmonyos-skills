---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-addautomappingsubgraphioindexfunc
title: AddAutoMappingSubgraphIOIndexFunc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > FrameworkRegistry > AddAutoMappingSubgraphIOIndexFunc
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ceb65f61db8965b2e168b380c80b69f4341bfd389cf6bd96d11eb324848ac781
---

## 函数功能

注册的具体网络类型的自动映射函数。

## 函数原型

```
1. void AddAutoMappingSubgraphIOIndexFunc(domi::FrameworkType framework, AutoMappingSubgraphIOIndexFunc fun);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| framework | 输入 | 网络类型，FrameworkType类型定义请参考[FrameworkType](cannkit-frameworktype.md)。 |
| fun | 输入 | 自动映射输入输出函数，函数类型详见[AutoMappingSubgraphIndex](cannkit-automappingsubgraphindex.md)。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
