---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e
title: Enums
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Enums
category: harmonyos-references
scraped_at: 2026-09-02T15:01:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:98fed077000ef7fd382a6aadc77091c4e40553b01b0ecb0cb97ed8035a4c51ea
---

ArkWeb Enums模块是ArkWeb（Web子系统）的枚举类型定义集合，为WebView组件及其关联的API类提供统一的类型约束和状态描述能力。本模块定义了覆盖Web 页面交互、安全状态、DNS配置、下载任务、媒体播控、内核版本、进程模式、内存管理、离线资源、无白屏加载、站点隔离、软键盘行为、Cookie策略、滚动控制、设备形态等多领域的枚举类型，是整个WebView API体系的基础类型支撑层。

开发者在使用[模块描述](arkts-apis-webview.md)中的WebviewController、WebMessagePort、WebDownloadItem、NativeMediaPlayerHandler、NativeMediaPlayerBridge、WebSchemeHandlerRequest等核心类时，均需依赖本模块中的枚举类型来配置行为参数或解析返回结果。当开发者需要精细控制Web组件的运行模式、查询页面状态、处理下载任务、接入原生媒体播控或优化加载体验时，应查阅本模块中对应的枚举定义。

**说明** 

本模块首批接口从API version 9开始支持，后续版本的新增接口，则采用上角标单独标记接口的起始版本。

## WebHitTestType

指示光标命中的节点类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EditText | 0 | 可编辑的区域。 |
| Email | 1 | 电子邮件地址。 |
| HttpAnchor | 2 | 超链接，其中链接地址为http。 |
| HttpAnchorImg | 3 | 带有超链接的图片，其中链接地址为http + HTML::img。 |
| Img | 4 | HTML::img标签。 |
| Map | 5 | 地理地址。 |
| Phone | 6 | 电话号码。 |
| Unknown | 7 | 未知内容。 |

## SecureDnsMode10+

Web组件使用HTTPDNS的模式。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 不使用HTTPDNS，可以用于撤销之前使用的HTTPDNS配置。 |
| AUTO | 1 | 自动模式，用于解析的设定DNS服务器不可用时，可自动回落至系统DNS。 |
| SECURE\_ONLY | 2 | 强制使用设定的HTTPDNS服务器进行域名解析。 |

## SecurityLevel11+

当前网页的安全级别。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 页面既不绝对安全，也不是不安全，即是中立。例如，部分scheme非http/https的URL。 |
| SECURE | 1 | 页面安全，页面使用的是HTTPS协议，且使用了信任的证书。 |
| WARNING | 2 | 页面不安全。例如，使用HTTP协议或使用HTTPS协议但使用旧版TLS版本。 |
| DANGEROUS | 3 | 页面不安全。尝试HTTPS并失败、页面未通过身份验证、页面上包含不安全活动内容的HTTPS、恶意软件、网络钓鱼或任何其他可能危险的严重安全问题。 |

## MediaPlaybackState12+

当前网页的播放控制状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 页面无音视频启播。 |
| PLAYING | 1 | 页面音视频播放中。 |
| PAUSED | 2 | 页面音视频暂停。 |
| STOPPED | 3 | 页面音视频停止。 |

## PressureLevel14+

内存压力等级。在应用主动清理Web组件占用的缓存时，Web内核会根据内存压力等级，进行缓存释放。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEMORY\_PRESSURE\_LEVEL\_MODERATE | 1 | 中等内存压力等级。这个等级下，Web内核会尝试释放重新分配开销较小且不需要立即使用的缓存。 |
| MEMORY\_PRESSURE\_LEVEL\_CRITICAL | 2 | 严重内存压力等级。这个等级下，Web内核会尝试释放所有可能的内存缓存。 |

## WebMessageType10+

[WebMessagePort](arkts-apis-webview-webmessageport.md)接口所支持的数据类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_SUPPORT | 0 | 不支持的数据类型。 |
| STRING | 1 | 字符串类型。 |
| NUMBER | 2 | 数值类型。 |
| BOOLEAN | 3 | 布尔类型。 |
| ARRAY\_BUFFER | 4 | 原始二进制数据缓冲区。 |
| ARRAY | 5 | 数组类型。 |
| ERROR | 6 | 错误类型。 |

## JsMessageType10+

[runJavaScriptExt](arkts-apis-webview-webviewcontroller.md#runjavascriptext10)接口脚本执行后返回的结果的类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_SUPPORT | 0 | 不支持的数据类型。 |
| STRING | 1 | 字符串类型。 |
| NUMBER | 2 | 数值类型。 |
| BOOLEAN | 3 | 布尔类型。 |
| ARRAY\_BUFFER | 4 | 原始二进制数据缓冲区。 |
| ARRAY | 5 | 数组类型。 |

## RenderProcessMode12+

ArkWeb渲染子进程模式类型，可根据应用对内存占用与渲染进程隔离的需求选择对应的模式。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLE | 0 | ArkWeb单渲染子进程模式。该模式下，多个Web复用一个渲染子进程。 |
| MULTIPLE | 1 | ArkWeb多渲染子进程模式。该模式下，每个Web一个渲染子进程。 |

## OfflineResourceType12+

[OfflineResourceMap](arkts-apis-webview-i.md#offlineresourcemap12)对象对应的本地离线资源的接口类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE | 0 | 图片类型的资源。 |
| CSS | 1 | CSS类型的资源。 |
| CLASSIC\_JS | 2 | 通过<script src="" />标签加载的JavaScript资源。 |
| MODULE\_JS | 3 | 通过<script src="" type="module" />标签加载的JavaScript资源。 |

## ScrollType12+

Scroll滚动类型，用于[setScrollable](arkts-apis-webview-webviewcontroller.md#setscrollable12)。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT | 0 | 滚动事件，表示通过触摸屏、触摸板、鼠标滚轮生成的网页滚动。 |

## WebDownloadState11+

下载任务的状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IN\_PROGRESS | 0 | 下载任务正在进行中。 |
| COMPLETED | 1 | 下载任务已经完成。 |
| CANCELED | 2 | 下载任务已经被取消。 |
| INTERRUPTED | 3 | 下载任务被中断。 |
| PENDING | 4 | 下载任务等待开始。 |
| PAUSED | 5 | 下载任务已经被暂停。 |
| UNKNOWN | 6 | 下载任务未知状态。 |

## WebDownloadErrorCode11+

下载任务的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_UNKNOWN | 0 | 未知的错误。 |
| FILE\_FAILED | 1 | 常规文件操作失败。 |
| FILE\_ACCESS\_DENIED | 2 | 没有权限访问文件。 |
| FILE\_NO\_SPACE | 3 | 磁盘没有足够的空间。 |
| FILE\_NAME\_TOO\_LONG | 5 | 文件名过长。 |
| FILE\_TOO\_LARGE | 6 | 文件太大。 |
| FILE\_TRANSIENT\_ERROR | 10 | 出现了一些临时问题，例如内存不足、文件正在使用以及同时打开的文件过多。 |
| FILE\_BLOCKED | 11 | 由于某些本地策略，文件被阻止访问。 |
| FILE\_TOO\_SHORT | 13 | 当尝试恢复下载时，发现文件不够长，可能该文件已不存在。 |
| FILE\_HASH\_MISMATCH | 14 | 哈希不匹配。 |
| FILE\_SAME\_AS\_SOURCE | 15 | 文件已存在。 |
| NETWORK\_FAILED | 20 | 一般网络错误。 |
| NETWORK\_TIMEOUT | 21 | 网络超时。 |
| NETWORK\_DISCONNECTED | 22 | 网络断开连接。 |
| NETWORK\_SERVER\_DOWN | 23 | 服务器关闭。 |
| NETWORK\_INVALID\_REQUEST | 24 | 无效的网络请求，可能重定向到不支持的方案或无效的URL。 |
| SERVER\_FAILED | 30 | 服务器返回了一个一般性错误。 |
| SERVER\_NO\_RANGE | 31 | 服务器不支持范围请求。 |
| SERVER\_BAD\_CONTENT | 33 | 服务器没有请求的数据。 |
| SERVER\_UNAUTHORIZED | 34 | 服务器不允许下载该文件。 |
| SERVER\_CERT\_PROBLEM | 35 | 服务器证书错误。 |
| SERVER\_FORBIDDEN | 36 | 服务器访问被禁止。 |
| SERVER\_UNREACHABLE | 37 | 无法访问服务器。 |
| SERVER\_CONTENT\_LENGTH\_MISMATCH | 38 | 接收到的数据与内容长度不匹配。 |
| SERVER\_CROSS\_ORIGIN\_REDIRECT | 39 | 发生意外的跨站重定向。 |
| USER\_CANCELED | 40 | 用户取消了下载。 |
| USER\_SHUTDOWN | 41 | 用户关闭了应用。 |
| CRASH | 50 | 应用发生了崩溃。 |

## WebResourceType12+

资源请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MAIN\_FRAME | 0 | 顶层页面。 |
| SUB\_FRAME | 1 | Frame或Iframe。 |
| STYLE\_SHEET | 2 | CSS样式表。 |
| SCRIPT | 3 | 外部脚本。 |
| IMAGE | 4 | 图片（jpg/gif/png/以及其他）。 |
| FONT\_RESOURCE | 5 | 字体。 |
| SUB\_RESOURCE | 6 | 其他子资源。如果实际类型未知，则是默认类型。 |
| OBJECT | 7 | 插件的Object（或embed）标签，或者插件请求的资源。 |
| MEDIA | 8 | 媒体资源。 |
| WORKER | 9 | 专用工作线程的主资源。 |
| SHARED\_WORKER | 10 | 共享工作线程的主资源。 |
| PREFETCH | 11 | 明确的预取请求。 |
| FAVICON | 12 | 网站图标。 |
| XHR | 13 | XMLHttpRequest。 |
| PING | 14 | <a ping>/sendBeacon的Ping请求。 |
| SERVICE\_WORKER | 15 | service worker的主资源。 |
| CSP\_REPORT | 16 | 内容安全策略违规报告。 |
| PLUGIN\_RESOURCE | 17 | 插件请求的资源。 |
| NAVIGATION\_PRELOAD\_MAIN\_FRAME | 19 | 触发service worker预热的主frame跳转请求。 |
| NAVIGATION\_PRELOAD\_SUB\_FRAME | 20 | 触发service worker预热的子frame跳转请求。 |

## PlaybackStatus12+

[handleStatusChanged](arkts-apis-webview-nativemediaplayerhandler.md#handlestatuschanged12) 接口参数， 用于表示播放器的播放状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAUSED | 0 | 表示媒体已暂停。 |
| PLAYING | 1 | 表示媒体正在播放。 |

## NetworkState12+

播放器的网络状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EMPTY | 0 | 播放器还没有开始下载数据。 |
| IDLE | 1 | 播放器网络状态空闲，比如媒体分片下载完成，下一个分片还没有开始下载。 |
| LOADING | 2 | 播放器正在下载媒体数据。 |
| NETWORK\_ERROR | 3 | 发生了网络错误。 |

## ReadyState12+

播放器的缓存状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HAVE\_NOTHING | 0 | 没有缓存。 |
| HAVE\_METADATA | 1 | 只缓存了媒体元数据。 |
| HAVE\_CURRENT\_DATA | 2 | 只缓存到当前的播放进度。 |
| HAVE\_FUTURE\_DATA | 3 | 缓存时长超过了当前的播放进度，但是仍有可能导致卡顿。 |
| HAVE\_ENOUGH\_DATA | 4 | 缓存了足够的数据，保证播放流畅。 |

## MediaError12+

播放器的错误类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NETWORK\_ERROR | 1 | 网络错误。 |
| FORMAT\_ERROR | 2 | 媒体格式错误。 |
| DECODE\_ERROR | 3 | 解码错误。 |

## SuspendType12+

表示播放器的挂起类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENTER\_BACK\_FORWARD\_CACHE | 0 | 页面进入BFCache。 |
| ENTER\_BACKGROUND | 1 | 页面进入后台。 |
| AUTO\_CLEANUP | 2 | 系统自动清理。 |

## MediaType12+

表示媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO | 0 | 视频。 |
| AUDIO | 1 | 音频。 |

## SourceType12+

表示媒体源的类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| URL | 0 | 媒体源的类型是URL。 |
| MSE | 1 | 媒体源的类型是blob。 |

## Preload12+

播放器预加载媒体数据。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不预加载。 |
| METADATA | 1 | 只预加载媒体的元数据。 |
| AUTO | 2 | 预加载足够多的媒体数据，以保证能流畅地播放。 |

## ProxySchemeFilter15+

使用代理的请求的scheme信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MATCH\_ALL\_SCHEMES | 0 | 所有的scheme都会使用代理。 |
| MATCH\_HTTP | 1 | HTTP请求会使用代理。 |
| MATCH\_HTTPS | 2 | HTTPS请求会使用代理。 |

## WebDestroyMode20+

Web组件的销毁模式，当Web组件销毁时，销毁模式会影响Web内核的资源释放时机，例如JavaScript运行上下文、渲染上下文等等。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL\_MODE | 0 | 普通模式，由系统决定Web组件资源的销毁时机。 |
| FAST\_MODE | 1 | 快速模式，当Web组件触发销毁时，立即销毁相关的内部资源。 |

## ScrollbarMode23+

Web页面场景下，全局滚动条模式。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERLAY\_LAYOUT\_SCROLLBAR | 0 | 非常驻滚动条，可以拖拽。 |
| FORCE\_DISPLAY\_SCROLLBAR | 1 | 常驻滚动条。 |
| OVERLAY\_VISUAL\_SCROLLBAR | 2 | 非常驻滚动条，不可以拖拽。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |

## WebBlanklessErrorCode20+

无白屏加载的异常错误码。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 成功。 |
| ERR\_UNKNOWN | -1 | 未知错误，内部状态错误等。 |
| ERR\_INVALID\_PARAM | -2 | 参数不合法。 |
| ERR\_CONTROLLER\_NOT\_INITED | -3 | WebViewController未绑定组件。 |
| ERR\_KEY\_NOT\_MATCH | -4 | 未匹配到key值，对于[setBlanklessLoadingWithKey](arkts-apis-webview-webviewcontroller.md#setblanklessloadingwithkey20)需与[getBlanklessInfoWithKey](arkts-apis-webview-webviewcontroller.md#getblanklessinfowithkey20)配套使用并且key值一致，否则返回该错误码。 |
| ERR\_SIGNIFICANT\_CHANGE | -5 | 当相似度较低时，系统会判定为跳变太大，[setBlanklessLoadingWithKey](arkts-apis-webview-webviewcontroller.md#setblanklessloadingwithkey20)接口不会成功启用插帧。 |
| ERR\_DURATION\_OUT\_OF\_RANGE23+ | -6 | 在[BlanklessLoadingParam](arkts-apis-webview-i.md#blanklessloadingparam23)设置的插帧持续时间超出范围。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| ERR\_EXPIRATION\_TIME\_OUT\_OF\_RANGE23+ | -7 | 在[BlanklessLoadingParam](arkts-apis-webview-i.md#blanklessloadingparam23)设置的历史帧失效时间超出范围。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## BlanklessFrameInterpolationState 23+

白屏插帧状态。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FRAME\_INTERPOLATION\_SUCCEEDED | 0 | 插帧成功。 |
| FRAME\_INTERPOLATION\_FAILED | 1 | 插帧失败。 |
| FRAME\_INTERPOLATION\_REMOVED | 2 | 插帧移除。 |

## ArkWebEngineVersion20+

ArkWeb内核版本，请参考[M114内核在HarmonyOS 6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/CompatibleWithLegacyWebEngine_6.0.md)，[M132内核在HarmonyOS 7.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/CompatibleWithLegacyWebEngine_7.0.md)。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM\_DEFAULT | 0 | 系统默认内核（可参考[约束与限制](../harmonyos-guides/web-component-overview.md#约束与限制)），HarmonyOS 6.0版本默认为M132，HarmonyOS 7.0版本默认为M144。 |
| M114 | 1 | HarmonyOS 6.0版本的遗留内核。开发者可选择此遗留内核，若系统版本上不存在此内核则设置无效，使用系统默认内核。 |
| M132 | 2 | HarmonyOS 6.0版本的常青内核（HarmonyOS 7.0版本的遗留内核），M132为HarmonyOS 6.0版本的默认内核。若系统版本上不存在此内核则设置无效，使用系统默认内核。 |
| M144 | 3 | HarmonyOS 7.0版本的常青内核，M144为HarmonyOS 7.0版本的默认内核。若系统版本上不存在此内核则设置无效，使用系统默认内核。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |
| ARKWEB\_EVERGREEN23+ | 99999 | 系统的最新内核（常青内核）。开发者可选择在每个系统版本上都使用最新的内核，HarmonyOS开发套件API version 23及之后所有系统版本都生效。 |

**表1** 常青内核与遗留内核含义说明

| 内核类型 | 英文 | 说明 |
| --- | --- | --- |
| 常青内核 | EVERGREEN WebCore | 当前系统的最新Web内核，系统基于此内核进行完整的功能实现，推荐应用使用。 |
| 遗留内核 | LEGACY WebCore | 复用上一版本的内核，只做安全补丁及舆情问题修复，仅作为兼容性回滚使用，且遗留内核的支持有时间限制。 |

## SiteIsolationMode21+

站点隔离机制将不同源的网站隔离在不同的渲染子进程中，减少跨域攻击面。例如，PC上原有进程模型是每一个Tab对应一个渲染子进程，站点隔离打开后，让不同源的Iframe运行在独立的渲染子进程中。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARTIAL | 0 | 部分站点隔离，即在同一个渲染进程内加载新站点。 |
| STRICT | 1 | 严格站点隔离，跨站点的Iframe将切换到新的渲染进程。 |

## WebSoftKeyboardBehaviorMode22+

Web软键盘自动控制模式。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 当Web组件失去焦点或获得焦点、状态切换为inactive或active时，系统均会尝试触发软键盘自动隐藏或拉起（默认值）。 |
| DISABLE\_AUTO\_KEYBOARD\_ON\_ACTIVE | 1 | Web组件在inactive或active状态切换时，系统不再尝试触发软键盘自动隐藏或拉起。 |

## WebHttpCookieSameSitePolicy23+

控制cookie在跨站请求中的发送行为。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 允许在跨站请求中携带cookie，但必须同时设置secure属性。 |
| LAX | 1 | 允许特定的跨站请求携带cookie，如某些get请求的导航场景。 |
| STRICT | 2 | 禁止在跨站请求中携带cookie。 |

## UserAgentFormFactor24+

用户设备形态。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTOMOTIVE | 'Automotive' | 车机，字符串类型。 |
| DESKTOP | 'Desktop' | PC，字符串类型。 |
| MOBILE | 'Mobile' | 手机，字符串类型。 |
| EINK | 'EInk' | 墨水屏，字符串类型。 |
| TABLET | 'Tablet' | 平板，字符串类型。 |
| WATCH | 'Watch' | 手表，字符串类型。 |
| XR | 'XR' | VR+AR设备，字符串类型。 |

## ControllerAttachState20+

WebviewController与Web组件的绑定状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNATTACHED | 0 | 未绑定状态。 |
| ATTACHED | 1 | 已绑定状态。 |
