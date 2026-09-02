---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1609
title: 页面上图片展示不完整
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面上图片展示不完整
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c8382f974f334f7978066c5b9915b141fc4e729ffcbd28ed40b05a1b0eec739a
---

## 问题现象

加载应用内的图片时，图片显示不完整。

图一：完整显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/71NbwiWuS0e5bLO4X7T31Q/zh-cn_image_0000002658972591.png "点击放大")

图二：显示不完整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/5CRITqW2STerRo8t1TM6uQ/zh-cn_image_0000002658852639.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。
* [objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)：设置图片的缩放类型。
* [background-size](../quickApp-References/quickapp-common-styles-0000001170210009.md)可以通过设置背景尺寸来控制图片的缩放比例，以实现不同的背景填充效果。

## 问题定位

1. 使用DevEco Testing查看问题组件，该组件为Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/SJQ7OQA1TGSG38ctvfnjPw/zh-cn_image_0000002628773276.png "点击放大")
2. 查看Image组件的objectFit属性是否正确，图片的缩放模式选用不当可能造成图片显示不完整，如果图片缩放模式设置为cover，图片会保持宽高比，并填满容器，超出部分会被裁剪。

   ```ts
   @Entry
   @Component
   struct ImgEmpty {

     build() {
       Stack() {
         Image($r('app.media.product')) // $r('app.media.product')需要替换为开发者需要的图片资源文件
           .width(300)
           .height(200)
           .objectFit(ImageFit.Cover) // 图片保持宽高比并填满容器，超出部分会被裁剪
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 分析结论

图片使用了不合适的缩放模式，造成超出容器的部分被裁剪，导致图片显示不完整。

## 修改建议

objectFit属性设置为Contain，该缩放模式会保持宽高比，完整显示图片。

```ts
@Entry
@Component
struct ImgTruncation {
  build() {
    Stack() {
      Image($r('app.media.product')) // $r('app.media.product')需要替换为开发者需要的图片资源文件
        .width(300)
        .height(200)
        .objectFit(ImageFit.Contain) // 保持宽高比，完整显示图片
    }
    .width('100%')
    .height('100%');
  }
}
```
