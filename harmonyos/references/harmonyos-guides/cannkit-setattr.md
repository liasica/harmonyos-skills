---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setattr
title: SetAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SetAttr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de39bf9255f91bc469e0ea9ac4fb630681ebba38ba2871119e31343e31a94743
---

## 函数功能

设置算子属性的属性值。

算子可以包括多个属性，初次设置值后，算子属性值的类型固定，算子属性值的类型包括：

* 整型：接受int64\_t、uint32\_t、int32\_t类型的整型值

  使用SetAttr(const string& name, int64\_t attrValue)设置属性值，以GetAttr(const string& name, int32\_t& attrValue) 、GetAttr(const string& name, uint32\_t& attrValue) 取值时，开发者需保证整型数据没有截断，同理针对int32\_t和uint32\_t混用时需要保证不被截断。
* 整型列表：接受std::vector<int64\_t>、std::vector<int32\_t>、std::vector<uint32\_t>、std::initializer\_list<int64\_t>&&表示的整型列表数据
* 浮点数：float
* 浮点数列表：std::vector<float>
* 字符串：string
* 字符串列表：std::vector<std::string>
* 布尔：bool
* 布尔列表：std::vector<bool>
* Tensor：Tensor
* Tensor列表：std::vector<Tensor>
* Bytes：字节数组，SetAttr接受通过OpBytes（即vector<uint8\_t>），和（const uint8\_t\* data, size\_t size）表示的字节数组
* AttrValue类型
* 整型二维列表类型：std::vector<std::vector<int64\_t>>
* DataType列表类型：std::vector<ge::DataType>
* DataType类型：ge::DataType
* NamedAttrs类型： ge::NamedAttrs
* NamedAttrs列表类型：std::vector<ge::NamedAttrs>

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. Operator &SetAttr(const std::string &name, int64_t attr_value);
2. Operator &SetAttr(const std::string &name, int32_t attr_value);
3. Operator &SetAttr(const std::string &name, uint32_t attr_value);
4. Operator &SetAttr(const std::string &name, const std::vector<int64_t> &attr_value);
5. Operator &SetAttr(const std::string &name, const std::vector<int32_t> &attr_value);
6. Operator &SetAttr(const std::string &name, const std::vector<uint32_t> &attr_value);
7. Operator &SetAttr(const std::string &name, std::initializer_list<int64_t> &&attr_value);
8. Operator &SetAttr(const std::string &name, float32_t attr_value);
9. Operator &SetAttr(const std::string &name, const std::vector<float32_t> &attr_value);
10. Operator &SetAttr(const std::string &name, AttrValue &&attr_value);
11. Operator &SetAttr(const std::string &name, const std::string &attr_value);
12. Operator &SetAttr(const std::string &name, const std::vector<std::string> &attr_value);
13. Operator &SetAttr(const std::string &name, bool attr_value);
14. Operator &SetAttr(const std::string &name, const std::vector<bool> &attr_value);
15. Operator &SetAttr(const std::string &name, const Tensor &attr_value);
16. Operator &SetAttr(const std::string &name, const std::vector<Tensor> &attr_value);
17. Operator &SetAttr(const std::string &name, const OpBytes &attr_value);
18. Operator &SetAttr(const std::string &name, const std::vector<std::vector<int64_t>> &attr_value);
19. Operator &SetAttr(const std::string &name, const std::vector<ge::DataType> &attr_value);
20. Operator &SetAttr(const std::string &name, const ge::DataType &attr_value);
21. Operator &SetAttr(const std::string &name, const ge::NamedAttrs &attr_value);
22. Operator &SetAttr(const std::string &name, const std::vector<ge::NamedAttrs> &attr_value);
23. Operator &SetAttr(const char_t *name, int64_t attr_value);
24. Operator &SetAttr(const char_t *name, int32_t attr_value);
25. Operator &SetAttr(const char_t *name, uint32_t attr_value);
26. Operator &SetAttr(const char_t *name, const std::vector<int64_t> &attr_value);
27. Operator &SetAttr(const char_t *name, const std::vector<int32_t> &attr_value);
28. Operator &SetAttr(const char_t *name, const std::vector<uint32_t> &attr_value);
29. Operator &SetAttr(const char_t *name, std::initializer_list<int64_t> &&attr_value);
30. Operator &SetAttr(const char_t *name, float32_t attr_value);
31. Operator &SetAttr(const char_t *name, const std::vector<float32_t> &attr_value);
32. Operator &SetAttr(const char_t *name, AttrValue &&attr_value);
33. Operator &SetAttr(const char_t *name, const char_t *attr_value);
34. Operator &SetAttr(const char_t *name, const AscendString &attr_value);
35. Operator &SetAttr(const char_t *name, const std::vector<AscendString> &attr_values);
36. Operator &SetAttr(const char_t *name, bool attr_value);
37. Operator &SetAttr(const char_t *name, const std::vector<bool> &attr_value);
38. Operator &SetAttr(const char_t *name, const Tensor &attr_value);
39. Operator &SetAttr(const char_t *name, const std::vector<Tensor> &attr_value);
40. Operator &SetAttr(const char_t *name, const OpBytes &attr_value);
41. Operator &SetAttr(const char_t *name, const std::vector<std::vector<int64_t>> &attr_value);
42. Operator &SetAttr(const char_t *name, const std::vector<ge::DataType> &attr_value);
43. Operator &SetAttr(const char_t *name, const ge::DataType &attr_value);
44. Operator &SetAttr(const char_t *name, const ge::NamedAttrs &attr_value);
45. Operator &SetAttr(const char_t *name, const std::vector<ge::NamedAttrs> &attr_value);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 属性名称。 |
| attr\_value | 输入 | 需设置的int64\_t表示的整型类型属性值。 |
| attr\_value | 输入 | 需设置的int32\_t表示的整型类型属性值。 |
| attr\_value | 输入 | 需设置的uint32\_t表示的整型类型属性值。 |
| attr\_value | 输入 | 需设置的vector<int64\_t>表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的vector<int32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的vector<uint32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的std::initializer\_list<int64\_t>&&表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的浮点类型的属性值。 |
| attr\_value | 输入 | 需设置的浮点列表类型的属性值。 |
| attr\_value | 输入 | 需设置的布尔类型的属性值。 |
| attr\_value | 输入 | 需设置的布尔列表类型的属性值。 |
| attr\_value | 输入 | 需设置的AttrValue类型的属性值。 |
| attr\_value | 输入 | 需设置的字符串类型的属性值。 |
| attr\_value | 输入 | 需设置的字符串列表类型的属性值。 |
| attr\_value | 输入 | 需设置的Tensor类型的属性值。 |
| attr\_value | 输入 | 需设置的Tensor列表类型的属性值。 |
| attr\_value | 输入 | 需设置的Bytes，即字节数组类型的属性值，OpBytes即vector<uint8\_t>。 |
| data | 输入 | 需设置的Bytes，即字节数组类型的属性值，指定了字节流的首地址。 |
| size | 输入 | 需设置的Bytes，即字节数组类型的属性值，指定了字节流的长度。 |
| attr\_value | 输入 | 需设置的量化数据的属性值。 |
| attr\_value | 输入 | 需设置的vector<vector<int64\_t>>表示的整型二维列表类型属性值。 |
| attr\_value | 输入 | 需设置的vector<ge::DataType>表示的DataType列表类型属性值。 |
| attr\_value | 输入 | 需设置的DataType类型的属性值。 |
| attr\_value | 输入 | 需设置的NamedAttrs类型的属性值。 |
| attr\_value | 输入 | 需设置的vector<ge::NamedAttrs>表示的NamedAttrs列表类型的属性值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| [Operator](cannkit-operator-construction-and-destructor.md)& | 对象本身。 |

## 异常处理

无

## 约束说明

无
