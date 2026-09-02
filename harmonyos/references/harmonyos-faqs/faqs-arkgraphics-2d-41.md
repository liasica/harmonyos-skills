---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-41
title: 如何为图片、视频添加水印
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何为图片、视频添加水印
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:7e98661f160d1de3e321e720851f3fe16175844a768bd301f9e94b7308642f0c
---

## 问题现象

在图片、视频绘制过程中，如何添加水印（文字或emoji表情）？

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)：在当前组件上，增加遮罩文本或者叠加自定义组件以及ComponentContent作为该组件的浮层。浮层的定位同样基于当前组件进行计算。浮层不通过组件树进行渲染，部分接口（例如getRectangleById）不支持获取浮层中的组件。
* [mp4parser](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)：一个读取、写入操作音视频文件编辑的工具。可通过ohpm install @ohos/mp4parser安装。
* [OpenGL](../harmonyos-references/opengl.md)：跨平台的图形API，用于为3D图形处理硬件指定标准的软件接口。

## 解决方案

* 图片添加水印。
  + 方案一：使用[overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)属性或[Stack](../harmonyos-references/ts-container-stack.md)布局，将水印图文（支持emoji表情）覆盖在原图上层显示。
  + 方案二：使用[图片编解码](../harmonyos-guides/image-decoding.md)获取图片的像素数据信息，将获取的像素数据创建新的PixelMap实例应用到画布上进行绘制，最后使用[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)获取绘制后的图片，并将绘制后图片写进指定文件中。

    **注**：OffscreenCanvas默认单位是vp，而PixelMap宽高是px，在创建OffscreenCanvas的时候将OffscreenCanvas宽高按vp和px比例缩放转换单位，即可避免绘制后的图片内存变大。

    完整示例可参考[官方文档](../best-practices/bpta-add-watermark.md#section580010194206)及[示例demo](https://gitee.com/harmonyos_samples/watermark/tree/master)。

  两种方案对比：

  | 方案 | 性能 | 是否修改源数据 | 适用场景 |
  | --- | --- | --- | --- |
  | 方案一 | 在UI层进行布局操作，使用简单，性能较好。 | 不会修改图像源数据。如果用户保存图片，水印不会被保存。 | 1. 图像原始数据不能被修改的场景；  2. 图片不需要保存的场景，如数据预览等。 |
  | 方案二 | 需要对图片进行编解码和像素数据处理，尤其是在处理大图片或多张图片时，性能开销较大。 | 水印会嵌入到图片的像素数据中，会修改图像原始数据，生成新的图片文件，水印会永久保存在图片中。 | 适用于需要将水印永久保存在图片中的场景，如版权保护、标记等。 |
* 视频添加水印。
  + 方案一：通过[Stack](../harmonyos-references/ts-container-stack.md)组件或[overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)属性实现图片水印效果（支持emoji表情），使用第三方库[mp4parser](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用FFmpeg命令合成加水印的视频。完整示例可以参考[视频静态水印添加](../architecture-guides/video_water_mark-0000002408013854.md)。
  + 方案二：通过Drawing模块绘制水印，使用glTexImage2D方法将水印纹理（支持emoji表情）与视频纹理绑定完成水印添加，最终通过XComponent进行显示。完整示例可参考[视频添加水印](https://gitee.com/harmonyos_samples/video-water-mark/blob/master/README.md)。**注**：[OH\_Drawing\_TypographyHandlerAddText](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_typographyhandleraddtext)接口中入参为char\*，只能输入单字节编码表示的emoji表情，不可以传入u16\_string表示的emoji表情。

  两种方案对比：

  | 方案 | 是否修改源数据 | 适用场景 |
  | --- | --- | --- |
  | 方案一 | 水印会嵌入到视频文件中，会修改图像原始数据，生成新的视频文件，水印会永久保存在视频中。 | 适用于需动态调整水印位置（如用户拖拽）、视频编辑类应用（如添加多个贴纸/文字）等。 |
  | 方案二 | 支持修改，可以跟具体场景决定是否修改。 | 适用场景广泛。如添加时间、视频弹幕等。 |

## 常见FAQ

Q：视频是否支持添加动态水印效果（如弧线等动态水印）？

A：支持。可通过Native API编译实现动态水印效果。若功能无法满足实际场景，也可参考[ohos\_quick\_video\_edit](https://gitcode.com/openharmony-sig/ohos_quick_video_edit/tree/develop)获取更多视频编辑功能场景，常见功能包括视频裁剪、调整时长、添加背景音乐、去除视频原声、嵌入贴纸与动效、添加文字等。
