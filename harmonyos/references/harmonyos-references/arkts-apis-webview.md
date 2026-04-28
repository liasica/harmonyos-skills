---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T08:05:00+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d21d3a1df263150d15163a00eaea8e6bc29cabecc13f0747611fb2fe4fca58d1
---

本模块提供Web控制能力，网页显示的能力请参考[组件描述](arkts-basic-components-web.md)。

元服务中使用ArkWeb的说明，请参考[Web组件概述](../atomic-guides/atomicserviceweb-guidelines.md)。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。
* 静态方法必须在用户界面（UI）线程上使用。

该模块提供以下Web控制相关的常用功能：

* [AdsBlockManager](arkts-apis-webview-adsblockmanager.md)：广告过滤配置。
* [BackForwardCacheOptions](arkts-apis-webview-backforwardcacheoptions.md)：前进后退缓存配置。
* [BackForwardCacheSupportedFeatures](kts-apis-webview-backforwardcachesupportedfeatures.md)：设置前进后退缓存配置所支持的特性。
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

PhonePC/2in1TabletTVWearable

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

**系统能力：** SystemCapability.Web.Webview.Core
