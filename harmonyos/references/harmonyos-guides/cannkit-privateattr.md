---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-privateattr
title: PrivateAttr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > PrivateAttr
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b89b8075394a79d45de078623755e1bbc5ea0aa0456ab58190689ae3d34c94f9
---

## 函数功能

用于注册算子的私有属性。

算子的属性包含属性名以及属性值。

通常情况下，注册算子的私有属性时开发者需要同时指定私有属性的名字**private\_attr**以及该属性的值**private\_attr\_val**，此处称为场景一。但是考虑到算子可能已经存在某个属性的场景，因此也支持开发者在设置该属性时只设置属性名的做法，称为场景二。所以提供了两种类型的注册函数，分别对应上述两种场景。

对于场景一，若算子已存在某个属性，且开发者重新设置了该属性值，那么该算子的已有属性值将被开发者注册的属性覆盖。

对于场景二，如果算子不存在某个属性，且开发者仅设置了属性名，那么在后续获取算子私有属性列表流程时会存在该属性无法找到的错误。

## 函数原型

```cpp
// 仅设置私有属性名的接口
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr);
// 同时设置属性名以及属性值的接口
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr, int64_t private_attr_val);
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr, const std::vector<int64_t> &private_attr_val);
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr, const ge::char_t *private_attr_val);
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr, ge::float32_t private_attr_val);
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr, bool private_attr_val);
OpImplRegisterV2 &PrivateAttr(const ge::char_t *private_attr, const std::vector<ge::float32_t> &private_attr_val);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| private\_attr | 输入 | 需要注册的私有属性名。 |
| private\_attr\_val | 输入 | 需要注册的私有属性名对应的属性值。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了私有属性。

## 约束说明

无
