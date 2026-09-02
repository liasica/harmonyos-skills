---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-trygetinputdesc
title: TryGetInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > TryGetInputDesc
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:974982221ce73907ad01f8b91e13975f1bacef8f6968f53de4958bcd8cc7b088
---

## 函数功能

根据算子Input名称获取算子Input的TensorDesc。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus TryGetInputDesc(const std::string &name, TensorDesc &tensor_desc) const;
graphStatus TryGetInputDesc(const char_t *name, TensorDesc &tensor_desc) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子的Input名。 |
| tensor\_desc | 输出 | 返回算子端口的当前设置格式，为TensorDesc对象。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_SUCCESS：有此端口，获取TensorDesc成功。  GRAPH\_FAILED：无此端口，出参为空，获取TensorDesc失败。 |

## 异常处理

| 异常场景 | 说明 |
| --- | --- |
| 无对应name输入 | 返回GRAPH\_FAILED。 |

## 约束说明

无
