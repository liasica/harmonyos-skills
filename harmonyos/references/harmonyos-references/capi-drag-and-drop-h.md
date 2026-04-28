---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h
title: drag_and_drop.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > drag_and_drop.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:44+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:aa4615b3b8b658405d45d4aaab612e976b17155f54fc62ef5b30308eb75ba630
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeDrag相关接口定义。

**引用文件：** <arkui/drag\_and\_drop.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeDragDrop](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeDragDrop)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md) | ArkUI\_NodeEvent | 组件事件的通用结构类型。 |
| [ArkUI\_Context](capi-arkui-nativemodule-arkui-context.md) | ArkUI\_Context | native UI的上下文实例对象。 |
| [ArkUI\_Context\*](capi-arkui-nativemodule-arkui-context8h.md) | ArkUI\_ContextHandle | native UI的上下文实例对象指针定义。 |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md) | ArkUI\_DragEvent | 拖拽事件。 |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md) | ArkUI\_DragPreviewOption | 设置拖拽跟手图的相关自定义参数。 |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md) | ArkUI\_DragAction | 拖拽行为，用于主动发起拖拽。 |
| [ArkUI\_DragAndDropInfo](capi-arkui-nativemodule-arkui-draganddropinfo.md) | ArkUI\_DragAndDropInfo | 主动发起拖拽后，通过拖拽状态监听返回的系统拖拽相关数据。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_DragResult](capi-drag-and-drop-h.md#arkui_dragresult) | ArkUI\_DragResult | 拖拽结果定义，由数据接收方设置，并由系统传递给数据拖出方，拖出方可感知接收方对数据的处理结果。 |
| [ArkUI\_DropOperation](capi-drag-and-drop-h.md#arkui_dropoperation) | ArkUI\_DropOperation | 定义拖拽释放时的数据处理方式，可影响角标的显示。 |
| [ArkUI\_PreDragStatus](capi-drag-and-drop-h.md#arkui_predragstatus) | ArkUI\_PreDragStatus | 定义拖拽发起前的长按交互阶段的变化状态。 |
| [ArkUI\_DragPreviewScaleMode](capi-drag-and-drop-h.md#arkui_dragpreviewscalemode) | ArkUI\_DragPreviewScaleMode | 拖拽预览缩放模式。 |
| [ArkUI\_DragStatus](capi-drag-and-drop-h.md#arkui_dragstatus) | ArkUI\_DragStatus | 拖拽状态。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent\* OH\_ArkUI\_NodeEvent\_GetDragEvent(ArkUI\_NodeEvent\* nodeEvent)](capi-drag-and-drop-h.md#oh_arkui_nodeevent_getdragevent) | 从 NodeEvent 中获取DragEvent。 |
| [ArkUI\_PreDragStatus OH\_ArkUI\_NodeEvent\_GetPreDragStatus(ArkUI\_NodeEvent\* nodeEvent)](capi-drag-and-drop-h.md#oh_arkui_nodeevent_getpredragstatus) | 获取预览拖拽事件状态。 |
| [int32\_t OH\_ArkUI\_DragEvent\_DisableDefaultDropAnimation(ArkUI\_DragEvent\* event, bool disable)](capi-drag-and-drop-h.md#oh_arkui_dragevent_disabledefaultdropanimation) | 设置是否禁用松手时的系统默认动效，默认不禁用，通常在应用需要自定义落位动效时配置。 |
| [int32\_t OH\_ArkUI\_DragEvent\_SetSuggestedDropOperation(ArkUI\_DragEvent\* event, ArkUI\_DropOperation dropOperation)](capi-drag-and-drop-h.md#oh_arkui_dragevent_setsuggesteddropoperation) | 设置数据处理方式。 |
| [int32\_t OH\_ArkUI\_DragEvent\_SetDragResult(ArkUI\_DragEvent\* event, ArkUI\_DragResult result)](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdragresult) | 设置拖拽事件的结果。 |
| [int32\_t OH\_ArkUI\_DragEvent\_SetData(ArkUI\_DragEvent\* event, OH\_UdmfData\* data)](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdata) | 向ArkUI\_DragEvent中设置拖拽数据。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_SetDataLoadParams(ArkUI\_DragEvent\* event, OH\_UdmfDataLoadParams\* dataLoadParams)](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdataloadparams) | 调用此方法向系统提供数据加载参数，而非直接传入完整的数据对象。当用户将数据拖拽至目标应用程序并释放时，系统将使用dataLoadParams请求数据。这可以显著提高拖拽大量数据及目标应用程序处理释放数据的效率。此方法应始终优先于[OH\_ArkUI\_DragEvent\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdata)使用。请参考**udmf.h**中的[OH\_UdmfDataLoadParams\_Create](capi-udmf-h.md#oh_udmfdataloadparams_create)了解如何创建和准备数据加载参数。该方法与[OH\_ArkUI\_DragEvent\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdata)存在冲突，系统始终以最后调用的方法为准。 |
| [int32\_t OH\_ArkUI\_DragEvent\_GetUdmfData(ArkUI\_DragEvent\* event, OH\_UdmfData \*data)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getudmfdata) | 从ArkUI\_DragEvent中获取拖拽默认相关数据。 |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDataTypeCount(ArkUI\_DragEvent\* event, int32\_t\* count)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getdatatypecount) | 从ArkUI\_DragEvent中获取所拖拽的数据类型种类个数。 |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDataTypes(ArkUI\_DragEvent \*event, char \*eventTypeArray[], int32\_t length, int32\_t maxStrLen)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h#oh_arkui_dragevent_getdatatypes) | 从ArkUI\_DragEvent中获取拖拽数据的类型列表。 |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDragResult(ArkUI\_DragEvent\* event, ArkUI\_DragResult\* result)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getdragresult) | 从ArkUI\_DragEvent中获取拖拽结果。 |
| [int32\_t OH\_ArkUI\_DragEvent\_GetDropOperation(ArkUI\_DragEvent\* event, ArkUI\_DropOperation\* operation)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getdropoperation) | 从ArkUI\_DragEvent中获取数据处理方式。 |
| [float OH\_ArkUI\_DragEvent\_GetPreviewTouchPointX(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getpreviewtouchpointx) | 从ArkUI\_DragEvent中获取预览图跟手点的x轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetPreviewTouchPointY(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getpreviewtouchpointy) | 从ArkUI\_DragEvent中获取预览图跟手点的y轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetPreviewRectWidth(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getpreviewrectwidth) | 从ArkUI\_DragEvent中获取预览图的宽。 |
| [float OH\_ArkUI\_DragEvent\_GetPreviewRectHeight(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getpreviewrectheight) | 从ArkUI\_DragEvent中获取预览图的高。 |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointXToWindow(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_gettouchpointxtowindow) | 从ArkUI\_DragEvent中获取跟手点相对于window的x轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointYToWindow(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_gettouchpointytowindow) | 从ArkUI\_DragEvent中获取跟手点相对于window的y轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointXToDisplay(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_gettouchpointxtodisplay) | 从ArkUI\_DragEvent中获取跟手点相对于当前Display的x轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointYToDisplay(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_gettouchpointytodisplay) | 从ArkUI\_DragEvent中获取跟手点相对于当前Display的y轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetVelocityX(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getvelocityx) | 获取当前拖拽的x轴方向拖动速度。 |
| [float OH\_ArkUI\_DragEvent\_GetVelocityY(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getvelocityy) | 获取当前拖拽的y轴方向拖动速度。 |
| [float OH\_ArkUI\_DragEvent\_GetVelocity(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getvelocity) | 获取当前拖拽的主方向拖动速度。 |
| [int32\_t OH\_ArkUI\_DragEvent\_GetModifierKeyStates(ArkUI\_DragEvent\* event, uint64\_t\* keys)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getmodifierkeystates) | 获取功能键按压状态。 |
| [int32\_t OH\_ArkUI\_DragEvent\_StartDataLoading(ArkUI\_DragEvent\* event, OH\_UdmfGetDataParams\* options, char\* key, unsigned int keyLen)](capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading) | 使用指定的同步参数开始数据同步。 |
| [int32\_t OH\_ArkUI\_CancelDataLoading(ArkUI\_ContextHandle uiContext, const char\* key)](capi-drag-and-drop-h.md#oh_arkui_canceldataloading) | 取消正在进行的数据同步。 |
| [int32\_t OH\_ArkUI\_DisableDropDataPrefetchOnNode(ArkUI\_NodeHandle node, bool disabled)](capi-drag-and-drop-h.md#oh_arkui_disabledropdataprefetchonnode) | 设置是否在执行[NODE\_ON\_DROP](capi-native-node-h.md#arkui_nodeeventtype)之前禁用数据预获取过程。系统将重试获取数据，直到达到最大时间限制（目前为2.4秒），这对跨设备的拖动操作非常有用，因为它有助于系统稳定通信。然而，对于[OH\_ArkUI\_DragEvent\_StartDataLoading](capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading)方法而言，这一特性显得多余。该方法采用异步机制获取数据，因此在NODE\_ON\_DROP中使用[OH\_ArkUI\_DragEvent\_StartDataLoading](capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading)时，为了避免在NODE\_ON\_DROP执行前意外获取数据，必须将此字段设置为true。 |
| [int32\_t OH\_ArkUI\_SetDragEventStrictReportWithNode(ArkUI\_NodeHandle node, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_setdrageventstrictreportwithnode) | 控制是否使能严格dragEvent上报，建议开启；默认是不开启的；当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，需要通过传入一个当前UI实例上的一个具体的组件节点来关联。 |
| [int32\_t OH\_ArkUI\_SetDragEventStrictReportWithContext(ArkUI\_ContextHandle uiContext, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_setdrageventstrictreportwithcontext) | 控制是否使能严格dragEvent上报，建议开启；默认是不开启的;当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，可通过传入一个UI实例进行关联。 |
| [int32\_t OH\_ArkUI\_SetNodeAllowedDropDataTypes(ArkUI\_NodeHandle node, const char\* typesArray[], int32\_t count)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h#oh_arkui_setnodealloweddropdatatypes) | 配置组件允许接受落入的数据类型，该接口会重置通过 [OH\_ArkUI\_DisallowNodeAnyDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_disallownodeanydropdatatypes) 或[OH\_ArkUI\_AllowNodeAllDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_allownodealldropdatatypes)进行的配置。 |
| [int32\_t OH\_ArkUI\_DisallowNodeAnyDropDataTypes(ArkUI\_NodeHandle node)](capi-drag-and-drop-h.md#oh_arkui_disallownodeanydropdatatypes) | 配置组件不允许接受任何数据类型，该接口会重置通过[OH\_ArkUI\_SetNodeAllowedDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_setnodealloweddropdatatypes)配置的数据类型。 |
| [int32\_t OH\_ArkUI\_AllowNodeAllDropDataTypes(ArkUI\_NodeHandle node)](capi-drag-and-drop-h.md#oh_arkui_allownodealldropdatatypes) | 配置组件允许接受任意数据类型，该接口会重置通过[OH\_ArkUI\_SetNodeAllowedDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_setnodealloweddropdatatypes)配置的数据类型。 |
| [int32\_t OH\_ArkUI\_SetNodeDraggable(ArkUI\_NodeHandle node, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_setnodedraggable) | 设置该组件是否允许进行拖拽。 |
| [int32\_t OH\_ArkUI\_SetNodeDragPreview(ArkUI\_NodeHandle node, OH\_PixelmapNative\* preview)](capi-drag-and-drop-h.md#oh_arkui_setnodedragpreview) | 设置组件在被拖拽时的自定义跟手图。 |
| [ArkUI\_DragPreviewOption\* OH\_ArkUI\_CreateDragPreviewOption(void)](capi-drag-and-drop-h.md#oh_arkui_createdragpreviewoption) | 构建一个ArkUI\_DragPreviewOption对象。 |
| [void OH\_ArkUI\_DragPreviewOption\_Dispose(ArkUI\_DragPreviewOption\* option)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_dispose) | 销毁跟手图自定义参数对象实例。 |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetScaleMode(ArkUI\_DragPreviewOption\* option, ArkUI\_DragPreviewScaleMode scaleMode)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setscalemode) | 设置拖拽跟手图是否根据系统定义自动进行缩放。 |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setdefaultshadowenabled) | 设置跟手图背板默认的投影效果，默认不开启。 |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setdefaultradiusenabled) | 设置跟手图背板默认的圆角效果（默认圆角半径为12.0vp），默认不开启。 |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setnumberbadgeenabled) | 设置跟手图背板是否显示角标,开启后,系统会根据拖拽数量自动进行角标显示。 |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetBadgeNumber(ArkUI\_DragPreviewOption\* option, uint32\_t forcedNumber)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setbadgenumber) | 强制显示角标的数量，覆盖[OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setnumberbadgeenabled)设置的值。 |
| [int32\_t OH\_ArkUI\_DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled(ArkUI\_DragPreviewOption\* option, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setdefaultanimationbeforeliftingenabled) | 配置是否开启点按时的默认动画。 |
| [int32\_t OH\_ArkUI\_SetNodeDragPreviewOption(ArkUI\_NodeHandle node, ArkUI\_DragPreviewOption\* option)](capi-drag-and-drop-h.md#oh_arkui_setnodedragpreviewoption) | 将构造的ArkUI\_DragPreviewOption设置给组件。 |
| [ArkUI\_DragAction\* OH\_ArkUI\_CreateDragActionWithNode(ArkUI\_NodeHandle node)](capi-drag-and-drop-h.md#oh_arkui_createdragactionwithnode) | 创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个当前UI实例的某个组件节点来指定。 |
| [ArkUI\_DragAction\* OH\_ArkUI\_CreateDragActionWithContext(ArkUI\_ContextHandle uiContext)](capi-drag-and-drop-h.md#oh_arkui_createdragactionwithcontext) | 创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个UI实例指针来关联。 |
| [void OH\_ArkUI\_DragAction\_Dispose(ArkUI\_DragAction\* dragAction)](capi-drag-and-drop-h.md#oh_arkui_dragaction_dispose) | 销毁创建的 ArkUI\_DragAction 对象。 |
| [int32\_t OH\_ArkUI\_DragAction\_SetPointerId(ArkUI\_DragAction\* dragAction, int32\_t pointer)](capi-drag-and-drop-h.md#oh_arkui_dragaction_setpointerid) | 设置手指ID，当屏幕上仅有一只手指在操作时，手指ID为0；一般情况下，配置0即可。 |
| [int32\_t OH\_ArkUI\_DragAction\_SetPixelMaps(ArkUI\_DragAction\* dragAction, OH\_PixelmapNative\* pixelmapArray[], int32\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h#oh_arkui_dragaction_setpixelmaps) | 设置拖拽跟手图，只能使用 pixelmap 格式对象。 |
| [int32\_t OH\_ArkUI\_DragAction\_SetTouchPointX(ArkUI\_DragAction\* dragAction, float x)](capi-drag-and-drop-h.md#oh_arkui_dragaction_settouchpointx) | 设置跟手点，相对于设置的第一个pixelmap的左上角。 |
| [int32\_t OH\_ArkUI\_DragAction\_SetTouchPointY(ArkUI\_DragAction\* dragAction, float y)](capi-drag-and-drop-h.md#oh_arkui_dragaction_settouchpointy) | 设置跟手点，相对于设置的第一个pixelmap的左上角。 |
| [int32\_t OH\_ArkUI\_DragAction\_SetData(ArkUI\_DragAction\* dragAction, OH\_UdmfData\* data)](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdata) | 设置拖拽数据。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragAction\_SetDataLoadParams(ArkUI\_DragAction\* dragAction,OH\_UdmfDataLoadParams\* dataLoadParams)](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdataloadparams) | 使用此方法为系统提供一个数据加载参数，而不是直接提供一个完整的数据对象。当用户拖拽到目标应用程序并落入时，系统将使用dataLoadParams请求数据。可以极大地提高拖拽大量数据的效率，以及目标应用程序中处理落入数据的效率。此方法应始终优先于[OH\_ArkUI\_DragAction\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdata)使用。请参考**udmf.h**中的[OH\_UdmfDataLoadParams\_Create](capi-udmf-h.md#oh_udmfdataloadparams_create)了解如何创建和准备数据加载参数。该方法与[OH\_ArkUI\_DragAction\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdata)存在冲突，系统始终以最后调用的方法为准。 |
| [int32\_t OH\_ArkUI\_DragAction\_SetDragPreviewOption(ArkUI\_DragAction\* dragAction, ArkUI\_DragPreviewOption\* option)](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdragpreviewoption) | 将构造的ArkUI\_DragPreviewOption设置给ArkUI\_DragAction。 |
| [int32\_t OH\_ArkUI\_DragAction\_RegisterStatusListener(ArkUI\_DragAction\* dragAction, void\* userData,void(\*listener)(ArkUI\_DragAndDropInfo\* dragAndDropInfo, void\* userData))](capi-drag-and-drop-h.md#oh_arkui_dragaction_registerstatuslistener) | 注册拖拽状态监听回调，该回调可感知到拖拽已经发起或用户松手结束的状态，可通过该监听获取到落入方对数据的接收处理是否成功。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_GetDisplayId(ArkUI\_DragEvent\* event, int32\_t\* displayId)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getdisplayid) | 获取当前拖拽事件发生时所在的屏幕ID，不支持当eventType为NODE\_ON\_DRAG\_END时获取。 |
| [void OH\_ArkUI\_DragAction\_UnregisterStatusListener(ArkUI\_DragAction\* dragAction)](capi-drag-and-drop-h.md#oh_arkui_dragaction_unregisterstatuslistener) | 解注册拖拽状态监听回调。 |
| [ArkUI\_DragStatus OH\_ArkUI\_DragAndDropInfo\_GetDragStatus(ArkUI\_DragAndDropInfo\* dragAndDropInfo)](capi-drag-and-drop-h.md#oh_arkui_draganddropinfo_getdragstatus) | 获取[ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)发起拖拽的状态，获取异常时返回 ArkUI\_DRAG\_STATUS\_UNKNOWN。 |
| [ArkUI\_DragEvent\* OH\_ArkUI\_DragAndDropInfo\_GetDragEvent(ArkUI\_DragAndDropInfo\* dragAndDropInfo)](capi-drag-and-drop-h.md#oh_arkui_draganddropinfo_getdragevent) | 通过dragAndDropInfo获取到DragEvent，可通过DragEvent获取释放结果等。 |
| [int32\_t OH\_ArkUI\_StartDrag(ArkUI\_DragAction\* dragAction)](capi-drag-and-drop-h.md#oh_arkui_startdrag) | 通过构造的DragAction对象发起拖拽。 |
| [int32\_t OH\_ArkUI\_DragEvent\_RequestDragEndPending(ArkUI\_DragEvent\* event, int32\_t\* requestIdentify)](capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending) | 请求延迟处理拖拽结束事件，等待应用程序确认操作结果。应用程序需通过 [OH\_ArkUI\_NotifyDragResult](capi-drag-and-drop-h.md#oh_arkui_notifydragresult)接口将最终结果回传至系统，并在所有处理完成后调用 [OH\_ArkUI\_NotifyDragEndPendingDone](capi-drag-and-drop-h.md#oh_arkui_notifydragendpendingdone)。最大等待时间为2秒。 |
| [int32\_t OH\_ArkUI\_NotifyDragResult(int32\_t requestIdentify, ArkUI\_DragResult result)](capi-drag-and-drop-h.md#oh_arkui_notifydragresult) | 通知系统最终拖拽结果。系统会校验请求标识符是否与[OH\_ArkUI\_DragEvent\_RequestDragEndPending](capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending)返回的一致，不一致则忽略本次调用。 |
| [int32\_t OH\_ArkUI\_NotifyDragEndPendingDone(int32\_t requestIdentify)](capi-drag-and-drop-h.md#oh_arkui_notifydragendpendingdone) | 通知系统所有异步处理已完成，可结束拖拽结束挂起状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_EnableDropDisallowedBadge(ArkUI\_ContextHandle uiContext, bool enabled)](capi-drag-and-drop-h.md#oh_arkui_enabledropdisallowedbadge) | 设置是否可以显示禁用角标。 |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointXToGlobalDisplay(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_gettouchpointxtoglobaldisplay) | 从ArkUI\_DragEvent中获取跟手点相对于全局屏幕的x轴坐标。 |
| [float OH\_ArkUI\_DragEvent\_GetTouchPointYToGlobalDisplay(ArkUI\_DragEvent\* event)](capi-drag-and-drop-h.md#oh_arkui_dragevent_gettouchpointytoglobaldisplay) | 从ArkUI\_DragEvent中获取跟手点相对于全局屏幕的y轴坐标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_GetDragSource(ArkUI\_DragEvent\* event, char \*bundleName, int32\_t length)](capi-drag-and-drop-h.md#oh_arkui_dragevent_getdragsource) | 获取拖拽发起方的应用包名信息，需要传递一个字符数组来接收包名字符串，并显式指明数组长度，该数组长度不小于128个字符。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_DragEvent\_IsRemote(ArkUI\_DragEvent\* event, bool\* isRemote)](capi-drag-and-drop-h.md#oh_arkui_dragevent_isremote) | 判断当前的拖拽操作是否是跨设备拖拽。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_DragResult

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DragResult
```

**描述：**

拖拽结果定义，由数据接收方设置，并由系统传递给数据拖出方，拖出方可感知接收方对数据的处理结果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DRAG\_RESULT\_SUCCESSFUL = 0 | 拖拽处理成功。 |
| ARKUI\_DRAG\_RESULT\_FAILED = 1 | 拖拽处理失败。 |
| ARKUI\_DRAG\_RESULT\_CANCELED = 2 | 拖拽处理取消。 |

### ArkUI\_DropOperation

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DropOperation
```

**描述：**

定义拖拽释放时的数据处理方式，影响角标的显示。当设置为复制行为时角标显示加号，设置为剪切行为时角标不显示加号。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DROP\_OPERATION\_COPY = 0 | 复制行为。 |
| ARKUI\_DROP\_OPERATION\_MOVE = 1 | 剪切行为。 |

### ArkUI\_PreDragStatus

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_PreDragStatus
```

**描述：**

定义拖拽发起前的长按交互阶段的变化状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PRE\_DRAG\_STATUS\_UNKNOWN = -1 | Unknown。 |
| ARKUI\_PRE\_DRAG\_STATUS\_ACTION\_DETECTING = 0 | 拖拽手势启动阶段。 |
| ARKUI\_PRE\_DRAG\_STATUS\_READY\_TO\_TRIGGER\_DRAG = 1 | 拖拽准备完成，可发起拖拽阶段。 |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LIFT\_STARTED = 2 | 拖拽浮起动效发起阶段。 |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LIFT\_FINISHED = 3 | 拖拽浮起动效结束阶段。 |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LANDING\_STARTED = 4 | 拖拽落回动效发起阶段。 |
| ARKUI\_PRE\_DRAG\_STATUS\_PREVIEW\_LANDING\_FINISHED = 5 | 拖拽落回动效结束阶段。 |
| ARKUI\_PRE\_DRAG\_STATUS\_CANCELED\_BEFORE\_DRAG = 6 | 拖拽浮起落位动效中断。 |

### ArkUI\_DragPreviewScaleMode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DragPreviewScaleMode
```

**描述：**

拖拽预览缩放模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DRAG\_PREVIEW\_SCALE\_AUTO = 0 | 系统根据拖拽场景自动改变跟手点位置，根据规则自动对拖拽背板图进行缩放变换等。 |
| ARKUI\_DRAG\_PREVIEW\_SCALE\_DISABLED = 1 | 禁用系统对拖拽背板图的缩放行为。 |

### ArkUI\_DragStatus

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_DragStatus
```

**描述：**

拖拽状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DRAG\_STATUS\_UNKNOWN = -1 | 未知的拖拽状态。 |
| ARKUI\_DRAG\_STATUS\_STARTED = 0 | 拖拽开始。 |
| ARKUI\_DRAG\_STATUS\_ENDED = 1 | 拖拽结束。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_NodeEvent\_GetDragEvent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DragEvent* OH_ArkUI_NodeEvent_GetDragEvent(ArkUI_NodeEvent* nodeEvent)
```

**描述：**

从 NodeEvent 中获取DragEvent。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* nodeEvent | ArkUI\_NodeEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* | ArkUI\_DragEvent 事件指针，当传入的 NodeEvent 无效或不是拖拽相关的事件时，则返回空。 |

### OH\_ArkUI\_NodeEvent\_GetPreDragStatus()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_PreDragStatus OH_ArkUI_NodeEvent_GetPreDragStatus(ArkUI_NodeEvent* nodeEvent)
```

**描述：**

获取预览拖拽事件状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* nodeEvent | ArkUI\_NodeEvent节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PreDragStatus](capi-drag-and-drop-h.md#arkui_predragstatus) | ArkUI\_PreDragStatus 拖拽发起前交互状态。 |

### OH\_ArkUI\_DragEvent\_DisableDefaultDropAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_DisableDefaultDropAnimation(ArkUI_DragEvent* event, bool disable)
```

**描述：**

设置是否禁用松手时的系统默认动效，默认不禁用，通常在应用需要自定义落位动效时配置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| bool disable | 是否禁用松手时的系统默认动效，true禁用，false不禁用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_SetSuggestedDropOperation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_SetSuggestedDropOperation(ArkUI_DragEvent* event, ArkUI_DropOperation dropOperation)
```

**描述：**

设置数据处理方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [ArkUI\_DropOperation](capi-drag-and-drop-h.md#arkui_dropoperation) dropOperation | 角标显示状态的类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_SetDragResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_SetDragResult(ArkUI_DragEvent* event, ArkUI_DragResult result)
```

**描述：**

设置拖拽事件的结果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [ArkUI\_DragResult](capi-drag-and-drop-h.md#arkui_dragresult) result | 拖拽数据处理结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_SetData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_SetData(ArkUI_DragEvent* event, OH_UdmfData* data)
```

**描述：**

向ArkUI\_DragEvent中设置拖拽数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [OH\_UdmfData](capi-udmf-oh-udmfdata.md)\* data | 拖拽数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_SetDataLoadParams()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_DragEvent_SetDataLoadParams(ArkUI_DragEvent* event, OH_UdmfDataLoadParams* dataLoadParams)
```

**描述：**

使用此方法为系统提供一个数据加载参数，而不是直接提供一个完整的数据对象。当用户拖拽到目标应用程序并落入时，系统将使用dataLoadParams请求数据。可以极大地提高拖拽大量数据的效率，以及目标应用程序中处理落入数据的效率。此方法应始终优先于[OH\_ArkUI\_DragEvent\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdata)使用。请参考**udmf.h**中的[OH\_UdmfDataLoadParams\_Create](capi-udmf-h.md#oh_udmfdataloadparams_create)了解如何创建和准备数据加载参数。该方法与[OH\_ArkUI\_DragEvent\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragevent_setdata)存在冲突，系统始终以最后调用的方法为准。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [OH\_UdmfDataLoadParams](capi-udmf-oh-udmfdataloadparams.md)\* dataLoadParams | 落入操作时使用的数据加载参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_GetUdmfData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_GetUdmfData(ArkUI_DragEvent* event, OH_UdmfData *data)
```

**描述：**

从ArkUI\_DragEvent中获取拖拽默认相关数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [OH\_UdmfData](capi-udmf-oh-udmfdata.md) \*data | OH\_UdmfData 拖拽的数据指针，应用在接收时需通过 [OH\_UdmfData\_Create](capi-udmf-h.md#oh_udmfdata_create) 方法创建一个用于接收数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_GetDataTypeCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_GetDataTypeCount(ArkUI_DragEvent* event, int32_t* count)
```

**描述：**

从ArkUI\_DragEvent中获取所拖拽的数据类型种类个数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| int32\_t\* count | 出参，返回所拖拽数据的类型的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_GetDataTypes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_GetDataTypes(ArkUI_DragEvent *event, char *eventTypeArray[], int32_t length, int32_t maxStrLen)
```

**描述：**

从ArkUI\_DragEvent中获取拖拽数据的类型列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md) \*event | ArkUI\_DragEvent事件指针。 |
| char \*eventTypeArray[] | 返回拖拽数据的类型列表，需要先自行创建字符串数组。 |
| int32\_t length | 数组总长度，不应少于使用OH\_ArkUI\_DragEvent\_GetDataTypesCount获取到的数量。 |
| int32\_t maxStrLen | 拖拽数据类型的最大字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-native-type-h.md#arkui_errorcode) 传入的缓冲区大小异常。 |

### OH\_ArkUI\_DragEvent\_GetDragResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_GetDragResult(ArkUI_DragEvent* event, ArkUI_DragResult* result)
```

**描述：**

从ArkUI\_DragEvent中获取拖拽结果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [ArkUI\_DragResult](capi-drag-and-drop-h.md#arkui_dragresult)\* result | 出参，返回拖拽事件对应的拖拽结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_GetDropOperation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_GetDropOperation(ArkUI_DragEvent* event, ArkUI_DropOperation* operation)
```

**描述：**

从ArkUI\_DragEvent中获取数据处理方式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [ArkUI\_DropOperation](capi-drag-and-drop-h.md#arkui_dropoperation)\* operation | 数据的处理方式. |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  可能原因: 1. 参数为空或event非有效的DragEvent. |

### OH\_ArkUI\_DragEvent\_GetPreviewTouchPointX()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetPreviewTouchPointX(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取预览图跟手点的x轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetPreviewTouchPointY()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetPreviewTouchPointY(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取预览图跟手点的y轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点的y轴坐标，单位px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetPreviewRectWidth()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetPreviewRectWidth(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取预览图的宽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手图宽度，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetPreviewRectHeight()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetPreviewRectHeight(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取预览图的高。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手图高度，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetTouchPointXToWindow()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetTouchPointXToWindow(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取跟手点相对于window的x轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回跟手点相对于window的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetTouchPointYToWindow()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetTouchPointYToWindow(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取跟手点相对于window的y轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回跟手点相对于window的y轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetTouchPointXToDisplay()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetTouchPointXToDisplay(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取跟手点相对于当前Display的x轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于当前Display的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetTouchPointYToDisplay()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetTouchPointYToDisplay(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取跟手点相对于当前Display的y轴坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于当前Display的y轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetVelocityX()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetVelocityX(ArkUI_DragEvent* event)
```

**描述：**

获取当前拖拽的x轴方向拖动速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回当前拖拽的x轴方向移动速度，单位为px/s，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetVelocityY()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetVelocityY(ArkUI_DragEvent* event)
```

**描述：**

获取当前拖拽的y轴方向拖动速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回当前拖拽的y轴方向移动速度，单位为px/s，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetVelocity()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetVelocity(ArkUI_DragEvent* event)
```

**描述：**

获取当前拖拽的主方向拖动速度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回当前拖拽移动速度，单位为px/s，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetModifierKeyStates()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_GetModifierKeyStates(ArkUI_DragEvent* event, uint64_t* keys)
```

**描述：**

获取功能键按压状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| uint64\_t\* keys | 返回当前处于按下状态的修饰键组合（Ctrl、Shift和Alt），应用可通过位运算进行判断。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_StartDataLoading()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_StartDataLoading(ArkUI_DragEvent* event, OH_UdmfGetDataParams* options, char* key, unsigned int keyLen)
```

**描述：**

使用指定的同步参数开始数据同步。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| [OH\_UdmfGetDataParams](capi-udmf-oh-udmfgetdataparams.md)\* options | OH\_UdmfGetDataParams参数指针。 |
| char\* key | 返回数据设置成功之后的key值，字符串长度不小于[UDMF\_KEY\_BUFFER\_LEN](capi-udmf-h.md#udmf_key_buffer_len)。 |
| unsigned int keyLen | 表示key字符串的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CancelDataLoading()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_CancelDataLoading(ArkUI_ContextHandle uiContext, const char* key)
```

**描述：**

取消正在进行的数据同步。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| const char\* key | 表示数据的key值并通过 [OH\_ArkUI\_DragEvent\_StartDataLoading](capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading) 返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DisableDropDataPrefetchOnNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DisableDropDataPrefetchOnNode(ArkUI_NodeHandle node, bool disabled)
```

**描述：**

设置是否在执行[NODE\_ON\_DROP](capi-native-node-h.md#arkui_nodeeventtype)之前禁用数据预获取过程。系统将重试获取数据，直到达到最大时间限制（目前为2.4秒），这对跨设备的拖动操作非常有用，因为它有助于系统稳定通信。然而，对于[OH\_ArkUI\_DragEvent\_StartDataLoading](capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading)方法而言，这一特性显得多余。该方法采用异步机制获取数据，因此在NODE\_ON\_DROP中使用[OH\_ArkUI\_DragEvent\_StartDataLoading](capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading)时，为了避免在NODE\_ON\_DROP执行前意外获取数据，必须将此字段设置为true。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |
| bool disabled | 表示是禁用数据预取过程。true表示禁止，false表示不禁止。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetDragEventStrictReportWithNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetDragEventStrictReportWithNode(ArkUI_NodeHandle node, bool enabled)
```

**描述：**

控制是否使能严格dragEvent上报，建议开启；默认是不开启的；当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，需要通过传入一个当前UI实例上的一个具体的组件节点来关联。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |
| bool enabled | 是否开启严格上报。true表示开启严格上报，false表示关闭严格上报。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetDragEventStrictReportWithContext()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetDragEventStrictReportWithContext(ArkUI_ContextHandle uiContext, bool enabled)
```

**描述：**

控制是否使能严格dragEvent上报，建议开启；默认是不开启的;当不开启时，从父组件拖移进子组件时，父组件并不会收到leave的通知；而开启之后，只要前后两个组件发生变化，上一个组件就会收到leave，新的组件收到enter通知；该配置与具体的UI实例相关，可通过传入一个UI实例进行关联。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例指针。 |
| bool enabled | 是否开启严格上报。true表示开启严格上报，false表示关闭严格上报。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetNodeAllowedDropDataTypes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetNodeAllowedDropDataTypes(ArkUI_NodeHandle node, const char* typesArray[], int32_t count)
```

**描述：**

配置组件允许接受落入的数据类型，该接口会重置通过 [OH\_ArkUI\_DisallowNodeAnyDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_disallownodeanydropdatatypes) 或[OH\_ArkUI\_AllowNodeAllDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_allownodealldropdatatypes)进行的配置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |
| const char\* typesArray[] | 允许落入的数据类型数组。 |
| int32\_t count | 数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DisallowNodeAnyDropDataTypes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DisallowNodeAnyDropDataTypes(ArkUI_NodeHandle node)
```

**描述：**

配置组件不允许接受任何数据类型，该接口会重置通过[OH\_ArkUI\_SetNodeAllowedDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_setnodealloweddropdatatypes)配置的数据类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AllowNodeAllDropDataTypes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_AllowNodeAllDropDataTypes(ArkUI_NodeHandle node)
```

**描述：**

配置组件允许接受任意数据类型，该接口会重置通过[OH\_ArkUI\_SetNodeAllowedDropDataTypes](capi-drag-and-drop-h.md#oh_arkui_setnodealloweddropdatatypes)配置的数据类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetNodeDraggable()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetNodeDraggable(ArkUI_NodeHandle node, bool enabled)
```

**描述：**

设置该组件是否允许进行拖拽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |
| bool enabled | 是否支持拖出。true表示支持拖出，false表示不支持拖出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetNodeDragPreview()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetNodeDragPreview(ArkUI_NodeHandle node, OH_PixelmapNative* preview)
```

**描述：**

设置组件在被拖拽时的自定义跟手图。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标组件节点指针。 |
| [OH\_PixelmapNative](capi-arkui-nativemodule-oh-pixelmapnative8h.md)\* preview | 自定义跟手图，使用 pixelmap 格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CreateDragPreviewOption()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DragPreviewOption* OH_ArkUI_CreateDragPreviewOption(void)
```

**描述：**

构建一个ArkUI\_DragPreviewOption对象。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* | ArkUI\_DragPreviewOption对象。 |

### OH\_ArkUI\_DragPreviewOption\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DragPreviewOption_Dispose(ArkUI_DragPreviewOption* option)
```

**描述：**

销毁跟手图自定义参数对象实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |

### OH\_ArkUI\_DragPreviewOption\_SetScaleMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragPreviewOption_SetScaleMode(ArkUI_DragPreviewOption* option, ArkUI_DragPreviewScaleMode scaleMode)
```

**描述：**

设置拖拽跟手图是否根据系统定义自动进行缩放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |
| [ArkUI\_DragPreviewScaleMode](capi-drag-and-drop-h.md#arkui_dragpreviewscalemode) scaleMode | 设置组件拖拽过程中的跟手图缩放模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragPreviewOption\_SetDefaultShadowEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragPreviewOption_SetDefaultShadowEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

**描述：**

设置跟手图背板默认的投影效果，默认不开启。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |
| bool enabled | 是否使用默认投影效果。true表示使用默认投影效果，false表示不使用默认投影效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragPreviewOption\_SetDefaultRadiusEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragPreviewOption_SetDefaultRadiusEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

**描述：**

设置跟手图背板默认的圆角效果（默认圆角半径为12.0vp），默认不开启。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |
| bool enabled | 是否开启圆角效果显示。true表示开启圆角效果显示，false表示不开启圆角效果显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragPreviewOption_SetNumberBadgeEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

**描述：**

设置跟手图背板是否显示角标,开启后,系统会根据拖拽数量自动进行角标显示。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |
| bool enabled | 是否开启角标显示。true表示开启角标显示，false表示不开启角标显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragPreviewOption\_SetBadgeNumber()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragPreviewOption_SetBadgeNumber(ArkUI_DragPreviewOption* option, uint32_t forcedNumber)
```

**描述：**

强制显示角标的数量，覆盖[OH\_ArkUI\_DragPreviewOption\_SetNumberBadgeEnabled](capi-drag-and-drop-h.md#oh_arkui_dragpreviewoption_setnumberbadgeenabled)设置的值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |
| uint32\_t forcedNumber | 角标的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragPreviewOption\_SetDefaultAnimationBeforeLiftingEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragPreviewOption_SetDefaultAnimationBeforeLiftingEnabled(ArkUI_DragPreviewOption* option, bool enabled)
```

**描述：**

配置是否开启点按时的默认动画。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |
| bool enabled | 是否开启默认点按效果。true表示开启默认点按效果，false表示不开启默认点按效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetNodeDragPreviewOption()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetNodeDragPreviewOption(ArkUI_NodeHandle node, ArkUI_DragPreviewOption* option)
```

**描述：**

将构造的ArkUI\_DragPreviewOption设置给组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_CreateDragActionWithNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DragAction* OH_ArkUI_CreateDragActionWithNode(ArkUI_NodeHandle node)
```

**描述：**

创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个当前UI实例的某个组件节点来指定。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 组件节点指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* | ArkUI\_DragAction对象指针，如果创建失败，则返回空。 |

### OH\_ArkUI\_CreateDragActionWithContext()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DragAction* OH_ArkUI_CreateDragActionWithContext(ArkUI_ContextHandle uiContext)
```

**描述：**

创建一个拖拽操作对象，该对象需与一个UI实例相关联，可通过传入一个UI实例指针来关联。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* | ArkUI\_DragAction对象，如果创建失败，则返回空。 |

### OH\_ArkUI\_DragAction\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DragAction_Dispose(ArkUI_DragAction* dragAction)
```

**描述：**

销毁创建的 ArkUI\_DragAction 对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |

### OH\_ArkUI\_DragAction\_SetPointerId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_SetPointerId(ArkUI_DragAction* dragAction, int32_t pointer)
```

**描述：**

设置手指ID，当屏幕上仅有一只手指在操作时，手指ID为0；一般情况下，配置0即可。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| int32\_t pointer | 手指ID，范围0～9。取值超出时默认置为-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_SetPixelMaps()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_SetPixelMaps(ArkUI_DragAction* dragAction, OH_PixelmapNative* pixelmapArray[], int32_t size)
```

**描述：**

设置拖拽跟手图，只能使用 pixelmap 格式对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| [OH\_PixelmapNative](capi-arkui-nativemodule-oh-pixelmapnative8h.md)\* pixelmapArray[] | 拖拽跟手图位图数组。  **说明：** 该参数必须为堆上分配对象，请开发者手动管理其生命周期。 |
| int32\_t size | 拖拽跟手图数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_SetTouchPointX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_SetTouchPointX(ArkUI_DragAction* dragAction, float x)
```

**描述：**

设置跟手点，相对于设置的第一个pixelmap的左上角。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| float x | 跟手点坐标x值，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_SetTouchPointY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_SetTouchPointY(ArkUI_DragAction* dragAction, float y)
```

**描述：**

设置跟手点，相对于设置的第一个pixelmap的左上角。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| float y | 跟手点坐标y值，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_SetData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_SetData(ArkUI_DragAction* dragAction, OH_UdmfData* data)
```

**描述：**

设置拖拽数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| [OH\_UdmfData](capi-udmf-oh-udmfdata.md)\* data | 拖拽数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_SetDataLoadParams()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_DragAction_SetDataLoadParams(ArkUI_DragAction* dragAction,OH_UdmfDataLoadParams* dataLoadParams)
```

**描述：**

使用此方法为系统提供一个数据加载参数，而不是直接提供一个完整的数据对象。当用户拖拽到目标应用程序并落入时，系统将使用dataLoadParams请求数据。可以极大地提高拖拽大量数据的效率，以及目标应用程序中处理落入数据的效率。此方法应始终优先于[OH\_ArkUI\_DragAction\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdata)使用。请参考**udmf.h**中的[OH\_UdmfDataLoadParams\_Create](capi-udmf-h.md#oh_udmfdataloadparams_create)了解如何创建和准备数据加载参数。该方法与[OH\_ArkUI\_DragAction\_SetData](capi-drag-and-drop-h.md#oh_arkui_dragaction_setdata)存在冲突，系统始终以最后调用的方法为准。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| [OH\_UdmfDataLoadParams](capi-udmf-oh-udmfdataloadparams.md)\* dataLoadParams | 在落入操作时使用的数据加载参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_SetDragPreviewOption()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_SetDragPreviewOption(ArkUI_DragAction* dragAction, ArkUI_DragPreviewOption* option)
```

**描述：**

将构造的ArkUI\_DragPreviewOption设置给ArkUI\_DragAction。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| [ArkUI\_DragPreviewOption](capi-arkui-nativemodule-arkui-dragpreviewoption.md)\* option | 自定义参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_RegisterStatusListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragAction_RegisterStatusListener(ArkUI_DragAction* dragAction, void* userData,void(*listener)(ArkUI_DragAndDropInfo* dragAndDropInfo, void* userData))
```

**描述：**

注册拖拽状态监听回调，该回调可感知到拖拽已经发起或用户松手结束的状态，可通过该监听获取到落入方对数据的接收处理是否成功。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |
| void\* userData | 应用自定义数据。 |
| listener | 状态监听回调，回调触发时，系统会返回一个拖拽状态对象指针，该指针会在回调执行完成后被销毁，应用不应再持有。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_GetDisplayId()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_DragEvent_GetDisplayId(ArkUI_DragEvent* event, int32_t* displayId)
```

**描述：**

获取当前拖拽事件发生时所在的屏幕ID，不支持当eventType为NODE\_ON\_DRAG\_END时获取。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |
| int32\_t\* displayId | 返回当前拖拽事件发生时所在的屏幕ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragAction\_UnregisterStatusListener()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_DragAction_UnregisterStatusListener(ArkUI_DragAction* dragAction)
```

**描述：**

解注册拖拽状态监听回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽行为对象。 |

### OH\_ArkUI\_DragAndDropInfo\_GetDragStatus()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DragStatus OH_ArkUI_DragAndDropInfo_GetDragStatus(ArkUI_DragAndDropInfo* dragAndDropInfo)
```

**描述：**

获取[ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)发起拖拽的状态，获取异常时返回 ArkUI\_DRAG\_STATUS\_UNKNOWN。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAndDropInfo](capi-arkui-nativemodule-arkui-draganddropinfo.md)\* dragAndDropInfo | 拖拽状态监听返回的拖拽相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DragStatus](capi-drag-and-drop-h.md#arkui_dragstatus) | ArkUI\_DragStatus 拖拽状态，如果获取失败，返回默认值 ArkUI\_DRAG\_STATUS\_UNKNOWN。 |

### OH\_ArkUI\_DragAndDropInfo\_GetDragEvent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DragEvent* OH_ArkUI_DragAndDropInfo_GetDragEvent(ArkUI_DragAndDropInfo* dragAndDropInfo)
```

**描述：**

通过dragAndDropInfo获取到DragEvent，可通过DragEvent获取释放结果等。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAndDropInfo](capi-arkui-nativemodule-arkui-draganddropinfo.md)\* dragAndDropInfo | 拖拽状态监听返回的拖拽相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* | ArkUI\_DragEvent 拖拽事件，如果获取失败，则返回空。 |

### OH\_ArkUI\_StartDrag()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_StartDrag(ArkUI_DragAction* dragAction)
```

**描述：**

通过构造的DragAction对象发起拖拽。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragAction](capi-arkui-nativemodule-arkui-dragaction.md)\* dragAction | 拖拽action对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_RequestDragEndPending()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_DragEvent_RequestDragEndPending(ArkUI_DragEvent* event, int32_t* requestIdentify)
```

**描述：**

请求延迟处理拖拽结束事件，等待应用程序确认操作结果。应用程序需通过 [OH\_ArkUI\_NotifyDragResult](capi-drag-and-drop-h.md#oh_arkui_notifydragresult)接口将最终结果回传至系统，并在所有处理完成后调用 [OH\_ArkUI\_NotifyDragEndPendingDone](capi-drag-and-drop-h.md#oh_arkui_notifydragendpendingdone)。最大等待时间为2秒。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | 指向 **ArkUI\_DragEvent** 对象的指针。 |
| int32\_t\* requestIdentify | 系统自动生成的请求标识符，是一个输出参数，需要为一个有效的地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED](capi-native-type-h.md#arkui_errorcode) 当前阶段不允许该操作。 |

### OH\_ArkUI\_NotifyDragResult()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NotifyDragResult(int32_t requestIdentify, ArkUI_DragResult result)
```

**描述：**

通知系统最终拖拽结果。系统会校验请求标识符是否与[OH\_ArkUI\_DragEvent\_RequestDragEndPending](capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending)返回的一致，不一致则忽略本次调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t requestIdentify | 由 [OH\_ArkUI\_DragEvent\_RequestDragEndPending](capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending) 返回的标识符。 |
| [ArkUI\_DragResult](capi-drag-and-drop-h.md#arkui_dragresult) result | 拖拽结果枚举值（[ArkUI\_DragResult](capi-drag-and-drop-h.md#arkui_dragresult) 类型）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED](capi-native-type-h.md#arkui_errorcode) 当前阶段不允许该操作。 |

### OH\_ArkUI\_NotifyDragEndPendingDone()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NotifyDragEndPendingDone(int32_t requestIdentify)
```

**描述：**

通知系统所有异步处理已完成，可结束拖拽结束挂起状态。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t requestIdentify | 由 [OH\_ArkUI\_DragEvent\_RequestDragEndPending](capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending) 返回的标识符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_DRAG\_DROP\_OPERATION\_NOT\_ALLOWED](capi-native-type-h.md#arkui_errorcode) 当前阶段不允许该操作。 |

### OH\_ArkUI\_EnableDropDisallowedBadge()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_EnableDropDisallowedBadge(ArkUI_ContextHandle uiContext, bool enabled)
```

**描述：**

设置是否可以显示禁用角标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。 |
| bool enabled | 是否可以显示禁用角标。true表示可以显示禁用角标，false表示不可以显示禁用角标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_GetTouchPointXToGlobalDisplay()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetTouchPointXToGlobalDisplay(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取跟手点相对于全局屏幕的x轴坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于全局Display的x轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetTouchPointYToGlobalDisplay()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_DragEvent_GetTouchPointYToGlobalDisplay(ArkUI_DragEvent* event)
```

**描述：**

从ArkUI\_DragEvent中获取跟手点相对于全局屏幕的y轴坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | ArkUI\_DragEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | float 返回拖拽跟手点相对于全局Display的y轴坐标，单位为px，传入参数无效时返回默认值0。 |

### OH\_ArkUI\_DragEvent\_GetDragSource()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_DragEvent_GetDragSource(ArkUI_DragEvent* event, char *bundleName, int32_t length)
```

**描述：**

获取拖拽发起方的应用包名信息，需要传递一个字符数组来接收包名字符串，并显式指明数组长度，该数组长度不小于128个字符。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | 指向**ArkUI\_DragEvent**对象的指针。 |
| char \*bundleName | 用来接收拖起方包名的字符串数组，长度不应小于128个字符。 |
| int32\_t length | 用来显式指明传入的字符串数组长度，不应小于128个字符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_DragEvent\_IsRemote()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_DragEvent_IsRemote(ArkUI_DragEvent* event, bool* isRemote)
```

**描述：**

判断当前的拖拽操作是否是跨设备拖拽。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)\* event | 指向**ArkUI\_DragEvent**对象的指针。 |
| bool\* isRemote | 布尔变量指针，用来接收是否是跨设备拖拽。true表示是跨设备拖拽，false表示非跨设备拖拽。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
