---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opattrdef
title: OpAttrDef
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpAttrDef
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3414bf4db4e32acf7d1e5e2305d712d48112fec4f37988d73cfb3c5a195bbcd
---

## 功能说明

定义算子属性。

## 定义原型

```
1. class OpAttrDef {
2. public:
3. explicit OpAttrDef(const char *name);
4. OpAttrDef(const OpAttrDef &attr_def);
5. ~OpAttrDef();
6. OpAttrDef &operator=(const OpAttrDef &attr_def);
7. OpAttrDef &AttrType(Option attr_type);
8. OpAttrDef &Bool(void);
9. OpAttrDef &Bool(bool value);
10. OpAttrDef &Float(void);
11. OpAttrDef &Float(float value);
12. OpAttrDef &Int(void);
13. OpAttrDef &Int(int64_t value);
14. OpAttrDef &String(void);
15. OpAttrDef &String(const char *value);
16. OpAttrDef &ListBool(void);
17. OpAttrDef &ListBool(std::vector<bool> value);
18. OpAttrDef &ListFloat(void);
19. OpAttrDef &ListFloat(std::vector<float> value);
20. OpAttrDef &ListInt(void);
21. OpAttrDef &ListInt(std::vector<int64_t> value);
22. ge::AscendString &GetName(void) const;
23. bool IsRequired(void);
24. private:
25. // ...
26. };
```

## 函数说明

**表1** OpAttrDef类成员函数说明

| 函数名称 | 入参说明 | 功能说明 |
| --- | --- | --- |
| AttrType | attr\_type: 属性类型 | 设置算子属性类型，取值为：OPTIONAL（可选）、REQUIRED（必选）。 |
| Bool | 无 | 设置算子属性数据类型为Bool。 |
| Bool | value | 设置算子属性数据类型为Bool, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| Float | 无 | 设置算子属性数据类型为Float。 |
| Float | value | 设置算子属性数据类型为Float, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| Int | 无 | 设置算子属性数据类型为Int。 |
| Int | value | 设置算子属性数据类型为Int, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| String | 无 | 设置算子属性数据类型为String。 |
| String | value | 设置算子属性数据类型为String, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| ListBool | 无 | 设置算子属性数据类型为ListBool。 |
| ListBool | value | 设置算子属性数据类型为ListBool, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| ListFloat | 无 | 设置算子属性数据类型为ListFloat。 |
| ListFloat | value | 设置算子属性数据类型为ListFloat, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| ListInt | 无 | 设置算子属性数据类型为ListInt。 |
| ListInt | value | 设置算子属性数据类型为ListInt, 并设置属性默认值为value。属性类型设置为OPTIONAL时必须调用该类接口设置默认值。 |
| GetName | 无 | 获取属性名称。 |
| IsRequired | 无 | 判断算子属性是否为必选，必选返回true, 可选返回false。 |
