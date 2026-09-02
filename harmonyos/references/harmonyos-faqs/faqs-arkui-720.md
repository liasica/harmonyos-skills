---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-720
title: 怎么解决Image组件加载图片被旋转90度的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 怎么解决Image组件加载图片被旋转90度的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:60fa2dc593c650292ceac5129668b4d894e1a47a311fcdd5932d33359b0fa2b8
---

## 问题现象

使用Image组件加载图片时，图片自动被旋转了90度，如何使图片显示方向正确。问题代码如下：

```ts
@Entry
@Component
struct ImageRotationProblem {
  build() {
    Column() {
      // 运行时请按需替换图片资源
      Image($r('app.media.startIcon'));
    };
  }
}
```

左图为正常显示效果，右图为Image加载显示效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/HFwkJPWuRnao_cmaS8xMYA/zh-cn_image_0000002658794579.png "点击放大")

## 背景知识

* [Image组件](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)属性能够设置组件旋转。可使组件在以组件左上角为坐标原点的坐标系中进行旋转。
* [orientation](../harmonyos-references/ts-basic-components-image.md#orientation14)属性能够设置图像内容的显示方向。该属性对alt占位图不生效，不支持gif和svg类型的图片。如果需要显示携带旋转角度信息或翻转信息的图片，建议使用ImageRotateOrientation.AUTO进行设置。
* [ImageSource类](../harmonyos-references/arkts-apis-image-imagesource.md)，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过createImageSource构建一个ImageSource实例。
* [EXIF（Exchangeable image file format）](../harmonyos-guides/image-tool.md)是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF格式，且需要图片包含EXIF信息。
* [图片旋转角度](../harmonyos-guides/image-rotate-faq.md#图片旋转角度介绍)在数码摄影中，拍摄设备（如手机、相机）会将图片的旋转角度（方向）信息保存在图片的Exif（Exchangeable image file format）数据的Orientation字段。

## 问题定位

1. 使用Image组件加载其他图片，检查是否为组件问题。由于“新闻”图片正常显示，确认非组件问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/U_kXHGeWTlur-_aGlTThAg/zh-cn_image_0000002628555212.png "点击放大")
2. 检查原图片Exif信息，定位其orientation属性。通过在线网站查看图片信息得知该图片的拍摄方向为逆时针旋转90度。由此，定位到图片被旋转的原因。

   | 属性 | 说明 | 值 |
   | --- | --- | --- |
   | ImageWidth | 像素宽度 | 4032 |
   | XResolution | X分辨率 | 72 |
   | YResolution | Y分辨率 | 72 |
   | Resolution | 分辨率单位 | 英寸 |
   | Orientation | 拍摄方向 | 6（逆时针旋转90°） |

## 分析结论

图片旋转是因为图像的拍摄方向属性固定为旋转90度导致的，需要旋转归位或者对图像进行其他处理。

## 修改建议

* **方案一：通过组件旋转属性，使图片显示方向正常：**

  直接给Image组件加上对应的旋转属性，使图片正常显示。因为图片的方向是逆时针90度，将Image组件顺时针旋转90度后，图片会正常显示。通过以下属性旋转：

  ```ts
  @Entry
  @Component
  struct ImageRotationOne {
    build() {
      Column() {
        // 运行时请按需替换图片资源
        Image($r('app.media.startIcon'))
          .rotate({ angle: 90 });
      };
    }
  }
  ```

  **说明** 

  这种方案只有在确定图片的方向信息时才能使用，如果是从网络加载的、不能确定方向的图片列表，该方案则不适用。
* **方案二：通过orientation属性，设置图片的显示方向：**

  利用orientation属性，[设置图像内容的显示方向](../harmonyos-references/ts-basic-components-image.md#示例21设置图像内容的显示方向)。如果需要显示携带旋转角度信息或翻转信息的图片建议使用ImageRotateOrientation.AUTO进行设置。

  ```ts
  // 运行时请按需替换图片资源
  @Entry
  @Component
  struct ImageRotationTwo {
    build() {
      Column() {
        // 运行时请按需替换图片资源
        Image($r('app.media.startIcon'))
          .orientation(ImageRotateOrientation.AUTO);
      };
    }
  }
  ```

  **说明** 

  这种方案不支持gif和svg类型的图片。
* **方案三：将图片转成ImageSource对象后读取旋转信息：**

  **思路**：读取每张图片的方向orientation信息，根据其方向，设置图片的显示方向。

  1. 使用Image Kit的createImageSource接口，将图片转换成image.ImageSource对象。
  2. 使用ImageSource的getImageProperty接口获取图片的image.PropertyKey.ORIENTATION旋转信息。
  3. 根据图片的EXIF方向信息设置orientation属性值进行旋转，使图片正常显示。

  详细代码可以参考：[获取图片的Exif信息并设置图像内容的显示方向](../harmonyos-references/ts-basic-components-image.md#示例22获取图片的exif信息并设置图像内容的显示方向)。
