---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaddelegate
title: Class (WebDownloadDelegate)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebDownloadDelegate)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:05+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:7e6887ffedf661c783318ef34902ed1388ff054d641641e97b6225b716e64fba
---

下载任务的状态会通过该类的回调接口通知给用户。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 11开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## onBeforeDownload11+

PhonePC/2in1TabletTVWearable

onBeforeDownload(callback: Callback<WebDownloadItem>): void

下载开始前通知给用户，用户需要在此接口中调用WebDownloadItem.start("xxx")并提供下载路径，否则下载会一直处于PENDING状态。

说明

处于PENDING状态的下载任务会首先将文件保存至临时目录。在调用WebDownloadItem.start并指定目标路径后，临时文件将被重命名为目标文件名，未完成下载的部分会在调用WebDownloadItem.start并指定目标路径后直接下载到目标路径。若希望避免在调用WebDownloadItem.start前生成临时文件，可先通过WebDownloadItem.cancel来取消当前的下载任务，之后再使用WebDownloadManager.resumeDownload来恢复被取消的下载任务。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[WebDownloadItem](arkts-apis-webview-webdownloaditem.md)> | 是 | 触发下载的回调。 |

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
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Button('startDownload')
41. .onClick(() => {
42. try {
43. this.controller.startDownload('https://www.example.com');
44. } catch (error) {
45. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
46. }
47. })
48. Button('resumeDownload')
49. .onClick(() => {
50. try {
51. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
52. } catch (error) {
53. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
54. }
55. })
56. Button('cancel')
57. .onClick(() => {
58. try {
59. this.download.cancel();
60. } catch (error) {
61. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
62. }
63. })
64. Button('pause')
65. .onClick(() => {
66. try {
67. this.download.pause();
68. } catch (error) {
69. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
70. }
71. })
72. Button('resume')
73. .onClick(() => {
74. try {
75. this.download.resume();
76. } catch (error) {
77. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
78. }
79. })
80. Web({ src: 'www.example.com', controller: this.controller })
81. }
82. }
83. }
```

## onDownloadUpdated11+

PhonePC/2in1TabletTVWearable

onDownloadUpdated(callback: Callback<WebDownloadItem>): void

下载过程中的回调，通过该回调的参数可以了解下载进度等信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[WebDownloadItem](arkts-apis-webview-webdownloaditem.md)> | 是 | 下载更新的回调。 |

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
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Button('startDownload')
41. .onClick(() => {
42. try {
43. this.controller.startDownload('https://www.example.com');
44. } catch (error) {
45. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
46. }
47. })
48. Button('resumeDownload')
49. .onClick(() => {
50. try {
51. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
52. } catch (error) {
53. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
54. }
55. })
56. Button('cancel')
57. .onClick(() => {
58. try {
59. this.download.cancel();
60. } catch (error) {
61. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
62. }
63. })
64. Button('pause')
65. .onClick(() => {
66. try {
67. this.download.pause();
68. } catch (error) {
69. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
70. }
71. })
72. Button('resume')
73. .onClick(() => {
74. try {
75. this.download.resume();
76. } catch (error) {
77. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
78. }
79. })
80. Web({ src: 'www.example.com', controller: this.controller })
81. }
82. }
83. }
```

## onDownloadFinish11+

PhonePC/2in1TabletTVWearable

onDownloadFinish(callback: Callback<WebDownloadItem>): void

下载完成的通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[WebDownloadItem](arkts-apis-webview-webdownloaditem.md)> | 是 | 下载完成的回调。 |

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
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Button('startDownload')
41. .onClick(() => {
42. try {
43. this.controller.startDownload('https://www.example.com');
44. } catch (error) {
45. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
46. }
47. })
48. Button('resumeDownload')
49. .onClick(() => {
50. try {
51. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
52. } catch (error) {
53. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
54. }
55. })
56. Button('cancel')
57. .onClick(() => {
58. try {
59. this.download.cancel();
60. } catch (error) {
61. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
62. }
63. })
64. Button('pause')
65. .onClick(() => {
66. try {
67. this.download.pause();
68. } catch (error) {
69. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
70. }
71. })
72. Button('resume')
73. .onClick(() => {
74. try {
75. this.download.resume();
76. } catch (error) {
77. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
78. }
79. })
80. Web({ src: 'www.example.com', controller: this.controller })
81. }
82. }
83. }
```

## onDownloadFailed11+

PhonePC/2in1TabletTVWearable

onDownloadFailed(callback: Callback<WebDownloadItem>): void

下载失败的通知。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[WebDownloadItem](arkts-apis-webview-webdownloaditem.md)> | 是 | 下载失败的回调。 |

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
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Button('startDownload')
41. .onClick(() => {
42. try {
43. this.controller.startDownload('https://www.example.com');
44. } catch (error) {
45. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
46. }
47. })
48. Button('resumeDownload')
49. .onClick(() => {
50. try {
51. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
52. } catch (error) {
53. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
54. }
55. })
56. Button('cancel')
57. .onClick(() => {
58. try {
59. this.download.cancel();
60. } catch (error) {
61. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
62. }
63. })
64. Button('pause')
65. .onClick(() => {
66. try {
67. this.download.pause();
68. } catch (error) {
69. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
70. }
71. })
72. Button('resume')
73. .onClick(() => {
74. try {
75. this.download.resume();
76. } catch (error) {
77. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
78. }
79. })
80. Web({ src: 'www.example.com', controller: this.controller })
81. }
82. }
83. }
```
