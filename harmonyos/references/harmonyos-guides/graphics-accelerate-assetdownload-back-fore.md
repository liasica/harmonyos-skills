---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-back-fore
title: 系统后台切应用前台接续下载资源包
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 系统后台切应用前台接续下载资源包
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:037b9fe72164ce5a03d21452f886f10e5cfaf775d01d64a680f88b51f9e32ba3
---

系统后台静默下载过程中启动游戏，应用前台将接管系统后台下载任务，资源包下载任务将在应用前台接续执行。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/jDfeeMkZQNOkrVY1-ybZiw/zh-cn_image_0000002558605562.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=BA7C13DBF2CC043F64458D40770B6934B2F2D515E1843D54F66D7EE2E320F719)

1. 用户在应用市场安装游戏后、用户在应用市场更新游戏后、系统检测到用户设备符合闲时条件时，游戏资源加速服务开启资源包后台下载。
2. 游戏资源加速服务携带manifestUrl资源清单，向资源加速ExtensionAbility获取资源包下载任务列表。
3. 游戏实现资源加速ExtensionAbility的[onDownloadContentRequest](../harmonyos-references/graphics-accelerate-extensionability.md#ondownloadcontentrequest)方法，解析manifestUrl指向的资源清单文件，对比本地资源差异，生成资源包下载任务列表。若manifestUrl不为空，资源加速ExtensionAbility从华为CDN获取下载任务列表，若manifestUrl为空，从三方CDN获取下载任务列表。
4. 资源加速ExtensionAbility向游戏资源加速服务返回不超过200条下载任务的配置信息列表[AssetDownloadConfig](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadconfig)。
5. 游戏资源加速服务根据配置信息列表逐一从华为CDN或三方CDN下载资源包。
6. 游戏资源加速服务每完成一个下载任务，均会向资源加速ExtensionAbility通知当前任务的下载状态。
7. 游戏实现资源加速ExtensionAbility的[onBackgroundDownloadSucceeded](../harmonyos-references/graphics-accelerate-extensionability.md#onbackgrounddownloadsucceeded)方法，接收“成功”状态的下载任务信息，并前往下载路径操作（例如转移、解压）资源文件。游戏实现资源加速ExtensionAbility的[onBackgroundDownloadFailed](../harmonyos-references/graphics-accelerate-extensionability.md#onbackgrounddownloadfailed)方法，接收“失败”状态的下载任务信息，并根据失败原因[DownloadFault](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadfault)自行实现处理逻辑。
8. 用户在后台下载资源包的过程中打开游戏App。
9. 游戏资源加速服务通知资源加速ExtensionAbility即将关闭资源包后台下载功能。
10. 游戏资源加速服务关闭资源包后台下载功能。
11. 游戏向资源加速服务订阅资源包下载进度/状态事件。游戏调用[on('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)方法，监听资源包下载进度。游戏调用[on('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)方法，监听下载任务是否暂停。游戏调用[on('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroncomplete)方法，监听资源是否成功下载。游戏调用[on('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)方法，监听下载任务是否失败。
12. 游戏资源加速服务继续下载资源包。
13. 游戏资源加速服务每完成一个下载任务，还会向游戏通知当前任务的下载进度和下载状态。
14. 若游戏接收到[on('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)方法返回的[DownloadCompletedInfo](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadcompletedinfo)，表示资源包下载成功，游戏可前往下载路径操作（例如转移、解压）资源文件。若游戏接收到[on('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)方法返回的[DownloadFailedInfo](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadfailedinfo)，表示下载任务失败，游戏可以根据[DownloadFault](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadfault)自行实现处理逻辑。若游戏接收到[on('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)方法返回的[AssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadtask)，表示下载任务已暂停，游戏可以携带taskId，调用[resumeAssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerresumeassetdownloadtask)方法，恢复暂停中的下载任务。
15. 游戏向资源加速服务取消订阅资源包下载进度/状态事件。游戏调用[off('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffprogress)方法，取消监听资源包下载进度。游戏调用[off('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffpause)方法，取消监听下载任务暂停事件。游戏调用[off('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffcomplete)方法，取消监听资源包下载成功事件。游戏调用[off('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerofffail)方法，取消监听资源包下载失败事件。

## 开发步骤

1. 在“src/main/module.json5”的extensionAbilities层级中添加资源加速ExtensionAbility信息。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "AssetAccelExtAbility", // 游戏资源加速ExtensionAbility组件的名称。
   4. "srcEntry": "./ets/extensionability/AssetAccelExtAbility.ets", // 游戏资源加速ExtensionAbility组件所对应的代码路径。
   5. "type": "assetAcceleration"
   6. }
   7. ]
   ```
2. 新建extensionability文件夹及AssetAccelExtAbility.ets文件，导入assetDownloadManager模块、AssetAccelerationExtensionAbility模块及相关模块，同时新增AssetAccelExtAbility类继承AssetAccelerationExtensionAbility。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { assetDownloadManager, AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

   4. export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
   5. };
   ```
3. 游戏实现[onDownloadContentRequest](../harmonyos-references/graphics-accelerate-extensionability.md#ondownloadcontentrequest)方法，收集资源包下载任务列表。

   ```
   1. async onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string,
   2. assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig[]> {
   3. console.info('AssetAccelDemo', `onDownloadContentRequest enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.`);
   4. // 1.根据manifestUrl获取下载资源包。2.manifestUrl不为空，获取华为CDN侧资源，为空则获取三方CDN侧资源。3.返回资源包下载任务列表。
   5. let downloadConfigArr: Array<assetDownloadManager.AssetDownloadConfig> = [];
   6. return downloadConfigArr;
   7. }
   ```
4. 游戏实现[onBackgroundDownloadSucceeded](../harmonyos-references/graphics-accelerate-extensionability.md#onbackgrounddownloadsucceeded)方法，接收“成功”状态的下载任务，并前往下载路径操作（例如转移、解压）资源文件。

   ```
   1. async onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask,
   2. filePath: string): Promise<void> {
   3. console.info('AssetAccelDemo', `onBackgroundDownloadSucceeded enter, taskId is ${downloadTask.taskId}, filePath = ${filePath}`);
   4. // 添加已下载资源包转移等处理逻辑。
   5. }
   ```
5. 游戏实现[onBackgroundDownloadFailed](../harmonyos-references/graphics-accelerate-extensionability.md#onbackgrounddownloadfailed)方法，接收“失败”状态的下载任务，并根据失败原因[DownloadFault](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadfault)自行实现处理逻辑。

   ```
   1. async onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask,
   2. fault: assetDownloadManager.DownloadFault): Promise<void> {
   3. console.info('AssetAccelDemo', `onBackgroundDownloadFailed enter, download url: ${downloadTask.config.url}, err: ${fault}`);
   4. // 添加资源包下载失败处理逻辑。
   5. }
   ```
6. 游戏实现[onExtensionWillTerminate](../harmonyos-references/graphics-accelerate-extensionability.md#onextensionwillterminate)方法，接收游戏资源加速服务关闭资源包后台下载功能的通知。

   ```
   1. async onExtensionWillTerminate(error?: BusinessError): Promise<void> {
   2. // 避免进行耗时处理。
   3. if (error) {
   4. console.error('AssetAccelDemo', `onExtensionWillTerminate enter, TerminateReason：${error?.code}, msg: ${error?.message}.`);
   5. // 添加异常终止处理逻辑。
   6. return;
   7. }
   8. // 添加资源清理等处理逻辑。
   9. }
   ```
7. 游戏调用[on('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)方法，监听资源包下载进度。游戏调用[on('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)方法，监听下载任务是否暂停。游戏调用[on('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroncomplete)方法，监听资源是否成功下载。游戏调用[on('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)方法，监听下载任务是否失败。

   ```
   1. onProgressCallback: (progressArray: assetDownloadManager.DownloadProgressInfo[]) => void = (progressArray) => {
   2. console.info('AssetAccelDemo', `onProgressCallback progressArray length: ${progressArray.length}`);
   3. // 添加资源包下载进度处理逻辑。
   4. }

   6. onPauseCallback: (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => void = (downloadTaskInfo) => {
   7. console.info('AssetAccelDemo', `task identifier = ${downloadTaskInfo.config.identifier} has paused.`);
   8. // 添加资源包下载暂停处理逻辑。
   9. }

   11. onCompleteCallback: (completeInfo: assetDownloadManager.DownloadCompletedInfo) => void = async (completeInfo) => {
   12. console.info('AssetAccelDemo', `task identifier = ${completeInfo.downloadTask.config.identifier} has completed.`);
   13. // 添加资源包下载完成处理逻辑。
   14. }

   16. onFailedCallback: (failedInfo: assetDownloadManager.DownloadFailedInfo) => void = async (failedInfo) => {
   17. console.info('AssetAccelDemo', `task identifier = ${failedInfo.downloadTask.config.identifier} has failed.`);
   18. // 添加资源包下载失败处理逻辑。
   19. }

   21. // 订阅下载状态和下载进度事件。
   22. try {
   23. assetDownloadManager.on("progress", this.onProgressCallback);
   24. assetDownloadManager.on("pause", this.onPauseCallback);
   25. assetDownloadManager.on("complete", this.onCompleteCallback);
   26. assetDownloadManager.on("fail", this.onFailedCallback);
   27. } catch (error) {
   28. console.error('AssetAccelDemo', `Failed to do assetDownloadManager.on, errCode: ${error.code}, errMessage: ${error.message}`);
   29. }
   ```
8. 游戏调用[off('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffprogress)方法，取消监听资源包下载进度。游戏调用[off('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffpause)方法，取消监听下载任务暂停事件。游戏调用[off('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffcomplete)方法，取消监听资源包下载成功事件。游戏调用[off('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerofffail)方法，取消监听资源包下载失败事件。

   ```
   1. // 取消订阅下载状态和下载进度事件。
   2. try {
   3. assetDownloadManager.off("progress", this.onProgressCallback);
   4. assetDownloadManager.off("pause", this.onPauseCallback);
   5. assetDownloadManager.off("complete", this.onCompleteCallback);
   6. assetDownloadManager.off("fail", this.onFailedCallback);
   7. } catch (error) {
   8. console.error('AssetAccelDemo', `Failed to do assetDownloadManager.off, errCode: ${error.code}, errMessage: ${error.message}`);
   9. }
   ```
