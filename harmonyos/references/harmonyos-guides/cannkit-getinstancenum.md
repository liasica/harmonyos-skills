---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinstancenum
title: GetInstanceNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > GetInstanceNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:034a826073e3ff1eaf24d735b5e683f5a55e57bdc15e908ef6ba9a8bda00d4b6
---

## 函数功能

获取IR定义某个输入对应的实际输入个数。

## 函数原型

```
1. uint32_t GetInstanceNum() const
```

## 参数说明

无

## 返回值

IR定义某个输入对应的实际输入个数。

## 约束说明

无

## 调用示例

```
1. // IR定义的第一个输入是动态输入，且有10个实际输入
2. AnchorInstanceInfo anchor_0(0, 10);
3. auto input_num_0 = anchor_0.GetInstanceNum(); // input_num_0 = 10
```
