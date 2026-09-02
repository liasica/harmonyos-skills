---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-actions
title: 自定义配置操作区
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 宿主应用发起分享 > 自定义配置操作区
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:921a4cdecb57047920420ef3114eebb2a87dfb40e8550ab36d7574885d2137b6
---

## 场景介绍

系统操作区提供了复制、保存、另存为、打印、复制到中转站等系统级快捷操作。宿主应用可以根据自己的业务体验需要判断是否给用户提供相关操作。

比如，分享的图片不需要被打印出来，本次分享将打印按钮从操作区移除。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { fileUri } from '@kit.CoreFileKit';
   import { systemShare } from '@kit.ShareKit';
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   ```
2. 构造分享数据，可添加多条分享记录。

   ```typescript
   // 构造ShareData，需配置一条有效数据信息
   let data: systemShare.SharedData = new systemShare.SharedData({
     utd: utd.UniformDataType.PLAIN_TEXT,
     content: 'Hello HarmonyOS'
   });
   // 通过addRecord方法可添加多条记录 通过设置selectionMode实现一条或批量分享
   let uiContext: UIContext = this.getUIContext();
   let contextFaker: Context = uiContext.getHostContext() as Context;
   let filePath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
   data.addRecord({
     utd: utd.UniformDataType.PNG,
     uri: fileUri.getUriFromPath(filePath)
   });
   ```
3. 启动分享面板，并配置不显示打印快捷操作。如需屏蔽其他系统级快捷操作，请参考[ShareAbilityType](../harmonyos-references/share-system-share.md#shareabilitytype)介绍。

   ```typescript
   // 构建ShareController
   let controller: systemShare.ShareController = new systemShare.ShareController(data);
   let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
   // 注册分享面板关闭监听
   controller.on('dismiss', () => {
     console.info('Share panel closed');
     // 分享结束，可处理其他业务。
   });
   // 进行分享面板显示
   controller.show(context, {
     previewMode: systemShare.SharePreviewMode.DETAIL,
     selectionMode: systemShare.SelectionMode.SINGLE,
     excludedAbilities: [systemShare.ShareAbilityType.PRINT]
   })
   ```
