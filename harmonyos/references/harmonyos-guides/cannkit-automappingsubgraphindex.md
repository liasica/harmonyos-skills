---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingsubgraphindex
title: AutoMappingSubgraphIndex
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > AutoMappingSubgraphIndex
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b4f8acd9cd26adc441f0e482c1f2b2e1bb4f45a94f6438f27d32741295f35fd5
---

## 函数功能

设置子图的输入输出和主图对应父节点输入输出的对应关系。

## 函数原型

```
1. Status AutoMappingSubgraphIndex(const ge::Graph &graph,
2. const std::function<int32_t(int32_t data_index)> &input,
3. const std::function<int32_t(int32_t netoutput_index)> &output)
4. Status AutoMappingSubgraphIndex(const ge::Graph &graph,
5. const std::function<Status(int32_t data_index, int32_t &parent_input_index)> &input,
6. const std::function<Status(int32_t netoutput_index, int32_t &parent_output_index)> &output)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| graph | 输入 | 子图对象 |
| input | 输入 | 输入对应关系函数 |
| output | 输入 | 输出对应关系函数 |

## 约束说明

无
