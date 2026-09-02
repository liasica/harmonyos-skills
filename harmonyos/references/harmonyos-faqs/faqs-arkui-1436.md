---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1436
title: Toast是否支持设置字体大小和弹窗宽高等属性
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Toast是否支持设置字体大小和弹窗宽高等属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:28c417ecb8dab34f4bcc96828dbf07b2544aa0d2fa3453d44f93e581318c5874
---

## 问题现象

Toast是否支持自定义设置字体大小和弹窗背板的宽高等属性？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/_vhMeuFsRzaetoR_unRN4g/zh-cn_image_0000002628763654.gif "点击放大")

## 背景知识

* [即时反馈（Toast）](../harmonyos-guides/arkts-create-toast.md)是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。
* [不依赖UI组件的全局自定义弹出框](../harmonyos-guides/arkts-uicontext-custom-dialog.md)：在相对较复杂的应用场景中推荐使用UIContext中获取到的PromptAction对象提供的openCustomDialog接口来实现自定义弹出框。

## 解决方案

[this.getUIContext().getPromptAction().openToast](../harmonyos-references/js-apis-promptaction.md#promptactionopentoast18)接口未提供设置字体大小和弹窗宽高等方法，可以使用this.getUIContext().getPromptAction().openCustomDialog打开自定义弹窗来实现定制化样式。方案如下：

* 使用[this.getUIContext().getPromptAction().openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)自定义弹窗，在相对较复杂的应用场景中推荐使用[全局自定义弹出框](../harmonyos-guides/arkts-uicontext-custom-dialog.md)的方式。

  ```ts
  let customDialogId: number = 0;

  @Builder
  function customDialogBuilder() {
    Column() {
      // 可自定义文字大小及颜色
      Text('自定义Toast').fontSize(20).fontColor('#fff');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }

  @Entry
  @Component
  struct Index99 {
    @Builder
    customDialogComponent() {
      customDialogBuilder();
    }

    build() {
      Row() {
        Column() {
          Text('点击弹出Toast')
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              this.getUIContext().getPromptAction().openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                },
                // 弹窗背景色
                backgroundColor: 'rgba(0,0,0,0.8)',
                backgroundBlurStyle: BlurStyle.NONE,
                cornerRadius: 5,
                width: '50%', // 弹窗宽度
                height: 50, // 弹窗高度
                isModal: false,
                alignment: DialogAlignment.Center,
                offset: { dx: 0, dy: 100 }
              }).then((dialogId: number) => {
                customDialogId = dialogId;
                setTimeout(() => {
                  this.getUIContext().getPromptAction().closeCustomDialog(customDialogId);
                }, 1500);
              });
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
