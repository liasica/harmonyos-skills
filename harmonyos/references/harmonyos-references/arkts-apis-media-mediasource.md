---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasource
title: Interface (MediaSource)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (MediaSource)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f281450f7272a4e807be962ad2eb2eae912daebcd45a6a6acbffd577a173e4d6
---

媒体数据信息。来源于[createMediaSourceWithUrl](arkts-apis-media-f.md#mediacreatemediasourcewithurl12)。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { media } from '@kit.MediaKit';
```

## setMimeType12+

PhonePC/2in1TabletTVWearable

setMimeType(mimeType: AVMimeTypes): void

设置媒体MIME类型，以帮助播放器处理扩展的媒体源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | [AVMimeTypes](arkts-apis-media-e.md#avmimetypes12) | 是 | 媒体MIME类型。 |

## setMediaResourceLoaderDelegate18+

PhonePC/2in1TabletTVWearable

setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void

设置MediaSourceLoader，帮助播放器请求媒体数据。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceLoader | [MediaSourceLoader](arkts-apis-media-i.md#mediasourceloader18) | 是 | 应用实现的媒体数据获取接口，方便播放器获取数据。 |

**示例：**

```
1. import { HashMap } from '@kit.ArkTS';
2. import { media } from '@kit.MediaKit';

4. let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
5. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
6. let uuid: number = 1;
7. let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();

9. let sourceOpenCallback: media.SourceOpenCallback = (request: media.MediaSourceLoadingRequest) => {
10. console.info(`Opening resource: ${request.url}`);
11. // 成功打开资源，返回唯一的句柄, 保证uuid和request对应。
12. uuid += 1;
13. requests.set(uuid, request);
14. return uuid;
15. };

17. let sourceReadCallback: media.SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => {
18. console.info(`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}`);
19. // 判断uuid是否合法、存储read请求，不要在read请求阻塞去推送数据和头信息。
20. };

22. let sourceCloseCallback: media.SourceCloseCallback = (uuid: number) => {
23. console.info(`Closing resource with handle ${uuid}`);
24. // 清除当前uuid相关资源。
25. requests.remove(uuid);
26. };

28. // 应用按需实现。
29. let resourceLoader: media.MediaSourceLoader = {
30. open: sourceOpenCallback,
31. read: sourceReadCallback,
32. close: sourceCloseCallback
33. };

35. mediaSource.setMediaResourceLoaderDelegate(resourceLoader);
```

## enableOfflineCache23+

PhonePC/2in1TabletTVWearable

enableOfflineCache(enable: boolean): void

是否在视频播放期间启用离线缓存。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否在视频播放期间启用离线缓存。true表示启用，false表示不启用。 |
