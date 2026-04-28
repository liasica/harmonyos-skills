---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expanddimstype-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > 构造函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c12c6d7f450ae28cf5d98a6d1ca29715df89b742c1f300311b6c3987fee2680d
---

## 函数功能

创建一个补维规则。

## 函数原型

* 构造的实例中，补维规则（mask\_）以及补维后的维度（size\_）均为0

  ```
  1. ExpandDimsType() : size_(0U), mask_(0U)
  ```
* 通过字符串创建一个补维规则

  ```
  1. ExpandDimsType(const ge::char_t *const expand_dims_type)
  ```
* 通过int64\_t位域定义创建一个补维规则

  ```
  1. ExpandDimsType(const int64_t reshape_type_mask)
  ```

## 参数说明

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| expand\_dims\_type | 输入 | - 字符串描述的补维规则。字符串长度最大为56Bytes。  - int64\_t类型的补维规则，共64位，int中的位域定义参见表2。  为了简化，补维规则部分与字符串的顺序相反，例如字符串描述的补维规则为"1100"，那么对应的补维规则为"0011"，转换为数字为3。补维规则的概念和描述方法请参考[简介](cannkit-expanddimstype-introduction.md)。 |

**表2** int64\_t位域定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| 高8比特 | uint8\_t | 补维规则长度。 |
| 低56比特 | 位域 | 使用0、1描述的补维规则。 |

## 返回值

返回一个ExpandDimsType对象，且该对象的补维规则（mask\_）以及补维后的维度（size\_）均根据入参expand\_dims\_type完成设置。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType type("1001"); // 设置mask_为1001，size_为4
```
