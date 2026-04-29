---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-file-transmission-based-on-sfft
title: 基于SFFT的大文件高速并发传输
breadcrumb: 最佳实践 > 网络 > 基于SFFT的大文件高速并发传输
category: best-practices
scraped_at: 2026-04-29T14:11:09+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c424248c90bbacce561f2e20cbb357d147600121ad20ad6e2c75cd619ebccc9c
---

## 概述

文件传输（包括上传和下载）是应用程序中极为常见的功能。然而，当应用使用HTTP协议传输长视频、数据集、压缩包等通常超过100MB的大文件时，由于网络不稳定等因素，传输过程可能会耗时较长或直接失败。因此，针对大文件传输的性能优化尤为必要，开发者需要采用特定的策略来确保传输的高效性和可靠性。

目前，super\_fast\_file\_trans（以下简称SFFT）库提供了针对大文件传输过程中的多线程下载、分片上传、断点续传、断点续下及自动重试等特性的完整封装，帮助开发者快速实现大文件传输场景，提高开发效率，开发者可参考[Sample工程](https://gitcode.com/harmonyos_samples/SuperFastFileTrans)进行安装配置与快速上手。下文将以上述SFFT支持的各个特性为例，介绍SFFT的使用。

## 多线程下载

### 场景描述

多线程下载是一种通过同时开启多个线程，并行下载文件不同部分的文件传输特性，能够充分利用带宽资源，显著提升下载速度，尤其适用于下载大文件或在网络带宽受限的环境下下载文件。其核心原理是将文件分割为多个小块，由多个线程同时下载这些部分，并发写入到本地文件中，从而实现高效、稳定的下载。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/fLnslDs9RSulspMx88IPJA/zh-cn_image_0000002236694464.png?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=524A7EA23D6D40EAD1BF3A22423908461BF8786DD86900C0AD4E653F4E97F569 "点击放大")

### 实现原理

SFFT基于[TaskPool](../harmonyos-references/js-apis-taskpool.md)和[@kit.RemoteCommunicationKit](../harmonyos-references/remote-communication-rcp.md)（后续简称RCP）实现了多线程下载，实现流程如下：

当使用多线程下载时：

1. 对于每一个下载任务，SFFT都会在正式下载前发送一个“试连”请求。请求使用RCP的[fetch()](../harmonyos-references/remote-communication-rcp.md#section20139131372817)接口发送，使用的HTTP请求方法为“HEAD”，该请求仅用于获取文件资源的元数据而不会获取实际文件数据。
2. 当试连成功后，SFFT会从HEAD请求响应头中的“content-length”字段中获取文件大小，并根据开发者设置的下载策略将远端文件分成包含起始字节和结束字节的若干个数据块。
3. 对于每一个块，SFFT都会向TaskPool的[TaskGroup](../harmonyos-references/js-apis-taskpool.md#taskgroup10)中添加一个请求任务，该请求任务请求头中的[transferRange](../harmonyos-references/remote-communication-rcp.md#section838945575618)字段与文件块中的起始字节和结束字节相对应，在HTTP请求中，transferRange的值会被转为HTTP请求中的Range请求头字段。
4. SFFT使用TaskPool的[taskpool.execute()](../harmonyos-references/js-apis-taskpool.md#taskpoolexecute)接口启用多个线程并发执行TaskGroup中的任务，获取服务端文件数据。
5. 通过指定[rcp.Request](../harmonyos-references/remote-communication-rcp.md#section10768169134510)的[ResponseBodyDestination](../harmonyos-references/remote-communication-rcp.md#section9250173916506)字段中数据流的写入位置和偏移量，将每个线程请求获取的传输数据并发写入到本地的同一文件中。

### 开发步骤

说明

SFFT三方库使用RCP发送HTTP请求，因此使用了以下权限。权限设置详情参考[应用权限](../harmonyos-guides/remote-communication-preparations.md#section178884218124)。

* ohos.permission.INTERNET：允许应用访问互联网。
* ohos.permission.GET\_NETWORK\_INFO：允许应用获取数据网络信息。

以下代码默认应用已经安装并导入了SFFT三方库，详细的三方库安装教程可以参考["如何使用ohpm引入三四方库"](../harmonyos-faqs/faqs-command-line-tool-13.md)。

* 下载初始化。

  ```
  1. await DownloadManager.getInstance().init(context);
  ```

  [EntryAbility.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L45-L45)
* 开发者开启多线程下载，并指定使用的线程数。

  ```
  1. let downloadConfig: DownloadConfig = {
  2. url: this.url, // URL of the remote file.
  3. fileName: this.fileName, // Local file name.
  4. concurrency: this.concurrency, // Number of download threads. The value is an integer ranging from 1 to 8.
  5. // ...
  6. };
  7. // Create a download task, with downloadListener specified as an optional callback.
  8. this.downloadInstance = DownloadManager.getInstance().createDownloadTask(downloadConfig, downloadListener);
  9. // ...
  10. await this.downloadInstance?.start(); // Enable multi-threaded download.
  ```

  [DownloadItem.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/components/DownloadItem.ets#L102-L166)

* 当开发者未指定下载线程数（concurrency）时，SFFT会根据试连响应中的文件大小信息自动计算启用的线程数。详情可见[Sample工程](https://gitcode.com/harmonyos_samples/SuperFastFileTrans)。

### 实现效果

当使用SFFT进行大文件多线程下载时，下载速率相比于单线程下的普通下载，可以得到明显地提升。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/HJDu_ligQvyimBmu8xF9yQ/zh-cn_image_0000002271813645.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=27BB786232DE01738BABF1C282A252F75A00DAD44333DE7E9E0DA9EC14899DA2 "点击放大")

## 分片上传

### 场景描述

分片上传是一种将本地大文件分成多个小块（分片）后，分别上传的特性，可提升传输效率并减少网络波动的影响。若某个分片上传失败，只需重传该分片，无需重新上传整个文件。结合断点续传技术，即使传输被中断也能继续上传，确保上传过程的稳定性，特别适合复杂的网络环境。分片上传需要服务端支持将多个小文件合并成完整文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/FrrCFzJ5T-aWoM-MfPyeAA/zh-cn_image_0000002271853533.png?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=26E19B781618528516B386F83989DEE6B66705675A51319F753A2E501057EBA9 "点击放大")

### 实现原理

SFFT基于RCP实现了分片上传，实现步骤如下：

1. 对于每一个上传任务，SFFT会先使用[fs.createStream()](../harmonyos-references/js-apis-file-fs.md#fscreatestream)创建一个基于本地文件路径的文件流。
2. 根据分片策略，SFFT会将本地文件分成若干个小块（分片），并创建与分片数量对等的Promise请求，每个Promise将计算对应分片在文件中的字节偏移量，使用Stream对象的[read()](../harmonyos-references/js-apis-file-fs.md#read)接口读取对应的分片数据。
3. SFFT控制Promise的并发度，使用RCP的[fetch()](../harmonyos-references/remote-communication-rcp.md#section20139131372817)接口并发发送上传请求。

### 开发步骤

* 上传初始化。

  ```
  1. await UploadManager.getInstance().init(context);
  ```

  [EntryAbility.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L48-L48)
* 开发者主动启用分片上传，并设置了分片大小。

  ```
  1. let uploadConfig: UploadConfig = {
  2. url: this.isChunk ? CONSTANTS_CONFIG.urls.chunkUploadUrl :
  3. CONSTANTS_CONFIG.urls.ordinaryUploadUrl, // URL of the upload request
  4. filePath: this.filePath, // Local file path.
  5. isChunk: this.isChunk, // Enable chunk upload by setting isChunk to true, which also activates download functionality.
  6. chunkSize: 1024 * 1024 * 10, // Set chunk size to 10MB. This field is effective only when isChunk is set to true.
  7. // ...
  8. };
  9. // Create a upload task, with uploadListener specified as an optional callback.
  10. this.uploadInstance = UploadManager.getInstance().createUploadTask(uploadConfig, uploadListener);
  11. // ...
  12. await this.uploadInstance?.start(); // Enable chunk upload.
  ```

  [UploadItem.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/components/UploadItem.ets#L100-L152)

* 当开发者开启分片上传（isChunk），但并未设置分片大小（chunkSize）时，SFFT会根据本地待上传文件的大小采用默认策略自动计算分片大小，详情可见[Sample工程](https://gitcode.com/harmonyos_samples/SuperFastFileTrans)。

### 实现效果

当使用SFFT进行大文件分片上传时，上传速率相比于不使用分片上传，可以得到明显地提升。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/ZCqri1ihROKJjc20g2Y-dg/zh-cn_image_0000002236854260.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=D5075E1335140C2D70A17F306E5DB48897F6CFD7897909C0C189449F048A3AE2 "点击放大")

## 断点续传/断点续下

### 场景描述

断点续传/断点续下是指在文件下载或上传过程中，因网络中断、程序崩溃等异常导致传输中断后，应用能够从中断处继续传输剩余文件数据的特性。

这一特性尤其适用于大文件传输场景。在数据传输过程中，应用会周期性地自动保存断点信息，以应对突发中断。当应用再次恢复到正常运行状态时，即可从本地读取断点信息，继续传输文件的剩余部分。这种传输方式能有效应对网络不稳定的问题，减少因网络波动而造成的传输失败，节省流量消耗，为用户提供流畅、可靠的传输体验。

### 实现原理

**断点续下**

在SFFT中，断点续下基于上述多线程下载原理，结合关系型数据库[RDB](../harmonyos-references/js-apis-data-relationalstore.md)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zWnDTQpZR9irIOfJYYt_Lw/zh-cn_image_0000002236694468.png?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=FAD8DF16ED130085B2040F1871A8D6133D2637092542FE2E7E8F7FF3A0174CE5 "点击放大")

当使用断点续下时：

1. 对于每个下载任务，为记录完整的下载任务信息，SFFT会调用RDB接口在本地持久化保存完整的任务信息，任务信息包括：任务ID、下载URL、文件名、下载到的文件路径、使用的线程数等。
2. 对于每个下载任务，为记录每个线程的下载状况，SFFT会调用RDB接口在本地持久化保存与使用线程数数量相等的“块信息”，每个块信息包括：块ID、对应的任务ID、块序号、该块在完整文件中的起始字节偏移、当前已下载的字节偏移、该块需要下载的完整字节大小等。
3. 在多线程下载过程中，SFFT会根据实际下载信息周期性地更新上述字段。
4. 当遇到网络中断或程序崩溃等情况，应用再恢复下载时，SFFT会从RDB数据库读取任务信息和块信息，重新设置每个线程对应请求的transferRange，从断点处继续下载。

**断点续传**

在SFFT中，断点续传基于上述分片上传原理，结合RDB实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/JFOIYWxrTq-xMXM048U13w/zh-cn_image_0000002271813649.png?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=0770989FC068EF306702B478FAF0EF768F000D9C2BA21F9E5339E1247C7966C2 "点击放大")

当使用断点续传时：

1. 对于每个上传任务，为记录完整的上传任务信息，SFFT会调用RDB接口在本地持久化保存完整的任务信息，任务信息包括：任务ID、上传URL、本地文件路径、文件哈希值、是否启用分片上传、分片大小、未成功上传的分片序号集合等。
2. 在分片上传过程中，SFFT会根据实际上传信息周期性地更新上述字段。
3. 当遇到网络中断或程序崩溃等情况，应用再恢复上传时，SFFT会从RDB数据库读取任务信息，遍历还未上传成功的分片序号集合并将这些序号对应的分片数据重新上传。

### 开发步骤

* 断点续下。

  ```
  1. let downloadConfig: DownloadConfig = {
  2. url: this.url, // URL of the remote file.
  3. fileName: this.fileName, // Local file name.
  4. concurrency: this.concurrency, // Number of download threads. The value is an integer ranging from 1 to 8.
  5. isBreakpointResume: this.isResumable, // Enable resumable download by setting isBreakpointResume to true.
  6. // ...
  7. };
  8. // Create a download task, with downloadListener specified as an optional callback.
  9. this.downloadInstance = DownloadManager.getInstance().createDownloadTask(downloadConfig, downloadListener);
  10. // ...
  11. await this.downloadInstance?.start(); // Enable multi-threaded download.
  12. // ...
  13. await this.downloadInstance?.pause(); // Pause the download manually or through other methods.
  14. // ...
  15. await this.downloadInstance?.resume(); // Resume the download.
  ```

  [DownloadItem.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/components/DownloadItem.ets#L103-L179)

* 断点续传。

  ```
  1. let uploadConfig: UploadConfig = {
  2. url: this.isChunk ? CONSTANTS_CONFIG.urls.chunkUploadUrl :
  3. CONSTANTS_CONFIG.urls.ordinaryUploadUrl, // URL of the upload request
  4. filePath: this.filePath, // Local file path.
  5. isChunk: this.isChunk, // Enable chunk upload by setting isChunk to true, which also activates download functionality.
  6. chunkSize: 1024 * 1024 * 10, // Set chunk size to 10MB. This field is effective only when isChunk is set to true.
  7. // ...
  8. };
  9. // Create a upload task, with uploadListener specified as an optional callback.
  10. this.uploadInstance = UploadManager.getInstance().createUploadTask(uploadConfig, uploadListener);
  11. // ...
  12. await this.uploadInstance?.start(); // Enable chunk upload.
  13. // ...
  14. await this.uploadInstance?.pause(); // Pause the upload manually or through other methods.
  15. // ...
  16. await this.uploadInstance?.resume(); // Resume the upload.
  ```

  [UploadItem.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/components/UploadItem.ets#L101-L165)

### 实现效果

当使用SFFT进行大文件传输时，文件能从应用退出时的传输断点处重新传输。

| 断点续下 | 断点续传 |
| --- | --- |
|  |  |

## 自动重连

### 场景描述

自动重连是指当文件传输失败时，应用根据异常类型自动尝试重新连接服务端，并继续传输文件数据的特性，目的是为了减少异常情况下的人工干预，确保任务顺利完成。该特性需要断点续下或断点续传支持。

### 实现原理

当使用自动重连时：

* 若在文件传输时遇到网络波动、服务器宕机等导致传输中断的状况，SFFT会自动捕捉到异常。
* 根据异常的类型，SFFT会自动判断是否需要自动重连，并根据开发者设置的重试间隔、重试次数，周期性地尝试发起连接请求，从断点处继续传输。

### 开发步骤

* 以文件下载为例，下面的代码使用了自动重连特性。在下载失败时，将自动尝试进行3次重连，重连间隔为2000毫秒。

  ```
  1. let downloadConfig: DownloadConfig = {
  2. url: this.url, // URL of the remote file.
  3. fileName: this.fileName, // Local file name.
  4. concurrency: this.concurrency, // Number of download threads. The value is an integer ranging from 1 to 8.
  5. isBreakpointResume: this.isResumable, // Enable resumable download by setting isBreakpointResume to true.
  6. maxRetries: 3, // Set the maximum retry attempts to 3.
  7. retryInterval: 2000, // Set the retry interval to 2000 ms.
  8. // ...
  9. };
  10. // Create a download task, with downloadListener specified as an optional callback.
  11. this.downloadInstance = DownloadManager.getInstance().createDownloadTask(downloadConfig, downloadListener);
  ```

  [DownloadItem.ets](https://gitcode.com/harmonyos_samples/SuperFastFileTrans/blob/master/entry/src/main/ets/components/DownloadItem.ets#L104-L120)

### 实现效果

当使用SFFT进行大文件传输时，应用能在网络条件恢复时自动重新连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/YNYyGcmNSFOUxyX7d6JqMA/zh-cn_image_0000002236694472.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061103Z&HW-CC-Expire=86400&HW-CC-Sign=F59EF5F1653EC00510E4DB368C79532F265E8518CC8BADE0CB99D81DA031C0F0 "点击放大")

## 服务端要求

### 下载文件

SFFT依赖服务端支持实现多线程下载，因此服务端需满足以下要求：

1. 服务端支持HEAD请求。
2. 服务端必须支持HTTP协议中的Range请求头，支持分块下载。该字段允许客户端在请求中指定所需数据块的字节范围，而非一次性获取整个文件。

### 上传文件

SFFT依赖服务端支持实现分片下载，因此服务端需满足以下要求：

1. 服务端必须支持“multipart/form-data”类型的请求，这种格式允许文件数据与其他表单数据在同一个HTTP请求中同时上传。
2. 服务端需要具备接收并解析分片数据的能力，能够准确提取上传请求中的表单数据（如分片内容、分片信息等），并将这些数据保存到指定的存储位置。此外，服务端还需确保分片数据的完整性和顺序性，以便能够正确合并还原为完整的文件。

## 示例代码

* [super\_fast\_file\_trans](https://gitcode.com/harmonyos_samples/SuperFastFileTrans)
