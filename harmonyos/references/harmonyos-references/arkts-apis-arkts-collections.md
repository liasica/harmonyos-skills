---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T07:59:50+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:f10933b0692dc6b652e1ca4742b9e08e84344015ee2880132d965ec841f1bd62
---

本模块提供的ArkTS容器集，可以用于并发场景下的高性能数据传递。功能与JavaScript内建的对应容器类似，但ArkTS容器实例无法通过"."或者"[]"添加或更新属性。

ArkTS容器在多个并发实例间传递时，其默认行为是引用传递，支持多个并发实例可以同时操作同一个容器实例。另外，也支持拷贝传递，即每个并发实例持有一个ArkTS容器实例。

ArkTS容器并不是线程安全的，内部使用了fail-fast（快速失败）机制：当检测多个并发实例同时对容器进行结构性改变时，会触发异常。因此，在多线程读写容器时，容器使用方需要使用ArkTS提供的异步锁机制保证ArkTS容器的安全访问。

当前ArkTS容器集主要包含以下几种容器：[Array](arkts-apis-arkts-collections-array.md)、[Map](arkts-apis-arkts-collections-map.md)、[Set](arkts-apis-arkts-collections-set.md)、TypedArray（[Int8Array](arkts-apis-arkts-collections-int8array.md)、[Uint8Array](arkts-apis-arkts-collections-uint8array.md)、[Int16Array](arkts-apis-arkts-collections-int16array.md)、[Uint16Array](arkts-apis-arkts-collections-uint16array.md)、[Int32Array](arkts-apis-arkts-collections-int32array.md)、[Uint32Array](arkts-apis-arkts-collections-uint32array.md)、[Uint8ClampedArray](arkts-apis-arkts-collections-uint8clampedarray.md)、[Float32Array](arkts-apis-arkts-collections-float32array.md)）、[ArrayBuffer](arkts-apis-arkts-collections-arraybuffer.md)、[BitVector](arkts-apis-arkts-collections-bitvector.md)、[ConcatArray](arkts-apis-arkts-collections-concatarray.md)。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

```
1. import { collections } from '@kit.ArkTS';
```
