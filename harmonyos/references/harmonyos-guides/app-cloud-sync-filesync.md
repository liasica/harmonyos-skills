---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-cloud-sync-filesync
title: 端云文件协同适配指导
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 端云文件协同 > 端云文件协同适配指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be4f7907cac712f27ec7c8308dad3b8488d7ca32b9bf73a553e41756b3d2f6ac
---

为方便开发者使用端云文件协同的文件缓存、同步等能力，此篇指南介绍了环境准备、文件同步和文件缓存，并且在指南的最后提供了完整的应用工程示例。

## 环境准备

* 调试设备：两部鸿蒙设备，系统版本在HarmonyOS 6.0.0.115及以上，云空间版本在6.0.0.300及以上。
* 开发环境：受云空间版本限制，IDE为DevEco Studio 6.0.1 Release或更新版本，构建版本为6.0.1.251，SDK 版本为 API Version 21 Release及以上。
* 配置应用：在项目路径AppScope/app.json5中添加cloudFileSyncEnabled字段为true。

  ```
  1. {
  2. "app": {
  3. "cloudFileSyncEnabled": true
  4. }
  5. }
  ```
* 安装应用：两部设备应用安装后，登录账号，在设置->云空间中找到开发应用同步开关，如下图中的端云协同demo，打开同步开关，可以借助IDE的[Device File Browser](ide-device-file-explorer.md)浏览/data/storage/el2/cloud目录。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/c7eHVxn-SWGAIwPErPp9qg/zh-cn_image_0000002583478281.png?HW-CC-KV=V1&HW-CC-Date=20260427T234119Z&HW-CC-Expire=86400&HW-CC-Sign=E511D790629AD770D07185B91D169A8116578B394D7183DD40BA9FFF25DDFF0C)

## 文件同步

开发者可以使用基本的[文件操作接口](app-file-access.md)，在沙箱路径/data/storage/el2/cloud下进行文件的读写、重命名、拷贝、创建目录等操作，在文件完成写入或文件夹创建成功后，端云协同服务会自动触发同步流程，将新建的文件或文件夹同步上云。

针对一些设备的网络异常、温度过高、电量过低异常场景，受功耗管控，端云协同服务**无法及时**将文件修改同步到云服务器，此时开发者可以通过cloudSync.FileSync对象来订阅同步状态，并根据状态完成对同步的管理。

同时开发者可以在另外一部设备的沙箱路径/data/storage/el2/cloud下，查看到新增的文件或已有文件的修改，另外一部设备主要用于验证多端同步功能。

### 接口说明

| 接口名 | 描述 | 注意事项 |
| --- | --- | --- |
| [FileSync.on(event: 'progress', callback: Callback<SyncProgress>): void](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#onprogress12) | 云盘同步对象添加同步过程事件监听 | 添加监听的对象和触发同步的对象不要混用 |
| [FileSync.off(event: 'progress', callback?: Callback<SyncProgress>): void](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#offprogress12) | 云盘同步对象移除'progress'类型的指定callback回调 | 移除事件监听前，保证要先添加事件监听 |
| [FileSync.start(): Promise<void>](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#start12) | 异步方法启动云盘端云同步 | 添加监听的对象和触发同步的对象保持一致。  **使用约束**：该异步接口仅支持有限并发，调用频率过高会导致整机异常。 |
| [FileSync.stop(): Promise<void>](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#stop12) | 异步方法停止云盘端云同步 | 移除监听的对象和停止同步的对象保持一致 |

### 示例代码

```
1. // Index.ets
2. import { cloudSync } from '@kit.CoreFileKit';

4. @Entry
5. @Component
6. struct Index {
7. @State errorCode: number = 0;
8. @State errorMessage: string = "";
9. // 记录此次同步流程的状态，枚举值参考接口说明
10. @State state: cloudSync.SyncState = cloudSync.SyncState.STOPPED;
11. // 记录同步流程终止时的错误信息，包含温度、电量、网络等错误状态
12. @State errCode: cloudSync.ErrorType = cloudSync.ErrorType.NO_ERROR;
13. // 声明一个FileSync类的对象
14. private fileSync = new cloudSync.FileSync();
15. // 声明一个事件监听函数，用于获取同步状态和同步错误码
16. private cloudSyncCallback = (pg: cloudSync.SyncProgress) => {
17. this.state = pg.state;
18. this.errCode = pg.error;
19. }

21. build() {
22. Column({space: 20}) {
23. // 为FileSync对象添加事件监听，连续点击会捕获异常
24. Button("注册监听").onClick(() => {
25. try {
26. this.fileSync.on("progress", this.cloudSyncCallback);
27. } catch (error) {
28. console.error("注册监听失败: ", error);
29. this.errorCode = error.code;
30. this.errorMessage = error.message;
31. }
32. });
33. // 通过FileSync对象主动触发同步，当端侧和云侧数据不一致时，同步流程会将云上修改同步至端侧，本地修改同步至云上
34. Button("触发同步").onClick(() => {
35. try {
36. this.fileSync.start();
37. } catch (error) {
38. console.error("触发同步失败: ", error);
39. this.errorCode = error.code;
40. this.errorMessage = error.message;
41. }
42. });
43. // 通过FileSync对象主动停止同步，端侧不想与云侧保持同步时，停止同步流程可以停止与云上同步
44. Button("停止同步").onClick(() => {
45. try {
46. this.fileSync.stop();
47. } catch (error) {
48. console.error("停止同步失败: ", error);
49. this.errorCode = error.code;
50. this.errorMessage = error.message;
51. }
52. })
53. // 将同步事件监听移除，移除后，同步状态发生变化，应用将无法感知同步状态以及同步错误码
54. Button("解除监听").onClick(() => {
55. try {
56. this.fileSync.off("progress");
57. } catch (error) {
58. console.error("解注册监听: ", error);
59. this.errorCode = error.code;
60. this.errorMessage = error.message;
61. }
62. });
63. // 用于展示当前同步状态和同步错误码，当网络异常时，错误码为 NETWORK_UNAVAILABLE=1
64. Text(`同步状态：${this.state}`).fontSize(12)
65. Text(`错误码：${this.errCode}`).fontSize(12)
66. }
67. .width("100%")
68. .height("100%")
69. }
70. }
```

## 文件缓存

开发者将/data/storage/el2/cloud目录下的文件上云后，可以选择将本地空间占用释放，同时也可以缓存云上的文件到本地。调用[fileIo.statSync](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-fs.md#fsstatsync)方法可以获取文件的Location信息，根据文件的Location信息，可以有三种状态，分别对应：local=1, cloud=2, local&cloud=3，其中本地新建的文件上云成功后Location为3，此时用户的数据本地一份，云上一份，会同时占用本地空间和云上空间；未上云的文件Location为1，此时用户的数据只有本地一份，只占用本地空间；云上新增的文件，元数据下行到本地时，Location为2，此时用户本地只有元数据信息，文件本身在云上，只占用云上空间。开发者可以通过CloudFileCache对象提供的缓存和释放缓存接口，将Location在2和3之间转换，将本地占用的空间释放或将云上的数据缓存到本地。

### 接口说明

| 接口名 | 描述 | 注意事项 |
| --- | --- | --- |
| [CloudFileCache.on(event: 'progress', callback: Callback<DownloadProgress>): void](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#onprogress11) | 添加云盘文件缓存过程事件监听 | 添加监听的对象和触发缓存的对象不要混用 |
| [CloudFileCache.off(event: 'progress', callback?: Callback<DownloadProgress>): void](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#offprogress11) | 云盘文件缓存对象移除'progress'类型的指定callback回调 | 移除事件监听前，保证要先添加事件监听 |
| [CloudFileCache.start(uri: string): Promise<void>](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#start11) | 异步方法启动云盘文件缓存 | 添加监听的对象和触发缓存的对象保持一致。  **使用约束**：该异步接口仅支持有限并发，最大并发数不超过10，调用超过此限制会导致整机异常。如果云盘文件缓存数超过10，建议使用批量下载接口[startbatch](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#startbatch20) |
| [CloudFileCache.stop(uri: string, needClean?: boolean): Promise<void>](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#stop11) | 异步方法停止云盘文件缓存 | 移除监听的对象和停止缓存的对象保持一致 |
| [CloudFileCache.cleanFileCache(uri: string): void](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-cloudsync.md#cleanfilecache20) | 同步方法删除文件缓存 | 不允许对正在上传的文件进行释放缓存 |

### 示例代码

```
1. // Index.ets
2. import { cloudSync, fileIo, fileUri } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. @State currFilePath: string = "";
9. @State errorCode: number = 0;
10. @State errorMessage: string = "";
11. // 用于记录缓存过程中，单个文件已缓存的大小
12. @State process: number = 0;
13. // 用于记录缓存过程中遇到的错误码，参考接口说明
14. @State downloadErr: cloudSync.DownloadErrorType = cloudSync.DownloadErrorType.NO_ERROR;
15. private context = getContext(this) as common.UIAbilityContext;
16. // 获取当前应用的 /data/storage/el2/cloud 沙箱路径
17. private basePath = this.context.cloudFileDir + "/";
18. // 声明一个 CloudFileCache 的对象
19. private cloudFileCache = new cloudSync.CloudFileCache();
20. // 声明一个缓存过程监听函数，用于监听当前文件的缓存进度
21. private downloadProcess = (pg: cloudSync.DownloadProgress) => {
22. this.process = pg.processed;
23. this.downloadErr = pg.error;
24. }

26. build() {
27. Column({space: 20}) {
28. // 添加文件缓存过程的事件监听
29. Button("注册监听").onClick(() => {
30. try {
31. this.cloudFileCache.on("progress", this.downloadProcess);
32. } catch (error) {
33. console.error("缓存过程注册监听失败: ", error);
34. this.errorCode = error.code;
35. this.errorMessage = error.message;
36. }
37. });
38. // 当本地只有文件元数据信息，文件实体资源在云上时，文件Location信息为2，此时可通过缓存文件将文件实体从云上缓存至本地
39. Button("缓存文件").onClick(() => {
40. try {
41. let uri = fileUri.getUriFromPath(this.basePath + this.currFilePath);
42. let fileStat = fileIo.statSync(this.basePath + this.currFilePath);
43. console.info("文件Location信息：", fileStat.location);
44. this.cloudFileCache.start(uri);
45. } catch (error) {
46. console.error("文件缓存失败: ", error);
47. this.errorCode = error.code;
48. this.errorMessage = error.message;
49. }
50. });
51. // 当文件实体资源在云上和本地都存在时，文件Location信息为3，此时可通过释放缓存将本地占用的空间释放
52. Button("释放缓存").onClick(() => {
53. try {
54. let uri = fileUri.getUriFromPath(this.basePath + this.currFilePath);
55. let fileStat = fileIo.statSync(this.basePath + this.currFilePath);
56. console.info("文件Location信息：", fileStat.location);
57. this.cloudFileCache.cleanFileCache(uri);
58. } catch (error) {
59. console.error("释放文件缓存失败: ", error);
60. this.errorCode = error.code;
61. this.errorMessage = error.message;
62. }
63. });
64. // 对缓存进度监听进行解除注册
65. Button("解除监听").onClick(() => {
66. try {
67. this.cloudFileCache.off("progress");
68. } catch (error) {
69. console.error("解除缓存进度回调失败: ", error);
70. this.errorCode = error.code;
71. this.errorMessage = error.message;
72. }
73. });
74. Text(`缓存进度：${this.process}`).fontSize(12)
75. Text(`错误码：${this.downloadErr}`).fontSize(12)
76. }
77. .width("100%")
78. .height("100%")
79. }
80. }
```

## 文件属性同步

开发者可以设置沙箱内（/data/storage/el2/cloud）文件或目录的自定义扩展属性，设置后该自定义扩展属性可以跟随文件自动上云并同步至多端。

### 接口说明

| 接口名 | 描述 | 注意事项 |
| --- | --- | --- |
| [setxattrSync(path: string, key: string, value: string): Promise<void>](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-fs.md#fileiosetxattrsync12) | 设置文件或目录的扩展属性 | path为沙箱内文件或目录，沙箱根路径：/data/storage/el2/cloud，key需要以user.开头，且长度需小于256字节 |
| [getxattrSync(path: string, key: string): Promise<string>](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-core-file-kit/js-apis-file-fs.md#fileiogetxattrsync12) | 获取文件或目录的扩展属性 | path为沙箱内文件或目录，沙箱根路径：/data/storage/el2/cloud，key需要以user.开头，且长度需小于256字节 |

### 示例代码

```
1. // Index.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { cloudSync, fileIo, fileUri } from '@kit.CoreFileKit';
4. import { common } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. @State fileName: string = "";
10. @State attrKey: string = "";
11. @State attrVal: string = "";
12. private context = getContext(this) as common.UIAbilityContext;
13. private basePath = this.context.cloudFileDir + "/";

15. build() {
16. Column({space: 20}) {
17. // 用来展示当前选中的文件路径
18. Text(`当前选中的文本路径：${this.basePath + this.fileName}`)
19. .fontSize(16).fontWeight(500).margin({top: 10})

21. // 文本输入框，用来选中当前文件
22. TextInput({
23. placeholder: "请输入文件名",
24. text: this.fileName
25. }).onChange((value: string) => {
26. this.fileName = value
27. }).width("80%").height(50).backgroundColor("#f0f0f0").borderRadius(10).margin({top: 20})

29. // 文本输入框，用来输入当前文件的自定义标签key
30. TextInput({
31. placeholder: "请输入自定义标签key",
32. text: this.attrKey
33. }).onChange((value: string) => {
34. this.attrKey = value
35. }).width("80%").height(50).backgroundColor("#f0f0f0").borderRadius(10).margin({top: 20})

37. // 文本输入框，用来输入/输出当前文件的自定义标签value
38. TextInput({
39. placeholder: "设置时，此处需要输入对应的value。获取时，此处用来展示获取到的value",
40. text: this.attrVal
41. }).onChange((value: string) => {
42. this.attrVal = value
43. }).width("80%").height(50).backgroundColor("#f0f0f0").borderRadius(10).margin({top: 20})

45. // 设置自定义标签
46. Button("设置自定义标签").onClick(() => {
47. try {
48. fileIo.setxattrSync(this.basePath + this.fileName, this.attrKey, this.attrVal);
49. console.info("Set extended attribute successfully.");
50. } catch (err) {
51. console.error(`Failed to set extended attribute. Code: ${err.code}, message: ${err.message}`);
52. }
53. });

55. // 获取自定义标签
56. Button("获取自定义标签").onClick(() => {
57. this.attrVal = "";
58. try {
59. let attrValue = fileIo.getxattrSync(this.basePath + this.fileName, this.attrKey);
60. this.attrVal = attrValue;
61. console.info("Get extended attribute succeed, the value is: " + attrValue);
62. } catch (err) {
63. console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
64. }
65. });
66. }
67. }
68. }
```

## 端云协同应用

为便于开发者快速熟悉接口功能，特提供一套涵盖文件缓存、同步及基本文件操作的示例应用代码。该示例支持在两台调试设备间协同工作：设备 A 可创建和编辑文件，设备 B 则可缓存初始文件并在 A 端修改后自动同步更新。[端云文件协同示例链接](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/CoreFile/AppCloudSync)
