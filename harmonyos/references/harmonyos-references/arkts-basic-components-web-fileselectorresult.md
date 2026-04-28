---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorresult
title: Class (FileSelectorResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (FileSelectorResult)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:39f0979254661f09201346510aedce7e1a925ca8ff8add62abebd46065b88f79
---

通知Web组件的文件选择结果。示例代码参考[onShowFileSelector事件](arkts-basic-components-web-events.md#onshowfileselector9)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

FileSelectorResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## handleFileList9+

PhonePC/2in1TabletTVWearable

handleFileList(fileList: Array<string>): void

通知Web组件进行文件选择操作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileList | Array<string> | 是 | 需要进行操作的文件列表。 |
