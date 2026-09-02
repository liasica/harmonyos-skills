---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-842
title: Image动态设置圆角大小
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Image动态设置圆角大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:19635d1b6d6024d93e917c3cfc504ca20709623143e1fbc48316e292aa953334
---

## 问题现象

使用Slider组件希望实现滑动时控制Image组件圆角的变化，但滑动Slider时圆角没有改变。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/tIbyrHAPQyuMhQET4FLDwg/zh-cn_image_0000002628558546.gif "点击放大")

## 背景知识

* [clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)：用于对组件进行裁剪、遮罩处理。
* [borderRadius](../harmonyos-references/ts-universal-attributes-border.md#borderradius)：设置边框的圆角。圆角大小受组件尺寸限制，最大值为组件宽或高的一半。
* [Slider](../harmonyos-references/ts-basic-components-slider.md)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
* [$$语法](../harmonyos-guides/arkts-two-way-sync.md)：内置组件双向同步。

## 解决方案

针对滑动Slider时圆角没有改变的问题，需要注意以下事项：

* 想通过Slider组件值改变来同步改变Image组件的圆角，需要将.borderRadius()属性值和Slider组件的value值双向绑定。
* 实现圆角变化效果后如果需要图片跟随圆角值发生变化，需要给Image组件添加.clip(true)属性。

完整示例参考如下：

```screen
@Entry
@Component
struct ImageChange {
  @State radius: number = 0;

  build() {
    Column() {

      Image($r('app.media.background')) // 可根据具体场景替换为可用资源
        .width(100)
        .borderRadius(this.radius)
        .clip(true) // 裁剪超出Image组件的图片
      Column() {
        Text(this.radius + 'PX')
          .fontColor('#007AFF')
        Slider({
          min: 0,
          max: 60,
          style: SliderStyle.OutSet,
          value: $$this.radius // 双向绑定
        })
          .blockSize({ width: 20, height: 20 })
          .trackColor('#E5E5EA')
          .selectedColor('#007AFF')
          .trackThickness(6)
          .width('100%')
          .margin({
            top: 7,
            bottom: 13
          })
      }
    }
    .padding(50)
    .width('100%')
    .height('100%')
  }
}
```
