---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gestures-share-scenes
title: 分享App Linking直达应用
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 隔空传送 > 分享App Linking直达应用
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4ad49c2763206cb182155078a880605d6a99c74bb01350d76088d50b4ce6b51c
---

提供如何通过隔空传送分享实现直达应用，应用需接入App Linking以确保端到端完整的体验。参考：[使用App Linking实现应用间跳转](app-linking-startup.md)。

## 注意事项

1. 当进入可分享页面时，使用[harmonyShare.on('gesturesShare')](../harmonyos-references/share-harmony-share.md#ongesturesshare)方法注册隔空传送监听事件。
2. 当离开可分享页面（包括**应用退至后台**等场景）时，使用[harmonyShare.off('gesturesShare')](../harmonyos-references/share-harmony-share.md#offgesturesshare)方法取消隔空传送监听事件。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   import { systemShare, harmonyShare } from '@kit.ShareKit';
   import { fileUri } from '@kit.CoreFileKit';
   ```
2. 定义隔空传送分享事件监听/取消监听方法（收到隔空传送分享事件回调后，建议3秒内调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#share)方法发起分享，否则可能导致超时失败）。

   ```typescript
   private immersiveCallback = (sharableTarget: harmonyShare.SharableTarget) => {
     let uiContext: UIContext = this.getUIContext();
     let contextFaker: Context = uiContext.getHostContext() as Context;
     let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
     let shareData: systemShare.SharedData = new systemShare.SharedData({
       utd: utd.UniformDataType.HYPERLINK,
       content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
       thumbnailUri: fileUri.getUriFromPath(filePath),
       title: '隔空传送分享卡片标题',
       description: '隔空传送分享卡片描述'
     });
     sharableTarget.share(shareData);
   }

   private immersiveListening() {
     harmonyShare.on('gesturesShare', this.immersiveCallback);
   }

   private immersiveDisablingListening() {
     harmonyShare.off('gesturesShare', this.immersiveCallback);
   }
   ```
3. 进入可分享页面时，注册隔空传送分享监听事件；离开可分享页面（包括**应用退至后台**等场景）时，取消隔空传送分享监听事件。

   ```typescript
   // Entry Component 代码片段
   onPageHide(): void {
     let uiContext: UIContext = this.getUIContext();
     let context: Context = uiContext.getHostContext() as Context;
     context.eventHub.emit('onBackGround');
   }
   ```

   ```typescript
   aboutToAppear(): void {
     this.immersiveListening();
     let uiContext: UIContext = this.getUIContext();
     let context: Context = uiContext.getHostContext() as Context;
     context.eventHub.on('onBackGround', this.onBackGround);
   }

   aboutToDisappear(): void {
     this.immersiveDisablingListening();
     let uiContext: UIContext = this.getUIContext();
     let context: Context = uiContext.getHostContext() as Context;
     context.eventHub.off('onBackGround', this.onBackGround);
   }

   private onBackGround = () => {
     this.immersiveDisablingListening();
   }
   ```
