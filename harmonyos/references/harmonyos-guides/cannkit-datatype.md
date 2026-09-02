---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-datatype
title: DataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpParamDef > DataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8064b6cb9e2b93766b193b41d6169314e8e7abc1e46a1af5ec7ad62648e880b2
---

## 函数功能

定义算子参数数据类型。

## 函数原型

```cpp
OpParamDef &DataType(std::vector<ge::DataType> types);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| types | 输入 | 算子参数数据类型，ge::DataType请参考[DataType](cannkit-ge-datatype.md)。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子定义。

## 约束说明

无
