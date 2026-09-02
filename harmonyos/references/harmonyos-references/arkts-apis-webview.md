---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > 模块描述
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:35db4468be5a575e6868009ed131f0fcf81770c52dd9e63ef19ea1e50bb2f5f6
---

WebView模块是HarmonyOS ArkWeb框架提供的Web控制能力模块，用于在应用侧对Web组件的行为进行编程式控制。该模块不涉及网页的显示渲染（显示能力由Web组件提供），而是聚焦于Web组件运行过程中的控制逻辑，包括页面加载与导航、JavaScript脚本执行与双向消息通信、Cookie与存储管理、下载任务管理、网络请求拦截与自定义响应、代理配置、地理位置权限管理、广告过滤、前进后退缓存、媒体播放托管、PDF生成等能力。

开发者在使用Web组件展示网页内容时，如需在应用侧对网页行为进行干预、监听或扩展（例如：向网页发送消息、拦截特定Scheme请求并返回本地资源、管理下载流程、配置代理、控制缓存策略等），应通过本模块提供的Controller和各类Manager/Delegate来实现。

网页显示的能力请参考[组件描述](arkts-basic-components-web.md)。

元服务中使用ArkWeb的说明，请参考[Web组件概述](../atomic-guides/atomicserviceweb-guidelines.md)。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。
* 静态方法必须在用户界面（UI）线程上使用。

该模块提供以下Web控制相关的常用功能：

* [AdsBlockManager](arkts-apis-webview-adsblockmanager.md)：广告过滤配置。
* [AIPageCommand](arkts-apis-webview-aipagecommand.md)：[executeAIPageCommand](arkts-apis-webview-webviewcontroller.md#executeaipagecommand)支持的JSON命令协议。
* [BackForwardCacheOptions](arkts-apis-webview-backforwardcacheoptions.md)：前进后退缓存配置。
* [BackForwardCacheSupportedFeatures](arkts-apis-webview-backforwardcachesupportedfeatures.md)：设置前进后退缓存配置所支持的特性。
* [GeolocationPermissions](arkts-apis-webview-geolocationpermissions.md)：地理位置权限配置。
* [JsMessageExt](arkts-apis-webview-jsmessageext.md)：执行JavaScript脚本的结果。
* [MediaSourceInfo](arkts-apis-webview-mediasourceinfo.md)：媒体源信息。
* [NativeMediaPlayerSurfaceInfo](arkts-apis-webview-nativemediaplayersurfaceinfo.md)：应用接管媒体播放时渲染信息。
* [PdfData](arkts-apis-webview-pdfdata.md)：生成的PDF输出数据。
* [ProxyConfig](arkts-apis-webview-proxyconfig.md)：网络代理配置。
* [ProxyController](arkts-apis-webview-proxycontroller.md)：网络代理控制器。
* [WebviewController](arkts-apis-webview-webviewcontroller.md)：Web组件控制器。
* [WebCookieManager](arkts-apis-webview-webcookiemanager.md)：Cookie管理。
* [WebDataBase](arkts-apis-webview-webdatabase.md)：数据库管理。
* [WebDownloadDelegate](arkts-apis-webview-webdownloaddelegate.md)：下载任务状态事件。
* [WebDownloadItem](arkts-apis-webview-webdownloaditem.md)：下载任务。
* [WebDownloadManager](arkts-apis-webview-webdownloadmanager.md)：下载任务管理。
* [WebHttpBodyStream](arkts-apis-webview-webhttpbodystream.md)：HTTP请求体。
* [WebMessageExt](arkts-apis-webview-webmessageext.md)：前端与应用通信数据对象。
* [WebResourceHandler](arkts-apis-webview-webresourcehandler.md)：资源加载控制。
* [WebSchemeHandler](arkts-apis-webview-webschemehandler.md)：指定Scheme的请求拦截器。
* [WebSchemeHandlerRequest](arkts-apis-webview-webschemehandlerrequest.md)：通过拦截器拦截到的请求。
* [WebSchemeHandlerResponse](arkts-apis-webview-webschemehandlerresponse.md)：为拦截到的请求创建自定义响应。
* [WebStorage](arkts-apis-webview-webstorage.md)：Web组件存储操作接口。
* [BackForwardList](arkts-apis-webview-backforwardlist.md)：历史信息列表。
* [NativeMediaPlayerBridge](arkts-apis-webview-nativemediaplayerbridge.md)：托管网页媒体播放器桥接接口。
* [NativeMediaPlayerHandler](arkts-apis-webview-nativemediaplayerhandler.md)：托管网页媒体播放器的事件接口。
* [WebMessagePort](arkts-apis-webview-webmessageport.md)：网页前端与应用的消息端口。

## 需要权限

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 导入模块

```ts
import { webview } from '@kit.ArkWeb';
```

**系统能力：** SystemCapability.Web.Webview.Core
