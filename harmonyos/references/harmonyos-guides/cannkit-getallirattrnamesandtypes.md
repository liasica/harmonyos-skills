---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getallirattrnamesandtypes
title: GetAllIrAttrNamesAndTypes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetAllIrAttrNamesAndTypes
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df335744b8ab4ac7fa0197b62be76bbc096447abe99e4955782ab37cd02bfba1
---

## 函数功能

获取该算子所有的IR定义的属性名称和属性类型，包含普通和必选属性两种。

## 函数原型

```cpp
graphStatus GetAllIrAttrNamesAndTypes(std::map<AscendString, AscendString> &attr_name_types) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| attr\_name\_types | 输出 | 所有的IR定义的属性名称和属性类型。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
