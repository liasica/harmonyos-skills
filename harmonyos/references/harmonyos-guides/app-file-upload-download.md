---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-upload-download
title: 应用文件上传下载
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 上传下载 > 应用文件上传下载
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a74828fea8a3eab611b881a6ee314dad4b1f90db60ade05371a463bd1e945847
---

应用支持将文件上传到网络服务器，也支持从网络服务器下载资源文件到本地目录。

## 上传应用文件

开发者可以使用上传下载模块（[ohos.request](../harmonyos-references/js-apis-request.md)）的上传接口将本地文件上传。文件上传过程通过系统服务代理完成。在API version 12中，request.agent.create接口增加了设置代理地址的参数，支持设置自定义代理地址。

说明

· 当前上传应用文件功能，request.uploadFile方式仅支持上传应用缓存文件路径（cacheDir）下的文件，request.agent方式支持上传用户公共文件和应用缓存文件路径下的文件。

· 使用上传下载模块，需[声明权限](declare-permissions.md)：ohos.permission.INTERNET。

· 上传下载模块不支持Charles、Fiddler等代理抓包工具。

· 上传下载模块接口目前暂不支持子线程调用场景，如[TaskPool](taskpool-introduction.md)等。

以下示例代码展示了两种将缓存文件上传至服务器的方法：

```
1. async requestUploadFile(fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 获取应用文件路径
4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let url = await urlUtils.getUrl(context);
6. let cacheDir = context.cacheDir;

8. // 新建一个本地应用文件
9. try {
10. let file = fs.openSync(cacheDir + '/test.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
11. fs.writeSync(file.fd, 'upload file test');
12. fs.closeSync(file);
13. } catch (error) {
14. let err: BusinessError = error as BusinessError;
15. logger.error(TAG, `Invoke uploadFile failed, code=${err.code}, message=${err.message}`);
16. }

18. // 上传任务配置项
19. let files: request.File[] = [
20. //uri前缀internal://cache 对应cacheDir目录
21. {
22. filename: fileName,
23. name: 'test',
24. uri: 'internal://cache/' + fileName,
25. type: 'txt'
26. }
27. ]
28. let data: request.RequestData[] = [{ name: 'name', value: 'value' }];
29. let uploadConfig: request.UploadConfig = {
30. url: url,
31. header: {
32. 'key1': 'value1',
33. 'key2': 'value2'
34. },
35. method: 'POST',
36. files: files,
37. data: data
38. }

40. // 将本地应用文件上传至网络服务器
41. try {
42. request.uploadFile(context, uploadConfig)
43. .then((uploadTask: request.UploadTask) => {
44. uploadTask.on('complete', (taskStates: Array<request.TaskState>) => {
45. for (let i = 0; i < taskStates.length; i++) {
46. logger.info(TAG, `upload complete taskState: ${JSON.stringify(taskStates[i])}`);
47. }
48. callback(100, true);
49. });
50. })
51. .catch((err: BusinessError) => {
52. logger.error(TAG, `Invoke uploadFile failed, code=${err.code}, message=${err.message}`);
53. })
54. } catch (error) {
55. let err: BusinessError = error as BusinessError;
56. logger.error(TAG, `Invoke uploadFile failed, code=${err.code}, message=${err.message}`);
57. }
58. }
```

[RequestUpload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/upload/RequestUpload.ets#L25-L85)

```
1. async requestAgentUpload(fileName: string, callback: (progress: number, isSucceed: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 获取应用文件路径
4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let url = await urlUtils.getUrl(context);
6. let cacheDir = context.cacheDir;

8. let attachments: request.agent.FormItem[] = [{
9. name: 'test',
10. value: [
11. {
12. filename: fileName,
13. path: cacheDir + '/' + fileName,
14. },
15. ]
16. }];
17. let config: request.agent.Config = {
18. action: request.agent.Action.UPLOAD,
19. url: url,
20. mode: request.agent.Mode.FOREGROUND,
21. overwrite: true,
22. method: 'POST',
23. headers: {
24. 'key1': 'value1',
25. 'key2': 'value2'
26. },
27. data: attachments
28. };
29. request.agent.create(context, config).then((task: request.agent.Task) => {
30. task.start((err: BusinessError) => {
31. if (err) {
32. logger.error(TAG, `Failed to start the upload task, code=${err.code}, message=${err.message}`);
33. return;
34. }
35. });
36. task.on('progress', async (progress) => {
37. logger.info(TAG, `Request upload status ${progress.state}, uploaded ${progress.processed}`);
38. })
39. task.on('completed', async () => {
40. logger.info(TAG, `Request upload completed`);
41. callback(100, true);
42. // 该方法需用户管理任务生命周期，任务结束后调用remove释放task对象
43. request.agent.remove(task.tid);
44. })
45. }).catch((err: BusinessError) => {
46. logger.error(TAG, `Failed to start the upload task, code=${err.code}, message=${err.message}`);
47. });
48. }
```

[RequestUpload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/upload/RequestUpload.ets#L87-L137)

## 下载网络资源文件至应用文件目录

开发者可以使用上传下载模块（[ohos.request](../harmonyos-references/js-apis-request.md)）的下载接口将网络资源文件下载到应用文件目录。对已下载的网络资源应用文件，开发者可以使用基础文件IO接口（[ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)）对其进行访问，使用方式与[应用文件访问](app-file-access.md)一致。文件下载过程使用系统服务代理完成，在api12中request.agent.create接口增加了设置代理地址参数，支持用户设置自定义代理地址。

说明

当前网络资源文件仅支持下载至应用文件目录。

使用上传下载模块，需[声明权限](declare-permissions.md)：ohos.permission.INTERNET。

以下示例代码展示了将网络资源文件下载到应用内部文件目录的两种方法（示例requestDownloadFile中的clearExistFile方法可点击代码块右下角链接查看）：

```
1. async requestDownloadFile(url: string, fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 获取应用文件路径
4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let filesDir = context.cacheDir;
6. let filePath = filesDir + '/' + fileName;
7. this.clearExistFile(filePath);
8. try {
9. await request.downloadFile(context, {
10. url: url,
11. filePath: filePath,
12. }).then((downloadTask: request.DownloadTask) => {
13. downloadTask.on('complete', () => {
14. // 获取文件状态信息，其中包含大小
15. let fileStat = fileIo.statSync(filePath);
16. let fileSize = fileStat.size;
17. logger.info(TAG, `download complete, file= ${url}, size=${fileSize}, progress = 100%`);
18. callback(100, true);
19. })
20. }).catch((err: BusinessError) => {
21. logger.error(TAG, `downloadFile error, code=${err.code}, message=${err.message}`);
22. });
23. } catch (error) {
24. let err: BusinessError = error as BusinessError;
25. logger.error(TAG, `downloadFile catch error, code=${err.code}, message=${err.message}`);
26. }
27. }
```

[RequestDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/RequestDownload.ets#L25-L54)

```
1. async requestAgentDownload(url: string, fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 获取应用文件路径
4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let filesDir = context.cacheDir;

7. let config: request.agent.Config = {
8. action: request.agent.Action.DOWNLOAD,
9. url: url,
10. saveas: fileName,
11. gauge: true,
12. overwrite: true,
13. network: request.agent.Network.WIFI,
14. };
15. await request.agent.create(context, config).then((task: request.agent.Task) => {
16. task.start((error: BusinessError) => {
17. if (error) {
18. logger.error(TAG, `start agent download task error, code=${error.code}, message=${error.message}`);
19. return;
20. }
21. });
22. task.on('progress', async (progress) => {
23. logger.info(TAG, `Request download status ${progress.state}, downloaded ${progress.processed}`);
24. })
25. task.on('completed', async () => {
26. logger.info(TAG, `Request download completed`);
27. let filePath = filesDir + '/' + fileName;
28. // 获取文件状态信息，其中包含大小
29. let fileStat = fileIo.statSync(filePath);
30. let fileSize = fileStat.size;
31. logger.info(TAG, `download complete, file= ${url}, size=${fileSize}, progress = 100%`);
32. callback(100, true);
33. request.agent.remove(task.tid);
34. })
35. }).catch((err: BusinessError) => {
36. logger.error(TAG, `download agent task catch error, code=${err.code}, message=${err.message}`);
37. });
38. }
```

[RequestDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/RequestDownload.ets#L56-L96)

## 下载网络资源文件至用户文件

开发者可以使用[ohos.request](../harmonyos-references/js-apis-request.md)的[request.agent](../harmonyos-references/js-apis-request.md#requestagentcreate10)接口下载网络资源文件到指定的用户文件目录。

说明

从API version 20开始支持下载网络资源文件至用户文件。

### 下载文档类文件

开发者可以通过调用[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)的[save()](../harmonyos-references/js-apis-file-picker.md#save)接口保存文件并获得用户文件的uri，将此uri作为[Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)的saveas字段值进行下载。

```
1. async docFileAgentTask(url: string, fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 创建文件管理器选项实例。
4. try {
5. const documentSaveOptions = new picker.DocumentSaveOptions();
6. // 保存文件名（可选）。 默认为空。
7. documentSaveOptions.newFileNames = [fileName];
8. // 保存文件类型['后缀类型描述|后缀类型']，选择所有文件：'所有文件(*.*)|.*'（可选），如果选择项存在多个后缀（最大限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
9. documentSaveOptions.fileSuffixChoices = ['文档|.txt', '.pdf'];
10. let uri: string = '';
11. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
12. const documentViewPicker = new picker.DocumentViewPicker(context);
13. await documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
14. uri = documentSaveResult[0];
15. logger.info(TAG, `DocumentViewPicker.save to file succeed and uri is ${uri}`);
16. }).catch((err: BusinessError) => {
17. logger.error(TAG, `documentViewPicker.save error, code=${err.code}, message=${err.message}`);
18. })
19. if (uri != '') {
20. let config: request.agent.Config = {
21. action: request.agent.Action.DOWNLOAD,
22. url: url,
23. // saveas字段是DocumentViewPicker保存的文件的uri
24. saveas: uri,
25. gauge: true,
26. // overwrite字段必须为true
27. overwrite: true,
28. network: request.agent.Network.WIFI,
29. // mode字段必须为request.agent.Mode.FOREGROUND
30. mode: request.agent.Mode.FOREGROUND,
31. };
32. try {
33. await request.agent.create(context, config).then((task: request.agent.Task) => {
34. task.start((err: BusinessError) => {
35. if (err) {
36. logger.error(TAG, `start download task error, code=${err.code}, message=${err.message}`);
37. return;
38. }
39. });
40. task.on('progress', async (progress) => {
41. logger.info(TAG, `download status ${progress.state}, downloaded ${progress.processed}`);
42. })
43. task.on('completed', async (progress) => {
44. logger.info(TAG, `download completed ${JSON.stringify(progress)}`);
45. callback(100, true);
46. // 该方法需用户管理任务生命周期，任务结束后调用remove释放task对象
47. request.agent.remove(task.tid);
48. })
49. }).catch((err: BusinessError) => {
50. logger.error(TAG, `Failed to operate a download task, Code: ${err.code}, message: ${err.message}`);
51. });
52. } catch (error) {
53. let err: BusinessError = error as BusinessError;
54. logger.error(TAG, `Failed to create a download task, code=${err.code}, message=${err.message}`);
55. }
56. }
57. } catch (error) {
58. let err: BusinessError = error as BusinessError;
59. logger.error(TAG, `Failed to create a documentSaveOptions, code=${err.code}, message=${err.message}`);
60. return;
61. }
62. }
```

[DocumentDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/userFile/DocumentDownload.ets#L24-L88)

### 下载音频类文件

开发者可以通过调用[AudioViewPicker](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)的[save()](../harmonyos-references/js-apis-file-picker.md#save-3)接口保存文件并获得用户文件的uri，将此uri作为[Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)的saveas字段值进行下载。

```
1. async audioFileAgentTask(url: string, fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 创建文件管理器选项实例。
4. const audioSaveOptions = new picker.AudioSaveOptions();
5. // 保存文件名（可选）。 默认为空。
6. audioSaveOptions.newFileNames = [fileName];

8. let uri: string = '';
9. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
10. const audioViewPicker = new picker.AudioViewPicker(context);
11. await audioViewPicker.save(audioSaveOptions).then((audioSelectResult: Array<string>) => {
12. uri = audioSelectResult[0];
13. logger.info(TAG, `AudioViewPicker.save to file succeed and uri is ${uri}`);
14. }).catch((err: BusinessError) => {
15. logger.error(TAG, `Invoke audioViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
16. })
17. if (uri != '') {
18. let config: request.agent.Config = {
19. action: request.agent.Action.DOWNLOAD,
20. url: url,
21. // saveas字段是AudioViewPicker保存的文件的uri
22. saveas: uri,
23. gauge: true,
24. // overwrite字段必须为true
25. overwrite: true,
26. network: request.agent.Network.WIFI,
27. // mode字段必须为request.agent.Mode.FOREGROUND
28. mode: request.agent.Mode.FOREGROUND,
29. };
30. try {
31. request.agent.create(context, config).then((task: request.agent.Task) => {
32. task.start((err: BusinessError) => {
33. if (err) {
34. logger.error(TAG, `Failed to start the download task, Code: ${err.code}  message: ${err.message}`);
35. return;
36. }
37. });
38. task.on('progress', async (progress) => {
39. logger.info(TAG, `Request download status ${progress.state}, downloaded ${progress.processed}`);
40. })
41. task.on('completed', async (progress) => {
42. logger.info(TAG, `Request download completed, ${JSON.stringify(progress)}`);
43. callback(100, true);
44. // 该方法需用户管理任务生命周期，任务结束后调用remove释放task对象.
45. request.agent.remove(task.tid);
46. })
47. }).catch((err: BusinessError) => {
48. logger.error(TAG, `Failed to create a download task, code=${err.code}, message=${err.message}`);
49. });
50. } catch (error) {
51. let err: BusinessError = error as BusinessError;
52. logger.error(TAG, `Failed to create a audio download task, code=${err.code}, message=${err.message}`);
53. }
54. }
55. }
```

[AudioDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/userFile/AudioDownload.ets#L24-L81)

### 下载图片或视频类文件

开发者可以通过调用PhotoAccessHelper[模块描述](../harmonyos-references/arkts-apis-photoaccesshelper.md)的[createAsset()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#createasset-2)接口创建媒体文件并获取用户文件的URI，将其作为[Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)的saveas字段值进行下载。

需要权限：[ohos.permission.WRITE\_IMAGEVIDEO](restricted-permissions.md#ohospermissionwrite_imagevideo)

权限[ohos.permission.WRITE\_IMAGEVIDEO](restricted-permissions.md#ohospermissionwrite_imagevideo)是[权限机制中的基本概念](app-permission-mgmt-overview.md#权限机制中的基本概念)中system\_basic(系统基础服务)级别的[受限开放权限](restricted-permissions.md)，normal等级的应用需要将自身的APL等级声明为system\_basic及以上。授权方式为user\_grant，需要[向用户申请授权](request-user-authorization.md)。

```
1. async mediaFileAgentTask(url: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
4. bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
5. // 获取应用程序的accessTokenID。
6. let tokenID = -1;
7. try {
8. await bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
9. logger.info(TAG, `Request getBundleInfoForSelf successfully. Data: ${JSON.stringify(data)}`);
10. tokenID = data.appInfo.accessTokenId;
11. }).catch((err: BusinessError) => {
12. logger.error(TAG, `GetBundleInfoForSelf failed, code=${err.code}, message=${err.message}`);
13. });
14. } catch (err) {
15. let message = (err as BusinessError).message;
16. logger.error(`GetBundleInfoForSelf failed: ${message}`);
17. }

19. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
20. let grant = true;
21. // 校验应用是否授予权限。使用Promise异步回调。
22. await atManager.checkAccessToken(tokenID, 'ohos.permission.WRITE_IMAGEVIDEO')
23. .then((data: abilityAccessCtrl.GrantStatus) => {
24. logger.info(TAG, `Request checkAccessToken success, data->${JSON.stringify(data)}`);
25. if (data != abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
26. grant = false;
27. }
28. })
29. .catch((err: BusinessError) => {
30. logger.error(TAG, `CheckAccessToken fail, code=${err.code}, message=${err.message}`);
31. });

33. if (!grant) {
34. // 用于UIAbility拉起弹框请求用户授权。使用callback异步回调。
35. await atManager.requestPermissionsFromUser(context, ['ohos.permission.WRITE_IMAGEVIDEO'])
36. .then((data: PermissionRequestResult) => {
37. logger.info(TAG, `Request grant: ${JSON.stringify(data)}`);
38. logger.info(TAG, `Request grant permissions: ${data.permissions}`);
39. logger.info(TAG, `Request grant authResults: ${data.authResults}`);
40. logger.info(TAG, `Request grant dialogShownResults: ${data.dialogShownResults}`);
41. }).catch((err: BusinessError) => {
42. logger.error(TAG, `Grant error, code=${err.code}, message=${err.message}`);
43. });
44. }

46. try {
47. let photoType: photoAccessHelper.PhotoType = photoAccessHelper.PhotoType.IMAGE;
48. let extension: string = 'jpg';
49. let options: photoAccessHelper.CreateOptions = {
50. title: 'media'
51. }
52. // 获取相册管理模块的实例，用于访问和修改相册中的媒体文件。
53. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
54. // 指定文件类型、后缀和创建选项，创建图片或视频资源，以Promise方式返回结果。
55. let uri: string = await phAccessHelper.createAsset(photoType, extension, options);
56. logger.info(TAG, `Request createAsset uri ${uri}`);

58. let config: request.agent.Config = {
59. action: request.agent.Action.DOWNLOAD,
60. url: url,
61. // saveas字段是PhotoAccessHelper保存的文件的uri
62. saveas: uri,
63. gauge: true,
64. // overwrite字段必须为true
65. overwrite: true,
66. network: request.agent.Network.WIFI,
67. // mode字段必须为request.agent.Mode.FOREGROUND
68. mode: request.agent.Mode.FOREGROUND,
69. };
70. request.agent.create(context, config).then((task: request.agent.Task) => {
71. task.start((err: BusinessError) => {
72. if (err) {
73. logger.error(TAG, `Failed to start the download task, Code: ${err.code}  message: ${err.message}`);
74. return;
75. }
76. });
77. task.on('progress', async (progress) => {
78. logger.info(TAG, `Request download status ${progress.state}, downloaded ${progress.processed}`);
79. })
80. task.on('completed', async (progress) => {
81. logger.info(TAG, `Request download completed, ${JSON.stringify(progress)}`);
82. callback(100, true);
83. // 该方法需用户管理任务生命周期，任务结束后调用remove释放task对象
84. request.agent.remove(task.tid);
85. })
86. }).catch((err: BusinessError) => {
87. logger.error(TAG, `Failed to operate a download task, Code: ${err.code}, message: ${err.message}`);
88. });
89. } catch (error) {
90. let err: BusinessError = error as BusinessError;
91. logger.error(TAG, `Failed to create a media download task, code=${err.code}, message=${err.message}`);
92. }
93. }
```

[MediaDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/userFile/MediaDownload.ets#L26-L121)

## 添加任务速度限制与超时限制

开发者可以使用[ohos.request (上传下载)](../harmonyos-references/js-apis-request.md)模块中的接口上传本地文件或下载网络资源文件。为方便对任务速度及时长进行限制，分别在API version 18中增加了[setMaxSpeed](../harmonyos-references/js-apis-request.md#setmaxspeed18)接口，支持用户设置任务的最高速度限制；在API version 20的[request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10-1)接口中增加了最低限速及超时参数，支持用户自定义最低速度限制以及超时时间。

以下是对下载任务进行速度限制与超时限制的方式的示例代码演示：

```
1. async speedLimitDownload(url: string, fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 获取应用文件路径
4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let filesDir = context.cacheDir;

7. let config: request.agent.Config = {
8. action: request.agent.Action.DOWNLOAD,
9. url: url,
10. saveas: fileName,
11. gauge: true,
12. overwrite: true,
13. network: request.agent.Network.WIFI,
14. // 最低速度限制规则：
15. // 1. 若任务速度持续低于设定值（如：16 * 1024 B/s）达到指定时长（如：10s），则任务失败
16. // 2. 重置计时条件：
17. // - 任一秒速度超过最低限速
18. // - 任务暂停后恢复
19. // - 任务停止后重启
20. minSpeed: {
21. speed: 16 * 1024,
22. duration: 10
23. },
24. // 超时控制规则：
25. // 1. 连接超时（connectionTimeout）：
26. // - 单次连接建立耗时超过设定值（如：60s）则任务失败
27. // - 多次连接时各次独立计时（不累积）
28. // 2. 总超时（totalTimeout）：
29. // - 任务总耗时（含连接+传输时间）超过设定值（如：120s）则失败
30. // - 暂停期间不计时，恢复后累积计时
31. // 3. 重置计时条件：任务失败或停止时重置计时
32. timeout: {
33. connectionTimeout: 60,
34. totalTimeout: 120,
35. }
36. };
37. request.agent.create(context, config).then((task: request.agent.Task) => {
38. // 设置任务速度上限
39. task.setMaxSpeed(10 * 1024 * 1024).then(() => {
40. logger.info(TAG, `Succeeded in setting the max speed of the task. result: ${task.tid}`);
41. }).catch((err: BusinessError) => {
42. logger.error(TAG, `Failed to set the max speed of the task, code=${err.code}, message=${err.message}`);
43. });
44. task.start((err: BusinessError) => {
45. if (err) {
46. logger.error(TAG, `Failed to start the download task, code=${err.code}, message=${err.message}`);
47. return;
48. }
49. });
50. task.on('progress', async (progress) => {
51. logger.info(TAG, `Request download status ${progress.state}, downloaded ${progress.processed}`);
52. })
53. task.on('completed', async () => {
54. logger.info(TAG, `Request download completed`);
55. // 获取文件状态信息，其中包含大小
56. let filePath = filesDir + '/' + fileName;
57. // 获取文件状态信息，其中包含大小
58. let fileStat = fileIo.statSync(filePath);
59. let fileSize = fileStat.size;
60. logger.info(TAG, `download complete, file= ${url}, size=${fileSize}, progress = 100%`);
61. callback(100, true);
62. request.agent.remove(task.tid);
63. })
64. }).catch((err: BusinessError) => {
65. logger.error(TAG, `Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
66. });
67. }
```

[SpeedLimitDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/SpeedLimitDownload.ets#L24-L93)

## 添加网络配置

### HTTP拦截

开发者可以通过设置配置文件实现HTTP拦截功能。上传下载模块在应用配置文件中禁用HTTP后，无法创建明文HTTP传输的上传下载任务。配置文件在APP中的路径是：src/main/resources/base/profile/network\_config.json。请参考网络管理模块配置文件[网络连接安全配置](../best-practices/bpta-network-ca-security.md#section5454123841911)，了解需要配置的具体参数。

参考配置文件如下所示：

```
1. {
2. "network-security-config": {
3. "base-config": {
4. "cleartextTrafficPermitted": true,
5. "trust-anchors": [
6. {
7. "certificates": "/etc/security/certificates"
8. }
9. ]
10. },
11. "domain-config": [
12. {
13. "cleartextTrafficPermitted": true,
14. "domains": [
15. {
16. "include-subdomains": true,
17. "name": "*.example.com"
18. }
19. ],
20. }
21. ]
22. }
23. }
```

## 使用WantAgent实现通知栏跳转功能

从API version 22开始，开发者可以使用[wantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md)接口与上传下载模块结合，实现点击任务通知后跳转至应用指定页面的功能。

### 功能介绍

通过在下载任务的配置[request.agent.Notification](../harmonyos-references/js-apis-request.md#requestagentnotification15)中设置wantAgent参数，开发者可以指定用户点击通知后要跳转的应用页面及相关参数。当用户点击正在进行或已完成的下载任务通知时，系统会根据wantAgent参数启动指定的应用能力。

### 示例代码

以下示例代码展示了如何创建一个带有wantAgent功能的下载任务：

```
1. async wantAgentDownload(url: string, fileName: string, callback: (progress: number, isSuccess: boolean) => void,
2. context: common.UIAbilityContext) {
3. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext

5. // 创建wantAgentInfo对象，用于定义点击通知后要执行的操作
6. let wantAgentInfo: wantAgent.WantAgentInfo = {
7. wants: [
8. {
9. deviceId: '',
10. bundleName: 'com.samples.uploaddownloadguide', // 替换为实际应用的包名
11. abilityName: 'EntryAbility', // 替换为实际的ability名称
12. action: '',
13. entities: [],
14. uri: '',
15. parameters: {} // 可以传递自定义参数
16. }
17. ],
18. actionType: wantAgent.OperationType.START_ABILITY,
19. requestCode: 0,
20. wantAgentFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
21. };

23. // 获取WantAgent实例
24. let wantAgentInstance: WantAgent;
25. try {
26. wantAgentInstance = await wantAgent.getWantAgent(wantAgentInfo);
27. } catch (error) {
28. logger.error(TAG, `Failed to get WantAgent, Code: ${error.code}  message: ${error.message}`);
29. return;
30. }

32. let filesDir = context.cacheDir;
33. // 创建下载任务配置，包含wantAgent参数
34. let config: request.agent.Config = {
35. action: request.agent.Action.DOWNLOAD,
36. url: url, // 替换为实际的下载地址
37. title: '下载任务通知标题',
38. description: '下载任务通知描述',
39. mode: request.agent.Mode.BACKGROUND,
40. overwrite: true,
41. method: 'GET',
42. saveas: fileName,
43. network: request.agent.Network.ANY,
44. gauge: true,
45. notification: {
46. visibility: request.agent.VISIBILITY_COMPLETION | request.agent.VISIBILITY_PROGRESS,
47. wantAgent: wantAgentInstance,
48. }
49. };

51. // 创建并启动下载任务
52. try {
53. request.agent.create(context, config).then((task: request.agent.Task) => {
54. task.start((err: BusinessError) => {
55. if (err) {
56. logger.error(TAG, `Failed to start the download task, Code: ${err.code}  message: ${err.message}`);
57. return;
58. }
59. });
60. task.on('progress', async (progress) => {
61. logger.error(TAG, `Request download status ${progress.state}, downloaded ${progress.processed}`);
62. })
63. task.on('completed', async (progress) => {
64. console.warn('Request download completed, ' + JSON.stringify(progress));
65. logger.error(TAG, `Request download completed, ${JSON.stringify(progress)}`);
66. // 获取文件状态信息，其中包含大小
67. let filePath = filesDir + '/' + fileName;
68. // 获取文件状态信息，其中包含大小
69. let fileStat = fileIo.statSync(filePath);
70. let fileSize = fileStat.size;
71. logger.info(TAG, `download complete, file= ${url}, size=${fileSize}, progress = 100%`);
72. callback(100, true);
73. // 该方法需用户管理任务生命周期，任务结束后调用remove释放task对象
74. request.agent.remove(task.tid);
75. })
76. }).catch((err: BusinessError) => {
77. logger.error(TAG, `Failed to operate a download task, Code: ${err.code}, message: ${err.message}`);
78. });
79. } catch (error) {
80. let err: BusinessError = error as BusinessError;
81. logger.error(TAG, `Failed to operate a download task, Code: ${err.code}, message: ${err.message}`);
82. }
83. }
```

[WantAgentDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Basic-Services-Kit/request/UploadDownloadGuide/features/uploadanddownload/src/main/ets/download/WantAgentDownload.ets#L26-L111)

### 配置说明

在上面的示例代码中，我们主要通过以下几个步骤实现了通知栏跳转功能：

1. **创建WantAgentInfo对象**：定义点击通知后要执行的操作，包括目标应用的包名、ability名称和需要传递的具体参数。
2. **获取WantAgent实例**：通过wantAgent.getWantAgent()方法获取WantAgent实例。
3. **配置下载任务**：在request.agent.Config中设置notification属性，并将wantAgent参数设置为前面获取的WantAgent实例。
4. **设置通知可见性**：通过visibility参数可以控制通知显示的内容，例如进度、完成状态等。

### 注意事项

* 此功能仅支持API version 22及以上版本。
* 确保在配置wantAgentInfo时，填写正确的应用包名和ability名称。
* wantAgent参数需要与notification参数配合使用，才能在通知中显示跳转功能。
* 在实际应用中，建议根据业务需求调整通知的标题、描述、可见性以及其他相关参数。
