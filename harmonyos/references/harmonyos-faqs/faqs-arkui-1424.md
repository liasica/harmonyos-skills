---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1424
title: Image加载失败时显示不同图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Image加载失败时显示不同图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aea4b39493030ca08fdbc909acee816d7f4fdefbb9c708f5b013b563f804593b
---

## 问题现象

如何在Image组件加载失败时，将加载中的图片替换为失败状态的图片？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/jvFeqMJUS2uAR-ISSEFdkg/zh-cn_image_0000002628603744.gif "点击放大")

## 背景知识

[Image](../harmonyos-references/ts-basic-components-image.md)是图片组件，通过图片数据源获取图片，用于后续渲染展示。当加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束；加载成功且组件不设置宽高时，其显示大小自适应父组件。

## 解决方案

引入状态变量控制图片的加载状态，当加载失败时切换状态为“error”，具体步骤如下：

1. 引入状态变量status，并设置初始值“loading”。
2. 通过alt设置图片加载时显示的占位图，并通过状态变量status控制图片变化。
3. 在回调函数onError中设置状态变量status为“error”，实现图片切换功能。

完整示例参考如下：

```screen
@Entry
@Component
struct ImageComponentExample {
  @State status: string = 'loading';
  @State loadingImg: Resource = $r('sys.media.clone_app_badge_1');
  @State errorImg: Resource = $r('sys.media.clone_app_badge_2');

  build() {
    Column() {
      Image('')
        .width(300)
        .height(300)
        .margin(15)
        .alt(this.status === 'loading' ? this.loadingImg : this.errorImg)
        .onError(() => {
          // 通过定时器延迟3s，方便观察加载中和加载失败过程图片的切换
          setTimeout(() => {
            this.status = 'error';
          }, 3000);
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
