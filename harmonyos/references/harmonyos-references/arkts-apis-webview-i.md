---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i
title: Interfaces (其他)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-04-29T13:55:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a63b13f886a11990931308abc101566df376b5bcc8e52d4a962954ca8d0634a8
---

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。

## WebStorageOrigin

PhonePC/2in1TabletTVWearable

提供Web SQL数据库的使用信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| origin | string | 否 | 否 | 指定源的字符串索引。 |
| usage | number | 否 | 否 | 指定源的存储量。  单位：byte。 |
| quota | number | 否 | 否 | 指定源的存储配额。  单位：byte。 |

## WebHeader

PhonePC/2in1TabletTVWearable

Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| headerKey | string | 否 | 否 | 请求/响应头的key。 |
| headerValue | string | 否 | 否 | 请求/响应头的value。 |

## WebCustomScheme

PhonePC/2in1TabletTVWearable

自定义协议配置。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| schemeName | string | 否 | 否 | 自定义协议名称。最大长度为32，其字符仅支持小写字母、数字、'.'、'+'、'-'，同时需要以字母开头。 |
| isSupportCORS | boolean | 否 | 否 | 是否支持跨域请求。  true表示支持跨域请求，false表示不支持跨域请求。  默认值：true。 |
| isSupportFetch | boolean | 否 | 否 | 是否支持fetch请求。  true表示支持fetch请求，false表示不支持fetch请求。  默认值：true。 |
| isStandard12+ | boolean | 否 | 是 | 设置了该选项的scheme是否将作为标准scheme进行处理。标准scheme需要符合RFC 1738第3.1节中定义的URL规范化和解析规则。  true表示设置了该选项的scheme将作为标准scheme进行处理，false表示设置了该选项的scheme不作为标准scheme进行处理。  默认值：true。 |
| isLocal12+ | boolean | 否 | 是 | 设置了该选项的scheme是否将使用与“file”协议相同的安全规则来处理。  true表示设置了该选项的scheme将使用与“file”协议相同的安全规则来处理，false表示设置了该选项的scheme不使用与“file”协议相同的安全规则来处理。  默认值：true。 |
| isDisplayIsolated12+ | boolean | 否 | 是 | 设置了该选项的scheme的内容是否只能从相同scheme的其他内容中显示或访问。  true表示设置了该选项的scheme的内容只能从相同scheme的其他内容中显示或访问，false表示设置了该选项的scheme的内容不是只能从相同scheme的其他内容中显示或访问。  默认值：true。 |
| isSecure12+ | boolean | 否 | 是 | 设置了该选项的scheme是否将使用与应用于“https”的安全规则相同的安全规则来处理。true表示设置了该选项的scheme将使用与应用于“https”的安全规则相同的安全规则来处理，false表示设置了该选项的scheme不使用与应用于“https”的安全规则相同的安全规则来处理。  默认值：true。 |
| isCspBypassing12+ | boolean | 否 | 是 | 设置了该选项的scheme可以绕过内容安全策略（CSP）检查。  true表示设置了该选项的scheme可以绕过内容安全策略（CSP）检查，false表示设置了该选项的scheme不可以绕过内容安全策略（CSP）检查。  默认值：true。  在大多数情况下，当设置isStandard为true时，不应设置此值。 |
| isCodeCacheSupported12+ | boolean | 否 | 是 | 设置了该选项的scheme的js资源是否支持生成code cache。  true表示设置了该选项的scheme的js资源支持生成code cache，false表示设置了该选项的scheme的js资源不支持生成code cache。  默认值：false。 |

## RequestInfo12+

PhonePC/2in1TabletTVWearable

Web组件发送的资源请求信息。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 请求的链接。 |
| method | string | 否 | 否 | 请求的方法。 |
| formData | string | 否 | 否 | 请求的表单数据。 |

## CacheOptions12+

PhonePC/2in1TabletTVWearable

Web组件预编译JavaScript生成字节码缓存的配置对象，用于控制字节码缓存更新。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| responseHeaders | Array<[WebHeader](arkts-apis-webview-i.md#webheader)> | 否 | 否 | 请求此JavaScript文件时服务器返回的响应头，使用E-Tag或Last-Modified标识文件版本，判断是否需要更新。 |

## SnapshotInfo12+

PhonePC/2in1TabletTVWearable

获取全量绘制结果入参。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 是 | snapshot的id。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | web绘制的尺寸，最多支持16000px \* 16000px，长度单位支持px、vp、%，需保持不同参数传入长度单位一致，默认单位vp，超过规格时返回最大规格。（示例：width:'100px'，height:'200px'。或者 width:'20%'，height:'30%'。只写数字时单位为vp。） |

## SnapshotResult12+

PhonePC/2in1TabletTVWearable

全量绘制回调结果。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 是 | snapshot的id。 |
| status | boolean | 否 | 是 | snapshot的状态，正常为true，失败为false，获取全量绘制结果失败，返回size的长宽都为0，map为空。 |
| size | [SizeOptions](ts-types.md#sizeoptions) | 否 | 是 | web绘制的真实尺寸，number类型，单位vp。 |
| imagePixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 全量绘制结果为image.PixelMap格式。 |

## OfflineResourceMap12+

PhonePC/2in1TabletTVWearable

本地离线资源配置对象，用于配置将被[injectOfflineResources](arkts-apis-webview-webviewcontroller.md#injectofflineresources12)接口注入到内存缓存的本地离线资源的相关信息，内核会根据此信息生成资源缓存，并据此控制缓存的有效期。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| urlList | Array<string> | 否 | 否 | 本地离线资源对应的网络地址列表，列表的第一项将作为资源的源（Origin），如果仅提供一个网络地址，则使用该地址作为这个资源的源。url仅支持http或https协议，长度不超过2048。 |
| resource | Uint8Array | 否 | 否 | 本地离线资源的内容。 |
| responseHeaders | Array<[WebHeader](arkts-apis-webview-i.md#webheader)> | 否 | 否 | 资源对应的HTTP响应头。其中提供的Cache-Control或Expires响应头将被用于控制资源在内存缓存中的有效期。如果不提供，默认的有效期为86400秒，即1天。其中提供的Content-Type响应头将被用于定义资源的MIMEType，MODULE\_JS必须提供有效的MIMEType，其他类型可不提供，无默认值，不符合标准的MIMEType会导致内存缓存失效。如果业务网页中的script标签使用了crossorigin属性，则必须在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous或use-credentials。 |
| type | [OfflineResourceType](arkts-apis-webview-e.md#offlineresourcetype12) | 否 | 否 | 资源的类型，目前仅支持JavaScript、图片和CSS类型的资源。 |

## PdfConfiguration14+

PhonePC/2in1TabletTVWearable

createPdf函数输入参数。

说明

英寸与像素之间转换公式：像素 = 96 \* 英寸。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 页面宽度。  单位：英寸。  推荐值：A4纸页面宽度8.27英寸。 |
| height | number | 否 | 否 | 页面高度。  单位：英寸。  推荐值：A4纸页面高度11.69英寸。 |
| scale | number | 否 | 是 | 放大倍数。  取值范围：[0.0, 2.0]。如果不在取值范围内，小于0.0设置为0.0，大于2.0设置为2.0。  默认值：1.0。 |
| marginTop | number | 否 | 否 | 上边距。  取值范围：[0.0, 页面高度的一半)。如果不在取值范围内，则设置为0.0。  单位：英寸。 |
| marginBottom | number | 否 | 否 | 下边距。  取值范围：[0.0, 页面高度的一半)。如果不在取值范围内，则设置为0.0。  单位：英寸。 |
| marginRight | number | 否 | 否 | 右边距。  取值范围：[0.0, 页面宽度的一半)。如果不在取值范围内，则设置为0.0。  单位：英寸。 |
| marginLeft | number | 否 | 否 | 左边距。  取值范围：[0.0, 页面宽度的一半)。如果不在取值范围内，则设置为0.0。  单位：英寸。 |
| shouldPrintBackground | boolean | 否 | 是 | true表示打印背景颜色，false表示不打印背景颜色。  默认值：false。 |

## ScrollOffset13+

PhonePC/2in1TabletTVWearable

网页当前的滚动偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 网页在水平方向的滚动偏移量。取值为网页左边界x坐标与Web组件左边界x坐标的差值。  当网页向右过滚动时，取值范围为负值。  当网页没有过滚动或者网页向左过滚动时，取值为0或正值。  单位：vp。 |
| y | number | 否 | 否 | 网页在垂直方向的滚动偏移量。取值为网页上边界y坐标与Web组件上边界y坐标的差值。  当网页向下过滚动时，取值范围为负值。  当网页没有过滚动或者网页向上过滚动时，取值为0或正值。  单位：vp。 |

## HitTestValue

PhonePC/2in1TabletTVWearable

提供点击区域的元素信息。示例代码参考[getLastHitTest](arkts-apis-webview-webviewcontroller.md#getlasthittest18)。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [WebHitTestType](arkts-apis-webview-e.md#webhittesttype) | 否 | 否 | 当前被点击区域的元素类型。 |
| extra | string | 否 | 否 | 点击区域的附加参数信息。若被点击区域为图片或链接，则附加参数信息为其url地址。 |

## ControllerAttachState20+

PhonePC/2in1TabletTVWearable

WebViewController与Web组件的绑定状态。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNATTACHED | 0 | 未绑定状态。 |
| ATTACHED | 1 | 已绑定状态。 |

## BlanklessInfo20+

PhonePC/2in1TabletTVWearable

页面首屏加载预测信息，主要包括首屏相似度预测值，首屏加载耗时预测值，预测错误码，应用需根据此信息来决策是否启用无白屏加载插帧方案。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errCode | WebBlanklessErrorCode | 否 | 否 | 无白屏加载的异常错误码，见[WebBlanklessErrorCode](arkts-apis-webview-e.md#webblanklesserrorcode20)定义。 |
| similarity | number | 否 | 否 | 首屏相似度，根据历史加载首屏内容计算相似度，范围为[0, 1.0]，1.0表示完全一致，数值越接近1，相似度越高。该值存在滞后性，本地加载的相似度将在下次加载时才可反映。建议当相似度较低时，应用不启用无白屏加载插帧方案。 |
| loadingTime | number | 否 | 否 | 根据历史加载首屏耗时预测本次加载耗时，单位ms，取值范围需大于0。 |

## BlanklessFrameInterpolationInfo23+

PhonePC/2in1TabletTVWearable

白屏插帧状态信息，作为[BlanklessLoadingParam](arkts-apis-webview-i.md#blanklessloadingparam23)中的回调入参使用。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 唯一标识插帧页面的key值。与[setBlanklessLoadingWithParams](arkts-apis-webview-webviewcontroller.md#setblanklessloadingwithparams23)的key值相同。 |
| state | [BlanklessFrameInterpolationState](arkts-apis-webview-e.md#blanklessframeinterpolationstate-23) | 否 | 否 | 当前插帧状态。 |
| timestamp | number | 否 | 否 | 插帧成功、失败或移除的时间点，UTC时间，单位ms。 |
| reason | string | 否 | 否 | 插帧失败的原因。 |

## BlanklessLoadingParam23+

PhonePC/2in1TabletTVWearable

白屏插帧加载参数。

**系统能力：** SystemCapability.Web.Webview.Core

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enable | boolean | 否 | 否 | 是否启用白屏插帧。  true：启用，false：不启用。 |
| duration | number | 否 | 是 | 插帧持续时间。  取值范围：[200, 2000] ∪ {0}，其中0表示不指定持续时间，由系统自动设置合适的持续时间。  单位：ms。 |
| expirationTime | number | 否 | 是 | 历史帧失效时间，UTC时间。  用T表示当前UTC时间，同时已知30天为2592000000ms，取值范围：(T, T + 2592000000] ∪ {0}，其中0表示不指定失效时间，采用系统默认失效时间（7天）。  单位：ms。 |
| callback | Callback<[BlanklessFrameInterpolationInfo](arkts-apis-webview-i.md#blanklessframeinterpolationinfo23)> | 否 | 是 | 插帧成功、失败或移除后执行的回调。  只有在enable为true时生效。可选，不设置则不进行任何操作。 |

## HistoryItem

PhonePC/2in1TabletTVWearable

页面历史记录项。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 历史页面图标的PixelMap对象。 |
| historyUrl | string | 否 | 否 | 历史记录项的url地址。 |
| historyRawUrl | string | 否 | 否 | 历史记录项的原始url地址。 |
| title | string | 否 | 否 | 历史记录项的标题。 |

## MediaInfo12+

PhonePC/2in1TabletTVWearable

[CreateNativeMediaPlayerCallback](arkts-apis-webview-t.md#createnativemediaplayercallback12)回调函数的一个参数。包含了网页中媒体的信息。应用可以根据这些信息来创建接管网页媒体播放的播放器。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| embedID | string | 否 | 否 | 网页中的 <video> 或 <audio> 的 ID 。 |
| mediaType | [MediaType](arkts-apis-webview-e.md#mediatype12) | 否 | 否 | 媒体的类型。 |
| mediaSrcList | [MediaSourceInfo](arkts-apis-webview-mediasourceinfo.md)[] | 否 | 否 | 媒体的源。可能有多个源，应用需要选择一个支持的源来播放。 |
| surfaceInfo | [NativeMediaPlayerSurfaceInfo](arkts-apis-webview-nativemediaplayersurfaceinfo.md) | 否 | 否 | 用于同层渲染的 surface 信息。 |
| controlsShown | boolean | 否 | 否 | <video> 或 <audio> 中是否有 controls属性。  true表示有，false表示没有。 |
| controlList | string[] | 否 | 否 | <video> 或 <audio> 中的 controlslist 属性的值。 |
| muted | boolean | 否 | 否 | 是否要求静音播放。  true表示静音播放，false表示未静音播放。 |
| posterUrl | string | 否 | 否 | 海报的地址。 |
| preload | [Preload](arkts-apis-webview-e.md#preload12) | 否 | 否 | 是否需要预加载。 |
| headers | Record<string, string> | 否 | 否 | 播放器请求媒体资源时，需要携带的 HTTP 头。 |
| attributes | Record<string, string> | 否 | 否 | <video> 或 <audio> 标签中的属性。 |

## RectEvent12+

PhonePC/2in1TabletTVWearable

矩形定义。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 矩形区域左上角x坐标。 |
| y | number | 否 | 否 | 矩形区域左上角y坐标。 |
| width | number | 否 | 否 | 矩形的宽度。  单位：px |
| height | number | 否 | 否 | 矩形的高度。  单位：px |

## WebHttpCookie23+

PhonePC/2in1TabletTVWearable

cookie的相关字段。

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| samesitePolicy | [WebHttpCookieSameSitePolicy](arkts-apis-webview-e.md#webhttpcookiesamesitepolicy23) | 否 | 否 | cookie的同站策略。 |
| expiresDate | string | 否 | 否 | cookie的过期时间。时间格式详见[Date](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Reference/Headers/Date)。 |
| name | string | 否 | 否 | cookie的名称。 |
| isSessionCookie | boolean | 否 | 否 | 标记该cookie是否是session cookie。  true表示是session cookie，false表示不是session cookie。 |
| value | string | 否 | 否 | cookie的值。 |
| path | string | 否 | 否 | cookie的路径。 |
| isHttpOnly | boolean | 否 | 否 | 标记该cookie是否只能通过http请求访问。  true表示仅能通过http访问，不能通过JavaScript访问，false表示可以通过JavaScript访问。 |
| isSecure | boolean | 否 | 否 | 标记该cookie是否只能通过https发送。  true表示仅能通过https发送，不能通过http发送，false表示可以通过http发送。 |
| domain | string | 否 | 否 | 指定哪些域名可以访问该cookie。 |
