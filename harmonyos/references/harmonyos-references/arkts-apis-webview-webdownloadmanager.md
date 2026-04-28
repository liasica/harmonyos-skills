---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloadmanager
title: Class (WebDownloadManager)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebDownloadManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c3d3137fad5854e8a12818711fa57d1f372481ca89f63ad253572369e4f25e19
---

可以通过该类提供的接口来恢复失败的下载任务。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 11开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## setDownloadDelegate11+

PhonePC/2in1TabletTVWearable

static setDownloadDelegate(delegate: WebDownloadDelegate): void

设置用于接收从WebDownloadManager触发的下载进度的委托。

说明

在调用本接口前，若尚未创建Web组件且未执行initializeWebEngine方法完成Web内核初始化，必须先调用initializeWebEngine方法进行初始化，否则接口调用无效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-apis-webview-webdownloaddelegate.md) | 是 | 用来接收下载进度的委托。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
10. download: webview.WebDownloadItem = new webview.WebDownloadItem();
11. failedData: Uint8Array = new Uint8Array();

13. build() {
14. Column() {
15. Button('setDownloadDelegate')
16. .onClick(() => {
17. try {
18. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
19. console.info("will start a download.");
20. // 传入一个下载路径，并开始下载。
21. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
22. })
23. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
24. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
25. this.download = webDownloadItem;
26. })
27. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
28. console.error("download failed guid: " + webDownloadItem.getGuid());
29. // 序列化失败的下载到一个字节数组。
30. this.failedData = webDownloadItem.serialize();
31. })
32. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
33. console.info("download finish guid: " + webDownloadItem.getGuid());
34. })
35. this.controller.setDownloadDelegate(this.delegate);
36. webview.WebDownloadManager.setDownloadDelegate(this.delegate);
37. } catch (error) {
38. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
39. }
40. })
41. Button('startDownload')
42. .onClick(() => {
43. try {
44. this.controller.startDownload('https://www.example.com');
45. } catch (error) {
46. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
47. }
48. })
49. Button('resumeDownload')
50. .onClick(() => {
51. try {
52. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
53. } catch (error) {
54. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
55. }
56. })
57. Button('cancel')
58. .onClick(() => {
59. try {
60. this.download.cancel();
61. } catch (error) {
62. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
63. }
64. })
65. Button('pause')
66. .onClick(() => {
67. try {
68. this.download.pause();
69. } catch (error) {
70. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
71. }
72. })
73. Button('resume')
74. .onClick(() => {
75. try {
76. this.download.resume();
77. } catch (error) {
78. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
79. }
80. })
81. Web({ src: 'www.example.com', controller: this.controller })
82. }
83. }
84. }
```

## resumeDownload11+

PhonePC/2in1TabletTVWearable

static resumeDownload(webDownloadItem: WebDownloadItem): void

恢复一个失败的下载任务。

说明

在调用本接口前，若尚未创建Web组件且未执行initializeWebEngine方法完成Web内核初始化，必须先调用initializeWebEngine方法进行初始化，否则接口调用无效。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDownloadItem | [WebDownloadItem](arkts-apis-webview-webdownloaditem.md) | 是 | 待恢复的下载任务。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100018 | No WebDownloadDelegate has been set yet. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
10. download: webview.WebDownloadItem = new webview.WebDownloadItem();
11. failedData: Uint8Array = new Uint8Array();

13. build() {
14. Column() {
15. Button('setDownloadDelegate')
16. .onClick(() => {
17. try {
18. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
19. console.info("will start a download.");
20. // 传入一个下载路径，并开始下载。
21. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
22. })
23. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
24. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
25. this.download = webDownloadItem;
26. })
27. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
28. console.error("download failed guid: " + webDownloadItem.getGuid());
29. // 序列化失败的下载到一个字节数组。
30. this.failedData = webDownloadItem.serialize();
31. })
32. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
33. console.info("download finish guid: " + webDownloadItem.getGuid());
34. })
35. this.controller.setDownloadDelegate(this.delegate);
36. webview.WebDownloadManager.setDownloadDelegate(this.delegate);
37. } catch (error) {
38. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
39. }
40. })
41. Button('startDownload')
42. .onClick(() => {
43. try {
44. this.controller.startDownload('https://www.example.com');
45. } catch (error) {
46. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
47. }
48. })
49. Button('resumeDownload')
50. .onClick(() => {
51. try {
52. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
53. } catch (error) {
54. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
55. }
56. })
57. Button('cancel')
58. .onClick(() => {
59. try {
60. this.download.cancel();
61. } catch (error) {
62. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
63. }
64. })
65. Button('pause')
66. .onClick(() => {
67. try {
68. this.download.pause();
69. } catch (error) {
70. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
71. }
72. })
73. Button('resume')
74. .onClick(() => {
75. try {
76. this.download.resume();
77. } catch (error) {
78. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
79. }
80. })
81. Web({ src: 'www.example.com', controller: this.controller })
82. }
83. }
84. }
```
