---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-894
title: Image加载本地图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Image加载本地图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:31cb94ff917e62a02d5f7e796490d930cddf220d9a786e8091eaf82703567761
---

## 问题现象

如何使用Image组件加载本地图片？

## 背景知识

[Image](../harmonyos-references/ts-basic-components-image.md)：Image为图片组件，常用于在应用中显示图片。Image支持加载[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)、[ResourceStr](../harmonyos-references/ts-types.md#resourcestr)和[DrawableDescriptor](../harmonyos-references/ts-basic-components-image.md#drawabledescriptor10)类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式，不支持apng和svga格式。

## 解决方案

* 方案一、通过Resource资源管理加载（推荐）。
  + 将图片放置在resources/base/media或resources/rawfile目录下。
  + 使用$r('app.media.图片名')。
  + 使用$rawfile('图片路径')引用资源。
  + 特点：
    - 跨模块/包访问：Resource方式支持跨模块调用。
    - 资源校验：rawfile目录下的图片会进行资源校验，不支持动态拼接文件名。
    - 性能优化：底层自动处理资源缩放和格式适配。
* 方案二、通过本地路径直接引用。
  + 将图片放在ets目录下的任意位置（如ets/images/）。

    新建工程或模块时，默认配置enable字段并且值为false，即默认不打包ets目录下的资源文件。需要在entry/build-profile.json5中将"copyCodeResource": {"enable": false}的false改为true。详细参考：[resOptions](../harmonyos-guides/ide-hvigor-build-profile.md#section754823013348)资源编译配置项。
  + 特点：
    - 灵活性：支持动态拼接路径（如'images/'+fileName）。
    - 限制如下：
    - 不支持跨模块调用。
    - 修改图片文件需先删除再创建同名文件，否则可能导致崩溃。
* 方案三、通过base64字符串加载。(注意：需要将this.base64ImageData替换成对应的图片资源)
  + 实现方式：

    ```ts
    Image('data:image/jpg;base64,' + this.base64ImageData)
    ```
  + 特点：
    - 适合加载小型图片或需要动态生成的图片。
    - 需注意字符串长度对性能的影响。

## 常见FAQ

Q：Image组件如何加载apng图片？

A：可以通过[ohos\_apng](https://gitee.com/openharmony-sig/ohos_apng)库来实现。

## 总结

| 方案 | 适用场景 | 跨模块支持 | 动态路径 | 资源校验 | 性能优化 |
| --- | --- | --- | --- | --- | --- |
| Resource资源管理 | 全局/多模块共用图片 | ✔️ | ❌ | ✔️ | ✔️ |
| $rawfile方法 | rawfile目录固定资源 | ✔️ | ❌ | ✔️ | ✔️ |
| 本地路径引用 | 简单本地图片、动态路径 | ❌ | ✔️ | ❌ | ❌ |
| Base64字符串 | 小图/动态生成图片 | ✔️ | ❌ | ❌ | ❌ |

建议：

* 通用图片推荐使用Resource资源管理。
* 需要动态加载时选择本地路径引用。
* 优先使用官方推荐的Resource和rawfile方式以保证兼容性和稳定性。
