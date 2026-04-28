---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getallattrnamesandtypes
title: GetAllAttrNamesAndTypes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetAllAttrNamesAndTypes
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f20ebccc11bf74f4aa530786a5fb592f2d5be7a6c37d08702d854f88ccc699d7
---

## 函数功能

获取算子所有已配置的属性名称及类型，包含IR定义的普通属性和开发者自定义属性。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. const std::map<std::string, std::string> GetAllAttrNamesAndTypes() const;
2. graphStatus GetAllAttrNamesAndTypes(std::map<AscendString, AscendString> &attr_name_types) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| attr\_name\_types | 输出 | 所有的属性名称和属性类型。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
