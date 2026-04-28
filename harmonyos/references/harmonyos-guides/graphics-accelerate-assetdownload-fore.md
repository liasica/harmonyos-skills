---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-fore
title: 应用前台下载资源包
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6706628282f302d98a7a893f8ac81ee18db48f55bf2fada0a3c824f7ee420d71
---

启动游戏后，为游戏提供管理、创建资源包下载任务功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Th1hNzDQSUa7TU1uGu9Kmw/zh-cn_image_0000002552958718.png?HW-CC-KV=V1&HW-CC-Date=20260427T234740Z&HW-CC-Expire=86400&HW-CC-Sign=2C7132C1E58CD5F2F1D572202CEA4D2FE7D2FDF2BB87A4BB76122059B1AE7D2E)

1. 用户打开游戏App。
2. 游戏调用[fetchManifestUrl](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerfetchmanifesturl)方法，从游戏资源加速服务获取manifestUrl资源清单。
3. 游戏根据manifestUrl获取资源包下载任务列表。若manifestUrl不为空，游戏从华为CDN获取资源包下载任务列表，若manifestUrl为空，从三方CDN获取资源包下载任务列表。
4. 游戏向资源加速服务订阅资源包下载进度/状态事件。游戏调用[on('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)方法，监听资源包下载进度。游戏调用[on('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)方法，监听下载任务是否暂停。游戏调用[on('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroncomplete)方法，监听资源是否成功下载。游戏调用[on('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)方法，监听下载任务是否失败。
5. 游戏调用[addAssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageraddassetdownloadtask)方法，新增manifestUrl清单上的资源包下载任务。
6. 游戏资源加速服务根据下载任务逐一下载资源包。
7. 游戏资源加速服务每完成一个下载任务，均会向游戏通知当前任务的下载进度和下载状态。
8. 若游戏接收到[on('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)方法返回的[DownloadCompletedInfo](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadcompletedinfo)，表示资源包下载成功，游戏可前往下载路径操作（例如转移、解压）资源文件。若游戏接收到[on('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)方法返回的[DownloadFailedInfo](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadfailedinfo)，表示下载任务失败，游戏可以根据[DownloadFault](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#downloadfault)自行实现处理逻辑。若游戏接收到[on('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)方法返回的[AssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadtask)，表示下载任务已暂停，游戏可以携带taskId，调用[resumeAssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerresumeassetdownloadtask)方法，恢复暂停中的下载任务。
9. 游戏向资源加速服务取消订阅资源包下载进度/状态事件。游戏调用[off('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffprogress)方法，取消监听资源包下载进度。游戏调用[off('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffpause)方法，取消监听下载任务暂停事件。游戏调用[off('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffcomplete)方法，取消监听资源包下载成功事件。游戏调用[off('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerofffail)方法，取消监听资源包下载失败事件。

## 接口说明

具体API说明请详见[接口文档](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [fetchManifestUrl](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerfetchmanifesturl)(): Promise<string> | 获取资源包文件下载列表。使用Promise异步回调。 |
| [on](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)(type: 'progress', callback: Callback<DownloadProgressInfo[]>): void | 订阅资源包下载进度事件。使用callback形式返回结果。 |
| [on](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)(type: 'pause', callback: Callback<AssetDownloadTask>): void | 订阅资源包下载暂停事件。使用callback形式返回结果。 |
| [on](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroncomplete)(type: 'complete', callback: Callback<DownloadCompletedInfo>): void | 订阅资源包下载成功事件。使用callback形式返回结果。 |
| [on](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)(type: 'fail', callback: Callback<DownloadFailedInfo>): void | 订阅资源包下载失败事件。使用callback形式返回结果。 |
| [addAssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageraddassetdownloadtask)(context: common.BaseContext, downloadConfig: AssetDownloadConfig): Promise<string> | 新增资源包下载任务。使用Promise异步回调。 |
| [off](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffprogress)(type: 'progress', callback?: Callback<DownloadProgressInfo[]>): void | 取消订阅资源包下载进度事件。使用callback形式返回结果。 |
| [off](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffpause)(type: 'pause', callback?: Callback<AssetDownloadTask>): void | 取消订阅资源包下载暂停事件。使用callback形式返回结果。 |
| [off](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffcomplete)(type: 'complete', callback?: Callback<DownloadCompletedInfo>): void | 取消订阅资源包下载成功事件。使用callback形式返回结果。 |
| [off](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerofffail)(type: 'fail', callback?: Callback<DownloadFailedInfo>): void | 取消订阅资源包下载失败事件。使用callback形式返回结果。 |

## 开发步骤

1. 导入assetDownloadManager模块。

   ```
   1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
   2. import { common } from '@kit.AbilityKit';
   ```
2. 游戏调用[fetchManifestUrl](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerfetchmanifesturl)方法，获取manifestUrl资源清单，并根据manifestUrl获取资源包下载任务列表。若manifestUrl不为空，则游戏从华为CDN获取资源包下载任务列表。若manifestUrl为空，则从三方CDN获取资源包下载任务列表。

   ```
   1. async fetchManifestUrl() {
   2. let manifestUrl : string = '';
   3. try {
   4. manifestUrl = await assetDownloadManager.fetchManifestUrl();
   5. console.info('AssetAccelDemo', `Succeeded in fetching manifestUrl, manifestUrl = ${manifestUrl}`);
   6. } catch (error) {
   7. console.error('AssetAccelDemo', `Failed to fetch manifestUrl, errCode: ${error.code}, errMessage: ${error.message}`);
   8. return;
   9. }
   10. // 根据获取到的manifestUrl不为空，获取华为CDN侧资源。若获取到的manifestUrl为空，则获取三方CDN侧资源。
   11. }
   ```
3. 游戏调用[on('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronprogress)方法，监听资源包下载进度。游戏调用[on('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronpause)方法，监听下载任务是否暂停。游戏调用[on('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroncomplete)方法，监听资源是否成功下载。游戏调用[on('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageronfail)方法，监听下载任务是否失败。

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
4. 游戏调用[addAssetDownloadTask](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageraddassetdownloadtask)方法，新增资源包下载任务。

   ```
   1. async addAssetDownloadTask() {
   2. // 构造资源包下载配置信息。
   3. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
   4. fileName: 'fileName', // 下载资源文件名。
   5. url: 'url', // 下载资源url。
   6. isEssential: false, // 是否是必要下载资源。
   7. identifier: 'identifier', // 标识信息。
   8. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
   9. }
   10. try {
   11. // 添加资源包下载任务。
   12. // 根据实际代码上下文自行传入合适的context。
   13. const taskId: string = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
   14. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
   15. } catch (error) {
   16. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
   17. }
   18. }
   ```
5. 游戏调用[off('progress')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffprogress)方法，取消监听资源包下载进度。游戏调用[off('pause')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffpause)方法，取消监听下载任务暂停事件。游戏调用[off('complete')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanageroffcomplete)方法，取消监听资源包下载成功事件。游戏调用[off('fail')](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerofffail)方法，取消监听资源包下载失败事件。

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
