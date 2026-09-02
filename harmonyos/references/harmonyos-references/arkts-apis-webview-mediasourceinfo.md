---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo
title: Class (MediaSourceInfo)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (MediaSourceInfo)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa9aa2a0424f36b51ac7927af0f2d62f1f4a095ee813280f3cf50200d4e31c29
---

MediaSourceInfo 是表示媒体源信息的数据类。在 Web 媒体播放场景中，MediaSourceInfo 类封装了媒体源的基本信息，帮助应用了解媒体源的类型、地址和格式，应用根据这些信息创建自定义播放器并开始播放。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type12+ | [SourceType](arkts-apis-webview-e.md#sourcetype12) | 否 | 否 | 媒体源的类型。 |
| source12+ | string | 否 | 否 | 媒体源地址。 |
| format12+ | string | 否 | 否 | 媒体源格式，可能为空，需要开发者自行判断格式。 |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

const mediaInfo: webview.MediaSourceInfo = {
  type: webview.SourceType.URL,
  source: 'https://example.com/video.mp4',
  format: 'mp4'
};
```
