---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-installation-package
title: 传输安装包
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发指导 > 传输安装包
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fab2cb2114ae90d1208717d01fc675341d078c36c9840f5dc962d6490739c813
---

游戏近场快传支持已安装游戏的玩家通过碰一碰或隔空传送将游戏安装包传输给未安装游戏的玩家，实现游戏传播效率的提升。

说明

付费游戏不支持使用近场快传传输安装包。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/vVT3-NjAQvGqTZ8HWGTs9A/zh-cn_image_0000002583478905.png?HW-CC-KV=V1&HW-CC-Date=20260427T234905Z&HW-CC-Expire=86400&HW-CC-Sign=EADFB3B5D847A2383D3B6613334510E18983386454ED41C5778D24E4C6AF6F8B)

1. 发送端设备打开游戏后与接收端设备通过[碰一碰](knock-share-between-phones-overview.md)或[隔空传送](gestures-share-overview.md)触发安装包传输。
2. 发送端调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)创建安装包传输任务。
3. 创建成功后，游戏客户端调[onRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)注册远程安装信息事件监听。
4. 游戏应用获取到安装游戏所需要的linkingForInstallation地址。
5. 通过linkingForInstallation地址拉起接收端游戏服务。
6. 接收端发送游戏安装包是否安装的信息，发送端接收到[onRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)远程安装信息事件监听回调。
7. 根据接收端游戏是否已安装，后续分为两种情况：

   * 接收端未安装游戏

     1. 发送端传输游戏安装包。
     2. 接收端检查游戏中心是否安装，若未安装将重新自动安装游戏中心。
     3. 接收端拉起游戏中心客户端，并打开游戏详情页。
     4. 接收端完成安装包的接收，安装并打开游戏。
     5. 接收端游戏中心客户端向游戏服务返回安装包安装结果。
     6. 接收端游戏服务自动关闭。
   * 接收端已安装游戏

     发送端调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)销毁服务，并确认是否进行资源包传输。若确认进行资源包传输，则发送端创建资源包传输任务，详情请参见[传输资源包](gameservice-nearbytransfer-resource-package.md)。接收端打开已安装的游戏。

   说明

   * destroy接口会清除已接收数据，请确保对已接收数据做好处理或转移后再调用该接口。
   * 发送端或接收端每次调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口都会自动清理自身历史数据。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-nearbytransfer.md)。

| 接口名 | 描述 |
| --- | --- |
| [create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)(createParameters: CreateParameters): Promise<CreateResult> | 创建游戏近场快传服务。 |
| [onRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)(callback: Callback<RemoteInstallationInfo>): void | 订阅远程安装信息事件。 |
| [offRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferoffremoteinstallationinfonotify)(callback?: Callback<RemoteInstallationInfo>): void | 取消订阅远程安装信息事件。 |
| [destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)(): Promise<void> | 销毁游戏近场快传服务。 |

## 接入步骤

### 导入模块

导入Game Service Kit、Share Kit及公共模块。

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';
3. import { fileUri } from '@kit.CoreFileKit';
4. import { gameNearbyTransfer } from '@kit.GameServiceKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';
6. import { common } from '@kit.AbilityKit';
```

### 定义碰一碰/隔空传送分享事件监听和取消监听回调

定义触发碰一碰/隔空传送分享事件监听方法和取消监听回调（收到隔空传送分享事件回调后，建议3秒内调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#share)方法发起分享，否则可能导致超时失败）。

```
1. private immersiveListening() {
2. harmonyShare.on('knockShare', this.immersiveCallback);
3. harmonyShare.on('gesturesShare', this.immersiveCallback);
4. }

6. private immersiveDisablingListening() {
7. harmonyShare.off('knockShare', this.immersiveCallback);
8. harmonyShare.off('gesturesShare', this.immersiveCallback);
9. }

11. private immersiveCallback = async (sharableTarget: harmonyShare.SharableTarget) => {
12. try {
13. let result = await this.create();
14. if (!result) {
15. sharableTarget?.reject(harmonyShare.SharableErrorCode.NO_CONTENT_ERROR);
16. return;
17. }
18. let uiContext: UIContext = this.getUIContext();
19. let contextFaker: Context = uiContext.getHostContext() as Context;
20. let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
21. // 构造分享数据
22. let shareData: systemShare.SharedData = new systemShare.SharedData({
23. utd: utd.UniformDataType.HYPERLINK,
24. content: result,
25. thumbnailUri: fileUri.getUriFromPath(filePath),
26. title: '近场快传',
27. description: '用于进行安装包传输'
28. });
29. // 发起分享
30. sharableTarget?.share(shareData);
31. } catch (err) {
32. sharableTarget?.reject(harmonyShare.SharableErrorCode.NO_CONTENT_ERROR);
33. hilog.error(0x0000, '[nearby]', '%{public}s', `Failed to share the installation package ${err}`);
34. }
35. }
```

### 创建游戏安装包传输任务并注册相关回调

收到碰一碰/隔空传送分享事件回调后，调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口创建安装包传输任务，然后注册[onRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)回调事件。

说明

[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口是调用其他接口的前提，如果未创建游戏近场快传服务或创建失败，将无法调用其他接口。

```
1. public async create(): Promise<string | undefined> {
2. let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
3. let initParam: gameNearbyTransfer.CreateParameters = {
4. abilityName: uiAbilityContext.abilityInfo.name,
5. moduleName: uiAbilityContext.abilityInfo.moduleName,
6. contentType: gameNearbyTransfer.ContentType.INSTALLATION_PACKAGE, // 指定传输类型为安装包
7. gameLinking: "nearbytransfer://com.huawei.nearbytransferdemo?type=nearbyTransfer" // 安装包场景需要传入游戏deeplink
8. };
9. try {
10. let createResult = await gameNearbyTransfer.create(initParam);
11. try {
12. gameNearbyTransfer.onRemoteInstallationInfoNotify(remoteCallBack);
13. } catch (error) {
14. let err = error as BusinessError;
15. hilog.error(0x0000, 'nearby',
16. `Failed to subscribe offRemoteInstallationInfoNotify error. Code: ${err.code}, message: ${err.message}`);
17. }
18. hilog.info(0x0000, '[nearby]', `create success linking: ${createResult.linkingForInstallation}`);
19. return createResult.linkingForInstallation;
20. } catch (error) {
21. let err = error as BusinessError;
22. hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
23. return undefined;
24. }
25. }

27. function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
28. // 对端是否已安装
29. hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
30. }
```

### 注册和取消碰一碰/隔空传送分享监听事件

进入可分享页面时，注册碰一碰/隔空传送分享监听事件；离开可分享页面（包括游戏退至后台等场景）时，取消碰一碰/隔空传送分享监听事件。

```
1. onPageShow(): void {
2. this.immersiveListening();
3. }

5. onPageHide(): void {
6. this.immersiveDisablingListening();
7. }
```

### 发送端销毁服务

接收端完成安装包的接收后，发送端调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)接口销毁服务。若服务销毁后再次使用近场快传服务，需重新[创建游戏近场快传服务并注册相关回调](gameservice-nearbytransfer-resource-package.md#创建游戏近场快传服务并注册相关回调)。

```
1. public destroy(): void {
2. try {
3. gameNearbyTransfer.offRemoteInstallationInfoNotify(remoteCallBack);
4. gameNearbyTransfer.destroy().then(() => {
5. hilog.info(0x0000, 'nearby', `destroy success`);
6. }).catch((err: BusinessError) => {
7. hilog.error(0x0000, 'nearby', `destroy failed. Code: ${err.code}, message: ${err.message}`);
8. });
9. } catch (error) {
10. let err = error as BusinessError;
11. hilog.error(0x0000, 'nearby', `destroy exception. Code: ${err.code}, message: ${err.message}`);
12. }
13. }

15. function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
16. // 对端是否已安装
17. hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
18. }
```
