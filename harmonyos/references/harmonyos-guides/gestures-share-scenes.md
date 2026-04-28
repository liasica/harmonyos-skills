---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gestures-share-scenes
title: 分享App Linking直达应用
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 隔空传送 > 分享App Linking直达应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:500963e46dcfd64bf58d23dfc61509c853f9598115bd18d03c34417476648450
---

提供如何通过隔空传送分享实现直达应用，应用需接入App Linking以确保端到端完整的体验。参考：[使用App Linking实现应用间跳转](app-linking-startup.md)。

## 注意事项

1. 当进入可分享页面时，使用[harmonyShare.on('gesturesShare')](../harmonyos-references/share-harmony-share.md#ongesturesshare)方法注册隔空传送监听事件。
2. 当离开可分享页面（包括**应用退至后台**等场景）时，使用[harmonyShare.off('gesturesShare')](../harmonyos-references/share-harmony-share.md#offgesturesshare)方法取消隔空传送监听事件。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   2. import { systemShare, harmonyShare } from '@kit.ShareKit';
   3. import { fileUri } from '@kit.CoreFileKit';
   ```
2. 定义隔空传送分享事件监听/取消监听方法（收到隔空传送分享事件回调后，建议3秒内调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#share)方法发起分享，否则可能导致超时失败）。

   ```
   1. private immersiveCallback = (sharableTarget: harmonyShare.SharableTarget) => {
   2. let uiContext: UIContext = this.getUIContext();
   3. let contextFaker: Context = uiContext.getHostContext() as Context;
   4. let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
   5. let shareData: systemShare.SharedData = new systemShare.SharedData({
   6. utd: utd.UniformDataType.HYPERLINK,
   7. content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
   8. thumbnailUri: fileUri.getUriFromPath(filePath),
   9. title: '隔空传送分享卡片标题',
   10. description: '隔空传送分享卡片描述'
   11. });
   12. sharableTarget.share(shareData);
   13. }

   15. private immersiveListening() {
   16. harmonyShare.on('gesturesShare', this.immersiveCallback);
   17. }

   19. private immersiveDisablingListening() {
   20. harmonyShare.off('gesturesShare', this.immersiveCallback);
   21. }
   ```
3. 进入可分享页面时，注册隔空传送分享监听事件；离开可分享页面（包括**应用退至后台**等场景）时，取消隔空传送分享监听事件。

   ```
   1. // Entry Component 代码片段
   2. onPageHide(): void {
   3. let uiContext: UIContext = this.getUIContext();
   4. let context: Context = uiContext.getHostContext() as Context;
   5. context.eventHub.emit('onBackGround');
   6. }
   ```

   ```
   1. aboutToAppear(): void {
   2. this.immersiveListening();
   3. let uiContext: UIContext = this.getUIContext();
   4. let context: Context = uiContext.getHostContext() as Context;
   5. context.eventHub.on('onBackGround', this.onBackGround);
   6. }

   8. aboutToDisappear(): void {
   9. this.immersiveDisablingListening();
   10. let uiContext: UIContext = this.getUIContext();
   11. let context: Context = uiContext.getHostContext() as Context;
   12. context.eventHub.off('onBackGround', this.onBackGround);
   13. }

   15. private onBackGround = () => {
   16. this.immersiveDisablingListening();
   17. }
   ```
