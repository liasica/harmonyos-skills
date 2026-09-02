---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcacheoptions
title: Class (BackForwardCacheOptions)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (BackForwardCacheOptions)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5b9f382992d1300c1686baf25c4abcfeab573e17e2647f3716c4413aaccf870e
---

BackForwardCacheOptions是ArkWeb框架中用于配置Web组件前进后退缓存（BFCache）行为的参数类。BFCache是一种页面缓存机制，当用户在浏览历史中前进或后退时，可将页面完整快照（包括JavaScript状态）缓存起来，实现瞬时加载效果，显著提升用户体验。通过BackForwardCacheOptions，开发者可以控制每个Web组件允许缓存的最大页面个数以及页面在缓存中的最长停留时间。

**说明** 

* 本模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

**系统能力：** SystemCapability.Web.Webview.Core

## 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size12+ | number | 否 | 否 | 设置每个Web组件允许缓存的最大页面个数。  默认为1，最大可设置为50。  设置为0或负数时，前进后退缓存功能不生效。  Web组件会根据内存压力对缓存进行回收。 |
| timeToLive12+ | number | 否 | 否 | 设置每个Web组件允许页面在前进后退缓存中停留的时间。  设置为0或负数时，前进后退缓存功能不生效。  默认值：600。  单位：秒。 |

## constructor12+

constructor()

BackForwardCacheOptions的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
