---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opattrdef
title: OpAttrDef
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpAttrDef
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d72fb46e3c118c2c92ae262c0f4369d02e055e1061be1c545b4e680c7d532836
---

## 功能说明

定义算子属性。

## 定义原型

```cpp
class OpAttrDef {
public:
  explicit OpAttrDef(const char *name);
  OpAttrDef(const OpAttrDef &attr_def);
  ~OpAttrDef();
  OpAttrDef &operator=(const OpAttrDef &attr_def);
  OpAttrDef &AttrType(Option attr_type);
  OpAttrDef &Bool(void);
  OpAttrDef &Bool(bool value);
  OpAttrDef &Float(void);
  OpAttrDef &Float(float value);
  OpAttrDef &Int(void);
  OpAttrDef &Int(int64_t value);
  OpAttrDef &String(void);
  OpAttrDef &String(const char *value);
  OpAttrDef &ListBool(void);
  OpAttrDef &ListBool(std::vector<bool> value);
  OpAttrDef &ListFloat(void);
  OpAttrDef &ListFloat(std::vector<float> value);
  OpAttrDef &ListInt(void);
  OpAttrDef &ListInt(std::vector<int64_t> value);
  ge::AscendString &GetName(void) const;
  bool IsRequired(void);
private:
  // ...
};
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
