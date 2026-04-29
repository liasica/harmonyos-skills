---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-output
title: Output
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpDef > Output
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38c017da348b8b384db27920a1b807da4937703e6ae06db8fc9f95a441b8b1f2
---

## 函数功能

注册算子输出，调用该接口后会返回一个OpParamDef结构，后续可通过该结构配置算子输出信息。

## 函数原型

```
1. OpParamDef &Output(const char *name);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| name | 输入 | 算子输出名称。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子参数定义。

## 约束说明

无
