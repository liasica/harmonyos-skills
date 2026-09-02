---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opreceiver
title: OpReceiver
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpReceiver
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a91018d97bfc6590ae7e9a1d2d81bfe75dec73db33dbc94bc96c97b25c351eb
---

## 函数功能

OpReceiver构造函数，接收自定义算子的注册信息。

## 函数原型

```cpp
OpReceiver(OpRegistrationData &reg_data);
~OpReceiver();
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| reg\_data | 输入 | 需要注册的算子信息。 |

## 返回值

OpReceiver构造函数返回OpReceiver类型的对象。

## 异常处理

无

## 约束说明

无
