---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinput
title: SetInput
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SetInput
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:029e42e7f46b031e742bc2ae4604d8f5509517b9bb234b6f00636971045614cd
---

## 函数功能

设置算子Input，即由哪个算子的输出连到本算子。

有如下几种SetInput方法：

* 如果指定srcOprt第0个Output为当前算子Input，使用第一个函数原型设置当前算子Input，不需要指定srcOprt的Output名称。
* 如果指定srcOprt的其它Output为当前算子Input，使用第二个函数原型设置当前算子Input，需要指定srcOprt的Output名称。
* 如果指定srcOprt的其它Output为当前算子Input，使用第三个函数原型设置当前算子Input，需要指定srcOprt的第index个Output。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. Operator &SetInput(const std::string &dst_name, const Operator &src_oprt);
2. Operator &SetInput(const char_t *dst_name, const Operator &src_oprt);
3. Operator &SetInput(const std::string &dst_name, const Operator &src_oprt, const std::string &name);
4. Operator &SetInput(const char_t *dst_name, const Operator &src_oprt, const char_t *name);
5. Operator &SetInput(const std::string &dst_name, const Operator &src_oprt, uint32_t index);
6. Operator &SetInput(const char_t *dst_name, const Operator &src_oprt, uint32_t index);
7. Operator &SetInput(uint32_t dst_index, const Operator &src_oprt, uint32_t src_index);
8. Operator &SetInput(const char_t *dst_name, uint32_t dst_index, const Operator &src_oprt, const char_t *name);
9. Operator &SetInput(const char_t *dst_name, uint32_t dst_index, const Operator &src_oprt);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dst\_name | 输入 | 当前算子Input名称。 |
| src\_oprt | 输入 | Input名称为dst\_name的输入算子对象。 |
| src\_index | 输入 | src\_oprt的第src\_index个输出。 |
| name | 输入 | srcOprt的Output名称。 |
| index | 输入 | srcOprt的第index个Output。 |
| dst\_index | 输入 | 名称为dst\_name的第dst\_index个动态输入。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| Operator& | 当前算子本身。 |

## 异常处理

无

## 约束说明

无
