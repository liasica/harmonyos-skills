---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-773
title: Progress组件实现时钟样式进度条
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Progress组件实现时钟样式进度条
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3a4e0bcc3b9695dc57493eaa648dee1dd4658c1fe6af98939220fa8a9bdf6fa5
---

## 问题现象

如何实现一个360度圆形刻度盘，并在圆周上添加一根跟随旋转的白色虚线（类似钟表的指针）？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/1wDwVzS8RWi3N8rZtLuKJA/zh-cn_image_0000002658915021.gif "点击放大")

## 背景知识

[进度条 (Progress)](../harmonyos-guides/arkts-common-components-progress-indicator.md)：Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参考[Progress](../harmonyos-references/ts-basic-components-progress.md)。

## 解决方案

圆环进度条参考官方文档中的[进度条](../harmonyos-guides/arkts-common-components-progress-indicator.md) ，虚线通过Divider()组件设置属性，旋转角度跟随进度条进度。

```screen
@Entry
@Component
struct Index {
  @State rotateAngle: number = 0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }

  build() {
    Column() {
      Column() {
        Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
          .backgroundColor(Color.Black)
          .style({ scaleCount: 20, scaleWidth: 5 })

        Divider()
          .height(40)
          .width(0)
          .borderWidth(2)
          .margin({ top: -90 }) // 通过centerX、centerY设置旋转中心
          .rotate({
            centerX: '100%',
            centerY: '100%',
            angle: this.rotateAngle
          })
          .onAppear(() => {
            this.uiContext?.animateTo({
              duration: 3000,
              curve: Curve.Linear,
              iterations: -1, // 设置-1表示动画无限循环
            }, () => {
              this.rotateAngle = 360 * 20 / 150;
            });
          })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
}
```
