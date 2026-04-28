---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattr
title: GetAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetAttr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:736374d1302d92e1f5df6f715244e58d1df08729762984dfe2bcc65985a2ce8c
---

## 函数功能

根据属性名称获取对应的属性值。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. graphStatus GetAttr(const std::string &name, int64_t &attr_value) const;
2. graphStatus GetAttr(const std::string &name, int32_t &attr_value) const;
3. graphStatus GetAttr(const std::string &name, uint32_t &attr_value) const;
4. graphStatus GetAttr(const std::string &name, std::vector<int64_t> &attr_value) const;
5. graphStatus GetAttr(const std::string &name, std::vector<int32_t> &attr_value) const;
6. graphStatus GetAttr(const std::string &name, std::vector<uint32_t> &attr_value) const;
7. graphStatus GetAttr(const std::string &name, float32_t &attr_value) const;
8. graphStatus GetAttr(const std::string &name, std::vector<float32_t> &attr_value) const;
9. graphStatus GetAttr(const std::string &name, AttrValue &attr_value) const;
10. graphStatus GetAttr(const std::string &name, std::string &attr_value) const;
11. graphStatus GetAttr(const std::string &name, std::vector<std::string> &attr_value) const;
12. graphStatus GetAttr(const std::string &name, bool &attr_value) const;
13. graphStatus GetAttr(const std::string &name, std::vector<bool> &attr_value) const;
14. graphStatus GetAttr(const std::string &name, Tensor &attr_value) const;
15. graphStatus GetAttr(const std::string &name, std::vector<Tensor> &attr_value) const;
16. graphStatus GetAttr(const std::string &name, OpBytes &attr_value) const;
17. graphStatus GetAttr(const std::string &name, std::vector<std::vector<int64_t>> &attr_value) const;
18. graphStatus GetAttr(const std::string &name, std::vector<ge::DataType> &attr_value) const;
19. graphStatus GetAttr(const std::string &name, ge::DataType &attr_value) const;
20. graphStatus GetAttr(const std::string &name, ge::NamedAttrs &attr_value) const;
21. graphStatus GetAttr(const std::string &name, std::vector<ge::NamedAttrs> &attr_value) const;
22. graphStatus GetAttr(const char_t *name, int64_t &attr_value) const;
23. graphStatus GetAttr(const char_t *name, int32_t &attr_value) const;
24. graphStatus GetAttr(const char_t *name, uint32_t &attr_value) const;
25. graphStatus GetAttr(const char_t *name, std::vector<int64_t> &attr_value) const;
26. graphStatus GetAttr(const char_t *name, std::vector<int32_t> &attr_value) const;
27. graphStatus GetAttr(const char_t *name, std::vector<uint32_t> &attr_value) const;
28. graphStatus GetAttr(const char_t *name, float32_t &attr_value) const;
29. graphStatus GetAttr(const char_t *name, std::vector<float32_t> &attr_value) const;
30. graphStatus GetAttr(const char_t *name, AttrValue &attr_value) const;
31. graphStatus GetAttr(const char_t *name, AscendString &attr_value) const;
32. graphStatus GetAttr(const char_t *name, std::vector<AscendString> &attr_values) const;
33. graphStatus GetAttr(const char_t *name, bool &attr_value) const;
34. graphStatus GetAttr(const char_t *name, std::vector<bool> &attr_value) const;
35. graphStatus GetAttr(const char_t *name, Tensor &attr_value) const;
36. graphStatus GetAttr(const char_t *name, std::vector<Tensor> &attr_value) const;
37. graphStatus GetAttr(const char_t *name, OpBytes &attr_value) const;
38. graphStatus GetAttr(const char_t *name, std::vector<std::vector<int64_t>> &attr_value) const;
39. graphStatus GetAttr(const char_t *name, std::vector<ge::DataType> &attr_value) const;
40. graphStatus GetAttr(const char_t *name, ge::DataType &attr_value) const;
41. graphStatus GetAttr(const char_t *name, ge::NamedAttrs &attr_value) const;
42. graphStatus GetAttr(const char_t *name, std::vector<ge::NamedAttrs> &attr_value) const;
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
