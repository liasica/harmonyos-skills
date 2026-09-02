---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-193
title: ArkWeb本地资源跨域问题和解决方案
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > ArkWeb本地资源跨域问题和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f8a59a5e606d961352fac4521a668508d93ab63c43b04dc60fb082b659ca0b6
---

## 问题现象

为了提高安全性，ArkWeb内核不允许file协议或者resource协议访问URL上下文中来自跨域的请求，在使用ArkWeb加载H5页面时，会因为该限制遇到跨域相关的问题，本文总结了本地资源跨域问题和解决方案。

## 背景知识

* [setPathAllowingUniversalAccess](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setpathallowinguniversalaccess12)：设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件，也允许跨域访问其他在线资源；
* [onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)：当Web组件加载URL之前触发该回调，用于拦截URL并返回响应数据；
* [WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)：用于拦截指定scheme请求的拦截器。

## 问题定位

* 问题一：加载本地静态资源报跨域错误，控制台常见报错：

  ```txt
  "Uncaught SecurityError: Failed to construct 'Worker': Script at 'xxx' cannot be accessed from origin 'null'."
  ```
* 问题二：本地资源请求服务端跨域，控制台常见报错：

  ```txt
  Access to XMLHttpRequest at 'xxx' from origin 'resource://rawfile' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, arkweb-extension, https, chrome-untrusted, arkweb, data, chrome-extension, chrome.
  ```

## 分析结论

针对本地资源跨域问题，通常有以下两种解决方案：

方案一：通过setPathAllowingUniversalAccess设置一个路径列表，再使用file协议访问该路径列表中的资源，允许跨域访问本地文件；

方案二：对本地资源进行拦截和替换：采用http或https等协议，替代原先使用的file或resource协议进行加载。

## 修改建议

* 针对问题一加载本地资源跨域的问题，解决方案如下：

  方案一：通过[setPathAllowingUniversalAccess()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setpathallowinguniversalaccess12)设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件。

  设置路径列表时，有以下注意点：

  1. 如果设置跨域的路径为resourceDir，对应静态资源目录为应用resources目录下的resfile目录（与rawfile目录同级）；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Z760_4JgTsWyEBWS6R_1GQ/zh-cn_image_0000002659138445.png)
  2. 如果设置跨域路径为应用文件目录的子目录，不能直接指定应用沙箱目录，需要指定应用沙箱目录的子目录。例如不能直接指定沙箱文件目录/data/storage/el2/base/haps/entry/files，需要指定文件目录下的子目录，如：/data/storage/el2/base/haps/entry/files/example。

  方案二：参考[本地资源跨域问题解决方法](../harmonyos-guides/web-cross-origin.md#本地资源跨域问题解决方法)的方法一，使用http或https协议替代file或resource协议，即先加载自定义构造的http或者https的URL，再结合Web的设置请求拦截器接口如[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)拦截替换加载资源。
* 针对问题二遇到的本地资源请求服务端跨域，解决方案如下：

  方案一：因setPathAllowingUniversalAccess接口也允许跨域访问其他在线资源，可直接使用该接口解决；

  方案二：使用http或https协议替代file或resource协议的方案，需要注意的是，加载自定义构造的URL需要与服务端URL一致；

  方案三：可参考[远程请求跨域](../best-practices/bpta-cross-domain-solutions-for-web-pages.md#section1281615241211)中的代理请求方案，通过设置拦截器如[setWebSchemeHandler()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebschemehandler12)拦截H5中的http请求，并通过[RCP](../harmonyos-references/remote-communication-rcp.md)作为跨域请求的代理请求，请求完成后将结果和响应头设置到[resourceHandler](../harmonyos-references/arkts-apis-webview-webresourcehandler.md)中通知Web组件被拦截的请求已经完成，实现代码demo可参考：[基于ArkWeb拦截器和Cookies管理能力实现Web页面跨域](https://gitcode.com/HarmonyOS_Samples/WebCrossDomain/tree/master)。
