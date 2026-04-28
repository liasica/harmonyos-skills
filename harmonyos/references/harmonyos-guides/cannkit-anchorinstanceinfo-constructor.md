---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-anchorinstanceinfo-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > 构造函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:acbfa90198528ef01d4292d6428d94d442eb709f8c62839c939a5de31ca3703c
---

## 函数功能

提供了默认的构造函数以及指定了两个数据成员信息的构造函数。

## 函数原型

```
1. AnchorInstanceInfo()
2. AnchorInstanceInfo(const uint32_t instance_start, const uint32_t instantiation_num)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| instance\_start | 输入 | 指定了本对象的instance\_start\_。 |
| instantiation\_num | 输入 | 指定了本对象的instantiation\_num\_。 |

## 返回值

返回一个AnchorInstanceInfo对象。

## 约束说明

无

## 调用示例

```
1. // IR定义的第一个输入是动态输入，且有10个实际输入。
2. AnchorInstanceInfo anchor_0(0, 10);
```
