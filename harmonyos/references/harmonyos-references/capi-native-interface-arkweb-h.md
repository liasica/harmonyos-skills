---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-arkweb-h
title: native_interface_arkweb.h
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 头文件 > native_interface_arkweb.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a9e8fa9913d97c8b939f9f98bff1ab0e1703e1dbc69f77bc88543e18dca0e81
---

## 概述

PhonePC/2in1TabletTVWearable

声明API接口供开发者使用注入对象和执行JavaScript代码等功能。

**引用文件：** <web/native\_interface\_arkweb.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**相关模块：** [Web](capi-web.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_BlanklessInfo](capi-web-arkweb-blanklessinfo.md) | ArkWeb\_BlanklessInfo | 页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，预测错误码，应用需根据此信息来决策是否启用无白屏加载插帧方案。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWebEngineVersion](capi-native-interface-arkweb-h.md#arkwebengineversion) | ArkWebEngineVersion | ArkWeb内核版本，请参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*NativeArkWeb\_OnJavaScriptCallback)(const char\*)](capi-native-interface-arkweb-h.md#nativearkweb_onjavascriptcallback) | NativeArkWeb\_OnJavaScriptCallback | 定义执行JavaScript代码后返回结果的回调函数的类型。 |
| [typedef char\* (\*NativeArkWeb\_OnJavaScriptProxyCallback)(const char\*\* argv, int32\_t argc)](capi-native-interface-arkweb-h.md#nativearkweb_onjavascriptproxycallback) | NativeArkWeb\_OnJavaScriptProxyCallback | 定义注入对象的回调函数的类型。 |
| [typedef void (\*NativeArkWeb\_OnValidCallback)(const char\*)](capi-native-interface-arkweb-h.md#nativearkweb_onvalidcallback) | NativeArkWeb\_OnValidCallback | 定义Web组件可用时的回调函数的类型。 |
| [typedef void (\*NativeArkWeb\_OnDestroyCallback)(const char\*)](capi-native-interface-arkweb-h.md#nativearkweb_ondestroycallback) | NativeArkWeb\_OnDestroyCallback | 定义Web组件销毁时的回调函数的类型。 |
| [typedef void (\*OH\_ArkWeb\_OnCookieSaveCallback)(ArkWeb\_ErrorCode errorCode)](capi-native-interface-arkweb-h.md#oh_arkweb_oncookiesavecallback) | OH\_ArkWeb\_OnCookieSaveCallback | 定义保存cookie的回调函数的类型。  **起始版本：** 20 |
| [void OH\_NativeArkWeb\_RunJavaScript(const char\* webTag, const char\* jsCode, NativeArkWeb\_OnJavaScriptCallback callback)](capi-native-interface-arkweb-h.md#oh_nativearkweb_runjavascript) | - | 在当前显示页面的环境下，加载并异步执行一段JavaScript代码。 |
| [void OH\_NativeArkWeb\_RegisterJavaScriptProxy(const char\* webTag, const char\* objName, const char\*\* methodList,NativeArkWeb\_OnJavaScriptProxyCallback\* callback, int32\_t size, bool needRefresh)](capi-native-interface-arkweb-h.md#oh_nativearkweb_registerjavascriptproxy) | - | 注册对象及函数名称列表。 |
| [void OH\_NativeArkWeb\_UnregisterJavaScriptProxy(const char\* webTag, const char\* objName)](capi-native-interface-arkweb-h.md#oh_nativearkweb_unregisterjavascriptproxy) | - | 删除已注册的对象及其下的回调函数。 |
| [void OH\_NativeArkWeb\_SetJavaScriptProxyValidCallback(const char\* webTag, NativeArkWeb\_OnValidCallback callback)](capi-native-interface-arkweb-h.md#oh_nativearkweb_setjavascriptproxyvalidcallback) | - | 设置对象可注册时的回调函数。 |
| [NativeArkWeb\_OnValidCallback OH\_NativeArkWeb\_GetJavaScriptProxyValidCallback(const char\* webTag)](capi-native-interface-arkweb-h.md#oh_nativearkweb_getjavascriptproxyvalidcallback) | - | 获取已注册的对象可注册时的回调函数。 |
| [void OH\_NativeArkWeb\_SetDestroyCallback(const char\* webTag, NativeArkWeb\_OnDestroyCallback callback)](capi-native-interface-arkweb-h.md#oh_nativearkweb_setdestroycallback) | - | 设置组件销毁时的回调函数。 |
| [NativeArkWeb\_OnDestroyCallback OH\_NativeArkWeb\_GetDestroyCallback(const char\* webTag)](capi-native-interface-arkweb-h.md#oh_nativearkweb_getdestroycallback) | - | 获取已注册的组件销毁时的回调函数。 |
| [ArkWeb\_ErrorCode OH\_NativeArkWeb\_LoadData(const char\* webTag,const char\* data,const char\* mimeType,const char\* encoding,const char\* baseUrl,const char\* historyUrl)](capi-native-interface-arkweb-h.md#oh_nativearkweb_loaddata) | - | 加载数据或URL，此函数应在主线程中调用。 |
| [void OH\_NativeArkWeb\_RegisterAsyncThreadJavaScriptProxy(const char\* webTag,const ArkWeb\_ProxyObjectWithResult\* proxyObject, const char\* permission)](capi-native-interface-arkweb-h.md#oh_nativearkweb_registerasyncthreadjavascriptproxy) | - | 注册一个包含回调方法的 JavaScript 对象，这些方法可带有返回值。该对象将被注入到当前页面的所有frame中，包括所有的 iframe，并且可以通过在 ArkWeb\_ProxyObjectWithResult 中指定的名称进行访问。该对象只会在下一次加载或重新加载页面后在 JavaScript 中生效。这些方法将在 ArkWeb 的工作线程中执行。 |
| [ArkWeb\_ErrorCode OH\_ArkWebCookieManager\_SaveCookieSync()](capi-native-interface-arkweb-h.md#oh_arkwebcookiemanager_savecookiesync) | - | 将当前可通过CookieManager API访问的所有Cookie持久化到磁盘。如果要在非UI线程中使用此接口，则需要先使用OH\_ArkWeb\_GetNativeAPI初始化CookieManager接口。  **起始版本：** 20 |
| [void OH\_ArkWebCookieManager\_SaveCookieAsync(OH\_ArkWeb\_OnCookieSaveCallback callback)](capi-native-interface-arkweb-h.md#oh_arkwebcookiemanager_savecookieasync) | - | 将当前可通过CookieManager API访问的所有Cookie持久化到磁盘。在不初始化CookieManager接口的情况下，此接口将在UI线程上自动执行。  **起始版本：** 20 |
| [ArkWeb\_BlanklessInfo OH\_NativeArkWeb\_GetBlanklessInfoWithKey(const char\* webTag, const char\* key)](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey) | - | 获取页面首屏加载预测信息（详细说明见[ArkWeb\_BlanklessInfo](capi-web-arkweb-blanklessinfo.md)），并开始本次加载过渡帧生成，应用根据此信息确定是否需要启用无白屏加载。必须与[OH\_NativeArkWeb\_SetBlanklessLoadingWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingwithkey)接口配套使用，并且必须在触发加载页面的接口之前调用。需在WebViewController与Web组件绑定后才能使用。 |
| [ArkWeb\_BlanklessErrorCode OH\_NativeArkWeb\_SetBlanklessLoadingWithKey(const char\* webTag, const char\* key, bool isStarted)](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingwithkey) | - | 设置无白屏加载是否启用。本接口必须与[OH\_NativeArkWeb\_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey)接口配套使用。 |
| [void OH\_NativeArkWeb\_ClearBlanklessLoadingCache(const char\* key[], uint32\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-arkweb-h#oh_nativearkweb_clearblanklessloadingcache) | - | 清除指定key值页面无白屏优化缓存，本接口只清除缓存。 |
| [uint32\_t OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity(uint32\_t capacity)](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingcachecapacity) | - | 设置无白屏加载方案的持久化缓存容量，返回实际生效值。默认缓存容量为30MB，最大值为100MB。当实际缓存超过容量时，将采用淘汰不常用的过渡帧的方式清理。 |
| [void OH\_NativeArkWeb\_SetActiveWebEngineVersion(ArkWebEngineVersion webEngineVersion)](capi-native-interface-arkweb-h.md#oh_nativearkweb_setactivewebengineversion) | - | 设置ArkWeb内核版本。若系统不支持指定版本，则设置无效。该接口为全局静态方法，须在调用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。 |
| [ArkWebEngineVersion OH\_NativeArkWeb\_GetActiveWebEngineVersion()](capi-native-interface-arkweb-h.md#oh_nativearkweb_getactivewebengineversion) | - | 获取当前使用的ArkWeb内核版本。 |
| [bool OH\_NativeArkWeb\_IsActiveWebEngineEvergreen()](capi-native-interface-arkweb-h.md#oh_nativearkweb_isactivewebengineevergreen) | - | 判断应用所使用ArkWeb内核是否是常青内核，即系统的最新内核。 |
| [void OH\_NativeArkWeb\_LazyInitializeWebEngineInCookieManager(bool lazy)](capi-native-interface-arkweb-h.md#oh_nativearkweb_lazyinitializewebengineincookiemanager) | - | 设置是否延后初始化ArkWeb内核，不调用该方法时，默认不延后初始化ArkWeb内核。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkWebEngineVersion

PhonePC/2in1TabletTVWearable

```
1. enum ArkWebEngineVersion
```

**描述：**

ArkWeb内核版本，请参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)。

| **内核类型** | **英文** | **说明** |
| --- | --- | --- |
| 常青内核 | EVERGREEN WebCore | 当前系统的最新Web内核，系统基于此内核进行完整的功能实现，推荐应用使用。 |
| 遗留内核 | LEGACY WebCore | 复用上一版本的内核，只做安全补丁及舆情问题修复，仅作为兼容性回滚使用，且遗留内核的支持有时间限制。 |

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| SYSTEM\_DEFAULT = 0 | 系统默认内核，HarmonyOS 6.0版本默认为M132。 |
| ARKWEB\_M114 = 1 | HarmonyOS 6.0版本的遗留内核。开发者可选择此遗留内核，若系统版本上不存在此内核则设置无效。 |
| ARKWEB\_M132 = 2 | HarmonyOS 6.0版本的常青内核，M132为此版本的默认内核。若系统版本上不存在此内核则设置无效。 |
| ARKWEB\_EVERGREEN = 99999 | 常青内核，系统的最新内核。开发者可选择在每个系统版本上都使用最新的内核，HarmonyOS 6.1及之后所有系统版本都生效。  **起始版本：** 23 |

## 函数说明

PhonePC/2in1TabletTVWearable

### NativeArkWeb\_OnJavaScriptCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*NativeArkWeb_OnJavaScriptCallback)(const char*)
```

**描述：**

定义执行JavaScript代码后返回结果的回调函数的类型。

**起始版本：** 11

### NativeArkWeb\_OnJavaScriptProxyCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef char* (*NativeArkWeb_OnJavaScriptProxyCallback)(const char** argv, int32_t argc)
```

**描述：**

定义注入对象的回调函数的类型。

**起始版本：** 11

### NativeArkWeb\_OnValidCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*NativeArkWeb_OnValidCallback)(const char*)
```

**描述：**

定义Web组件可用时的回调函数的类型。

**起始版本：** 11

### NativeArkWeb\_OnDestroyCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*NativeArkWeb_OnDestroyCallback)(const char*)
```

**描述：**

定义Web组件销毁时的回调函数的类型。

**起始版本：** 11

### OH\_ArkWeb\_OnCookieSaveCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_ArkWeb_OnCookieSaveCallback)(ArkWeb_ErrorCode errorCode)
```

**描述：**

定义保存cookie的回调函数的类型。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) errorCode | [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 保存cookie成功。  [ARKWEB\_COOKIE\_SAVE\_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode) 保存cookie失败。  [ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode) CookieManager初始化失败。 |

### OH\_NativeArkWeb\_RunJavaScript()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_RunJavaScript(const char* webTag, const char* jsCode, NativeArkWeb_OnJavaScriptCallback callback)
```

**描述：**

在当前显示页面的环境下，加载并异步执行一段JavaScript代码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| const char\* jsCode | 一段JavaScript的代码脚本。 |
| [NativeArkWeb\_OnJavaScriptCallback](capi-native-interface-arkweb-h.md#nativearkweb_onjavascriptcallback) callback | 代码执行完后通知开发者结果的回调函数。 |

### OH\_NativeArkWeb\_RegisterJavaScriptProxy()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_RegisterJavaScriptProxy(const char* webTag, const char* objName, const char** methodList,NativeArkWeb_OnJavaScriptProxyCallback* callback, int32_t size, bool needRefresh)
```

**描述：**

注册对象及函数名称列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| const char\* objName | 注入对象的名称。 |
| const char\*\* methodList | 注入函数列表的名称。 |
| [NativeArkWeb\_OnJavaScriptProxyCallback](capi-native-interface-arkweb-h.md#nativearkweb_onjavascriptproxycallback)\* callback | 注入的回调函数。 |
| int32\_t size | 注入的回调函数的个数。 |
| bool needRefresh | 是否需要刷新页面。true：刷新页面，false：不刷新页面。 |

### OH\_NativeArkWeb\_UnregisterJavaScriptProxy()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_UnregisterJavaScriptProxy(const char* webTag, const char* objName)
```

**描述：**

删除已注册的对象及其下的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| const char\* objName | 注入对象的名称。 |

### OH\_NativeArkWeb\_SetJavaScriptProxyValidCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_SetJavaScriptProxyValidCallback(const char* webTag, NativeArkWeb_OnValidCallback callback)
```

**描述：**

设置对象可注册时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| [NativeArkWeb\_OnValidCallback](capi-native-interface-arkweb-h.md#nativearkweb_onvalidcallback) callback | 对象可注册时的回调函数。 |

### OH\_NativeArkWeb\_GetJavaScriptProxyValidCallback()

PhonePC/2in1TabletTVWearable

```
1. NativeArkWeb_OnValidCallback OH_NativeArkWeb_GetJavaScriptProxyValidCallback(const char* webTag)
```

**描述：**

获取已注册的对象可注册时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeArkWeb\_OnValidCallback](capi-native-interface-arkweb-h.md#nativearkweb_onvalidcallback) | 已注册的对象可注册时的回调函数。如果未设置由参数webTag指定的有效回调函数，则将返回空指针。 |

### OH\_NativeArkWeb\_SetDestroyCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_SetDestroyCallback(const char* webTag, NativeArkWeb_OnDestroyCallback callback)
```

**描述：**

设置组件销毁时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| [NativeArkWeb\_OnDestroyCallback](capi-native-interface-arkweb-h.md#nativearkweb_ondestroycallback) callback | 组件销毁时的回调函数。 |

### OH\_NativeArkWeb\_GetDestroyCallback()

PhonePC/2in1TabletTVWearable

```
1. NativeArkWeb_OnDestroyCallback OH_NativeArkWeb_GetDestroyCallback(const char* webTag)
```

**描述：**

获取已注册的组件销毁时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeArkWeb\_OnDestroyCallback](capi-native-interface-arkweb-h.md#nativearkweb_ondestroycallback) | 返回已注册的组件销毁时的回调函数。如果未设置由参数webTag指定的销毁回调函数，则将返回空指针。 |

### OH\_NativeArkWeb\_LoadData()

PhonePC/2in1TabletTVWearable

```
1. ArkWeb_ErrorCode OH_NativeArkWeb_LoadData(const char* webTag,const char* data,const char* mimeType,const char* encoding,const char* baseUrl,const char* historyUrl)
```

**描述：**

加载数据或URL，此函数应在主线程中调用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| const char\* data | "Base64"或"URL"编码的字符串，不能为空。 |
| const char\* mimeType | 媒体类型，例如"text/html"，不能为空。 |
| const char\* encoding | 编码类型，例如"UTF-8"，不能为空。 |
| const char\* baseUrl | 指定的URL路径("http"/"https"/"data"协议),由Web组件分配给window.origin。 |
| const char\* historyUrl | 历史URL，当它不为空时，可以通过历史记录来管理，实现前进和后退功能。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | LoadData 错误码。  [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 加载数据成功。  [ARKWEB\_INVALID\_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode) 必填参数未指定或参数类型不正确或参数校验失败。  [ARKWEB\_INIT\_ERROR](capi-arkweb-error-code-h.md#arkweb_errorcode) 初始化失败，根据传入的"webTag"找不到有效的Web组件。  [ARKWEB\_LIBRARY\_OPEN\_FAILURE](capi-arkweb-error-code-h.md#arkweb_errorcode) 打开动态链接库失败。  [ARKWEB\_LIBRARY\_SYMBOL\_NOT\_FOUND](capi-arkweb-error-code-h.md#arkweb_errorcode) 动态链接库中未找到所需的符号。 |

### OH\_NativeArkWeb\_RegisterAsyncThreadJavaScriptProxy()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_RegisterAsyncThreadJavaScriptProxy(const char* webTag,const ArkWeb_ProxyObjectWithResult* proxyObject, const char* permission)
```

**描述：**

注册一个包含回调方法的 JavaScript 对象，这些方法可带有返回值。该对象将被注入到当前页面的所有frame中，包括所有的 iframe，并且可以通过在 ArkWeb\_ProxyObjectWithResult 中指定的名称进行访问。该对象只会在下一次加载或重新加载页面后在 JavaScript 中生效。这些方法将在 ArkWeb 的工作线程中执行。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_ProxyObjectWithResult](capi-web-arkweb-proxyobjectwithresult.md)\* proxyObject | 注册的对象。 |
| const char\* permission | json格式字符串，默认值为空。该字符串用来配置JSBridge的权限限制，可以配置对象和方法级别。 |

### OH\_ArkWebCookieManager\_SaveCookieSync()

PhonePC/2in1TabletTVWearable

```
1. ArkWeb_ErrorCode OH_ArkWebCookieManager_SaveCookieSync()
```

**描述：**

将当前可通过CookieManager API访问的所有Cookie持久化到磁盘。如果要在非UI线程中使用此接口，则需要先使用OH\_ArkWeb\_GetNativeAPI初始化CookieManager接口。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | SaveCookieSync错误码。  [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 保存cookie成功。  [ARKWEB\_COOKIE\_SAVE\_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode) 保存cookie失败。  [ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode) CookieManager初始化失败。  [ARKWEB\_COOKIE\_MANAGER\_NOT\_INITIALIZED](capi-arkweb-error-code-h.md#arkweb_errorcode) 在非UI线程中，不允许在不初始化CookieManager接口的情况下调用该接口。请先使用OH\_ArkWeb\_GetNativeAPI初始化CookieManager接口。 |

### OH\_ArkWebCookieManager\_SaveCookieAsync()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkWebCookieManager_SaveCookieAsync(OH_ArkWeb_OnCookieSaveCallback callback)
```

**描述：**

将当前可通过CookieManager API访问的所有Cookie持久化到磁盘。在不初始化CookieManager接口的情况下，此接口将在UI线程上自动执行。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkWeb\_OnCookieSaveCallback](capi-native-interface-arkweb-h.md#oh_arkweb_oncookiesavecallback)\* callback | 保存cookie完成后执行该回调。 |

### OH\_NativeArkWeb\_GetBlanklessInfoWithKey()

PhonePC/2in1TabletTVWearable

```
1. ArkWeb_BlanklessInfo OH_NativeArkWeb_GetBlanklessInfoWithKey(const char* webTag, const char* key)
```

**描述：**

获取页面首屏加载预测信息（详细说明见[ArkWeb\_BlanklessInfo](capi-web-arkweb-blanklessinfo.md)），并开始本次加载过渡帧生成，应用根据此信息确定是否需要启用无白屏加载。必须与[OH\_NativeArkWeb\_SetBlanklessLoadingWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingwithkey)接口配套使用，并且必须在触发加载页面的接口之前调用。需在WebViewController与Web组件绑定后才能使用。

说明

* 持久缓存容量：默认大小为30MB（约30页），可以通过接口[OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingcachecapacity)设置缓存容量，具体见该接口说明。超过容量时根据LRU（Least Recently Used，淘汰不常用缓存的策略）机制更新缓存。自动清理超过7天的持久缓存数据，缓存清除后第三次加载页面开始有优化效果。
* 如果发现相似度（即[ArkWeb\_BlanklessInfo](capi-web-arkweb-blanklessinfo.md)中的similarity）极低，请检查key值是否正确传递。
* 调用本接口后，会启用页面加载快照检测及生成过渡帧计算，产生一定资源开销。
* 启用无白屏加载的页面会带来一定的资源开销，开销的大小与Web组件的分辨率相关。假设分辨率的宽度和高度分别为：w, h。页面在打开阶段会增加峰值内存，增加量约为12wh B。页面打开后，内存会被回收，不影响稳态内存。增加固态应用缓存的大小，每个页面增加的缓存约w\*h/10 B，缓存位于应用缓存的位置。

**需要权限：** ohos.permission.INTERNET和ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 20

**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const char\* key | 唯一标识本页面的key值。  合法取值范围：非空，长度不超过2048个字符。  设置非法值时不生效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_BlanklessInfo](capi-web-arkweb-blanklessinfo.md) | 页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，应用需根据此信息来决策是否启用无白屏加载插帧。 |

### OH\_NativeArkWeb\_SetBlanklessLoadingWithKey()

PhonePC/2in1TabletTVWearable

```
1. ArkWeb_BlanklessErrorCode OH_NativeArkWeb_SetBlanklessLoadingWithKey(const char* webTag, const char* key, bool isStarted)
```

**描述：**

设置无白屏加载是否启用。本接口必须与[OH\_NativeArkWeb\_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey)接口配套使用。

说明

* 需在触发页面加载的接口之后调用。其他约束同[OH\_NativeArkWeb\_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey)。
* 页面的加载必须在调用本套接口的组件中进行。
* 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。

**需要权限：** ohos.permission.INTERNET和ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const char\* key | 唯一标识本页面的key值。必须与[OH\_NativeArkWeb\_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey)接口的key值相同。  合法取值范围：非空，长度不超过2048个字符。  非法值设置行为：返回错误码[ArkWeb\_BlanklessErrorCode](capi-arkweb-error-code-h.md#arkweb_blanklesserrorcode)，插帧不生效。 |
| bool isStarted | 是否启用开始插帧，true：启用，false：不启用。  默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_BlanklessErrorCode](capi-arkweb-error-code-h.md#arkweb_blanklesserrorcode) | 返回接口调用是否成功，具体见[ArkWeb\_BlanklessErrorCode](capi-arkweb-error-code-h.md#arkweb_blanklesserrorcode)定义。 |

### OH\_NativeArkWeb\_ClearBlanklessLoadingCache()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_ClearBlanklessLoadingCache(const char* key[], uint32_t size)
```

**描述：**

清除指定key值页面无白屏优化缓存，本接口只清除缓存。

在小程序或Web应用场景中，当页面加载时内容变化显著，可能会出现一次明显的跳变。若对此跳变有所顾虑，可使用该接口清除页面缓存。

说明

* 清除之后的页面，需在第三次加载页面时才会产生优化效果。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* key[] | 清除Blankless优化方案页面的key值列表，key值为[OH\_NativeArkWeb\_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey)中指定过的。  默认值：所有Blankless优化方案缓存的页面key列表。  合法取值范围：长度不超过2048，key列表长度<=100。key和加载页面时输入给ArkWeb的相同。  非法值设置行为：key长度超过2048时该key不生效；长度超过100时，取前100个；当为NULL时，使用默认值。 |
| uint32\_t size | keys数组的大小。  默认值：0。  合法取值范围：0~100。取值超过100时，keys数组取前100个。  非法值设置行为：0。 |

### OH\_NativeArkWeb\_SetBlanklessLoadingCacheCapacity()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_NativeArkWeb_SetBlanklessLoadingCacheCapacity(uint32_t capacity)
```

**描述：**

设置无白屏加载方案的持久化缓存容量，返回实际生效值。默认缓存容量为30MB，最大值为100MB。当实际缓存超过容量时，将采用淘汰不常用的过渡帧的方式清理。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t capacity | 设置持久化缓存设置，单位MB，最大设置不超过100MB。  默认值：30MB。  合法取值范围：0~100，当设置为0时，无缓存空间，则功能全局不开启。  非法值设置行为：小于0时生效值为0，大于100时生效值为100。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回实际生效的容量值，范围0~100。  小于0时生效值为0，大于100时生效值为100。 |

### OH\_NativeArkWeb\_SetActiveWebEngineVersion()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_SetActiveWebEngineVersion(ArkWebEngineVersion webEngineVersion)
```

**描述：**

设置ArkWeb内核版本。若系统不支持指定版本，则设置无效。

该接口为全局静态方法，须在调用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。

**遗留内核适配：**

在HarmonyOS 6.0及以后，使用遗留内核时，部分ArkWeb接口不会生效，参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkWebEngineVersion webEngineVersion | ArkWeb内核版本（详细说明见[ArkWebEngineVersion](capi-native-interface-arkweb-h.md#arkwebengineversion)）。 |

### OH\_NativeArkWeb\_GetActiveWebEngineVersion()

PhonePC/2in1TabletTVWearable

```
1. ArkWebEngineVersion OH_NativeArkWeb_GetActiveWebEngineVersion()
```

**描述：**

获取当前使用的ArkWeb内核版本。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkWebEngineVersion | 返回由[ArkWebEngineVersion](capi-native-interface-arkweb-h.md#arkwebengineversion)枚举所定义的当前使用的ArkWeb内核版本。 |

### OH\_NativeArkWeb\_IsActiveWebEngineEvergreen()

PhonePC/2in1TabletTVWearable

```
1. bool OH_NativeArkWeb_IsActiveWebEngineEvergreen()
```

**描述：**

判断应用所使用ArkWeb内核是否是常青内核，即系统的最新内核。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 表示当前应用所使用内核是否为常青内核。true表示当前应用所使用内核是常青内核，false表示当前应用所使用内核不是常青内核。 |

### OH\_NativeArkWeb\_LazyInitializeWebEngineInCookieManager()

PhonePC/2in1TabletTVWearable

```
1. void OH_NativeArkWeb_LazyInitializeWebEngineInCookieManager(bool lazy)
```

**描述：**

设置是否延后初始化ArkWeb内核，不调用该方法时，默认不延后初始化ArkWeb内核。

说明

* 该接口为全局静态方法，须在使用ArkWeb组件和初始化ArkWeb内核前调用，否则该设置无效。
* 该接口仅适用于调用后会初始化CookieManager的接口，比如[ArkWeb\_CookieManagerAPI](capi-web-arkweb-cookiemanagerapi.md)的接口。调用本接口后，再调用适用的接口，会在初始化CookieManager时跳过初始化ArkWeb内核，后续需自行初始化ArkWeb内核。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool lazy | 是否延后初始化ArkWeb内核，true：延后，false：不延后。 |
