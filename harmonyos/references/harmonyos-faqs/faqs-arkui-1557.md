---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1557
title: Progress如何控制平滑过渡的速率
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Progress如何控制平滑过渡的速率
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ff28cc76f2bc5134c8515a5b8ab6552b4cbea9e85d2a6201ef38ccb08ca789fd
---

## 问题现象

如何通过Progress实现进度条功能，且可以控制其过渡速率？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gSA19RF3S1OxzC_mac2BSQ/zh-cn_image_0000002658968451.gif "点击放大")

## 背景知识

* [Progress](../harmonyos-references/ts-basic-components-progress.md)：进度条组件，用于显示内容加载或操作处理等进度，通过[style](../harmonyos-references/ts-basic-components-progress.md#style8)属性可以设置进度条样式。[CommonProgressStyleOptions](../harmonyos-references/ts-basic-components-progress.md#commonprogressstyleoptions10)（进度条通用样式设置）对象中enableSmoothEffect参数可以开启/关闭进度条的平滑动效。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

为实现进度条功能，可通过修改Progress的value值来实现，若要实现控制其过渡速率可将Progress的enableSmoothEffect属性设置为false，关闭进度平滑动效，通过animateTo来设置其过渡动效。

```ts
@Entry
@Component
struct WidgetsProgress {
  @State proValue: number = 0;

  build() {
    Column() {
      Progress({ value: this.proValue, type: ProgressType.Linear })
        .width(300)
        .style({ strokeWidth: 10, enableSmoothEffect: false });
      // 当进度达到100%时显示“加载完成”文本
      Text('加载完成').visibility(this.proValue >= 100 ? Visibility.Visible : Visibility.None);
      Button('进度条++')
        .margin({ top: 5, bottom: 5 })
        .onClick(() => {
          this.getUIContext().animateTo({
            duration: 1000,
            curve: Curve.Linear,
            playMode: PlayMode.Normal
          }, () => {
            this.proValue += 10;
          });
        });
      Button('进度条重置')
        .onClick(() => {
          // 重置进度值为0
          this.proValue = 0;
        });
    }
    .width('100%')
    .margin({ top: 50 });
  }
}
```
