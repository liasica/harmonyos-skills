---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-social-share
title: 社交分享跳转
breadcrumb: 最佳实践 > 应用框架 > 程序框架 > 社交分享跳转
category: best-practices
scraped_at: 2026-04-29T14:10:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:50128a324d982540f3d88d0e6f08a962c348d1897693c5d0d31ca4f50694831d
---

## 概述

随着内容社交和移动应用的发展，用户越来越习惯于通过社交平台快捷地分享文章、商品或活动等内容，并期待受邀好友能够“一键直达”目标内容。为满足这一需求，系统提供了[App Linking](../harmonyos-guides/app-linking-startup.md)技术，实现高效、安全且用户体验极佳的社交分享跳转。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/c9/v3/2UaZPFX-SV-VP-B2uJgN4A/zh-cn_media_0000002284820638.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=64100545AD8FD53C15C6C958F046DA87C7B1C36B22C037B66F24371A19EABDC9)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 3.90%

0:00

Duration 0:16

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

应用场景举例：

* 用户在社交应用中分享文章、商品或活动页面给好友，好友点击链接后自动拉起目标应用对应详情页。
* 当好友未装目标应用时，自动跳转应用市场，一键安装后首次打开即直达目标内容页面。
* 若不希望强制用户安装，可跳转到浏览器中打开Web页面，让用户直接访问对应内容，并可引导安装应用以获取更完整体验。

## 典型场景

App Linking 支持三种典型跳转场景，根据用户设备状态智能路由。

### 场景一：目标应用已安装

用户点击分享链接后，系统直接拉起目标应用并定位到内容详情页，无需经过浏览器中转，实现一键直达，极大提高便捷度和转化率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/lWY5AkXnTlaSASxvaSernQ/zh-cn_image_0000002286508986.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=0E60E36326B0EF1E59EC7D96D201D31889946B3FDBFF6B8AA4CF9D933A36600C "点击放大")

### 场景二：目标应用未安装，已配置直达应用市场

当用户未安装目标应用且开发者配置了[直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)功能时，点击链接将直接跳转到应用市场的应用详情页。

安装完成后，首次打开应用将通过[延迟链接](../harmonyos-guides/applinking-deferredlink.md)功能自动导航至原始分享内容，无需用户重新搜索或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/F8PX5dKEQzG81CKVH7xnWA/zh-cn_image_0000002286545728.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=711553C9AD0C7C583FDD82108C3D7AC7A3EC7398154239AB34BD3440AB0890C5 "点击放大")

### 场景三：目标应用未安装，未配置直达应用市场（有Web页面）

用户点击链接后，系统通过浏览器打开Web页面，用户可直接查看内容。

在Web页面可提供“下载”按钮，引导用户安装应用获取更佳体验，安装后仍可通过[延迟链接](../harmonyos-guides/applinking-deferredlink.md)直达原内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/kkf9yxksRhW_FmYRw_hyig/zh-cn_image_0000002321144557.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=932ADD4DD09EE1DDAF8F2CE2DFB2EA85E3D7E306F38C441C73D9F5F47AE1DAE3 "点击放大")

说明

对于不提供Web页面的应用，建议开启[直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)功能，避免因无法访问内容而造成体验断裂。

## 实现原理

App Linking基于HTTPS域名校验和云端配置，自动判断目标应用是否安装、是否提供Web页面，并做出最优跳转：

* 唯一绑定与安全防护：每个分享链接与内容和目标应用强关联，有效杜绝劫持与伪造。
* 智能路由：系统根据设备状态，自动选择拉起本地应用、跳转应用市场或打开浏览器Web页面。
* [延迟链接](../harmonyos-guides/applinking-deferredlink.md)还原：即便用户经历先装应用再首次启动，也能还原到用户首次点开的具体内容页，极大提升转化率。

社交分享应用跳转的流程图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/OkAL67j5TVKkGA5FpublaA/zh-cn_image_0000002402603517.png?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=A4725B6EDF06AF19C65E7D2C722861CD2CCB721DED6F2D5C2CA7156BC2078687 "点击放大")

上图展示了从用户分享内容到好友接收并跳转的完整流程。系统根据接收方设备状态，自动选择最佳路径，确保无论哪种情况，用户都能获得连贯流畅的体验。

1. 用户A在社交应用中生成App Linking分享链接。
2. 用户B收到并点击链接，系统根据设备环境做出相应处理（跳转目标应用/应用市场/浏览器Web页面）。
3. 若中间跳转市场并安装，首次打开App可自动直达内容页，保证体验闭环。

本文将详细介绍社交分享应用使用App Linking实现跳转的开发步骤，可根据业务需求决定是否配置直达应用市场的跳转路径。社交应用主要开发步骤如下：

* [配置App Linking服务](bpta-social-share.md#section109826570198)
* [接入分享面板](bpta-social-share.md#section2364187182115)
* [应用内处理并跳转指定页面](bpta-social-share.md#section17342105516215)
* [配置直达应用市场与延迟链接（可选）](bpta-social-share.md#section11682827182215)
* [Web页面开发与部署（可选）](bpta-social-share.md#section157709544229)

## 开发步骤

### 配置App Linking服务

1. [在AGC开通App Linking服务](../harmonyos-guides/app-linking-startup.md#zh-cn_topic_0000001862787784_section189581229144811)。
2. [在开发者网站上关联应用](../harmonyos-guides/app-linking-startup.md#section6903241628)。
3. [在AGC控制台关联网址域名](../harmonyos-guides/app-linking-startup.md#section1101111611317)。
4. [在DevEco Studio中配置关联的网址域名](../harmonyos-guides/app-linking-startup.md#section13808113610362)。

   ```
   1. // entry/src/main/module.json5
   2. {
   3. "module": {
   4. // ...
   5. "abilities": [
   6. {
   7. "name": "EntryAbility",
   8. // ...
   9. "exported": true,
   10. "skills": [
   11. {
   12. "entities": [
   13. "entity.system.home",
   14. // entities must contain "entity.system.browsable"
   15. "entity.system.browsable"
   16. ],
   17. "actions": [
   18. "ohos.want.action.home",
   19. // Actions must contain "ohos.want.action.viewData"
   20. "ohos.want.action.viewData"
   21. ],
   22. "uris": [
   23. {
   24. // The scheme must be configured as https
   25. "scheme": "https",
   26. // The host must be configured as the associated domain name
   27. "host": "******",
   28. "path": ""
   29. }
   30. ],
   31. // domainVerify must be set to true
   32. "domainVerify": true
   33. }
   34. ]
   35. }
   36. ],
   37. // ...
   38. }
   39. }
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/module.json5#L2-L73)
5. 验证应用被拉起效果。
   1. 对应用进行[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)。
   2. 编译打包，并安装应用至调试设备。
   3. 可以通过如下命令查询应用域名校验结果。

      ```
      1. hdc shell hidumper -s AppDomainVerifyManager
      ```

      运行hidumper命令后，即可在控制台上看到success消息。

      ```
      1. BundleName:
      2. appIdentifier: 123456789
      3. domain verify status:
      4. https://www.example.com: success
      ```

      说明

      将生成的App Linking链接保存到备忘录应用中。通过在备忘录应用中点击该链接，可以一键拉起对应的社交应用，以此来测试该社交应用是否能够成功通过App Linking链接被启动。此方法可用于验证App Linking配置的正确性以及应用的响应情况。

### 接入分享面板

社交应用可通过集成[Share Kit（分享服务）](../harmonyos-guides/share-introduction.md)拉起分享面板，用于分享文章详情的App Linking链接。接收方点击链接后可直接跳转至目标应用。详细请参见[分享App Linking直达应用](../harmonyos-guides/share-utd-link.md#section195231314185618)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/g9CjDegVRsKBrpr7vhjUvg/zh-cn_image_0000002319316965.png?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=BCF9301C2471214356EE68F2069FE0CA224B4A7A29D69BABABDA0B2361478E8A "点击放大")

分享内容类型设为utd.UniformDataType.HYPERLINK，content字段传递生成的App Linking链接（带内容唯一标识）。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import { systemShare } from '@kit.ShareKit';
4. import { uniformTypeDescriptor } from '@kit.ArkData';
5. import { Logger } from '../common/Logger';
6. // ...
7. // entry/src/main/ets/pages/Detail.ets
8. @Entry
9. @Component
10. struct Detail {
11. // ...
12. private async share() {
13. try {
14. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. // ...
16. // To construct ShareData, you need to configure a valid data message
17. let shareData: systemShare.SharedData = new systemShare.SharedData({
18. // The type of data shared is a link
19. utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
20. // The shared App Linking link is replaced with the real address here
21. content: `https://hello.dra.agchosting.link?aid=${this.article?.aId}`,
22. // ...
23. });
24. // The sharing panel is displayed
25. let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
26. controller.show(context, {
27. previewMode: systemShare.SharePreviewMode.DEFAULT,
28. selectionMode: systemShare.SelectionMode.SINGLE
29. })
30. // ...
31. } catch (err) {
32. let error = err as BusinessError;
33. Logger.error(TAG, `share err, code: ${error.code}, mesage: ${error.message}`);
34. }
35. }

37. // ...
38. }
```

[Detail.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/pages/Detail.ets#L17-L258)

### 应用内处理并跳转指定页面

当用户点击分享链接并拉起应用时，跳转到文章详情页有以下两种情况：

1. 应用未在后台运行：如果应用从冷启动开始（即不在后台），需要在onCreate()方法中获取链接中的文章唯一标识符aid。

   ```
   1. // entry/src/main/ets/entryability/EntryAbility.ets
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { window } from '@kit.ArkUI';
   6. import { url } from '@kit.ArkTS';
   7. import { Logger } from '../common/Logger';

   9. const DOMAIN = 0x0000;
   10. const TAG = 'EntryAbilityLogTag';

   12. export default class EntryAbility extends UIAbility {
   13. private mAid: string = '';

   15. private getAid(want: Want): string {
   16. let uri = want?.uri;
   17. let aid: string = '';
   18. // Parse the parameters to obtain the app linking
   19. if (uri) {
   20. try {
   21. let urlObject = url.URL.parseURL(want?.uri);
   22. aid = urlObject.params.get('aid') as string;
   23. hilog.info(DOMAIN, 'testTag', '%{public}s', `getAid aid:${aid}`);
   24. } catch (err) {
   25. let error = err as BusinessError;
   26. Logger.error(TAG, `onAddForm err, code: ${error.code}, mesage: ${error.message}`);
   27. }
   28. }
   29. return aid;
   30. }

   32. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   33. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   34. try {
   35. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   36. } catch (err) {
   37. let error = err as BusinessError;
   38. Logger.error(TAG, `setColorMode err, code: ${error.code}, mesage: ${error.message}`);
   39. }
   40. this.mAid = this.getAid(want);
   41. }

   43. // ...
   44. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L17-L134)

   在onWindowStageCreate()回调中使用windowStage.loadContent()方法加载详情页的URL为“pages/Detail”。

   ```
   1. // entry/src/main/ets/entryability/EntryAbility.ets
   2. onWindowStageCreate(windowStage: window.WindowStage): void {

   4. let pageUrl: string = 'pages/Index';
   5. if (this.mAid && this.mAid !== '') {
   6. pageUrl = 'pages/Detail';
   7. AppStorage.setOrCreate('aid', this.mAid);
   8. }

   10. windowStage.loadContent(pageUrl, (err) => {
   11. if (err.code) {
   12. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
   13. return;
   14. }
   15. try {
   16. // ...
   17. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   18. } catch (err) {
   19. let error = err as BusinessError;
   20. Logger.error(TAG, `loadContent err, code: ${error.code}, mesage: ${error.message}`);
   21. }
   22. });
   23. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L65-L102)
2. 应用已在后台运行：如果应用已经在后台，它将从后台切换到前台。此时，需要在onNewWant()方法中获取链接中的文章唯一标识符aid，保存到AppStorage。

   ```
   1. export default class EntryAbility extends UIAbility {
   2. private mAid: string = '';

   4. private getAid(want: Want): string {
   5. // ...
   6. }

   8. // ...
   9. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   10. let aid: string = this.getAid(want);
   11. if(aid){
   12. AppStorage.setOrCreate('aid',aid);
   13. AppStorage.setOrCreate('newWantFlag',true);
   14. }
   15. }

   17. // ...
   18. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L29-L135)

   在首页通过StorageLink获取aid，并通过UIContext.getRouter().pushUrl()方法进行页面跳转。

   ```
   1. @StorageLink('newWantFlag') @Watch('newWantFlagChange') isNewWant: boolean = false;

   3. newWantFlagChange() {
   4. if (this.isNewWant && AppStorage.has('aid')) {
   5. let aid: string = AppStorage.get('aid') as string;
   6. if (aid) {
   7. this.isNewWant = false;
   8. this.getUIContext().getRouter().pushUrl({
   9. url: 'pages/Detail',
   10. params: {
   11. aid: aid
   12. }
   13. }).catch((error: BusinessError) => {
   14. Logger.error(TAG, `pushUrl err, code: ${error.code}, mesage: ${error.message}`);
   15. });
   16. }
   17. }
   18. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/pages/Index.ets#L37-L54)
3. 获取到文章唯一标识aid之后，在详情页加载文章详情数据。

   ```
   1. // entry/src/main/ets/pages/Detail.ets
   2. @Entry
   3. @Component
   4. struct Detail {
   5. // ...
   6. private article: Article | undefined;

   8. aboutToAppear(): void {
   9. if (this.aid && this.aid !== '') {
   10. this.article = getArticleById(this.aid);
   11. } else {
   12. let params = this.getUIContext().getRouter().getParams() as Record<string, string>;
   13. this.article = getArticleById(params.aid);
   14. }
   15. }

   17. // ...
   18. }
   ```

   [Detail.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/pages/Detail.ets#L29-L259)

### 配置直达应用市场与延迟链接（可选）

为提升用户未安装应用时的体验，可配置[直达应用市场](../harmonyos-guides/applinking-direct-to-ag.md)功能，引导用户下载安装应用。

在AGC控制台的App Linking服务中，开启"直达应用市场"功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/RGrwYD7eSqGqOTN3US2yNQ/zh-cn_image_0000002284717436.png?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=C757D360A7D971FC9ECAFE22EC3F9FD4217AED6DDC7C1DA3EB91117FD656B32C "点击放大")

配置完成后，当用户点击畅连中分享的App Linking链接时，若设备未安装目标应用，系统将直接跳转至应用市场的应用详情页，支持一键下载安装。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Mql6_L60SDKjeoyyw6xN1A/zh-cn_image_0000002286657862.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=531A0563AE03B33990583B8FBD818D13590D774E759BEC61E3B8CF31F23A5B18 "点击放大")

同时，需要实现[延迟链接](../harmonyos-guides/applinking-deferredlink.md)功能，确保安装后首次启动可直达内容。

安装完应用之后，开发者可以在用户首次打开应用时，使用延迟链接，可以直接跳转到文章详情，这一流程不仅优化了用户体验，还有助于提升链接的转化率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-GLwRmF7Ss6iowg3KJrkBw/zh-cn_image_0000002286660298.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=F81A2174B9EF65EF64D1FAF36DB091E919FA1B7D4DBE50138435E889204CE533 "点击放大")

通过[deferredLink.popDeferredLink()](../harmonyos-references/applinking-deferredlink-api.md#section15555111210233)接口获取原始App Linking链接，并根据解析该链接直接跳转至对应的内容详情页。

```
1. // entry/src/main/ets/pages/Index.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { deferredLink } from '@kit.AppLinkingKit';
4. import { url } from '@kit.ArkTS';
5. import { Logger } from '../common/Logger';
6. // ...
7. @Entry
8. @Component
9. struct Index {
10. // ...
11. aboutToAppear(): void {
12. // Get the deferred link parameter and go to the details page
13. deferredLink.popDeferredLink().then((link: string) => {
14. Logger.info(TAG, `Succeeded in getting deferred link, result: ${link}`);
15. if (link) {
16. // Get the link parameters
17. let urlObject = url.URL.parseURL(link);
18. let aid = urlObject.params.get('aid') as string;
19. // Go to the details component
20. this.getUIContext().getRouter().pushUrl({
21. url: 'pages/Detail',
22. params: {
23. aid: aid
24. }
25. });
26. }
27. }).catch((error: BusinessError) => {
28. Logger.error(TAG, `Failed to get deferred link. code: ${error.code}, message: ${error.message}`);
29. });
30. }
31. // ...
32. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/ets/pages/Index.ets#L17-L142)

### Web页面开发与部署（可选）

当应用未安装且未配置直达应用市场时，系统会打开浏览器Web页面。合理的Web页面开发是完善用户体验的关键环节，特别是与[延迟链接](../harmonyos-guides/applinking-deferredlink.md)结合使用。

**Web页面UA适配**

首先，需要准确识别HarmonyOS设备，以实现合适的跳转和内容适配。HarmonyOS设备的User-Agent（UA）字符串中通常包含特定的标识信息。开发者应解析UA字符串，结合系统类型（例如OS名称）和版本号进行判断。

如果未正确适配UA，可能导致以下问题：

* 页面无法正确识别设备类型，影响后续的应用跳转逻辑。
* 用户被错误跳转到不适合的下载或支持页面。
* 错误的文件提供（如直接提供APK下载而非对应平台软件）。

通过UserAgent中的{OSName}字段识别HarmonyOS系统，同时通过UserAgent中的{OSName}和{OSVersion}字段识别HarmonyOS系统及版本。

```
1. function matchHarmonyOS() {
2. // Determine whether the recognition system is HarmonyOS.
3. const isHarmonyOS = /OpenHarmony/i.test(navigator.userAgent);
4. // Get system version number
5. const matches = navigator.userAgent.match(/OpenHarmony (\d+\.?\d*)/);
6. return isHarmonyOS && matches?.length && Number(matches[1]) >= 5;
7. }

9. function openLink() {
10. if (matchHarmonyOS()) {
11. // Launch the application through app linking.
12. // ...
13. } else {
14. // Redirect logic for other platforms
15. }
16. }
```

[detail.js](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/service/detail/js/detail.js#L21-L43)

详细请参见[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。

**实现智能跳转逻辑**

Web页面需提供两个关键功能：

1. “打开”按钮 - 尝试拉起已安装的应用。
2. “下载”按钮 - 引导未安装用户前往应用市场。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/r0r5hUS4RTS8xzjfu8IIMw/zh-cn_image_0000002319316973.png?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=5FF27C030907C0E5138191206BFCA6D25432A6F3B752781FD859519C37322404 "点击放大")

当应用已安装时，点击“打开”按钮，可以直接跳转社交应用，直达文章详情页。跳转链接使用前面[配置App Linking服务](bpta-social-share.md#section109826570198)中配置的链接，例如“https://www.example.com/”，通过设置window.location.href属性进行页面跳转。

```
1. function openLink() {
2. if (matchHarmonyOS()) {
3. // Launch the application through app linking.
4. // Replace with a real usable app linking link.
5. window.location.href = 'https://www.example.com?aid=' + aid;
6. } else {
7. // Redirect logic for other platforms
8. }
9. }
```

[detail.js](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/service/detail/js/detail.js#L30-L42)

当用户未安装社交应用时，点击“下载”按钮，可以直接跳转到应用市场详情页，方便用户下载安装应用，开发者可以使用应用市场的App Linking链接，通过设置window.location.href属性进行页面跳转。

```
1. function toAppgallery() {
2. // Replace with a real usable application market app linking link.
3. window.location.href = 'https://appgallery.huawei.com/app/detail?id=com.huawei.hmsapp.books';
4. }
```

[detail.js](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/service/detail/js/detail.js#L46-L49)

**延迟链接与Web页面结合**

Web页面与延迟链接的结合是创建完整用户体验的关键。当用户通过Web页面安装应用后，可通过[延迟链接](../harmonyos-guides/applinking-deferredlink.md)实现首次打开应用时自动跳转到原始内容。

说明

为确保App Linking正常工作，需要注意：

* Web页面域名应与App Linking配置的域名不同，否则系统将优先使用浏览器打开链接。
* 建议部署架构：
  + 主域名（https://www.example.com）配置为App Linking域名，部署引导页。
  + 子域名（https://m.example.com/detail）：部署实际内容页面。
  + 引导页通过重定向将用户引导至内容页。

## 常见问题

### 如何查看App Linking是否在AGC上配置成功

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击HarmonyOS应用所在的项目。
3. 在左侧导航栏中选择“增长 > App Linking”菜单栏查看App Linking链接地址的配置状态，若为成功则表明AGC上App Linking配置成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/2OkidG9MQJGakc0XZod7vA/zh-cn_image_0000002425293594.png?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=7663D26E678B664521C931EB5357DA6E9C21D7A96FFE4D0F5E9FF4B8674BD606 "点击放大")

### AGC中App Linking显示配置失败如何解决

**问题现象**

App Linking菜单栏查看App Linking链接地址的配置状态如下图，显示红色圆点并文本提示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/5siyPqKjQOWYTJZXsCQpNw/zh-cn_image_0000002458692429.png?HW-CC-KV=V1&HW-CC-Date=20260429T061048Z&HW-CC-Expire=86400&HW-CC-Sign=7A1735746CF0DC3FCE9F51C28F3F68793C1B65C6E720AB99C4686FE9F6BB3225 "点击放大")

**解决措施**

* 首先，显示 App Linking 状态失败并不一定意味着配置错误。也有可能是配置正确，但 AppGallery Connect（AGC）未及时更新。若不确定是否为此问题，可以采取删除链接后重新添加的方式。如果问题依旧存在，那么大概率是服务器配置问题。
* applinking.json配置文件配置错误，请参考[在开发者网站上关联应用](../harmonyos-guides/app-linking-startup.md#section6903241628)进行配置。
* App Linking地址仅支持https链接、若为http链接，请自行申请SSL证书。
* 检查配置文件所处的文件目录与文件权限确保外部可以访问。

若上述检查无误，建议求助网站运维侧人员，共同解决。

### AGC上显示了配置成功，但是配置到目标方后无法拉起如何解决

**问题现象**

AGC上显示链接地址配置成功，但是配置到目标方后，尝试使用openLink()或其他拉起方式，应用并未成功拉起。

**可能原因**

1. AGC配置App Linking链接时以“/”结尾。
2. 目标方中module.json5配置的链接与AGC配置链接不一致导致无法拉起。
3. 应用未手动从AGC上申请证书签名进行应用签名。
4. 开发者所处的网络有访问限制。
5. module.json5配置文件配置错误。

**解决措施**

1. 检查AGC上配置AppLinking链接地址，当前该链接不支持末尾以“/”结尾，检查AGC配置的链接地址末尾是否多了“/”。
2. 检查module.json5中配置的链接地址与AGC中配置的链接地址是否一致，如AGC中配置了“https://www.huawei.com”而在代码中使用了“https://developer.huawei.com”。
3. 开发者请参考[验证应用被拉起效果](../harmonyos-guides/app-linking-startup.md#section1862871612126)在AGC上手动申请证书与Profile进行手动签名。
4. 重新更换其他网络。
5. 请对照以下代码检查module.json5配置是否满足要求。

   ```
   1. // entry/src/main/module.json5
   2. {
   3. "module": {
   4. // ...
   5. "abilities": [
   6. {
   7. "name": "EntryAbility",
   8. // ...
   9. "exported": true,
   10. "skills": [
   11. {
   12. "entities": [
   13. "entity.system.home",
   14. // entities must contain "entity.system.browsable"
   15. "entity.system.browsable"
   16. ],
   17. "actions": [
   18. "ohos.want.action.home",
   19. // Actions must contain "ohos.want.action.viewData"
   20. "ohos.want.action.viewData"
   21. ],
   22. "uris": [
   23. {
   24. // The scheme must be configured as https
   25. "scheme": "https",
   26. // The host must be configured as the associated domain name
   27. "host": "******",
   28. "path": ""
   29. }
   30. ],
   31. // domainVerify must be set to true
   32. "domainVerify": true
   33. }
   34. ]
   35. }
   36. ],
   37. // ...
   38. }
   39. }
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/SocialShareJump/blob/master/entry/src/main/module.json5#L2-L73)

### 社交应用的链接点击后，打开的浏览器Web页面显示异常

**问题现象**

社交应用的链接点击后，打开的浏览器Web页面显示空白、无法正常交互，或页面加载异常。

**可能原因**

1. Web页面的User-Agent（后续简称为UA）标识未适配HarmonyOS设备或浏览器环境，导致兼容性问题。
2. 对应的Web页面可能未完全开发或存在错误（如资源加载失败、后端服务异常等）。
3. 链接地址错误，导致无法正确加载目标页面。

**解决措施**

1. 适配UA标识。确保Web页面适配了HarmonyOS设备和配套浏览器的UA标识，以正确识别设备并跳转到对应页面或平台。详细请参见[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。
2. 检查页面开发完整性。确认页面资源是否正常加载，后端接口是否返回正确数据。
3. 验证链接地址。确保社交应用的聊天界面中发送的链接地址正确无误。

### Web页面跳转跨应用页面异常

**问题现象**

用户点击社交应用的聊天界面中的链接进入Web页面后，尝试从该应用的Web A页面跳转到跨应用的Web B页面时发生异常（例如A应用的宽带充值页面跳转B应用的支付页面，在B应用的支付页面使用时发生异常）。

* 页面跳转失败，停留在当前页面。
* 跳转后页面加载错误或显示空白。

**可能原因**

1. 目标Web B页面的UA标识未适配HarmonyOS设备或浏览器环境，导致兼容性问题。
2. 目标Web B页面资源加载失败。

**解决措施**

1. 适配UA标识。确保Web B页面适配了HarmonyOS设备和配套浏览器的UA标识，以正确识别设备并跳转到对应页面或平台。详细请参见[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。
2. 检查Web B页面的资源加载情况。

### Web页面跳转应用异常

**问题现象**

用户从社交应用的聊天界面中的链接跳转到Web页面后，尝试通过页面操作跳转应用时发生异常，例如：

1. 点击“打开”按钮后无反应。
2. 点击“下载”按钮后跳转到错误平台，或提示直接下载APK包。

**可能原因**

1. 点击“打开”按钮无反应，可能是因为目标应用未正确配置跳转逻辑（例如App Linking），或者配置过程中存在错误。
2. 点击“打开”按钮无反应，Web页面使用链接不正确。
3. 目标应用未安装，点击“下载”按钮，触发应用下载逻辑跳转到应用下载的Web页面，但如果Web页面未正确适配HarmonyOS设备的UA标识，导致跳转到错误平台，或提示直接下载APK包。

**解决措施**

* 检查跳转逻辑。确保Web页面跳转的目标应用正确配置了App Linking。详细请参见[配置App Linking服务](bpta-social-share.md#section109826570198)。
* 检查Web页面“打开”跳转地址的正确性。使用正确的App Linking跳转地址。
* 适配UA标识。确保Web页面适配了HarmonyOS设备和配套浏览器的UA标识，以正确识别设备并跳转到对应页面或平台。详细请参见[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。

## 示例代码

* [基于App Linking实现社交分享跳转](https://gitcode.com/harmonyos_samples/SocialShareJump)
