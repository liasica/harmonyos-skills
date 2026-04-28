---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-trygetinputdesc
title: TryGetInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > TryGetInputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94f86893ec620f4fac15904732cf3523b1d7e26d8b87c16dd14a86a7344bb611
---

## 函数功能

根据算子Input名称获取算子Input的TensorDesc。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. graphStatus TryGetInputDesc(const std::string &name, TensorDesc &tensor_desc) const;
2. graphStatus TryGetInputDesc(const char_t *name, TensorDesc &tensor_desc) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的Input名。 |
| tensor\_desc | 输出 | 返回算子端口的当前设置格式，为TensorDesc对象。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | true：有此端口，获取TensorDesc成功。  false：无此端口，出参为空，获取TensorDesc失败。 |

## 异常处理

| 异常场景 | 说明 |
| --- | --- |
| 无对应name输入 | 返回false。 |

## 约束说明

无
