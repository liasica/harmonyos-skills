---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyrule
title: Class (ProxyRule)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (ProxyRule)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5028b17c9237af6e0b1864249322bdc51aee3684e665df67123a1e484f1b1041
---

[insertProxyRule](arkts-apis-webview-proxyconfig.md#insertproxyrule15)中使用的代理规则。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 15开始支持。
* 示例效果请以真机运行为准。

## getSchemeFilter15+

PhonePC/2in1TabletTVWearable

getSchemeFilter(): ProxySchemeFilter

获取代理规则中的ProxySchemeFilter信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProxySchemeFilter](arkts-apis-webview-e.md#proxyschemefilter15) | 代理规则中的ProxySchemeFilter信息。 |

**示例：**

完整示例代码参考[removeProxyOverride](arkts-apis-webview-proxycontroller.md#removeproxyoverride15)。

## getUrl15+

PhonePC/2in1TabletTVWearable

getUrl(): string

获取代理规则中的代理的Url信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 代理规则中的代理的Url信息。 |

**示例：**

完整示例代码参考[removeProxyOverride](arkts-apis-webview-proxycontroller.md#removeproxyoverride15)。
