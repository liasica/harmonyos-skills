---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-rotate-faq
title: 如何获取图片的旋转角度信息
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit常见问题 > 如何获取图片的旋转角度信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b0c1431766c4f84bd567951b7cb38754bb7a4a73db3ee46fd149e1d5ea5c571d
---

## 图片旋转角度介绍

在数码摄影中，拍摄设备（如手机、相机）会将图片的旋转角度（方向）信息保存在图片的Exif（Exchangeable image file format）数据的Orientation字段。

该信息不会直接改变图片的像素内容，但会告诉图像查看器如何正确地显示图像方向。

Exif标准中定义了8个Orientation值和它们的字符串表示。

要将图片正确显示需要执行与之对应的特定的操作，如下表所示：

| 值 | 字符串表示 | 要将图片正确显示需要执行的操作 |
| --- | --- | --- |
| 1 | "Top-left" | 正常方向（无需旋转）。 |
| 2 | "Top-right" | 水平镜像翻转。 |
| 3 | "Bottom-right" | 旋转180°。 |
| 4 | "Bottom-left" | 垂直镜像翻转。 |
| 5 | "Left-top" | 先水平镜像翻转，再顺时针旋转270°。 |
| 6 | "Right-top" | 顺时针旋转90°。 |
| 7 | "Right-bottom" | 先水平镜像翻转，再顺时针旋转90°。 |
| 8 | "Left-bottom" | 顺时针旋转270°。 |

ArkTS场景下读取和编辑图片的旋转角度信息，可参考：[编辑图片Exif信息](image-tool.md)，对应的propertyKey需要设置为：ORIENTATION。

C/C++场景下读取和编辑图片的旋转角度信息，可参考：[使用Image\_NativeModule编辑图片Exif信息](image-tool-c.md)，对应的key需要设置为：OHOS\_IMAGE\_PROPERTY\_ORIENTATION。

## 常见问题

### 读取图片旋转角度为空怎么办

部分图片可能没有Exif数据，或者Exif数据中没有写入Orientation字段，这些图片无需旋转（与Orientation值为1的情况保持一致）。

### 为什么会出现Exif数据丢失

与图片来源有关，网络传输的图片可能进行了二次编码，在编码时未保存Exif数据，导致无法获取旋转角度。

### 图片编码时，如何保存Exif数据

在调用图片编码接口时，需要设置[packingOption](../harmonyos-references/arkts-apis-image-i.md#packingoption)的needsPackProperties属性为true（该属性的默认值为false）。
