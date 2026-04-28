---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsync
title: @ohos.file.cloudSync (端云同步能力)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.cloudSync (端云同步能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:855ad70fd5026afff1e1863efa7a25183eccc8921ce34ef8adbdc22ce4b5419f
---

该模块向应用提供端云同步能力，包括启动/停止端云同步以及启动/停止原图下载功能。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { cloudSync } from '@kit.CoreFileKit';
```

## SyncState12+

PhonePC/2in1TabletTVWearable

端云同步状态，为枚举类型。

说明

以下同步状态发生变更时，如果应用注册了同步过程事件监听，则通过回调通知应用。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UPLOADING | 0 | 上行同步中。 |
| UPLOAD\_FAILED | 1 | 上行同步失败。 |
| DOWNLOADING | 2 | 下行同步中。 |
| DOWNLOAD\_FAILED | 3 | 下行同步失败。 |
| COMPLETED | 4 | 同步成功。 |
| STOPPED | 5 | 同步已停止。 |

## ErrorType12+

PhonePC/2in1TabletTVWearable

端云同步失败类型，为枚举类型。

* 当前阶段，同步过程中，当开启无限量使用移动数据网络，移动数据网络和WIFI均不可用时，才会返回NETWORK\_UNAVAILABLE；开启无限量使用移动数据网络，若有一种类型网络可用，则能正常同步。
* 同步过程中，非充电场景下，电量低于10%，完成当前批上行同步后停止同步，返回低电量；
* 触发同步时，非充电场景下，若电量低于10%，则不允许同步
* 上行时，若云端空间不足，则文件上行失败，云端无该文件记录。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_ERROR | 0 | 没有错误。 |
| NETWORK\_UNAVAILABLE | 1 | 所有网络不可用。 |
| WIFI\_UNAVAILABLE | 2 | WIFI不可用。 |
| BATTERY\_LEVEL\_LOW | 3 | 低电量（低于10%）。 |
| BATTERY\_LEVEL\_WARNING | 4 | 告警电量（低于15%）。 |
| CLOUD\_STORAGE\_FULL | 5 | 云端空间不足。 |
| LOCAL\_STORAGE\_FULL | 6 | 本地空间不足。 |
| DEVICE\_TEMPERATURE\_TOO\_HIGH | 7 | 设备温度过高。 |
| REMOTE\_SERVER\_ABNORMAL20+ | 8 | 远端服务不可用。 |

## SyncProgress12+

PhonePC/2in1TabletTVWearable

端云同步过程。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [SyncState](js-apis-file-cloudsync.md#syncstate12) | 否 | 否 | 枚举值，端云同步状态。 |
| error | [ErrorType](js-apis-file-cloudsync.md#errortype12) | 否 | 否 | 枚举值，同步失败错误类型。 |

## State11+

PhonePC/2in1TabletTVWearable

云文件下载状态，为枚举类型。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RUNNING | 0 | 云文件正在下载中。 |
| COMPLETED | 1 | 云文件下载完成。 |
| FAILED | 2 | 云文件下载失败。 |
| STOPPED | 3 | 云文件下载已停止。 |

## DownloadProgress11+

PhonePC/2in1TabletTVWearable

云文件下载过程。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [State](js-apis-file-cloudsync.md#state11) | 否 | 否 | 枚举值，云文件下载状态。 |
| processed | number | 否 | 否 | 已下载数据大小，取值范围[0，9223372036854775807]（单位：Byte）。 |
| size | number | 否 | 否 | 当前云文件大小，取值范围[0，9223372036854775807]（单位：Byte）。 |
| uri | string | 否 | 否 | 当前云文件URI。 |
| error | [DownloadErrorType](js-apis-file-cloudsync.md#downloaderrortype11) | 否 | 否 | 下载的错误类型。 |

## FileSync12+

PhonePC/2in1TabletTVWearable

云盘同步对象，用于支撑文件管理器应用完成云盘文件的端云同步流程。在使用前，需要先创建FileSync实例。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

### constructor12+

PhonePC/2in1TabletTVWearable

constructor()

端云同步流程的构造函数，用于获取FileSync类的实例。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |

**示例：**

```
1. let fileSync = new cloudSync.FileSync()
```

### on('progress')12+

PhonePC/2in1TabletTVWearable

on(event: 'progress', callback: Callback<SyncProgress>): void

云盘同步对象添加同步过程事件监听。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | Callback<[SyncProgress](js-apis-file-cloudsync.md#syncprogress12)> | 是 | 回调函数。同步过程事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. let fileSync = new cloudSync.FileSync();
2. let callback = (pg: cloudSync.SyncProgress) => {
3. console.info("file sync state: " + pg.state + "error type: " + pg.error);
4. }

6. fileSync.on('progress', callback);
```

### off('progress')12+

PhonePC/2in1TabletTVWearable

off(event: 'progress', callback?: Callback<SyncProgress>): void

云盘同步对象移除'progress'类型的指定callback回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | Callback<[SyncProgress](js-apis-file-cloudsync.md#syncprogress12)> | 否 | 回调函数。同步过程事件， 默认值为null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. let fileSync = new cloudSync.FileSync();

3. let callback = (pg: cloudSync.SyncProgress) => {
4. console.info("file sync state: " + pg.state + "error type: " + pg.error);
5. }

7. fileSync.on('progress', callback);

9. fileSync.off('progress', callback);
```

### start12+

PhonePC/2in1TabletTVWearable

start(): Promise<void>

异步方法启动云盘端云同步。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |
| 22400001 | Cloud status not ready. |
| 22400002 | Network unavailable. |
| 22400003 | Low battery level. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileSync = new cloudSync.FileSync();

5. let callback = (pg: cloudSync.SyncProgress) => {
6. console.info("file sync state: " + pg.state + "error type: " + pg.error);
7. }

9. fileSync.on('progress', callback);

11. fileSync.start().then(() => {
12. console.info("start sync successfully");
13. }).catch((err: BusinessError) => {
14. console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
15. });
```

### start12+

PhonePC/2in1TabletTVWearable

start(callback: AsyncCallback<void>): void

异步方法启动云盘端云同步。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。异步启动端云同步。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 22400001 | Cloud status not ready. |
| 22400002 | Network unavailable. |
| 22400003 | Low battery level. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileSync = new cloudSync.FileSync();

5. fileSync.start((err: BusinessError) => {
6. if (err) {
7. console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
8. } else {
9. console.info("start sync successfully");
10. }
11. });
```

### stop12+

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

异步方法停止云盘端云同步。使用Promise异步回调。

调用stop接口，同步流程会停止。再次调用[start](js-apis-file-cloudsync.md#start12)接口会继续同步。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileSync = new cloudSync.FileSync();

5. fileSync.stop().then(() => {
6. console.info("stop sync successfully");
7. }).catch((err: BusinessError) => {
8. console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
9. });
```

### stop12+

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

异步方法停止云盘端云同步。使用callback异步回调。

调用stop接口，同步流程会停止。再次调用[start](js-apis-file-cloudsync.md#start12)接口会继续同步。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。异步停止端云同步。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileSync = new cloudSync.FileSync();

5. fileSync.stop((err: BusinessError) => {
6. if (err) {
7. console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
8. } else {
9. console.info("stop sync successfully");
10. }
11. });
```

### getLastSyncTime12+

PhonePC/2in1TabletTVWearable

getLastSyncTime(): Promise<number>

异步方法获取上次同步时间。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回上次同步时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileSync = new cloudSync.FileSync();

5. fileSync.getLastSyncTime().then((timeStamp: number) => {
6. let date = new Date(timeStamp);
7. console.info("get last sync time successfully: "+ date);
8. }).catch((err: BusinessError) => {
9. console.error("get last sync time failed with error message: " + err.message + ", error code: " + err.code);
10. });
```

### getLastSyncTime12+

PhonePC/2in1TabletTVWearable

getLastSyncTime(callback: AsyncCallback<number>): void

获取上次同步时间。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。异步获取上次同步时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileSync = new cloudSync.FileSync();

5. fileSync.getLastSyncTime((err: BusinessError, timeStamp: number) => {
6. if (err) {
7. console.error("get last sync time with error message: " + err.message + ", error code: " + err.code);
8. } else {
9. let date = new Date(timeStamp);
10. console.info("get last sync time successfully: "+ date);
11. }
12. });
```

## CloudFileCache11+

PhonePC/2in1TabletTVWearable

云盘文件缓存对象，用来支撑文件管理应用原文件下载流程。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

### construct11+

PhonePC/2in1TabletTVWearable

constructor()

云盘文件缓存流程的构造函数，用于获取CloudFileCache类的实例。多个实例之间不互相共享数据。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes:Incorrect parameter types. |

**示例：**

```
1. let fileCache = new cloudSync.CloudFileCache();
```

### on('progress')11+

PhonePC/2in1TabletTVWearable

on(event: 'progress', callback: Callback<DownloadProgress>): void

添加云盘文件缓存过程事件监听。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件类型，取值为'progress'（下载过程事件）。 |
| callback | Callback<[DownloadProgress](js-apis-file-cloudsync.md#downloadprogress11)> | 是 | 回调函数。云文件下载过程事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileCache = new cloudSync.CloudFileCache();
4. let callback = (pg: cloudSync.DownloadProgress) => {
5. console.info("download state: " + pg.state);
6. };

8. try {
9. fileCache.on('progress', callback);
10. } catch (e) {
11. const error = e as BusinessError;
12. console.error(`Error code: ${error.code}, message: ${error.message}`);
13. }
```

### on('batchDownload')20+

PhonePC/2in1TabletTVWearable

on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void

添加云文件批量缓存事件的监听。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件类型，取值为'batchDownload'，表示批量缓存过程事件。 |
| callback | Callback<[MultiDownloadProgress](js-apis-file-cloudsync.md#multidownloadprogress20)> | 是 | 回调函数。云文件批量缓存过程的事件。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileCache = new cloudSync.CloudFileCache();
4. let callback = (data: cloudSync.MultiDownloadProgress) => {
5. console.info(`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
6. if (data.state == cloudSync.State.COMPLETED) {
7. console.info('Batch download finished.');
8. } else if (data.state == cloudSync.State.FAILED) {
9. console.info(`Batch download stopped, error type: ${data.errType}.`);
10. }
11. };

13. try {
14. fileCache.on('batchDownload', callback);
15. } catch (e) {
16. let error = e as BusinessError;
17. console.error(`Failed to register download callback, error code: ${error.code}, message: ${error.message}`);
18. }
```

### off('progress')11+

PhonePC/2in1TabletTVWearable

off(event: 'progress', callback?: Callback<DownloadProgress>): void

云盘文件缓存对象移除'progress'类型的指定callback回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | Callback<[DownloadProgress](js-apis-file-cloudsync.md#downloadprogress11)> | 否 | 回调函数。云文件下载过程事件。若填写，将视为取消指定的回调函数；否则为取消当前订阅的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileCache = new cloudSync.CloudFileCache();

5. let callback = (pg: cloudSync.DownloadProgress) => {
6. console.info("download state: " + pg.state);
7. }

9. try {
10. fileCache.on('progress', callback);
11. fileCache.off('progress', callback);
12. } catch (e) {
13. const error = e as BusinessError;
14. console.error(`Error code: ${error.code}, message: ${error.message}`);
15. }
```

### off('batchDownload')20+

PhonePC/2in1TabletTVWearable

off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void

云盘文件缓存对象移除由[on](js-apis-file-cloudsync.md#onbatchdownload20)接口添加的云文件批量缓存过程事件的监听。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件类型，取值为'batchDownload'，表示批量缓存过程事件。 |
| callback | Callback<[MultiDownloadProgress](js-apis-file-cloudsync.md#multidownloadprogress20)> | 否 | 回调函数。云文件批量缓存过程事件。如果填写此参数，将取消指定的回调函数；否则，将取消当前订阅的相同事件类型的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileCache = new cloudSync.CloudFileCache();
4. let callback = (pg: cloudSync.MultiDownloadProgress) => {
5. console.info("download state: " + pg.state);
6. }

8. try {
9. fileCache.on('batchDownload', callback);
10. fileCache.off('batchDownload', callback);
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`Failed to unregister download callback, error code: ${error.code}, message: ${error.message}`);
14. }
```

### start11+

PhonePC/2in1TabletTVWearable

start(uri: string): Promise<void>

异步方法启动云盘文件缓存。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待下载文件uri。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 13900025 | No space left on device. |
| 14000002 | Invalid URI. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let fileCache = new cloudSync.CloudFileCache();
5. let path = "/data/storage/el2/cloud/1.txt";
6. let uri = fileUri.getUriFromPath(path);

8. try {
9. fileCache.on('progress', (pg: cloudSync.DownloadProgress) => {
10. console.info("download state: " + pg.state);
11. });
12. } catch (e) {
13. const error = e as BusinessError;
14. console.error(`Error code: ${error.code}, message: ${error.message}`);
15. }

17. fileCache.start(uri).then(() => {
18. console.info("start download successfully");
19. }).catch((err: BusinessError) => {
20. console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
21. });
```

### start11+

PhonePC/2in1TabletTVWearable

start(uri: string, callback: AsyncCallback<void>): void

异步方法启动云盘文件缓存。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待下载文件uri。 |
| callback | AsyncCallback<void> | 是 | 回调函数。异步启动云文件下载。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 13900025 | No space left on device. |
| 14000002 | Invalid URI. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let fileCache = new cloudSync.CloudFileCache();
5. let path = "/data/storage/el2/cloud/1.txt";
6. let uri = fileUri.getUriFromPath(path);

8. fileCache.start(uri, (err: BusinessError) => {
9. if (err) {
10. console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
11. } else {
12. console.info("start download successfully");
13. }
14. });
```

### startBatch20+

PhonePC/2in1TabletTVWearable

startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<number>

启动云文件批量缓存。使用Promise异步回调。

不同的批量缓存任务可以通过接口返回的任务ID区分。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uris | Array<string> | 是 | URI列表，一次调用最多支持传入400个URI，超过报错22400004。 |
| fileType | [DownloadFileType](js-apis-file-cloudsync.md#downloadfiletype20) | 否 | 文件类型，默认值为CONTENT类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回启动的云文件批量缓存任务的ID。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 14000002 | Invalid uri. |
| 22400004 | Exceed the maximum limit. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let fileCache = new cloudSync.CloudFileCache();
4. try {
5. fileCache.on('batchDownload', (pg: cloudSync.MultiDownloadProgress) => {
6. console.info(`batch download state: ${pg.state}`);
7. });
8. } catch (e) {
9. let error = e as BusinessError;
10. console.error(`Failed to unregister download callback, error code: ${error.code}, message: ${error.message}`);
11. }

13. let uriList: Array<string> = [];
14. fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
15. console.info(`start batch download successfully, taskId: ${downloadId}`);
16. }).catch((err: BusinessError) => {
17. console.error(`start download failed with error message: ${err.message}, error code: ${err.code}`);
18. });
```

### stop11+

PhonePC/2in1TabletTVWearable

stop(uri: string, needClean?: boolean): Promise<void>

异步方法停止云盘文件缓存。使用Promise异步回调。

调用stop接口，当前文件下载流程会终止，默认不删除缓存文件，再次调用start接口重新启动下载。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待下载文件uri。 |
| needClean12+ | boolean | 否 | 是否删除已下载的文件。默认值为false表示不删除；true表示删除。  从API version12开始支持该参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 14000002 | Invalid URI. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let fileCache = new cloudSync.CloudFileCache();
5. let path = "/data/storage/el2/cloud/1.txt";
6. let uri = fileUri.getUriFromPath(path);

8. fileCache.stop(uri, true).then(() => {
9. console.info("stop download successfully");
10. }).catch((err: BusinessError) => {
11. console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
12. });
```

### stop11+

PhonePC/2in1TabletTVWearable

stop(uri: string, callback: AsyncCallback<void>): void

异步方法停止云盘文件缓存。使用callback异步回调。

调用stop接口，当前文件下载流程会终止，不删除缓存文件，再次调用start接口重新启动下载。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待下载文件uri。 |
| callback | AsyncCallback<void> | 是 | 回调函数。异步停止云文件下载。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13600001 | IPC error. |
| 13900002 | No such file or directory. |
| 14000002 | Invalid URI. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let fileCache = new cloudSync.CloudFileCache();
5. let path = "/data/storage/el2/cloud/1.txt";
6. let uri = fileUri.getUriFromPath(path);

8. fileCache.stop(uri, (err: BusinessError) => {
9. if (err) {
10. console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
11. } else {
12. console.info("stop download successfully");
13. }
14. });
```

### stopBatch20+

PhonePC/2in1TabletTVWearable

stopBatch(downloadId: number, needClean?: boolean): Promise<void>

停止由[startBatch](js-apis-file-cloudsync.md#startbatch20)启动的云文件批量缓存任务。使用Promise异步回调。

调用stopBatch接口会终止当前文件批量缓存流程，未下载完成的缓存文件是否删除由needClean参数决定。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| downloadId | number | 是 | 需要停止缓存的任务ID。 |
| needClean | boolean | 否 | 是否删除未完成缓存的文件。默认值为false表示不删除；true表示删除。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900020 | Invalid argument. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let taskId = -1;
4. let uriList: Array<string> = [];
5. let fileCache = new cloudSync.CloudFileCache();
6. fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
7. taskId = downloadId;
8. console.info("start batch download successfully");
9. }).catch((err: BusinessError) => {
10. console.error(`start batch download failed with error message: ${err.message}, error code: ${err.code}`);
11. });

13. let needStop = true;
14. if (needStop && taskId > 0) {
15. fileCache.stopBatch(taskId, true).then(() => {
16. console.info("stop batch download successfully");
17. }).catch((err: BusinessError) => {
18. console.error(`stop batch download failed with error message: ${err.message}, error code: ${err.code}`);
19. });
20. }
```

### cleanFileCache20+

PhonePC/2in1TabletTVWearable

cleanFileCache(uri: string): void

同步方法删除文件缓存。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待删除缓存文件的URI。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes:1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes:1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let fileCache = new cloudSync.CloudFileCache();
5. let path = "/data/storage/el2/cloud/1.txt";
6. let uri = fileUri.getUriFromPath(path);

8. try {
9. fileCache.cleanFileCache(uri);
10. } catch (err) {
11. let error:BusinessError = err as BusinessError;
12. console.error("clean file cache failed with error message: " + err.message + ", error code: " + err.code);
13. }
```

## DownloadErrorType11+

PhonePC/2in1TabletTVWearable

端云下载错误类型，为枚举类型。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_ERROR | 0 | 没有错误。 |
| UNKNOWN\_ERROR | 1 | 未知错误。 |
| NETWORK\_UNAVAILABLE | 2 | 网络不可用。 |
| LOCAL\_STORAGE\_FULL | 3 | 本地空间不足。 |
| CONTENT\_NOT\_FOUND | 4 | 云端空间未找到对应文件。 |
| FREQUENT\_USER\_REQUESTS | 5 | 用户请求过于频繁。 |

## DownloadFileType20+

PhonePC/2in1TabletTVWearable

云盘缓存文件类型的枚举。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT | 0 | content类型文件。 |
| THUMBNAIL | 1 | thumbnail类型文件。 |
| LCD | 2 | lcd类型文件。 |

## FailedFileInfo20+

PhonePC/2in1TabletTVWearable

云文件批量缓存失败列表及失败原因。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 下载失败文件URI。 |
| error | [DownloadErrorType](js-apis-file-cloudsync.md#downloaderrortype11) | 否 | 否 | 文件下载失败错误类型。 |

## MultiDownloadProgress20+

PhonePC/2in1TabletTVWearable

云文件批量缓存的进度信息。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [State](js-apis-file-cloudsync.md#state11) | 否 | 否 | 批量缓存任务的执行状态。 |
| taskId | number | 否 | 否 | 批量缓存任务的ID，取值范围为0到INT64\_MAX。如果进度异常，返回值为-1。 |
| successfulCount | number | 否 | 否 | 缓存成功的文件数量，取值范围为0至400，单位：个。如果进度异常，返回值为-1。 |
| failedCount | number | 否 | 否 | 缓存失败的文件数，取值范围为0至400，单位：个。如果进度异常，返回值为-1。 |
| totalCount | number | 否 | 否 | 文件总数，取值范围为0至400，单位：个。如果进度异常，返回值为-1。 |
| downloadedSize | number | 否 | 否 | 已缓存的文件大小，取值范围为 [0, INT64\_MAX)，单位：Byte。如果进度异常，返回值为 INT64\_MAX。 |
| totalSize | number | 否 | 否 | 待缓存的文件总大小，取值范围为 [0, INT64\_MAX)，单位为 Byte。如果进度异常，返回值为 INT64\_MAX。 |
| errType | [DownloadErrorType](js-apis-file-cloudsync.md#downloaderrortype11) | 否 | 否 | 返回批量缓存任务执行失败时的错误类型。 |

### getFailedFiles20+

PhonePC/2in1TabletTVWearable

getFailedFiles(): Array<FailedFileInfo>

获取批量缓存失败的文件列表。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[FailedFileInfo](js-apis-file-cloudsync.md#failedfileinfo20)> | 返回缓存失败的文件URI列表及其对应的错误类型。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let taskId = -1;
4. let failedList: Array<cloudSync.FailedFileInfo> = [];
5. let fileCache = new cloudSync.CloudFileCache();
6. let callback = (data: cloudSync.MultiDownloadProgress) => {
7. console.info(`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
8. if (data.state == cloudSync.State.FAILED) {
9. console.info(`Batch download stopped, error type: ${data.errType}.`);
10. failedList = data.getFailedFiles();
11. }
12. };

14. try {
15. fileCache.on('batchDownload', callback);
16. } catch (e) {
17. let error = e as BusinessError;
18. console.error(`Failed to register download callback, error code: ${error.code}, message: ${error.message}`);
19. }

21. let uriList: Array<string> = [];
22. fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
23. taskId = downloadId;
24. console.info("start batch download successfully");
25. }).catch((err: BusinessError) => {
26. console.error(`start batch download failed with error message: ${err.message}, error code: ${err.code}`);
27. });
```

### getSuccessfulFiles20+

PhonePC/2in1TabletTVWearable

getSuccessfulFiles(): Array<string>

获取批量缓存成功的文件列表。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 数组类型，返回缓存成功的文件URI列表。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let finishedList: Array<string> = [];
4. let fileCache = new cloudSync.CloudFileCache();
5. let callback = (data: cloudSync.MultiDownloadProgress) => {
6. console.info(`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
7. if (data.state == cloudSync.State.COMPLETED) {
8. console.info(`Batch download stopped, error type: ${data.errType}.`);
9. finishedList = data.getSuccessfulFiles();
10. }
11. };

13. try {
14. fileCache.on('batchDownload', callback);
15. } catch (e) {
16. const error = e as BusinessError;
17. console.error(`Failed to register download callback, error code: ${error.code}, message: ${error.message}`);
18. }

20. let uriList: Array<string> = [];
21. fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
22. console.info(`start batch download successfully, taskId: ${downloadId}`);
23. }).catch((err: BusinessError) => {
24. console.error(`start batch download failed with error message: ${err.message}, error code: ${err.code}`);
25. });
```

## cloudSync.registerChange12+

PhonePC/2in1TabletTVWearable

registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void

订阅监听指定文件的变化通知。callback返回更改的数据。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待下载文件uri。 |
| recursion | boolean | 是 | true为监听该URI以及子文件和子目录，false为仅监听该URI文件。 |
| callback | Callback<[ChangeData](js-apis-file-cloudsync.md#changedata12)> | 是 | 回调函数。返回更改的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13900001 | Operation not permitted. |
| 13900002 | No such file or directory. |
| 13900012 | Permission denied. |
| 14000002 | Invalid URI. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';

3. let path = "/data/storage/el2/cloud/1.txt";
4. let uri = fileUri.getUriFromPath(path);
5. let onCallback1 = (changeData: cloudSync.ChangeData) => {
6. if (changeData.type == cloudSync.NotifyType.NOTIFY_ADDED) {
7. // file has been added, do something
8. } else if (changeData.type== cloudSync.NotifyType.NOTIFY_DELETED) {
9. // file has been removed, do something
10. }
11. }
12. cloudSync.registerChange(uri, false, onCallback1);
13. // 取消注册监听
14. cloudSync.unregisterChange(uri);
```

## cloudSync.unregisterChange12+

PhonePC/2in1TabletTVWearable

unregisterChange(uri: string): void

取消订阅监听指定文件的变化通知。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待下载文件uri。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 13900001 | Operation not permitted. |
| 13900002 | No such file or directory. |
| 13900012 | Permission denied. |
| 14000002 | Invalid URI. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';

3. let path = "/data/storage/el2/cloud/1.txt";
4. let uri = fileUri.getUriFromPath(path);
5. let onCallback1 = (changeData: cloudSync.ChangeData) => {
6. if (changeData.type == cloudSync.NotifyType.NOTIFY_ADDED) {
7. // file has been added, do something
8. } else if (changeData.type== cloudSync.NotifyType.NOTIFY_DELETED) {
9. // file has been removed, do something
10. }
11. }
12. cloudSync.registerChange(uri, false, onCallback1);
13. // 取消注册监听
14. cloudSync.unregisterChange(uri);
```

## NotifyType12+

PhonePC/2in1TabletTVWearable

数据变更通知类型。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFY\_ADDED | 0 | 文件已新建。 |
| NOTIFY\_MODIFIED | 1 | 文件已修改。 |
| NOTIFY\_DELETED | 2 | 文件已被删除。 |
| NOTIFY\_RENAMED | 3 | 文件被重命名或者移动。 |

## ChangeData12+

PhonePC/2in1TabletTVWearable

定义变更数据。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NotifyType](js-apis-file-cloudsync.md#notifytype12) | 否 | 否 | 更改的通知类型。 |
| isDirectory | Array<boolean> | 否 | 否 | 指示更改的URI是否为目录。true：是目录。false：非目录。 |
| uris | Array<string> | 否 | 否 | 需要更改的URI列表。 |

## HistoryVersion20+

PhonePC/2in1TabletTVWearable

端云文件历史版本信息，调用端云文件版本管理类[FileVersion](js-apis-file-cloudsync.md#fileversion20)的[gethistoryversionlist](js-apis-file-cloudsync.md#gethistoryversionlist20)方法时，历史版本列表中的属性。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| editedTime | number | 否 | 否 | 文件内容修改时间。 |
| fileSize | number | 否 | 否 | 文件大小，单位：Byte。 |
| versionId | string | 否 | 否 | 文件版本号。 |
| originalFileName | string | 否 | 否 | 当前版本对应的文件名。 |
| sha256 | string | 否 | 否 | 当前版本对应文件内容的哈希值。 |
| autoResolved | boolean | 否 | 否 | 当前版本是否为自动解决冲突的版本。  应用设置手动解冲突时，默认返回false，无意义。  应用设置自动解冲突时，端侧会自动解冲突，true表示当前版本存在冲突，端云服务已自动解决冲突，false表示无冲突，未自动解冲突。 |

**补充说明**：当本地和他端同时修改文件产生冲突时，当前端云同步有自动解冲突机制，但有些应用希望由用户手动解决冲突，此时应用可以通过在项目工程的/entry/src/main/resources/base/profile目录下增加cloudkit\_config.json文件，并配置manualConflictResolutionEnable为true，表示手动解决冲突使能；若应用不需要手动解决冲突，可以不配置该文件或者配置manualConflictResolutionEnable为false，表示采用已有的自动解冲突策略。

配置文件cloudkit\_config.json样例：

```
1. {
2. "cloudKitConfig": {
3. "cloudFileSyncConfig": {
4. "manualConflictResolutionEnable": "true"
5. }
6. }
7. }
```

## VersionDownloadProgress20+

PhonePC/2in1TabletTVWearable

历史版本文件下载状态和进度信息，调用端云文件版本管理类[FileVersion](js-apis-file-cloudsync.md#fileversion20)的[downloadHistoryVersion](js-apis-file-cloudsync.md#downloadhistoryversion20)方法时，回调函数的入参类型。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [State](js-apis-file-cloudsync.md#state11) | 否 | 否 | 所选版本云文件的下载状态。 |
| progress | number | 否 | 否 | 下载进度。 |
| errType | [DownloadErrorType](js-apis-file-cloudsync.md#downloaderrortype11) | 否 | 否 | 若出现下载失败，失败的错误类型。 |

## FileVersion20+

PhonePC/2in1TabletTVWearable

端云文件版本管理类。支持对端云文件的历史版本进行管理，提供获取文件历史版本信息列表的能力，通过历史版本信息，可将历史版本下载到本地；并提供历史版本文件替换当前本地文件的能力，针对版本冲突，提供查询冲突标志，解除冲突标志的能力。

### construct20+

PhonePC/2in1TabletTVWearable

constructor()

端云文件版本管理的构造函数，用于获取FileVersion类的实例。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. let fileVersion = new cloudSync.FileVersion();
```

### getHistoryVersionList20+

PhonePC/2in1TabletTVWearable

getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>

获取历史版本列表，返回内容按修改时间排序，修改时间越早，位置越靠后。使用Promise异步回调。

当云上版本数量小于传入的长度限制时，按照实际版本数量返回历史版本列表。

当云上版本数量大于等于传入的长度限制时，则返回最新的versionNumLimit个版本。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 文件的URI。 |
| versionNumLimit | number | 是 | 历史版本列表长度限制，取值范围[0, 100000]（单位：个）。当输入值大于100000时，按照最大值返回列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[HistoryVersion](js-apis-file-cloudsync.md#historyversion20)>> | Promise对象，返回历史版本列表。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Invalid argument. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400002 | Network unavailable. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let fileVersion = new cloudSync.FileVersion();

6. let path = "/data/storage/el2/cloud/1.txt";
7. let uri = fileUri.getUriFromPath(path);
8. let limit = 10;

10. fileVersion.getHistoryVersionList(uri, limit).then((versionList: Array<cloudSync.HistoryVersion>) => {
11. for(let i = 0, len = versionList.length; i < len; i++) {
12. console.info("get history versionId: " + versionList[i].versionId);
13. }
14. }).catch((err: BusinessError) => {
15. console.error("get history version failed with error message: " + err.message + ", error code: " + err.code);
16. });
```

### downloadHistoryVersion20+

PhonePC/2in1TabletTVWearable

downloadHistoryVersion(uri: string, versionId: string, callback: Callback<[VersionDownloadProgress](js-apis-file-cloudsync.md#versiondownloadprogress20)>): Promise<string>

根据版本号获取指定文件的某一版本的文件内容。用户通过版本号指定云上某一版本，将其下载到本地临时存储路径，临时文件由应用自行决定是否替换原始文件，也可以选择保留或直接删除。callback返回文件下载进度，Promise返回历史版本临时文件的URI。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 文件的URI。 |
| versionId | string | 是 | 文件某一版本的版本号，格式以接口[gethistoryversionlist](js-apis-file-cloudsync.md#gethistoryversionlist20)返回为准。 |
| callback | Callback<[VersionDownloadProgress](js-apis-file-cloudsync.md#versiondownloadprogress20)> | 是 | 回调函数。返回下载进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回历史版本临时存储文件的URI。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400002 | Network unavailable. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let fileVersion = new cloudSync.FileVersion();

6. let path = "/data/storage/el2/cloud/1.txt";
7. let uri = fileUri.getUriFromPath(path);
8. let versionId = '123456'; // 以 getHistoryVersionList 方法返回的格式为准，此处仅作为 demo 示例。

10. let callback = (data: cloudSync.VersionDownloadProgress) => {
11. if (data.state == cloudSync.State.RUNNING) {
12. console.info("download progress: " + data.progress);
13. } else if (data.state == cloudSync.State.FAILED) {
14. console.info("download failed errType: " + data.errType);
15. } else if (data.state == cloudSync.State.COMPLETED) {
16. console.info("download version file success");
17. }
18. };

20. fileVersion.downloadHistoryVersion(uri, versionId, callback).then((fileUri: string) => {
21. console.info("success to begin download, downloadFileUri: " + fileUri);
22. }).catch((err: BusinessError) => {
23. console.error("download history version file failed with error message: " + err.message + ", error code: " + err.code);
24. });
```

### replaceFileWithHistoryVersion20+

PhonePC/2in1TabletTVWearable

replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>

提供使用历史版本文件替换本地文件的能力。在替换前，需要调用[downloadHistoryVersion](js-apis-file-cloudsync.md#downloadhistoryversion20)方法对选择的历史版本进行下载并拿到versionUri；直接调用此接口或者versionUri非法会产生异常；替换完成后会删除临时存储文件。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalUri | string | 是 | 本地文件的URI。 |
| versionUri | string | 是 | 历史版本文件的URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900005 | I/O error. |
| 13900008 | Bad file descriptor. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |
| 22400007 | The version file specified to replace the original file does not exist. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let fileVersion = new cloudSync.FileVersion();

6. let path = "/data/storage/el2/cloud/1.txt";
7. let uri = fileUri.getUriFromPath(path);
8. let versionId = '123456'; // 以 getHistoryVersionList 方法返回的格式为准，此处仅作为 demo 示例。

10. let callback = (data: cloudSync.VersionDownloadProgress) => {
11. if (data.state == cloudSync.State.RUNNING) {
12. console.info("download progress: " + data.progress);
13. } else if (data.state == cloudSync.State.FAILED) {
14. console.info("download failed errType: " + data.errType);
15. } else if (data.state == cloudSync.State.COMPLETED) {
16. console.info("download version file success");
17. }
18. };

20. let versionUri = "";
21. fileVersion.downloadHistoryVersion(uri, versionId, callback).then((fileUri: string) => {
22. versionUri = fileUri;
23. console.info("success to begin download, downloadFileUri: " + fileUri);
24. }).catch((err: BusinessError) => {
25. console.error(`download history version file failed with error message: ${err.message}, error code: ${err.code}`);
26. });
27. fileVersion.replaceFileWithHistoryVersion(uri, versionUri).then(() => {
28. console.info("replace file with history version success.");
29. }).catch((err: BusinessError) => {
30. console.error("replace file with history version failed with error message: " + err.message + ", error code: " + err.code);
31. });
```

### isFileConflict20+

PhonePC/2in1TabletTVWearable

isFileConflict(uri: string): Promise<boolean>

获取本地文件版本冲突标志。使用Promise异步回调。此方法只有应用在配置手动解冲突后才会生效，否则默认自动解冲突，返回值为false，由同步流程自动完成解冲突；

当应用配置手动解冲突后，调用此方法会返回当前文件是否与云侧文件产生冲突，并且由应用提示用户对冲突进行处理，在冲突解决前不会再自动同步上云。当处理完冲突后，需要调用[clearFileConflict](js-apis-file-cloudsync.md#clearfileconflict20)方法来清除冲突标志，后续才会继续触发同步，与云端保持一致。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 文件的URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回本地文件和云端文件的冲突标志，true表示冲突，false表示不冲突。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let fileVersion = new cloudSync.FileVersion();

6. let path = "/data/storage/el2/cloud/1.txt";
7. let uri = fileUri.getUriFromPath(path);

9. fileVersion.isFileConflict(uri).then((isConflict: boolean) => {
10. console.info("current file is conflict: " + isConflict);
11. }).catch((err: BusinessError) => {
12. console.error("get current file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
13. });
```

### clearFileConflict20+

PhonePC/2in1TabletTVWearable

clearFileConflict(uri: string): Promise<void>

清除本地文件版本冲突标志。如果产生冲突，本地解决冲突后需要调用此方法来清除冲突标记，后续才可以触发自动同步机制，和云上保持一致。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待清除冲突标志的文件URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes: 1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes: 1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { fileUri } from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let fileVersion = new cloudSync.FileVersion();

6. let path = "/data/storage/el2/cloud/1.txt";
7. let uri = fileUri.getUriFromPath(path);

9. let isConflict = false;
10. fileVersion.isFileConflict(uri).then((isConflictRet: boolean) => {
11. isConflict = isConflictRet;
12. console.info("current file is conflict: " + isConflictRet);
13. }).catch((err: BusinessError) => {
14. console.error(`get current file conflict flag failed with error message: ${err.message}, error code: ${err.code}`);
15. });
16. fileVersion.clearFileConflict(uri).then(() => {
17. console.info("clean file conflict flag success");
18. }).catch((err: BusinessError) => {
19. console.error("clean file conflict flag failed with error message: " + err.message + ", error code: " + err.code);
20. });
```

## cloudSync.getCoreFileSyncState20+

PhonePC/2in1TabletTVWearable

getCoreFileSyncState(uri: string): FileState

同步方法获取云盘文件同步上行状态。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待获取云盘文件同步上行状态的文件URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FileState](js-apis-file-cloudsync.md#filestate20) | 返回给定云盘文件的同步上行状态。 |

**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. Possible causes:1.IPC failed or timed out. 2.Failed to load the service. |
| 13900002 | No such file or directory. |
| 13900004 | Interrupted system call. |
| 13900010 | Try again. |
| 13900012 | Permission denied by the file system. |
| 13900020 | Invalid argument. Possible causes:1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 13900031 | Function not implemented. |
| 14000002 | Invalid URI. |
| 22400005 | Inner error. Possible causes:1.Failed to access the database or execute the SQL statement. 2.System error, such as a null pointer, insufficient memory or a JS engine exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';

4. let path = "/data/storage/el2/cloud/1.txt";
5. let uri = fileUri.getUriFromPath(path);
6. try {
7. let state = cloudSync.getCoreFileSyncState(uri);
8. } catch (err) {
9. let error:BusinessError = err as BusinessError;
10. console.error(`getCoreFileSyncState failed with error ${error.code}, message is ${error.message}`);
11. }
```

## FileState20+

PhonePC/2in1TabletTVWearable

端云文件同步状态，为枚举类型。

**系统能力**：SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INITIAL\_AFTER\_DOWNLOAD | 0 | 首次下行后的初始状态。 |
| UPLOADING | 1 | 上行同步中。 |
| STOPPED | 2 | 上行已停止。 |
| TO\_BE\_UPLOADED | 3 | 正在等待上行。 |
| UPLOAD\_SUCCESS | 4 | 文件已成功上行。 |
| UPLOAD\_FAILURE | 5 | 文件上行失败。 |
