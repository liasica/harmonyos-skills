---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputattr
title: GetOutputAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetOutputAttr
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:63a8ce784a5a4cbd611680fbb34a8a86ce67777ff7965530c35f8de5cce19d5a
---

## 函数功能

根据属性名称获取算子输出Tensor对应的属性值。

## 函数原型

```cpp
graphStatus GetOutputAttr(const int32_t index, const char_t *name, AscendString &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, AscendString &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, int64_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, int64_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, int32_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, int32_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, uint32_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, uint32_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, bool &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, bool &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, float32_t &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, float32_t &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector<AscendString> &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector<AscendString> &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector<int64_t> &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector<int64_t> &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector<int32_t> &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector<int32_t> &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector<uint32_t> &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector<uint32_t> &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector<bool> &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector<bool> &attr_value) const;
graphStatus GetOutputAttr(const int32_t index, const char_t *name, std::vector<float32_t> &attr_value) const;
graphStatus GetOutputAttr(const char_t *dst_name, const char_t *name, std::vector<float32_t> &attr_value) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 属性名称。 |
| index | 输出 | 输出索引。 |
| dst\_name | 输出 | 输出边名称。 |
| attr\_value | 输出 | 获取到的int64\_t表示的整型类型属性值。 |
| attr\_value | 输出 | 获取到的int32\_t表示的整型类型属性值。 |
| attr\_value | 输出 | 获取到的uint32\_t表示的整型类型属性值。 |
| attr\_value | 输出 | 获取到的vector<int64\_t>表示的整型列表类型属性值。 |
| attr\_value | 输出 | 获取到的vector<int32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输出 | 获取到的vector<uint32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输出 | 获取到的浮点类型的属性值。 |
| attr\_value | 输出 | 获取到的浮点列表类型的属性值。 |
| attr\_value | 输出 | 获取到的布尔类型的属性值。 |
| attr\_value | 输出 | 获取到的布尔列表类型的属性值。 |
| attr\_value | 输出 | 获取到的字符串类型的属性值。 |
| attr\_value | 输出 | 获取到的字符串列表类型的属性值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 找到对应属性，返回GRAPH\_SUCCESS，否则返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
