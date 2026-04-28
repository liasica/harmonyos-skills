---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaditem
title: Class (WebDownloadItem)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebDownloadItem)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:06+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:86f3858908201997b6618569c8d8f33172880d74606626633649356c06c16cc9
---

表示下载任务，您可以使用此对象来操作相应的下载任务。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 11开始支持。
* 示例效果请以真机运行为准。
* 在下载过程中，下载的进度会通过WebDownloadDelegate通知给使用者，使用者可以通过参数WebDownloadItem来操作下载任务。
* 当前WebDownloadItem支持的下载文件名最长长度为255字节。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## getGuid11+

PhonePC/2in1TabletTVWearable

getGuid(): string

获取下载任务的唯一ID。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 下载任务的唯一ID。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update guid: " + webDownloadItem.getGuid());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getCurrentSpeed11+

PhonePC/2in1TabletTVWearable

getCurrentSpeed(): number

获取下载的速度，单位：字节每秒。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 下载的速度（字节每秒）。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update current speed: " + webDownloadItem.getCurrentSpeed());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getPercentComplete11+

PhonePC/2in1TabletTVWearable

getPercentComplete(): number

获取下载的进度，100代表下载完成。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 下载完成的进度，100代表下载完成，-1代表进度未知。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getTotalBytes11+

PhonePC/2in1TabletTVWearable

getTotalBytes(): number

获取待下载文件的总长度。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 待下载文件的总长度，-1代表总大小未知。单位：字节。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update total bytes: " + webDownloadItem.getTotalBytes());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getState11+

PhonePC/2in1TabletTVWearable

getState(): WebDownloadState

获取下载的状态。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebDownloadState](arkts-apis-webview-e.md#webdownloadstate11) | 下载的状态。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update download state: " + webDownloadItem.getState());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getLastErrorCode11+

PhonePC/2in1TabletTVWearable

getLastErrorCode(): WebDownloadErrorCode

获取下载的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebDownloadErrorCode](arkts-apis-webview-e.md#webdownloaderrorcode11) | 下载发生错误的时候的错误码。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. console.info("download error code: " + webDownloadItem.getLastErrorCode());
27. })
28. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
29. console.info("download finish guid: " + webDownloadItem.getGuid());
30. })
31. this.controller.setDownloadDelegate(this.delegate);
32. } catch (error) {
33. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
34. }
35. })
36. Button('startDownload')
37. .onClick(() => {
38. try {
39. this.controller.startDownload('https://www.example.com');
40. } catch (error) {
41. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
42. }
43. })
44. Web({ src: 'www.example.com', controller: this.controller })
45. }
46. }
47. }
```

## getMethod11+

PhonePC/2in1TabletTVWearable

getMethod(): string

获取下载任务的请求方式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 下载的请求方式。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download， method:" + webDownloadItem.getMethod());
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getMimeType11+

PhonePC/2in1TabletTVWearable

getMimeType(): string

获取下载的媒体类型（例如，一个声音文件可能被标记为 audio/ogg ，一个图像文件可能是 image/png）。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 下载的媒体类型（例如，一个声音文件可能被标记为 audio/ogg ，一个图像文件可能是 image/png）。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download， mime type:" + webDownloadItem.getMimeType());
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getUrl11+

PhonePC/2in1TabletTVWearable

getUrl(): string

获取下载的请求地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 下载的请求地址。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download, url:" + webDownloadItem.getUrl());
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getSuggestedFileName11+

PhonePC/2in1TabletTVWearable

getSuggestedFileName(): string

获取下载的建议文件名。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 下载的建议文件名。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download, suggest name:" + webDownloadItem.getSuggestedFileName());
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. })
30. this.controller.setDownloadDelegate(this.delegate);
31. } catch (error) {
32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
33. }
34. })
35. Button('startDownload')
36. .onClick(() => {
37. try {
38. this.controller.startDownload('https://www.example.com');
39. } catch (error) {
40. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
41. }
42. })
43. Web({ src: 'www.example.com', controller: this.controller })
44. }
45. }
46. }
```

## getReceivedBytes11+

PhonePC/2in1TabletTVWearable

getReceivedBytes(): number

获取已经接收的字节数。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 已经接收的字节数。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. console.info("download update received bytes: " + webDownloadItem.getReceivedBytes());
24. })
25. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
26. console.error("download failed guid: " + webDownloadItem.getGuid());
27. })
28. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
29. console.info("download finish guid: " + webDownloadItem.getGuid());
30. })
31. this.controller.setDownloadDelegate(this.delegate);
32. } catch (error) {
33. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
34. }
35. })
36. Button('startDownload')
37. .onClick(() => {
38. try {
39. this.controller.startDownload('https://www.example.com');
40. } catch (error) {
41. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
42. }
43. })
44. Web({ src: 'www.example.com', controller: this.controller })
45. }
46. }
47. }
```

## getFullPath11+

PhonePC/2in1TabletTVWearable

getFullPath(): string

获取下载文件在磁盘上的全路径。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 下载文件在磁盘上的全路径。 |

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

11. build() {
12. Column() {
13. Button('setDownloadDelegate')
14. .onClick(() => {
15. try {
16. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
17. console.info("will start a download.");
18. // 传入一个下载路径，并开始下载。
19. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
20. })
21. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
22. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
23. })
24. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
25. console.error("download failed guid: " + webDownloadItem.getGuid());
26. })
27. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
28. console.info("download finish guid: " + webDownloadItem.getGuid());
29. console.info("download finish full path: " + webDownloadItem.getFullPath());
30. })
31. this.controller.setDownloadDelegate(this.delegate);
32. } catch (error) {
33. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
34. }
35. })
36. Button('startDownload')
37. .onClick(() => {
38. try {
39. this.controller.startDownload('https://www.example.com');
40. } catch (error) {
41. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
42. }
43. })
44. Web({ src: 'www.example.com', controller: this.controller })
45. }
46. }
47. }
```

## serialize11+

PhonePC/2in1TabletTVWearable

serialize(): Uint8Array

将失败的下载序列化到一个字节数组。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 失败的下载序列化后的字节数组。 |

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
10. failedData: Uint8Array = new Uint8Array();

12. build() {
13. Column() {
14. Button('setDownloadDelegate')
15. .onClick(() => {
16. try {
17. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
18. console.info("will start a download.");
19. // 传入一个下载路径，并开始下载。
20. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
21. })
22. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
23. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
24. })
25. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
26. console.error("download failed guid: " + webDownloadItem.getGuid());
27. // 序列化失败的下载到一个字节数组。
28. this.failedData = webDownloadItem.serialize();
29. })
30. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
31. console.info("download finish guid: " + webDownloadItem.getGuid());
32. })
33. this.controller.setDownloadDelegate(this.delegate);
34. } catch (error) {
35. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
36. }
37. })
38. Button('startDownload')
39. .onClick(() => {
40. try {
41. this.controller.startDownload('https://www.example.com');
42. } catch (error) {
43. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })
46. Web({ src: 'www.example.com', controller: this.controller })
47. }
48. }
49. }
```

## deserialize11+

PhonePC/2in1TabletTVWearable

static deserialize(serializedData: Uint8Array): WebDownloadItem

将序列化后的字节数组反序列化为一个WebDownloadItem对象。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serializedData | Uint8Array | 是 | 序列化后的下载。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WebDownloadItem | 从字节数组反序列化为一个WebDownloadItem对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

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
10. failedData: Uint8Array = new Uint8Array();

12. build() {
13. Column() {
14. Button('setDownloadDelegate')
15. .onClick(() => {
16. try {
17. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
18. console.info("will start a download.");
19. // 传入一个下载路径，并开始下载。
20. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
21. })
22. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
23. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
24. })
25. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
26. console.error("download failed guid: " + webDownloadItem.getGuid());
27. // 序列化失败的下载到一个字节数组。
28. this.failedData = webDownloadItem.serialize();
29. })
30. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
31. console.info("download finish guid: " + webDownloadItem.getGuid());
32. })
33. this.controller.setDownloadDelegate(this.delegate);
34. } catch (error) {
35. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
36. }
37. })
38. Button('startDownload')
39. .onClick(() => {
40. try {
41. this.controller.startDownload('https://www.example.com');
42. } catch (error) {
43. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })
46. Button('resumeDownload')
47. .onClick(() => {
48. try {
49. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
50. } catch (error) {
51. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
52. }
53. })
54. Web({ src: 'www.example.com', controller: this.controller })
55. }
56. }
57. }
```

## start11+

PhonePC/2in1TabletTVWearable

start(downloadPath: string): void

开始下载到指定目录，参数为下载文件的磁盘存储路径（包含文件名）。

说明

该接口应在WebDownloadDelegate的onBeforeDownload回调中使用。若在WebDownloadDelegate的onBeforeDownload中未调用start('xxx')，则下载任务将保持在PENDING状态。处于PENDING状态的下载会将文件下载到临时目录，临时文件会在WebDownloadItem.start指定目标路径后被重命名为目标路径，未下载完成的部分会在WebDownloadItem.start指定目标路径后直接下载到目标路径。如果在调用WebDownloadItem.start之前不希望下载到临时文件路径，可以先通过WebDownloadItem.cancel取消当前下载任务，随后通过WebDownloadManager.resumeDownload恢复被取消的下载任务。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| downloadPath | string | 是 | 下载文件的路径（包含文件名），路径长度与文件管理中长度一致，最长255字节。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

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
10. failedData: Uint8Array = new Uint8Array();

12. build() {
13. Column() {
14. Button('setDownloadDelegate')
15. .onClick(() => {
16. try {
17. this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
18. console.info("will start a download.");
19. // 传入一个下载路径，并开始下载。
20. webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
21. })
22. this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
23. console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
24. })
25. this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
26. console.error("download failed guid: " + webDownloadItem.getGuid());
27. // 序列化失败的下载到一个字节数组。
28. this.failedData = webDownloadItem.serialize();
29. })
30. this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
31. console.info("download finish guid: " + webDownloadItem.getGuid());
32. })
33. this.controller.setDownloadDelegate(this.delegate);
34. } catch (error) {
35. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
36. }
37. })
38. Button('startDownload')
39. .onClick(() => {
40. try {
41. this.controller.startDownload('https://www.example.com');
42. } catch (error) {
43. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })
46. Button('resumeDownload')
47. .onClick(() => {
48. try {
49. webview.WebDownloadManager.resumeDownload(webview.WebDownloadItem.deserialize(this.failedData));
50. } catch (error) {
51. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
52. }
53. })
54. Web({ src: 'www.example.com', controller: this.controller })
55. }
56. }
57. }
```

## cancel11+

PhonePC/2in1TabletTVWearable

cancel(): void

取消一个正在下载的下载任务。

**系统能力：** SystemCapability.Web.Webview.Core

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
64. Web({ src: 'www.example.com', controller: this.controller })
65. }
66. }
67. }
```

## pause11+

PhonePC/2in1TabletTVWearable

pause(): void

暂停一个正在下载的下载任务。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100019 | The download task is not started yet. |

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
72. Web({ src: 'www.example.com', controller: this.controller })
73. }
74. }
75. }
```

## resume11+

PhonePC/2in1TabletTVWearable

resume(): void

恢复一个暂停的下载任务。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100016 | The download task is not paused. |

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
