---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop
title: 拖拽事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 拖拽事件
category: harmonyos-references
scraped_at: 2026-09-05T06:17:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c768e81090989b239ddde45037789d8d326989a71365288d7826715d1e74e91f
---

拖拽事件是指在用户界面中，当用户拖动某个对象（如文件、控件或元素）时触发的一系列事件。这些事件允许开发者自定义拖拽行为，实现诸如拖放、调整位置等功能。

**说明** 

* 从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 应用本身预置的资源文件（即应用在安装前的HAP包中已经存在的资源文件）仅支持本地应用内拖拽。

ArkUI框架对以下组件实现了默认的拖拽能力，支持对数据的拖出或拖入响应。开发者也可以通过实现通用拖拽事件来自定义拖拽能力。

* 默认支持拖出能力的组件（可从组件上拖出数据）：[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)、[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)、[Hyperlink](ts-container-hyperlink.md)，开发者可通过设置这些组件的[draggable](ts-universal-attributes-drag-drop.md#draggable)属性来控制对默认拖拽能力的使用。
* 默认支持拖入能力的组件（目标组件可响应拖入数据）：[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)，开发者可通过设置这些组件的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)属性为null来禁用对默认拖入能力的支持。

其他支持拖出能力的组件需要开发者将[draggable](ts-universal-attributes-drag-drop.md#draggable)属性设置为true，并在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)等接口中实现数据传输相关内容，才能正确处理拖拽能力。

Text、TextInput、TextArea、Hyperlink、Image、RichEditor和Web组件的draggable属性默认为true，默认支持拖出能力。

**说明** 

Text组件需配合[copyOption](ts-basic-components-text.md#copyoption9)一起使用，设置copyOption为CopyOptions.InApp或者CopyOptions.LocalDevice。

## onDragStart

onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T

在手势拖拽场景中，在可拖拽的组件上长按时间超过500ms，然后手指移动距离大于10vp时触发此回调；在鼠标拖拽场景中，鼠标左键在可拖拽的组件上按下并移动超过1vp时，即可触发此回调。

针对默认支持拖拽能力的组件，如果开发者设置了onDragStart，优先执行onDragStart，并根据执行情况决定是否使用系统默认的拖拽能力，具体规则为：

* 如果开发者返回了自定义预览图，则不再使用系统默认的拖拽预览图；
* 如果开发者设置了拖拽数据，则不再使用系统默认填充的拖拽数据。

文本类组件[Text](ts-basic-components-text.md)、[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)对选中的文本内容进行拖拽时，不支持自定义预览图。当onDragStart与菜单预览一起使用或使用了默认支持拖拽能力的组件时，预览及菜单项上的自定义内容不支持拖拽。

**说明** 

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

onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T

绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。如果开发者没有在onDrop中主动调用event.[setResult](ts-universal-events-drag-drop.md#setresult10)()设置拖拽接收的结果，若拖拽组件为系统支持默认拖入的组件，以系统实际处理数据结果为准，其他组件则系统按照数据接收成功处理。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventCallback | [OnDragEventCallback](ts-universal-events-drag-drop.md#ondrageventcallback15) | 是 | 拖拽释放事件的回调函数，用于在组件作为拖拽释放目标并触发onDrop时接收拖拽事件信息。 |
| dropOptions | [DropOptions](ts-universal-events-drag-drop.md#dropoptions15) | 否 | 落入过程的参数。当需要配置拖拽落入过程行为（如禁用数据预获取）时传入；不传入时使用默认落入配置，默认提前获取拖拽数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragEnd10+

onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T

绑定此事件的组件触发的拖拽结束后，触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

onPreDrag(callback: Callback<PreDragStatus>): T

绑定此事件的组件，当处于手势拖拽发起前的不同阶段时，触发回调。拖拽发起前的各阶段可参考[PreDragStatus](ts-universal-events-drag-drop.md#predragstatus12枚举说明)。此接口不支持在鼠标拖拽中触发。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PreDragStatus](ts-universal-events-drag-drop.md#predragstatus12枚举说明)> | 是 | 拖拽发起前状态变化的回调函数，用于接收当前拖拽手势触发前所处阶段。回调参数为PreDragStatus，表示拖拽发起前的各阶段状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onDragSpringLoading20+

onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T

绑定此事件的组件可作为具有悬停检测功能的拖拽响应目标。当拖拽对象悬停在目标上时，触发回调通知。此时只有一个目标可以成为响应方，并且子组件始终具有更高的响应优先级。

关于悬停检测的触发机制及详细使用方法，请参考开发指南[支持悬停检测](../harmonyos-guides/arkts-common-events-drag-event.md#支持悬停检测)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SpringLoadingContext](ts-universal-events-drag-drop.md#springloadingcontext20)> | null | 是 | 悬停检测回调函数，当值为null时禁用悬停检测。 |
| configuration | [DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20) | 否 | 悬停检测配置信息。当需要自定义悬停检测的触发时长、更新间隔或通知次数等行为时传入；不传入或为undefined时取[DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20)默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## DragItemInfo

定义拖拽过程中拖拽项的相关信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 设置拖拽过程中显示的图片。未设置时不使用图片作为拖拽预览。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 拖拽过程中显示自定义组件，未设置时不使用自定义组件作为拖拽预览。如果设置了pixelMap，则忽略此值。  **说明：**  不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，建议配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true以开启同步加载。该builder只用于生成当次拖拽中显示的图片，builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。  builder传参时，建议传参格式为builder: ()=>{this.customBuilder()}，用以保证this指向的正确性。具体请参考[将@Builder装饰的函数当作CustomBuilder类型使用](../harmonyos-guides/arkts-builder.md#将builder装饰的函数当作custombuilder类型使用)。 |
| extraInfo | string | 否 | 是 | 拖拽项的附加信息，用于描述拖拽项。未设置时无附加信息。 |

## PreviewConfiguration15+

配置自定义拖拽过程中的预览图样式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onlyForLifting | boolean | 否 | 是 | 自定义配置的预览图是否仅用于浮起。  **说明：**  默认值为false。true表示自定义预览图仅用于浮起，false表示可用于浮起和拖拽。设置为true时，如果发起长按拖拽，浮起时的预览图为自定义配置的预览图，拖拽时的预览图不使用[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)属性，优先使用开发者在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中返回的预览图，如果[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中没有返回预览图则使用组件自截图。 |
| delayCreating | boolean | 否 | 是 | 组件预览builder是否在设置时加载。  默认值为false。true表示组件预览builder在设置时加载，false表示组件预览builder不在设置时加载。 |

## extraParams说明

用于返回组件在拖拽中需要用到的额外信息。

extraParams是由JSON对象转换得到的string，可通过JSON.parse解析后获取如下属性。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| selectedIndex | number | 当拖拽事件设在父容器的子元素时，selectedIndex表示当前被拖拽子元素是父容器第selectedIndex个子元素，selectedIndex从0开始。  仅在[ListItem](ts-container-listitem.md)组件的拖拽事件中生效，否则返回undefined。 |
| insertIndex | number | 当前拖拽元素在List组件中放下时，insertIndex表示被拖拽元素插入该组件的第insertIndex个位置，insertIndex从0开始。  仅在[List](ts-container-list.md)组件的拖拽事件中生效，否则返回undefined。 |

## DragEvent7+

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| useCustomDropAnimation10+ | boolean | 否 | 否 | 当拖拽结束时，是否禁用系统默认落位动效。  应用可将该值设定为true来禁用系统默认落位动效，并实现自定义落位动效。  当不配置或设置为false时，系统默认落位动效生效，当[setResult](ts-universal-events-drag-drop.md#setresult10)设置为DRAG\_SUCCESSFUL时，落位为缩小消失动效，不为DRAG\_SUCCESSFUL时，则为放大消失动效。  当未禁用系统默认落位动效时，应用不应再实现自定义动效，以避免动效上的冲突。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| autoHideComponentUniqueIds | number | number[] | 否 | 是 | 设置拖拽过程中需要自动隐藏的组件uniqueId，支持传入单个uniqueId或数组。  仅在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)回调中设置生效。拖拽成功发起后，系统会在显示拖拽预览窗口前隐藏目标组件。  若拖拽源本身也需要隐藏，需要同时传入拖拽源组件的uniqueId。  组件的uniqueId可通过[UIContext.getFrameNodeById()](arkts-apis-uicontext-uicontext.md#getframenodebyid12)配合[FrameNode.getUniqueId()](js-apis-arkui-framenode.md#getuniqueid12)获取。  开发者应在[onDragEnd](ts-universal-events-drag-drop.md#ondragend10)或[onDrop](ts-universal-events-drag-drop.md#ondrop)中恢复组件显示状态。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| dragBehavior10+ | [DragBehavior](ts-universal-events-drag-drop.md#dragbehavior10) | 否 | 否 | 切换复制和剪切模式的角标显示状态。  默认值：DragBehavior.COPY。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

### setData10+

setData(unifiedData: UnifiedData): void

向DragEvent中设置用于拖拽的数据。与[setDataLoadParams](ts-universal-events-drag-drop.md#setdataloadparams20)方法同时使用时，以最后调用的方法为准。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unifiedData | [UnifiedData](ts-universal-events-drag-drop.md#unifieddata10) | 是 | 拖拽相关的数据。 |

### getData10+

getData(): UnifiedData

获取拖拽相关数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

getSummary(): Summary

获取所拖拽数据的概要，包括数据类型及大小信息；在延迟拖拽场景下，只能获取到数据类型信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Summary](ts-universal-events-drag-drop.md#summary10) | 拖拽相关数据的概要。 |

### setResult10+

setResult(dragResult: DragResult): void

在DragEvent中设置拖拽结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dragResult | [DragResult](ts-universal-events-drag-drop.md#dragresult10枚举说明) | 是 | 拖拽结果。 |

### getResult10+

getResult(): DragResult

获取拖拽结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DragResult](ts-universal-events-drag-drop.md#dragresult10枚举说明) | 从DragEvent中获取的拖拽结果。 |

### getPreviewRect10+

getPreviewRect(): Rectangle

获取拖拽预览图相对于当前窗口的位置，以及预览图尺寸信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 拖拽预览图相对于当前窗口的位置，以及预览图尺寸信息，单位vp，其中x和y代表预览图左上角的窗口坐标，width和height代表预览图的尺寸。 |

### getVelocityX10+

getVelocityX(): number

获取当前拖拽的x轴方向拖动速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽的x轴方向拖动速度。坐标轴原点为屏幕左上角，单位为vp/s，分正负方向速度，从左往右为正，反之为负。 |

### getVelocityY10+

getVelocityY(): number

获取当前拖拽的y轴方向拖动速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽的y轴方向拖动速度。坐标轴原点为屏幕左上角，单位为vp/s，分正负方向速度，从上往下为正，反之为负。 |

### getVelocity10+

getVelocity(): number

获取当前拖拽的主方向拖动速度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽的主方向拖动速度。为xy轴方向速度的平方和的算术平方根，单位为vp/s。 |

### getWindowX10+

getWindowX(): number

获取拖拽点相对于窗口左上角的x轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于窗口左上角的x轴坐标，单位为vp。 |

### getWindowY10+

getWindowY(): number

获取拖拽点相对于窗口左上角的y轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于窗口左上角的y轴坐标，单位为vp。 |

### getDisplayX10+

getDisplayX(): number

获取当前拖拽点相对于屏幕左上角的x轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于屏幕左上角的x轴坐标，单位为vp。 |

### getDisplayY10+

getDisplayY(): number

获取当前拖拽点相对于屏幕左上角的y轴坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽点相对于屏幕左上角的y轴坐标，单位为vp。 |

### getModifierKeyState12+

getModifierKeyState?(keys: Array<string>): boolean

获取修饰键按压状态。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array<string> | 是 | 获取修饰键按压状态。报错信息请参考以下错误码。支持功能键 'Ctrl' | 'Alt' | 'Shift'。  **说明：**  此接口不支持在手写笔场景下使用。 |

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

startDataLoading(options: DataSyncOptions): string

异步获取拖拽数据，并通知开发者当前数据同步进度，仅支持在onDrop阶段使用。使用该接口获取数据时，需将[DropOptions](ts-universal-events-drag-drop.md#dropoptions15)中的disableDataPrefetch设置为true，防止拖拽提前获取数据。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

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

executeDropAnimation(customDropAnimation: Callback<void>): void

设置自定义落位动效的执行函数，仅在[useCustomDropAnimation](ts-universal-events-drag-drop.md#属性)为true时有效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customDropAnimation | [Callback<void>](js-apis-base.md#callback) | 是 | 在此回调函数中实现自定义落位动效。  **说明：**  1. 该接口仅在onDrop回调中使用有效。  2. 使用前需设置useCustomDropAnimation为true，否则该接口不生效。  3. 不要在动画callback中实现与动效无关的逻辑，避免影响执行效率。 |

### getDisplayId20+

getDisplayId(): number

获取当前拖拽事件发生时所在的屏幕ID，可用于多屏设备拖拽场景中识别拖拽发生的屏幕并适配目标屏幕处理逻辑，不支持在[onDragEnd](ts-universal-events-drag-drop.md#ondragend10)阶段使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前拖拽事件发生时所在的屏幕ID。 |

### getDragSource20+

getDragSource(): string

获取拖起方包名，可用于跨应用拖拽场景中识别数据来源应用，并根据来源应用进行数据接收校验或业务处理。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 拖起方的包名。 |

### isRemote20+

isRemote(): boolean

获取是否是跨设备拖拽，跨设备拖拽时为true，可用于跨设备拖拽场景中区分本机拖拽和跨设备拖拽，并据此调整数据传输、权限校验或提示逻辑。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否是跨设备拖拽，返回true表示是跨设备拖拽，返回false表示不是跨设备拖拽。 |

### setDataLoadParams20+

setDataLoadParams(dataLoadParams: DataLoadParams): void

设置起拖方延迟提供数据。使用此方法向系统提供数据加载参数，而不是直接提供完整的数据对象。当用户在目标应用上落入时，系统将使用此参数从起拖方请求实际数据。与[setData](ts-universal-events-drag-drop.md#setdata10)方法同时使用，以最后调用的方法为准。该接口仅在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)回调中生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataLoadParams | [DataLoadParams](ts-universal-events-drag-drop.md#dataloadparams20) | 是 | 起拖方延迟提供数据时使用的数据加载参数，用于在目标应用落入时向系统提供实际拖拽数据的加载方式。 |

### getX(deprecated)

getX(): number

当前拖拽点相对于窗口左上角的x轴坐标，单位为vp。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[getWindowX](ts-universal-events-drag-drop.md#getwindowx10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于窗口左上角的x轴坐标。  单位：vp |

### getY(deprecated)

getY(): number

当前拖拽点相对于窗口左上角的y轴坐标，单位为vp。

**说明** 

从API version 7开始支持，从API version 10开始废弃，建议使用[getWindowY](ts-universal-events-drag-drop.md#getwindowy10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于窗口左上角的y轴坐标。  单位：vp |

### getGlobalDisplayX20+

getGlobalDisplayX(): number

当前拖拽点相对于全局屏幕的左上角的X坐标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于全局屏幕的左上角的X坐标。  单位：vp，取值范围：(-∞, +∞) |

### getGlobalDisplayY20+

getGlobalDisplayY(): number

当前拖拽点相对于全局屏幕的左上角的Y坐标。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前拖拽点相对于全局屏幕的左上角的Y坐标。  单位：vp，取值范围：(-∞, +∞) |

## DragResult10+枚举说明

定义拖拽操作的结果及组件的落入选定状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN24+ | -1 | 拖拽结果尚未设置，在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)，[onDragEnter](ts-universal-events-drag-drop.md#ondragenter)，[onDragMove](ts-universal-events-drag-drop.md#ondragmove)，[onDragLeave](ts-universal-events-drag-drop.md#ondragleave)，[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| DRAG\_SUCCESSFUL | 0 | 拖拽成功，在[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DRAG\_FAILED | 1 | 拖拽失败，在[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DRAG\_CANCELED | 2 | 拖拽取消，在[onDrop](ts-universal-events-drag-drop.md#ondrop)中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DROP\_ENABLED | 3 | 组件允许落入，在[onDragEnter](ts-universal-events-drag-drop.md#ondragenter)，[onDragMove](ts-universal-events-drag-drop.md#ondragmove)，[onDragLeave](ts-universal-events-drag-drop.md#ondragleave)中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DROP\_DISABLED | 4 | 组件不允许落入，在[onDragEnter](ts-universal-events-drag-drop.md#ondragenter)，[onDragMove](ts-universal-events-drag-drop.md#ondragmove)，[onDragLeave](ts-universal-events-drag-drop.md#ondragleave)中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## DragBehavior10+

当设置[DragResult](ts-universal-events-drag-drop.md#dragresult10枚举说明)为DROP\_ENABLED后，可设置DragBehavior为复制（COPY）或剪切（MOVE）。当DragBehavior为复制（COPY）时，拖拽对象的角标会显示加号；为剪切（MOVE）时，拖拽对象的角标不会显示加号。DragBehavior用来向开发者描述数据的处理方式是复制（COPY）还是剪切（MOVE），但无法最终决定对数据的实际处理方式。DragBehavior会通过onDragEnd带回给数据拖出方，发起拖拽的一方可通过DragBehavior区分数据处理方式是复制（COPY）还是剪切（MOVE）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COPY | 0 | 指定对数据的处理方式为复制。 |
| MOVE | 1 | 指定对数据的处理方式为剪切。 |

## PreDragStatus12+枚举说明

定义拖拽手势触发前的各阶段状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_DETECTING\_STATUS | 0 | 拖拽手势启动阶段。（按下50ms时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| READY\_TO\_TRIGGER\_DRAG\_ACTION | 1 | 拖拽准备完成，可发起拖拽阶段。（按下500ms时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LIFT\_STARTED | 2 | 拖拽浮起动效发起阶段。（按下800ms时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LIFT\_FINISHED | 3 | 拖拽浮起动效结束阶段。（浮起动效完全结束时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LANDING\_STARTED | 4 | 拖拽落回动效发起阶段。（落回动效发起时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREVIEW\_LANDING\_FINISHED | 5 | 拖拽落回动效结束阶段。（落回动效结束时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ACTION\_CANCELED\_BEFORE\_DRAG | 6 | 拖拽浮起落位动效中断。（已满足READY\_TO\_TRIGGER\_DRAG\_ACTION状态后，未达到动效阶段，手指抬手时触发）  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PREPARING\_FOR\_DRAG\_DETECTION18+ | 7 | 拖拽准备完成，可发起拖拽阶段。（按下350ms时触发）  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## UnifiedData10+

type UnifiedData = import('../api/@ohos.data.unifiedDataChannel').default.UnifiedData

拖拽相关的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.data.unifiedDataChannel').default.[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 拖拽相关的数据。 |

## Summary10+

type Summary = import('../api/@ohos.data.unifiedDataChannel').default.Summary

拖拽相关数据的简介。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.data.unifiedDataChannel').default.[Summary](js-apis-data-unifieddatachannel.md#summary) | 拖拽相关数据的简介。 |

## DataLoadParams20+

type DataLoadParams = import('../api/@ohos.data.unifiedDataChannel').default.DataLoadParams

落入操作时使用的数据加载参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.data.unifiedDataChannel').default.[DataLoadParams](js-apis-data-unifieddatachannel.md#dataloadparams20) | 落入操作时使用的数据加载参数。 |

## DataSyncOptions15+

type DataSyncOptions = import('../api/@ohos.data.unifiedDataChannel').default.GetDataParams

作为startDataLoading的入参对象。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.data.unifiedDataChannel').default.[GetDataParams](js-apis-data-unifieddatachannel.md#getdataparams15) | 表示从[UDMF](capi-udmf.md)获取数据时的参数，包含目标路径、文件冲突选项、进度条类型等。 |

## OnDragEventCallback15+

type OnDragEventCallback = (event: DragEvent, extraParams?: string) => void

拖拽事件的回调函数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [DragEvent](ts-universal-events-drag-drop.md#dragevent7) | 是 | event为拖拽事件信息，包括拖拽点坐标。 |
| extraParams | string | 否 | extraParams为拖拽事件额外信息，需要解析为JSON格式，参考[extraParams](ts-universal-events-drag-drop.md#extraparams说明)说明。未传入时无额外信息。 |

## DropOptions15+

设置落入过程的参数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| disableDataPrefetch | boolean | 否 | 是 | 设置拖拽是否提前获取数据。true表示不提前获取数据，false表示提前获取数据，默认值为false。  **说明：**  当使用[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)获取数据时需设置该参数为true，防止拖拽提前获取数据。 |

## DragSpringLoadingConfiguration20+

type DragSpringLoadingConfiguration = import('../api/@ohos.arkui.dragController').default.DragSpringLoadingConfiguration

定义拖拽的悬停检测配置参数的接口。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.dragController').default.[DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20) | 定义拖拽的悬停检测配置参数的接口。 |

## SpringLoadingContext20+

type SpringLoadingContext = import('../api/@ohos.arkui.dragController').default.SpringLoadingContext

定义回调上下文信息的类，用于在悬停检测回调中传递给应用，使其能访问拖拽状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.dragController').default.[SpringLoadingContext](js-apis-arkui-dragcontroller.md#springloadingcontext20) | 定义回调上下文信息的类，用于在悬停检测回调中传递给应用，以便应用能访问拖拽状态。 |

## 示例

### 示例1（设置组件拖拽和落入）

示例1展示了部分组件（如Image和Text等）拖拽和可落入区域的设置。

```ts
// xxx.ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State targetImage: string = '';
  @State targetText: string = 'Drag Text';
  @State imageWidth: number = 100;
  @State imageHeight: number = 100;
  @State imgState: Visibility = Visibility.Visible;
  @State abstractContent: string = 'abstract';
  @State textContent: string = '';
  @State backGroundColor: Color = Color.Transparent;

  // 获取Udmf数据
  getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
    try {
      let data: UnifiedData = event.getData();
      if (!data) {
        return false;
      }
      let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
      if (!records || records.length <= 0) {
        return false;
      }
      callback(event);
      return true;
    } catch (error) {
      console.error(`Failed to get data. Code: ${error.code}, message: ${error.message}`);
      return false;
    }
  }

  // 首次获取Udmf数据失败后自动重试
  getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
    if (this.getDataFromUdmfRetry(event, callback)) {
      return;
    }
    setTimeout(() => {
      this.getDataFromUdmfRetry(event, callback);
    }, 1500);
  }

  // 根据拖拽发起前的不同阶段更改背景色
  private preDragChange(preDragStatus: PreDragStatus): void {
    if (preDragStatus == PreDragStatus.READY_TO_TRIGGER_DRAG_ACTION) {
      this.backGroundColor = Color.Red;
    } else if (preDragStatus == PreDragStatus.ACTION_CANCELED_BEFORE_DRAG
      || preDragStatus == PreDragStatus.PREVIEW_LANDING_FINISHED) {
      this.backGroundColor = Color.Blue;
    }
  }

  build() {
    Row() {
      Column() {
        Text('start Drag')
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        // $r('app.media.icon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.icon'))
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .visibility(this.imgState)
          .onDragEnd((event) => {
            // onDragEnd里取到的result值在接收方onDrop设置
            if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
            } else if (event.getResult() === DragResult.DRAG_FAILED) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
            }
          })
        Text('test drag event')
          .width('100%')
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .copyOption(CopyOptions.InApp)
        TextArea({ placeholder: 'please input words' })
          .copyOption(CopyOptions.InApp)
          .width('100%')
          .height(50)
          .draggable(true)
        Search({ placeholder: 'please input your word' })
          .searchButton('Search')
          .width('100%')
          .height(80)
          .textFont({ size: 20 })

        Column() {
          Text('this is abstract')
            .fontSize(20)
            .width('100%')
        }
        .margin({ left: 40, top: 20 })
        .width('100%')
        .height(100)
        .onDragStart((event) => {
          this.backGroundColor = Color.Transparent;
          let data: unifiedDataChannel.PlainText = new unifiedDataChannel.PlainText();
          data.abstract = 'this is abstract';
          data.textContent = 'this is content this is content';
          (event as DragEvent).setData(new unifiedDataChannel.UnifiedData(data));
        })
        .onPreDrag((status: PreDragStatus) => {
          this.preDragChange(status);
        })
        .backgroundColor(this.backGroundColor)
      }.width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        Image(this.targetImage)
          .width(this.imageWidth)
          .height(this.imageHeight)
          .draggable(true)
          .margin({ left: 15 })
          .border({ color: Color.Black, width: 1 })
          .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
          .onDrop((dragEvent?: DragEvent) => {
            this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
              let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
              let rect: Rectangle = event.getPreviewRect();
              this.imageWidth = Number(rect.width);
              this.imageHeight = Number(rect.height);
              this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
              event.useCustomDropAnimation = false;
              this.imgState = Visibility.None;
              // 显式设置result为successful，则将该值传递给拖出方的onDragEnd
              event.setResult(DragResult.DRAG_SUCCESSFUL);
            });
          })

        Text(this.targetText)
          .width('100%')
          .height(100)
          .border({ color: Color.Black, width: 1 })
          .margin(15)
          .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
          .onDrop((dragEvent?: DragEvent) => {
            this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
              let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
              let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
              this.targetText = plainText.textContent;
            });
          })

        Column() {
          Text(this.abstractContent).fontSize(20).width('100%')
          Text(this.textContent).fontSize(15).width('100%')
        }
        .width('100%')
        .height(100)
        .margin(20)
        .border({ color: Color.Black, width: 1 })
        .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
        .onDrop((dragEvent?: DragEvent) => {
          this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
            let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
            let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
            this.abstractContent = plainText.abstract as string;
            this.textContent = plainText.textContent;
          });
        })
      }.width('45%')
      .height('100%')
      .margin({ left: '5%' });
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/y6PaByUaQAC3mtG7DKnP0Q/zh-cn_image_0000002742124753.png)

### 示例2（自定义落位动效）

从API version 18开始，示例2展示了通过[executeDropAnimation](ts-universal-events-drag-drop.md#executedropanimation18)接口，实现自定义落位动效。

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct DropAnimationExample {
  @State targetImage: string = '';
  @State imageWidth: number = 100;
  @State imageHeight: number = 100;
  @State imgState: Visibility = Visibility.Visible;
  customDropAnimation =
    () => {
      this.getUIContext().animateTo({ duration: 1000, curve: Curve.EaseOut, playMode: PlayMode.Normal }, () => {
        this.imageWidth = 200;
        this.imageHeight = 200;
        this.imgState = Visibility.None;
      })
    }

  build() {
    Row() {
      Column() {
        // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.app_icon'))
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15, top: 40 })
          .visibility(this.imgState)
          .onDragStart((event) => {
          })
          .onDragEnd((event) => {
            if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
              console.info('Drag Success');
            } else if (event.getResult() === DragResult.DRAG_FAILED) {
              console.error('Drag failed');
            }
          })
      }.width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width(180)
          .height(40)
          .textAlign(TextAlign.Center)
          .margin(10)
          .backgroundColor('rgb(240,250,255)')
        Column() {
          Image(this.targetImage)
            .width(this.imageWidth)
            .height(this.imageHeight)
        }
        .draggable(true)
        .margin({ left: 15 })
        .border({ color: Color.Black, width: 1 })
        .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
        // onDrop回调，获取拖拽图片的信息和尺寸并更新显示，同时启用并执行自定义下落动画
        .onDrop((dragEvent: DragEvent) => {
          let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
          let rect: Rectangle = dragEvent.getPreviewRect();
          this.imageWidth = Number(rect.width);
          this.imageHeight = Number(rect.height);
          this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
          dragEvent.useCustomDropAnimation = true;
          dragEvent.executeDropAnimation(this.customDropAnimation);
        })
        .width(this.imageWidth)
        .height(this.imageHeight)
      }.width('45%')
      .height('100%')
      .margin({ left: '5%' })
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/N2ItG5y4SR6SPllBiYl4dQ/zh-cn_image_0000002712245846.gif)

### 示例3（拖拽异步获取数据）

从API version 15开始，示例3展示了通过[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)实现拖拽异步获取数据。

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { fileUri, fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct ImageExample {
  @State uri: string = '';
  @State blockArr: string[] = [];
  uiContext = this.getUIContext();
  udKey: string = '';

  build() {
    Column() {
      Text('Image拖拽')
        .fontSize('30dp')
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.startIcon'))
          .width(100)
          .height(100)
          .border({ width: 1 })
          .draggable(true)
          .onDragStart((event: DragEvent) => {
            const context: Context | undefined = this.uiContext.getHostContext();
            if (context) {
              let data = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id, 120);
              const arrayBuffer: ArrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
              let filePath = context.filesDir + '/test.png';
              let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
              try {
                fileIo.writeSync(file.fd, arrayBuffer);
              } finally {
                fileIo.closeSync(file.fd);
              }
              fileIo.writeSync(file.fd, arrayBuffer);
              // 获取图片的uri
              let uri = fileUri.getUriFromPath(filePath);
              let image: unifiedDataChannel.Image = new unifiedDataChannel.Image();
              image.imageUri = uri;
              let dragData: unifiedDataChannel.UnifiedData = new unifiedDataChannel.UnifiedData(image);
              (event as DragEvent).setData(dragData);
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('可释放区域')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.blockArr, (item: string, index) => {
              ListItem() {
                Image(item)
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .border({ width: 1 })
          .height('90%')
          .width('100%')
          .onDrop((event?: DragEvent, extraParams?: string) => {
            console.info('enter onDrop');
            let context = this.uiContext.getHostContext() as common.UIAbilityContext;
            let pathDir: string = context.distributedFilesDir;
            let destUri = fileUri.getUriFromPath(pathDir);
            // 创建DataProgressListener监听数据传输进度
            let progressListener: unifiedDataChannel.DataProgressListener =
              (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
                if (dragData != null) {
                  // 获取数据记录数组
                  let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
                  if (arr.length > 0) {
                    // 检查首记录类型是否为IMAGE
                    if (arr[0].getType() === uniformTypeDescriptor.UniformDataType.IMAGE) {
                      // 类型匹配成功，记录数据Uri
                      let image = arr[0] as unifiedDataChannel.Image;
                      this.uri = image.imageUri;
                      this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
                    }
                  } else {
                    console.info('dragData arr is null');
                  }
                } else {
                  console.info('dragData is undefined');
                }
                console.info(`percentage: ${progress.progress}`);
              };
            // 设置异步数据加载参数项
            let options: DataSyncOptions = {
              destUri: destUri,
              fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
              progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
              dataProgressListener: progressListener,
            }
            try {
              // 启动数据传输
              this.udKey = (event as DragEvent).startDataLoading(options);
              console.info(`udKey: ${this.udKey}`);
            } catch (e) {
              console.error(`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
            }
          }, { disableDataPrefetch: true })
        }
        .height('50%')
        .width('90%')
        .border({ width: 1 })
      }

      Button('取消数据传输')
        .onClick(() => {
          try {
            this.getUIContext().getDragController().cancelDataLoading(this.udKey);
          } catch (e) {
            console.error(`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
          }
        })
        .margin({ top: 10 })
    }.width('100%')
  }
}
```

### 示例4（获取当前拖拽的屏幕ID）

从API version 20开始，示例4展示了通过onDragXXX（不支持onDragEnd）接口获取拖拽事件，并调用拖拽事件的[getDisplayId](ts-universal-events-drag-drop.md#getdisplayid20)接口获取屏幕ID。

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State targetImage: string = '';
  @State imageWidth: number = 100;
  @State imageHeight: number = 100;
  @State imgState: Visibility = Visibility.Visible;
  @State backGroundColor: Color = Color.Transparent;
  @State startDisplayId: number = -1;
  @State enterDisplayId: number = -1;
  @State moveDisplayId: number = -1;
  @State leaveDisplayId: number = -1;
  @State dropDisplayId: number = -1;

  getDataFromUdmfRetry(event: DragEvent, callback: (data: DragEvent) => void) {
    try {
      let data: UnifiedData = event.getData();
      if (!data) {
        return false;
      }
      let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
      if (!records || records.length <= 0) {
        return false;
      }
      callback(event);
      return true;
    } catch (error) {
      console.error(`Failed to get data. Code: ${error.code}, message: ${error.message}`);
      return false;
    }
  }

  getDataFromUdmf(event: DragEvent, callback: (data: DragEvent) => void) {
    if (this.getDataFromUdmfRetry(event, callback)) {
      return;
    }
    setTimeout(() => {
      this.getDataFromUdmfRetry(event, callback);
    }, 1500);
  }

  private preDragChange(preDragStatus: PreDragStatus): void {
    if (preDragStatus == PreDragStatus.READY_TO_TRIGGER_DRAG_ACTION) {
      this.backGroundColor = Color.Red;
    } else if (preDragStatus == PreDragStatus.ACTION_CANCELED_BEFORE_DRAG
      || preDragStatus == PreDragStatus.PREVIEW_LANDING_FINISHED) {
      this.backGroundColor = Color.Blue;
    }
  }

  build() {
    Row() {
      Column() {
        Text('start Drag')
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.startIcon'))
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .visibility(this.imgState)
          .onDragStart((event) => {
            let id = event.getDisplayId();
            this.startDisplayId = id;
          })

          .onDragEnd((event) => {
            if (event.getResult() === DragResult.DRAG_SUCCESSFUL) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success' });
            } else if (event.getResult() === DragResult.DRAG_FAILED) {
              this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag failed' });
            }
          })

        Text('displayID in onDragStart: ' + this.startDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDragEnter: ' + this.enterDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDragMove: ' + this.moveDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDragLeave: ' + this.leaveDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
        Text('displayID in onDrop: ' + this.dropDisplayId.toString())
          .width('100%')
          .height(50)
          .draggable(true)
          .margin({ left: 15 })
          .onPreDrag((status: PreDragStatus) => {
            this.preDragChange(status);
          })
      }.width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        Image(this.targetImage)
          .width(this.imageWidth)
          .height(this.imageHeight)
          .draggable(true)
          .margin({ left: 15 })
          .border({ color: Color.Black, width: 1 })
          .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
          .onDragEnter((event) => {
            let id = event.getDisplayId();
            this.enterDisplayId = id;
          })
          .onDragMove((event) => {
            let id = event.getDisplayId();
            this.moveDisplayId = id;
          })
          .onDragLeave((event) => {
            let id = event.getDisplayId();
            this.leaveDisplayId = id;
          })
          .onDrop((dragEvent: DragEvent) => {
            let id = dragEvent.getDisplayId();
            this.dropDisplayId = id;
            this.getDataFromUdmf((dragEvent as DragEvent), (event: DragEvent) => {
              let records: Array<unifiedDataChannel.UnifiedRecord> = event.getData().getRecords();
              let rect: Rectangle = event.getPreviewRect();
              this.imageWidth = Number(rect.width);
              this.imageHeight = Number(rect.height);
              this.targetImage = (records[0] as unifiedDataChannel.Image).imageUri;
              event.useCustomDropAnimation = false;
              this.imgState = Visibility.None;
              event.setResult(DragResult.DRAG_SUCCESSFUL);
            });
          })
      }.width('45%')
      .height('100%')
      .margin({ left: '5%' })
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/VGyrUnTcQYmam4ClYGIPmg/zh-cn_image_0000002742004795.png)

### 示例5（获取包名和是否是跨设备）

从API version 20开始，示例5展示了通过onDragXXX接口获取拖拽事件，调用拖拽事件的[getDragSource](ts-universal-events-drag-drop.md#getdragsource20)接口获取包名，调用isRemote接口判断是否为跨设备拖拽。

```ts
@Entry
@Component
struct Index {
  @State targetImage: string = '';
  @State startDragSource: string = '';
  @State startIsRemote: boolean = true;
  @State enterDragSource: string = '';
  @State enterIsRemote: boolean = true;

  build() {
    Column() {
      Row() {
        Column() {
          Text('start Drag Area')
            .fontSize(18)
            .width('100%')
            .height(40)
            .margin(10)
            .backgroundColor('#008888')
          // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
          Image($r('app.media.startIcon'))
            .onDragStart((event) => {
              this.startDragSource = (event as DragEvent).getDragSource();
              this.startIsRemote = (event as DragEvent).isRemote();
            })
            .width(100)
            .height(100)
            .draggable(true)
            .margin({ left: 15 })
        }
        .border({ color: Color.Black, width: 1 })
        .width('45%')
        .height('50%')

        Column() {
          Text('Drag Target Area')
            .fontSize(20)
            .width('100%')
            .height(40)
            .margin(10)
            .backgroundColor('#008888')
          Image(this.targetImage)
            .width(100)
            .height(100)
            .draggable(true)
            .margin({ left: 15 })
            .border({ color: Color.Black, width: 1 })
            .onDragEnter((event) => {
              this.enterDragSource = (event as DragEvent).getDragSource();
              this.enterIsRemote = (event as DragEvent).isRemote();
            })
            .onDrop(() => {
            })
        }
        .border({ color: Color.Black, width: 1 })
        .width('45%')
        .height('50%')
        .margin({ left: '5%' })
      }
      .height('70%')

      Text('onDragStart dragSource: ' + this.startDragSource.toString() + '\n' + 'onDragStart isRemote: ' +
      this.startIsRemote.toString())
        .width('100%')
        .height(50)
        .margin({ left: 15 })
      Text('onDragEnter dragSource: ' + this.enterDragSource.toString() + '\n' + 'onDragEnter isRemote: ' +
      this.enterIsRemote.toString())
        .width('100%')
        .height(50)
        .margin({ left: 15 })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/U2ffbR9-QHaCEzwxjucUMA/zh-cn_image_0000002712405806.png)

### 示例6（拖拽支持悬停检测）

从API version 20开始，示例6展示了通过[onDragSpringLoading](ts-universal-events-drag-drop.md#ondragspringloading20)接口注册回调，并通过回调中的[SpringLoadingContext](ts-universal-events-drag-drop.md#springloadingcontext20)获取上下文信息（当前状态、通知序列）。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @State state: number = 0;
  @State currentNotifySequence: number = 0;
  @State config: DragSpringLoadingConfiguration = {
    stillTimeLimit: 200,
    updateInterval: 300,
    updateNotifyCount: 4,
    updateToFinishInterval: 300
  };

  build() {
    Row() {
      Column() {
        Text('start Drag')
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.startIcon'))
          .id('ori_image')
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
        Text('当前状态是: ' + this.state)
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
        Text('当前通知序列是: ' + this.currentNotifySequence)
          .fontSize(18)
          .width('100%')
          .height(40)
          .margin(10)
      }
      .width('45%')
      .height('100%')

      Column() {
        Text('Drag Target Area')
          .fontSize(20)
          .width('100%')
          .height(40)
          .margin(10)
          .backgroundColor('#008888')
          .id('text')
        Image('')
          .width(100)
          .height(100)
          .draggable(true)
          .margin({ left: 15 })
          .border({ color: Color.Black, width: 2 })
          .onDragSpringLoading((context: SpringLoadingContext) => {
            this.state = context.state;
            this.currentNotifySequence = context.currentNotifySequence;
          }, this.config)
      }
      .width('45%')
      .height('100%')
      .margin({ left: '5%' })
      .onDragSpringLoading((context: SpringLoadingContext) => {
        this.state = context.state;
        this.currentNotifySequence = context.currentNotifySequence;
      }, this.config)
      .id('column')
      .backgroundColor(Color.Grey)
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/iKZhbZswRbSbAyoSuBnrdg/zh-cn_image_0000002742124755.gif)

### 示例7（拖起方延迟提供数据）

从API version 20开始，示例7展示了在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中调用[setDataLoadParams](ts-universal-events-drag-drop.md#setdataloadparams20)延迟提供数据接口，并在[onDrop](ts-universal-events-drag-drop.md#ondrop)中调用[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)异步获取数据接口。

```ts
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { fileUri, fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct VideoExample {
  @State uri: string = '';
  @State blockArr: string[] = [];
  uiContext = this.getUIContext();
  udKey: string = '';

  build() {
    Column() {
      Text('video拖拽')
        .fontSize('30dp')
      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
        // $rawfile('test1.mp4')需要替换为开发者所需的资源文件
        Video({ src: $rawfile('test1.mp4'), controller: new VideoController() })
          .width(200)
          .height(200)
          .border({ width: 1 })
          .draggable(true)
          .onDragStart((event: DragEvent) => {
            const context: Context | undefined = this.uiContext.getHostContext();
            if (context) {
              // 定义延迟数据加载回调，在目标端请求数据时读取视频资源并封装为UnifiedData。
              let loadHandler: unifiedDataChannel.DataLoadHandler = (acceptableInfo) => {
                console.info(`acceptableInfo recordCount ${acceptableInfo?.recordCount}`);
                if (acceptableInfo?.types) {
                  console.info(`acceptableInfo types ${Array.from(acceptableInfo.types)}`);
                } else {
                  console.error('acceptableInfo types is undefined');
                }
                let data = context.resourceManager.getRawFdSync('test1.mp4');
                let filePath = context.filesDir + '/test1.mp4';
                let file: fileIo.File = null!;
                try {
                  file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
                  let bufferSize = data.length as number;
                  let buf = new ArrayBuffer(bufferSize);
                  fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
                  fileIo.writeSync(file.fd, buf, { offset: 0, length: bufferSize });
                } catch (error) {
                  console.error(`openSync errorCode: ${error.code}, errorMessage: ${error.message}`);
                } finally {
                  if (file !== null) {
                    fileIo.closeSync(file.fd);
                  }
                }
                context.resourceManager.closeRawFdSync('test1.mp4');
                this.uri = fileUri.getUriFromPath(filePath);
                let videoMp: uniformDataStruct.FileUri = {
                  uniformDataType: 'general.file-uri',
                  oriUri: this.uri,
                  fileType: 'general.video',
                };
                let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
                let unifiedData = new unifiedDataChannel.UnifiedData();
                unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, videoMp);
                unifiedData.addRecord(unifiedRecord);
                return unifiedData;
              }
              (event as DragEvent).setDataLoadParams({
                loadHandler: loadHandler,
                dataLoadInfo: { types: new Set([uniformTypeDescriptor.UniformDataType.FILE_URI]), recordCount: 1 }
              });
            }
          })
      }
      .margin({ bottom: 20 })

      Row() {
        Column() {
          Text('可释放区域')
            .fontSize('15dp')
            .height('10%')
          List() {
            ForEach(this.blockArr, (item: string, index) => {
              ListItem() {
                Video({ src: item, controller: new VideoController() })
                  .width(100)
                  .height(100)
                  .border({ width: 1 })
              }
              .margin({ left: 30, top: 30 })
            }, (item: string) => item)
          }
          .border({ width: 1 })
          .height('90%')
          .width('100%')
          .onDrop((event: DragEvent, extraParams?: string) => {
            let context = this.uiContext.getHostContext() as common.UIAbilityContext;
            let pathDir: string = context.distributedFilesDir;
            let destUri = fileUri.getUriFromPath(pathDir);
            let progressListener: unifiedDataChannel.DataProgressListener =
              (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
                if (dragData != null) {
                  let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
                  if (arr.length > 0) {
                    if (arr[0].getType() === uniformTypeDescriptor.UniformDataType.VIDEO) {
                      this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
                    }
                  } else {
                    console.info('dragData arr is null');
                  }
                } else {
                  console.info('dragData is undefined');
                }
                console.info(`percentage: ${progress.progress}`);
              };
            let info: unifiedDataChannel.DataLoadInfo =
              { types: new Set([uniformTypeDescriptor.UniformDataType.VIDEO]), recordCount: 100 };
            let options: DataSyncOptions = {
              destUri: destUri,
              fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
              progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
              dataProgressListener: progressListener,
              acceptableInfo: info,
            }
            try {
              // 启动异步数据加载，并保存数据加载标识用于后续取消传输。
              this.udKey = (event as DragEvent).startDataLoading(options);
              console.info(`udKey: ${this.udKey}`);
            } catch (error) {
              console.error(`startDataLoading errorCode: ${error.code}, errorMessage: ${error.message}`);
            }
          }, { disableDataPrefetch: true })
        }
        .height('50%')
        .width('90%')
        .border({ width: 1 })
      }

      Button('取消数据传输')
        .onClick(() => {
          try {
            this.getUIContext().getDragController().cancelDataLoading(this.udKey);
          } catch (error) {
            console.error(`cancelDataLoading errorCode: ${error.code}, errorMessage: ${error.message}`);
          }
        })
        .margin({ top: 10 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/k0MmXe5_SjiF1dc5uiPTCg/zh-cn_image_0000002712245848.gif)

### 示例8（拖拽自动隐藏指定组件）

该示例通过DragEvent的[autoHideComponentUniqueIds](ts-universal-events-drag-drop.md#属性)属性，在拖拽成功发起后自动隐藏指定组件。

从API版本26.0.0开始，DragEvent新增autoHideComponentUniqueIds属性。

```ts
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragEventAutoHideSample {
  @State sourceVisibility: Visibility = Visibility.Visible;
  @State badgeVisibility: Visibility = Visibility.Visible;
  @State statusText: string = '状态：等待拖拽';

  private buildData(textValue: string): unifiedDataChannel.UnifiedData {
    let plainText = new unifiedDataChannel.PlainText();
    plainText.textContent = textValue;
    plainText.abstract = textValue;
    return new unifiedDataChannel.UnifiedData(plainText);
  }

  private collectHideIds(): number[] {
    let hideIds: number[] = [];
    let sourceNode = this.getUIContext().getFrameNodeById('drag_source');
    let badgeNode = this.getUIContext().getFrameNodeById('drag_badge');
    if (sourceNode?.getUniqueId() !== undefined) {
      hideIds.push(sourceNode.getUniqueId());
    }
    if (badgeNode?.getUniqueId() !== undefined) {
      hideIds.push(badgeNode.getUniqueId());
    }
    return hideIds;
  }

  private hideTargets(): void {
    this.sourceVisibility = Visibility.Hidden;
    this.badgeVisibility = Visibility.Hidden;
    this.statusText = '状态：拖拽中，目标组件已隐藏';
  }

  private restoreTargets(): void {
    this.sourceVisibility = Visibility.Visible;
    this.badgeVisibility = Visibility.Visible;
    this.statusText = '状态：拖拽结束，组件已恢复显示';
  }

  build() {
    Column({ space: 12 }) {
      Text(this.statusText)
        .width('100%')
        .fontSize(14)
        .fontColor('#BF360C')

      Row({ space: 12 }) {
        Column() {
          Text('拖拽源')
            .fontColor(Color.White)
            .fontWeight(FontWeight.Medium)
          Text('id: drag_source')
            .fontSize(10)
            .fontColor('#E8F5E9')
        }
          .id('drag_source')
          .width(140)
          .height(90)
          .backgroundColor('#2E7D32')
          .borderRadius(12)
          .justifyContent(FlexAlign.Center)
          .visibility(this.sourceVisibility)
          .draggable(true)
          .onDragStart((event: DragEvent) => {
            let hideIds = this.collectHideIds();
            event.autoHideComponentUniqueIds = hideIds;
            event.setData(this.buildData('drag event auto hide test data'));
            this.hideTargets();
            return () => {
              Text('拖拽预览')
            };
          })
          .onDragEnd(() => {
            this.restoreTargets();
          })

        Column() {
          Text('跟随隐藏组件')
            .fontColor(Color.White)
            .fontWeight(FontWeight.Medium)
          Text('id: drag_badge')
            .fontSize(10)
            .fontColor('#E3F2FD')
        }
          .id('drag_badge')
          .width(140)
          .height(90)
          .backgroundColor('#1565C0')
          .borderRadius(12)
          .justifyContent(FlexAlign.Center)
          .visibility(this.badgeVisibility)
      }

      Column() {
        Text('拖拽落点')
          .fontWeight(FontWeight.Medium)
        Text('松手后恢复组件显示')
          .fontSize(10)
          .fontColor('#6D4C41')
      }
        .width('100%')
        .height(120)
        .backgroundColor('#FFE082')
        .borderRadius(12)
        .justifyContent(FlexAlign.Center)
        .onDrop(() => {
          this.restoreTargets();
        })
    }
    .width('100%')
    .padding(16)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/8Py8liq-RjiF6VVDVhd6Lg/zh-cn_image_0000002742004797.gif)
