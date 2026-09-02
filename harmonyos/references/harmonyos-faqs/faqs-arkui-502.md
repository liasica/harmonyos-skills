---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-502
title: 图片全屏预览蒙层未遮住背景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 图片全屏预览蒙层未遮住背景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:54c941f2f7625acd9c763d4435c4d8f7fac665d308848f8f749aa4c373051130
---

## 问题现象

点击图片进行全屏预览，蒙层未遮住背景，导致背景内容仍可查看。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/elOnq3MrSTWpX2u74G0rVg/zh-cn_image_0000002658907829.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/gTiLPKoNTpKbFRE5_SypYw/zh-cn_image_0000002658787893.gif "点击放大")

## 背景知识

[层叠布局](../harmonyos-guides/arkts-layout-development-stack-layout.md)（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过Stack容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

## 问题定位

1. 排查是否使用Stack布局，添加了一个类似蒙层的背景色。
2. 排查控制显隐的变量是否只对蒙层进行了控制。

```ts
@Entry
@Component
struct ImagePage {
  @State isFullScreen: boolean = false;

  build() {
    Column() {
      Stack() {
        if (this.isFullScreen) {
          Column() {
            Image($r('app.media.startIcon'))   // 大图
              .width(200)
              .height(200)
          }
          .height('100%')
          .width('100%')
          .alignItems(HorizontalAlign.Center)
          .justifyContent(FlexAlign.Center)
          .backgroundColor(this.isFullScreen ? '#ffb5b5b5' : '') // 蒙层的背景色
        }
        Column() {
          Image($r('app.media.startIcon')) // 小图
            .width(40)
            .height(40)
            .onClick(() => {
              this.isFullScreen = true;
            })

        }
        .onClick(() => {
          this.isFullScreen = false;
        })
        .height('100%')
        .width('100%')
      }

    }
    .height('100%')
    .width('100%')
  }
}
```

## 分析结论

1. 使用Stack布局添加一个蒙层背景。
2. 未对背景模块进行显隐控制，导致蒙层模块和背景同时展示。

## 修改建议

通过添加显隐变量，预览时不展示背景模块。

```ts
@Entry
@Component
struct FullScreenImagePage {
  @State isFullScreen: boolean = false;

  build() {
    Column() {
      Stack() {
        if (this.isFullScreen) {
          Column() {
            Image($r('app.media.startIcon'))
              .width(200)
              .height(200)
          }
          .height('100%')
          .width('100%')
          .alignItems(HorizontalAlign.Center)
          .justifyContent(FlexAlign.Center)
          .backgroundColor(this.isFullScreen ? '#FF808080' : '')  // 使用Stack布局添加一个蒙层背景。
        }
        Column() {
          // 通过添加显隐变量，预览时不展示背景模块
          if (!this.isFullScreen) {
            Image($r('app.media.startIcon'))
              .width(40)
              .height(40)
              .onClick(() => {
                this.isFullScreen = true;
              })
          }

        }
        .onClick(() => {
          this.isFullScreen = false;
        })
        .height('100%')
        .width('100%')
      }

    }
    .height('100%')
    .width('100%')
  }
}
```
