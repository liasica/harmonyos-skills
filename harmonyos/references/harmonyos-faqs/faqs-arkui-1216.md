---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1216
title: 移除bindPopup弹窗的阴影效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 移除bindPopup弹窗的阴影效果
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5eb6925e82dcf0841c50fe68361b11e09012b31b7f4e2c7bdc4195df9a0e0d18
---

## 问题现象

如何移除bindPopup弹窗的阴影效果？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/LTR43xnqQImAgtowSmamfg/zh-cn_image_0000002628753486.png?HW-CC-KV=V1&HW-CC-Date=20261112T233150Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD77E50F5C525B1C944A6648BC535274CFCC5AE8450AF75C06C2402306218376 "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/-Cwda_2mSlyqkUptYr2hDQ/zh-cn_image_0000002658952799.png?HW-CC-KV=V1&HW-CC-Date=20261112T233150Z&HW-CC-Expire=31536000000&HW-CC-Sign=0900D58BC78B6D7D199F267C5E69ABFAF6E479DEB0B5AA4A743FBC47270195B4 "点击放大")

## 背景知识

* [ShadowOptions](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)：阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。
* [阴影效果](../harmonyos-guides/arkts-shadow-effect.md)：阴影接口shadow可以为当前组件添加阴影效果。

## 解决方案

通过配置ShadowOptions实现阴影效果的灵活控制。在ShadowOptions模式中，当满足radius设置为0时，即可实现无阴影效果。

```screen
@Entry
@Component
struct PopupExample {
  @State customPopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button('popup')
        .margin({ top: 50 })
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          message: 'this is a popup',
          arrowHeight: 20,
          arrowWidth: 20,
          radius: 20,
          shadow: {
            radius: 0
          },
        });
    }
    .width('100%');
  }
}
```
