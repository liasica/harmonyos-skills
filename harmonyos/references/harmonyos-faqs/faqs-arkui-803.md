---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-803
title: 在折叠屏展开态下，页面内容重叠
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 在折叠屏展开态下，页面内容重叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fcce1b60e487bc9eabd2e675b04f92e8476f352aab55bf1887394a5f166c9708
---

## 问题现象

在折叠屏展开态下，页面部分内容出现了重叠。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/lWl2fWMwQfGwMScF-QTFQQ/zh-cn_image_0000002658917107.png "点击放大")

## 背景知识

[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)：可设置组件的宽高、边距。通过设置width、height、padding、margin等尺寸通用属性调整组件尺寸。

## 问题定位

使用[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)查看页面布局，发现子组件的高度大于父组件的高度，溢出了父组件的范围。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/j_yrVzs_RPqk408eOElzFQ/zh-cn_image_0000002628397886.png "点击放大")

## 分析结论

当前页面子组件的高度大于父组件的高度，溢出了父组件的范围，导致在折叠屏展开态下，页面内容重叠。

## 修改建议

父组件不设置高度或将高度设置为auto，使父容器的高度自适应子组件的高度。示例代码如下：

```ts
@Entry
@Component
struct HeightAutoPage {
  message: string = 'Hello World';
  controller: VideoController = new VideoController();

  build() {
    Column() {
      Scroll() {
        Column() {
          Column() {
            Image($r('app.media.startIcon')) // 请替换成实际资源图片
              .width('20%')
              .objectFit(ImageFit.Contain);
            Text(this.message)
              .fontSize(20)
              .fontWeight(600)
              .margin({ top: 16, bottom: 16 });
            Image($r('app.media.startIcon')) // 请替换成实际资源图片
              .width('20%')
              .objectFit(ImageFit.Contain);
            Text(this.message)
              .fontSize(20)
              .fontWeight(600)
              .margin({ top: 16, bottom: 16 });
            Image($r('app.media.startIcon')) // 请替换成实际资源图片
              .width('20%')
              .objectFit(ImageFit.Contain);
            Text(this.message)
              .fontSize(20)
              .fontWeight(600)
              .margin({ top: 16, bottom: 16 });
            Image($r('app.media.startIcon')) // 请替换成实际资源图片
              .width('20%')
              .objectFit(ImageFit.Contain);
          }
          .width('100%')
          .height('auto') // 父组件高度设置为auto，使父容器的高度自适应子组件的高度
          .margin({ top: 16 });

          Text(this.message)
            .fontSize(20)
            .fontWeight(600)
            .margin({ top: 16, bottom: 16 });
          Column()
            .width('100%')
            .height(300)
            .backgroundColor('#f1f3f5');
        }
        .justifyContent(FlexAlign.Start);
      }
      .height('100%')
      .width('100%')
      .scrollBar(BarState.Off);
    }
    .height('100%')
    .width('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/tJkJepriQQi0tQA-ma-oXw/zh-cn_image_0000002658797155.png "点击放大")
