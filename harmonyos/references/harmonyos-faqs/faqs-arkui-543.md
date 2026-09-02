---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-543
title: 长图渐变色效果未正常显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 长图渐变色效果未正常显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a2e215316081300e8111e72c5d64ee21ff0db1b10384aa0d160b7a0a6b74d7ef
---

## 问题现象

页面展示图片时通常先是展示缩略图，点击后才会显示原图。长图以缩略图样式展示时通常添加渐变色以提高用户体验。

图一：无渐变色的缩略图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/zgrL70IcQ5KAAdI4vGL4wQ/zh-cn_image_0000002658790883.png "点击放大")

图二：有渐变色的缩略图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/lcn8NyP8TIaQAoEFJuK8rQ/zh-cn_image_0000002628551518.png "点击放大")

## 背景知识

[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)：设置组件的颜色渐变效果，支持方向控制和多颜色配置。

## 问题定位

1. 通过DevEco Testing查看问题组件，发现是Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/o6SHYOZxQNSvOszfTJW04g/zh-cn_image_0000002628391622.png "点击放大")
2. 排查该Image组件的同层组件的设置，发现没有使用linearGradient设置颜色渐变的同层组件。

   ```screen
   @Entry
   @Component
   struct ImgExample {

     build() {
       Stack() {
         Image($r('app.media.long')) // $r('app.media.long')需要替换为开发者需要的图片资源文件
           .width(200)
           .height(300)
           .objectFit(ImageFit.Auto)
           // 没有使用linearGradient设置颜色渐变的同层组件
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 分析结论

Image组件没有使用linearGradient设置颜色渐变的同层组件，导致长图没有渐变色效果。

## 修改建议

添加使用linearGradient设置颜色渐变的同层组件。

```screen
@Entry
@Component
struct ImgExample {
  build() {
    Stack() {
      Stack() {
        Image($r('app.media.long')) // $r('app.media.long')需要替换为开发者需要的图片资源文件
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Auto);

        // 使用linearGradient设置颜色渐变的同层组件
        Row()
          .width('100%')
          .height('40')
          .linearGradient({
            direction: GradientDirection.Bottom,
            colors: [['#00000000', 0.0], ['#ff000000', 1.0]]
          });
      }
      .width(200)
      .height(300)
      .alignContent(Alignment.Bottom);
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/ZkpIxp9HSZ-ZtA1a80sxKw/zh-cn_image_0000002658910837.png "点击放大")
