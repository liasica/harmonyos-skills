---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata
title: CommonEventData
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > commonEvent > CommonEventData
category: harmonyos-references
scraped_at: 2026-09-02T15:02:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d467e48ba889e7ea2b3905de5f8fa6eca2f5b05af008ffd772bc0a51b47250ce
---

表示公共事件的数据。CommonEventData用于在公共事件订阅场景中承载订阅者接收到的公共事件数据，包含事件名称、发布者包名、code数据、data数据及附加参数等信息，适用于应用订阅并处理公共事件、解析事件携带数据的场景。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | string | 否 | 否 | 表示当前接收的公共事件名称。 |
| bundleName | string | 否 | 是 | 表示发布公共事件的应用包名，默认为空字符串。 |
| code | number | 否 | 是 | 表示订阅者接收到的公共事件数据。该字段取值与发布者使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish-1)发布公共事件时，通过[CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md)中的code字段传递的数据一致。取值范围[-2147483648, 2147483647]，默认值为0。 |
| data | string | 否 | 是 | 表示订阅者接收到的公共事件数据，数据大小不超过64KB。该字段取值与发布者使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish-1)发布公共事件时，通过[CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md)中的data字段传递的数据一致。 |
| parameters | {[key: string]: any} | 否 | 是 | 表示订阅者接收到的公共事件的附加信息。该字段取值与发布者使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish-1)发布公共事件时，通过[CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md)中的parameters字段传递的数据一致。 |
