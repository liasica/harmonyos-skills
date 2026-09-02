---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-75
title: 如何解决HAR包资源被覆盖问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何解决HAR包资源被覆盖问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b3f0b73cbf53fea58a83c91d2c11120e2b9e8e54cbf9760f80591ef74c96e8af
---

## 问题现象

了解到HAR中的资源优先级最低，如何规避HAR包资源被覆盖问题？

## 背景知识

在编译构建HAP时，DevEco Studio会从HAP模块及依赖的模块中收集资源文件，如果不同模块下的资源文件出现重名冲突时，[DevEco Studio会按照以下优先级进行覆盖（优先级由高到低）](../harmonyos-guides/har-package.md#导出资源)：

* AppScope（仅Stage模型支持）。
* HAP包自身模块。
* 依赖的HAR模块，如果依赖的多个HAR之间有资源冲突，会按照工程oh-package.json5中dependencies下的依赖顺序进行覆盖，依赖顺序在前的优先级较高。例如下方示例中dayjs和lottie中包含同名文件时，会优先使用dayjs中的资源。

```json
// oh-package.json5
{
  "dependencies": {
    "dayjs": "^1.10.4",
    "lottie": "^2.0.0"
  }
}
```

## 解决方案

* 在HAR包中为所有资源（如图片、字符串、颜色等）添加唯一前缀（如模块名缩写），之后就可以指定引用HAR包中的资源。
* 为不同HAR模块创建专属的资源子目录，将HAR包中的资源按功能或模块分类存放。
* 使用别名引用资源，避免硬编码资源ID。
