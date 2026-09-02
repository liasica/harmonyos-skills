---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyrule
title: Class (ProxyRule)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (ProxyRule)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9d26f8707d6fac4d4a13edb6cdb8ca83ee1a33edd71b653b66b5fe80adac234d
---

ProxyRule是ArkWeb框架中代理规则只读信息的类，通过[getProxyRules](arkts-apis-webview-proxyconfig.md#getproxyrules15)方法获取。当开发者通过ProxyConfig配置了代理规则后，可通过getProxyRules获取已配置的规则列表，每条规则对应一个ProxyRule对象，用于查询规则的详细信息。

ProxyRule提供两个方法：getSchemeFilter用于获取该代理规则对应的协议过滤器（如MATCH\_ALL\_SCHEMES、MATCH\_HTTP、MATCH\_HTTPS等），getUrl用于获取该代理规则中指定的代理服务器URL信息。ProxyRule对象为只读，由系统在配置代理规则时创建，应用只能查询其内容而不能修改。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 15开始支持。
* 示例效果请以真机运行为准。

## getSchemeFilter15+

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

getUrl(): string

获取代理规则中代理的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 代理规则中代理的URL信息。 |

**示例：**

完整示例代码参考[removeProxyOverride](arkts-apis-webview-proxycontroller.md#removeproxyoverride15)。
