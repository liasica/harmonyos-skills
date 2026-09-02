---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1459
title: 使用openCustomDialog时如何关闭指定的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用openCustomDialog时如何关闭指定的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:69b46f0cbb9da22db2447efb731efc99454edd842ad59b4119ea9bf538b7b08e
---

## 问题现象

使用openCustomDialog创建自定义弹窗时，如果在页面中打开不同弹窗，如何能够正确关闭指定的弹窗？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/TVIo_YCyS8OSEs_Sj6-I2w/zh-cn_image_0000002628765240.gif "点击放大")

## 背景知识

UIContext中getPromptAction获取PromptAction实例提供了openCustomDialog和closeCustomDialog方法，分别用来实现打开和关闭自定义弹窗：

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：打开自定义弹窗，弹窗支持自定义样式，如宽度、高度、背景色、阴影。
* [closeCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closecustomdialog12)：关闭自定义弹窗。

## 解决方案

在openCustomDialog创建并打开弹窗时，在打开弹窗成功的回调中返回了dialogId表示当前打开的弹窗，通过该id可以唯一标识弹窗，因此可以结合Map等相关的数据结构，存储打开的弹窗和对应的id标识，以实现对页面中多个弹窗的区分。

promptAction.openCustomDialog返回值说明如下：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回供closeCustomDialog使用的对话框id。 |

```screen
import { BusinessError } from '@kit.BasicServicesKit';
import { HashMap } from '@kit.ArkTS';

@Entry
@Component
struct CustomDialogDemo {
  @State dialogNum: number = 0;
  ctx: UIContext = this.getUIContext();
  dialogMap: HashMap<number, number> = new HashMap();

  @Builder
  customDialogComponent(dialogNumber: number) {
    Column() {
      Text('弹窗' + dialogNumber).fontSize(30)
      Row({ space: 50 }) {
        Button('关闭弹窗').onClick(() => {
          try {
            // 关闭时找到对应的弹窗id，进而实现关闭指定的弹窗
            this.ctx.getPromptAction().closeCustomDialog(this.dialogMap.get(dialogNumber));
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        })
      }
    }.height(500).padding(5)
    .backgroundColor('#0a59f7')
    .margin({ left: dialogNumber * 20 })
  }

  build() {
    Column({ space: 20 }) {
      Text('点击打开弹窗')
        .fontSize(30)
        .onClick(() => {
          this.dialogNum += 1;
          this.ctx.getPromptAction()
            .openCustomDialog({
              builder: () => {
                this.customDialogComponent(this.dialogNum);
              },
              isModal: false
            })
            .then((dialogId: number) => {
              // 存储对应的弹框id
              try {
                this.dialogMap.set(this.dialogNum, dialogId);
              } catch (error) {
                console.error(`error: ${error}`);
              }
              ;
            })
            .catch((error: BusinessError) => {
              console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
            });
        })
    }
    .width('100%')
  }
}
```
