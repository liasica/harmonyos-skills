---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingsubgraphioindexfuncregister
title: AutoMappingSubgraphIOIndexFuncRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AutoMappingSubgraphIOIndexFuncRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e7c9bccfa55d34805f4d8203a92f3ffb05b3ea47326cc75f47baa5b4c24874ca
---

## 函数功能

FrameworkRegistry类的封装，通过类的构造函数调用FrameworkRegistry类的AddAutoMappingSubgraphIOIndexFunc函数完成映射函数的注册。

## 函数原型

```
1. AutoMappingSubgraphIOIndexFuncRegister(domi::FrameworkType framework, AutoMappingSubgraphIOIndexFunc fun)
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
