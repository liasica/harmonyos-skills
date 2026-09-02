---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-532
title: 播放视频时，画面展示不全，存在截断的情况
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 播放视频时，画面展示不全，存在截断的情况
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c7c5c7d22e8f3b897a0c7418c67acdb0f0849c78a0d9443bd438dd78f433e4be
---

## 问题现象

视频画面显示不全，出现截断，超出页面边界，或者与页面中其他组件发生重叠。

## 背景知识

* 视频组件的主要布局参数有position，width，height和size。其中[position](../harmonyos-references/ts-universal-attributes-location.md#position)是绝对定位，确定子组件相对父组件的位置，参数为由x和y组成的数对，表示元素在x轴和y轴上的坐标，参数类型为number，单位为vp。
* [width](../harmonyos-references/ts-universal-attributes-size.md#width15)用于设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。在Row、Column、RelativeContainer等组件中，width、height设置auto表示自适应子组件。
* [size](../harmonyos-references/ts-universal-attributes-size.md#size)同样可以用于设置组件自身的宽高尺寸，参数为由width和height组成的数对，表示元素的宽度与高度。

## 问题定位

1. 通过DevEco Testing的UIView工具可以获取视频播放组件的布局信息，包含中心点的坐标（position）以及宽度（width）和高度（height）等。
2. 根据获取到的坐标，宽度和高度，计算出视频组件和其他页面组件的显示范围，判断是否重叠。如果出现重叠，则会导致部分视频内容被遮挡，显示不全，影响用户使用体验。

### 场景一

和其他组件重叠/遮挡。Video组件的y坐标是60，高度是120vp，其下方的兄弟组件y坐标是160，遮挡住了Video组件一部分内容。

```screen
Column() {
  Column() {
    Text('占位')
  }
  .width('100%')
  .height(40)
  .backgroundColor('#f1f3f5')
  .justifyContent(FlexAlign.Center)
  .borderRadius(this.radius)

  Video({
    src: this.videoSrc, // 视频资源
    posterOptions: { showFirstFrame: true } // 配置首帧送显
  })
    .position({ x: 0, y: 60 })
    .width('100%')
    .height(120)
    .controls(false) // 隐藏控制栏
    .autoPlay(true) // 自动播放
    .borderRadius(this.radius)

  Column() {
    Text('占位')
  }
  .position({ y: 160 })
  .width('100%')
  .height(`calc(100% - 160vp)`)
  .backgroundColor('#f1f3f5')
  .justifyContent(FlexAlign.Center)
  .borderRadius(this.radius)
}
.height('100%')
.width('100%')
.padding(10)
```

### 场景二

位置超出页面边界。Video组件的x坐标是40，宽度是100%，组件右侧有40vp宽的区域超出了页面。

```screen
Column() {
  Column() {
    Text('占位')
  }
  .width('100%')
  .height(40)
  .backgroundColor('#f1f3f5')
  .justifyContent(FlexAlign.Center)
  .borderRadius(this.radius)

  Video({
    src: this.videoSrc, // 视频资源
    posterOptions: { showFirstFrame: true } // 配置首帧送显
  })
    .position({ x: 40, y: 60 })
    .width('100%')
    .height(120)
    .controls(false) // 隐藏控制栏
    .autoPlay(true) // 自动播放
    .borderRadius(this.radius)

  Column() {
    Text('占位')
  }
  .position({ y: 200 })
  .width('100%')
  .height(`calc(100% - 200vp)`)
  .backgroundColor('#f1f3f5')
  .justifyContent(FlexAlign.Center)
  .borderRadius(this.radius)
}
.height('100%')
.width('100%')
.padding(10)
```

### 场景三

宽度或高度错误超出页面边界。Video组件的宽度是500vp，超出了一般手机屏幕的宽度，组件右侧存在部分区域无法显示在屏幕上。

```screen
Column() {
  Column() {
    Text('占位')
  }
  .width('100%')
  .height(40)
  .backgroundColor('#f1f3f5')
  .justifyContent(FlexAlign.Center)
  .borderRadius(this.radius)

  Video({
    src: this.videoSrc, // 视频资源
    posterOptions: { showFirstFrame: true } // 配置首帧送显
  })
    .position({ x: 0, y: 60 })
    .width(500)
    .height(120)
    .controls(false) // 隐藏控制栏
    .autoPlay(true) // 自动播放
    .borderRadius(this.radius)

  Column() {
    Text('占位')
  }
  .position({ y: 200 })
  .width('100%')
  .height(`calc(100% - 200vp)`)
  .backgroundColor('#f1f3f5')
  .justifyContent(FlexAlign.Center)
  .borderRadius(this.radius)
}
.height('100%')
.width('100%')
.padding(10)
```

## 分析结论

### 场景一

和其他组件重叠/遮挡。视频组件的position设置不合理，与其他页面组件发生重叠或遮挡，导致视频画面无法完整显示。

### 场景二

位置超出页面边界。视频组件的position设置错误，超出了页面边界，导致视频画面截断。

### 场景三

宽度或高度错误超出页面边界。视频组件的width或height设置错误，超出了页面边界，导致视频画面截断。

## 修改建议

需要根据页面中组件的位置、宽度等适当调整视频组件的位置、宽高。

### 场景一

和其他组件重叠/遮挡。需要根据视频组件和其他页面组件的显示范围，计算出组件间发生重叠的坐标值，适当调整position的x值或y值，避免视频被遮挡。

### 场景二

位置超出页面边界。需要根据视频的宽高调整position属性，即调整组件的位置。需要确保视频可以完整显示，不会超出页面显示区域。

### 场景三

宽度或高度错误超出页面边界。此时需要根据视频源的尺寸，对视频组件的width属性或height属性进行调整，确保小于屏幕宽度，之后视频就可以完整显示。

完整示例代码如下：

```screen
@Entry
@Component
struct VideoLayoutTest {
  // 需要替换为实际视频文件
  videoSrc = $rawfile('example.mp4'); // 本地rawfile视频文件，该视频资源的宽高为1920*648
  videoX = 0; // video组件x坐标
  videoY = 60; // video组件y坐标
  videoWidth = '100%'; // video组件宽度，
  videoHeight = 120; // video组件高度
  parentPadding = 10; // 页面边距，顶层容器组件边距
  radius = 10; // 圆角数值
  bottomY = this.videoY + this.videoHeight + 2 * this.parentPadding; // 计算下方组件y坐标，和上组件间隔20vp

  build() {
    Column() {
      Column() {
        Text('占位')
      }
      .width('100%')
      .height(40)
      .backgroundColor('#f1f3f5')
      .justifyContent(FlexAlign.Center)
      .borderRadius(this.radius)

      Video({
        src: this.videoSrc,
        posterOptions: { showFirstFrame: true } // 配置首帧送显
      })
        .position({ x: this.videoX, y: this.videoY })
        .width(this.videoWidth)
        .height(this.videoHeight)
        // position、width、height等属性需要根据实际视频尺寸以及页面布局进行调整
        .zIndex(2) // 组件堆叠顺序，值越大显示层级越高
        .controls(false) // 隐藏控制栏
        .autoPlay(true) // 自动播放
        .borderRadius(this.radius)

      Column() {
        Text('占位')
      }
      .position({ y: this.bottomY })
      .width('100%')
      .height(`calc(100% - ${this.bottomY}vp)`)
      .backgroundColor('#f1f3f5')
      .justifyContent(FlexAlign.Center)
      .borderRadius(this.radius)
    }
    .height('100%')
    .width('100%')
    .padding(this.parentPadding)
  }
}
```
