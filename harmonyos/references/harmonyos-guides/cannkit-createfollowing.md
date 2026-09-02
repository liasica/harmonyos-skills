---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-createfollowing
title: CreateFollowing
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > CreateFollowing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:304b822b96b4890c3ec2cbc61043a7e3599be07ab0c7811349cfc4baf37965f8
---

## 函数功能

创建一个指定数据类型以及大小的Tensor，其数据在Tensor对象后连续排布。

## 函数原型

* 传入元素个数和数据类型，创建Tensor

  ```cpp
  static std::unique_ptr<uint8_t[]> CreateFollowing(const int64_t shape_size, const ge::DataType dt, size_t &total_size)
  ```
* 传入数据类型和Tensor长度，创建Tensor

  ```cpp
  static std::unique_ptr<uint8_t[]> CreateFollowing(const ge::DataType dt, const size_t tensor_size, size_t &total_size)
  ```

## 参数说明

**表1** 参数说明（传入元素个数和数据类型，创建Tensor）

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| shape\_size | 输入 | 元素个数。 |
| dt | 输入 | 数据类型，[DataType](cannkit-ge-datatype.md)类型。 |
| total\_size | 输出 | 创建出的Tensor在内存中的长度。包含Tensor对象的长度和Tensor数据的长度。 |

**表2** 参数说明（传入数据类型和Tensor长度，创建Tensor）

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| dt | 输入 | 数据类型，[DataType](cannkit-ge-datatype.md)类型。 |
| tensor\_size | 输入 | Tensor数据的长度。单位为字节。 |
| total\_size | 输出 | 创建出的Tensor在内存中的长度。和tensor\_size参数不同，total\_size包含Tensor对象的长度和Tensor数据的长度。单位为字节。 |

## 返回值

创建的Tensor指针。

## 约束说明

无

## 调用示例

```cpp
size_t total_size;
auto tensor_holder = Tensor::CreateFollowing(shape_size, tensor_desc.GetDataType(), total_size);
```
