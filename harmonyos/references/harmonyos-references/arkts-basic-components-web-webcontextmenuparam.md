---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuparam
title: Class (WebContextMenuParam)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebContextMenuParam)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:20+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:4070b3974d5b1fc2375fc7e8ba7557bc09dd1abf24b0d37b572c855cc8be1d18
---

实现长按页面元素或鼠标右键弹出来的菜单信息。示例代码参考[onContextMenuShow事件](arkts-basic-components-web-events.md#oncontextmenushow9)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

WebContextMenuParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## x9+

PhonePC/2in1TabletTVWearable

x(): number

弹出菜单的x坐标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。  单位：vp（虚拟像素）。 |

## y9+

PhonePC/2in1TabletTVWearable

y(): number

弹出菜单的y坐标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。  单位：vp（虚拟像素）。 |

## getLinkUrl9+

PhonePC/2in1TabletTVWearable

getLinkUrl(): string

获取经过安全检查的URL链接地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回经过安全检查的URL链接。 |

## getUnfilteredLinkUrl9+

PhonePC/2in1TabletTVWearable

getUnfilteredLinkUrl(): string

获取原始URL链接地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回原始的URL链接。 |

## getSourceUrl9+

PhonePC/2in1TabletTVWearable

getSourceUrl(): string

获取sourceUrl链接。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 如果选中的元素有src属性，返回src的URL。返回URL的最大上限为2MB，超出上限时返回空字符串。 |

## existsImageContents9+

PhonePC/2in1TabletTVWearable

existsImageContents(): boolean

是否存在图像内容。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 长按位置中有图片返回true，否则返回false。 |

## getMediaType9+

PhonePC/2in1TabletTVWearable

getMediaType(): ContextMenuMediaType

获取网页元素媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuMediaType](arkts-basic-components-web-e.md#contextmenumediatype9) | 网页元素媒体类型。 |

## getSelectionText9+

PhonePC/2in1TabletTVWearable

getSelectionText(): string

获取选中文本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 菜单上下文选中文本内容，不存在则返回空。 |

## getSourceType9+

PhonePC/2in1TabletTVWearable

getSourceType(): ContextMenuSourceType

获取菜单事件来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuSourceType](arkts-basic-components-web-e.md#contextmenusourcetype9) | 菜单事件来源。 |

## getInputFieldType9+

PhonePC/2in1TabletTVWearable

getInputFieldType(): ContextMenuInputFieldType

获取网页元素输入框类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuInputFieldType](arkts-basic-components-web-e.md#contextmenuinputfieldtype9) | 输入框类型。 |

## isEditable9+

PhonePC/2in1TabletTVWearable

isEditable(): boolean

获取网页元素是否可编辑状态。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 网页元素可编辑返回true，不可编辑返回false。 |

## getEditStateFlags9+

PhonePC/2in1TabletTVWearable

getEditStateFlags(): number

获取网页元素可编辑标识。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 网页元素可编辑标识，参照[ContextMenuEditStateFlags](arkts-basic-components-web-e.md#contextmenueditstateflags9)。 |

## getPreviewWidth13+

PhonePC/2in1TabletTVWearable

getPreviewWidth(): number

获取预览图的宽。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 预览图的宽。  单位：vp（虚拟像素）。 |

## getPreviewHeight13+

PhonePC/2in1TabletTVWearable

getPreviewHeight(): number

获取预览图的高。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 预览图的高。  单位：vp（虚拟像素）。 |

## getContextMenuMediaType22+

PhonePC/2in1TabletTVWearable

getContextMenuMediaType(): ContextMenuDataMediaType

在上报上下文菜单事件时，获取用户点击的网页元素类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuDataMediaType](arkts-basic-components-web-e.md#contextmenudatamediatype22) | 网页元素媒体类型。 |
