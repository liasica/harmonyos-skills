---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-download
title: 使用Web组件的下载能力
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页文件上传与下载 > 使用Web组件的下载能力
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1015254a0cee0a677552856026e46761f5e42f4e102a0c00d3eab95ad23bd82
---

当需要通过Web页面进行文件下载时，可以通过此方式调用Web接口。

## 监听页面触发的下载

通过[setDownloadDelegate()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setdownloaddelegate11)向Web组件注册一个DownloadDelegate来监听页面触发的下载任务。资源由Web组件来下载，Web组件会通过DownloadDelegate将下载的进度通知给应用。

下面的示例中，在应用的rawfile中创建index.html。应用启动后会创建一个Web组件并加载index.html，点击setDownloadDelegate按钮向Web组件注册一个DownloadDelegate，点击页面里的下载按钮的时候会触发一个下载任务，在DownloadDelegate中可以监听到下载的进度。

默认路径在应用沙箱的web目录内，用户无法查看。如果希望用户能够查看，需要将下载路径修改到有访问权限的目录，比如Download目录，请参考[使用Web组件发起一个下载任务](web-download.md#使用web组件发起一个下载任务)。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
9. @State myText: string = 'download';

11. build() {
12. Column() {
13. Text(this.myText)
14. Button('setDownloadDelegate')
15. .onClick(() => {
16. try {
17. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
18. console.info('will start a download.');
19. // 传入一个下载路径，并开始下载。
20. // 如果传入一个不存在的路径，则会下载到默认/data/storage/el2/base/cache/web/目录。
21. webDownloadItem.start('/data/storage/el2/base/cache/web/' + webDownloadItem.getSuggestedFileName());
22. })
23. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
24. // 下载任务的唯一标识。
25. console.info('download update guid: ' + webDownloadItem.getGuid());
26. // 下载的进度。
27. console.info('download update percent complete: ' + webDownloadItem.getPercentComplete());
28. // 当前的下载速度。
29. console.info('download update speed: ' + webDownloadItem.getCurrentSpeed());
30. })
31. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
32. console.error('download failed guid: ' + webDownloadItem.getGuid());
33. // 下载任务失败的错误码。
34. console.error('download failed last error code: ' + webDownloadItem.getLastErrorCode());
35. })
36. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
37. console.info('download finish guid: ' + webDownloadItem.getGuid());
38. this.myText = 'download finish';
39. })
40. this.controller.setDownloadDelegate(this.delegate);
41. } catch (error) {
42. console.error(
43. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })
46. Web({ src: $rawfile('index.html'), controller: this.controller })
47. }
48. }
49. }
```

[ListenForPageDown.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageFileIO/entry/src/main/ets/pages/ListenForPageDown.ets#L16-L66)

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <!-- 点击视频右下方菜单的下载按钮会触发下载任务。-->
6. <video controls="controls" width="800px" height="580px"
7. src="http://vjs.zencdn.net/v/oceans.mp4"
8. type="video/mp4">
9. </video>
10. <a href='data:text/html,%3Ch1%3EHello%2C%20World%21%3C%2Fh1%3E' download='download.html'>下载download.html</a>
11. </body>
12. </html>
```

## 使用Web组件发起一个下载任务

使用[startDownload()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#startdownload11)接口发起一个下载。

Web组件发起的下载会根据当前显示的url以及Web组件默认的Referrer Policy来计算referrer。

在下面的示例中，先点击setDownloadDelegate按钮向Web注册一个监听类，然后点击startDownload主动发起了一个下载，该下载任务也会通过设置的DownloadDelegate来通知app下载的进度。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
9. @State myText: string = 'download';

11. build() {
12. Column() {
13. Text(this.myText)
14. Button('setDownloadDelegate')
15. .onClick(() => {
16. try {
17. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
18. console.info('will start a download.');
19. // 传入一个下载路径，并开始下载。
20. // 如果传入一个不存在的路径，则会下载到默认/data/storage/el2/base/cache/web/目录。
21. webDownloadItem.start('/data/storage/el2/base/cache/web/' + webDownloadItem.getSuggestedFileName());
22. })
23. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
24. console.info('download update guid: ' + webDownloadItem.getGuid());
25. })
26. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
27. console.error('download failed guid: ' + webDownloadItem.getGuid());
28. })
29. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
30. console.info('download finish guid: ' + webDownloadItem.getGuid());
31. this.myText = 'download finish';
32. })
33. this.controller.setDownloadDelegate(this.delegate);
34. } catch (error) {
35. console.error(
36. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
37. }
38. })
39. Button('startDownload')
40. .onClick(() => {
41. try {
42. // 这里指定下载地址为 https://www.example.com/，Web组件会发起一个下载任务将该页面下载下来。
43. // 开发者需要替换为自己想要下载的内容的地址。
44. this.controller.startDownload('https://www.example.com/');
45. } catch (error) {
46. console.error(
47. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Web({ src: 'www.example.com', controller: this.controller })
51. }
52. }
53. }
```

[InitiatingADownloadTask.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageFileIO/entry/src/main/ets/pages/InitiatingADownloadTask.ets#L16-L70)

使用[DocumentViewPicker()](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)获取当前示例的默认下载目录，将该目录设置为下载目录。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { picker, fileUri } from  '@kit.CoreFileKit';
5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 使用DocumentViewPicker()获取当前示例的默认下载目录，将该目录设置为下载目录
19. getDownloadPathFromPicker().then((downloadPath) => {
20. webDownloadItem.start(downloadPath + '/' + webDownloadItem.getSuggestedFileName());
21. });

23. })
24. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
25. // 下载任务的唯一标识。
26. console.info("download update guid: " + webDownloadItem.getGuid());
27. // 下载的进度。
28. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
29. // 当前的下载速度。
30. console.info("download update speed: " + webDownloadItem.getCurrentSpeed())
31. })
32. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
33. console.error("download failed guid: " + webDownloadItem.getGuid());
34. // 下载任务失败的错误码。
35. console.error("download failed last error code: " + webDownloadItem.getLastErrorCode());
36. })
37. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
38. console.info("download finish guid: " + webDownloadItem.getGuid());
39. })
40. this.controller.setDownloadDelegate(this.delegate);
41. } catch (error) {
42. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
43. }
44. })
45. Web({ src: $rawfile('index.html'), controller: this.controller })
46. }
47. }

49. }
50. function getDownloadPathFromPicker(): Promise<string> {
51. return new Promise<string>(resolve => {
52. try {
53. const documentSaveOptions = new picker.DocumentSaveOptions();
54. documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD
55. const documentPicker = new picker.DocumentViewPicker();
56. documentPicker.save(documentSaveOptions).then(async (documentSaveResult: Array<string>) => {
57. if (documentSaveResult.length <= 0) {
58. resolve('');
59. return;
60. }
61. const uriString = documentSaveResult[0];
62. if (!uriString) {
63. resolve('');
64. return;
65. }
66. const uri = new fileUri.FileUri(uriString);
67. resolve(uri.path);
68. }).catch((err: BusinessError) => {
69. console.error(`ErrorCode: ${err.code},  Message: ${err.message}`);
70. resolve('');
71. });
72. } catch (error) {
73. resolve('');
74. }
75. })
76. }
```

说明

Web组件的下载功能要求应用通过调用[WebDownloadItem.start](../harmonyos-references/arkts-apis-webview-webdownloaditem.md#start11)来指定下载文件的保存路径。

值得注意的是，WebDownloadItem.start并非启动下载，下载过程实际上在用户点击页面链接时即已开始。WebDownloadItem.start的作用是将已经下载到临时文件的部分移动到指定目标路径，后续未完成的下载的内容将直接保存到指定目标路径，临时目录位于/data/storage/el2/base/cache/web/Temp/。如果决定取消当前下载，应调用[WebDownloadItem.cancel](../harmonyos-references/arkts-apis-webview-webdownloaditem.md#cancel11)，此时临时文件将被删除。

如果不希望在WebDownloadItem.start之前将文件下载到临时目录，可以通过WebDownloadItem.cancel中断下载，后续可通过[WebDownloadManager.resumeDownload](../harmonyos-references/arkts-apis-webview-webdownloadmanager.md#resumedownload11)恢复中断的下载。

## 使用Web组件恢复进程退出时未下载完成的任务

在Web组件启动时，可通过[resumeDownload()](../harmonyos-references/arkts-apis-webview-webdownloadmanager.md#resumedownload11)接口恢复未完成的下载任务。

在以下示例中，通过“record”按钮将当前下载任务保存至持久化文件中，应用重启后，可借助“recovery”按钮恢复持久化的下载任务。示例代码实现了将当前下载任务持久化保存至文件的功能，若需保存多个下载任务，应用可根据需求调整持久化的时机与方式。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { DownloadUtil, fileName, filePath } from './downloadUtil'; // downloadUtil.ets 见下文

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
10. download: webview.WebDownloadItem = new webview.WebDownloadItem();
11. // 用于记录失败的下载任务。
12. failedData: Uint8Array = new Uint8Array();

14. aboutToAppear(): void {
15. DownloadUtil.init(this.getUIContext());
16. }

18. build() {
19. Column() {
20. Button('setDownloadDelegate')
21. .onClick(() => {
22. try {
23. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
24. console.info('will start a download.');
25. // 传入一个下载路径，并开始下载。
26. // 如果传入一个不存在的路径，则会下载到默认/data/storage/el2/base/cache/web/目录。
27. webDownloadItem.start('/data/storage/el2/base/cache/web/' + webDownloadItem.getSuggestedFileName());
28. })
29. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
30. console.info('download update percent complete: ' + webDownloadItem.getPercentComplete());
31. this.download = webDownloadItem;
32. })
33. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
34. console.error('download failed guid: ' + webDownloadItem.getGuid());
35. // 序列化失败的下载任务到一个字节数组。
36. this.failedData = webDownloadItem.serialize();
37. })
38. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
39. console.info('download finish guid: ' + webDownloadItem.getGuid());
40. })
41. this.controller.setDownloadDelegate(this.delegate);
42. webview.WebDownloadManager.setDownloadDelegate(this.delegate);
43. } catch (error) {
44. console.error(
45. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
46. }
47. })
48. Button('startDownload')
49. .onClick(() => {
50. try {
51. // 这里指定下载地址为 https://www.example.com/，Web组件会发起一个下载任务将该页面下载下来。
52. // 开发者需要替换为自己想要下载的内容的地址。
53. this.controller.startDownload('https://www.example.com/');
54. } catch (error) {
55. console.error(
56. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
57. }
58. })
59. // 将当前的下载任务信息序列化保存，用于后续恢复下载任务。
60. // 当前用例仅展示下载一个任务的场景，多任务场景请按需扩展。
61. Button('record')
62. .onClick(() => {
63. try {
64. // 保存当前下载数据到持久化文档中。
65. DownloadUtil.saveDownloadInfo(DownloadUtil.uint8ArrayToStr(this.download.serialize()));
66. } catch (error) {
67. console.error(
68. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
69. }
70. })
71. // 从序列化的下载任务信息中，恢复下载任务。
72. // 按钮触发时必须保证WebDownloadManager.setDownloadDelegate设置完成。
73. Button('recovery')
74. .onClick(() => {
75. try {
76. // 当前默认持久化文件存在，用户根据实际情况增加判断。
77. let webDownloadItem =
78. webview.WebDownloadItem.deserialize(
79. DownloadUtil.strToUint8Array(DownloadUtil.readFileSync(filePath, fileName)));
80. webview.WebDownloadManager.resumeDownload(webDownloadItem);
81. } catch (error) {
82. console.error(
83. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
84. }
85. })

87. Web({ src: 'www.example.com', controller: this.controller })
88. }
89. }
90. }
```

[ResumeDownload.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageFileIO/entry/src/main/ets/pages/ResumeDownload.ets#L16-L107)

下载任务信息持久化工具类文件。

```
1. import { util } from '@kit.ArkTS';
2. import { fileIo } from '@kit.CoreFileKit';

4. const helper = new util.Base64Helper();

6. export let filePath : string;
7. export const fileName = 'demoFile.txt';
8. export namespace  DownloadUtil {

10. export function init(context: UIContext): void {
11. filePath = context.getHostContext()!.filesDir;
12. }

14. export function uint8ArrayToStr(uint8Array: Uint8Array): string {
15. return helper.encodeToStringSync(uint8Array);
16. }

18. export function strToUint8Array(str: string): Uint8Array {
19. return helper.decodeSync(str);
20. }

22. export function saveDownloadInfo(downloadInfo: string): void {
23. if (!fileExists(filePath)) {
24. mkDirectorySync(filePath);
25. }

27. writeToFileSync(filePath, fileName, downloadInfo);
28. }

30. export function fileExists(filePath: string): boolean {
31. try {
32. return fileIo.accessSync(filePath);
33. } catch (error) {
34. return false;
35. }
36. }

38. export function mkDirectorySync(directoryPath: string, recursion?: boolean): void {
39. try {
40. fileIo.mkdirSync(directoryPath, recursion ?? false);
41. } catch (error) {
42. console.error(`mk dir error. err message: ${error.message}, err code: ${error.code}`);
43. }
44. }

46. export function writeToFileSync(dir: string, fileName: string, msg: string): void {
47. let file = fileIo.openSync(dir + '/' + fileName, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE);
48. fileIo.writeSync(file.fd, msg);
49. }

51. export function readFileSync(dir: string, fileName: string): string {
52. return fileIo.readTextSync(dir + '/' + fileName);
53. }

55. }
```

[downloadUtil.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageFileIO/entry/src/main/ets/pages/downloadUtil.ets#L16-L72)
