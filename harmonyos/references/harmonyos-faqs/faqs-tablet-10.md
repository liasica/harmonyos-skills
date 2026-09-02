---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-10
title: 平板端页面背景与字体颜色对比度不足
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板端页面背景与字体颜色对比度不足
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:61ab485208c545cc3b4ae0dee0919ecb74add753e159a339dacf9244777b5e02
---

## 问题现象

当应用在直板手机查看时，背景大小显示正常；在平板查看时，背景大小显示异常，且与字体和组件重叠。

手机查看图与平板查看图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/BgvKquFIQWS7dGzvSw_EDQ/zh-cn_image_0000002658790869.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/6Lj2XJ6ESvWQSpP8SZfK3g/zh-cn_image_0000002628551510.png "点击放大")

## 背景知识

* [Image组件](../harmonyos-references/ts-basic-components-image.md)：Image为图片组件，用于在应用中显示图片。
* 通用属性[backgroundImage](../harmonyos-references/ts-universal-attributes-background.md#backgroundimage)与[backgroundImageSize](../harmonyos-references/ts-universal-attributes-background.md#backgroundimagesize)：用于设置组件的背景图片和背景大小。

## 问题定位

1. 通过DevEco Testing查看页面结构，确认页面是否有使用Stack容器，图片是否为Image组件。
2. 选择页面容器，确认backgroundImage是否有配置资源。
3. 模拟页面结构编写demo，未针对页面尺寸大小进行监听并调整页面结构和组件尺寸，复现问题。

## 分析结论

由于页面容器设置backgroundImage背景图片，且未根据页面尺寸大小调整页面结构，导致背景图片随窗口大小铺满，与组件出现重叠。

## 修改建议

通过设置backgroundImageSize属性，限制背景图片尺寸，避免因页面尺寸变化导致背景图片显示异常。若不同的页面尺寸需要显示不同尺寸的背景图片，可以配合[断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)进行设置。

示例代码如下：

```screen
@Entry
@Component
struct ImageStretch {
  bgImage: Resource = $r('app.media.backgroundcolorgray'); // 背景图更换为实际图片

  build() {
    Scroll() {
      Column() {
        Column() {
          TextInput({ placeholder: 'Account' })
            .width('95%')
            .borderColor(Color.Gray)
            .borderWidth(0.5)
            .backgroundColor(Color.White)
            .margin({ bottom: 10 });

          TextInput({ placeholder: 'Password' })
            .width('95%')
            .borderColor(Color.Gray)
            .borderWidth(0.5)
            .backgroundColor(Color.White);
        }
        .height('60%')
        .justifyContent(FlexAlign.End)
        .margin({ bottom: 20 });

        Button('Login')
          .type(ButtonType.Capsule)
          .width('60%');
      }
      .height('100%')
      .justifyContent(FlexAlign.Start);
    }
    .height('100%')
    .width('100%')
    .backgroundImage(this.bgImage)
    // 设置backgroundImageSize属性，限制背景图片尺寸
    .backgroundImageSize({ height: 258, width: '100%' })
    .expandSafeArea([SafeAreaType.SYSTEM]);
  }
}
```
