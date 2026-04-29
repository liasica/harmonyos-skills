---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getautomappingsubgraphioindexfunc
title: GetAutoMappingSubgraphIOIndexFunc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > FrameworkRegistry > GetAutoMappingSubgraphIOIndexFunc
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:19ad91bc037b35589576767e77becc6d75fedccb676ceb4ad0a53e0e6d06666b
---

## 函数功能

根据网络类型，获取已经注册的自动映射函数。

## 函数原型

```
1. AutoMappingSubgraphIOIndexFunc GetAutoMappingSubgraphIOIndexFunc(domi::FrameworkType framework)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| framework | 输入 | 网络类型，FrameworkType类型定义请参考[FrameworkType](cannkit-frameworktype.md)。 |

## 返回值

AutoMappingSubgraphIOIndexFunc：自动映射输入输出函数，函数类型详见[AutoMappingSubgraphIndex](cannkit-automappingsubgraphindex.md)。

## 异常处理

无

## 约束说明

无
