---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shapeandtype-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > ShapeAndType > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:18e9af108fa7918936ade9fef535a64bb3737099ec34a5bc0133f85722f84b29
---

## 函数功能

ShapeAndType构造函数和析构函数。

## 函数原型

```
1. ShapeAndType();
2. ~ShapeAndType();
3. ShapeAndType(const Shape &shape, DataType data_type);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| shape | 输入 | 需设置的shape。 |
| data\_type | 输入 | 需设置的dataType。 |

## 返回值

ShapeAndType构造函数返回ShapeAndType类型的对象。

## 异常处理

无

## 约束说明

无
