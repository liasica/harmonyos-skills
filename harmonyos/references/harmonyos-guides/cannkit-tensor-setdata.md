---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdata
title: SetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetData
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5c627c744a3250a5673d9b9df7d306a16a231dbd7af6b4061cf9ba4423f3eb7
---

## 函数功能

向Tensor中设置数据。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus SetData(std::vector<uint8_t> &&data);
graphStatus SetData(const std::vector<uint8_t> &data);
graphStatus SetData(const uint8_t *data, size_t size);
graphStatus SetData(const std::string &data);
graphStatus SetData(const char_t *data);
graphStatus SetData(const std::vector<std::string> &data);
graphStatus SetData(const std::vector<AscendString> &datas);
graphStatus SetData(uint8_t *data, size_t size, const Tensor::DeleteFunc &deleter_func);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| data/datas | 输入 | 需设置的数据。 |
| size | 输入 | 数据的长度，单位为字节。 |
| deleter\_func | 输入 | 用于释放data数据。  using DeleteFunc = std::function<void(uint8\_t \*)>; |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
