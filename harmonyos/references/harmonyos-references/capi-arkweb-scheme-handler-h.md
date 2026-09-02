---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-scheme-handler-h
title: arkweb_scheme_handler.h
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 头文件 > arkweb_scheme_handler.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9489ec95ae80ea645049a3d098a227bbaadfdd73f6d97fc11d88dba9f13eaff5
---

## 概述

arkweb\_scheme\_handler.h是ArkWeb中用于拦截和自定义网络请求的完整C API头文件。该模块定义了注册自定义Scheme拦截器的ArkWeb\_SchemeHandler、发送自定义响应的ArkWeb\_ResourceHandler、构建HTTP响应的ArkWeb\_Response、检查请求详情的ArkWeb\_ResourceRequest，以及用于读取上传数据的ArkWeb\_HttpBodyStream和访问请求头的ArkWeb\_RequestHeaderList。该API配合ArkWeb\_NativeAPIVariantKind系统使用，通过OH\_ArkWeb\_SetSchemeHandler或OH\_ArkWebServiceWorker\_SetSchemeHandler注册。开发者可以实现自定义协议的资源加载和响应，适用于本地资源替换、数据加密传输、离线缓存等场景，通过拦截和自定义网络请求，帮助开发者解决标准协议无法满足的特殊业务需求，提升应用的安全性和数据控制能力，优化网络资源加载效率。

**引用文件：** <web/arkweb\_scheme\_handler.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**相关示例：** [ArkWebSchemeHandler](https://gitcode.com/harmonyos_samples/DocsSample_ArkWeb/tree/master/ArkWebSchemeHandler)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_SchemeHandler\_](capi-web-arkweb-schemehandler.md) | ArkWeb\_SchemeHandler | 用于拦截指定scheme的请求。 |
| [ArkWeb\_ResourceHandler\_](capi-web-arkweb-resourcehandler.md) | ArkWeb\_ResourceHandler | 用于被拦截的URL请求。可以通过ArkWeb\_ResourceHandler发送自定义响应头以及自定义响应体。 |
| [ArkWeb\_Response\_](capi-web-arkweb-response.md) | ArkWeb\_Response | 为被拦截的请求构造一个ArkWeb\_Response。 |
| [ArkWeb\_ResourceRequest\_](capi-web-arkweb-resourcerequest.md) | ArkWeb\_ResourceRequest | 对应内核的一个请求，可以通过OH\_ArkWebResourceRequest\_系列接口获取请求的URL、method、post data以及其他信息。如通过[OH\_ArkWebResourceRequest\_GetUrl](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_geturl)获取请求的URL。 |
| [ArkWeb\_RequestHeaderList\_](capi-web-arkweb-requestheaderlist.md) | ArkWeb\_RequestHeaderList | 请求头列表。 |
| [ArkWeb\_HttpBodyStream\_](capi-web-arkweb-httpbodystream.md) | ArkWeb\_HttpBodyStream | 请求的上传数据。使用OH\_ArkWebHttpBodyStream\_接口来读取上传的数据。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_CustomSchemeOption](capi-arkweb-scheme-handler-h.md#arkweb_customschemeoption) | ArkWeb\_CustomSchemeOption | custom scheme的配置信息。 |
| [ArkWeb\_ResourceType](capi-arkweb-scheme-handler-h.md#arkweb_resourcetype) | ArkWeb\_ResourceType | 请求的资源类型。这些常量与Chromium中的ResourceType的对应项相匹配，不应重新编号。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*ArkWeb\_OnRequestStart)(const ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_ResourceRequest\* resourceRequest,const ArkWeb\_ResourceHandler\* resourceHandler,bool\* intercept)](capi-arkweb-scheme-handler-h.md#arkweb_onrequeststart) | ArkWeb\_OnRequestStart | 请求开始的回调，这将在IO线程上被调用。 |
| [typedef void (\*ArkWeb\_OnRequestStop)(const ArkWeb\_SchemeHandler\* schemeHandler,const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#arkweb_onrequeststop) | ArkWeb\_OnRequestStop | 请求完成时的回调函数。这将在IO线程上被调用。  应该使用OH\_ArkWebResourceRequest\_Destroy销毁resourceRequest，  并使用OH\_ArkWebResourceHandler\_Destroy销毁在ArkWeb\_OnRequestStart中接收到的ArkWeb\_ResourceHandler。 |
| [typedef void (\*ArkWeb\_HttpBodyStreamReadCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream,uint8\_t\* buffer,int bytesRead)](capi-arkweb-scheme-handler-h.md#arkweb_httpbodystreamreadcallback) | ArkWeb\_HttpBodyStreamReadCallback | 当OH\_ArkWebHttpBodyStream\_Read读取操作完成时的回调函数。 |
| [typedef void (\*ArkWeb\_HttpBodyStreamAsyncReadCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream,uint8\_t\* buffer,int bytesRead)](capi-arkweb-scheme-handler-h.md#arkweb_httpbodystreamasyncreadcallback) | ArkWeb\_HttpBodyStreamAsyncReadCallback | 当OH\_ArkWebHttpBodyStream\_AsyncRead读取操作完成时的回调函数。 |
| [typedef void (\*ArkWeb\_HttpBodyStreamInitCallback)(const ArkWeb\_HttpBodyStream\* httpBodyStream, ArkWeb\_NetError result)](capi-arkweb-scheme-handler-h.md#arkweb_httpbodystreaminitcallback) | ArkWeb\_HttpBodyStreamInitCallback | ArkWeb\_HttpBodyStream初始化操作完成时回调函数。 |
| [void OH\_ArkWebRequestHeaderList\_Destroy(ArkWeb\_RequestHeaderList\* requestHeaderList)](capi-arkweb-scheme-handler-h.md#oh_arkwebrequestheaderlist_destroy) | - | 销毁ArkWeb\_RequestHeaderList对象。 |
| [int32\_t OH\_ArkWebRequestHeaderList\_GetSize(const ArkWeb\_RequestHeaderList\* requestHeaderList)](capi-arkweb-scheme-handler-h.md#oh_arkwebrequestheaderlist_getsize) | - | 获取请求头列表的大小。 |
| [void OH\_ArkWebRequestHeaderList\_GetHeader(const ArkWeb\_RequestHeaderList\* requestHeaderList,int32\_t index,char\*\* key,char\*\* value)](capi-arkweb-scheme-handler-h.md#oh_arkwebrequestheaderlist_getheader) | - | 获取指定的请求头。 |
| [int32\_t OH\_ArkWebResourceRequest\_SetUserData(ArkWeb\_ResourceRequest\* resourceRequest, void\* userData)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_setuserdata) | - | 将一个用户数据设置到ArkWeb\_ResourceRequest对象中。 |
| [void\* OH\_ArkWebResourceRequest\_GetUserData(const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getuserdata) | - | 从ArkWeb\_ResourceRequest获取用户数据。 |
| [void OH\_ArkWebResourceRequest\_GetMethod(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* method)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getmethod) | - | 获取请求的method。 |
| [void OH\_ArkWebResourceRequest\_GetUrl(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* url)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_geturl) | - | 获取请求的url。 |
| [void OH\_ArkWebResourceRequest\_GetHttpBodyStream(const ArkWeb\_ResourceRequest\* resourceRequest,ArkWeb\_HttpBodyStream\*\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_gethttpbodystream) | - | 创建一个ArkWeb\_HttpBodyStream，用于读取请求的上传数据。 |
| [void OH\_ArkWebResourceRequest\_DestroyHttpBodyStream(ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_destroyhttpbodystream) | - | 销毁ArkWeb\_HttpBodyStream对象。 |
| [int32\_t OH\_ArkWebResourceRequest\_GetResourceType(const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getresourcetype) | - | 获取请求的资源类型。 |
| [void OH\_ArkWebResourceRequest\_GetFrameUrl(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* frameUrl)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getframeurl) | - | 获取触发此请求的Frame的URL。 |
| [int32\_t OH\_ArkWebHttpBodyStream\_SetUserData(ArkWeb\_HttpBodyStream\* httpBodyStream, void\* userData)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_setuserdata) | - | 将一个用户数据设置到ArkWeb\_HttpBodyStream对象中。 |
| [void\* OH\_ArkWebHttpBodyStream\_GetUserData(const ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_getuserdata) | - | 从ArkWeb\_HttpBodyStream获取用户数据。 |
| [int32\_t OH\_ArkWebHttpBodyStream\_SetReadCallback(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamReadCallback readCallback)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_setreadcallback) | - | 为OH\_ArkWebHttpBodyStream\_Read设置回调函数。OH\_ArkWebHttpBodyStream\_Read的结果将通过readCallback通知给调用者。  该回调函数将在与OH\_ArkWebHttpBodyStream\_Read相同的线程中运行。 |
| [int32\_t OH\_ArkWebHttpBodyStream\_SetAsyncReadCallback(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamAsyncReadCallback readCallback)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_setasyncreadcallback) | - | 为OH\_ArkWebHttpBodyStream\_AsyncRead设置回调函数。OH\_ArkWebHttpBodyStream\_AsyncRead的结果将通过readCallback通知给开发者。  该回调函数会在ArkWeb工作线程中运行。 |
| [int32\_t OH\_ArkWebHttpBodyStream\_Init(ArkWeb\_HttpBodyStream\* httpBodyStream,ArkWeb\_HttpBodyStreamInitCallback initCallback)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_init) | - | 初始化ArkWeb\_HttpBodyStream。在调用任何其他函数之前，必须调用此函数。该接口需要在IO线程调用。 |
| [void OH\_ArkWebHttpBodyStream\_Read(const ArkWeb\_HttpBodyStream\* httpBodyStream, uint8\_t\* buffer, int bufLen)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_read) | - | 将请求的上传数据读取到buffer。buffer的大小必须大于或等于bufLen。我们将从工作线程读取数据到buffer，因此在回调函数返回之前，不应在其他线程中使用buffer，以避免并发问题。 |
| [void OH\_ArkWebHttpBodyStream\_AsyncRead(const ArkWeb\_HttpBodyStream\* httpBodyStream, uint8\_t\* buffer, int bufLen)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_asyncread) | - | 将请求的上传数据读取到buffer。buffer的大小必须大于或等于bufLen。数据将从工作线程读取到buffer，因此在回调函数返回之前，不应在其他线程中使用buffer，以避免并发问题。 |
| [uint64\_t OH\_ArkWebHttpBodyStream\_GetSize(const ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_getsize) | - | 获取httpBodyStream的大小。当数据以分块的形式传输或httpBodyStream无效时，始终返回0。 |
| [uint64\_t OH\_ArkWebHttpBodyStream\_GetPosition(const ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_getposition) | - | 获取httpBodyStream当前的读取位置。 |
| [bool OH\_ArkWebHttpBodyStream\_IsChunked(const ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_ischunked) | - | 获取httpBodyStream是否采用分块传输。 |
| [bool OH\_ArkWebHttpBodyStream\_IsEof(const ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_iseof) | - | 如果httpBodyStream中的所有数据都已被读取，则返回true。对于分块传输类型的httpBodyStream，在第一次读取尝试之前返回false。 |
| [bool OH\_ArkWebHttpBodyStream\_IsInMemory(const ArkWeb\_HttpBodyStream\* httpBodyStream)](capi-arkweb-scheme-handler-h.md#oh_arkwebhttpbodystream_isinmemory) | - | 如果httpBodyStream中的上传数据完全在内存中，并且所有读取请求都将同步成功，则返回true。对于分块传输类型的数据，预期返回false。 |
| [int32\_t OH\_ArkWebResourceRequest\_Destroy(const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_destroy) | - | 销毁ArkWeb\_ResourceRequest对象。 |
| [void OH\_ArkWebResourceRequest\_GetReferrer(const ArkWeb\_ResourceRequest\* resourceRequest, char\*\* referrer)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getreferrer) | - | 获取请求的Referrer。 |
| [void OH\_ArkWebResourceRequest\_GetRequestHeaders(const ArkWeb\_ResourceRequest\* resourceRequest,ArkWeb\_RequestHeaderList\*\* requestHeaderList)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getrequestheaders) | - | 获取请求的请求头列表ArkWeb\_RequestHeaderList。 |
| [bool OH\_ArkWebResourceRequest\_IsRedirect(const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_isredirect) | - | 判断这是否是一个重定向请求。 |
| [bool OH\_ArkWebResourceRequest\_IsMainFrame(const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_ismainframe) | - | 判断这是否是主框架文档资源的请求。 |
| [bool OH\_ArkWebResourceRequest\_HasGesture(const ArkWeb\_ResourceRequest\* resourceRequest)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_hasgesture) | - | 判断这是否是一个由用户手势触发的请求。 |
| [int32\_t OH\_ArkWeb\_RegisterCustomSchemes(const char\* scheme, int32\_t option)](capi-arkweb-scheme-handler-h.md#oh_arkweb_registercustomschemes) | - | 将custom scheme注册到ArkWeb。对于内置的HTTP、HTTPS、FILE、FTP、ABOUT和DATA协议，不应调用此函数。  此函数应在主线程上调用并且需要在内核初始化之前调用。 |
| [bool OH\_ArkWebServiceWorker\_SetSchemeHandler(const char\* scheme, ArkWeb\_SchemeHandler\* schemeHandler)](capi-arkweb-scheme-handler-h.md#oh_arkwebserviceworker_setschemehandler) | - | 为指定scheme设置一个ArkWeb\_SchemeHandler以拦截ServiceWorker触发的该scheme类型的请求。应该在创建BrowserContext之后设置SchemeHandler。  可以使用WebviewController.initializeWebEngine来初始化BrowserContext而无需创建ArkWeb。 |
| [bool OH\_ArkWeb\_SetSchemeHandler(const char\* scheme, const char\* webTag, ArkWeb\_SchemeHandler\* schemeHandler)](capi-arkweb-scheme-handler-h.md#oh_arkweb_setschemehandler) | - | 为指定scheme设置一个ArkWeb\_SchemeHandler以拦截该scheme类型的请求。应该在创建BrowserContext之后设置SchemeHandler。  可以使用WebviewController.initializeWebEngine来初始化BrowserContext而无需创建ArkWeb。 |
| [int32\_t OH\_ArkWebServiceWorker\_ClearSchemeHandlers()](capi-arkweb-scheme-handler-h.md#oh_arkwebserviceworker_clearschemehandlers) | - | 清除为ServiceWorker注册的SchemeHandler。 |
| [int32\_t OH\_ArkWeb\_ClearSchemeHandlers(const char\* webTag)](capi-arkweb-scheme-handler-h.md#oh_arkweb_clearschemehandlers) | - | 清除为指定web注册的SchemeHandler。 |
| [void OH\_ArkWeb\_CreateSchemeHandler(ArkWeb\_SchemeHandler\*\* schemeHandler)](capi-arkweb-scheme-handler-h.md#oh_arkweb_createschemehandler) | - | 创建一个ArkWeb\_SchemeHandler对象。 |
| [void OH\_ArkWeb\_DestroySchemeHandler(ArkWeb\_SchemeHandler\* schemeHandler)](capi-arkweb-scheme-handler-h.md#oh_arkweb_destroyschemehandler) | - | 销毁一个ArkWeb\_SchemeHandler对象。 |
| [int32\_t OH\_ArkWebSchemeHandler\_SetUserData(ArkWeb\_SchemeHandler\* schemeHandler, void\* userData)](capi-arkweb-scheme-handler-h.md#oh_arkwebschemehandler_setuserdata) | - | 将一个用户数据设置到ArkWeb\_SchemeHandler对象中。 |
| [void\* OH\_ArkWebSchemeHandler\_GetUserData(const ArkWeb\_SchemeHandler\* schemeHandler)](capi-arkweb-scheme-handler-h.md#oh_arkwebschemehandler_getuserdata) | - | 从ArkWeb\_SchemeHandler获取用户数据。 |
| [int32\_t OH\_ArkWebSchemeHandler\_SetOnRequestStart(ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_OnRequestStart onRequestStart)](capi-arkweb-scheme-handler-h.md#oh_arkwebschemehandler_setonrequeststart) | - | 为SchemeHandler设置OnRequestStart回调。 |
| [int32\_t OH\_ArkWebSchemeHandler\_SetOnRequestStop(ArkWeb\_SchemeHandler\* schemeHandler,ArkWeb\_OnRequestStop onRequestStop)](capi-arkweb-scheme-handler-h.md#oh_arkwebschemehandler_setonrequeststop) | - | 为SchemeHandler设置OnRequestStop回调。 |
| [void OH\_ArkWeb\_CreateResponse(ArkWeb\_Response\*\* response)](capi-arkweb-scheme-handler-h.md#oh_arkweb_createresponse) | - | 为被拦截的请求创建一个ArkWeb\_Response对象。 |
| [void OH\_ArkWeb\_DestroyResponse(ArkWeb\_Response\* response)](capi-arkweb-scheme-handler-h.md#oh_arkweb_destroyresponse) | - | 销毁一个ArkWeb\_Response对象。 |
| [int32\_t OH\_ArkWebResponse\_SetUrl(ArkWeb\_Response\* response, const char\* url)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_seturl) | - | 设置经过重定向或由于HSTS而改变后的解析URL，设置后会触发跳转。 |
| [void OH\_ArkWebResponse\_GetUrl(const ArkWeb\_Response\* response, char\*\* url)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_geturl) | - | 获取经过重定向或由于HSTS而更改后的解析URL。 |
| [int32\_t OH\_ArkWebResponse\_SetError(ArkWeb\_Response\* response, ArkWeb\_NetError errorCode)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_seterror) | - | 给ArkWeb\_Response对象设置一个错误码。 |
| [ArkWeb\_NetError OH\_ArkWebResponse\_GetError(const ArkWeb\_Response\* response)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_geterror) | - | 获取ArkWeb\_Response的错误码。 |
| [int32\_t OH\_ArkWebResponse\_SetStatus(ArkWeb\_Response\* response, int status)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_setstatus) | - | 为ArkWeb\_Response对象设置一个HTTP状态码。 |
| [int OH\_ArkWebResponse\_GetStatus(const ArkWeb\_Response\* response)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_getstatus) | - | 获取ArkWeb\_Response的HTTP状态码。 |
| [int32\_t OH\_ArkWebResponse\_SetStatusText(ArkWeb\_Response\* response, const char\* statusText)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_setstatustext) | - | 为ArkWeb\_Response设置状态文本。 |
| [void OH\_ArkWebResponse\_GetStatusText(const ArkWeb\_Response\* response, char\*\* statusText)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_getstatustext) | - | 获取ArkWeb\_Response的状态文本。 |
| [int32\_t OH\_ArkWebResponse\_SetMimeType(ArkWeb\_Response\* response, const char\* mimeType)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_setmimetype) | - | 为ArkWeb\_Response设置媒体类型。 |
| [void OH\_ArkWebResponse\_GetMimeType(const ArkWeb\_Response\* response, char\*\* mimeType)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_getmimetype) | - | 获取ArkWeb\_Response的媒体类型。 |
| [int32\_t OH\_ArkWebResponse\_SetCharset(ArkWeb\_Response\* response, const char\* charset)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_setcharset) | - | 为ArkWeb\_Response设置字符集。 |
| [void OH\_ArkWebResponse\_GetCharset(const ArkWeb\_Response\* response, char\*\* charset)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_getcharset) | - | 获取ArkWeb\_Response的字符集。 |
| [int32\_t OH\_ArkWebResponse\_SetHeaderByName(ArkWeb\_Response\* response,const char\* name,const char\* value,bool overwrite)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_setheaderbyname) | - | 为ArkWeb\_Response设置一个header。 |
| [void OH\_ArkWebResponse\_GetHeaderByName(const ArkWeb\_Response\* response, const char\* name, char\*\* value)](capi-arkweb-scheme-handler-h.md#oh_arkwebresponse_getheaderbyname) | - | 从ArkWeb\_Response中获取header。 |
| [int32\_t OH\_ArkWebResourceHandler\_Destroy(const ArkWeb\_ResourceHandler\* resourceHandler)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_destroy) | - | 销毁一个ArkWeb\_ResourceHandler对象。 |
| [int32\_t OH\_ArkWebResourceHandler\_DidReceiveResponse(const ArkWeb\_ResourceHandler\* resourceHandler,const ArkWeb\_Response\* response)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse) | - | 将构造的响应头传递给被拦截的请求。 |
| [int32\_t OH\_ArkWebResourceHandler\_DidReceiveData(const ArkWeb\_ResourceHandler\* resourceHandler,const uint8\_t\* buffer,int64\_t bufLen)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceivedata) | - | 将构造的响应体传递给被拦截的请求。 |
| [int32\_t OH\_ArkWebResourceHandler\_DidFinish(const ArkWeb\_ResourceHandler\* resourceHandler)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfinish) | - | 通知ArkWeb内核被拦截的请求已经完成，并且没有更多的数据可用。 |
| [int32\_t OH\_ArkWebResourceHandler\_DidFailWithError(const ArkWeb\_ResourceHandler\* resourceHandler,ArkWeb\_NetError errorCode)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfailwitherror) | - | 通知ArkWeb内核，被拦截的请求应该失败。 |
| [int32\_t OH\_ArkWebResourceHandler\_DidFailWithErrorV2(const ArkWeb\_ResourceHandler\* resourceHandler,ArkWeb\_NetError errorCode,bool completeIfNoResponse)](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfailwitherrorv2) | - | 通知ArkWeb内核，被拦截的请求应该失败。对比OH\_ArkWebResourceHandler\_DidFailWithError接口，新增参数completeIfNoResponse，当值为true时，若之前未调用过OH\_ArkWebResourceHandler\_DidReceiveResponse，则会自动生成一个response以完成此次网络请求，网络错误码为-104；值为false时，将等待应用调用OH\_ArkWebResourceHandler\_DidReceiveResponse并传入response，不会直接完成此次网络请求。 |
| [void OH\_ArkWeb\_ReleaseString(char\* string)](capi-arkweb-scheme-handler-h.md#oh_arkweb_releasestring) | - | 释放由NDK接口创建的字符串。 |
| [void OH\_ArkWeb\_ReleaseByteArray(uint8\_t\* byteArray)](capi-arkweb-scheme-handler-h.md#oh_arkweb_releasebytearray) | - | 释放由NDK接口创建的字节数组。 |

## 枚举类型说明

### ArkWeb\_CustomSchemeOption

```c
enum ArkWeb_CustomSchemeOption
```

**描述：**

custom scheme的配置信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARKWEB\_SCHEME\_OPTION\_NONE = 0 | 表示注册自定义scheme时不赋予它任何特殊行为或能力。 |
| ARKWEB\_SCHEME\_OPTION\_STANDARD = 1 << 0 | 如果设置了ARKWEB\_SCHEME\_OPTION\_STANDARD，那么该scheme将被视为标准scheme来处理。 |
| ARKWEB\_SCHEME\_OPTION\_LOCAL = 1 << 1 | 如果设置了ARKWEB\_SCHEME\_OPTION\_LOCAL，则将使用与“file” URL相同的安全规则来处理该scheme。 |
| ARKWEB\_SCHEME\_OPTION\_DISPLAY\_ISOLATED = 1 << 2 | 如果设置了ARKWEB\_SCHEME\_OPTION\_DISPLAY\_ISOLATED，则该scheme的请求只能由使用相同scheme加载的页面中发起。 |
| ARKWEB\_SCHEME\_OPTION\_SECURE = 1 << 3 | 如果设置了ARKWEB\_SCHEME\_OPTION\_SECURE，则将使用与“https” URL相同的安全规则来处理该scheme。 |
| ARKWEB\_SCHEME\_OPTION\_CORS\_ENABLED = 1 << 4 | 如果设置了ARKWEB\_SCHEME\_OPTION\_CORS\_ENABLED，则该scheme可以发送CORS请求。在大多数情况下，当设置了ARKWEB\_SCHEME\_OPTION\_STANDARD时，应该设置此值。 |
| ARKWEB\_SCHEME\_OPTION\_CSP\_BYPASSING = 1 << 5 | 如果设置了ARKWEB\_SCHEME\_OPTION\_CSP\_BYPASSING，则该scheme可以绕过内容安全策略（CSP）检查。 |
| ARKWEB\_SCHEME\_OPTION\_FETCH\_ENABLED = 1 << 6 | 如果设置了ARKWEB\_SCHEME\_OPTION\_FETCH\_ENABLED，则可以发起该scheme的FETCH API请求。 |
| ARKWEB\_SCHEME\_OPTION\_CODE\_CACHE\_ENABLED = 1 << 7 | 如果设置了ARKWEB\_SCHEME\_OPTION\_CODE\_CACHE\_ENABLED，则该scheme的js资源支持生成code cache。 |

### ArkWeb\_ResourceType

```c
enum ArkWeb_ResourceType
```

**描述：**

请求的资源类型。这些常量与Chromium中的ResourceType的对应项相匹配，不应重新编号。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| MAIN\_FRAME = 0 | 顶层页面。 |
| SUB\_FRAME = 1 | Frame或Iframe。 |
| STYLE\_SHEET = 2 | CSS样式表。 |
| SCRIPT = 3 | 外部脚本。 |
| IMAGE = 4 | 图片（jpg/gif/png/以及其他）。 |
| FONT\_RESOURCE = 5 | 字体。 |
| SUB\_RESOURCE = 6 | 其他子资源。如果实际类型未知，则是默认类型。 |
| OBJECT = 7 | 插件的Object（或embed）标签，或者插件请求的资源。 |
| MEDIA = 8 | 媒体资源。 |
| WORKER = 9 | 专用工作线程的主资源。 |
| SHARED\_WORKER = 10 | 共享工作线程的主资源。 |
| PREFETCH = 11 | 明确的预取请求。 |
| FAVICON = 12 | 网站图标。 |
| XHR = 13 | XMLHttpRequest。 |
| PING = 14 | /sendBeacon的Ping请求。 |
| SERVICE\_WORKER = 15 | service worker的主资源。 |
| CSP\_REPORT = 16 | 内容安全策略违规报告。 |
| PLUGIN\_RESOURCE = 17 | 插件请求的资源。 |
| NAVIGATION\_PRELOAD\_MAIN\_FRAME = 19 | 触发service worker预热的主frame跳转请求。 |
| NAVIGATION\_PRELOAD\_SUB\_FRAME = 20 | 触发service worker预热的子frame跳转请求。 |

## 函数说明

### ArkWeb\_OnRequestStart()

```c
typedef void (*ArkWeb_OnRequestStart)(const ArkWeb_SchemeHandler* schemeHandler,ArkWeb_ResourceRequest* resourceRequest,const ArkWeb_ResourceHandler* resourceHandler,bool* intercept)
```

**描述：**

请求开始的回调，这将在IO线程上被调用。用于在请求开始时拦截和处理指定scheme的网络请求，开发者可通过此回调实现自定义协议处理、本地资源替换、数据加密传输等功能。

**说明** 

* 重定向后的URL无法单独拦截。如需拦截，必须同时对原始请求URL进行拦截。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | ArkWeb\_SchemeHandler。 |
| [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | 通过该对象获取请求的信息。 |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | 请求的ArkWeb\_ResourceHandler。如果intercept设置为false，则不应使用它。 |
| bool\* intercept | 如果为true，则会拦截请求；如果为false，则不会拦截。 |

### ArkWeb\_OnRequestStop()

```c
typedef void (*ArkWeb_OnRequestStop)(const ArkWeb_SchemeHandler* schemeHandler,const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

请求完成时的回调函数。这将在IO线程上被调用。用于在请求完成时进行资源清理、状态更新或日志记录等操作。

应该使用OH\_ArkWebResourceRequest\_Destroy销毁resourceRequest，并使用OH\_ArkWebResourceHandler\_Destroy销毁在ArkWeb\_OnRequestStart中接收到的ArkWeb\_ResourceHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | ArkWeb\_SchemeHandler。 |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

### ArkWeb\_HttpBodyStreamReadCallback()

```c
typedef void (*ArkWeb_HttpBodyStreamReadCallback)(const ArkWeb_HttpBodyStream* httpBodyStream,uint8_t* buffer,int bytesRead)
```

**描述：**

当OH\_ArkWebHttpBodyStream\_Read读取操作完成时的回调函数。该回调函数会在ArkWeb工作线程中运行。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| uint8\_t\* buffer | 接收数据的buffer。 |
| int bytesRead | 读取的字节数。如果bytesRead大于0，则表示buffer已填充了bytesRead字节的数据。开发者可以从buffer中读取数据，如果OH\_ArkWebHttpBodyStream\_IsEof为false，则开发者可以继续读取剩余的数据。 |

### ArkWeb\_HttpBodyStreamAsyncReadCallback()

```c
typedef void (*ArkWeb_HttpBodyStreamAsyncReadCallback)(const ArkWeb_HttpBodyStream *httpBodyStream,uint8_t *buffer,int bytesRead)
```

**描述：**

当OH\_ArkWebHttpBodyStream\_AsyncRead读取操作完成时的回调函数。该回调函数会在ArkWeb工作线程中运行。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| uint8\_t\* buffer | 接收数据的缓冲区。 |
| int bytesRead | 标识异步读取操作执行结果的字节计数值。如果bytesRead大于0，则表示buffer已填充了bytesRead字节的数据。开发者可以从buffer中读取数据，如果OH\_ArkWebHttpBodyStream\_IsEof为false，则开发者可以继续读取剩余的数据。 |

### ArkWeb\_HttpBodyStreamInitCallback()

```c
typedef void (*ArkWeb_HttpBodyStreamInitCallback)(const ArkWeb_HttpBodyStream* httpBodyStream, ArkWeb_NetError result)
```

**描述：**

ArkWeb\_HttpBodyStream初始化操作完成时回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| [ArkWeb\_NetError](capi-arkweb-net-error-list-h.md#arkweb_neterror) result | 成功时返回ARKWEB\_NET\_OK，否则请参考[arkweb\_net\_error\_list.h](capi-arkweb-net-error-list-h.md)。 |

### OH\_ArkWebRequestHeaderList\_Destroy()

```c
void OH_ArkWebRequestHeaderList_Destroy(ArkWeb_RequestHeaderList* requestHeaderList)
```

**描述：**

销毁ArkWeb\_RequestHeaderList对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_RequestHeaderList](capi-web-arkweb-requestheaderlist.md)\* requestHeaderList | 将被销毁的ArkWeb\_RequestHeaderList。 |

### OH\_ArkWebRequestHeaderList\_GetSize()

```c
int32_t OH_ArkWebRequestHeaderList_GetSize(const ArkWeb_RequestHeaderList* requestHeaderList)
```

**描述：**

获取请求头列表的大小。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_RequestHeaderList](capi-web-arkweb-requestheaderlist.md)\* requestHeaderList | 请求头的列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 请求头的大小。如果requestHeaderList无效，则为-1。 |

### OH\_ArkWebRequestHeaderList\_GetHeader()

```c
void OH_ArkWebRequestHeaderList_GetHeader(const ArkWeb_RequestHeaderList* requestHeaderList,int32_t index,char** key,char** value)
```

**描述：**

获取指定的请求头。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkWeb\_RequestHeaderList\* requestHeaderList | 请求头列表。 |
| int32\_t index | 请求头的索引。取值范围为[0, size-1]，其中size是请求头列表的大小。 |
| char\*\* key | 请求头的键（key）。调用者必须使用OH\_ArkWeb\_ReleaseString函数来释放这个字符串。 |
| char\*\* value | 请求头的值（value）。调用者必须使用OH\_ArkWeb\_ReleaseString函数来释放这个字符串。 |

### OH\_ArkWebResourceRequest\_SetUserData()

```c
int32_t OH_ArkWebResourceRequest_SetUserData(ArkWeb_ResourceRequest* resourceRequest, void* userData)
```

**描述：**

将一个用户数据设置到ArkWeb\_ResourceRequest对象中。用于在不同请求回调之间传递上下文信息或存储请求关联的状态，后续可通过[OH\_ArkWebResourceRequest\_GetUserData()](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_getuserdata)获取。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| void\* userData | 将要设置的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceRequest\_GetUserData()

```c
void* OH_ArkWebResourceRequest_GetUserData(const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

从ArkWeb\_ResourceRequest获取用户数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 指向用户数据的指针。该指针由开发者通过[OH\_ArkWebResourceRequest\_SetUserData](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_setuserdata)设置，可用于在回调中传递自定义上下文信息。 |

### OH\_ArkWebResourceRequest\_GetMethod()

```c
void OH_ArkWebResourceRequest_GetMethod(const ArkWeb_ResourceRequest* resourceRequest, char** method)
```

**描述：**

获取请求的method。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| char\*\* method | HTTP请求方法。此函数将为method字符串分配内存，调用者必须使用OH\_ArkWeb\_ReleaseString释放字符串。 |

### OH\_ArkWebResourceRequest\_GetUrl()

```c
void OH_ArkWebResourceRequest_GetUrl(const ArkWeb_ResourceRequest* resourceRequest, char** url)
```

**描述：**

获取请求的url。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| char\*\* url | 请求的URL。此函数将为URL字符串分配内存，调用者必须通过OH\_ArkWeb\_ReleaseString释放该字符串。 |

### OH\_ArkWebResourceRequest\_GetHttpBodyStream()

```c
void OH_ArkWebResourceRequest_GetHttpBodyStream(const ArkWeb_ResourceRequest* resourceRequest,ArkWeb_HttpBodyStream** httpBodyStream)
```

**描述：**

创建一个ArkWeb\_HttpBodyStream，用于读取请求的上传数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\*\* httpBodyStream | 请求的上传数据。此函数将为httpBodyStream分配内存，调用者必须使用OH\_ArkWebResourceRequest\_DestroyHttpBodyStream释放httpBodyStream。 |

### OH\_ArkWebResourceRequest\_DestroyHttpBodyStream()

```c
void OH_ArkWebResourceRequest_DestroyHttpBodyStream(ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

销毁ArkWeb\_HttpBodyStream对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | 待销毁的httpBodyStream。 |

### OH\_ArkWebResourceRequest\_GetResourceType()

```c
int32_t OH_ArkWebResourceRequest_GetResourceType(const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

获取请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 请求的资源类型。如果resourceRequest无效，则为-1，表示请求对象为空或已失效。其他值参考[ArkWeb\_ResourceType](capi-arkweb-scheme-handler-h.md#arkweb_resourcetype)。 |

### OH\_ArkWebResourceRequest\_GetFrameUrl()

```c
void OH_ArkWebResourceRequest_GetFrameUrl(const ArkWeb_ResourceRequest* resourceRequest, char** frameUrl)
```

**描述：**

获取触发此请求的Frame的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| char\*\* frameUrl | 触发此请求的Frame的URL。此函数将为URL字符串分配内存，并且调用者必须通过OH\_ArkWeb\_ReleaseString来释放该字符串。 |

### OH\_ArkWebHttpBodyStream\_SetUserData()

```c
int32_t OH_ArkWebHttpBodyStream_SetUserData(ArkWeb_HttpBodyStream* httpBodyStream, void* userData)
```

**描述：**

将一个用户数据设置到ArkWeb\_HttpBodyStream对象中。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| void\* userData | 要设置的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebHttpBodyStream\_GetUserData()

```c
void* OH_ArkWebHttpBodyStream_GetUserData(const ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

从ArkWeb\_HttpBodyStream获取用户数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 指向用户数据的指针。该指针由开发者通过OH\_ArkWebHttpBodyStream\_SetUserData设置，可用于在回调中传递自定义上下文信息。 |

### OH\_ArkWebHttpBodyStream\_SetReadCallback()

```c
int32_t OH_ArkWebHttpBodyStream_SetReadCallback(ArkWeb_HttpBodyStream* httpBodyStream,ArkWeb_HttpBodyStreamReadCallback readCallback)
```

**描述：**

为OH\_ArkWebHttpBodyStream\_Read设置回调函数。OH\_ArkWebHttpBodyStream\_Read的结果将通过readCallback通知给调用者。

该回调函数将在与OH\_ArkWebHttpBodyStream\_Read相同的线程中运行。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| [ArkWeb\_HttpBodyStreamReadCallback](capi-arkweb-scheme-handler-h.md#arkweb_httpbodystreamreadcallback) readCallback | OH\_ArkWebHttpBodyStream\_Read的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebHttpBodyStream\_SetAsyncReadCallback()

```c
int32_t OH_ArkWebHttpBodyStream_SetAsyncReadCallback(ArkWeb_HttpBodyStream* httpBodyStream,ArkWeb_HttpBodyStreamAsyncReadCallback readCallback)
```

**描述：**

为OH\_ArkWebHttpBodyStream\_AsyncRead设置回调函数。OH\_ArkWebHttpBodyStream\_AsyncRead的结果将通过readCallback通知给开发者。

该回调函数会在ArkWeb工作线程中运行。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| [ArkWeb\_HttpBodyStreamAsyncReadCallback](capi-arkweb-scheme-handler-h.md#arkweb_httpbodystreamasyncreadcallback) readCallback | OH\_ArkWebHttpBodyStream\_AsyncRead的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebHttpBodyStream\_Init()

```c
int32_t OH_ArkWebHttpBodyStream_Init(ArkWeb_HttpBodyStream* httpBodyStream,ArkWeb_HttpBodyStreamInitCallback initCallback)
```

**描述：**

初始化ArkWeb\_HttpBodyStream。该函数负责建立httpBodyStream的内部数据结构和连接，为后续的读取操作做准备。初始化过程中会分配必要的资源、建立与工作线程的通信机制。在调用任何其他函数之前，必须调用此函数，否则其他操作将无法正常执行。该接口需要在IO线程调用，以确保线程安全和正确的初始化顺序。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| [ArkWeb\_HttpBodyStreamInitCallback](capi-arkweb-scheme-handler-h.md#arkweb_httpbodystreaminitcallback) initCallback | 初始化的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebHttpBodyStream\_Read()

```c
void OH_ArkWebHttpBodyStream_Read(const ArkWeb_HttpBodyStream* httpBodyStream, uint8_t* buffer, int bufLen)
```

**描述：**

将请求的上传数据读取到buffer。该函数采用异步读取机制，将读取任务提交到工作线程执行，通过回调函数返回读取结果。buffer的大小必须大于或等于bufLen，以确保能够容纳读取的数据。我们将从工作线程读取数据到buffer，因此在回调函数返回之前，不应在其他线程中使用buffer，以避免并发问题。读取操作完成后，将通过之前设置的回调函数通知调用者，并返回实际读取的字节数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| uint8\_t\* buffer | 接收数据的buffer。buffer的大小必须大于或等于bufLen。 |
| int bufLen | 要读取的字节数。取值范围必须为正整数，传入负数或0将导致读取失败。 |

### OH\_ArkWebHttpBodyStream\_AsyncRead()

```c
void OH_ArkWebHttpBodyStream_AsyncRead(const ArkWeb_HttpBodyStream* httpBodyStream, uint8_t* buffer, int bufLen)
```

**描述：**

将请求的上传数据读取至buffer，buffer的大小必须超过bufLen。数据将由工作线程读取至buffer，因此在回调函数返回前，不应在其他线程中使用缓冲区，以避免并发问题。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |
| uint8\_t\* buffer | 接收数据的缓冲区。 |
| int bufLen | 要读取的字节数。 |

### OH\_ArkWebHttpBodyStream\_GetSize()

```c
uint64_t OH_ArkWebHttpBodyStream_GetSize(const ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

获取httpBodyStream的大小。当数据以分块的形式传输或httpBodyStream无效时，始终返回0。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | httpBodyStream的大小。 |

### OH\_ArkWebHttpBodyStream\_GetPosition()

```c
uint64_t OH_ArkWebHttpBodyStream_GetPosition(const ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

获取httpBodyStream当前的读取位置。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | httpBodyStream当前的读取位置。如果httpBodyStream无效，则返回0。 |

### OH\_ArkWebHttpBodyStream\_IsChunked()

```c
bool OH_ArkWebHttpBodyStream_IsChunked(const ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

获取httpBodyStream是否采用分块传输。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果采用分块传输则返回true；否则返回false。 |

### OH\_ArkWebHttpBodyStream\_IsEof()

```c
bool OH_ArkWebHttpBodyStream_IsEof(const ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

如果httpBodyStream中的所有数据都已被读取，则返回true。对于分块传输类型的httpBodyStream，在第一次读取尝试之前返回false。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果所有数据都已被读取则返回true；否则返回false。 |

### OH\_ArkWebHttpBodyStream\_IsInMemory()

```c
bool OH_ArkWebHttpBodyStream_IsInMemory(const ArkWeb_HttpBodyStream* httpBodyStream)
```

**描述：**

如果httpBodyStream中的上传数据完全在内存中，并且所有读取请求都将同步成功，则返回true。对于分块传输类型的数据，预期返回false。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_HttpBodyStream](capi-web-arkweb-httpbodystream.md)\* httpBodyStream | ArkWeb\_HttpBodyStream。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果上传数据完全在内存中则返回true；否则返回false。 |

### OH\_ArkWebResourceRequest\_Destroy()

```c
int32_t OH_ArkWebResourceRequest_Destroy(const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

销毁ArkWeb\_ResourceRequest对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceRequest\_GetReferrer()

```c
void OH_ArkWebResourceRequest_GetReferrer(const ArkWeb_ResourceRequest* resourceRequest, char** referrer)
```

**描述：**

获取请求的Referrer。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| char\*\* referrer | 请求的Referrer。此函数将为referrer字符串分配内存，调用者必须使用OH\_ArkWeb\_ReleaseString释放该字符串。 |

### OH\_ArkWebResourceRequest\_GetRequestHeaders()

```c
void OH_ArkWebResourceRequest_GetRequestHeaders(const ArkWeb_ResourceRequest* resourceRequest,ArkWeb_RequestHeaderList** requestHeaderList)
```

**描述：**

获取请求的请求头列表ArkWeb\_RequestHeaderList。此函数将为requestHeaderList分配内存，调用者必须使用OH\_ArkWebRequestHeaderList\_Destroy释放requestHeaderList。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |
| [ArkWeb\_RequestHeaderList](capi-web-arkweb-requestheaderlist.md)\*\* requestHeaderList | 请求的请求头列表。 |

### OH\_ArkWebResourceRequest\_IsRedirect()

```c
bool OH_ArkWebResourceRequest_IsRedirect(const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

判断这是否是一个重定向请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果这是一个重定向，则返回true；如果不是重定向，则返回false。 |

### OH\_ArkWebResourceRequest\_IsMainFrame()

```c
bool OH_ArkWebResourceRequest_IsMainFrame(const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

判断这是否是主框架文档资源的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果这是来自主框架，则返回true；如果不是来自主框架，则返回false。 |

### OH\_ArkWebResourceRequest\_HasGesture()

```c
bool OH_ArkWebResourceRequest_HasGesture(const ArkWeb_ResourceRequest* resourceRequest)
```

**描述：**

判断这是否是一个由用户手势触发的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceRequest](capi-web-arkweb-resourcerequest.md)\* resourceRequest | ArkWeb\_ResourceRequest。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果这是由用户手势触发的，则返回true；如果不是由用户手势触发的，则返回false。 |

### OH\_ArkWeb\_RegisterCustomSchemes()

```c
int32_t OH_ArkWeb_RegisterCustomSchemes(const char* scheme, int32_t option)
```

**描述：**

将custom scheme注册到ArkWeb。对于内置的HTTP、HTTPS、FILE、FTP、ABOUT和DATA协议，不应调用此函数。此函数应在主线程上调用并且需要在内核初始化之前调用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scheme | 待注册的scheme，需符合RFC 3986规范。 |
| int32\_t option | scheme的配置（行为），取值参考[ArkWeb\_CustomSchemeOption](capi-arkweb-scheme-handler-h.md#arkweb_customschemeoption)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100100，表示未知错误，请检查调用时机和参数配置；返回17100101，表示参数无效；返回17100102，表示注册scheme的配置失败，应该在创建ArkWeb之前注册。 |

### OH\_ArkWebServiceWorker\_SetSchemeHandler()

```c
bool OH_ArkWebServiceWorker_SetSchemeHandler(const char* scheme, ArkWeb_SchemeHandler* schemeHandler)
```

**描述：**

为指定scheme设置一个ArkWeb\_SchemeHandler以拦截ServiceWorker触发的该scheme类型的请求。应该在创建BrowserContext之后设置SchemeHandler。

可以使用WebviewController.initializeWebEngine来初始化BrowserContext而无需创建ArkWeb。

**说明** 

* 重定向后的URL无法单独拦截。如需拦截，必须同时对原始请求URL进行拦截。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scheme | 需要被拦截的scheme，需符合RFC 3986规范。 |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | 该scheme的拦截器ArkWeb\_SchemeHandler。只有通过ServiceWorker触发的请求才会通过这个schemeHandler进行通知。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果为指定scheme设置SchemeHandler成功，则返回true，否则返回false。 |

### OH\_ArkWeb\_SetSchemeHandler()

```c
bool OH_ArkWeb_SetSchemeHandler(const char* scheme, const char* webTag, ArkWeb_SchemeHandler* schemeHandler)
```

**描述：**

为指定scheme设置一个ArkWeb\_SchemeHandler以拦截该scheme类型的请求。应该在创建BrowserContext之后设置SchemeHandler。

可以使用WebviewController.initializeWebEngine来初始化BrowserContext而无需创建ArkWeb。

**说明** 

* 重定向后的URL无法单独拦截。如需拦截，必须同时对原始请求URL进行拦截。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* scheme | 需要被拦截的scheme。 |
| const char\* webTag | Web组件的标签名称，用于标识某个唯一组件，由开发者来保证名称唯一性。建议长度不超过256字符。 |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | 该scheme的拦截器ArkWeb\_SchemeHandler。只有从指定web触发的请求才会通过这个schemeHandler进行通知。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果为指定scheme设置SchemeHandler成功，则返回true，否则返回false。 |

### OH\_ArkWebServiceWorker\_ClearSchemeHandlers()

```c
int32_t OH_ArkWebServiceWorker_ClearSchemeHandlers()
```

**描述：**

清除为ServiceWorker注册的SchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功。 |

### OH\_ArkWeb\_ClearSchemeHandlers()

```c
int32_t OH_ArkWeb_ClearSchemeHandlers(const char* webTag)
```

**描述：**

清除为指定web注册的SchemeHandler。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的标签名称，用于标识某个唯一组件，由开发者来保证名称唯一性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWeb\_CreateSchemeHandler()

```c
void OH_ArkWeb_CreateSchemeHandler(ArkWeb_SchemeHandler** schemeHandler)
```

**描述：**

创建一个ArkWeb\_SchemeHandler对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\*\* schemeHandler | 返回创建的ArkWeb\_SchemeHandler。在不需要时使用[OH\_ArkWeb\_DestroySchemeHandler](capi-arkweb-scheme-handler-h.md#oh_arkweb_destroyschemehandler)销毁它。 |

### OH\_ArkWeb\_DestroySchemeHandler()

```c
void OH_ArkWeb_DestroySchemeHandler(ArkWeb_SchemeHandler* schemeHandler)
```

**描述：**

销毁一个ArkWeb\_SchemeHandler对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | 待销毁的ArkWeb\_SchemeHandler。 |

### OH\_ArkWebSchemeHandler\_SetUserData()

```c
int32_t OH_ArkWebSchemeHandler_SetUserData(ArkWeb_SchemeHandler* schemeHandler, void* userData)
```

**描述：**

将一个用户数据设置到ArkWeb\_SchemeHandler对象中。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | ArkWeb\_SchemeHandler。 |
| void\* userData | 要设置的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebSchemeHandler\_GetUserData()

```c
void* OH_ArkWebSchemeHandler_GetUserData(const ArkWeb_SchemeHandler* schemeHandler)
```

**描述：**

从ArkWeb\_SchemeHandler获取用户数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | ArkWeb\_SchemeHandler。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 指向用户数据的指针。该指针由开发者通过OH\_ArkWebSchemeHandler\_SetUserData设置，可用于在回调中传递自定义上下文信息。 |

### OH\_ArkWebSchemeHandler\_SetOnRequestStart()

```c
int32_t OH_ArkWebSchemeHandler_SetOnRequestStart(ArkWeb_SchemeHandler* schemeHandler,ArkWeb_OnRequestStart onRequestStart)
```

**描述：**

为SchemeHandler设置OnRequestStart回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | 该scheme的SchemeHandler。 |
| [ArkWeb\_OnRequestStart](capi-arkweb-scheme-handler-h.md#arkweb_onrequeststart) onRequestStart | OnRequestStart回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebSchemeHandler\_SetOnRequestStop()

```c
int32_t OH_ArkWebSchemeHandler_SetOnRequestStop(ArkWeb_SchemeHandler* schemeHandler,ArkWeb_OnRequestStop onRequestStop)
```

**描述：**

为SchemeHandler设置OnRequestStop回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_SchemeHandler](capi-web-arkweb-schemehandler.md)\* schemeHandler | 该scheme的SchemeHandler。 |
| [ArkWeb\_OnRequestStop](capi-arkweb-scheme-handler-h.md#arkweb_onrequeststop) onRequestStop | OnRequestStop回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWeb\_CreateResponse()

```c
void OH_ArkWeb_CreateResponse(ArkWeb_Response** response)
```

**描述：**

为被拦截的请求创建一个ArkWeb\_Response对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\*\* response | 返回创建的ArkWeb\_Response。在不需要时使用OH\_ArkWeb\_DestroyResponse进行销毁。 |

### OH\_ArkWeb\_DestroyResponse()

```c
void OH_ArkWeb_DestroyResponse(ArkWeb_Response* response)
```

**描述：**

销毁一个ArkWeb\_Response对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | 待销毁的ArkWeb\_Response。 |

### OH\_ArkWebResponse\_SetUrl()

```c
int32_t OH_ArkWebResponse_SetUrl(ArkWeb_Response* response, const char* url)
```

**描述：**

设置经过重定向或由于HSTS而改变后的解析URL，设置后会触发跳转。用于在自定义响应中实现URL重定向，如URL规范化、域名重定向、HTTP到HTTPS升级等场景。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| const char\* url | 解析后的URL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetUrl()

```c
void OH_ArkWebResponse_GetUrl(const ArkWeb_Response* response, char** url)
```

**描述：**

获取经过重定向或由于HSTS而更改后的解析URL。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| char\*\* url | 解析后的URL。此函数将为URL字符串分配内存，调用方必须通过OH\_ArkWeb\_ReleaseString释放该字符串。 |

### OH\_ArkWebResponse\_SetError()

```c
int32_t OH_ArkWebResponse_SetError(ArkWeb_Response* response, ArkWeb_NetError errorCode)
```

**描述：**

给ArkWeb\_Response对象设置一个错误码。用于与DidFailWithError配合使用，通过错误码告知客户端请求失败的具体原因，如权限错误、资源不存在等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| [ArkWeb\_NetError](capi-arkweb-net-error-list-h.md#arkweb_neterror) errorCode | 失败请求的错误码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetError()

```c
ArkWeb_NetError OH_ArkWebResponse_GetError(const ArkWeb_Response* response)
```

**描述：**

获取ArkWeb\_Response的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_NetError](capi-arkweb-net-error-list-h.md#arkweb_neterror) | ArkWeb\_Response的错误码。 |

### OH\_ArkWebResponse\_SetStatus()

```c
int32_t OH_ArkWebResponse_SetStatus(ArkWeb_Response* response, int status)
```

**描述：**

为ArkWeb\_Response对象设置一个HTTP状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| int status | 响应的HTTP状态码。取值范围为100-599，应符合HTTP标准状态码规范（信息100-199、成功200-299、重定向300-399、客户端错误400-499、服务器错误500-599）。超出范围时行为未定义。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetStatus()

```c
int OH_ArkWebResponse_GetStatus(const ArkWeb_Response* response)
```

**描述：**

获取ArkWeb\_Response的HTTP状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | ArkWeb\_Response的HTTP状态码。如果ArkWeb\_Response无效，则为-1。 |

### OH\_ArkWebResponse\_SetStatusText()

```c
int32_t OH_ArkWebResponse_SetStatusText(ArkWeb_Response* response, const char* statusText)
```

**描述：**

为ArkWeb\_Response设置状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| const char\* statusText | 响应的状态文本。设置状态文本会为HTTP状态码提供更详细的描述，例如：状态码200可以对应“OK”、状态码404可以对应“Not Found”等，帮助客户端更好地理解请求结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetStatusText()

```c
void OH_ArkWebResponse_GetStatusText(const ArkWeb_Response* response, char** statusText)
```

**描述：**

获取ArkWeb\_Response的状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| char\*\* statusText | 返回ArkWeb\_Response的状态文本。此函数将为statusText字符串分配内存，调用方必须通过OH\_ArkWeb\_ReleaseString释放该字符串。 |

### OH\_ArkWebResponse\_SetMimeType()

```c
int32_t OH_ArkWebResponse_SetMimeType(ArkWeb_Response* response, const char* mimeType)
```

**描述：**

为ArkWeb\_Response设置媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| const char\* mimeType | 响应的媒体类型。设置媒体类型会告诉客户端响应内容的类型，例如：text/html表示HTML文档、application/json表示JSON数据、image/png表示PNG图片等，浏览器会根据媒体类型选择合适的渲染方式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetMimeType()

```c
void OH_ArkWebResponse_GetMimeType(const ArkWeb_Response* response, char** mimeType)
```

**描述：**

获取ArkWeb\_Response的媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| char\*\* mimeType | 返回ArkWeb\_Response的媒体类型。此函数将为mimeType字符串分配内存，调用方必须通过OH\_ArkWeb\_ReleaseString释放该字符串。 |

### OH\_ArkWebResponse\_SetCharset()

```c
int32_t OH_ArkWebResponse_SetCharset(ArkWeb_Response* response, const char* charset)
```

**描述：**

为ArkWeb\_Response设置字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| const char\* charset | 响应的字符集。设置字符集会告诉客户端响应内容使用的字符编码，例如：UTF-8表示使用UTF-8编码、GBK表示使用GBK编码等，浏览器会根据字符集正确解析和显示文本内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetCharset()

```c
void OH_ArkWebResponse_GetCharset(const ArkWeb_Response* response, char** charset)
```

**描述：**

获取ArkWeb\_Response的字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| char\*\* charset | 返回ArkWeb\_Response的字符集。此函数将为charset字符串分配内存，调用方必须通过OH\_ArkWeb\_ReleaseString释放字符串。 |

### OH\_ArkWebResponse\_SetHeaderByName()

```c
int32_t OH_ArkWebResponse_SetHeaderByName(ArkWeb_Response* response,const char* name,const char* value,bool overwrite)
```

**描述：**

为ArkWeb\_Response设置一个header。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| const char\* name | header的名称。指定要设置的HTTP响应头名称，例如：Content-Type、Content-Length、Cache-Control等，不同的header会影响浏览器如何处理响应。 |
| const char\* value | header的值。指定HTTP响应头的值，例如：对于Content-Type可以设置为text/html、对于Cache-Control可以设置为no-cache等，实际效果取决于header的名称和值的组合。 |
| bool overwrite | 如果为true，将覆盖现有的header，否则不覆盖。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResponse\_GetHeaderByName()

```c
void OH_ArkWebResponse_GetHeaderByName(const ArkWeb_Response* response, const char* name, char** value)
```

**描述：**

从ArkWeb\_Response中获取header。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | ArkWeb\_Response。 |
| const char\* name | header的名称。 |
| char\*\* value | 返回header的值。此函数将为value字符串分配内存，调用方必须通过OH\_ArkWeb\_ReleaseString释放该字符串。 |

### OH\_ArkWebResourceHandler\_Destroy()

```c
int32_t OH_ArkWebResourceHandler_Destroy(const ArkWeb_ResourceHandler* resourceHandler)
```

**描述：**

销毁一个ArkWeb\_ResourceHandler对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | ArkWeb\_ResourceHandler。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceHandler\_DidReceiveResponse()

```c
int32_t OH_ArkWebResourceHandler_DidReceiveResponse(const ArkWeb_ResourceHandler* resourceHandler,const ArkWeb_Response* response)
```

**描述：**

将构造的响应头传递给被拦截的请求。在拦截请求并准备返回自定义响应时调用，用于设置HTTP响应状态码、媒体类型、字符集等响应头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | 该请求的ArkWeb\_ResourceHandler。 |
| const [ArkWeb\_Response](capi-web-arkweb-response.md)\* response | 该拦截请求的ArkWeb\_Response。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceHandler\_DidReceiveData()

```c
int32_t OH_ArkWebResourceHandler_DidReceiveData(const ArkWeb_ResourceHandler* resourceHandler,const uint8_t* buffer,int64_t bufLen)
```

**描述：**

将构造的响应体传递给被拦截的请求。在设置响应头后调用，用于发送响应数据。可以多次调用来分块传输数据，在传输完成后需调用OH\_ArkWebResourceHandler\_DidFinish通知请求结束。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | 该请求的ArkWeb\_ResourceHandler。 |
| const uint8\_t\* buffer | 要发送的buffer数据。 |
| int64\_t bufLen | buffer的大小，单位：字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceHandler\_DidFinish()

```c
int32_t OH_ArkWebResourceHandler_DidFinish(const ArkWeb_ResourceHandler* resourceHandler)
```

**描述：**

通知ArkWeb内核被拦截的请求已经完成，并且没有更多的数据可用。该函数向内核发送完成信号，内核将结束该请求的处理，并清理相关的内部资源。调用此函数后，不能再对该请求调用其他处理函数。如果请求过程中发生错误，应使用OH\_ArkWebResourceHandler\_DidFailWithError通知内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | 该请求的ArkWeb\_ResourceHandler。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceHandler\_DidFailWithError()

```c
int32_t OH_ArkWebResourceHandler_DidFailWithError(const ArkWeb_ResourceHandler* resourceHandler,ArkWeb_NetError errorCode)
```

**描述：**

通知ArkWeb内核，被拦截的请求应该失败。在权限验证失败、资源不存在、网络错误等场景下调用，用于标记请求失败并通过错误码告知客户端具体失败原因。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | 用于被拦截的URL请求。可以通过ArkWeb\_ResourceHandler发送自定义响应头以及自定义响应体。 |
| [ArkWeb\_NetError](capi-arkweb-net-error-list-h.md#arkweb_neterror) errorCode | 该请求的错误码。请参考[arkweb\_net\_error\_list.h](capi-arkweb-net-error-list-h.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWebResourceHandler\_DidFailWithErrorV2()

```c
int32_t OH_ArkWebResourceHandler_DidFailWithErrorV2(const ArkWeb_ResourceHandler* resourceHandler,ArkWeb_NetError errorCode,bool completeIfNoResponse)
```

**描述：**

通知ArkWeb内核，被拦截的请求应该失败。对比[OH\_ArkWebResourceHandler\_DidFailWithError](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfailwitherror)接口，新增参数completeIfNoResponse，值为true时，若之前未调用过[OH\_ArkWebResourceHandler\_DidReceiveResponse](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)，则会自动生成一个response以完成此次网络请求，网络错误码为-104；值为false时，将等待应用调用[OH\_ArkWebResourceHandler\_DidReceiveResponse](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)并传入response，不会直接完成此次网络请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_ResourceHandler](capi-web-arkweb-resourcehandler.md)\* resourceHandler | 用于被拦截的URL请求。可以通过ArkWeb\_ResourceHandler发送自定义响应头以及自定义响应体。 |
| [ArkWeb\_NetError](capi-arkweb-net-error-list-h.md#arkweb_neterror) errorCode | 该请求的错误码。请参考[arkweb\_net\_error\_list.h](capi-arkweb-net-error-list-h.md)。 |
| bool completeIfNoResponse | 若之前未调用过[OH\_ArkWebResourceHandler\_DidReceiveResponse](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)，调用[OH\_ArkWebResourceHandler\_DidFailWithErrorV2](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didfailwitherrorv2)时，此次网络请求是否完成；值为true时，若之前未调用过[OH\_ArkWebResourceHandler\_DidReceiveResponse](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)，则会自动生成一个response以完成此次网络请求，网络错误码为-104；值为false时，将等待应用调用[OH\_ArkWebResourceHandler\_DidReceiveResponse](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcehandler_didreceiveresponse)并传入response，不会直接完成此次网络请求。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果返回0，表示成功；返回17100101，表示参数无效。 |

### OH\_ArkWeb\_ReleaseString()

```c
void OH_ArkWeb_ReleaseString(char* string)
```

**描述：**

释放由NDK接口创建的字符串。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* string | 待释放的字符串。 |

### OH\_ArkWeb\_ReleaseByteArray()

```c
void OH_ArkWeb_ReleaseByteArray(uint8_t* byteArray)
```

**描述：**

释放由NDK接口创建的字节数组。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t\* byteArray | 待释放的字节数组。 |
