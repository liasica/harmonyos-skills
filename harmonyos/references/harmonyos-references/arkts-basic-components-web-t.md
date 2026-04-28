---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-t
title: Types
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Types
category: harmonyos-references
scraped_at: 2026-04-28T08:05:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ab525645c3d81efd2fa7567fad7577b203289ae68b92ac5b5703a33b6baa1de7
---

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。

## WebviewController9+

PhonePC/2in1TabletTVWearable

type WebviewController = WebviewController

提供Web控制器的方法。

**系统能力：** SystemCapability.Web.Webview.Core

| 类型 | 说明 |
| --- | --- |
| [WebviewController](arkts-apis-webview-webviewcontroller.md) | 通过WebviewController可以控制Web组件各种行为。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。 |

## OnAdsBlockedCallback12+

PhonePC/2in1TabletTVWearable

type OnAdsBlockedCallback = (details: AdsBlockedDetails) => void

当页面发生广告过滤时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| details | [AdsBlockedDetails](arkts-basic-components-web-i.md#adsblockeddetails12) | 是 | 发生广告拦截时，广告资源信息。 |

## OnSslErrorEventCallback12+

PhonePC/2in1TabletTVWearable

type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void

用户加载资源时发生SSL错误时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sslErrorEvent | [SslErrorEvent](arkts-basic-components-web-i.md#sslerrorevent12) | 是 | 用户加载资源时发生SSL错误时触发的回调详情。 |

## OnVerifyPinCallback22+

PhonePC/2in1TabletTVWearable

type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void

需要用户进行PIN码认证时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verifyPinEvent | [VerifyPinEvent](arkts-basic-components-web-i.md#verifypinevent22) | 是 | 需要用户进行PIN码认证时触发的回调详情。 |

## OnContextMenuHideCallback11+

PhonePC/2in1TabletTVWearable

type OnContextMenuHideCallback = () => void

上下文菜单自定义隐藏的回调。

**系统能力：** SystemCapability.Web.Webview.Core

## OnRenderProcessNotRespondingCallback12+

PhonePC/2in1TabletTVWearable

type OnRenderProcessNotRespondingCallback = (data : RenderProcessNotRespondingData) => void

渲染进程无响应时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [RenderProcessNotRespondingData](arkts-basic-components-web-i.md#renderprocessnotrespondingdata12) | 是 | 渲染进程无响应的详细信息。 |

## OnRenderProcessRespondingCallback12+

PhonePC/2in1TabletTVWearable

type OnRenderProcessRespondingCallback = () => void

渲染进程由无响应状态变回正常运行状态时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

## OnViewportFitChangedCallback12+

PhonePC/2in1TabletTVWearable

type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void

网页meta中viewport-fit配置项更改时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| viewportFit | [ViewportFit](arkts-basic-components-web-e.md#viewportfit12) | 是 | 网页meta中viewport-fit配置的视口类型。 |

## OnNativeEmbedVisibilityChangeCallback12+

PhonePC/2in1TabletTVWearable

type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void

当同层标签可见性变化时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nativeEmbedVisibilityInfo | [NativeEmbedVisibilityInfo](arkts-basic-components-web-i.md#nativeembedvisibilityinfo12) | 是 | 提供同层标签的可见性信息。 |

## OnFullScreenEnterCallback12+

PhonePC/2in1TabletTVWearable

type OnFullScreenEnterCallback = (event: FullScreenEnterEvent) => void

Web组件进入全屏时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [FullScreenEnterEvent](arkts-basic-components-web-i.md#fullscreenenterevent12) | 是 | Web组件进入全屏的回调事件详情。 |

## OnFirstMeaningfulPaintCallback12+

PhonePC/2in1TabletTVWearable

type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: [FirstMeaningfulPaint](arkts-basic-components-web-i.md#firstmeaningfulpaint12)) => void

网页绘制页面度量信息的回调，当网页加载完页面主要内容时会触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstMeaningfulPaint | [FirstMeaningfulPaint](arkts-basic-components-web-i.md#firstmeaningfulpaint12) | 是 | 绘制页面主要内容度量的详细信息。 |

## OnLargestContentfulPaintCallback12+

PhonePC/2in1TabletTVWearable

type OnLargestContentfulPaintCallback = (largestContentfulPaint: [LargestContentfulPaint](arkts-basic-components-web-i.md#largestcontentfulpaint12)) => void

网页绘制页面最大内容度量信息的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| largestContentfulPaint | [LargestContentfulPaint](arkts-basic-components-web-i.md#largestcontentfulpaint12) | 是 | 网页绘制页面最大内容度量的详细信息。 |

## OnNavigationEntryCommittedCallback11+

PhonePC/2in1TabletTVWearable

type OnNavigationEntryCommittedCallback = (loadCommittedDetails: [LoadCommittedDetails](arkts-basic-components-web-i.md#loadcommitteddetails11)) => void

导航条目提交时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loadCommittedDetails | [LoadCommittedDetails](arkts-basic-components-web-i.md#loadcommitteddetails11) | 是 | 提供已提交跳转的网页的详细信息。 |

## OnSafeBrowsingCheckResultCallback11+

PhonePC/2in1TabletTVWearable

type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void

网站安全风险检查触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| threatType | [ThreatType](arkts-basic-components-web-e.md#threattype11) | 是 | 定义网站threat类型。 |

## OnIntelligentTrackingPreventionCallback12+

PhonePC/2in1TabletTVWearable

type OnIntelligentTrackingPreventionCallback = (details: IntelligentTrackingPreventionDetails) => void

当跟踪者cookie被拦截时触发的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| details | [IntelligentTrackingPreventionDetails](arkts-basic-components-web-i.md#intelligenttrackingpreventiondetails12) | 是 | 提供智能防跟踪拦截的详细信息。 |

## OnOverrideUrlLoadingCallback12+

PhonePC/2in1TabletTVWearable

type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean

onOverrideUrlLoading的回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webResourceRequest | [WebResourceRequest](arkts-basic-components-web-webresourcerequest.md) | 是 | url请求的相关信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示阻止此次加载，否则允许此次加载。 |

## WebKeyboardCallback12+

PhonePC/2in1TabletTVWearable

type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions

拦截网页可编辑元素拉起软键盘的回调，一般在点击网页input标签时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyboardCallbackInfo | [WebKeyboardCallbackInfo](arkts-basic-components-web-i.md#webkeyboardcallbackinfo12) | 是 | 拦截网页拉起软键盘回调通知的入参，其中包括[WebKeyboardController](arkts-basic-components-web-webkeyboardcontroller.md)、可编辑元素的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebKeyboardOptions](arkts-basic-components-web-i.md#webkeyboardoptions12) | 回调函数通过返回[WebKeyboardOptions](arkts-basic-components-web-i.md#webkeyboardoptions12)来决定ArkWeb内核拉起不同类型的软键盘。 |

## OnOverrideErrorPageCallback20+

PhonePC/2in1TabletTVWearable

type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string

onOverrideErrorPage的回调函数，网页加载失败时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errorPageEvent | [OnErrorReceiveEvent](arkts-basic-components-web-i.md#onerrorreceiveevent12) | 是 | 网页加载遇到错误时返回的相关信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回以Base64编码的HTML文本内容。 |

## MouseInfoCallback20+

PhonePC/2in1TabletTVWearable

type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void

当鼠标/触摸板点击到同层标签时触发该回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NativeEmbedMouseInfo](arkts-basic-components-web-i.md#nativeembedmouseinfo20) | 是 | 提供鼠标/触摸板在同层标签上点击或长按的详细信息。 |

**示例：**

完整示例代码参考[onNativeEmbedMouseEvent](arkts-basic-components-web-events.md#onnativeembedmouseevent20)。

## OnNativeEmbedObjectParamChangeCallback21+

PhonePC/2in1TabletTVWearable

type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void

增加、修改或删除同层渲染object标签内嵌param元素时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NativeEmbedParamDataInfo](arkts-basic-components-web-i.md#nativeembedparamdatainfo21) | 是 | object标签内嵌param元素的详细变化信息。 |

**示例：**

完整示例代码参考[onNativeEmbedObjectParamChange](arkts-basic-components-web-events.md#onnativeembedobjectparamchange21)。

## OnDetectBlankScreenCallback22+

PhonePC/2in1TabletTVWearable

type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void

检测到白屏时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [BlankScreenDetectionEventInfo](arkts-basic-components-web-i.md#blankscreendetectioneventinfo22) | 是 | 检测到白屏时的详细信息。 |

**示例：**

完整示例代码参考[onDetectedBlankScreen](arkts-basic-components-web-events.md#ondetectedblankscreen22)。

## OnCameraCaptureStateChangeCallback23+

PhonePC/2in1TabletTVWearable

type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void;

当页面摄像设备状态发生改变时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [CameraCaptureStateChangeInfo](arkts-basic-components-web-i.md#cameracapturestatechangeinfo23) | 是 | 网页摄像头状态发生改变时，返回原来的状态和改变后的状态。 |

## OnMicrophoneCaptureStateChangeCallback23+

PhonePC/2in1TabletTVWearable

type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void;

当页面麦克风状态发生改变时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [MicrophoneCaptureStateChangeInfo](arkts-basic-components-web-i.md#microphonecapturestatechangeinfo23) | 是 | 网页麦克风状态发生改变时，返回原来的状态和改变后的状态。 |

## TextSelectionChangeCallback23+

PhonePC/2in1TabletTVWearable

type TextSelectionChangeCallback = (selectionText: string) => void

onTextSelectionChange的回调，选区内容改变时触发。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionText | string | 是 | 返回所选文本的内容。 |

**示例：**

完整示例代码参考[onTextSelectionChange](arkts-basic-components-web-events.md#ontextselectionchange23)。

## OnFirstScreenPaintCallback23+

PhonePC/2in1TabletTVWearable

type OnFirstScreenPaintCallback = (firstScreenPaint: FirstScreenPaint) => void

检测到首屏渲染结束时会触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstScreenPaint | [FirstScreenPaint](arkts-basic-components-web-i.md#firstscreenpaint23) | 是 | 检测到首屏渲染时的详细信息。 |

**示例：**

完整示例代码参考[onFirstScreenPaint](arkts-basic-components-web-events.md#onfirstscreenpaint23)。
