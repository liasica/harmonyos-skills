---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-718
title: PromptAction弹窗禁用点击蒙层隐藏弹窗功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > PromptAction弹窗禁用点击蒙层隐藏弹窗功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2e0ba7689c6bf15700db4489e9b422e913be02da211480599cbfc6893a7355e
---

## 问题现象

PromptAction自定义弹窗如何实现在点击弹窗外围的蒙层时，弹窗不关闭？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/WY2et_8HSXCqJuwLTarrkA/zh-cn_image_0000002628395300.png "点击放大")

## 背景知识

* [PromptAction弹窗](../harmonyos-references/js-apis-promptaction.md)：为官网提供的一种弹窗方式，由于上下文不明确，在API18以后部分接口废弃。废弃的接口建议通过[this.getUIContext().getPromptAction()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)获取弹窗实例后调用。
* [onWillDismiss](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)：PromptAction弹窗的关闭事件可以在通过onWillDismiss方法指定是否关闭弹窗。方法内指定对应的[DismissDialogAction](../harmonyos-references/js-apis-promptaction.md#dismissdialogaction12)信息控制是否关闭弹窗，关闭调用dismiss()函数，不关闭则不调用即可。控制关闭事件参考[DismissReason](../harmonyos-references/ts-universal-attributes-popup.md#dismissreason12枚举说明)。

## 解决方案

实现PromptAction弹窗禁用点击蒙层隐藏弹窗功能时，只需要在onWillDismiss内控制关闭信息：在dismissDialogAction.reason !== DismissReason.TOUCH\_OUTSIDE条件下调用dismiss()关闭函数即可，在该条件下除了点击蒙层不关闭弹窗外，其他关闭条件都不影响。

```ts
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  private customDialogComponentId: number = 0;

  @Builder
  customDialogComponent() {
    Column() {
      Text('弹窗').fontSize(30)
      Row({ space: 50 }) {
        Button('确认').onClick(() => {
          this.promptAction.closeCustomDialog(this.customDialogComponentId);
        })
        Button('取消').onClick(() => {
          this.promptAction.closeCustomDialog(this.customDialogComponentId);
        })
      }
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }

  build() {
    Row() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.promptAction.openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                if (dismissDialogAction.reason !== DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId;
            });
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

## 总结

本方案通过onWillDismiss内回调实现点击蒙层不关闭弹窗的功能。同时也可以采用isModal设置为false，取消弹窗蒙层，实现类似点击弹窗外不关闭的功能，但是该功能还会导致点击穿透。
