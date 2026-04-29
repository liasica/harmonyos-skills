---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-input
title: Input
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpDef > Input
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:70d4fb0ff77c156bcdd49914d34a02b81bff9c20d5c3816801f7ca01136a16cf
---

## 函数功能

注册算子输入，调用该接口后会返回一个OpParamDef结构，后续可通过该结构配置算子输入信息。

## 函数原型

```
1. OpParamDef &Input(const char *name);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| name | 输入 | 算子输入名称。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子参数定义。

## 约束说明

无
