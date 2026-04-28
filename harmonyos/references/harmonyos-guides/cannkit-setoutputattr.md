---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoutputattr
title: SetOutputAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SetOutputAttr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c6070d9653ac49c5c1830b4fdbc79e54e3bd98a01dfb246a5dbd3c8c5ee6b454
---

## 函数功能

设置算子输出Tensor属性的属性值。

算子可以包括多个属性，初次设置值后，算子属性值的类型固定，算子属性值的类型包括：

* 整型：接受int64\_t、uint32\_t、int32\_t类型的整型值。

  以int64\_t为例：

  ```
  1. SetOutputAttr(const char_t *dst_name, const char_t *name, int64_t attr_value);
  2. SetOutputAttr(const int32_t index, const char_t *name, int64_t attr_value);
  ```

  设置属性值：

  ```
  1. GetOutputAttr(const int32_t index, const char_t *name, int64_t &attr_value) const;
  2. GetOutputAttr(const char_t *dst_name, const char_t *name, int64_t &attr_value) const;
  ```

  取值时，开发者需保证整型数据没有截断，同理针对int32\_t和uint32\_t混用时需要保证不被截断。
* 整型列表：接受std::vector<int64\_t>、std::vector<int32\_t>、std::vector<uint32\_t>、std::initializer\_list<int64\_t>&&表示的整型列表数据。
* 浮点数：float32\_t
* 浮点数列表：std::vector<float32\_t>
* 字符串：string
* 布尔：bool
* 布尔列表：std::vector<bool>

## 函数原型

```
1. Operator &SetOutputAttr(const int32_t index, const char_t *name, const char_t *attr_value);
2. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const char_t *attr_value);
3. Operator &SetOutputAttr(const int32_t index, const char_t *name, const AscendString &attr_value);
4. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const AscendString &attr_value);
5. Operator &SetOutputAttr(const int32_t index, const char_t *name, int64_t attr_value);
6. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, int64_t attr_value);
7. Operator &SetOutputAttr(const int32_t index, const char_t *name, int32_t attr_value);
8. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, int32_t attr_value);
9. Operator &SetOutputAttr(const int32_t index, const char_t *name, uint32_t attr_value);
10. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, uint32_t attr_value);
11. Operator &SetOutputAttr(const int32_t index, const char_t *name, bool attr_value);
12. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, bool attr_value);
13. Operator &SetOutputAttr(const int32_t index, const char_t *name, float32_t attr_value);
14. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, float32_t attr_value);
15. Operator &SetOutputAttr(const int32_t index, const char_t *name, const std::vector<AscendString> &attr_value);
16. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const std::vector<AscendString> &attr_value);
17. Operator &SetOutputAttr(const int32_t index, const char_t *name, const std::vector<int64_t> &attr_value);
18. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const std::vector<int64_t> &attr_value);
19. Operator &SetOutputAttr(const int32_t index, const char_t *name, const std::vector<int32_t> &attr_value);
20. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const std::vector<int32_t> &attr_value);
21. Operator &SetOutputAttr(const int32_t index, const char_t *name, const std::vector<uint32_t> &attr_value);
22. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const std::vector<uint32_t> &attr_value);
23. Operator &SetOutputAttr(const int32_t index, const char_t *name, const std::vector<bool> &attr_value);
24. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const std::vector<bool> &attr_value);
25. Operator &SetOutputAttr(const int32_t index, const char_t *name, const std::vector<float32_t> &attr_value);
26. Operator &SetOutputAttr(const char_t *dst_name, const char_t *name, const std::vector<float32_t> &attr_value);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 属性名称。 |
| index | 输入 | 输出索引。 |
| dst\_name | 输入 | 输出边名称。 |
| attr\_value | 输入 | 需设置的int64\_t表示的整型类型属性值。 |
| attr\_value | 输入 | 需设置的int32\_t表示的整型类型属性值。 |
| attr\_value | 输入 | 需设置的uint32\_t表示的整型类型属性值。 |
| attr\_value | 输入 | 需设置的vector<int64\_t>表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的vector<int32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的vector<uint32\_t>表示的整型列表类型属性值。 |
| attr\_value | 输入 | 需设置的浮点类型的属性值。 |
| attr\_value | 输入 | 需设置的浮点列表类型的属性值。 |
| attr\_value | 输入 | 需设置的布尔类型的属性值。 |
| attr\_value | 输入 | 需设置的布尔列表类型的属性值。 |
| attr\_value | 输入 | 需设置的字符串类型的属性值。 |
| attr\_value | 输入 | 需设置的字符串列表类型的属性值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| Operator& | 对象本身。 |

## 异常处理

无

## 约束说明

无
