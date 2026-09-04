---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-installation-package
title: 传输安装包
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发指导 > 传输安装包
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:08+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2a2fc8db071be0ccc839e38ce70f4e940cb9dd763fe5724da230db9c883c56ec
---

游戏近场快传支持已安装游戏的玩家通过碰一碰或隔空传送将游戏安装包传输给未安装游戏的玩家，实现游戏传播效率的提升。

当前版本近场快传提供免集成Game Service Kit实现安装包传输和集成Game Service Kit实现安装包传输两种方式。

**说明** 

* 付费游戏、测试游戏及内测游戏不支持使用近场快传传输安装包。
* 当前版本免集成Game Service Kit实现安装包传输仅支持在手机上使用碰一碰传输，若使用的手机版本不支持免集成传输安装包，碰一碰后将无响应，无法进行传输。

## 免集成Game Service Kit实现安装包传输

从26.0.0版本开始，游戏近场快传服务支持在开发者不集成传输安装包相关能力的情况下，玩家仍可以在手机上通过碰一碰的方式传输游戏安装包给未安装游戏的玩家。

### 用户体验

1. 发送端设备打开游戏后在任意游戏界面与接收端设备通过[碰一碰](knock-share-between-phones-overview.md)触发安装包传输。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/sPRx3GEcRhOeI9-gZmB9Ww/zh-cn_image_0000002742004113.png)
2. 若当前接收端已安装该游戏，则会打开该游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/KL6waiQlQGq9W_nIOYny4g/zh-cn_image_0000002712405124.png)

## 集成Game Service Kit实现安装包传输

从6.1.0(23)版本开始，近场快传服务支持开发者通过集成安装包传输相关能力的方式，实现玩家可以通过碰一碰/隔空传送的方式传输游戏安装包给未安装游戏的玩家。

### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/rN4HiFl7Q92rP8SzMfK2yQ/zh-cn_image_0000002742124073.png)

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

   **说明** 

   * destroy接口会清除已接收数据，请确保对已接收数据做好处理或转移后再调用该接口。
   * 发送端或接收端每次调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口都会自动清理自身历史数据。

### 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-nearbytransfer.md)。

| 接口名 | 描述 |
| --- | --- |
| [create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)(createParameters: CreateParameters): Promise<CreateResult> | 创建游戏近场快传服务。 |
| [onRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)(callback: Callback<RemoteInstallationInfo>): void | 订阅远程安装信息事件。 |
| [offRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferoffremoteinstallationinfonotify)(callback?: Callback<RemoteInstallationInfo>): void | 取消订阅远程安装信息事件。 |
| [destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)(): Promise<void> | 销毁游戏近场快传服务。 |

### 接入步骤

1. 导入Game Service Kit、Share Kit及公共模块。

   ```typescript
   import { uniformTypeDescriptor } from '@kit.ArkData';
   import { systemShare, harmonyShare } from '@kit.ShareKit';
   import { fileUri } from '@kit.CoreFileKit';
   import { gameNearbyTransfer } from '@kit.GameServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 定义触发碰一碰/隔空传送分享事件监听方法和取消监听回调（收到隔空传送分享事件回调后，建议3秒内调用[sharableTarget.share()](../harmonyos-references/share-harmony-share.md#share)方法发起分享，否则可能导致超时失败）。

   ```typescript
   private immersiveListening() {
     harmonyShare.on('knockShare', this.immersiveCallback);
     harmonyShare.on('gesturesShare', this.immersiveCallback);
   }

   private immersiveDisablingListening() {
     harmonyShare.off('knockShare', this.immersiveCallback);
     harmonyShare.off('gesturesShare', this.immersiveCallback);
   }

   private immersiveCallback = async (sharableTarget: harmonyShare.SharableTarget) => {
     try {
       let result = await this.create();
       if (!result) {
         sharableTarget?.reject(harmonyShare.SharableErrorCode.NO_CONTENT_ERROR);
         return;
       }
       let uiContext: UIContext = this.getUIContext();
       let contextFaker: Context = uiContext.getHostContext() as Context;
       let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
       // 构造分享数据
       let shareData: systemShare.SharedData = new systemShare.SharedData({
         utd: uniformTypeDescriptor.UniformDataType.HYPERLINK,
         content: result,
         thumbnailUri: fileUri.getUriFromPath(filePath),
         title: '近场快传',
         description: '用于进行安装包传输'
       });
       // 发起分享
       sharableTarget?.share(shareData);
     } catch (err) {
       sharableTarget?.reject(harmonyShare.SharableErrorCode.NO_CONTENT_ERROR);
       hilog.error(0x0000, '[nearby]', `Failed to share the installation package ${err}`);
     }
   };
   ```
3. 收到碰一碰/隔空传送分享事件回调后，调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口创建安装包传输任务，然后注册[onRemoteInstallationInfoNotify](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)回调事件。

   **说明** 

   [create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口是调用其他接口的前提，如果未创建游戏近场快传服务或创建失败，将无法调用其他接口。

   ```typescript
   public async create(): Promise<string | undefined> {
     let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
     let initParam: gameNearbyTransfer.CreateParameters = {
       abilityName: uiAbilityContext.abilityInfo.name,
       moduleName: uiAbilityContext.abilityInfo.moduleName,
       contentType: gameNearbyTransfer.ContentType.INSTALLATION_PACKAGE, // 指定传输类型为安装包
       gameLinking: 'nearbytransfer://com.huawei.nearbytransferdemo?type=nearbyTransfer' // 安装包场景需要传入游戏deeplink
     };
     try {
       let createResult = await gameNearbyTransfer.create(initParam);
       try {
         gameNearbyTransfer.onRemoteInstallationInfoNotify(remoteCallBack);
       } catch (error) {
         let err = error as BusinessError;
         hilog.error(0x0000, 'nearby',
           `Failed to subscribe offRemoteInstallationInfoNotify error. Code: ${err.code}, message: ${err.message}`);
       }
       hilog.info(0x0000, '[nearby]', `create success linking: ${createResult.linkingForInstallation}`);
       return createResult.linkingForInstallation;
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
       return undefined;
     }
   }

   function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
     // 对端是否已安装
     hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
   }
   ```
4. 进入可分享页面时，注册碰一碰/隔空传送分享监听事件；离开可分享页面（包括游戏退至后台等场景）时，取消碰一碰/隔空传送分享监听事件。

   ```typescript
   onPageShow(): void {
     this.immersiveListening();
   }

   onPageHide(): void {
     this.immersiveDisablingListening();
   }
   ```
5. 接收端完成安装包的接收后，发送端调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)接口销毁服务。若服务销毁后再次使用近场快传服务，需重新[发送端注册相关回调](gameservice-nearbytransfer-resource-package.md#发送端注册相关回调)。

   ```typescript
   public destroy(): void {
     try {
       gameNearbyTransfer.offRemoteInstallationInfoNotify(remoteCallBack);
       gameNearbyTransfer.destroy().then(() => {
         hilog.info(0x0000, 'nearby', `destroy success`);
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'nearby', `destroy failed. Code: ${err.code}, message: ${err.message}`);
       });
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'nearby', `destroy exception. Code: ${err.code}, message: ${err.message}`);
     }
   }

   function remoteCallBack(callback: gameNearbyTransfer.RemoteInstallationInfo) {
     // 对端是否已安装
     hilog.info(0x0000, 'nearby', `remoteInstallationInfoNotify ${callback.installed}`);
   }
   ```
