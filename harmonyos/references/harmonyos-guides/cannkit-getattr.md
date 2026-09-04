---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattr
title: GetAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetAttr
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c80f84a76026939fe935c5ae1467d14ab1d561c7a46311b338d7a72b40ad942
---

## 函数功能

根据属性名称获取对应的属性值。

## 函数原型

![](https://media:401788444108961907) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus GetAttr(const std::string &name, int64_t &attr_value) const;
graphStatus GetAttr(const std::string &name, int32_t &attr_value) const;
graphStatus GetAttr(const std::string &name, uint32_t &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<int64_t> &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<int32_t> &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<uint32_t> &attr_value) const;
graphStatus GetAttr(const std::string &name, float32_t &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<float32_t> &attr_value) const;
graphStatus GetAttr(const std::string &name, AttrValue &attr_value) const;
graphStatus GetAttr(const std::string &name, std::string &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<std::string> &attr_value) const;
graphStatus GetAttr(const std::string &name, bool &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<bool> &attr_value) const;
graphStatus GetAttr(const std::string &name, Tensor &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<Tensor> &attr_value) const;
graphStatus GetAttr(const std::string &name, OpBytes &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<std::vector<int64_t>> &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<ge::DataType> &attr_value) const;
graphStatus GetAttr(const std::string &name, ge::DataType &attr_value) const;
graphStatus GetAttr(const std::string &name, ge::NamedAttrs &attr_value) const;
graphStatus GetAttr(const std::string &name, std::vector<ge::NamedAttrs> &attr_value) const;
graphStatus GetAttr(const char_t *name, int64_t &attr_value) const;
graphStatus GetAttr(const char_t *name, int32_t &attr_value) const;
graphStatus GetAttr(const char_t *name, uint32_t &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<int64_t> &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<int32_t> &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<uint32_t> &attr_value) const;
graphStatus GetAttr(const char_t *name, float32_t &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<float32_t> &attr_value) const;
graphStatus GetAttr(const char_t *name, AttrValue &attr_value) const;
graphStatus GetAttr(const char_t *name, AscendString &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<AscendString> &attr_values) const;
graphStatus GetAttr(const char_t *name, bool &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<bool> &attr_value) const;
graphStatus GetAttr(const char_t *name, Tensor &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<Tensor> &attr_value) const;
graphStatus GetAttr(const char_t *name, OpBytes &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<std::vector<int64_t>> &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<ge::DataType> &attr_value) const;
graphStatus GetAttr(const char_t *name, ge::DataType &attr_value) const;
graphStatus GetAttr(const char_t *name, ge::NamedAttrs &attr_value) const;
graphStatus GetAttr(const char_t *name, std::vector<ge::NamedAttrs> &attr_value) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 属性名称。 |
| attr\_value | 输出 | 返回的int64\_t表示的整型类型属性值。 |
| attr\_value | 输出 | 返回的int32\_t表示的整型类型属性值。 |
| attr\_value | 输出 | 返回的uint32\_t表示的整型类型属性值。 |
| attr\_value | 输出 | 返回的vector<int64\_t>表示的整型列表类型属性值。 |
| attr\_value | 输出 | 返回的vector<int32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输出 | 返回的vector<uint32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输出 | 返回的浮点类型的属性值。 |
| attr\_value | 输出 | 返回的浮点列表类型的属性值。 |
| attr\_value | 输出 | 返回的AttrValue类型的属性值。 |
| attr\_value | 输出 | 返回的布尔类型的属性值。 |
| attr\_value | 输出 | 返回的布尔列表类型的属性值。 |
| attr\_value | 输出 | 返回的字符串类型的属性值。 |
| attr\_value | 输出 | 返回的字符串列表类型的属性值。 |
| attr\_value | 输出 | 返回的Tensor类型的属性值。 |
| attr\_value | 输出 | 返回的Tensor列表类型的属性值。 |
| attr\_value | 输出 | 返回的Bytes，即字节数组类型的属性值，OpBytes即vector<uint8\_t>。 |
| attr\_value | 输出 | 返回的量化数据的属性值。 |
| attr\_value | 输出 | 返回的vector<vector<int64\_t>>表示的整型二维列表类型属性值。 |
| attr\_value | 输出 | 返回的vector<ge::DataType>表示的DataType列表类型属性值。 |
| attr\_value | 输出 | 返回的DataType类型的属性值。 |
| attr\_value | 输出 | 返回的vector<ge::NamedAttrs>表示的NamedAttrs列表类型属性值。 |
| attr\_value | 输出 | 返回的NamedAttrs类型的属性值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 找到对应name，返回GRAPH\_SUCCESS，否则返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
