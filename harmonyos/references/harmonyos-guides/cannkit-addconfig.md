---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-addconfig
title: AddConfig
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpAICoreDef > AddConfig
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:af94df3f022f4452f22a14aea4525dcf898bdd5f9fbc78e10dbf8650b0a0565d
---

## 函数功能

注册算子支持的AI处理器型号信息。

## 函数原型

```cpp
void AddConfig(const char *soc);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| soc | 输入 | 支持AI处理器型号。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

无
