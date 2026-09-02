---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1268
title: 父组件及其子组件实现持续缩放效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 父组件及其子组件实现持续缩放效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81ddc78280c205722b0f553401586ed0653e3d258025d0f018a3c4cfa854f10b
---

## 问题现象

如何实现Row组件及其子组件持续缩放效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/CxMBBcKnTKu7fGfW0e1uaA/zh-cn_image_0000002658835377.png "点击放大")

## 背景知识

* [scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)：设置组件缩放。和animateTo结合实现缩放效果。
* [onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)：组件挂载显示后触发此回调。表示组件已挂载显示。

## 解决方案

实现思路如下：

1. 父组件设置scale属性，设置x，y的缩放比例。
2. 在onAppear回调里，使用[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)，设置动画时长，是否循环，实现持续缩放效果。

代码如下

```ts
@Entry
@Component
struct ScaleAnimationExample {
  @State length: Length = 0;
  @State scaleSize: number = 1;

  build() {
    Column() {
      Row() {
        Column() {
          Text('我是文本1')
          Text('我是文本2')
        }
        .height(this.length === 0 ? 'auto' : this.length)

        Column() {
          Text('我是文本1')
          Text('我是文本2')
          Text('我是文本3')
          Text('我是文本4')
        }
        .height(this.length === 0 ? 'auto' : this.length)

        Column() {
          Text('我是文本1')
          Text('我是文本2')
          Text('我是文本3')
        }
        .height(this.length === 0 ? 'auto' : this.length)
      }
      .margin(16)
      .alignItems(VerticalAlign.Top)
      .scale({ x: this.scaleSize, y: this.scaleSize })
      .onAppear(() => {
        this.getUIContext().animateTo({
          iterations: -1,
          playMode: PlayMode.Alternate
        }, () => {
          this.scaleSize = 1.3;
        });
      })
    }
    .width('91%')
    .margin(16)
    .backgroundColor('#f3f5f7')
    .borderWidth(3)
    .borderRadius(36)
    .borderColor(Color.White)
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```
