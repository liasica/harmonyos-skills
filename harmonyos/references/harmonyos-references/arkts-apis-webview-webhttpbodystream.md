---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream
title: Class (WebHttpBodyStream)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebHttpBodyStream)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:08+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:9d6c519a93a3b541e5f05d7061e54472283ebd069fcfea8392e23ae21009660b
---

POST、PUT请求的数据体，支持BYTES、FILE、BLOB、CHUNKED类型的数据。注意本类中其他接口需要在[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)成功后才能调用。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## initialize12+

PhonePC/2in1TabletTVWearable

initialize(): Promise<void>

初始化WebHttpBodyStream。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取WebHttpBodyStream是否初始化成功。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100022 | Failed to initialize the HTTP body stream. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { buffer } from '@kit.ArkTS';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();
10. schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();
11. htmlData: string = "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>";

13. build() {
14. Column() {
15. Button('postUrl')
16. .onClick(() => {
17. try {
18. let postData = buffer.from(this.htmlData);
19. this.controller.postUrl('https://www.example.com', postData.buffer);
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'https://www.example.com', controller: this.controller })
25. .onControllerAttached(() => {
26. try {
27. this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler) => {
28. console.info("[schemeHandler] onRequestStart");
29. try {
30. let stream = request.getHttpBodyStream();
31. if (stream) {
32. stream.initialize().then(() => {
33. if (!stream) {
34. return;
35. }
36. console.info("[schemeHandler] onRequestStart postDataStream size:" + stream.getSize());
37. console.info("[schemeHandler] onRequestStart postDataStream position:" + stream.getPosition());
38. console.info("[schemeHandler] onRequestStart postDataStream isChunked:" + stream.isChunked());
39. console.info("[schemeHandler] onRequestStart postDataStream isEof:" + stream.isEof());
40. console.info("[schemeHandler] onRequestStart postDataStream isInMemory:" + stream.isInMemory());
41. stream.read(stream.getSize()).then((buffer) => {
42. if (!stream) {
43. return;
44. }
45. console.info("[schemeHandler] onRequestStart postDataStream readlength:" + buffer.byteLength);
46. console.info("[schemeHandler] onRequestStart postDataStream isEof:" + stream.isEof());
47. console.info("[schemeHandler] onRequestStart postDataStream position:" + stream.getPosition());
48. }).catch((error: BusinessError) => {
49. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
50. })
51. }).catch((error: BusinessError) => {
52. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
53. })
54. } else {
55. console.info("[schemeHandler] onRequestStart has no http body stream");
56. }
57. } catch (error) {
58. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
59. }

61. return false;
62. })

64. this.schemeHandler.onRequestStop((request: webview.WebSchemeHandlerRequest) => {
65. console.info("[schemeHandler] onRequestStop");
66. });

68. this.controller.setWebSchemeHandler('https', this.schemeHandler);
69. } catch (error) {
70. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
71. }
72. })
73. .javaScriptAccess(true)
74. .domStorageAccess(true)
75. }
76. }
77. }
```

## read12+

PhonePC/2in1TabletTVWearable

read(size: number): Promise<ArrayBuffer>

读取WebHttpBodyStream中的数据。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 读取WebHttpBodyStream中的字节数。单位：字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise实例，用于获取WebHttpBodyStream中读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

完整示例代码参考[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)。

## getSize12+

PhonePC/2in1TabletTVWearable

getSize(): number

获取WebHttpBodyStream中的数据大小，分块传输时总是返回零。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取WebHttpBodyStream中的数据大小。单位：字节。 |

**示例：**

完整示例代码参考[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)。

## getPosition12+

PhonePC/2in1TabletTVWearable

getPosition(): number

读取WebHttpBodyStream中当前的读取位置。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | WebHttpBodyStream中当前的读取位置。单位：字节。 |

**示例：**

完整示例代码参考[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)。

## isChunked12+

PhonePC/2in1TabletTVWearable

isChunked(): boolean

WebHttpBodyStream是否采用分块传输。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream是否采用分块传输，如果采用分块传输则返回true，否则返回false。 |

**示例：**

完整示例代码参考[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)。

## isEof12+

PhonePC/2in1TabletTVWearable

isEof(): boolean

判断WebHttpBodyStream中的所有数据是否都已被读取。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream中的所有数据是否都已被读取。  如果所有数据都已被读取，则返回true。对于分块传输类型的WebHttpBodyStream，在第一次读取尝试之前返回false。 |

**示例：**

完整示例代码参考[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)。

## isInMemory12+

PhonePC/2in1TabletTVWearable

isInMemory(): boolean

判断WebHttpBodyStream中的上传数据是否在内存中。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream中的上传数据是否在内存中。  如果WebHttpBodyStream中的上传数据完全在内存中，并且所有读取请求都将同步成功，则返回true。对于分块传输类型的数据，预期返回false。 |

**示例：**

完整示例代码参考[initialize](arkts-apis-webview-webhttpbodystream.md#initialize12)。
