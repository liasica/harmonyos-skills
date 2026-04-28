---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-implemt-inferfunc
title: IMPLEMT_INFERFUNC
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > IMPLEMT_INFERFUNC
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9dedd4e4709df751ba305a88e0ed335d1d7c4030f21d5c052257350b1154b82e
---

## 函数功能

封装算子的InferShape函数。

该函数传入的OpType为基于Operator类派生出来的子类，会自动生成一个类型为此子类的对象op，可以使用子类的成员函数获取输入输出描述的方法，从而进行InferShape的实现。

基于OpType派生出来的子类op的成员函数如下。

* op.set\_input\_\_x\_(Operator &v, const string &srcName)：将网络中算子v的输出srcName设置为当前算子的输入x。
* op.get\_input\_desc\_\_x\_()：获取该算子的输入x的描述信息，返回对象为TensorDesc类型。

  op.update\_input\_desc\_\_x\_(const TensorDesc& tensorDesc)：更新输入x的描述信息，包括shape、datatype与format。
* op.get\_output\_desc\_\_y\_()：获取该算子的输出y的描述信息，返回对象TensorDesc类型。
* op.update\_output\_desc\_\_y\_(const TensorDesc& tensorDesc)：更新输出y的描述信息，包括shape、datatype与format。
* op.get\_attr\_\_attr1\_(AscendString &val)：获取算子属性attr1的值val。

## 函数原型

```
1. IMPLEMT_INFERFUNC(op_name, func_name)
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| op\_name | 输入 | 算子类型。 |
| func\_name | 输入 | InferShape函数名，开发者自定义。 |

## 返回值

无
