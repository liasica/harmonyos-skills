---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1600
title: 如何实现倒计时结束前禁用弹窗按钮
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现倒计时结束前禁用弹窗按钮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6121a3ed6fd419cb8fc064219b8686e22c554561ce7129f8089a36a4a987f1b2
---

## 问题现象

如何给自定义弹窗使用CustomBuilder，实现下图的功能，且确认取消按钮需要一个带有倒计时的功能，倒计时结束后才能点击。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/yeUjE5AzSv2aPNTj9wX9Pw/zh-cn_image_0000002658972545.gif "点击放大")

## 背景知识

* [promptAction.openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：创建并弹出dialogContent对应的自定义弹窗，使用Promise异步回调。
* [@Builder](../harmonyos-guides/arkts-builder.md)：ArkUI提供轻量的UI元素复用机制@Builder，其内部UI结构固定，仅与使用方进行数据传递。开发者可将重复使用的UI元素抽象成方法，在build方法中调用。
* onWillDismiss：openCustomDialog方法的[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数中的交互式关闭回调函数。

## 解决方案

实现弹窗按钮计时禁用效果步骤如下：

1. 使用@Builder创建自定义的组件，传入自定义的弹窗组件。
2. 使用状态变量isEnabled，初始为false，设置按钮是否禁用。
3. 设置定时器，实现倒计时功能。当计时结束时，isEnabled为true，并清除计时器。
4. 当弹窗关闭时，触发onWillDismiss回调，isEnabled为false，并重置定时功能。

代码如下：

```ts
@Entry
@Component
struct BuildPage {
  @State time: number = 3;
  @State isEnabled: boolean = false;
  private customDialogComponentId: number = 0;

  timeout() {
    let intervalID = setInterval(() => {
      this.time--;
      if (this.time === 0 || this.time < 0) {
        this.isEnabled = true;
        clearInterval(intervalID);
      }
    }, 1000);
  }

  @Builder
  customDialogComponent() {
    Column({ space: 10 }) {
      Row() {
        Text('标题')
      }
      .width('100%')
      .margin({ top: 10 })
      .justifyContent(FlexAlign.Center)

      Text('我们会不时修订本隐私权政策。未经您明确同意，我们不会减降您按照本隐私权政策的规定所享有的权利')
        .width('80%')
      Row() {
        Button(this.time === 0 || this.time < 0 ? '我已知悉' : `(${this.time})`)
          .enabled(this.isEnabled)
          .width(80)
          .onClick(() => {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          })
      }.width('100%')
      .height(100)
      .justifyContent(FlexAlign.SpaceAround)
      .alignItems(VerticalAlign.Center)
    }.width('100%')
  }

  @Builder
  buildAlertDialog() {
    Column() {
      Row() {
        Text('组件内弹窗')
          .fontSize(30)
          .onClick(() => {
            this.timeout();
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              onWillAppear: () => {
                this.time = 3;
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                // 时间归零前，禁止关闭弹窗
                if (this.time <= 0) {
                  dismissDialogAction.dismiss();
                }
              },
              onWillDisappear: () => {
                this.isEnabled = false;
              }
            })
              .then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              });
          })
      }.width('100%')
      .justifyContent(FlexAlign.SpaceAround)
    }
  }

  build() {
    Row() {
      this.buildAlertDialog();
    }
    .height('100%')
  }
}
```
