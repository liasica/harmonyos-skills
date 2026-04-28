---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery
title: Class (MediaQuery)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (MediaQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2e8430ead6c4bdfd73ba9269d9db4215acab1be481883265f0465b6f31eab41f
---

提供根据不同媒体类型定义不同的样式。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getMediaQuery()](arkts-apis-uicontext-uicontext.md#getmediaquery)方法获取到MediaQuery对象，再通过该对象调用对应方法。

## matchMediaSync

PhonePC/2in1TabletTVWearable

matchMediaSync(condition: string): mediaQuery.MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | string | 是 | 媒体事件的匹配条件，具体可参考[媒体查询语法规则](../harmonyos-guides/arkts-layout-development-media-query.md#语法规则)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mediaQuery.MediaQueryListener](js-apis-mediaquery.md#mediaquerylistener) | 媒体事件监听句柄，用于注册和去注册监听回调。 |

**示例：**

完整示例请参考[mediaquery示例](js-apis-mediaquery.md#示例)。
