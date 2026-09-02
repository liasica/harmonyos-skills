---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1236
title: Image动态适配Text的宽高
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Image动态适配Text的宽高
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9af2cfca54ce48df8361e397b781baae965e9e398b328505ed4457f63bcedb28
---

## 问题现象

如何实现图标自适应文本框的尺寸变化，使Image组件动态适配Text组件的宽高。

## 背景知识

* [组件区域变化事件](../harmonyos-references/ts-universal-component-area-change-event.md)onAreaChange会在组件显示的尺寸、位置等发生变化时触发，返回目标元素位置信息变化情况。
* [resizable](../harmonyos-references/ts-basic-components-image.md#resizable11)可以设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。

## 解决方案

通过onAreaChange监听Text的变化，并设置图片组件的resizable属性，设置顶部、右侧、底部、左侧的距离，使其边缘部分在图片拉伸时不会发生变化，仅图片中央区域被拉伸，从而动态调整Image的大小位置等。

```ts
@Entry
@Component
struct TextView {
  @State textWidth: Length = 0;
  @State fontSize: number = 16;

  build() {
    Column({ space: 16 }) {
      Button('increase font size')
        .margin({ top: 16 })
        .onClick(() => {
          this.fontSize += 2;
        });
      Text('这是一个Text')
        .fontSize(`${this.fontSize}fp`)
        .onAreaChange((oldValue: Area, newValue: Area) => {
          this.textWidth = newValue.width;
        })
        .padding({
          left: '5vp',
          right: '5vp'
        });
      Image($r('app.media.img1')) // 图片资源文件需自行替换
        .width(this.textWidth)
        .resizable({
          slice: {
            top: '5vp',
            right: '5vp',
            left: '5vp',
            bottom: '5vp'
          }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

实现效果如下：增大Text文本，图片对应变大。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/T98JJAIsSe-NqXsXxVy14w/zh-cn_image_0000002628753944.png "点击放大")
