---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > 构造函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:354877f3696773862fb9dd74e37e4ae46632b5b1abe9ca770a987d7b6d1af3d4
---

## 函数功能

Shape构造函数。

## 函数原型

下文中的dim\_num\_为维度个数，即有几维；dims\_为具体的维度值信息。

* 默认构造一个shape，默认构造的shape实例中，dim\_num\_长度为0

  ```
  1. Shape() : dim_num_(0), dims_{0}
  ```
* 通过dims\_值构造shape，例如：Shape({8,3,224,224})表示创建一个Shape实例，有4个维度，每个维度的值分别是8,3,224,224

  ```
  1. Shape(const std::initializer_list<int64_t> &args) : Shape()
  ```
* 拷贝构造，为了提升性能，dims\_超过源Shape dim\_num\_的空间没有拷贝，可能有脏数据

  ```
  1. Shape(const Shape &other)
  ```
* 拷贝赋值，为了提升性能，dims\_超过源Shape dim\_num\_的空间没有拷贝，可能有脏数据

  ```
  1. Shape &operator=(const Shape &other)
  ```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| args | 输入 | shape的所有dim值。 |
| other | 输入 | 源shape对象。 |

## 返回值

生成一个初始化的Shape对象。

## 约束说明

无

## 调用示例

```
1. Shape shape({3, 256, 256}); // dim_num_=3  dims_的前三维的维度为3,256,256
```
