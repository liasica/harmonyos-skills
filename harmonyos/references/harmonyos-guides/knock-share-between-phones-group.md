---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-group
title: 邀请组队
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与手机碰一碰分享 > 邀请组队
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:99341f34901203f8e68f78214b96ef05fae7f2475180c392468090242e360b97
---

## 注册碰一碰事件

在组队房间邀请界面注册碰一碰事件。

**图1** 横屏应用示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/oERGofuCQWanFZRTL6o-aA/zh-cn_image_0000002552959188.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=DF2C078909ABD8A1DFF1BDFAC2A2976368C1E66391FF0368766BD0D531F38104)

**图2** 竖屏应用示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/dyYfajFBSl6uyUNKkq7z2w/zh-cn_image_0000002583479189.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=16EC9E99767365A4AD55A68569390A97ABC27D1DAB779A1CB249E52D7CC7ADF3)

## 注册单向分享能力

通过碰一碰分享邀请好友加入组队房间，若双方都同时在组队房间内互相邀请，无法相互加入对方的组队房间。

针对以上场景，Share Kit提供单向仅发送能力。参考：[SendCapabilityRegistry](../harmonyos-references/share-harmony-share.md#sendcapabilityregistry)的sendOnly属性。

若碰一碰的双方都设置单向仅发送，则终止本次分享并提示用户"请任意一方退出当前应用后再试"；反之，均可分享成功。

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';
3. import { fileUri } from '@kit.CoreFileKit';

5. @Component
6. export default struct Index {
7. aboutToAppear(): void {
8. let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
9. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
10. sendOnly: true, // 声明仅支持单向发送 若对端也同样声明仅支持单向发送 则双向分享时会失败
11. }
12. harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
13. let uiContext: UIContext = this.getUIContext();
14. let contextFaker: Context = uiContext.getHostContext() as Context;
15. let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
16. let shareData: systemShare.SharedData = new systemShare.SharedData({
17. utd: utd.UniformDataType.HYPERLINK,
18. content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
19. // 根据title,description,thumbnailUri会生成不同的卡片模板。
20. thumbnailUri: fileUri.getUriFromPath(filePath),
21. title: '碰一碰分享卡片标题',
22. description: '碰一碰分享卡片描述'
23. });
24. sharableTarget.share(shareData);
25. });
26. }

28. aboutToDisappear(): void {
29. let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
30. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
31. }
32. // 解除碰一碰分享'knockShare'监听事件
33. harmonyShare.off('knockShare', capabilityRegistry);
34. }

36. build() {
37. }
38. }
```

## 设置组队邀请预览

预览图设置参考：[设置分享预览](knock-share-between-phones-content.md#设置分享预览)。

## 处理组队链接

当目标应用被分享拉起时，可以通过[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中获取传入的want参数。其中want.uri字段为邀请组队的链接，通过链接上携带的参数信息，处理组队邀请的业务逻辑。

示例代码：

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
6. try {
7. windowStage.loadContent('pages/Index');
8. } catch (error) {
9. console.error(`onWindowStageCreate error. Code: ${error?.code}, message: ${error?.message}`);
10. }
11. }

13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. console.info('EntryAbility onCreate invoked. uri: ', want.uri);
15. // to do things.
16. }

18. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
19. console.info('EntryAbility onNewWant invoked. uri: ', want.uri);
20. // to do things.
21. }
22. }
```

## 异常场景终止分享

当碰一碰分享回调触发时，发生异常场景导致无法继续分享，可终止本次分享。

参考：[异常场景终止分享](knock-share-between-phones-content.md#异常场景需终止分享)。
