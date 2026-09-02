---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-chooseavatar
title: 选择头像Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 选择头像Button
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e29fad7f6be04eef9fd7b29a9b72b2bb3972b442a5b2d4d17ae33e792e437670
---

## 场景介绍

选择头像Button功能可以帮助开发者调用对应Button组件快速拉起头像选择页面，供用户完成华为账号头像或其他头像的选择与展示。

运行示例代码单击头像按钮，拉起选择头像页面来设置头像（完整场景可参考[获取头像昵称](account-get-avatar-nickname.md)）。

## 前提条件

应用开发前提条件，参见[开发前提](account-get-avatar-nickname.md#开发前提)。

元服务应用开发前提条件，参见[开发前提](../atomic-guides/account-guide-atomic-get-avatar-nickname-button.md#开发前提)。

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```typescript
   import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在容器中声明FunctionalButton，指定Button的openType，并设置对应的回调函数，代码如下：

   ```typescript
   @Entry
   @Component
   struct Index {
     // 将account.png文件添加到/resources/base/media/目录中。否则，将显示错误信息，提示找不到该文件。
     @State url: ResourceStr = $r('app.media.account');

     build() {
       Column() {
         // 构建FunctionalButton组件实例。
         FunctionalButton({
           params: {
             // OpenType.CHOOSE_AVATAR表示该按钮用于选择头像。
             openType: functionalButtonComponentManager.OpenType.CHOOSE_AVATAR,
             label: '',
             // 调整按钮样式。
             styleOption: {
               styleConfig: new functionalButtonComponentManager.ButtonConfig()
                 .type(ButtonType.Normal)
                 .backgroundImage(this.url)
                 .backgroundImageSize(ImageSize.Cover)
                 .width(80)
                 .height(80)
                 .backgroundColor('#E5E5E5')
             }
           },
           // 当OpenType设置为CHOOSE_AVATAR时，回调函数必须是onChooseAvatar。
           controller: new functionalButtonComponentManager.FunctionalButtonController().onChooseAvatar((err, data) => {
             if (err) {
               // 错误日志处理。
               hilog.error(0x0000, 'testTag', 'Failed to choose avatar, error: %{public}d %{public}s', err.code, err.message);
               return;
             }
             // 成功日志处理。
             hilog.info(0x0000, 'testTag', 'succeeded in choosing avatar');
             this.url = data.avatarUri!;
           })
         })
       }
       .padding({ top: 200 })
       .height('100%')
       .width('100%')
     }
   }
   ```

   **说明** 

   * openType参数填写"functionalButtonComponentManager.OpenType.CHOOSE\_AVATAR"指定Button为选择头像类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onChooseAvatar"。
   * 若成功调用，可通过回调函数中的"avatarUri"获取头像图片的地址。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
