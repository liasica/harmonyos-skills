---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-paramtype
title: ParamType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpParamDef > ParamType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce302e179e6586e728b7e92bd97f835d50180af1c8065eb842fca1c7228e3e22
---

## 函数功能

定义算子参数类型。

## 函数原型

```cpp
OpParamDef &ParamType(Option param_type);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| param\_type | 输入 | 参数类型，Option取值为：OPTIONAL（可选）、REQUIRED（必选）。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子定义。

## 约束说明

无
