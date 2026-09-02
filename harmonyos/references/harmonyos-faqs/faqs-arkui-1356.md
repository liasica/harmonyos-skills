---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1356
title: 如何使用图片实现旋转加载效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用图片实现旋转加载效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4336fc6b59abb21720406423e47c29589b6be13fb80fc6a9cca82e6a27c489e0
---

## 问题现象

如何实现图片在当前位置不停地转动，做出加载中的动态效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/mOCUCMspShqERkaB7CxprA/zh-cn_image_0000002628601522.gif "点击放大")

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)：是组件挂载到组件树并显示后触发的回调函数，常用于执行初始化操作（如数据加载、动画启动）。
* [if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)：条件渲染可根据应用状态，使用if、else和else if渲染相应的UI内容。

## 解决方案

通过条件渲染机制触发animateTo动画，实现显示状态的切换。在状态切换过程中，同步执行加载层的淡出动画与内容层的淡入动画，并结合旋转动画，从而实现从加载状态到正式内容展示的平滑过渡。

```ts
@Entry
@Component
struct RotatingLoadPage {
  @State imageAngle: number = 0;
  @State flag: boolean = false;
  @State opacityValue: number = 0;
  @State opacityValueNum: number = 1;

  // 通过生命周期模拟请求数据
  aboutToAppear(): void {
    setTimeout(() => {
      this.getUIContext()?.animateTo({ duration: 1000 }, () => {
        this.flag = true;
        this.opacityValueNum = 0;
        this.opacityValue = 1;
      });
    }, 3000);
  }

  build() {
    Column({ space: 20 }) {
      if (!this.flag) {
        Stack() {
          Image($r('app.media.startIcon')) // 此处'app.media.startIcon'等资源仅作示例，请开发者自行替换。
            .width(200)
            .height(200)
            .borderRadius(1000)
            .rotate({ z: 1, angle: this.imageAngle })
          Text('图片加载中...');
        }
        .opacity(this.opacityValueNum)
        .onAppear(() => {
          this.getUIContext()?.animateTo({ duration: 5000, iterations: -1 }, () => {
            this.imageAngle = 360;
            this.opacityValueNum = 0;
          });
        })
      } else {
        Image($r('app.media.startIcon'))  // 此处'app.media.startIcon'等资源仅作示例，请开发者自行替换。
          .width(200)
          .height(200)
          .borderRadius(1000) // 绑定透明度属性
          .opacity(this.opacityValue)
          .onAppear(() => {
            // 执行透明度渐变动画
            this.getUIContext()?.animateTo({
              duration: 5000, curve: Curve.EaseOut,
              iterations: 1
            }, () => {
              // 从0到1实现淡入效果
              this.opacityValue = 1;
            });
          })
      }
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
