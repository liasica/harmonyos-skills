---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-levelorder
title: 弹出框层级管理
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框层级管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1a70838c152613830568825e7ec1923ad1939658b5e37c22fe6898ae2eea00ef
---

ArkUI的弹出框节点默认直接挂载在根节点上，会根据层级从小到大依次挂载。根节点下，高层级的弹出框节点会显示在低层级的弹出框节点之上，新创建的弹出框节点会根据层级大小插入到对应的位置，同一层级大小的弹出框节点按照创建的先后顺序进行挂载。

从API version 18开始，可以通过设置[levelOrder](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来管理弹出框的显示顺序，确保层级较高的弹出框覆盖在层级较低的弹出框之上，从而根据需要灵活控制各层弹出框的显示效果。

## 使用约束

目前[openCustomDialog](arkts-uicontext-custom-dialog.md)、[CustomDialog](arkts-common-components-custom-dialog.md)、[AlertDialog](arkts-fixes-style-dialog.md#警告弹窗-alertdialog)、[ActionSheet](arkts-fixes-style-dialog.md#列表选择弹出框-actionsheet)、[showDialog](arkts-fixes-style-dialog.md#对话框-showdialog)支持通过levelOrder参数来管理弹出框的层级。

**说明** 

弹出框层级管理不支持子窗场景，即当showInSubWindow设置为true时，levelOrder参数设置无效。不支持动态刷新弹出框的显示顺序。

## 创建不同层级的弹出框

**说明** 

详细变量定义请参考[完整示例](arkts-dialog-levelorder.md#完整示例)。

1. 初始化一个弹出框内容区，内部包含一个Text组件。

   ```typescript
   @Builder
   normalCustomDialog(index: number) {
     Column() {
       // 请在resources\base\element\string.json文件中配置name为'open_normal_dialog'，value为非空字符串的资源
       Text(this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('open_normal_dialog') as string +
         index).fontSize(30)
     }.height(400).padding(5).justifyContent(FlexAlign.SpaceBetween)
   }
   ```
2. 初始化另一个弹出框内容区，内部包含一个点击打开普通弹出框的按钮，点击事件中通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)接口，并且设置层级为0的[levelOrder](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来创建普通层级弹出框。

   ```typescript
   @Builder
   topCustomDialog() {
     Column() {
       // 请将$r('app.string.top_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"我是置顶弹窗"
       Text($r('app.string.top_dialog')).fontSize(30)
       Row({ space: 50 }) {
         // 请将$r('app.string.open_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我打开普通弹窗"
         Button($r('app.string.open_dialog'))
           .onClick(() => {
             this.getUIContext().getPromptAction().openCustomDialog({
               builder: () => {
                 this.normalCustomDialog(this.dialogIndex);
               },
               levelOrder: LevelOrder.clamp(0),
             })
               .catch((err: BusinessError) => {
                 hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
               });
             this.dialogIndex++;
           })
       }
     }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
   }
   ```
3. 通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)接口，并且设置层级为100000的[levelOrder](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来创建最高层级弹出框。

   ```typescript
   this.getUIContext().getPromptAction().openCustomDialog({
     builder: () => {
       this.topCustomDialog();
     },
     levelOrder: LevelOrder.clamp(100000)
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
   });
   ```

## 完整示例

```typescript
import { LevelOrder } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const INDEX: number = 0;
const DOMAIN = 0x0000;

@Entry
@Component
export struct DialogBoxLayer {
  @StorageLink('dialogIndex') dialogIndex: number = INDEX;

  @Builder
  normalCustomDialog(index: number) {
    Column() {
      // 请在resources\base\element\string.json文件中配置name为'open_normal_dialog'，value为非空字符串的资源
      Text(this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('open_normal_dialog') as string +
        index).fontSize(30)
    }.height(400).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }

  @Builder
  topCustomDialog() {
    Column() {
      // 请将$r('app.string.top_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"我是置顶弹窗"
      Text($r('app.string.top_dialog')).fontSize(30)
      Row({ space: 50 }) {
        // 请将$r('app.string.open_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我打开普通弹窗"
        Button($r('app.string.open_dialog'))
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.normalCustomDialog(this.dialogIndex);
              },
              levelOrder: LevelOrder.clamp(0),
            })
              .catch((err: BusinessError) => {
                hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
              });
            this.dialogIndex++;
          })
      }
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }

  build() {
    NavDestination() {
      Row() {
        Column({ space: 5 }) {
          // 请将$r('app.string.click_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点击弹窗"
          Button($r('app.string.click_dialog'))
            .fontSize(20)
            .onClick(() => {
              this.getUIContext().getPromptAction().openCustomDialog({
                builder: () => {
                  this.topCustomDialog();
                },
                levelOrder: LevelOrder.clamp(100000)
              }).catch((err: BusinessError) => {
                hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
              });
            })
        }.width('100%')
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/UDEcbkZfTJ6oXb5-CtI5Ew/zh-cn_image_0000002706673748.gif)
