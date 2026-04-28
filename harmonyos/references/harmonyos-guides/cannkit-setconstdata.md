---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setconstdata
title: SetConstData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetConstData
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:611c3c99a8b53b25003b4074c59fc455a5e2131bbc4113b642e6b6bc797b41a3
---

## 函数功能

如果TensorDesc是常量节点的描述，向TensorDesc中设置权重值。

## 函数原型

```
1. void SetConstData(std::unique_ptr<uint8_t[]> const_data_buffer, const size_t &const_data_len);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| const\_data\_buffer | 输入 | 权重地址。 |
| const\_data\_len | 输入 | 权重长度。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
