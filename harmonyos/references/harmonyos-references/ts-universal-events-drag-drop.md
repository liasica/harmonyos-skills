---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop
title: 拖拽事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 拖拽事件
category: harmonyos-references
scraped_at: 2026-04-29T13:51:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:291db1089658e188b21d713021fedecc1a7bbbaad5582e450513a779e312244e
---

拖拽事件是指在用户界面中，当用户拖动某个对象（如文件、控件或元素）时触发的一系列事件。这些事件允许开发者自定义拖拽行为，实现诸如拖放、调整位置等功能。

说明

* 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 应用本身预置的资源文件（即应用在安装前的HAP包中已经存在的资源文件）仅支持本地应用内拖拽。

ArkUI框架对以下组件实现了默认的拖拽能力，支持对数据的拖出或拖入响应。开发者也可以通过实现通用拖拽事件来自定义拖拽能力。

* 默认支持拖出能力的组件（可从组件上拖出数据）：[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)、[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)、[Hyperlink](ts-container-hyperlink.md)，开发者可通过设置这些组件的[draggable](ts-universal-attributes-drag-drop.md#draggable)属性来控制对默认拖拽能力的使用。
* 默认支持拖入能力的组件（目标组件可响应拖入数据）：[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)，开发者可通过设置这些组件的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)属性为null来禁用对默认拖入能力的支持。

其他支持拖出能力的组件需要开发者将[draggable](ts-universal-attributes-drag-drop.md#draggable)属性设置为true，并在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)等接口中实现数据传输相关内容，才能正确处理拖拽能力。

Text、TextInput、TextArea、Hyperlink、Image、RichEditor和Web组件的draggable属性默认为true，默认支持拖出能力。

说明

Text组件需配合[copyOption](ts-basic-components-text.md#copyoption9)一起使用，设置copyOptions为CopyOptions.InApp或者CopyOptions.LocalDevice。

## onDragStart

PhonePC/2in1TabletTVWearable

onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T

在手势拖拽场景中，在可拖拽的组件上长按时间超过500ms，然后手指移动距离大于10vp时触发此回调；在鼠标拖拽场景中，鼠标左键在可拖拽的组件上按下并移动超过1vp时，即可触发此回调。

针对默认支持拖拽能力的组件，如果开发者设置了onDragStart，优先执行onDragStart，并根据执行情况决定是否使用系统默认的拖拽能力，具体规则为：

* 如果开发者返回了自定义预览图，则不再使用系统默认的拖拽预览图；
* 如果开发者设置了拖拽数据，则不再使用系统默认填充的拖拽数据。

文本类组件[Text](ts-basic-components-text.md)、[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)对选中的文本内容进行拖拽时，不支持自定义预览图。当onDragStart与菜单预览一起使用或使用了默认支持拖拽能力的组件时，预览及菜单项上的自定义内容不支持拖拽。

说明

从API version 13开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**事件优先级：** 长按事件触发时间 < 500ms，长按事件优先拖拽事件响应，长按事件触发时间 >= 500ms，拖拽事件优先长按事件响应。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [DragEvent](ts-universal-events-drag-drop.md#dragevent7), extraParams?: string) => [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 回调函数。  **说明：**  event参数为拖拽事件的信息。  extraParams参数为拖拽事件的额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。  CustomBuilder为拖拽过程中显示的组件信息，不支持全局builder。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragEnter

PhonePC/2in1TabletTVWearable

onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T

拖拽进入组件范围内时，触发回调，当监听了[onDrop](ts-universal-events-drag-drop.md#ondrop)事件时，此事件才有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [DragEvent](ts-universal-events-drag-drop.md#dragevent7), extraParams?: string) => void | 是 | 回调函数。  **说明：**  event为拖拽事件信息，包括拖拽点坐标。  extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragMove

PhonePC/2in1TabletTVWearable

onDragMove(event: (event: DragEvent, extraParams?: string) => void): T

拖拽在组件范围内移动时，触发回调，当监听了[onDrop](ts-universal-events-drag-drop.md#ondrop)事件时，此事件才有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [DragEvent](ts-universal-events-drag-drop.md#dragevent7), extraParams?: string) => void | 是 | 回调函数。  **说明：**  event为拖拽事件信息，包括拖拽点坐标。  extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragLeave

PhonePC/2in1TabletTVWearable

onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T

拖拽离开组件范围内时，触发回调，当监听了[onDrop](ts-universal-events-drag-drop.md#ondrop)事件时，此事件才有效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [DragEvent](ts-universal-events-drag-drop.md#dragevent7), extraParams?: string) => void | 是 | 回调函数。  **说明：**  event为拖拽事件信息，包括拖拽点坐标。  extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDrop

PhonePC/2in1TabletTVWearable

onDrop(event: (event: DragEvent, extraParams?: string) => void): T

绑定此事件的组件可作为释放目标。当在本组件范围内停止拖放行为时，将触发回调。如果开发者未在onDrop中主动调用event.setResult()来设置拖拽接收的结果，对于系统支持的默认可拖入组件，处理结果将以系统实际处理的数据为准。对于其他组件，系统将默认视为数据接收成功。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [DragEvent](ts-universal-events-drag-drop.md#dragevent7), extraParams?: string) => void | 是 | 回调函数。  **说明：**  event为拖拽事件信息，包括拖拽点坐标。  extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDrop15+

PhonePC/2in1TabletTVWearable

onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T

绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。如果开发者没有在onDrop中主动调用event.[setResult](ts-universal-events-drag-drop.md#setresult10)()设置拖拽接收的结果，若拖拽组件为系统支持默认拖入的组件，以系统实际处理数据结果为准，其它组件则系统按照数据接收成功处理。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventCallback | [OnDragEventCallback](ts-universal-events-drag-drop.md#ondrageventcallback15) | 是 | 回调函数。 |
| dropOptions | [DropOptions](ts-universal-events-drag-drop.md#dropoptions15) | 否 | 落入过程的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragEnd10+

PhonePC/2in1TabletTVWearable

onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T

绑定此事件的组件触发的拖拽结束后，触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [DragEvent](ts-universal-events-drag-drop.md#dragevent7), extraParams?: string) => void | 是 | 回调函数。  **说明：**  event为拖拽事件信息，在onDragEnd调用中不包括拖拽点坐标。  extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onPreDrag12+

PhonePC/2in1TabletTVWearable

onPreDrag(callback: Callback<PreDragStatus>): T

绑定此事件的组件，当处于手势拖拽发起前的不同阶段时，触发回调。拖拽发起前的各阶段可参考[PreDragStatus](ts-universal-events-drag-drop.md#predragstatus12枚举说明)。此接口不支持在鼠标拖拽中触发。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PreDragStatus](ts-universal-events-drag-drop.md#predragstatus12枚举说明)> | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragSpringLoading20+

PhonePC/2in1TabletTVWearable

onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T

绑定此事件的组件可作为具有悬停检测功能的拖拽响应目标。当拖拽对象悬停在目标上时，触发回调通知。此时只有一个目标可以成为响应方，并且子组件始终具有更高的响应优先级。

关于悬停检测的触发机制及详细使用方法，请参考开发指南[支持悬停检测](../harmonyos-guides/arkts-common-events-drag-event.md#支持悬停检测)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SpringLoadingContext](ts-universal-events-drag-drop.md#springloadingcontext20)> | null | 是 | 悬停检测回调函数，当值为null时禁用悬停检测。 |
| configuration | [DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20) | 否 | 悬停检测配置信息，为undefined时取[DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20)默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## DragItemInfo

PhonePC/2in1TabletTVWearable

定义拖拽过程中拖拽项的相关信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 设置拖拽过程中显示的图片。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 拖拽过程中显示自定义组件，如果设置了pixelMap，则忽略此值。  **说明：**  不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true。该builder只用于生成当次拖拽中显示的图片，builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。  builder传参时，建议传参格式为builder: ()=>{this.customBuilder()}，用以保证this指向的正确性。具体请参考[将@Builder装饰的函数当作CustomBuilder类型使用](../harmonyos-guides/arkts-builder.md#将builder装饰的函数当作custombuilder类型使用)。 |
| extraInfo | string | 否 | 是 | 拖拽项的附加信息，用于描述拖拽项。 |

## PreviewConfiguration15+

PhonePC/2in1TabletTVWearable

配置自定义拖拽过程中的预览图样式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onlyForLifting | boolean | 否 | 是 | 自定义配置的预览图是否仅用于浮起。  **说明：**  默认值为false。true表示自定义预览图仅用于浮起，false表示可用于浮起和拖拽。设置为true时，如果发起长按拖拽，浮起时的预览图为自定义配置的预览图，拖拽时的预览图不使用[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)属性，优先使用开发者在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中返回的预览图，如果[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中没有返回预览图则使用组件自截图。 |
| delayCreating | boolean | 否 | 是 | 组件预览builder是否在设置时加载。  默认值为false。true表示组件预览builder在设置时加载，false表示组件预览builder不在设置时加载。 |

## extraParams说明

PhonePC/2in1TabletTVWearable

用于返回组件在拖拽中需要用到的额外信息。

extraParams是JSON对象转换的string字符串，可以通过JSON.parse转换的JSON对象获取如下属性。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| selectedIndex | number | 当拖拽事件设在父容器的子元素时，selectedIndex表示当前被拖拽子元素是父容器第selectedIndex个子元素，selectedIndex从0开始。  仅在[ListItem](ts-container-listitem.md)组件的拖拽事件中生效，否则返回undefined。 |
| insertIndex | number | 当前拖拽元素在List组件中放下时，insertIndex表示被拖拽元素插入该组件的第insertIndex个位置，insertIndex从0开始。  仅在[List](ts-container-list.md)组件的拖拽事件中生效，否则返回undefined。 |

## DragEvent7+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| useCustomDropAnimation10+ | boolean | 否 | 否 | 当拖拽结束时，是否禁用系统默认落位动效。  应用可将该值设定为true来禁用系统默认落位动效，并实现自己的自定义落位动效。  当不配置或设置为false时，系统默认落位动效生效，当[setResult](ts-universal-events-drag-drop.md#setresult10)设置为DRAG\_SUCCESSFUL时，落位为缩小消失动效，不为DRAG\_SUCCESSFUL时，则为放大消失动效。  当未禁用系统默认落位动效时，应用不应再实现自定义动效，以避免动效上的冲突。  默认值：false |
| dragBehavior10+ | [DragBehavior](ts-universal-events-drag-drop.md#dragbehavior10) | 否 | 否 | 切换复制和剪贴模式的角标显示状态。  默认值：DragBehavior.COPY。 |

### setData10+

PhonePC/2in1TabletTVWearable

setData(unifiedData: UnifiedData): void

向DragEvent中设置用于拖拽的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unifiedData | [UnifiedData](ts-universal-events-drag-drop.md#unifieddata10) | 是 | 拖拽相关的数据。 |

### getData10+

PhonePC/2in1TabletTVWearable

getData(): UnifiedData

获取拖拽相关数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 从DragEvent中获取拖拽相关数据。数据获取结果请参考错误码说明。 |

**错误码：**

以下错误码的详细介绍请参见[拖拽事件错误码](errorcode-drag-event.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 190001 | Data not found. |
| 190002 | Data error. |

### getSummary10+

PhonePC/2in1TabletTVWearable

getSummary(): Summary

获取所拖拽数据的概要，包括数据类型及大小信息；在延迟拖拽场景下，只能获取到数据类型信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Summary](ts-universal-events-drag-drop.md#summary10) | 拖拽相关数据的概要。 |

### setResult10+

PhonePC/2in1TabletTVWearable

setResult(dragResult: DragResult): void

在DragEvent中设置拖拽结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dragResult | [DragResult](ts-universal-events-drag-drop.md#dragresult10枚举说明) | 是 | 拖拽结果。 |

### getResult10+

PhonePC/2in1TabletTVWearable

getResult(): DragResult

获取拖拽结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DragResult](ts-universal-events-drag-drop.md#dragresult10枚举说明) | 从DragEvent中获取的拖拽结果。 |

### getPreviewRect10+

PhonePC/2in1TabletTVWearable

getPreviewRect(): Rectangle

获取拖拽预览图相对于当前窗口的位置，以及预览图尺寸信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 拖拽预览图相对于当前窗口的位置，以及预览图尺寸信息，单位vp，其中x和y代表预览图左上角的窗口坐标，width和height代表预览图的尺寸。 |

### getVelocityX10+

PhonePC/2in1TabletTVWearable

getVelocityX(): number

获取当前拖拽的x轴方向拖动速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽的x轴方向拖动速度。坐标轴原点为屏幕左上角，单位为vp，分正负方向速度，从左往右为正，反之为负。 |

### getVelocityY10+

PhonePC/2in1TabletTVWearable

getVelocityY(): number

获取当前拖拽的y轴方向拖动速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽的y轴方向拖动速度。坐标轴原点为屏幕左上角，单位为vp，分正负方向速度，从上往下为正，反之为负。 |

### getVelocity10+

PhonePC/2in1TabletTVWearable

getVelocity(): number

获取当前拖拽的主方向拖动速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽的主方向拖动速度。为xy轴方向速度的平方和的算术平方根，单位为vp。 |

### getWindowX10+

PhonePC/2in1TabletTVWearable

getWindowX(): number

获取拖拽点相对于窗口左上角的x轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于窗口左上角的x轴坐标，单位为vp。 |

### getWindowY10+

PhonePC/2in1TabletTVWearable

getWindowY(): number

获取拖拽点相对于窗口左上角的y轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于窗口左上角的y轴坐标，单位为vp。 |

### getDisplayX10+

PhonePC/2in1TabletTVWearable

getDisplayX(): number

获取当前拖拽点相对于屏幕左上角的x轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于屏幕左上角的x轴坐标，单位为vp。 |

### getDisplayY10+

PhonePC/2in1TabletTVWearable

getDisplayY(): number

获取当前拖拽点相对于屏幕左上角的y轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于屏幕左上角的y轴坐标，单位为vp。 |

### getModifierKeyState12+

PhonePC/2in1TabletTVWearable

getModifierKeyState?(keys: Array<string>): boolean

获取功能键按压状态。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array<string> | 是 | 获取功能键按压状态。报错信息请参考以下错误码。支持功能键 'Ctrl' | 'Alt' | 'Shift'。  **说明：**  此接口不支持在手写笔场景下使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否被按下，返回true表示被按下，返回false表示未被按下 |

### startDataLoading15+

PhonePC/2in1TabletTVWearable

startDataLoading(options: DataSyncOptions): string

异步获取拖拽数据，并通知开发者当前数据同步进度，仅支持在onDrop阶段使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DataSyncOptions](ts-universal-events-drag-drop.md#datasyncoptions15) | 是 | 获取拖拽数据时的参数，包含目标路径、文件冲突选项、进度条类型等。数据传输过程中可使用[cancelDataLoading](arkts-apis-uicontext-dragcontroller.md#canceldataloading15)接口取消数据加载。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[拖拽事件错误码](errorcode-drag-event.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 190003 | Operation not allowed for current phase. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 拖拽数据的标识，用于区分每次拖拽。 |

### executeDropAnimation18+

PhonePC/2in1TabletTVWearable

executeDropAnimation(customDropAnimation: Callback<void>): void

设置自定义落位动效的执行函数，仅在[useCustomDropAnimation](ts-universal-events-drag-drop.md#属性)为true时有效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customDropAnimation | [Callback<void>](js-apis-base.md#callback) | 是 | 在此回调函数中实现自定义落位动效。  **说明：**  1. 该接口仅在onDrop回调中使用有效。  2. 使用前需设置useCustomDropAnimation为true，否则该接口不生效。  3. 不要在动画callback中实现与动效无关的逻辑，避免影响执行效率。 |

### getDisplayId20+

PhonePC/2in1TabletTVWearable

getDisplayId(): number

获取当前拖拽事件发生时所在的屏幕ID，不支持在[onDragEnd](ts-universal-events-drag-drop.md#ondragend10)阶段使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽事件发生时所在的屏幕ID。 |

### getDragSource20+

PhonePC/2in1TabletTVWearable

getDragSource(): string

获取拖起方包名。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 拖起方的包名。 |

### isRemote20+

PhonePC/2in1TabletTVWearable

isRemote(): boolean

获取是否是跨设备拖拽，跨设备拖拽时为true。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否是跨设备拖拽，返回true表示是跨设备拖拽，返回false表示不是跨设备拖拽。 |

### setDataLoadParams20+

PhonePC/2in1TabletTVWearable

setDataLoadParams(dataLoadParams: DataLoadParams): void

设置起拖方延迟提供数据。使用此方法向系统提供数据加载参数，而不是直接提供完整的数据对象。当用户在目标应用程序上落入时，系统将使用此参数从起拖方请求实际数据。与[setData](ts-universal-events-drag-drop.md#setdata10)方法同时使用，以最后调用的方法为准。该接口仅在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)回调中生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataLoadParams | [DataLoadParams](ts-universal-events-drag-drop.md#dataloadparams20) | 是 | 落入操作时使用的数据加载参数。 |

### getX(deprecated)

PhonePC/2in1TabletTVWearable

getX(): number

当前拖拽点相对于窗口左上角的x轴坐标，单位为vp。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[getWindowX](ts-universal-events-drag-drop.md#getwindowx10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于窗口左上角的x轴坐标。  单位：vp |

### getY(deprecated)

PhonePC/2in1TabletTVWearable

getY(): number

当前拖拽点相对于窗口左上角的y轴坐标，单位为vp。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[getWindowY](ts-universal-events-drag-drop.md#getwindowy10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于窗口左上角的y轴坐标。  单位：vp |

### getGlobalDisplayX20+

PhonePC/2in1TabletTVWearable

getGlobalDisplayX(): number

当前拖拽点相对于全局屏幕的左上角的X坐标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于全局屏幕的左上角的X坐标。  单位：vp，取值范围：[0, +∞) |

### getGlobalDisplayY20+

PhonePC/2in1TabletTVWearable

getGlobalDisplayY(): number

当前拖拽点相对于全局屏幕的左上角的Y坐标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于全局屏幕的左上角的Y坐标。  单位：vp，取值范围：[0, +∞) |

## DragResult10+枚举说明

PhonePC/2in1TabletTVWearable

定义拖拽操作的结果及组件的落入选定状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DRAG\_SUCCESSFUL | 0 | 拖拽成功，在[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。 |
| DRAG\_FAILED | 1 | 拖拽失败，在[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。 |
| DRAG\_CANCELED | 2 | 拖拽取消，在[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。 |
| DROP\_ENABLED | 3 | 组件允许落入，在[onDragEnter](ts-universal-events-drag-drop.md#ondragenter)，[onDragMove](ts-universal-events-drag-drop.md#ondragmove)，[onDragLeave](ts-universal-events-drag-drop.md#ondragleave)中使用。 |
| DROP\_DISABLED | 4 | 组件不允许落入，在[onDragEnter](ts-universal-events-drag-drop.md#ondragenter)，[onDragMove](ts-universal-events-drag-drop.md#ondragmove)，[onDragLeave](ts-universal-events-drag-drop.md#ondragleave)中使用。 |

## DragBehavior10+

PhonePC/2in1TabletTVWearable

当设置[DragResult](ts-universal-events-drag-drop.md#dragresult10枚举说明)为DROP\_ENABLED后，可设置DragBehavior为复制（COPY）或剪切（MOVE）。当DragBehavior为复制（COPY）时，拖拽对象的角标会显示加号；为剪切（MOVE）时，拖拽对象的角标不会显示加号。DragBehavior用来向开发者描述数据的处理方式是复制（COPY）还是剪切（MOVE），但无法最终决定对数据的实际处理方式。DragBehavior会通过onDragEnd带回给数据拖出方，发起拖拽的一方可通过DragBehavior来区分做出的是复制（COPY）还是剪切（MOVE）数据的不同行为。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COPY | 0 | 指定对数据的处理方式为复制。 |
| MOVE | 1 | 指定对数据的处理方式为剪切。 |

## PreDragStatus12+枚举说明

PhonePC/2in1TabletTVWearable

定义拖拽手势触发前的各阶段状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_DETECTING\_STATUS | 0 | 拖拽手势启动阶段。(按下50ms时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| READY\_TO\_TRIGGER\_DRAG\_ACTION | 1 | 拖拽准备完成，可发起拖拽阶段。(按下500ms时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LIFT\_STARTED | 2 | 拖拽浮起动效发起阶段。(按下800ms时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LIFT\_FINISHED | 3 | 拖拽浮起动效结束阶段。(浮起动效完全结束时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LANDING\_STARTED | 4 | 拖拽落回动效发起阶段。(落回动效发起时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LANDING\_FINISHED | 5 | 拖拽落回动效结束阶段。(落回动效结束时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ACTION\_CANCELED\_BEFORE\_DRAG | 6 | 拖拽浮起落位动效中断。(已满足READY\_TO\_TRIGGER\_DRAG\_ACTION状态后，未达到动效阶段，手指抬手时触发)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREPARING\_FOR\_DRAG\_DETECTION18+ | 7 | 拖拽准备完成，可发起拖拽阶段。(按下350ms时触发)  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## UnifiedData10+

PhonePC/2in1TabletTVWearable

type UnifiedData = UnifiedData

拖拽相关的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 拖拽相关的数据。 |

## Summary10+

PhonePC/2in1TabletTVWearable

type Summary = Summary

拖拽相关数据的简介。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Summary](js-apis-data-unifieddatachannel.md#summary) | 拖拽相关数据的简介。 |

## DataLoadParams20+

PhonePC/2in1TabletTVWearable

type DataLoadParams = DataLoadParams

落入操作时使用的数据加载参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DataLoadParams](js-apis-data-unifieddatachannel.md#dataloadparams20) | 落入操作时使用的数据加载参数。 |

## DataSyncOptions15+

PhonePC/2in1TabletTVWearable

type DataSyncOptions = GetDataParams

作为startDataLoading的入参对象。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [GetDataParams](js-apis-data-unifieddatachannel.md#getdataparams15) | 表示从[UDMF](capi-udmf.md)获取数据时的参数，包含目标路径、文件冲突选项、进度条类型等。 |

## OnDragEventCallback15+

PhonePC/2in1TabletTVWearable

type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void

拖拽事件的回调函数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [DragEvent](ts-universal-events-drag-drop.md#dragevent7) | 是 | event为拖拽事件信息，包括拖拽点坐标。 |
| extraParams | string | 否 | extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。 |

## DropOptions15+

PhonePC/2in1TabletTVWearable

设置落入过程的参数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| disableDataPrefetch | boolean | 否 | 是 | 设置拖拽是否提前获取数据。true表示不提前获取数据，false表示提前获取数据，默认值为false。  **说明：**  当使用[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)获取数据时需设置该参数为true，防止拖拽提前获取数据。 |

## DragSpringLoadingConfiguration20+

PhonePC/2in1TabletTVWearable

type DragSpringLoadingConfiguration = DragSpringLoadingConfiguration

定义拖拽的悬停检测配置参数的接口。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20) | 定义拖拽的悬停检测配置参数的接口。 |

## SpringLoadingContext20+

PhonePC/2in1TabletTVWearable

type SpringLoadingContext = SpringLoadingContext

定义回调上下文信息的类，用于在悬停检测回调中传递给应用程序，使其能访问拖拽状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [SpringLoadingContext](js-apis-arkui-dragcontroller.md#springloadingcontext20) | 定义回调上下文信息的类，用于在悬停检测回调中传递给应用程序，以便应用程序能访问拖拽状态。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置组件拖拽和落入）

示例1展示了部分组件（如Image和Text等）拖拽和可落入区域的设置。

```
1. // xxx.ets
2. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. @State targetImage: string = '';
9. @State targetText: string = 'Drag Text';
10. @State imageWidth: number = 100;
11. @State imageHeight: number = 100;
12. @State imgState: Visibility = Visibility.Visible;
13. @State abstractContent: string = "abstract";
14. @State textContent: string = "";
15. @State backGroundColor: Color = Color.Transparent;

17. @Builder
18. pixelMapBuilder() {
19. Column() {
20. // $r('app.media.icon')需要替换为开发者所需的图像资源文件
21. Image($r('app.media.icon'))
22. .width(120)
23. .height(120)
24. .backgroundColor(Color.Yellow)
25. }
26. }

28. // 获取Udmf数据
29. getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
30. try {
31. let data: UnifiedData = event.getData();
32. if (!data) {
33. return false;
34. }
35. let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
36. if (!records || records.length <= 0) {
37. return false;
38. }
39. callback(event);
40. return true;
41. } catch (e) {
42. console.error(`getData failed, code = ${(e as BusinessError).code}, message = ${(e as BusinessError).message}`);
43. return false;
44. }
45. }

47. // 首次获取Udmf数据失败后自动重试
48. getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
49. if (this.getDataFromUdmfRetry(event, callback)) {
50. return;
51. }
52. setTimeout(() => {
53. this.getDataFromUdmfRetry(event, callback);
54. }, 1500);
55. }

57. // 根据拖拽发起前的不同阶段更改背景色
58. private PreDragChange(preDragStatus: PreDragStatus): void {
59. if (preDragStatus == PreDragStatus.READY_TO_TRIGGER_DRAG_ACTION) {
60. this.backGroundColor = Color.Red;
61. } else if (preDragStatus == PreDragStatus.ACTION_CANCELED_BEFORE_DRAG
62. || preDragStatus == PreDragStatus.PREVIEW_LANDING_FINISHED) {
63. this.backGroundColor = Color.Blue;
64. }
65. }

67. build() {
68. Row() {
69. Column() {
70. Text('start Drag')
71. .fontSize(18)
72. .width('100%')
73. .height(40)
74. .margin(10)
75. .backgroundColor('#008888')
76. // $r('app.media.icon')需要替换为开发者所需的图像资源文件
77. Image($r('app.media.icon'))
78. .width(100)
79. .height(100)
80. .draggable(true)
81. .margin({ left: 15 })
82. .visibility(this.imgState)
83. .onDragEnd((event) => {
84. // onDragEnd里取到的result值在接收方onDrop设置
85. if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
86. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
87. } else if (event.getResult() === DragResult.DRAG_FAILED) {
88. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
89. }
90. })
91. Text('test drag event')
92. .width('100%')
93. .height(100)
94. .draggable(true)
95. .margin({ left: 15 })
96. .copyOption(CopyOptions.InApp)
97. TextArea({ placeholder: 'please input words' })
98. .copyOption(CopyOptions.InApp)
99. .width('100%')
100. .height(50)
101. .draggable(true)
102. Search({ placeholder: 'please input you word' })
103. .searchButton('Search')
104. .width('100%')
105. .height(80)
106. .textFont({ size: 20 })

108. Column() {
109. Text('this is abstract')
110. .fontSize(20)
111. .width('100%')
112. }
113. .margin({ left: 40, top: 20 })
114. .width('100%')
115. .height(100)
116. .onDragStart((event) => {
117. this.backGroundColor = Color.Transparent;
118. let data: unifiedDataChannel.PlainText = new unifiedDataChannel.PlainText();
119. data.abstract = 'this is abstract';
120. data.textContent = 'this is content this is content';
121. (event as DragEvent).setData(new unifiedDataChannel.UnifiedData(data));
122. })
123. .onPreDrag((status: PreDragStatus) => {
124. this.PreDragChange(status);
125. })
126. .backgroundColor(this.backGroundColor)
127. }.width('45%')
128. .height('100%')

130. Column() {
131. Text('Drag Target Area')
132. .fontSize(20)
133. .width('100%')
134. .height(40)
135. .margin(10)
136. .backgroundColor('#008888')
137. Image(this.targetImage)
138. .width(this.imageWidth)
139. .height(this.imageHeight)
140. .draggable(true)
141. .margin({ left: 15 })
142. .border({ color: Color.Black, width: 1 })
143. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
144. .onDrop((dragEvent?: DragEvent) => {
145. this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
146. let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
147. let rect: Rectangle = event.getPreviewRect();
148. this.imageWidth = Number(rect.width);
149. this.imageHeight = Number(rect.height);
150. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
151. event.useCustomDropAnimation = false;
152. this.imgState = Visibility.None;
153. // 显式设置result为successful，则将该值传递给拖出方的onDragEnd
154. event.setResult(DragResult.DRAG_SUCCESSFUL);
155. })
156. })

158. Text(this.targetText)
159. .width('100%')
160. .height(100)
161. .border({ color: Color.Black, width: 1 })
162. .margin(15)
163. .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
164. .onDrop((dragEvent?: DragEvent) => {
165. this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
166. let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
167. let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
168. this.targetText = plainText.textContent;
169. })
170. })

172. Column() {
173. Text(this.abstractContent).fontSize(20).width('100%')
174. Text(this.textContent).fontSize(15).width('100%')
175. }
176. .width('100%')
177. .height(100)
178. .margin(20)
179. .border({ color: Color.Black, width: 1 })
180. .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
181. .onDrop((dragEvent?: DragEvent) => {
182. this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
183. let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
184. let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
185. this.abstractContent = plainText.abstract as string;
186. this.textContent = plainText.textContent;
187. })
188. })
189. }.width('45%')
190. .height('100%')
191. .margin({ left: '5%' })
192. }
193. .height('100%')
194. }
195. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/d5jjnpnBTBin4qYunB171Q/zh-cn_image_0000002558765986.png?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=0A88AD3D1DECFA051702A88941E432E5F076E53CBE70A0239603B833EA33A40F)

### 示例2（自定义落位动效）

从API version 18开始，示例2展示了通过自定义接口[executeDropAnimation](ts-universal-events-drag-drop.md#executedropanimation18)，实现落位动效。

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

3. @Entry
4. @Component
5. struct DropAnimationExample {
6. @State targetImage: string = '';
7. @State imageWidth: number = 100;
8. @State imageHeight: number = 100;
9. @State imgState: Visibility = Visibility.Visible;
10. customDropAnimation =
11. () => {
12. this.getUIContext().animateTo({ duration: 1000, curve: Curve.EaseOut, playMode: PlayMode.Normal }, () => {
13. this.imageWidth = 200;
14. this.imageHeight = 200;
15. this.imgState = Visibility.None;
16. })
17. }

19. build() {
20. Row() {
21. Column() {
22. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件
23. Image($r('app.media.app_icon'))
24. .width(100)
25. .height(100)
26. .draggable(true)
27. .margin({ left: 15, top: 40 })
28. .visibility(this.imgState)
29. .onDragStart((event) => {
30. })
31. .onDragEnd((event) => {
32. if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
33. console.info('Drag Success');
34. } else if (event.getResult() === DragResult.DRAG_FAILED) {
35. console.error('Drag failed');
36. }
37. })
38. }.width('45%')
39. .height('100%')

41. Column() {
42. Text('Drag Target Area')
43. .fontSize(20)
44. .width(180)
45. .height(40)
46. .textAlign(TextAlign.Center)
47. .margin(10)
48. .backgroundColor('rgb(240,250,255)')
49. Column() {
50. Image(this.targetImage)
51. .width(this.imageWidth)
52. .height(this.imageHeight)
53. }
54. .draggable(true)
55. .margin({ left: 15 })
56. .border({ color: Color.Black, width: 1 })
57. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
58. // onDrop回调，获取拖拽图片的信息和尺寸并更新显示，同时启用并执行自定义下落动画
59. .onDrop((dragEvent: DragEvent) => {
60. let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
61. let rect: Rectangle = dragEvent.getPreviewRect();
62. this.imageWidth = Number(rect.width);
63. this.imageHeight = Number(rect.height);
64. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
65. dragEvent.useCustomDropAnimation = true;
66. dragEvent.executeDropAnimation(this.customDropAnimation)
67. })
68. .width(this.imageWidth)
69. .height(this.imageHeight)
70. }.width('45%')
71. .height('100%')
72. .margin({ left: '5%' })
73. }
74. .height('100%')
75. }
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/7rprE33QQB2qM2Ptwhq5Rg/zh-cn_image_0000002558606330.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=2AFF1BCFAC1E008886789835AEBB31627BB9E835F8EF8518B5BC849CFDC028AA)

### 示例3（拖拽异步获取数据）

从API version 15开始，示例3展示了通过[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)实现拖拽异步获取数据。

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. import { fileUri, fileIo as fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct ImageExample {
8. @State uri: string = "";
9. @State blockArr: string[] = [];
10. uiContext = this.getUIContext();
11. udKey: string = '';

13. build() {
14. Column() {
15. Text('Image拖拽')
16. .fontSize('30dp')
17. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
18. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
19. Image($r('app.media.startIcon'))
20. .width(100)
21. .height(100)
22. .border({ width: 1 })
23. .draggable(true)
24. .onDragStart((event: DragEvent) => {
25. const context: Context | undefined = this.uiContext.getHostContext();
26. if (context) {
27. let data = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id, 120);
28. const arrayBuffer: ArrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
29. let filePath = context.filesDir + '/test.png';
30. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
31. fileIo.writeSync(file.fd, arrayBuffer);
32. // 获取图片的uri
33. let uri = fileUri.getUriFromPath(filePath);
34. let image: unifiedDataChannel.Image = new unifiedDataChannel.Image();
35. image.imageUri = uri;
36. let dragData: unifiedDataChannel.UnifiedData = new unifiedDataChannel.UnifiedData(image);
37. (event as DragEvent).setData(dragData);
38. }
39. })
40. }
41. .margin({ bottom: 20 })

43. Row() {
44. Column() {
45. Text('可释放区域')
46. .fontSize('15dp')
47. .height('10%')
48. List() {
49. ForEach(this.blockArr, (item: string, index) => {
50. ListItem() {
51. Image(item)
52. .width(100)
53. .height(100)
54. .border({ width: 1 })
55. }
56. .margin({ left: 30, top: 30 })
57. }, (item: string) => item)
58. }
59. .border({ width: 1 })
60. .height('90%')
61. .width('100%')
62. .onDrop((event?: DragEvent, extraParams?: string) => {
63. console.info("enter onDrop")
64. let context = this.uiContext.getHostContext() as common.UIAbilityContext;
65. let pathDir: string = context.distributedFilesDir;
66. let destUri = fileUri.getUriFromPath(pathDir);
67. // 创建DataProgressListener监听数据传输进度
68. let progressListener: unifiedDataChannel.DataProgressListener =
69. (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
70. if (dragData != null) {
71. // 获取数据记录数组
72. let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
73. if (arr.length > 0) {
74. // 检查首记录类型是否为IMAGE
75. if (arr[0].getType() === uniformTypeDescriptor.UniformDataType.IMAGE) {
76. // 类型匹配成功，记录数据Uri
77. let image = arr[0] as unifiedDataChannel.Image;
78. this.uri = image.imageUri;
79. this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
80. }
81. } else {
82. console.info('dragData arr is null');
83. }
84. } else {
85. console.info('dragData is undefined');
86. }
87. console.info(`percentage: ${progress.progress}`);
88. };
89. // 设置异步数据加载参数项
90. let options: DataSyncOptions = {
91. destUri: destUri,
92. fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
93. progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
94. dataProgressListener: progressListener,
95. }
96. try {
97. // 启动数据传输
98. this.udKey = (event as DragEvent).startDataLoading(options);
99. console.info(`udKey: ${this.udKey}`);
100. } catch (e) {
101. console.error(`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
102. }
103. }, { disableDataPrefetch: true })
104. }
105. .height("50%")
106. .width("90%")
107. .border({ width: 1 })
108. }

110. Button('取消数据传输')
111. .onClick(() => {
112. try {
113. this.getUIContext().getDragController().cancelDataLoading(this.udKey);
114. } catch (e) {
115. console.error(`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
116. }
117. })
118. .margin({ top: 10 })
119. }.width('100%')
120. }
121. }
```

### 示例4（获取当前拖拽的屏幕ID）

从API version 20开始，示例4展示了通过onDragXXX（不支持onDragEnd）接口获取到拖拽事件，并调用拖拽事件里的[getDisplayId](ts-universal-events-drag-drop.md#getdisplayid20)接口获取屏幕ID。

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State targetImage: string = '';
8. @State imageWidth: number = 100;
9. @State imageHeight: number = 100;
10. @State imgState: Visibility = Visibility.Visible;
11. @State backGroundColor: Color = Color.Transparent;
12. @State startDisplayId: number = -1;
13. @State enterDisplayId: number = -1;
14. @State moveDisplayId: number = -1;
15. @State leaveDisplayId: number = -1;
16. @State dropDisplayId: number = -1;

18. @Builder
19. pixelMapBuilder() {
20. Column() {
21. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件
22. Image($r('app.media.app_icon'))
23. .width(120)
24. .height(120)
25. .backgroundColor(Color.Yellow)
26. }
27. }

29. getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
30. try {
31. let data: UnifiedData = event.getData();
32. if (!data) {
33. return false;
34. }
35. let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
36. if (!records || records.length <= 0) {
37. return false;
38. }
39. callback(event);
40. return true;
41. } catch (e) {
42. console.error(`getData failed, code = ${(e as BusinessError).code}, message = ${(e as BusinessError).message}`);
43. return false;
44. }
45. }

47. getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
48. if (this.getDataFromUdmfRetry(event, callback)) {
49. return;
50. }
51. setTimeout(() => {
52. this.getDataFromUdmfRetry(event, callback);
53. }, 1500);
54. }

56. private PreDragChange(preDragStatus: PreDragStatus): void {
57. if (preDragStatus == PreDragStatus.READY_TO_TRIGGER_DRAG_ACTION) {
58. this.backGroundColor = Color.Red;
59. } else if (preDragStatus == PreDragStatus.ACTION_CANCELED_BEFORE_DRAG
60. || preDragStatus == PreDragStatus.PREVIEW_LANDING_FINISHED) {
61. this.backGroundColor = Color.Blue;
62. }
63. }

65. build() {
66. Row() {
67. Column() {
68. Text('start Drag')
69. .fontSize(18)
70. .width('100%')
71. .height(40)
72. .margin(10)
73. .backgroundColor('#008888')
74. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
75. Image($r('app.media.startIcon'))
76. .width(100)
77. .height(100)
78. .draggable(true)
79. .margin({ left: 15 })
80. .visibility(this.imgState)
81. .onDragStart((event) => {
82. let id = event.getDisplayId();
83. this.startDisplayId = id;
84. })

86. .onDragEnd((event) => {
87. if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
88. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
89. } else if (event.getResult() === DragResult.DRAG_FAILED) {
90. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
91. }
92. })

94. Text('displayID in onDragStart: ' + this.startDisplayId.toString())
95. .width('100%')
96. .height(50)
97. .draggable(true)
98. .margin({ left: 15 })
99. Text('displayID in onDragEnter: ' + this.enterDisplayId.toString())
100. .width('100%')
101. .height(50)
102. .draggable(true)
103. .margin({ left: 15 })
104. Text('displayID in onDragMove: ' + this.moveDisplayId.toString())
105. .width('100%')
106. .height(50)
107. .draggable(true)
108. .margin({ left: 15 })
109. Text('displayID in onDragLeave: ' + this.leaveDisplayId.toString())
110. .width('100%')
111. .height(50)
112. .draggable(true)
113. .margin({ left: 15 })
114. Text('displayID in onDrop: ' + this.dropDisplayId.toString())
115. .width('100%')
116. .height(50)
117. .draggable(true)
118. .margin({ left: 15 })
119. .onPreDrag((status: PreDragStatus) => {
120. this.PreDragChange(status);
121. })
122. }.width('45%')
123. .height('100%')

125. Column() {
126. Text('Drag Target Area')
127. .fontSize(20)
128. .width('100%')
129. .height(40)
130. .margin(10)
131. .backgroundColor('#008888')
132. Image(this.targetImage)
133. .width(this.imageWidth)
134. .height(this.imageHeight)
135. .draggable(true)
136. .margin({ left: 15 })
137. .border({ color: Color.Black, width: 1 })
138. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
139. .onDragEnter((event) => {
140. let id = event.getDisplayId();
141. this.enterDisplayId = id;
142. })
143. .onDragMove((event) => {
144. let id = event.getDisplayId();
145. this.moveDisplayId = id;
146. })
147. .onDragLeave((event) => {
148. let id = event.getDisplayId();
149. this.leaveDisplayId = id;
150. })
151. .onDrop((dragEvent: DragEvent) => {
152. let id = dragEvent.getDisplayId();
153. this.dropDisplayId = id;
154. this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
155. let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
156. let rect: Rectangle = event.getPreviewRect();
157. this.imageWidth = Number(rect.width);
158. this.imageHeight = Number(rect.height);
159. this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
160. event.useCustomDropAnimation = false;
161. this.imgState = Visibility.None;
162. event.setResult(DragResult.DRAG_SUCCESSFUL);
163. })
164. })
165. }.width('45%')
166. .height('100%')
167. .margin({ left: '5%' })
168. }
169. .height('100%')
170. }
171. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/gtIBg9sBRtixBeFnzCaP2A/zh-cn_image_0000002589325857.png?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=D70ABCA994A6A919815752B6598B434AB9644683E556A3CA5434CFF8D6854442)

### 示例5（获取包名和是否是跨设备）

从API version 20开始，示例5展示了通过onDragXXX接口获取到拖拽事件，调用拖拽事件里的[getDragSource](ts-universal-events-drag-drop.md#getdragsource20)接口获取包名，调用isRemote接口获取是否是跨设备。

```
1. @Entry
2. @Component
3. struct Index {
4. @State targetImage: string = '';
5. @State startDragSource: string = '';
6. @State startIsRemote: boolean = true;
7. @State enterDragSource: string = '';
8. @State enterIsRemote: boolean = true;

10. build() {
11. Column() {
12. Row() {
13. Column() {
14. Text('start Drag Area')
15. .fontSize(18)
16. .width('100%')
17. .height(40)
18. .margin(10)
19. .backgroundColor('#008888')
20. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
21. Image($r('app.media.startIcon'))
22. .onDragStart((event) => {
23. this.startDragSource = (event as DragEvent).getDragSource();
24. this.startIsRemote = (event as DragEvent).isRemote();
25. })
26. .width(100)
27. .height(100)
28. .draggable(true)
29. .margin({ left: 15 })
30. }
31. .border({ color: Color.Black, width: 1 })
32. .width('45%')
33. .height('50%')

35. Column() {
36. Text('Drag Target Area')
37. .fontSize(20)
38. .width('100%')
39. .height(40)
40. .margin(10)
41. .backgroundColor('#008888')
42. Image(this.targetImage)
43. .width(100)
44. .height(100)
45. .draggable(true)
46. .margin({ left: 15 })
47. .border({ color: Color.Black, width: 1 })
48. .onDragEnter((event) => {
49. this.enterDragSource = (event as DragEvent).getDragSource();
50. this.enterIsRemote = (event as DragEvent).isRemote();
51. })
52. .onDrop(() => {
53. })
54. }
55. .border({ color: Color.Black, width: 1 })
56. .width('45%')
57. .height('50%')
58. .margin({ left: '5%' })
59. }
60. .height('70%')

62. Text('onDragStart dragSource: ' + this.startDragSource.toString() + '\n' + 'onDragStart isRemote: ' +
63. this.startIsRemote.toString())
64. .width('100%')
65. .height(50)
66. .margin({ left: 15 })
67. Text('onDragEnter dragSource: ' + this.enterDragSource.toString() + '\n' + 'onDragEnter isRemote: ' +
68. this.enterIsRemote.toString())
69. .width('100%')
70. .height(50)
71. .margin({ left: 15 })
72. }
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Rz30_3jORJqugvzVneBmmQ/zh-cn_image_0000002589245799.png?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=FBC92864FBCC610748B49CEF8A8D009221A5091912D00BAF8CC696292250DBD6)

### 示例6（拖拽支持悬停检测）

从API version 20开始，示例6展示了通过[onDragSpringLoading](ts-universal-events-drag-drop.md#ondragspringloading20)接口注册回调，并调用[SpringLoadingContext](ts-universal-events-drag-drop.md#springloadingcontext20)接口获取上下文（当前状态、通知序列）。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State targetText: string = 'Drag Text';
6. @State state: number = 0;
7. @State currentNotifySequence: number = 0;
8. @State config: DragSpringLoadingConfiguration = {
9. stillTimeLimit: 200,
10. updateInterval: 300,
11. updateNotifyCount: 4,
12. updateToFinishInterval: 300
13. };

15. build() {
16. Row() {
17. Column() {
18. Text('start Drag')
19. .fontSize(18)
20. .width('100%')
21. .height(40)
22. .margin(10)
23. .backgroundColor('#008888')
24. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
25. Image($r('app.media.startIcon'))
26. .id("ori_image")
27. .width(100)
28. .height(100)
29. .draggable(true)
30. .margin({ left: 15 })
31. Text('当前状态是： ' + this.state)
32. .fontSize(18)
33. .width('100%')
34. .height(40)
35. .margin(10)
36. Text('当前通知序列是： ' + this.currentNotifySequence)
37. .fontSize(18)
38. .width('100%')
39. .height(40)
40. .margin(10)
41. }
42. .width('45%')
43. .height('100%')

45. Column() {
46. Text('Drag Target Area')
47. .fontSize(20)
48. .width('100%')
49. .height(40)
50. .margin(10)
51. .backgroundColor('#008888')
52. .id("text")
53. Image("")
54. .width(100)
55. .height(100)
56. .draggable(true)
57. .margin({ left: 15 })
58. .border({ color: Color.Black, width: 2 })
59. .onDragSpringLoading((context: SpringLoadingContext) => {
60. this.state = context.state;
61. this.currentNotifySequence = context.currentNotifySequence;
62. }, this.config)
63. }
64. .width('45%')
65. .height('100%')
66. .margin({ left: '5%' })
67. .onDragSpringLoading((context: SpringLoadingContext) => {
68. this.state = context.state;
69. this.currentNotifySequence = context.currentNotifySequence;
70. }, this.config)
71. .id("column")
72. .backgroundColor(Color.Grey)
73. }
74. .height('100%')
75. }
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ZMM3hr4lQKSxNckMVqCO4Q/zh-cn_image_0000002558765988.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=D714A4DEA3AFE73690E5458DB87041850389C4F5695671696914AC7805FFE159)

### 示例7（拖起方延迟提供数据）

从API version 20开始，示例7展示了在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中调用[setDataLoadParams](ts-universal-events-drag-drop.md#setdataloadparams20)延迟提供数据接口，并在[onDrop](ts-universal-events-drag-drop.md#ondrop)中调用[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)异步获取数据接口。

```
1. import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { fileUri, fileIo as fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct VideoExample {
8. @State uri: string = "";
9. @State blockArr: string[] = [];
10. uiContext = this.getUIContext();
11. udKey: string = '';

13. build() {
14. Column() {
15. Text('video拖拽')
16. .fontSize('30dp')
17. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
18. // $rawfile('test1.mp4')需要替换为开发者所需的资源文件
19. Video({ src: $rawfile('test1.mp4'), controller: new VideoController() })
20. .width(200)
21. .height(200)
22. .border({ width: 1 })
23. .draggable(true)
24. .onDragStart((event: DragEvent) => {
25. const context: Context | undefined = this.uiContext.getHostContext();
26. if (context) {
27. let loadHandler: unifiedDataChannel.DataLoadHandler = (acceptableInfo) => {
28. console.info(`acceptableInfo recordCount ${acceptableInfo?.recordCount}`);
29. if (acceptableInfo?.types) {
30. console.info(`acceptableInfo types ${Array.from(acceptableInfo.types)}`);
31. } else {
32. console.error('acceptableInfo types is undefined');
33. }
34. let data = context.resourceManager.getRawFdSync('test1.mp4');
35. let filePath = context.filesDir + '/test1.mp4';
36. let file: fileIo.File = null!;
37. try {
38. file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
39. let bufferSize = data.length as number;
40. let buf = new ArrayBuffer(bufferSize);
41. fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
42. fileIo.writeSync(file.fd, buf, { offset: 0, length: bufferSize });
43. } catch (error) {
44. console.error(`openSync errorCode: ${error.code}, errorMessage: ${error.message}`);
45. } finally {
46. fileIo.closeSync(file.fd);
47. }
48. context.resourceManager.closeRawFdSync('test1.mp4')
49. this.uri = fileUri.getUriFromPath(filePath);
50. let videoMp: uniformDataStruct.FileUri = {
51. uniformDataType: 'general.file-uri',
52. oriUri: this.uri,
53. fileType: 'general.video',
54. }
55. let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
56. let unifiedData = new unifiedDataChannel.UnifiedData();
57. unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, videoMp);
58. unifiedData.addRecord(unifiedRecord);
59. return unifiedData;
60. }
61. (event as DragEvent).setDataLoadParams({
62. loadHandler: loadHandler,
63. dataLoadInfo: { types: new Set([uniformTypeDescriptor.UniformDataType.FILE_URI]), recordCount: 1 }
64. });
65. }
66. })
67. }
68. .margin({ bottom: 20 })

70. Row() {
71. Column() {
72. Text('可释放区域')
73. .fontSize('15dp')
74. .height('10%')
75. List() {
76. ForEach(this.blockArr, (item: string, index) => {
77. ListItem() {
78. Video({ src: item, controller: new VideoController() })
79. .width(100)
80. .height(100)
81. .border({ width: 1 })
82. }
83. .margin({ left: 30, top: 30 })
84. }, (item: string) => item)
85. }
86. .border({ width: 1 })
87. .height('90%')
88. .width('100%')
89. .onDrop((event: DragEvent, extraParams?: string) => {
90. let context = this.uiContext.getHostContext() as common.UIAbilityContext;
91. let pathDir: string = context.distributedFilesDir;
92. let destUri = fileUri.getUriFromPath(pathDir);
93. let progressListener: unifiedDataChannel.DataProgressListener =
94. (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
95. if (dragData != null) {
96. let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
97. if (arr.length > 0) {
98. if (arr[0].getType() === uniformTypeDescriptor.UniformDataType.VIDEO) {
99. this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
100. }
101. } else {
102. console.info('dragData arr is null');
103. }
104. } else {
105. console.info('dragData is undefined');
106. }
107. console.info(`percentage: ${progress.progress}`);
108. };
109. let info: unifiedDataChannel.DataLoadInfo =
110. { types: new Set([uniformTypeDescriptor.UniformDataType.VIDEO]), recordCount: 100 }
111. let options: DataSyncOptions = {
112. destUri: destUri,
113. fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
114. progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
115. dataProgressListener: progressListener,
116. acceptableInfo: info,
117. }
118. try {
119. this.udKey = (event as DragEvent).startDataLoading(options);
120. console.info(`udKey: ${this.udKey}`);
121. } catch (e) {
122. console.error(`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
123. }
124. }, { disableDataPrefetch: true })
125. }
126. .height("50%")
127. .width("90%")
128. .border({ width: 1 })
129. }

131. Button('取消数据传输')
132. .onClick(() => {
133. try {
134. this.getUIContext().getDragController().cancelDataLoading(this.udKey);
135. } catch (e) {
136. console.error(`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
137. }
138. })
139. .margin({ top: 10 })
140. }.width('100%')
141. }
142. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/_6sUW1R1SYWDbjDNA-E1FA/zh-cn_image_0000002558606332.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=4F22554715AD1418DAE3B81FF8FE2E598B88B2089D341473BC8ED24BED6D9D89)
