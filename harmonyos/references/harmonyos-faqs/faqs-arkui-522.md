---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-522
title: Progress组件起点与终点样式重叠及白边问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Progress组件起点与终点样式重叠及白边问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0fdddcfa994100ebc0c32f2c7b77783c095631dd294a2c4cb93ada2c0caa3c1d
---

## 问题现象

采用Progress组件设置环形进度条，运行时存在以下问题：

1. 进度值为100时起点与终点样式重叠形成一个点，如何使该点消失。
2. 进度条已经走过的边上有一点白边，如何去掉该白边？

问题代码示例参考如下：

```ts
@Entry
@Component
export struct Index {
  @State remainingTime: number = 0; // 剩余时间（默认10秒）

  aboutToAppear(): void {
    let timer: number
    timer = setInterval(() => {
      this.remainingTime += 1
      if (this.remainingTime == 100) {
        clearInterval(timer)
      }
    }, 50)
  }

  build() {
    Column() {
      Stack() { // 创建垂直布局容器
        Column() {
          Progress({
            value: this.remainingTime, // 设置进度
            total: 100, // 最大进度为100
            type: ProgressType.Ring, // 使用环形进度条
          })
            .style({ strokeWidth: 20 })
            .rotate({ angle: 90 })
            .color('#800a59f7')
            .backgroundColor('#fff')
            .width(300)
            .aspectRatio(1)
            .animation({ duration: 10 })
        }
        .justifyContent(FlexAlign.Center)
        .borderRadius(200)
        .backgroundColor(`rgba('10, 89, 247, 0.5')`)
      }
      .width(350)
      .aspectRatio(1)
      .borderRadius(200)
      .backgroundColor('#800a59f7')
      .alignContent(Alignment.Center)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/pn35qMjmShaL6gd9Tq9bpw/zh-cn_image_0000002658790419.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/iw3bZYZqTsy6d0u-npmOoA/zh-cn_image_0000002628551060.png "点击放大")

## 背景知识

[Progress](../harmonyos-references/ts-basic-components-progress.md)进度条组件，用于显示内容加载或操作处理等进度。Progress组件的[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)属性是直接添加在Progress组件上，生效进度条的底色。如需设置整个Progress组件的背景色，需要在外层容器上设置backgroundColor，并将Progress组件嵌入到容器中。

## 解决方案

1. 针对问题一的解决方案：外层Stack容器的backgroundColor和Progress组件进度条颜色设置了透明度，颜色叠加导致进度值为100时起点与终点样式重叠形成一个点。建议将外层Stack容器的backgroundColor和Progress组件底色设置成相同且不透明的颜色。
2. 针对问题二的解决方案：设置进度条前景色为白色，Progress组件底色设置与外层容器相同，进度值改为从100到0，由此解决白边的问题。此时进度条旋转方向与原代码相反，设置direction(Direction.Rtl)翻转Progress组件，实现与原效果一致。

完整示例参考如下：

```ts
@Entry
@Component
struct ProgressIndex {
  @State remainingTime: number = 100;

  aboutToAppear(): void {
    let timer: number;
    timer = setInterval(() => {
      this.remainingTime--;
      if (this.remainingTime === 0) {
        clearInterval(timer);
      }
    }, 50);
  }

  build() {
    Column() {
      Stack() { // 创建垂直布局容器
        Column() {
          Progress({
            value: this.remainingTime, // 设置进度
            total: 100, // 最大进度为100
            type: ProgressType.Ring, // 使用环形进度条
          })
            .style({ strokeWidth: 20 })
            .rotate({ angle: 90 })
            // 设置进度条前景色为白色
            .color('#fff')
            // 1、问题一，将外层容器backgroundColor和Progress组件底色设置成相同且不透明的颜色
            // 2、Progress组件底色设置与外层容器相同
            .backgroundColor('#0a59f7')
            // 设置翻转
            .direction(Direction.Rtl)
            .width(300)
            .aspectRatio(1)
            .animation({ duration: 10 });
        }
        .justifyContent(FlexAlign.Center)
        .borderRadius(200);
      }
      .width(350)
      .aspectRatio(1)
      .borderRadius(200)
      // 问题一与问题二都需将外层容器backgroundColor修改为不透明相同颜色
      .backgroundColor('#0a59f7')
      .alignContent(Alignment.Center);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
