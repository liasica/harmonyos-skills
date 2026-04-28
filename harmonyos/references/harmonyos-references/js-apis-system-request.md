---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-request
title: @system.request (上传下载)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @system.request (上传下载)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccca7e9b194853b74822c04dba24c440e6dd1b70b331954bb86347ad31e68a30
---

system.request部件主要给应用提供上传下载文件的基础能力。

说明

* 从API Version 9开始所有接口不再维护，推荐使用新接口[@ohos.request](js-apis-request.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Request } from '@kit.BasicServicesKit';
```

## request.upload(deprecated)

PhonePC/2in1TabletTVWearable

upload(options: UploadRequestOptions): void

上传文件，无返回值。

**系统能力**：SystemCapability.MiscServices.Upload

说明

从API version 3 开始支持，从API version 9 开始废弃，建议使用[request.uploadFile](js-apis-request.md#requestuploadfile9)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UploadRequestOptions](js-apis-system-request.md#uploadrequestoptionsdeprecated) | 是 | 上传的配置信息。 |

**示例：**

```
1. import  { Request, UploadRequestOptions, UploadResponse } from '@kit.BasicServicesKit';

3. let uploadRequestOptions: UploadRequestOptions = {
4. url: 'http://www.path.com',
5. method: 'POST',
6. files: [{
7. filename: "test",
8. name: "test",
9. uri: "internal://cache/test.jpg",
10. type: "jpg"
11. }],
12. data: [{
13. name: "name123",
14. value: "123"
15. }],
16. success: (data: UploadResponse) => {
17. console.info('Succeeded in uploading, code:' + JSON.stringify(data.code));
18. },
19. fail: (data: string, code: number) => {
20. console.info('Failed to upload, data: ' + data + 'code: ' + code);
21. },
22. complete: () => {
23. console.info('Upload complete');
24. }
25. }

27. try {
28. Request.upload(uploadRequestOptions);
29. console.info('Start Upload');
30. } catch (err) {
31. console.error('Failed to upload, err:' + err);
32. }
```

## UploadRequestOptions(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Upload

说明

从API version 3 开始支持，从API version 9 开始废弃，建议使用[UploadConfig](js-apis-request.md#uploadconfig)替代。

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 上传服务器地址。 |
| data | Array<[RequestData](js-apis-system-request.md#requestdatadeprecated)> | 否 | 请求的表单数据。 |
| files | Array<[RequestFile](js-apis-system-request.md#requestfiledeprecated)> | 是 | 待上传文件列表。请使用multipart/form-data进行提交。 |
| header | Object | 否 | 请求头。 |
| method | string | 否 | 请求方法：POST、PUT。缺省POST。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**success参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [UploadResponse](js-apis-system-request.md#uploadresponsedeprecated) | 是 | 上传任务成功返回信息。 |

**fail参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | any | 是 | 上传任务失败返回header信息。 |
| code | number | 是 | 上传任务失败返回HTTP状态码。 |

## UploadResponse(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Upload

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 服务器返回的HTTP状态码。 |
| data | string | 是 | 服务器返回的内容。根据返回头内容中的type决定该值的类型。 |
| headers | Object | 是 | 服务器返回的返回头内容。 |

## RequestFile(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Upload

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filename | string | 否 | multipart 提交时，请求头中的文件名。 |
| name | string | 否 | multipart 提交时，表单项目的名称，缺省为file。 |
| uri | string | 是 | 文件的本地存储路径。 |
| type | string | 否 | 文件的内容类型，默认根据文件名或路径的后缀获取。 |

## RequestData(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Upload

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 表示form 元素的名称。 |
| value | string | 是 | 表示form 元素的值。 |

## request.download(deprecated)

PhonePC/2in1TabletTVWearable

download(options: DownloadRequestOptions): void

下载文件，无返回值。

**系统能力**：SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DownloadRequestOptions](js-apis-system-request.md#downloadrequestoptionsdeprecated) | 是 | 下载的配置信息。 |

**示例：**

```
1. import  { Request, DownloadResponse, DownloadRequestOptions } from '@kit.BasicServicesKit';

3. let downloadRequestOptions: DownloadRequestOptions = {
4. url: 'http://www.path.com',
5. filename: 'requestSystemTest',
6. header: "",
7. description: 'this is requestSystem download response',
8. success: (data: DownloadResponse) => {
9. console.info('Succeeded in downloading, code:' + JSON.stringify(data));
10. },
11. fail: (data: string, code: number) => {
12. console.info('Failed to download, data: ' + data + 'code: ' + code);
13. },
14. complete: () => {
15. console.info('Download complete');
16. }
17. }

19. try {
20. Request.download(downloadRequestOptions);
21. console.info('Start download');
22. } catch(err) {
23. console.error('Failed to download, err:' + err);
24. }
```

## DownloadRequestOptions(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Download

说明

从API version 3 开始支持，从API version 9 开始废弃，建议使用[UploadConfig](js-apis-request.md#uploadconfig)替代。

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 资源地址。 |
| filename | string | 否 | 本次下载文件的名称。默认从本次请求或资源地址中获取。 |
| header | Object | 否 | 请求头。 |
| description | string | 否 | 资源地址的下载描述，默认为文件名称。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**success参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [DownloadResponse](js-apis-system-request.md#downloadresponsedeprecated) | 是 | 下载任务成功返回信息。 |

**fail参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | any | 是 | 下载任务失败返回header信息。 |
| code | number | 是 | 下载任务失败返回HTTP状态码。 |

## DownloadResponse(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Download

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 表示下载的token，获取下载状态的依据。 |

## request.onDownloadComplete(deprecated)

PhonePC/2in1TabletTVWearable

onDownloadComplete(options: OnDownloadCompleteOptions): void

获取下载任务状态，无返回值。

**系统能力**：SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [OnDownloadCompleteOptions](js-apis-system-request.md#ondownloadcompleteoptionsdeprecated) | 是 | 监听下载任务的配置信息。 |

**示例：**

```
1. import  { Request, OnDownloadCompleteOptions, OnDownloadCompleteResponse } from '@kit.BasicServicesKit';

3. let onDownloadCompleteOptions: OnDownloadCompleteOptions = {
4. token: 'token-index',
5. success: (data: OnDownloadCompleteResponse) => {
6. console.info('Succeeded in downloading, uri:' + JSON.stringify(data.uri));
7. },
8. fail: (data: string, code: number) => {
9. console.info('Failed to download, data: ' + data + 'code: ' + code);
10. },
11. complete: () => {
12. console.info('Download complete');
13. }
14. }

16. Request.onDownloadComplete(onDownloadCompleteOptions);
```

## OnDownloadCompleteOptions(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Download

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | download 接口返回的结果 token。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**success参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [OnDownloadCompleteResponse](js-apis-system-request.md#ondownloadcompleteresponsedeprecated) | 是 | 下载任务成功返回信息。 |

**fail参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | any | 是 | 下载任务失败返回header信息。 |
| code | number | 是 | 下载任务失败返回HTTP状态码。 |

## OnDownloadCompleteResponse(deprecated)

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.MiscServices.Download

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示下载文件的uri。 |
