---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-input
title: Input
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpDef > Input
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7bcfe263e120419a80cdb61daf12af827709986d2cff0313714f5430bdfe5229
---

## 函数功能

注册算子输入，调用该接口后会返回一个OpParamDef结构，后续可通过该结构配置算子输入信息。

## 函数原型

```cpp
OpParamDef &Input(const char *name);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| name | 输入 | 算子输入名称。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子参数定义。

## 约束说明

无
