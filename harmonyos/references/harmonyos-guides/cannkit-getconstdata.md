---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getconstdata
title: GetConstData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetConstData
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:67e375623f03a3452b3b74b5974810d5dffa117c6624393b3f5954e3895fd656
---

## 函数功能

如果TensorDesc是常量节点的描述，获取TensorDesc中的权重值。

## 函数原型

```
1. bool GetConstData(uint8_t **const_data_buffer, size_t &const_data_len) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| const\_data\_buffer | 输出 | 权重地址。 |
| const\_data\_len | 输出 | 权重长度。 |

## 返回值

获取成功，返回true。

获取失败，返回false。

## 异常处理

无

## 约束说明

无
