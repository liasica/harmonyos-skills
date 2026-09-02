---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcachesupportedfeatures
title: Class (BackForwardCacheSupportedFeatures)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (BackForwardCacheSupportedFeatures)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:147ae45e730a858633753050a1f271194af0c8d77b4b1175dd17f33ed34c35b2
---

BackForwardCacheSupportedFeatures是ArkWeb框架中用于选择性控制允许使用了特定Web特性的页面可以进入前进后退缓存（BFCache）的配置类。默认情况下，使用同层渲染或视频托管等特性的页面会被阻止进入BFCache，因为浏览器无法安全地保存和恢复这些与系统控件绑定的复杂状态。通过设置该类中的属性，开发者可以显式允许这些特性的页面进入BFCache，但需注意自行维护相关系统控件的生命周期，避免造成资源泄漏。完整示例代码参考[enableBackForwardCache](arkts-apis-webview-webviewcontroller.md#enablebackforwardcache12)。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nativeEmbed12+ | boolean | 否 | 否 | 是否允许使用同层渲染的页面进入前进后退缓存。  如果设置为允许，需要维护为同层渲染元素创建的系统控件的生命周期，避免造成资源泄漏。  true：允许，false：不允许。  默认值：false。 |
| mediaTakeOver12+ | boolean | 否 | 否 | 是否允许使用视频托管的页面进入前进后退缓存。  如果设置为允许，需要维护为视频元素创建的系统控件的生命周期，避免造成资源泄漏。  true：允许，false：不允许。  默认值：false。 |

## constructor12+

constructor()

BackForwardCacheSupportedFeatures的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
