---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h
title: native_node.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f57cc2fac1d960110a659d5128a134baf63019b4a849872868efec928b5e339d
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeNode接口的类型定义。

**引用文件：** <arkui/native\_node.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeNodeBaseSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeNodeBaseSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md) | ArkUI\_AttributeItem | 定义[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)函数通用入参结构。 |
| [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md) | ArkUI\_NodeComponentEvent | 定义组件回调事件的参数类型。 |
| [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md) | ArkUI\_StringAsyncEvent | 定义组件回调事件使用字符串参数的类型。 |
| [ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md) | ArkUI\_TextChangeEvent | 定义组件事件的混合类型数据。 |
| [ArkUI\_NativeNodeAPI\_1](capi-arkui-nativemodule-arkui-nativenodeapi-1.md) | ArkUI\_NativeNodeAPI\_1 | ArkUI提供的Native侧Node类型接口集合。Node模块相关接口需要在主线程上调用。 |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md) | ArkUI\_NodeEvent | 定义组件事件的通用结构类型。 |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md) | ArkUI\_NodeCustomEvent | 定义自定义组件事件的通用结构类型。 |
| [ArkUI\_NodeAdapter\*](capi-arkui-nativemodule-arkui-nodeadapter8h.md) | ArkUI\_NodeAdapterHandle | 定义组件适配器对象，用于滚动类组件的元素懒加载。 |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md) | ArkUI\_NodeAdapterEvent | 定义适配器事件对象。 |
| [ArkUI\_NodeContentEvent](capi-arkui-nativemodule-arkui-nodecontentevent.md) | ArkUI\_NodeContentEvent | 定义NodeContent事件的通用结构类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype) | ArkUI\_NodeType | 提供ArkUI在Native侧可创建组件类型。 |
| [ArkUI\_NodeAttributeType](capi-native-node-h.md#arkui_nodeattributetype) | ArkUI\_NodeAttributeType | 定义ArkUI在Native侧可以设置的属性样式集合。 |
| [ArkUI\_NodeEventType](capi-native-node-h.md#arkui_nodeeventtype) | ArkUI\_NodeEventType | 提供NativeNode组件支持的事件类型定义。 |
| [ArkUI\_NodeDirtyFlag](capi-native-node-h.md#arkui_nodedirtyflag) | ArkUI\_NodeDirtyFlag | 自定义组件调用**::markDirty**时，传递重新执行测量、布局或者绘制的标识类型。 |
| [ArkUI\_NodeCustomEventType](capi-native-node-h.md#arkui_nodecustomeventtype) | ArkUI\_NodeCustomEventType | 定义自定义组件事件类型。 |
| [ArkUI\_NodeAdapterEventType](capi-native-node-h.md#arkui_nodeadaptereventtype) | ArkUI\_NodeAdapterEventType | 定义节点适配器事件枚举值。 |
| [ArkUI\_NodeContentEventType](capi-native-node-h.md#arkui_nodecontenteventtype) | ArkUI\_NodeContentEventType | 定义NodeContent事件类型。 |
| [ArkUI\_InspectorErrorCode](capi-native-node-h.md#arkui_inspectorerrorcode) | ArkUI\_InspectorErrorCode | inspector错误码的枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NodeEventType OH\_ArkUI\_NodeEvent\_GetEventType(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_geteventtype) | - | 获取组件事件类型。 |
| [int32\_t OH\_ArkUI\_NodeEvent\_GetTargetId(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_gettargetid) | - | 获取事件自定义标识ID。该事件ID在调用[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)函数时作为参数传递进来，可应用于同一事件入口函数[registerNodeEventReceiver](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver)分发逻辑。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeEvent\_GetNodeHandle(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_getnodehandle) | - | 获取触发该事件的组件对象。 |
| [ArkUI\_UIInputEvent\* OH\_ArkUI\_NodeEvent\_GetInputEvent(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_getinputevent) | - | 获取组件事件中的输入事件（如触碰事件）数据。 |
| [ArkUI\_NodeComponentEvent\* OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_getnodecomponentevent) | - | 获取组件事件中的数字类型数据。 |
| [ArkUI\_StringAsyncEvent\* OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_getstringasyncevent) | - | 获取组件事件中的字符串数据。 |
| [ArkUI\_TextChangeEvent\* OH\_ArkUI\_NodeEvent\_GetTextChangeEvent(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_gettextchangeevent) | - | 获取组件事件中的ArkUI\_TextChangeEvent数据。 |
| [void\* OH\_ArkUI\_NodeEvent\_GetUserData(ArkUI\_NodeEvent\* event)](capi-native-node-h.md#oh_arkui_nodeevent_getuserdata) | - | 获取组件事件中的用户自定义数据。该自定义参数在调用[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)函数时作为参数传递进来，可应用于事件触发时的业务逻辑处理。 |
| [int32\_t OH\_ArkUI\_NodeEvent\_GetNumberValue(ArkUI\_NodeEvent\* event, int32\_t index, ArkUI\_NumberValue\* value)](capi-native-node-h.md#oh_arkui_nodeevent_getnumbervalue) | - | 获取组件回调事件的数字类型参数。 |
| [int32\_t OH\_ArkUI\_NodeEvent\_GetStringValue(ArkUI\_NodeEvent\* event, int32\_t index, char\*\* string, int32\_t\* stringSize)](capi-native-node-h.md#oh_arkui_nodeevent_getstringvalue) | - | 获取组件回调事件的字符串类型参数，字符串数据仅在事件回调过程中有效，需要在事件回调外使用建议进行额外拷贝处理。 |
| [int32\_t OH\_ArkUI\_NodeEvent\_SetReturnNumberValue(ArkUI\_NodeEvent\* event, ArkUI\_NumberValue\* value, int32\_t size)](capi-native-node-h.md#oh_arkui_nodeevent_setreturnnumbervalue) | - | 设置组件回调事件的返回值。 |
| [ArkUI\_NodeAdapterHandle OH\_ArkUI\_NodeAdapter\_Create()](capi-native-node-h.md#oh_arkui_nodeadapter_create) | - | 创建组件适配器对象。 |
| [void OH\_ArkUI\_NodeAdapter\_Dispose(ArkUI\_NodeAdapterHandle handle)](capi-native-node-h.md#oh_arkui_nodeadapter_dispose) | - | 销毁组件适配器对象。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount(ArkUI\_NodeAdapterHandle handle, uint32\_t size)](capi-native-node-h.md#oh_arkui_nodeadapter_settotalnodecount) | - | 设置Adapter中的元素总数。 |
| [uint32\_t OH\_ArkUI\_NodeAdapter\_GetTotalNodeCount(ArkUI\_NodeAdapterHandle handle)](capi-native-node-h.md#oh_arkui_nodeadapter_gettotalnodecount) | - | 获取Adapter中的元素总数。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver(ArkUI\_NodeAdapterHandle handle, void\* userData, void (\*receiver)(ArkUI\_NodeAdapterEvent\* event))](capi-native-node-h.md#oh_arkui_nodeadapter_registereventreceiver) | - | 注册Adapter相关回调事件。 |
| [void OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver(ArkUI\_NodeAdapterHandle handle)](capi-native-node-h.md#oh_arkui_nodeadapter_unregistereventreceiver) | - | 注销Adapter相关回调事件。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_ReloadAllItems(ArkUI\_NodeAdapterHandle handle)](capi-native-node-h.md#oh_arkui_nodeadapter_reloadallitems) | - | 通知Adapter进行全量元素变化。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_ReloadItem(ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)](capi-native-node-h.md#oh_arkui_nodeadapter_reloaditem) | - | 通知Adapter进行局部元素变化。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_RemoveItem(ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)](capi-native-node-h.md#oh_arkui_nodeadapter_removeitem) | - | 通知Adapter进行局部元素删除。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_InsertItem(ArkUI\_NodeAdapterHandle handle, uint32\_t startPosition, uint32\_t itemCount)](capi-native-node-h.md#oh_arkui_nodeadapter_insertitem) | - | 通知Adapter进行局部元素插入。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_MoveItem(ArkUI\_NodeAdapterHandle handle, uint32\_t from, uint32\_t to)](capi-native-node-h.md#oh_arkui_nodeadapter_moveitem) | - | 通知Adapter进行局部元素移位。 |
| [int32\_t OH\_ArkUI\_NodeAdapter\_GetAllItems(ArkUI\_NodeAdapterHandle handle, ArkUI\_NodeHandle\*\* items, uint32\_t\* size)](capi-native-node-h.md#oh_arkui_nodeadapter_getallitems) | - | 获取存储在Adapter中的所有元素。接口调用会返回元素的数组对象指针，该指针指向的内存数据需要开发者手动释放。 |
| [void\* OH\_ArkUI\_NodeAdapterEvent\_GetUserData(ArkUI\_NodeAdapterEvent\* event)](capi-native-node-h.md#oh_arkui_nodeadapterevent_getuserdata) | - | 获取注册事件时传入的自定义数据。 |
| [ArkUI\_NodeAdapterEventType OH\_ArkUI\_NodeAdapterEvent\_GetType(ArkUI\_NodeAdapterEvent\* event)](capi-native-node-h.md#oh_arkui_nodeadapterevent_gettype) | - | 获取事件类型。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode(ArkUI\_NodeAdapterEvent\* event)](capi-native-node-h.md#oh_arkui_nodeadapterevent_getremovednode) | - | 获取需要销毁的事件中待销毁的元素。 |
| [uint32\_t OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex(ArkUI\_NodeAdapterEvent\* event)](capi-native-node-h.md#oh_arkui_nodeadapterevent_getitemindex) | - | 获取适配器事件时需要操作的元素序号。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeAdapterEvent\_GetHostNode(ArkUI\_NodeAdapterEvent\* event)](capi-native-node-h.md#oh_arkui_nodeadapterevent_gethostnode) | - | 获取使用该适配器的滚动类容器节点。 |
| [int32\_t OH\_ArkUI\_NodeAdapterEvent\_SetItem(ArkUI\_NodeAdapterEvent\* event, ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodeadapterevent_setitem) | - | 设置需要新增到Adapter中的组件。 |
| [int32\_t OH\_ArkUI\_NodeAdapterEvent\_SetNodeId(ArkUI\_NodeAdapterEvent\* event, int32\_t id)](capi-native-node-h.md#oh_arkui_nodeadapterevent_setnodeid) | - | 设置生成的组件标识。 |
| [ArkUI\_LayoutConstraint\* OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_getlayoutconstraintinmeasure) | - | 通过自定义组件事件获取测算过程中的约束尺寸。 |
| [ArkUI\_IntOffset OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_getpositioninlayout) | - | 通过自定义组件事件获取在布局阶段期望自身相对父组件的位置。 |
| [ArkUI\_DrawContext\* OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_getdrawcontextindraw) | - | 通过自定义组件事件获取绘制上下文。请开发者在使用完成后及时释放获取的绘制上下文。 |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_geteventtargetid) | - | 通过自定义组件事件获取自定义事件ID。 |
| [void\* OH\_ArkUI\_NodeCustomEvent\_GetUserData(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_getuserdata) | - | 通过自定义组件事件获取自定义事件参数。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeCustomEvent\_GetNodeHandle(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_getnodehandle) | - | 通过自定义组件事件获取组件对象。 |
| [ArkUI\_NodeCustomEventType OH\_ArkUI\_NodeCustomEvent\_GetEventType(ArkUI\_NodeCustomEvent\* event)](capi-native-node-h.md#oh_arkui_nodecustomevent_geteventtype) | - | 通过自定义组件事件获取事件类型。 |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanMeasureInfo(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanMeasureInfo\* info)](capi-native-node-h.md#oh_arkui_nodecustomevent_getcustomspanmeasureinfo) | - | 通过自定义组件事件获取自定义段落组件的测量信息。 |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_SetCustomSpanMetrics(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanMetrics\* metrics)](capi-native-node-h.md#oh_arkui_nodecustomevent_setcustomspanmetrics) | - | 通过自定义组件事件设置自定义段落的度量指标。 |
| [int32\_t OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanDrawInfo(ArkUI\_NodeCustomEvent\* event, ArkUI\_CustomSpanDrawInfo\* info)](capi-native-node-h.md#oh_arkui_nodecustomevent_getcustomspandrawinfo) | - | 通过自定义组件事件获取自定义段落组件的绘制信息。 |
| [typedef void (\*ArkUI\_NodeContentCallback)(ArkUI\_NodeContentEvent\* event)](capi-native-node-h.md#arkui_nodecontentcallback) | ArkUI\_NodeContentCallback | 定义NodeContent事件的回调函数类型。 |
| [int32\_t OH\_ArkUI\_NodeContent\_RegisterCallback(ArkUI\_NodeContentHandle content, ArkUI\_NodeContentCallback callback)](capi-native-node-h.md#oh_arkui_nodecontent_registercallback) | - | 注册NodeContent事件函数。 |
| [ArkUI\_NodeContentEventType OH\_ArkUI\_NodeContentEvent\_GetEventType(ArkUI\_NodeContentEvent\* event)](capi-native-node-h.md#oh_arkui_nodecontentevent_geteventtype) | - | 获取触发NodeContent事件的事件类型。 |
| [ArkUI\_NodeContentHandle OH\_ArkUI\_NodeContentEvent\_GetNodeContentHandle(ArkUI\_NodeContentEvent\* event)](capi-native-node-h.md#oh_arkui_nodecontentevent_getnodecontenthandle) | - | 获取触发事件的NodeContent对象。 |
| [int32\_t OH\_ArkUI\_NodeContent\_SetUserData(ArkUI\_NodeContentHandle content, void\* userData)](capi-native-node-h.md#oh_arkui_nodecontent_setuserdata) | - | 在NodeContent对象上保存自定义数据。 |
| [void\* OH\_ArkUI\_NodeContent\_GetUserData(ArkUI\_NodeContentHandle content)](capi-native-node-h.md#oh_arkui_nodecontent_getuserdata) | - | 获取在NodeContent对象上保存的自定义数据。 |
| [int32\_t OH\_ArkUI\_NodeContent\_AddNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodecontent_addnode) | - | 将一个ArkUI组件节点添加到对应的NodeContent对象下。 |
| [int32\_t OH\_ArkUI\_NodeContent\_RemoveNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodecontent_removenode) | - | 删除NodeContent对象下的一个ArkUI组件节点。 |
| [int32\_t OH\_ArkUI\_NodeContent\_InsertNode(ArkUI\_NodeContentHandle content, ArkUI\_NodeHandle node, int32\_t position)](capi-native-node-h.md#oh_arkui_nodecontent_insertnode) | - | 将一个ArkUI组件节点插入到对应的NodeContent对象的特定位置下。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutSize(ArkUI\_NodeHandle node, ArkUI\_IntSize\* size)](capi-native-node-h.md#oh_arkui_nodeutils_getlayoutsize) | - | 获取组件布局区域的大小。布局区域大小不包含图形变化属性，如缩放。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPosition(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* localOffset)](capi-native-node-h.md#oh_arkui_nodeutils_getlayoutposition) | - | 获取组件布局区域相对父组件的位置。布局区域相对位置不包含图形变化属性，如平移。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInWindow(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* globalOffset)](capi-native-node-h.md#oh_arkui_nodeutils_getlayoutpositioninwindow) | - | 获取组件布局区域相对窗口的位置。布局区域相对位置不包含图形变化属性，如平移。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInScreen(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* screenOffset)](capi-native-node-h.md#oh_arkui_nodeutils_getlayoutpositioninscreen) | - | 获取组件布局区域相对屏幕的位置。布局区域相对位置不包含图形变化属性，如平移。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLayoutPositionInGlobalDisplay(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* offset)](capi-native-node-h.md#oh_arkui_nodeutils_getlayoutpositioninglobaldisplay) | - | 获取组件相对于全局屏幕的偏移。布局区域相对位置不包含图形变化属性，如平移。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInWindow(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* translateOffset)](capi-native-node-h.md#oh_arkui_nodeutils_getpositionwithtranslateinwindow) | - | 获取组件在窗口中的位置，包含了图形平移变化属性。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInScreen(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* translateOffset)](capi-native-node-h.md#oh_arkui_nodeutils_getpositionwithtranslateinscreen) | - | 获取组件在屏幕中的位置，包含了图形平移变化属性。 |
| [void OH\_ArkUI\_NodeUtils\_AddCustomProperty(ArkUI\_NodeHandle node, const char\* name, const char\* value)](capi-native-node-h.md#oh_arkui_nodeutils_addcustomproperty) | - | 设置组件的自定义属性。该接口仅在主线程生效。 |
| [void OH\_ArkUI\_NodeUtils\_RemoveCustomProperty(ArkUI\_NodeHandle node, const char\* name)](capi-native-node-h.md#oh_arkui_nodeutils_removecustomproperty) | - | 移除组件已设置的自定义属性。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetCustomProperty(ArkUI\_NodeHandle node, const char\* name, ArkUI\_CustomProperty\*\* handle)](capi-native-node-h.md#oh_arkui_nodeutils_getcustomproperty) | - | 获取组件的自定义属性的值。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeUtils\_GetParentInPageTree(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodeutils_getparentinpagetree) | - | 获取父节点，可获取由ArkTs创建的组件节点。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo(ArkUI\_NodeHandle head, ArkUI\_ActiveChildrenInfo\*\* handle)](capi-native-node-h.md#oh_arkui_nodeutils_getactivechildreninfo) | - | 获取某个节点所有活跃的子节点。Span将不会被计入子节点的统计中。 |
| [ArkUI\_NodeHandle OH\_ArkUI\_NodeUtils\_GetCurrentPageRootNode(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodeutils_getcurrentpagerootnode) | - | 获取当前页面的根节点。 |
| [bool OH\_ArkUI\_NodeUtils\_IsCreatedByNDK(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodeutils_iscreatedbyndk) | - | 获取组件是否由C-API创建的标签。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetNodeType(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nodeutils_getnodetype) | - | 获取节点的类型。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetWindowInfo(ArkUI\_NodeHandle node, ArkUI\_HostWindowInfo\*\* info)](capi-native-node-h.md#oh_arkui_nodeutils_getwindowinfo) | - | 获取节点所属的窗口信息。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_MoveTo(ArkUI\_NodeHandle node, ArkUI\_NodeHandle target\_parent, int32\_t index)](capi-native-node-h.md#oh_arkui_nodeutils_moveto) | - | 将节点移动到目标父节点下，作为子节点。 |
| [int32\_t OH\_ArkUI\_NativeModule\_InvalidateAttributes(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nativemodule_invalidateattributes) | - | 在当前帧触发节点属性更新。 |
| [int32\_t OH\_ArkUI\_List\_CloseAllSwipeActions(ArkUI\_NodeHandle node, void\* userData, void (\*onFinish)(void\* userData))](capi-native-node-h.md#oh_arkui_list_closeallswipeactions) | - | 收起展开状态下的[ListItem](ts-container-listitem.md)。 |
| [ArkUI\_ContextHandle OH\_ArkUI\_GetContextByNode(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_getcontextbynode) | - | 获取当前节点所在页面的UI的上下文实例对象指针。 |
| [int32\_t OH\_ArkUI\_RegisterSystemColorModeChangeEvent(ArkUI\_NodeHandle node,void\* userData, void (\*onColorModeChange)(ArkUI\_SystemColorMode colorMode, void\* userData))](capi-native-node-h.md#oh_arkui_registersystemcolormodechangeevent) | - | 注册系统深浅色变更事件。同一组件仅能注册一个系统深浅变更回调。示例请参考：[监听组件事件](../harmonyos-guides/ndk-listen-to-component-events.md)。 |
| [void OH\_ArkUI\_UnregisterSystemColorModeChangeEvent(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_unregistersystemcolormodechangeevent) | - | 注销系统深浅色变更事件。 |
| [int32\_t OH\_ArkUI\_RegisterSystemFontStyleChangeEvent(ArkUI\_NodeHandle node,void\* userData, void (\*onFontStyleChange)(ArkUI\_SystemFontStyleEvent\* event, void\* userData))](capi-native-node-h.md#oh_arkui_registersystemfontstylechangeevent) | - | 注册系统字体变更事件。同一组件仅能注册一个系统字体变更回调。 |
| [void OH\_ArkUI\_UnregisterSystemFontStyleChangeEvent(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_unregistersystemfontstylechangeevent) | - | 注销系统字体变更事件。 |
| [float OH\_ArkUI\_SystemFontStyleEvent\_GetFontSizeScale(const ArkUI\_SystemFontStyleEvent\* event)](capi-native-node-h.md#oh_arkui_systemfontstyleevent_getfontsizescale) | - | 获取系统字体变更事件的字体大小值。 |
| [float OH\_ArkUI\_SystemFontStyleEvent\_GetFontWeightScale(const ArkUI\_SystemFontStyleEvent\* event)](capi-native-node-h.md#oh_arkui_systemfontstyleevent_getfontweightscale) | - | 获取系统字体变更事件的字体粗细值。 |
| [int32\_t OH\_ArkUI\_RegisterLayoutCallbackOnNodeHandle(ArkUI\_NodeHandle node,void\* userData, void (\*onLayoutCompleted)(void\* userData))](capi-native-node-h.md#oh_arkui_registerlayoutcallbackonnodehandle) | - | 注册指定节点的布局完成回调函数。 |
| [int32\_t OH\_ArkUI\_RegisterDrawCallbackOnNodeHandle(ArkUI\_NodeHandle node,void\* userData, void (\*onDrawCompleted)(void\* userData))](capi-native-node-h.md#oh_arkui_registerdrawcallbackonnodehandle) | - | 注册指定节点的绘制完成回调函数。 |
| [int32\_t OH\_ArkUI\_UnregisterLayoutCallbackOnNodeHandle(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_unregisterlayoutcallbackonnodehandle) | - | 取消注册指定节点的布局完成回调函数。 |
| [int32\_t OH\_ArkUI\_UnregisterDrawCallbackOnNodeHandle(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_unregisterdrawcallbackonnodehandle) | - | 取消注册指定节点的绘制完成回调函数。 |
| [int32\_t OH\_ArkUI\_GetNodeSnapshot(ArkUI\_NodeHandle node, ArkUI\_SnapshotOptions\* snapshotOptions,OH\_PixelmapNative\*\* pixelmap)](capi-native-node-h.md#oh_arkui_getnodesnapshot) | - | 获取给定组件的截图，若节点不在组件树上或尚未渲染，截图操作将会失败。当pixelmap不再使用时，应通过调用[OH\_PixelmapNative\_Release](capi-pixelmap-native-h.md#oh_pixelmapnative_release)来释放。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById(const char\* id, ArkUI\_NodeHandle\* node)](capi-native-node-h.md#oh_arkui_nodeutils_getattachednodehandlebyid) | - | 根据用户id获取目标节点。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId(const uint32\_t uniqueId, ArkUI\_NodeHandle\* node)](capi-native-node-h.md#oh_arkui_nodeutils_getnodehandlebyuniqueid) | - | 通过uniqueId获取节点。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetNodeUniqueId(ArkUI\_NodeHandle node, int32\_t\* uniqueId)](capi-native-node-h.md#oh_arkui_nodeutils_getnodeuniqueid) | - | 获取目标节点的uniqueId。 |
| [int32\_t OH\_ArkUI\_NativeModule\_AdoptChild(ArkUI\_NodeHandle node, ArkUI\_NodeHandle child)](capi-native-node-h.md#oh_arkui_nativemodule_adoptchild) | - | 当前节点接纳目标节点为附属节点。被接纳的节点不能已有父节点。调用该接口实际上不会将其添加为子节点，而是仅允许其接收对应子节点的生命周期回调。 |
| [int32\_t OH\_ArkUI\_NativeModule\_RemoveAdoptedChild(ArkUI\_NodeHandle node, ArkUI\_NodeHandle child)](capi-native-node-h.md#oh_arkui_nativemodule_removeadoptedchild) | - | 移除被接纳的目标附属节点。 |
| [int32\_t OH\_ArkUI\_NativeModule\_IsInRenderState(ArkUI\_NodeHandle node, bool\* isInRenderState)](capi-native-node-h.md#oh_arkui_nativemodule_isinrenderstate) | - | 获取节点是否处于渲染状态，如果一个节点的对应RenderNode在渲染树上，则处于渲染状态。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption(ArkUI\_NodeHandle node, ArkUI\_CrossLanguageOption\* option)](capi-native-node-h.md#oh_arkui_nodeutils_setcrosslanguageoption) | - | 设置目标节点跨语言设置属性的能力。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption(ArkUI\_NodeHandle node, ArkUI\_CrossLanguageOption\* option)](capi-native-node-h.md#oh_arkui_nodeutils_getcrosslanguageoption) | - | 获取目标节点跨语言设置属性的配置项。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand(ArkUI\_NodeHandle node, uint32\_t\* index)](capi-native-node-h.md#oh_arkui_nodeutils_getfirstchildindexwithoutexpand) | - | 获取目标节点在树上的第一个子节点的下标。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand(ArkUI\_NodeHandle node, uint32\_t\* index)](capi-native-node-h.md#oh_arkui_nodeutils_getlastchildindexwithoutexpand) | - | 获取目标节点在树上的最后一个子节点的下标。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode(ArkUI\_NodeHandle node, int32\_t position,ArkUI\_NodeHandle\* subnode, uint32\_t expandMode)](capi-native-node-h.md#oh_arkui_nodeutils_getchildwithexpandmode) | - | 用不同的展开模式获取对应下标的子节点。 |
| [int32\_t OH\_ArkUI\_NodeUtils\_GetPositionToParent(ArkUI\_NodeHandle node, ArkUI\_IntOffset\* globalOffset)](capi-native-node-h.md#oh_arkui_nodeutils_getpositiontoparent) | - | 获取目标节点相对于父节点的偏移值，单位：px。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_AddSupportedUIStates(ArkUI\_NodeHandle node, int32\_t uiStates,void (statesChangeHandler)(int32\_t currentStates, void\* userData), bool excludeInner, void\* userData)](capi-native-node-h.md#oh_arkui_addsupporteduistates) | - | 设置组件支持的[多态样式](ts-universal-attributes-polymorphic-style.md)状态。为了更高效地处理，需传入所关注的状态值及对应的状态处理函数，当关注的状态发生时，处理函数会被执行。可在回调中根据当前状态调整UI样式。当在同一个节点上多次调用该方法时，将以最后一次传入的状态及处理函数为准。有些类型的组件节点，系统内部已有对某些状态的默认处理。例如，Button组件默认具备对PRESSED状态的样式变化，当在此类组件上使用此方法自定义状态处理时，会先应用系统默认样式变化，再执行自定义的样式处理，最终效果为两者叠加。可以通过指定excludeInner为true来禁用系统内部的默认样式效果，但这通常取决于系统内部实现规范是否允许。当调用该函数时，传入的statesChangeHandler函数会立即执行一次，且无需特意注册对NORMAL状态的监听，只要注册了非NORMAL状态，当状态从任意状态变化回NORMAL时，系统都会进行回调，以便应用进行样式复原。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_RemoveSupportedUIStates(ArkUI\_NodeHandle node, int32\_t uiStates)](capi-native-node-h.md#oh_arkui_removesupporteduistates) | - | 删除注册的状态处理。当通过OH\_ArkUI\_AddSupportedUIStates注册的状态都被删除时，所注册的stateChangeHandler也不会再被执行。 |
| [int32\_t OH\_ArkUI\_RunTaskInScope(ArkUI\_ContextHandle uiContext, void\* userData, void(\*callback)(void\* userData))](capi-native-node-h.md#oh_arkui_runtaskinscope) | - | 在目标UI上下文中执行传入的自定义回调函数。示例请参考：[在NDK中保证多实例场景功能正常](../harmonyos-guides/ndk-scope-task.md)。 |
| [int32\_t OH\_ArkUI\_PostAsyncUITask(ArkUI\_ContextHandle context, void\* asyncUITaskData, void (\*asyncUITask)(void\* asyncUITaskData), void (\*onFinish)(void\* asyncUITaskData))](capi-native-node-h.md#oh_arkui_postasyncuitask) | - | 将asyncUITask函数提交至ArkUI框架提供的非UI线程中执行，asyncUITask函数执行完毕后，在UI线程调用onFinish函数。适用于多线程创建UI组件的场景，开发者可使用此接口在非UI线程创建UI组件，随后在UI线程将创建完成的组件挂载至主树上。 |
| [int32\_t OH\_ArkUI\_PostUITask(ArkUI\_ContextHandle context, void\* taskData, void (\*task)(void\* taskData))](capi-native-node-h.md#oh_arkui_postuitask) | - | 将task函数提交至UI线程中执行。适用于多线程创建UI组件的场景，当开发者在自建的线程中创建UI组件时，可以使用此接口将创建完成的组件挂载到UI线程的主树上。 |
| [int32\_t OH\_ArkUI\_PostUITaskAndWait(ArkUI\_ContextHandle context, void\* taskData, void (\*task)(void\* taskData))](capi-native-node-h.md#oh_arkui_postuitaskandwait) | - | 将task函数提交至UI线程中执行，调用此接口的线程将阻塞，直至task函数执行完成。在UI线程调用此接口等同于同步调用task函数。适用于多线程创建UI组件的场景，当开发者在多线程创建组件过程中需要调用仅支持UI线程的函数时，使用此接口返回UI线程调用函数，调用完成后继续多线程创建组件。当UI线程负载较高时，调用此接口的非UI线程可能长时间阻塞，影响多线程创建UI组件的性能，不建议频繁使用。 |
| [int32\_t OH\_ArkUI\_NativeModule\_RegisterCommonEvent(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType, void\* userData, void (callback)(ArkUI\_NodeEvent event))](capi-native-node-h.md#oh_arkui_nativemodule_registercommonevent) | - | 注册目标节点的基础事件回调。 |
| [int32\_t OH\_ArkUI\_NativeModule\_UnregisterCommonEvent(ArkUI\_NodeHandle node, ArkUI\_NodeEventType eventType)](capi-native-node-h.md#oh_arkui_nativemodule_unregistercommonevent) | - | 注销目标节点的基础事件回调。 |
| [int32\_t OH\_ArkUI\_NativeModule\_RegisterCommonVisibleAreaApproximateChangeEvent(ArkUI\_NodeHandle node, float\* ratios, int32\_t size, float expectedUpdateInterval, void\* userData, void (callback)(ArkUI\_NodeEvent event))](capi-native-node-h.md#oh_arkui_nativemodule_registercommonvisibleareaapproximatechangeevent) | - | 注册限制回调间隔的可见区域变化的基础事件回调。 |
| [int32\_t OH\_ArkUI\_NativeModule\_UnregisterCommonVisibleAreaApproximateChangeEvent(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_nativemodule_unregistercommonvisibleareaapproximatechangeevent) | - | 注销限制回调间隔的可见区域变化的基础事件回调。 |
| [int32\_t OH\_ArkUI\_Swiper\_FinishAnimation(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_swiper_finishanimation) | - | 停止指定的Swiper节点正在执行的翻页动画。 |
| [int32\_t OH\_ArkUI\_SetForceDarkConfig(ArkUI\_ContextHandle uiContext, bool forceDark, ArkUI\_NodeType nodeType, uint32\_t (\*colorInvertFunc)(uint32\_t color))](capi-native-node-h.md#oh_arkui_setforcedarkconfig) | - | 为组件和实例设置反色算法。 |
| [ArkUI\_TouchTestInfo\* OH\_ArkUI\_NodeEvent\_GetTouchTestInfo(ArkUI\_NodeEvent\* nodeEvent)](capi-native-node-h.md#oh_arkui_nodeevent_gettouchtestinfo) | - | 获取组件事件中的触摸测试信息。 |
| [int32\_t OH\_ArkUI\_NativeModule\_ConvertPositionToWindow(ArkUI\_NodeHandle currentNode, ArkUI\_IntOffset localPosition, ArkUI\_IntOffset\* windowPosition)](capi-native-node-h.md#oh_arkui_nativemodule_convertpositiontowindow) | - | 将点的坐标从目标节点的坐标系转换至当前窗口的坐标系。 |
| [int32\_t OH\_ArkUI\_NativeModule\_ConvertPositionFromWindow(ArkUI\_NodeHandle targetNode, ArkUI\_IntOffset windowPosition, ArkUI\_IntOffset\* localPosition)](capi-native-node-h.md#oh_arkui_nativemodule_convertpositionfromwindow) | - | 将点的坐标从当前窗口的坐标系转换至目标节点的坐标系。 |
| [int32\_t OH\_ArkUI\_Swiper\_StartFakeDrag(ArkUI\_NodeHandle node, bool\* isSuccessful)](capi-native-node-h.md#oh_arkui_swiper_startfakedrag) | - | 启动Swiper节点的模拟拖拽操作。调用[OH\_ArkUI\_Swiper\_FakeDragBy](capi-native-node-h.md#oh_arkui_swiper_fakedragby)模拟拖拽动作。调用[OH\_ArkUI\_Swiper\_StopFakeDrag](capi-native-node-h.md#oh_arkui_swiper_stopfakedrag)停止模拟拖拽。  模拟拖拽操作可以被真实拖拽操作打断。如果需要在模拟拖拽期间忽略用户的拖拽事件，请使用[NODE\_SWIPER\_DISABLE\_SWIPE](capi-native-node-h.md#arkui_nodeattributetype)。 |
| [int32\_t OH\_ArkUI\_Swiper\_FakeDragBy(ArkUI\_NodeHandle node, float offset, bool\* isConsumedOffset)](capi-native-node-h.md#oh_arkui_swiper_fakedragby) | - | 通过设置Swiper节点的偏移量模拟拖拽效果。该接口调用前，必须先调用[OH\_ArkUI\_Swiper\_StartFakeDrag](capi-native-node-h.md#oh_arkui_swiper_startfakedrag)启动模拟拖拽。 |
| [int32\_t OH\_ArkUI\_Swiper\_StopFakeDrag(ArkUI\_NodeHandle node, bool\* isSuccessful)](capi-native-node-h.md#oh_arkui_swiper_stopfakedrag) | - | 停止对Swiper节点的模拟拖拽。 |
| [int32\_t OH\_ArkUI\_Swiper\_IsFakeDragging(ArkUI\_NodeHandle node, bool\* isFakeDragging)](capi-native-node-h.md#oh_arkui_swiper_isfakedragging) | - | 获取Swiper节点的模拟拖拽状态。 |
| [int32\_t OH\_ArkUI\_Swiper\_ShowPrevious(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_swiper_showprevious) | - | 显示Swiper节点的上一页。 |
| [int32\_t OH\_ArkUI\_Swiper\_ShowNext(ArkUI\_NodeHandle node)](capi-native-node-h.md#oh_arkui_swiper_shownext) | - | 显示Swiper节点的下一页。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| MAX\_NODE\_SCOPE\_NUM 1000 | 定义组件最大方法数量。 |
| MAX\_COMPONENT\_EVENT\_ARG\_NUM 12 | 定义组件事件最大参数数量。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_NodeType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeType
```

**描述：**

提供ArkUI在Native侧可创建组件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NODE\_CUSTOM = 0 | 自定义节点。 |
| ARKUI\_NODE\_TEXT = 1 | 文本。 |
| ARKUI\_NODE\_SPAN = 2 | 文本段落。 |
| ARKUI\_NODE\_IMAGE\_SPAN = 3 | 文本图片段落。 |
| ARKUI\_NODE\_IMAGE = 4 | 图片。 |
| ARKUI\_NODE\_TOGGLE = 5 | 状态开关。 |
| ARKUI\_NODE\_LOADING\_PROGRESS = 6 | 等待图标。 |
| ARKUI\_NODE\_TEXT\_INPUT = 7 | 单行文本输入。 |
| ARKUI\_NODE\_TEXT\_AREA = 8 | 多行文本。 |
| ARKUI\_NODE\_BUTTON = 9 | 按钮。 |
| ARKUI\_NODE\_PROGRESS = 10 | 进度条。 |
| ARKUI\_NODE\_CHECKBOX = 11 | 复选框。 |
| ARKUI\_NODE\_XCOMPONENT = 12 | SURFACE类型XComponent。 |
| ARKUI\_NODE\_DATE\_PICKER = 13 | 日期选择器组件。 |
| ARKUI\_NODE\_TIME\_PICKER = 14 | 时间选择组件。 |
| ARKUI\_NODE\_TEXT\_PICKER = 15 | 滑动选择文本内容的组件。 |
| ARKUI\_NODE\_CALENDAR\_PICKER = 16 | 日历选择器组件。 |
| ARKUI\_NODE\_SLIDER = 17 | 滑动条组件。 |
| ARKUI\_NODE\_RADIO = 18 | 单选框。 |
| ARKUI\_NODE\_IMAGE\_ANIMATOR = 19 | 帧动画组件。 |
| ARKUI\_NODE\_XCOMPONENT\_TEXTURE | TEXTURE类型XComponent。  **起始版本：** 18 |
| ARKUI\_NODE\_CHECKBOX\_GROUP = 21 | 复选框组。  **起始版本：** 15 |
| ARKUI\_NODE\_STACK = MAX\_NODE\_SCOPE\_NUM | 堆叠容器。 |
| ARKUI\_NODE\_SWIPER = 1001 | 翻页容器。 |
| ARKUI\_NODE\_SCROLL = 1002 | 滚动容器。 |
| ARKUI\_NODE\_LIST = 1003 | 列表。 |
| ARKUI\_NODE\_LIST\_ITEM = 1004 | 列表项。 |
| ARKUI\_NODE\_LIST\_ITEM\_GROUP = 1005 | 列表item分组。 |
| ARKUI\_NODE\_COLUMN = 1006 | 垂直布局容器。 |
| ARKUI\_NODE\_ROW = 1007 | 水平布局容器。 |
| ARKUI\_NODE\_FLEX = 1008 | 弹性布局容器。 |
| ARKUI\_NODE\_REFRESH = 1009 | 刷新组件。 |
| ARKUI\_NODE\_WATER\_FLOW = 1010 | 瀑布流容器。 |
| ARKUI\_NODE\_FLOW\_ITEM = 1011 | 瀑布流子组件。 |
| ARKUI\_NODE\_RELATIVE\_CONTAINER = 1012 | 相对布局组件。 |
| ARKUI\_NODE\_GRID = 1013 | 网格容器。 |
| ARKUI\_NODE\_GRID\_ITEM = 1014 | 网格子组件。 |
| ARKUI\_NODE\_CUSTOM\_SPAN = 1015 | 自定义文本段落。 |
| ARKUI\_NODE\_EMBEDDED\_COMPONENT = 1016 | 同应用进程嵌入式组件。  **起始版本：** 20 |
| ARKUI\_NODE\_UNDEFINED = 1017 | 组件类型未定义。在反色接口中代表全部组件类型。  **起始版本：** 20 |
| ARKUI\_NODE\_PICKER = 1018 | Picker容器，用于实现用户选择操作的组件。  **起始版本：** 23 |

### ArkUI\_NodeAttributeType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeAttributeType
```

**描述：**

定义ArkUI在Native侧可以设置的属性样式集合。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NODE\_WIDTH = 0 | 宽度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：宽度数值，单位为vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：宽度数值，单位为vp； |
| NODE\_HEIGHT = 1 | 高度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：高度数值，单位为vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：高度数值，单位为vp； |
| NODE\_BACKGROUND\_COLOR = 2 | 背景色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式，形如 0xFFFF0000 表示红色；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式，形如 0xFFFF0000 表示红色； |
| NODE\_BACKGROUND\_IMAGE = 3 | 背景色图片属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 图片地址。API version 22及之前版本，支持网络图片资源地址、本地图片资源地址、Base64和[PixelMap](arkts-apis-image-pixelmap.md)资源，不支持[svg](js-components-svg.md)图片、gif和webp等类型的动图。 从API version 23开始，新增支持webp和gif类型的动图，显示动图第一帧，不支持其他类型的动图。  .value[0]?.i32：可选值，repeat参数，参数类型[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)，默认值为ARKUI\_IMAGE\_REPEAT\_NONE；  .object：PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 图片地址。API version 22及之前版本，支持网络图片资源地址、本地图片资源地址、Base64和PixelMap资源，不支持svg图片、gif和webp等类型的动图。 从API version 23开始，新增支持webp和gif类型的动图，显示动图第一帧，不支持其他类型的动图。  .value[0].i32：repeat参数，参数类型[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)；  .object：PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置。 |
| NODE\_PADDING = 4 | 内间距属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式有两种：  1：上下左右四个位置的内间距值相等。  .value[0].f32：内间距数值，单位为vp；  2：分别指定上下左右四个位置的内间距值。  .value[0].f32：上内间距数值，单位为vp，默认值为0vp；  .value[1].f32：右内间距数值，单位为vp，默认值为0vp；  .value[2].f32：下内间距数值，单位为vp，默认值为0vp；  .value[3].f32：左内间距数值，单位为vp，默认值为0vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上内间距数值，单位为vp；  .value[1].f32：右内间距数值，单位为vp；  .value[2].f32：下内间距数值，单位为vp；  .value[3].f32：左内间距数值，单位为vp； |
| NODE\_ID = 5 | 组件ID属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: ID的内容；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: ID的内容； |
| NODE\_ENABLED = 6 | 设置组件是否可交互，支持属性设置，属性重置和属性获取。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示不可交互，true表示可交互；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：0表示不可交互，1表示可交互； |
| NODE\_MARGIN = 7 | 外间距属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式有两种：  1：上下左右四个位置的外间距值相等。  .value[0].f32：外间距数值，单位为vp；  2：分别指定上下左右四个位置的外间距值。  .value[0].f32：上外间距数值，单位为vp，默认值为0vp；  .value[1].f32：右外间距数值，单位为vp，默认值为0vp；  .value[2].f32：下外间距数值，单位为vp，默认值为0vp；  .value[3].f32：左外间距数值，单位为vp，默认值为0vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上外间距数值，单位为vp；  .value[1].f32：右外间距数值，单位为vp；  .value[2].f32：下外间距数值，单位为vp；  .value[3].f32：左外间距数值，单位为vp； |
| NODE\_TRANSLATE = 8 | 设置组件平移，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴移动距离，单位vp，默认值0；  .value[1].f32： y轴移动距离，单位vp，默认值0；  .value[2].f32： z轴移动距离，单位vp，默认值0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴移动距离，单位vp；  .value[1].f32： y轴移动距离，单位vp；  .value[2].f32： z轴移动距离，单位vp。 |
| NODE\_SCALE = 9 | 设置组件缩放，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴的缩放系数，默认值1；  .value[1].f32： y轴的缩放系数，默认值1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴的缩放系数；  .value[1].f32： y轴的缩放系数。 |
| NODE\_ROTATE = 10 | 设置组件旋转，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 旋转轴向量x坐标，默认值0；  .value[1].f32： 旋转轴向量y坐标，默认值0；  .value[2].f32： 旋转轴向量z坐标，默认值0；  .value[3].f32： 旋转角度，默认值0；  .value[4].f32： 视距，即视点到z=0平面的距离，单位vp，默认值0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 旋转轴向量x坐标；  .value[1].f32： 旋转轴向量y坐标；  .value[2].f32： 旋转轴向量z坐标；  .value[3].f32： 旋转角度；  .value[4].f32： 视距，即视点到z=0平面的距离，单位vp。 |
| NODE\_BRIGHTNESS = 11 | 设置组件高光效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 亮度值，默认值1.0，推荐取值范围[0, 2.0]。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 亮度值。 |
| NODE\_SATURATION = 12 | 设置组件饱和度效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 饱和度值，默认值1.0，推荐取值范围[0, 50.0)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 饱和度值。 |
| NODE\_BLUR = 13 | 设置组件内容模糊效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 模糊半径，模糊半径越大越模糊，为0时不模糊，小于0时按0处理且不会返回错误码。单位vp，默认值0.0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 模糊半径，模糊半径越大越模糊，为0时不模糊。单位vp。 |
| NODE\_LINEAR\_GRADIENT = 14 | 设置组件颜色渐变效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 线性渐变的起始角度，当[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle属性生效，否则按direction为主要布局方式。0点方向顺时针旋转为正向角度，默认值：180；  .value[1].i32：线性渐变的方向，设置除ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM的线性渐变方向后，angle不生效。数据类型[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)。  .value[2].i32： 为渐变的颜色重复着色，默认值 false。  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色。  stops：渐变位置。  size：颜色个数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 线性渐变的起始角度。当为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle为设置值，其他情况均为默认值。  .value[1].i32：线性渐变的方向。  .value[2].i32： 为渐变的颜色重复着色。  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色。  stops：渐变位置。  size：颜色个数。 |
| NODE\_ALIGNMENT = 15 | 设置组件内容在元素绘制区域内的对齐方式，支持属性设置，属性重置和属性获取接口。在Stack中该属性与NODE\_STACK\_ALIGN\_CONTENT效果一致，只能设置子组件在容器内的对齐方式。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 对齐方式，数据类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)，默认值ARKUI\_ALIGNMENT\_CENTER。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 对齐方式，数据类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。 |
| NODE\_OPACITY = 16 | 透明度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：透明度数值，默认值为1，取值范围为0到1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：透明度数值，取值范围为0到1。 |
| NODE\_BORDER\_WIDTH = 17 | 边框宽度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].f32：统一设置四条边的边框宽度。  2: .value[0].f32：设置上边框的边框宽度。  .value[1].f32：设置右边框的边框宽度。  .value[2].f32：设置下边框的边框宽度。  .value[3].f32：设置左边框的边框宽度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置上边框的边框宽度。  .value[1].f32：设置右边框的边框宽度。  .value[2].f32：设置下边框的边框宽度。  .value[3].f32：设置左边框的边框宽度。 |
| NODE\_BORDER\_RADIUS = 18 | 边框圆角属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].f32：统一设置四条边的边框圆角。  2: .value[0].f32：设置左上角圆角半径。  .value[1].f32：设置右上角圆角半径。  .value[2].f32：设置左下角圆角半径。  .value[3].f32：设置右下角圆角半径。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置左上角圆角半径。  .value[1].f32：设置右上角圆角半径。  .value[2].f32：设置左下角圆角半径。  .value[3].f32：设置右下角圆角半径。 |
| NODE\_BORDER\_COLOR = 19 | 边框颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].u32：统一设置四条边的边框颜色，使用0xargb表示，如0xFFFF11FF。  2: .value[0].u32：设置上侧边框颜色，使用0xargb表示，默认值为0xFF000000。  .value[1].u32：设置右侧边框颜色，使用0xargb表示，默认值为0xFF000000。  .value[2].u32：设置下侧边框颜色，使用0xargb表示，默认值为0xFF000000。  .value[3].u32：设置左侧边框颜色，使用0xargb表示，默认值为0xFF000000。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：设置上侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[1].u32：设置右侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[2].u32：设置下侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[3].u32：设置左侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| NODE\_BORDER\_STYLE = 20 | 边框线条样式属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].i32：统一设置四条边的边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。  2:.value[0].i32：设置上侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。  .value[1].i32：设置右侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。  .value[2].i32：设置下侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。  .value[3].i32：设置左侧边框线条样式，参数类型[ArkUI\_BorderStyle](capi-native-type-h.md#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：上侧边框线条样式对应的数值。  .value[1].i32：右侧边框线条样式对应的数值。  .value[2].i32：下侧边框线条样式对应的数值。  .value[3].i32：左侧边框线条样式对应的数值。 |
| NODE\_Z\_INDEX = 21 | 组件的堆叠顺序属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：堆叠顺序数值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：堆叠顺序数值。 |
| NODE\_VISIBILITY = 22 | 组件是否可见属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制当前组件显示或隐藏，参数类型[ArkUI\_Visibility](capi-native-type-h.md#arkui_visibility)，默认值为ARKUI\_VISIBILITY\_VISIBLE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制当前组件显示或隐藏，参数类型[ArkUI\_Visibility](capi-native-type-h.md#arkui_visibility)，默认值为ARKUI\_VISIBILITY\_VISIBLE。 |
| NODE\_CLIP = 23 | 组件进行裁剪、遮罩处理属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制是否对子组件超出当前组件范围外的区域进行裁剪，0表示不裁切，1表示裁切。默认为不裁切。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制是否对子组件超出当前组件范围外的区域进行裁剪，0表示不裁切，1表示裁切。 |
| NODE\_CLIP\_SHAPE = 24 | 组件上指定形状的裁剪，支持属性设置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式，共有4种类型：  1.rect类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_RECTANGLE；  .value[1].f32：矩形宽度，单位为vp；  .value[2].f32：矩形高度，单位为vp；  .value[3].f32：矩形圆角宽度，单位为vp；  .value[4].f32：矩形圆角高度，单位为vp；  .value[5]?.f32：矩形形状的左上圆角半径，单位为vp；  .value[6]?.f32：矩形形状的左下圆角半径，单位为vp；  .value[7]?.f32：矩形形状的右上圆角半径，单位为vp；  .value[8]?.f32：矩形形状的右下圆角半径，单位为vp；  .object：参数类型为[ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)，矩形形状的坐标偏移量，在仅传入.object参数时生效；  2.circle类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_CIRCLE；  .value[1].f32：圆形宽度，单位为vp；  .value[2].f32：圆形高度，单位为vp；  .object：参数类型为[ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)，圆形坐标偏移量，在仅传入.object参数时生效；  3.ellipse类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_ELLIPSE；  .value[1].f32：椭圆形宽度，单位为vp；  .value[2].f32：椭圆形高度，单位为vp；  .object：参数类型为[ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)，椭圆形坐标偏移量，在仅传入.object参数时生效；  4.path类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_PATH；  .value[1].f32：路径宽度，单位为vp；  .value[2].f32：路径高度，单位为vp；  .string：路径绘制的命令字符串；  .object：参数类型为[ArkUI\_RenderNodeClipOption](capi-arkui-nativemodule-arkui-rendernodeclipoption.md)，路径绘制的命令，在仅传入.object参数时生效；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式，共有4种类型：  1.rect类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_RECTANGLE；  .value[1].f32：矩形宽度，单位为vp；  .value[2].f32：矩形高度，单位为vp；  .value[3].f32：矩形圆角宽度，单位为vp；  .value[4].f32：矩形圆角高度，单位为vp；  .value[5]?.f32：矩形形状的左上圆角半径，单位为vp；  .value[6]?.f32：矩形形状的左下圆角半径，单位为vp；  .value[7]?.f32：矩形形状的右上圆角半径，单位为vp；  .value[8]?.f32：矩形形状的右下圆角半径，单位为vp；  .value[9]?.f32：矩形形状的横坐标偏移，单位为vp；  .value[10]?.f32：矩形形状的纵坐标偏移，单位为vp；  2.circle类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_CIRCLE；  .value[1].f32：圆形宽度，单位为vp；  .value[2].f32：圆形高度，单位为vp；  .value[3]?.f32：圆形横坐标偏移，单位为vp；  .value[4]?.f32：圆形纵坐标偏移，单位为vp；  3.ellipse类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_ELLIPSE；  .value[1].f32：椭圆形宽度，单位为vp；  .value[2].f32：椭圆形高度，单位为vp；  .value[3]?.f32：椭圆形横坐标偏移，单位为vp；  .value[4]?.f32：椭圆形纵坐标偏移，单位为vp；  4.path类型：  .value[0].i32：裁剪类型，参数类型[ArkUI\_ClipType](capi-native-type-h.md#arkui_cliptype)，ARKUI\_CLIP\_TYPE\_PATH；  .value[1].f32：路径宽度，单位为vp；  .value[2].f32：路径高度，单位为vp；  .string：路径绘制的命令字符串； |
| NODE\_TRANSFORM = 25 | 矩阵变换功能，可对图形进行平移、旋转和缩放等，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0...15].f32: 16个浮点数字。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0...15].f32: 16个浮点数字。 |
| NODE\_HIT\_TEST\_BEHAVIOR = 26 | 触摸测试类型，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制当前组件的触摸测试类型，参数类型[ArkUI\_HitTestMode](capi-native-type-h.md#arkui_hittestmode)，默认值为ARKUI\_HIT\_TEST\_MODE\_DEFAULT。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制当前组件的触摸测试类型，参数类型ArkUI\_HitTestMode，默认值为ARKUI\_HIT\_TEST\_MODE\_DEFAULT。 |
| NODE\_POSITION = 27 | 元素左上角相对于父容器左上角偏移位置，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：x轴坐标。  .value[1].f32: y轴坐标。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：x轴坐标。  .value[1].f32: y轴坐标。 |
| NODE\_SHADOW = 28 | 阴影效果属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置当前组件阴影效果，参数类型[ArkUI\_ShadowStyle](capi-native-type-h.md#arkui_shadowstyle)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置当前组件阴影效果，参数类型[ArkUI\_ShadowStyle](capi-native-type-h.md#arkui_shadowstyle)。 |
| NODE\_CUSTOM\_SHADOW = 29 | 自定义阴影效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32：阴影模糊半径，单位为px；  .value[1]?.i32：是否开启智能取色，0代表不开启，1代表开启，默认不开启；  .value[2]?.f32：阴影X轴偏移量，单位为px；  .value[3]?.f32：阴影Y轴偏移量，单位为px；  .value[4]?.i32：阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)，默认值为ARKUI\_SHADOW\_TYPE\_COLOR；  .value[5]?.u32：阴影颜色，0xargb格式，形如 0xFFFF0000 表示红色；  .value[6]?.u32：阴影是否内部填充，0表示不填充，1表示填充。    属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：阴影模糊半径，单位为px；  .value[1].i32：是否开启智能取色；  .value[2].f32：阴影X轴偏移量，单位为px；  .value[3].f32：阴影Y轴偏移量，单位为px；  .value[4].i32：阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)，默认值为ARKUI\_SHADOW\_TYPE\_COLOR；  .value[5].u32：阴影颜色，0xargb格式，形如 0xFFFF0000 表示红色；  .value[6].u32：阴影是否内部填充，0表示不填充，1表示填充； |
| NODE\_BACKGROUND\_IMAGE\_SIZE = 30 | 背景图片的宽高属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示图片的宽度值，取值范围[0,+∞)，单位为vp。  .value[1].f32 表示图片的高度值，取值范围[0,+∞)，单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示图片的宽度值，单位为vp。  .value[1].f32 表示图片的高度值，单位为vp。 |
| NODE\_BACKGROUND\_IMAGE\_SIZE\_WITH\_STYLE = 31 | 背景图片的宽高样式属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示背景图片的宽高样式，取[ArkUI\_ImageSize](capi-native-type-h.md#arkui_imagesize)枚举值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示背景图片的宽高样式，取[ArkUI\_ImageSize](capi-native-type-h.md#arkui_imagesize)枚举值。 |
| NODE\_BACKGROUND\_BLUR\_STYLE = 32 | 背景和内容之间的模糊属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示模糊类型，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。  .value[1]?.i32 表示深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。  .value[2]?.i32 表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[3]?.f32 表示模糊效果程度，取[0.0,1.0]范围内的值。  .value[4]?.f32 表示灰阶模糊起始边界。  .value[5]?.f32 表示灰阶模糊终点边界。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示模糊类型，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。  .value[1].i32 表示深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。  .value[2].i32 表示取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[3].f32 表示模糊效果程度，取[0.0,1.0]范围内的值。  .value[4].f32 表示灰阶模糊起始边界。  .value[5].f32 表示灰阶模糊终点边界。 |
| NODE\_TRANSFORM\_CENTER = 33 | 图形变换和转场的中心点属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32 表示中心点X轴坐标值，单位为vp。  .value[1]?.f32 表示中心点Y轴坐标，单位为vp。  .value[2]?.f32 表示中心点Z轴坐标，单位为vp。  .value[3]?.f32 表示中心点X轴坐标的百分比位置，如0.2表示百分之20的位置，该属性覆盖value[0].f32，默认值:0.5f。  .value[4]?.f32 表示中心点Y轴坐标的百分比位置，如0.2表示百分之20的位置，该属性覆盖value[1].f32，默认值:0.5f。  .value[5]?.f32 表示中心点Z轴坐标的百分比位置，如0.2表示百分之20的位置，该属性覆盖value[2].f32，默认值:0.0f。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示中心点X轴坐标，单位为vp。  .value[1].f32 表示中心点Y轴坐标，单位为vp。  .value[2].f32 表示中心点Z轴坐标，单位为vp。  注：如果设置坐标百分比位置，属性获取方法返回计算后的vp为单位的值。 |
| NODE\_OPACITY\_TRANSITION = 34 | 转场时的透明度效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示起终点的透明度值。  .value[1].i32 表示动画时长，单位ms。  .value[2].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[3]?.i32 表示动画延迟时长，单位ms。  .value[4]?.i32 表示动画播放次数。  .value[5]?.i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[6]?.f32 表示动画播放速度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示起终点的透明度值。  .value[1].i32 表示动画时长，单位ms。  .value[2].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[3].i32 表示动画延迟时长，单位ms。  .value[4].i32 表示动画播放次数。  .value[5].i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[6].f32 表示动画播放速度。 |
| NODE\_ROTATE\_TRANSITION = 35 | 转场时的旋转效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示横向旋转分量。  .value[1].f32 表示纵向的旋转分量。  .value[2].f32 表示竖向的旋转分量。  .value[3].f32 表示角度。  .value[4].f32 表示视距，默认值：0.0f。  .value[5].i32 表示动画时长，单位ms。  .value[6].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[7]?.i32 表示动画延迟时长，单位ms。  .value[8]?.i32 表示动画播放次数。  .value[9]?.i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[10]?.f32 表示动画播放速度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示横向旋转分量。  .value[1].f32 表示纵向的旋转分量。  .value[2].f32 表示竖向的旋转分量。  .value[3].f32 表示角度。  .value[4].f32 表示视距。  .value[5].i32 表示动画时长，单位ms。  .value[6].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[7].i32 表示动画延迟时长，单位ms。  .value[8].i32 表示动画播放次数。  .value[9].i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[10].f32 表示动画播放速度。 |
| NODE\_SCALE\_TRANSITION = 36 | 转场时的缩放效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 横向放大倍数。  .value[1].f32 纵向放大倍数。  .value[2].f32 竖向放大倍数。  .value[3].i32 表示动画时长，单位ms。  .value[4].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[5]?.i32 表示动画延迟时长，单位ms。  .value[6]?.i32 表示动画播放次数。  .value[7]?.i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[8]?.f32 表示动画播放速度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 横向放大倍数。  .value[1].f32 纵向放大倍数。  .value[2].f32 竖向放大倍数。  .value[3].i32 表示动画时长，单位ms。  .value[4].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[5].i32 表示动画延迟时长，单位ms。  .value[6].i32 表示动画播放次数。  .value[7].i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[8].f32 表示动画播放速度。 |
| NODE\_TRANSLATE\_TRANSITION = 37 | 转场时的平移效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32 表示横向平移距离值，单位为vp。默认值为0.0vp。  value[1].f32 表示纵向平移距离值，单位为vp。默认值为0.0vp。  value[2].f32 表示竖向平移距离值，单位为vp。默认值为0.0vp。  value[3].i32 表示动画时长，单位ms。  value[4].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  value[5]?.i32 表示动画延迟时长，单位ms。  value[6]?.i32 表示动画播放次数。  value[7]?.i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  value[8]?.f32 表示动画播放速度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32 表示横向平移距离值，单位为vp。  value[1].f32 表示纵向平移距离值，单位为vp。  value[2].f32 表示竖向平移距离值，单位为vp。  value[3].i32 表示动画时长，单位ms。  value[4].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  value[5].i32 表示动画延迟时长，单位ms。  value[6].i32 表示动画播放次数。  value[7].i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  value[8].f32 表示动画播放速度。 |
| NODE\_MOVE\_TRANSITION = 38 | 转场时从屏幕边缘滑入和滑出的效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 参数类型[ArkUI\_TransitionEdge](capi-native-type-h.md#arkui_transitionedge)。  .value[1].i32 表示动画时长，单位ms。  .value[2].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[3]?.i32 表示动画延迟时长，单位ms。  .value[4]?.i32 表示动画播放次数。  .value[5]?.i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[6]?.f32 表示动画播放速度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 参数类型[ArkUI\_TransitionEdge](capi-native-type-h.md#arkui_transitionedge)。  .value[1].i32 表示动画时长，单位ms。  .value[2].i32 表示动画曲线类型，取[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)枚举值。  .value[3].i32 表示动画延迟时长，单位ms。  .value[4].i32 表示动画播放次数。  .value[5].i32 表示动画播放模式，取[ArkUI\_AnimationPlayMode](capi-native-type-h.md#arkui_animationplaymode)枚举值。  .value[6].f32 表示动画播放速度。 |
| NODE\_FOCUSABLE = 39 | 获焦属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型为1表示可获焦，为0表示不可获焦。默认为不可获焦。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1表示可获焦，为0表示不可获焦。 |
| NODE\_DEFAULT\_FOCUS = 40 | 默认焦点属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  value[0].i32：参数类型为1表示是默认焦点，为0表示不是默认焦点。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].i32：参数类型为1表示是默认焦点，为0表示不是默认焦点。 |
| NODE\_RESPONSE\_REGION = 41 | 触摸热区属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .data[0].f32：触摸点相对于组件左上角的x轴坐标,单位为vp。  .data[1].f32：触摸点相对于组件左上角的y轴坐标,单位为vp。  .data[2].f32：触摸热区的宽度 ，单位为百分比。  .data[3].f32：触摸热区的高度，单位为百分比。  .data[4...].f32:可以设置多个手势响应区域，顺序和上述一致。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .data[0].f32：触摸点相对于组件左上角的x轴坐标,单位为vp。  .data[1].f32：触摸点相对于组件左上角的y轴坐标,单位为vp。  .data[2].f32：触摸热区的宽度，单位为百分比。  .data[3].f32：触摸热区的高度，单位为百分比。  .data[4...].f32:可以设置多个手势响应区域，顺序和上述一致。  **说明：** 设置时data数据大小无数量限制，均可以设置成功，但仅支持获取到前20个。 |
| NODE\_OVERLAY = 42 | 定义遮罩属性，支持属性设置，属性重置和属性获取。开发者可以通过如下.string或.object设置浮层内容，.string有更高的优先级。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string：遮罩文本；  .value[0]?.i32：可选值，浮层相对于组件的位置，参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)，默认值为ARKUI\_ALIGNMENT\_TOP\_START。  .value[1]?.f32：可选值，浮层基于自身左上角的偏移量X，单位为vp，默认值为0vp。  .value[2]?.f32：可选值，浮层基于自身左上角的偏移量Y，单位为vp，默认值为0vp。  .value[3]?.i32：可选值，浮层的布局方向，参数类型[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)，默认值为ARKUI\_DIRECTION\_LTR。  在大部分场景下，这个参数都应该被设置成Auto，这个模式允许系统自动处理布局方向，如果在某些场景下需要保持特定的方向，设置这个属性为LTR（Left-to-Right）或者RTL（Right-to-Left）。从API version 21开始支持。  .object：用于overlay的节点树，参数类型为[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)，默认值为nullptr。从API version 21开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：遮罩文本；  .value[0].i32：浮层相对于组件的位置，参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)，默认值为ARKUI\_ALIGNMENT\_TOP\_START。  .value[1].f32：浮层基于自身左上角的偏移量X，单位为vp。  .value[2].f32：浮层基于自身左上角的偏移量Y，单位为vp。  .value[3].i32：浮层的布局方向，参数类型[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)，默认值为ARKUI\_DIRECTION\_LTR。从API version 21开始支持。  .object：用于overlay的节点树，参数类型为[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。从API version 21开始支持。 |
| NODE\_SWEEP\_GRADIENT = 43 | 角度渐变效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32:为角度渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。  .value[1]?.f32:为角度渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。  .value[2]?.f32:角度渐变的起点，默认值0。  .value[3]?.f32:角度渐变的终点，默认值0。  .value[4]?.f32:角度渐变的旋转角度，默认值0。  .value[5]?.i32:为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色。  stops：渐变位置。  size：颜色个数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32:为角度渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。  .value[1].f32:为角度渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。  .value[2].f32:角度渐变的起点，默认值0。  .value[3].f32:角度渐变的终点，默认值0。  .value[4].f32:角度渐变的旋转角度，默认值0。  .value[5].i32:为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色。  stops：渐变位置。  size：颜色个数。 |
| NODE\_RADIAL\_GRADIENT = 44 | 径向渐变渐变效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32:为径向渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。  .value[1]?.f32:为径向渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。  .value[2]?.f32:径向渐变的半径，默认值0。  .value[3]?.i32:为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色。  stops：渐变位置。  size：颜色个数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32:为径向渐变的中心点，即相对于当前组件左上角的坐标,X轴坐标。  .value[1].f32:为径向渐变的中心点，即相对于当前组件左上角的坐标,Y轴坐标。  .value[2].f32:径向渐变的半径，默认值0。  .value[3].i32:为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色。  stops：渐变位置。  size：颜色个数。 |
| NODE\_MASK = 45 | 组件上加上指定形状的遮罩，支持属性设置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式,共有5种类型：  1.rect类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_RECTANGLE；  .value[4].f32：矩形宽度，单位为vp；  .value[5].f32：矩形高度，单位为vp；  .value[6].f32：矩形圆角宽度，单位为vp；  .value[7].f32：矩形圆角高度，单位为vp；  .value[8]?.f32：矩形形状的左上圆角半径，单位为vp；  .value[9]?.f32：矩形形状的左下圆角半径，单位为vp；  .value[10]?.f32：矩形形状的右上圆角半径，单位为vp；  .value[11]?.f32：矩形形状的右下圆角半径，单位为vp；  2.circle类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_CIRCLE；  .value[4].f32：圆形宽度，单位为vp；  .value[5].f32：圆形高度，单位为vp；  3.ellipse类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_ELLIPSE；  .value[4].f32：椭圆形宽度，单位为vp；  .value[5].f32：椭圆形高度，单位为vp；  4.path类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_PATH；  .value[4].f32：路径宽度，单位为vp；  .value[5].f32：路径高度，单位为vp；  .string：路径绘制的命令字符串；  5.progress类型：  .value[0].i32：遮罩类型，参数类型[ArkUI\_MaskType](capi-native-type-h.md#arkui_masktype)，遮罩类型枚举值为ARKUI\_MASK\_TYPE\_PROGRESS；  .value[1].f32：进度遮罩的当前值；  .value[2].f32：进度遮罩的最大值；  .value[3].u32：进度遮罩的颜色；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式,共有5种类型：  1.rect类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：矩形宽度，单位为vp；  .value[5].f32：矩形高度，单位为vp；  .value[6].f32：矩形圆角宽度，单位为vp；  .value[7].f32：矩形圆角高度，单位为vp；  .value[8]?.f32：矩形形状的左上圆角半径，单位为vp；  .value[9]?.f32：矩形形状的左下圆角半径，单位为vp；  .value[10]?.f32：矩形形状的右上圆角半径，单位为vp；  .value[11]?.f32：矩形形状的右下圆角半径，单位为vp；  2.circle类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：圆形宽度，单位为vp；  .value[5].f32：圆形高度，单位为vp；  3.ellipse类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：椭圆形宽度，单位为vp；  .value[5].f32：椭圆形高度，单位为vp；  4.path类型：  .value[0].u32：填充颜色，0xargb类型；  .value[1].u32：描边颜色，0xargb类型；  .value[2].f32：描边宽度，单位为vp；  .value[3].i32：遮罩类型；  .value[4].f32：路径宽度，单位为vp；  .value[5].f32：路径高度，单位为vp；  .string：路径绘制的命令字符串；  5.progress类型：  .value[0].i32：遮罩类型；  .value[1].f32：进度遮罩的当前值；  .value[2].f32：进度遮罩的最大值；  .value[3].u32：进度遮罩的颜色； |
| NODE\_BLEND\_MODE = 46 | 当前控件背景与子节点内容进行混合，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制当前组件的混合模式类型，参数类型[ArkUI\_BlendMode](capi-native-type-h.md#arkui_blendmode)，默认值为ARKUI\_BLEND\_MODE\_NONE。  .value[1].?i32：blendMode实现方式是否离屏，参数类型[ArkUI\_BlendApplyType](capi-native-type-h.md#arkui_blendapplytype)，默认值为BLEND\_APPLY\_TYPE\_FAST。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制当前组件的混合模式类型，参数类型[ArkUI\_BlendMode](capi-native-type-h.md#arkui_blendmode)，默认值为ARKUI\_BLEND\_MODE\_NONE。  .value[1].i32：blendMode实现方式是否离屏，参数类型[ArkUI\_BlendApplyType](capi-native-type-h.md#arkui_blendapplytype)，默认值为BLEND\_APPLY\_TYPE\_FAST。 |
| NODE\_DIRECTION = 47 | 设置容器元素内主轴方向上的布局，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置容器元素内主轴方向上的布局类型，  参数类型[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)，默认值为ARKUI\_DIRECTION\_AUTO。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置容器元素内主轴方向上的布局类型，  参数类型[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)，默认值为ARKUI\_DIRECTION\_AUTO。 |
| NODE\_CONSTRAINT\_SIZE = 48 | 约束尺寸属性，组件布局时，进行尺寸范围限制，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：最小宽度，单位vp；  .value[1].f32：最大宽度，单位vp；  .value[2].f32：最小高度，单位vp；  .value[3].f32：最大高度，单位vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：最小宽度，单位vp；  .value[1].f32：最大宽度，单位vp；  .value[2].f32：最小高度，单位vp；  .value[3].f32：最大高度，单位vp； |
| NODE\_GRAY\_SCALE = 49 | 灰度效果属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：灰度转换比例，范围0-1之间，默认值为0，比如0.5指按照50%进行灰度处理；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：灰度转换比例，范围0-1之间； |
| NODE\_INVERT = 50 | 反转输入的图像比例属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：图像反转比例，范围0-1之间，默认值为0，比如0.5指按照50%进行反转处理；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：图像反转比例，范围0-1之间； |
| NODE\_SEPIA = 51 | 图像转换为深褐色比例属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：图像转换为深褐色比例，范围0-1之间，默认值为0，比如0.5指按照50%进行深褐色处理；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：图像转换为深褐色比例，范围0-1之间； |
| NODE\_CONTRAST = 52 | 对比度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：对比度，等于1时为原图，越大则对比度越高，默认值为1，取值范围：[0, 10)；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：对比度，取值范围：[0, 10)； |
| NODE\_FOREGROUND\_COLOR = 53 | 前景颜色属性，支持属性设置和属性获取接口。属性重置接口无效果。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式，支持两种入参格式：  1：.value[0].u32：颜色数值，0xargb类型，如0xFFFF0000表示红色，默认值为0xFF000000；  2：.value[0].i32：颜色数值枚举ArkUI\_ColoringStrategy；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb类型； |
| NODE\_OFFSET = 54 | 组件子元素相对组件自身的额外偏移属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示x轴方向的偏移值, 单位为vp。  .value[1].f32 表示y轴方向的偏移值, 单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示x轴方向的偏移值, 单位为vp。  .value[1].f32 表示y轴方向的偏移值, 单位为vp。 |
| NODE\_MARK\_ANCHOR = 55 | 组件子元素在位置定位时的锚点属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示锚点x坐标值, 单位为vp。  .value[1].f32 表示锚点y坐标值, 单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示锚点x坐标值, 单位为vp。  .value[1].f32 表示锚点y坐标值, 单位为vp。 |
| NODE\_BACKGROUND\_IMAGE\_POSITION = 56 | 背景图在组件中显示位置，即相对于组件左上角的坐标，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：x轴方向的位置，单位为px。  .value[1].f32：y轴方向的位置, 单位为px。  .value[2].?i32：对齐模式。参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。默认值为ARKUI\_ALIGNMENT\_TOP\_START。**起始版本：** 12  .value[3].?i32：布局方向。参数类型为[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)。默认值为ARKUI\_DIRECTION\_AUTO。**起始版本：** 12  在大部分场景下，这个参数都应该被设置成AUTO，这个模式允许系统自动处理布局方向，如果在某些场景下需要保持特定的方向，设置这个属性为LTR（Left-to-Right）或者RTL（Right-to-Left）。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：x轴方向的位置，单位为px。  .value[1].f32：y轴方向的位置，单位为px。  .value[2].i32：对齐模式。参数类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。默认值为ARKUI\_ALIGNMENT\_TOP\_START。**起始版本：** 12  .value[3].i32：布局方向。参数类型为[ArkUI\_Direction](capi-native-type-h.md#arkui_direction)。默认值为ARKUI\_DIRECTION\_AUTO。**起始版本：** 12 |
| NODE\_ALIGN\_RULES = 57 | 相对容器中子组件的对齐规则属性，支持属性设置，属性重置，获取属性接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)对象作为组件的对齐规则。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_AlignmentRuleOption](capi-arkui-nativemodule-arkui-alignmentruleoption.md)对象作为组件的对齐规则。 |
| NODE\_ALIGN\_SELF = 58 | 设置子组件在父容器交叉轴的对齐格式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置子组件在父容器交叉轴的对齐格式类型，  参数类型[ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment)，默认值为ARKUI\_ITEM\_ALIGNMENT\_AUTO。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置子组件在父容器交叉轴的对齐格式类型，  参数类型[ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment)，默认值为ARKUI\_ITEM\_ALIGNMENT\_AUTO。 |
| NODE\_FLEX\_GROW = 59 | 设置组件在父容器的剩余空间所占比例，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：父容器的剩余空间所占比例。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：父容器的剩余空间所占比例。 |
| NODE\_FLEX\_SHRINK = 60 | 设置父容器压缩尺寸分配给此属性所在组件的比例，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：父容器压缩尺寸分配给此属性所在组件的比例数值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：父容器压缩尺寸分配给此属性所在组件的比例数值。 |
| NODE\_FLEX\_BASIS = 61 | 设置组件的基准尺寸，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：组件在父容器主轴方向上的基准尺寸。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：组件在父容器主轴方向上的基准尺寸。 |
| NODE\_ACCESSIBILITY\_GROUP = 62 | 无障碍组属性, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：为1时表示该组件及其所有子组件为一整个可以选中的组件。无障碍服务将不再关注其子组件内容。参数类型为1或者0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：为1时表示该组件及其所有子组件为一整个可以选中的组件。无障碍服务将不再关注其子组件内容。参数类型为1或者0。 |
| NODE\_ACCESSIBILITY\_TEXT = 63 | 无障碍文本属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string：无障碍文本。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：无障碍文本。 |
| NODE\_ACCESSIBILITY\_MODE = 64 | 无障碍辅助服务模式，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：辅助服务模式，参数类型[ArkUI\_AccessibilityMode](capi-native-type-h.md#arkui_accessibilitymode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：辅助服务模式，参数类型[ArkUI\_AccessibilityMode](capi-native-type-h.md#arkui_accessibilitymode)。 |
| NODE\_ACCESSIBILITY\_DESCRIPTION = 65 | 无障碍说明属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string：无障碍说明。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：无障碍说明。 |
| NODE\_FOCUS\_STATUS = 66 | 组件获取焦点属性，支持属性设置，属性获取。  **说明：** 设置参数为0时，当前层级页面获焦组件失焦，焦点转移到根容器上。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型为1表示组件获焦，为0表示组件失焦。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1表示组件获焦，为0表示组件失焦。 |
| NODE\_ASPECT\_RATIO = 67 | 设置组件的宽高比，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：组件的宽高比，输入值为 width/height。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：组件的宽高比，width/height的比值。 |
| NODE\_LAYOUT\_WEIGHT = 68 | Row/Column/Flex 布局下的子组件布局权重参数，支持属性设置、属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：子组件占主轴尺寸的权重。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：子组件占主轴尺寸的权重。 |
| NODE\_DISPLAY\_PRIORITY = 69 | Row/Column/Flex(单行) 布局下的子组件在布局容器中显示的优先级。当子组件的displayPriority大于1时，displayPriority数值越大，优先级越高。支持属性设置、属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：子组件在父容器中的显示优先级。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：子组件在父容器中的显示优先级。 |
| NODE\_OUTLINE\_WIDTH = 70 | 设置元素的外描边宽度。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：元素左边的外描边宽度。  .value[1].f32：元素上边的外描边宽度。  .value[2].f32：元素右边的外描边宽度。  .value[3].f32：元素下边的外描边宽度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：元素左边的外描边宽度。  .value[1].f32：元素上边的外描边宽度。  .value[2].f32：元素右边的外描边宽度。  .value[3].f32：元素下边的外描边宽度。 |
| NODE\_WIDTH\_PERCENT = 71 | 宽度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：宽度数值，单位为百分比；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：宽度数值，单位为百分比； |
| NODE\_HEIGHT\_PERCENT = 72 | 高度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：高度数值，单位为百分比；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：高度数值，单位为百分比； |
| NODE\_PADDING\_PERCENT = 73 | 内间距属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式有两种：  1：上下左右四个位置的内间距值相等。  .value[0].f32：内间距数值，单位为百分比；  2：分别指定上下左右四个位置的内间距值。  .value[0].f32：上内间距数值，单位为百分比；  .value[1].f32：右内间距数值，单位为百分比；  .value[2].f32：下内间距数值，单位为百分比；  .value[3].f32：左内间距数值，单位为百分比；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上内间距数值，单位为百分比；  .value[1].f32：右内间距数值，单位为百分比；  .value[2].f32：下内间距数值，单位为百分比；  .value[3].f32：左内间距数值，单位为百分比； |
| NODE\_MARGIN\_PERCENT = 74 | 外间距属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式有两种：  1：上下左右四个位置的外间距值相等。  .value[0].f32：外间距数值，单位为百分比；  2：分别指定上下左右四个位置的外间距值。  .value[0].f32：上外间距数值，单位为百分比；  .value[1].f32：右外间距数值，单位为百分比；  .value[2].f32：下外间距数值，单位为百分比；  .value[3].f32：左外间距数值，单位为百分比；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上外间距数值，单位为百分比；  .value[1].f32：右外间距数值，单位为百分比；  .value[2].f32：下外间距数值，单位为百分比；  .value[3].f32：左外间距数值，单位为百分比； |
| NODE\_GEOMETRY\_TRANSITION = 75 | 组件内隐式共享元素转场，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.i32：参数类型为1或者0。共享元素绑定的2个组件，针对出场元素未进行删除时是否要继续参与共享元素动画，默认为false，不参与保持原始位置不动。  .string 用于设置绑定关系，id置""清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1或者0。共享元素绑定的2个组件，针对出场元素未进行删除时是否要继续参与共享元素动画，默认未false，不参与保持原始位置不动。  .string 用于设置绑定关系，id置""清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |
| NODE\_RELATIVE\_LAYOUT\_CHAIN\_MODE = 76 | 指定以该组件为链头所构成的链的参数，支持属性设置、属性重置和属性获取接口。仅当父容器为RelativeContainer时生效。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：链的方向。枚举[ArkUI\_Axis](capi-native-type-h.md#arkui_axis)。  .value[1].i32：链的样式。枚举[ArkUI\_RelativeLayoutChainStyle](capi-native-type-h.md#arkui_relativelayoutchainstyle)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：链的方向。枚举[ArkUI\_Axis](capi-native-type-h.md#arkui_axis)。  .value[1].i32：链的样式。枚举[ArkUI\_RelativeLayoutChainStyle](capi-native-type-h.md#arkui_relativelayoutchainstyle)。 |
| NODE\_RENDER\_FIT = 77 | 设置宽高动画过程中的组件内容填充方式，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 内容填充方式，使用[ArkUI\_RenderFit](capi-native-type-h.md#arkui_renderfit)枚举值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 内容填充方式，使用[ArkUI\_RenderFit](capi-native-type-h.md#arkui_renderfit)枚举值。 |
| NODE\_OUTLINE\_COLOR = 78 | 外描边颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].u32：统一设置四条边的边框颜色，使用0xargb表示，如0xFFFF11FF。  2: .value[0].u32：设置上侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[1].u32：设置右侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[2].u32：设置下侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[3].u32：设置左侧边框颜色，使用0xargb表示，如0xFFFF11FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：设置上侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[1].u32：设置右侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[2].u32：设置下侧边框颜色，使用0xargb表示，如0xFFFF11FF。  .value[3].u32：设置左侧边框颜色，使用0xargb表示，如0xFFFF11FF。 |
| NODE\_SIZE = 79 | 设置高宽尺寸，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：宽度数值，单位为vp；  .value[1].f32：高度数值，单位为vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：宽度数值，单位为vp；  .value[1].f32：高度数值，单位为vp； |
| NODE\_RENDER\_GROUP = 80 | 设置当前组件和子组件是否先整体离屏渲染绘制后再与父控件融合绘制，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型为1表示当前组件与子组件需要先整体离屏渲染绘制后再与父控件融合绘制，参数类型为0表示不需要整体离屏渲染绘制后再与父控件融合绘制。默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1表示当前组件与子组件完成整体离屏渲染绘制，参数类型为0表示当前组件与子组件未完成整体离屏渲染绘制。 |
| NODE\_COLOR\_BLEND = 81 | 为组件添加颜色叠加效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：叠加的颜色，使用0xargb表示，默认值为0x00000000。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：叠加的颜色，使用0xargb表示，如0xFFFF11FF。 |
| NODE\_FOREGROUND\_BLUR\_STYLE = 82 | 为当前组件提供内容模糊能力，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示内容模糊样式，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。  .value[1]?.i32 表示内容模糊效果使用的深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。  .value[2]?.i32 表示内容模糊效果使用的取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[3]?.f32 表示模糊效果程度，取[0.0,1.0]范围内的值。  .value[4]?.i32 表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。  .value[5]?.i32 表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示内容模糊样式，取[ArkUI\_BlurStyle](capi-native-type-h.md#arkui_blurstyle)枚举值。  .value[1].i32 表示内容模糊效果使用的深浅色模式，取[ArkUI\_ColorMode](capi-native-type-h.md#arkui_colormode)枚举值。  .value[2].i32 表示内容模糊效果使用的取色模式，取[ArkUI\_AdaptiveColor](capi-native-type-h.md#arkui_adaptivecolor)枚举值。  .value[3].f32 表示模糊效果程度，取[0.0,1.0]范围内的值。  .value[4].i32 表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。  .value[5].i32 表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。 |
| NODE\_LAYOUT\_RECT = 83 | 组件布局大小位置属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：组件X轴坐标，单位为px；  .value[1].i32：组件Y轴坐标，单位为px；  .value[2].i32：组件宽度，单位为px；  .value[3].i32：组件高度，单位为px；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：组件X轴坐标，单位为px；  .value[1].i32：组件Y轴坐标，单位为px；  .value[2].i32：组件宽度，单位为px；  .value[3].i32：组件高度，单位为px； |
| NODE\_FOCUS\_ON\_TOUCH = 84 | 设置当前组件是否支持点击获焦能力，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型为1表示支持点击获焦，为0表示不支持点击获焦。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1表示支持点击获焦，为0表示不支持点击获焦。 |
| NODE\_BORDER\_WIDTH\_PERCENT = 85 | 边框宽度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].f32：统一设置四条边的边框宽度，单位为百分比。  2: .value[0].f32：设置上边框的边框宽度，单位为百分比。  .value[1].f32：设置右边框的边框宽度，单位为百分比。  .value[2].f32：设置下边框的边框宽度，单位为百分比。  .value[3].f32：设置左边框的边框宽度，单位为百分比。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置上边框的边框宽度，单位为百分比。  .value[1].f32：设置右边框的边框宽度，单位为百分比。  .value[2].f32：设置下边框的边框宽度，单位为百分比。  .value[3].f32：设置左边框的边框宽度，单位为百分比。 |
| NODE\_BORDER\_RADIUS\_PERCENT = 86 | 边框圆角属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  1: .value[0].f32：统一设置四条边的边框圆角半径，单位为百分比。  2: .value[0].f32：设置左上角圆角半径，单位为百分比。  .value[1].f32：设置右上角圆角半径，单位为百分比。  .value[2].f32：设置左下角圆角半径，单位为百分比。  .value[3].f32：设置右下角圆角半径，单位为百分比。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置左上角圆角半径，单位为百分比。  .value[1].f32：设置右上角圆角半径，单位为百分比。  .value[2].f32：设置左下角圆角半径，单位为百分比。  .value[3].f32：设置右下角圆角半径，单位为百分比。 |
| NODE\_ACCESSIBILITY\_ID = 87 | 无障碍自定义标识ID，支持属性获取。属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：无障碍自定义标识ID。 |
| NODE\_ACCESSIBILITY\_ACTIONS = 88 | 定义无障碍支持操作类型属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：配置无障碍操作类型，参数类型[ArkUI\_AccessibilityActionType](capi-native-type-h.md#arkui_accessibilityactiontype)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：配置无障碍操作类型，参数类型[ArkUI\_AccessibilityActionType](capi-native-type-h.md#arkui_accessibilityactiontype)。 |
| NODE\_ACCESSIBILITY\_ROLE = 89 | 定义无障碍组件类型属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：无障碍组件类型，参数类型[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：无障碍组件类型，参数类型[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)。 |
| NODE\_ACCESSIBILITY\_STATE = 90 | 定义无障碍状态属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数类型为[ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数类型为[ArkUI\_AccessibilityState](capi-arkui-nativemodule-arkui-accessibilitystate.md)。 |
| NODE\_ACCESSIBILITY\_VALUE = 91 | 定义无障碍信息属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数类型为[ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数类型为[ArkUI\_AccessibilityValue](capi-arkui-nativemodule-arkui-accessibilityvalue.md)。 |
| NODE\_EXPAND\_SAFE\_AREA = 92 | 定义控制组件扩展其安全区域，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0]?.u32：扩展安全区域的枚举值集合[ArkUI\_SafeAreaType](capi-native-type-h.md#arkui_safeareatype)，例如：ARKUI\_SAFE\_AREA\_TYPE\_SYSTEM | ARKUI\_SAFE\_AREA\_TYPE\_CUTOUT；  .value[1]?.u32：扩展安全区域的方向枚举值集合[ArkUI\_SafeAreaEdge](capi-native-type-h.md#arkui_safeareaedge)；例如：ARKUI\_SAFE\_AREA\_EDGE\_TOP | ARKUI\_SAFE\_AREA\_EDGE\_BOTTOM；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：扩展安全区域；  .value[1].u32：扩展安全区域的方向。 |
| NODE\_VISIBLE\_AREA\_CHANGE\_RATIO = 93 | 定义控制组件触发可视区域面积变更事件的可视区域面积占组件本身面积的比例阈值。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[...].f32：占比数值，输入范围0-1。  .?object：参数类型为[ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)。  **起始版本：** 22  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[...].f32：占比数值。  .object：返回类型为[ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)。  **起始版本：** 22 |
| NODE\_TRANSITION = 94 | 定义组件插入和删除时显示过渡动效，支持属性设置，属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数类型为[ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数类型为[ArkUI\_TransitionEffect](capi-arkui-nativemodule-arkui-transitioneffect.md)。 |
| NODE\_UNIQUE\_ID(deprecated) = 95 | 组件标识ID，支持属性获取。  组件标识ID只读，且进程内唯一。  **废弃版本：** 从API version 12开始支持，从API version 20开始废弃。建议使用[OH\_ArkUI\_NodeUtils\_GetNodeUniqueId](capi-native-node-h.md#oh_arkui_nodeutils_getnodeuniqueid)替代。 |
| NODE\_FOCUS\_BOX = 96 | 设置当前组件系统焦点框样式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 焦点框相对组件边缘的距离。  正数代表外侧，负数代表内侧。  不支持百分比。  .value[1].f32: 焦点框宽度。 不支持负数和百分比。  .value[2].u32: 焦点框颜色。 |
| NODE\_CLICK\_DISTANCE = 97 | 组件所绑定的点击手势移动距离限制，支持属性设置。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示识别点击手势时允许手指在该范围内移动，单位为vp。 |
| NODE\_TAB\_STOP = 98 | 控制焦点是否能停在当前组件，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型为1表示焦点能停在当前组件，为0表示焦点不能停在当前组件。默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1表示焦点停在当前组件，为0表示焦点未停在当前组件。  **起始版本：** 14 |
| NODE\_BACKDROP\_BLUR = 99 | 设置背景模糊效果，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：表示背景模糊半径，取值范围[0,+∞)。单位px，默认值0.0。  .value[1]?.f32：表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。  .value[2]?.f32：表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：表示背景模糊半径，取值范围[0,+∞)。单位px。  .value[1].f32：表示灰阶模糊参数，对黑色的提亮程度，取值范围为[0,127]。  .value[2].f32：表示灰阶模糊参数，对白色的压暗程度，取值范围为[0,127]。  **起始版本：** 15 |
| NODE\_BACKGROUND\_IMAGE\_RESIZABLE\_WITH\_SLICE = 100 | 设置背景图在拉伸时可调整大小的属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32: 图片左部拉伸时，图片的像素值保持不变，单位为vp。  .value[1].f32: 图片顶部拉伸时，图片的像素值保持不变，单位为vp。  .value[2].f32: 图片右部拉伸时，图片的像素值保持不变，单位为vp。  .value[3].f32: 图片底部拉伸时，图片的像素值保持不变，单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 图片左部拉伸时，图片的像素值保持不变，单位为vp。  .value[1].f32: 图片顶部拉伸时，图片的像素值保持不变，单位为vp。  .value[2].f32: 图片右部拉伸时，图片的像素值保持不变，单位为vp。  .value[3].f32: 图片底部拉伸时，图片的像素值保持不变，单位为vp。  **起始版本：** 19 |
| NODE\_NEXT\_FOCUS = 101 | 设置下一个走焦节点。[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的参数格式：  .value[0].i32：走焦类型，定义在 [ArkUI\_FocusMove](capi-native-type-h.md#arkui_focusmove)。.object: 下一个焦点。参数类型为[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。  **起始版本：** 18 |
| NODE\_VISIBLE\_AREA\_APPROXIMATE\_CHANGE\_RATIO = 102 | 设置可见区域变化监听的参数。  **说明：** 非实时回调，实际回调与预期间隔可能存在差别。两次可见区域回调的时间间隔不小于预期更新间隔。当开发者设置的预期间隔过小时，由系统负载决定实际回调间隔时间。当前接口的可见区域回调阈值默认包含0。例如，开发者设置回调阈值为[0.5]，实际生效的阈值为[0.0, 0.5]。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数类型为[ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数类型为[ArkUI\_VisibleAreaEventOptions](i-arkui-nativemodule-arkui-visibleareaeventoptions.md)。  **起始版本：** 17 |
| NODE\_TRANSLATE\_WITH\_PERCENT = 103 | 设置组件平移，支持百分比形式的平移入参，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴移动距离，默认单位为百分比，除非value[3]存在且value[3]为0时单位为vp，默认值0；  .value[1].f32： y轴移动距离，默认单位为百分比，除非value[4]存在且value[4]为0时单位为vp，默认值0；  .value[2].f32： z轴移动距离，单位vp，默认值0。  .value[3]?.i32： x轴移动距离是否为百分比形式指定，取值范围：0或1。为1时表示以百分比形式指定，例如value[0].f32=0.1且value[3].i32=1时表示x方向平移10%。默认值1。  .value[4]?.i32： y轴移动距离是否为百分比形式指定，取值范围：0或1。为1时表示以百分比形式指定，例如value[1].f32=0.1且value[4].i32=1时表示y方向平移10%，默认值1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴移动距离，单位取决于value[3]；  .value[1].f32： y轴移动距离，单位取决于value[4]；  .value[2].f32： z轴移动距离，单位vp；  .value[3].i32： x轴移动距离的单位是否为百分比，当value[3].i32为0时x轴移动距离单位为vp，当value[3].i32为1时x轴移动距离单位为百分比；  .value[4].i32： y轴移动距离的单位是否为百分比，当value[4].i32为0时y轴移动距离单位为vp，当value[4].i32为1时y轴移动距离单位为百分比；  **起始版本：** 20 |
| NODE\_ROTATE\_ANGLE = 104 | 设置组件旋转，支持各轴旋转角属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴方向旋转角度，默认值0；  .value[1].f32： y轴方向旋转角度，默认值0；  .value[2].f32： z轴方向旋转角度，默认值0；  .value[3].f32： 视距，即视点到z=0平面的距离，单位px，默认值0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： x轴方向旋转角度，默认值0；  .value[1].f32： y轴方向旋转角度，默认值0；  .value[2].f32： z轴方向旋转角度，默认值0；  .value[3].f32： 视距，即视点到z=0平面的距离，单位px，默认值0。  **起始版本：** 20 |
| NODE\_WIDTH\_LAYOUTPOLICY = 105 | 设置组件宽度布局策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 布局策略；参数类型为[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 布局策略；参数类型为[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。  **起始版本：** 21 |
| NODE\_HEIGHT\_LAYOUTPOLICY = 106 | 设置组件高度布局策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 布局策略；参数类型为[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 布局策略；参数类型为[ArkUI\_LayoutPolicy](capi-native-type-h.md#arkui_layoutpolicy)。  **起始版本：** 21 |
| NODE\_POSITION\_EDGES = 107 | 设置组件相对容器内容区边界的位置，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：组件相对容器内容区边界的位置；参数类型为[ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object： 组件相对容器内容区边界的位置；参数类型为[ArkUI\_PositionEdges](capi-arkui-nativemodule-arkui-positionedges.md)。  **起始版本：** 21 |
| NODE\_ALLOW\_FORCE\_DARK = 108 | 设置组件是否启用反色能力，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：反色能力；参数取值为0或1，取值为0表示不启用反色能力，取值为1表示启用反色能力。  **起始版本：** 21 |
| NODE\_PIXEL\_ROUND = 109 | 设置组件的像素取整策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：组件的像素取整策略；参数类型为[ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：组件的像素取整策略；参数类型为[ArkUI\_PixelRoundPolicy](capi-arkui-nativemodule-arkui-pixelroundpolicy.md)。  **起始版本：** 21 |
| NODE\_MOTION\_PATH = 111 | 设置组件的运动路径属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：指向路径动画的运动路径配置项的指针；参数类型为[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：指向路径动画的运动路径配置项的指针；参数类型为[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)。  **起始版本：** 23 |
| NODE\_HOVER\_EFFECT = 112 | 定义组件被悬停时的效果。该属性可根据需要通过API进行设置、重置和获取。  设置该属性时，[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数的格式：  .value[0].i32：组件在悬停状态下的悬停效果。参数类型为[ArkUI\_HoverEffect](capi-native-type-h.md#arkui_hovereffect)。默认值为**ARKUI\_HOVER\_EFFECT\_AUTO**。  返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .value[0].i32： 组件在悬停状态下的悬停效果。参数类型为[ArkUI\_HoverEffect](capi-native-type-h.md#arkui_hovereffect)。  **起始版本：** 23 |
| NODE\_FOCUS\_SCOPE\_ID = 113 | 将容器设置为具有特定标识符的焦点组，支持属性设置、属性重置和属性获取接口。  设置该属性时，[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数的格式：  .string：焦点作用域标识符。  .value[0].i32：该作用域是否为焦点组，默认值为0。取值范围为1或0。1表示设置为焦点组。0表示组件未被设置为焦点组。  .value[1].i32：箭头键是否可以将焦点从焦点组内部移至外部，仅当isGroup为true时有效，默认值为1。取值范围为1或0。1表示箭头键可以将焦点从焦点组内部移至外部，0表示箭头键无法将焦点从焦点组内部移至外部。  属性获取方法的返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：焦点作用域标识符。  .value[0].i32： 该作用域是否为焦点组，默认值为0。取值范围为1或0。1表示设置为焦点组。0表示组件未被设置为焦点组。  .value[1].i32： 箭头键是否可以将焦点从焦点组内部移至外部，仅当isGroup为true时有效，默认值为1。取值范围为1或0。1表示箭头键可以将焦点从焦点组内部移至外部，0表示箭头键无法将焦点从焦点组内部移至外部。  **起始版本：** 23 |
| NODE\_FOCUS\_SCOPE\_PRIORITY = 114 | 设置组件在特定焦点作用域内的焦点优先级，支持属性设置、属性重置和属性获取接口。  设置该属性时，[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数的格式：  .string：焦点作用域标识符。  .value[0].i32：焦点作用域内获焦优先级。参数类型为[ArkUI\_FocusPriority](capi-native-type-h.md#arkui_focuspriority)。默认值为 **ARKUI\_FOCUS\_PRIORITY\_AUTO**。  属性获取方法的返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：焦点作用域标识符。  .value[0].i32：焦点作用域优先级。参数类型为[ArkUI\_FocusPriority](capi-native-type-h.md#arkui_focuspriority)。  **起始版本：** 23 |
| NODE\_ON\_CLICK\_EVENT\_DISTANCE\_THRESHOLD = 115 | 设置点击事件的距离阈值，支持属性设置、属性重置和属性获取接口。  设置该属性时，[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数的格式：  .value[0].f32：点击事件移动阈值。取值范围(0, +∞)。默认值为+∞，单位vp。  属性获取方法的返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 点击事件移动阈值。  **起始版本：** 23 |
| NODE\_RESPONSE\_REGION\_LIST = 116 | 设置组件事件的响应区域，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .data[0].i32：适用于此响应区域的事件工具类型。参数类型为[ArkUI\_ResponseRegionSupportedTool](capi-native-type-h.md#arkui_responseregionsupportedtool)。默认值：ARKUI\_RESPONSE\_REGIN\_SUPPORTED\_TOOL\_ALL。  .data[1].f32：触摸点相对于组件左上角的x轴坐标，默认值：0.0，单位为vp。  .data[2].f32：触摸点相对于组件左上角的y轴坐标，默认值：0.0，单位为vp。  .data[3].f32：触摸热区的宽度，默认值：100.0，单位为百分比。  .data[4].f32：触摸热区的高度，默认值：100.0，单位为百分比。  .data[5...].f32：可以设置多个手势响应区域，顺序和上述一致。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .data[0].i32：适用于此响应区域的事件工具类型。参数类型为[ArkUI\_ResponseRegionSupportedTool](capi-native-type-h.md#arkui_responseregionsupportedtool)。默认值：ARKUI\_RESPONSE\_REGIN\_SUPPORTED\_TOOL\_ALL。  .data[1].f32：触摸点相对于组件左上角的x轴坐标，默认值：0.0，单位为vp。  .data[2].f32：触摸点相对于组件左上角的y轴坐标，默认值：0.0，单位为vp。  .data[3].f32：触摸热区的宽度，默认值：100.0，单位为百分比。  .data[4].f32：触摸热区的高度，默认值：100.0，单位为百分比。  .data[5...].f32：可以设置多个手势响应区域，顺序和上述一致。  **说明：** 设置时data数据大小无数量限制，均可以设置成功，但仅支持获取到20个。获取到的data数组顺序与设置顺序可能存在差异。  **起始版本：** 23 |
| NODE\_MONOPOLIZE\_EVENTS = 117 | 定义独占事件属性，该属性可根据需要通过API进行设置、重置和获取。  设置该属性时，[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数的格式：  .value[0].i32：取值范围为1或0。1表示设置组件独占。0表示组件未设置独占属性。  返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .value[0].i32：取值范围为1或0。1表示设置组件独占。0表示组件未设置独占属性。  **起始版本：** 23 |
| NODE\_CHAIN\_WEIGHT = 118 | 父组件为RelativeContainer时，设置已形成链的组件的布局位置，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：组件在水平方向的布局权重，默认值：0。  设置异常值时，按默认值显示。  .value[1].f32：组件在竖直方向的布局权重，默认值：0。  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：组件在水平方向的布局权重。  .value[1].f32：组件在竖直方向的布局权重。  **起始版本：** 23 |
| NODE\_IGNORE\_LAYOUT\_SAFE\_AREA = 119 | 设置扩展组件布局时的安全区域，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：扩展安全区域的类型。参数类型为[ArkUI\_LayoutSafeAreaType](capi-native-type-h.md#arkui_layoutsafeareatype)，默认值：ARKUI\_LAYOUT\_SAFE\_AREA\_TYPE\_SYSTEM。  设置异常值时，按默认值显示。  .value[1].u32：扩展安全区域的方向。参数类型为[ArkUI\_LayoutSafeAreaEdge](capi-native-type-h.md#arkui_layoutsafeareaedge)，默认值：ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_ALL，例如：ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_TOP | ARKUI\_LAYOUT\_SAFE\_AREA\_EDGE\_BOTTOM。  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：扩展安全区域的类型。  .value[1].u32：扩展安全区域的方向。  **起始版本：** 23 |
| NODE\_DASH\_WIDTH = 120 | 设置边框样式为虚线时虚线的长度，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上边框虚线的长度，单位vp。  .value[1].f32：右边框虚线的长度，单位vp。  .value[2].f32：下边框虚线的长度，单位vp。  .value[3].f32：左边框虚线的长度，单位vp。  取值范围：[0, +∞)  设置异常值时，按默认的虚线效果显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上边框虚线的长度，单位vp。  .value[1].f32：右边框虚线的长度，单位vp。  .value[2].f32：下边框虚线的长度，单位vp。  .value[3].f32：左边框虚线的长度，单位vp。  **起始版本：** 23 |
| NODE\_DASH\_GAP = 121 | 设置边框样式为虚线时虚线的间隙，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上边框虚线的间隙，单位vp。  .value[1].f32：右边框虚线的间隙，单位vp。  .value[2].f32：下边框虚线的间隙，单位vp。  .value[3].f32：左边框虚线的间隙，单位vp。  取值范围：[0, +∞)  设置异常值时，按默认的虚线效果显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：上边框虚线的间隙，单位vp。  .value[1].f32：右边框虚线的间隙，单位vp。  .value[2].f32：下边框虚线的间隙，单位vp。  .value[3].f32：左边框虚线的间隙，单位vp。  **起始版本：** 23 |
| NODE\_LAYOUT\_GRAVITY = 122 | 设置Stack容器中子组件的对齐规则，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Stack容器中子组件的对齐规则。参数类型为[ArkUI\_LocalizedAlignment](capi-native-type-h.md#arkui_localizedalignment)，默认值：ARKUI\_ALIGNMENT\_CENTER。  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Stack容器中子组件的对齐规则。参数类型为[ArkUI\_LocalizedAlignment](capi-native-type-h.md#arkui_localizedalignment)。  **起始版本：** 23 |
| NODE\_BORDER\_RADIUS\_TYPE = 123 | 设置组件绘制圆角的模式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：组件绘制圆角的模式。参数类型为[ArkUI\_RenderStrategy](capi-native-type-h.md#arkui_renderstrategy)，默认值：ARKUI\_RENDERSTRATEGY\_FAST。  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：组件绘制圆角的模式。参数类型为[ArkUI\_RenderStrategy](capi-native-type-h.md#arkui_renderstrategy)。  **起始版本：** 23 |
| NODE\_TEXT\_CONTENT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT = 1000 | Text组件设置文本内容属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示文本内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示文本内容。 |
| NODE\_FONT\_COLOR = 1001 | 组件字体颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：字体颜色数值，0xargb格式，形如 0xFFFF0000 表示红色；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：字体颜色数值，0xargb格式； |
| NODE\_FONT\_SIZE = 1002 | 组件字体大小属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：字体大小数值，单位为fp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：字体大小数值，单位为fp； |
| NODE\_FONT\_STYLE = 1003 | 组件字体样式属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)； |
| NODE\_FONT\_WEIGHT = 1004 | 组件字体粗细属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)； |
| NODE\_TEXT\_LINE\_HEIGHT = 1005 | 文本行高属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示lineHeight值，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示lineHeight值，单位为fp。 |
| NODE\_TEXT\_DECORATION = 1006 | 文本装饰线样式及其颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本装饰线类型[ArkUI\_TextDecorationType](capi-native-type-h.md#arkui_textdecorationtype)，默认值为ARKUI\_TEXT\_DECORATION\_TYPE\_NONE；  .value[1]?.u32：可选值，装饰线颜色，0xargb格式，形如 0xFFFF0000 表示红色；  .value[2]?.i32：文本装饰线样式[ArkUI\_TextDecorationStyle](capi-native-type-h.md#arkui_textdecorationstyle)；  .value[3]?.f32：可选值，文本装饰线粗细比例，默认值：1.0，取值范围：[0, +∞)。该参数从API version 22开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本装饰线类型[ArkUI\_TextDecorationType](capi-native-type-h.md#arkui_textdecorationtype)；  .value[1].u32：装饰线颜色，0xargb格式。  .value[2].i32：文本装饰线样式[ArkUI\_TextDecorationStyle](capi-native-type-h.md#arkui_textdecorationstyle)；  .value[3].f32：文本装饰线粗细比例。该返回值从API version 22开始支持。 |
| NODE\_TEXT\_CASE = 1007 | 文本大小写属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本大小写类型[ArkUI\_TextCase](capi-native-type-h.md#arkui_textcase)，默认值为ARKUI\_TEXT\_CASE\_NORMAL。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本大小写类型[ArkUI\_TextCase](capi-native-type-h.md#arkui_textcase)。 |
| NODE\_TEXT\_LETTER\_SPACING = 1008 | 文本字符间距属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示字符间距值，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示字符间距值，单位为fp。 |
| NODE\_TEXT\_MAX\_LINES = 1009 | 文本最大行数属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示最大行数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示最大行数。 |
| NODE\_TEXT\_ALIGN = 1010 | 文本水平对齐方式, 支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本水平对齐方式，取[ArkUI\_TextAlignment](capi-native-type-h.md#arkui_textalignment)枚举值。默认值为ARKUI\_TEXT\_ALIGNMENT\_START。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本水平对齐方式，取[ArkUI\_TextAlignment](capi-native-type-h.md#arkui_textalignment)枚举值。 |
| NODE\_TEXT\_OVERFLOW = 1011 | 文本超长时的显示方式属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本超长时的显示方式[ArkUI\_TextOverflow](capi-native-type-h.md#arkui_textoverflow)。默认值为ARKUI\_TEXT\_OVERFLOW\_NONE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本超长时的显示方式。[ArkUI\_TextOverflow](capi-native-type-h.md#arkui_textoverflow)  **说明：** 支持此属性的[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)为：ARKUI\_NODE\_TEXT、ARKUI\_NODE\_TEXT\_INPUT、ARKUI\_NODE\_TEXT\_AREA。 |
| NODE\_FONT\_FAMILY = 1012 | Text字体列表属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string：字体字符串，多个用,分隔。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：字体字符串，多个用,分隔。 |
| NODE\_TEXT\_COPY\_OPTION = 1013 | 文本复制粘贴属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：复制粘贴方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)，默认值为ARKUI\_COPY\_OPTIONS\_NONE；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：复制粘贴方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)。 |
| NODE\_TEXT\_BASELINE\_OFFSET = 1014 | 文本基线的偏移量属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：偏移量数值，单位为fp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：偏移量数值，单位为fp。 |
| NODE\_TEXT\_TEXT\_SHADOW = 1015 | 文字阴影效果属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：阴影模糊半径，单位为vp；  .value[1].i32：阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)，默认值为ARKUI\_SHADOW\_TYPE\_COLOR；  .value[2].u32：阴影颜色，0xargb格式，形如 0xFFFF0000 表示红色；  .value[3].f32：阴影X轴偏移量，单位为vp；  .value[4].f32：阴影Y轴偏移量，单位为vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：阴影模糊半径，单位为vp；  .value[1].i32：阴影类型[ArkUI\_ShadowType](capi-native-type-h.md#arkui_shadowtype)；  .value[2].u32：阴影颜色，0xargb格式；  .value[3].f32：阴影X轴偏移量，单位为vp；  .value[4].f32：阴影Y轴偏移量，单位为vp； |
| NODE\_TEXT\_MIN\_FONT\_SIZE = 1016 | Text最小显示字号，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：文本最小显示字号，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：文本最小显示字号，单位为fp。 |
| NODE\_TEXT\_MAX\_FONT\_SIZE = 1017 | Text最大显示字号，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：文本最大显示字号，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：文本最大显示字号，单位为fp。 |
| NODE\_TEXT\_FONT = 1018 | Text样式，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string?：可选值 字体列表，使用多个字体，使用','进行分割。  .value[0].f32：文本尺寸，单位为fp。  .value[1]?.i32：可选值，文本的字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。  .value[2]?.i32：可选值，字体样式，参数类型[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。默认值为ARKUI\_FONT\_STYLE\_NORMAL。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：字体列表，使用多个字体，使用','进行分割。  .value[0].f32：文本尺寸，单位为fp。  .value[1].i32：文本的字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。  .value[2].i32：字体样式，参数类型[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |
| NODE\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY = 1019 | Text自适应高度的方式，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型[ArkUI\_TextHeightAdaptivePolicy](capi-native-type-h.md#arkui_textheightadaptivepolicy)。默认值为ARKUI\_TEXT\_HEIGHT\_ADAPTIVE\_POLICY\_MAX\_LINES\_FIRST。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型[ArkUI\_TextHeightAdaptivePolicy](capi-native-type-h.md#arkui_textheightadaptivepolicy)。 |
| NODE\_TEXT\_INDENT = 1020 | 文本首行缩进属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 表示首行缩进值，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 表示首行缩进值，单位为vp。 |
| NODE\_TEXT\_WORD\_BREAK = 1021 | 文本断行规则属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。默认值为ARKUI\_WORD\_BREAK\_BREAK\_WORD。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。 |
| NODE\_TEXT\_ELLIPSIS\_MODE = 1022 | 设置文本省略位置，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 参数类型[ArkUI\_EllipsisMode](capi-native-type-h.md#arkui_ellipsismode)。默认值为ARKUI\_ELLIPSIS\_MODE\_END。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 参数类型[ArkUI\_EllipsisMode](capi-native-type-h.md#arkui_ellipsismode)。 |
| NODE\_TEXT\_LINE\_SPACING = 1023 | 文本行间距属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示lineSpacing值，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 表示lineSpacing值，单位为fp。 |
| NODE\_FONT\_FEATURE = 1024 | 设置文本特性效果，设置NODE\_FONT\_FEATURE属性，NODE\_FONT\_FEATURE是 OpenType 字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持,支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 符合文本特性格式的字符串，格式为normal | <feature-tag-value>,  <feature-tag-value>的格式为：<string> [ <integer> | on | off ],  <feature-tag-value>的个数可以有多个，中间用','隔开,例如，使用等宽数字的输入格式为：ss01 on。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示文本特性的内容，多个文本特性之间使用逗号分隔。 |
| NODE\_TEXT\_ENABLE\_DATA\_DETECTOR = 1025 | 设置使能文本识别。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：使能文本识别，默认值false，true表示文本可实体识别，false表示不可识别。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：使能文本识别。 |
| NODE\_TEXT\_ENABLE\_DATA\_DETECTOR\_CONFIG = 1026 | 设置文本识别配置。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0...].i32: 实体类型数组，参数类型[ArkUI\_TextDataDetectorType](capi-native-type-h.md#arkui_textdatadetectortype)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0...].i32：实体类型数组，参数类型[ArkUI\_TextDataDetectorType](capi-native-type-h.md#arkui_textdatadetectortype)。 |
| NODE\_TEXT\_SELECTED\_BACKGROUND\_COLOR = 1027 | 文本选中时的背景色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式。 |
| NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING = 1028 | Text组件使用格式化字符串对象设置文本内容属性，支持属性设置，属性重置，属性获取接口。配置自定义[OH\_Drawing\_Typography](capi-drawing-oh-drawing-typography.md)对象到Text组件，会跳过文本控件的布局测算阶段，需要注意：  1、需要保证OH\_ArkUI\_StyledString对象、OH\_Drawing\_Typography对象的生命周期跟随Text组件生命周期，Text组件析构时重置OH\_ArkUI\_StyledString对象，否则会导致应用出现空指针崩溃。  2、保证OH\_Drawing\_TypographyLayout方法调用时序在Text组件的布局测算之前。  3、释放OH\_ArkUI\_StyledString对象、OH\_Drawing\_Typography对象时，需要同步调用Text组件的reset方法，否则会导致应用出现空指针崩溃。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object 表示 ArkUI\_StyledString 格式化字符串数据，参数类型为[ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object 表示 ArkUI\_StyledString 格式化字符串数据，参数类型为[ArkUI\_StyledString](capi-arkui-nativemodule-arkui-styledstring.md)。 |
| NODE\_TEXT\_HALF\_LEADING = 1029 | Text组件设置文本纵向居中显示。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本是否纵向居中显示，默认值false。  true表示文本是纵向居中显示，false表示文本不是纵向居中显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本是否纵向居中显示。 |
| NODE\_IMMUTABLE\_FONT\_WEIGHT = 1030 | 组件字体粗细属性，支持属性设置，属性重置和属性获取接口。通过此接口设置的粗细属性不会跟随系统字体粗细变化。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)；  **起始版本：** 15 |
| NODE\_TEXT\_LINE\_COUNT = 1031 | 文本行数属性，支持属性获取接口。属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 表示文本行数。  **起始版本：** 20 |
| NODE\_TEXT\_OPTIMIZE\_TRAILING\_SPACE = 1032 | 设置文本排版时是否优化每行结尾的空格，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置文本排版时是否优化每行结尾的空格，默认值为false。  true表示设置文本排版时优化每行结尾的空格，false表示不优化。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 文本排版时是否优化每行结尾的空格。  **起始版本：** 20 |
| NODE\_TEXT\_LINEAR\_GRADIENT = 1033 | 设置文本线性渐变效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：线性渐变的起始角度。当direction属性设置为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle属性生效；否则，以direction属性为主要布局方式。0点方向顺时针旋转为正向角度，默认值：180  .value[1].i32：线性渐变的方向[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)。设置除ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM之外的线性渐变方向后，angle不生效。默认值：ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM  .value[2].i32：为渐变的颜色重复着色，false表示不重复着色，true表示重复着色。默认值：false  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。  colors：渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，数组元素建议递增设置，如后一个数组元素比前一个数组元素小的话，按照等于前一个数组元素的值处理。  size：颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置大于colors数组长度或小于等于0的值以及异常值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：线性渐变的起始角度。当为ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，angle为设置值，其他情况均为默认值0。  .value[1].i32：线性渐变的方向[ArkUI\_LinearGradientDirection](capi-native-type-h.md#arkui_lineargradientdirection)。  .value[2].i32：为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。默认值：0  .object：参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。  size：生效后渐变色的颜色个数。  **起始版本：** 20 |
| NODE\_TEXT\_RADIAL\_GRADIENT = 1034 | 设置文本径向渐变渐变效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32：为径向渐变的中心点，即相对于当前文本框左上角的X轴坐标。  .value[1]?.f32：为径向渐变的中心点，即相对于当前文本框左上角的Y轴坐标。文本框左上角的坐标为[0,0]。  .value[2]?.f32：径向渐变的半径，默认值0。  .value[3]?.i32：为渐变的颜色重复着色，false表示不重复着色，true表示重复着色。默认值：false  .object：参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，数组元素建议递增设置，如后一个数组元素比前一个数组元素小的话，按照等于前一个数组元素的值处理。  size：颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置大于colors数组长度或小于等于0的值以及异常值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32：为径向渐变的中心点，即相对于当前文本框左上角的X轴坐标。  .value[1]?.f32：为径向渐变的中心点，即相对于当前文本框左上角的Y轴坐标。文本框左上角的坐标为[0,0]。  .value[2]?.f32：径向渐变的半径，默认值0。  .value[3]?.i32：为渐变的颜色重复着色，0表示不重复着色，1表示重复着色。默认值：0  .object：参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过：  colors：渐变色颜色数组，数组元素为0xargb格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。  size：生效后渐变色的颜色个数。  **起始版本：** 20 |
| NODE\_TEXT\_VERTICAL\_ALIGN = 1035 | 设置文本内容垂直对齐方式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本内容垂直对齐方式[ArkUI\_TextVerticalAlignment](capi-native-type-h.md#arkui_textverticalalignment)，默认值：ARKUI\_TEXT\_VERTICAL\_ALIGNMENT\_BASELINE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本内容垂直对齐方式[ArkUI\_TextVerticalAlignment](capi-native-type-h.md#arkui_textverticalalignment)。  **说明：** 支持此属性的[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)为：ARKUI\_NODE\_TEXT。  **起始版本：** 20 |
| NODE\_TEXT\_CONTENT\_ALIGN = 1036 | 设置文本内容区垂直对齐方式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本内容区垂直对齐方式[ArkUI\_TextContentAlign](capi-native-type-h.md#arkui_textcontentalign)，默认值：ARKUI\_TEXT\_CONTENT\_ALIGN\_CENTER。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本内容区垂直对齐方式[ArkUI\_TextContentAlign](capi-native-type-h.md#arkui_textcontentalign)。  **起始版本：** 21 |
| NODE\_TEXT\_MIN\_LINES = 1037 | 文本最小行数属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本最小行数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本最小行数。  **起始版本：** 22 |
| NODE\_TEXT\_ENABLE\_SELECTED\_DATA\_DETECTOR = 1038 | 开启选中词文本识别。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：开启选中词文本识别，true表示开启识别，false表示关闭识别。默认值：true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启选中词文本识别。  **起始版本：** 22 |
| NODE\_TEXT\_MIN\_LINE\_HEIGHT = 1040 | 设置文本最小行高，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：文本最小行高，默认值：0。单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：文本最小行高。单位为fp。  **起始版本：** 22 |
| NODE\_TEXT\_MAX\_LINE\_HEIGHT = 1041 | 设置文本最大行高，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：文本最大行高，默认值：0，表示最大行高不受限制。单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：文本最大行高。单位为fp。  **起始版本：** 22 |
| NODE\_TEXT\_LINE\_HEIGHT\_MULTIPLE = 1042 | 设置倍数行高模式的倍数值，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：倍数行高模式的倍数值，默认值：0，表示使用默认行高高度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：倍数行高模式的倍数值。  **起始版本：** 22 |
| NODE\_TEXT\_LAYOUT\_MANAGER = 1043 | 文本布局管理器，支持属性获取接口。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本布局管理器对象，参数类型为[ArkUI\_TextLayoutManager](capi-arkui-nativemodule-arkui-textlayoutmanager.md)。  **起始版本：** 22 |
| NODE\_TEXT\_EDIT\_MENU\_OPTIONS = 1044 | 文本菜单扩展项，支持属性设置接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本菜单扩展项配置数据，参数类型为[ArkUI\_TextEditMenuOptions](capi-arkui-nativemodule-arkui-texteditmenuoptions.md)。  **起始版本：** 22 |
| NODE\_TEXT\_BIND\_SELECTION\_MENU = 1045 | 自定义文本选择菜单，支持属性设置接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义文本选择菜单配置数据，参数类型为[ArkUI\_TextSelectionMenuOptions](-arkui-nativemodule-arkui-textselectionmenuoptions.md)。  **起始版本：** 22 |
| NODE\_TEXT\_TEXT\_SELECTION = 1046 | 设置文本选择区域，设置后选中区域将被高亮显示，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本选择的起始位置。  .value[1].i32：文本选择的结束位置。  .object：选择选项。参数类型为[ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本选择的起始位置。  .value[1].i32：文本选择的结束位置。  .object：选择选项。参数类型为[ArkUI\_SelectionOptions](capi-arkui-nativemodule-arkui-selectionoptions.md)。  **起始版本：** 23 |
| NODE\_TEXT\_COMPRESS\_LEADING\_PUNCTUATION = 1048 | 文本行首标点压缩开关，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否打开行首标点压缩开关。  true表示开启行首标点压缩，false表示关闭行首标点压缩。默认值false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否打开行首标点压缩开关。  **起始版本：** 23 |
| NODE\_TEXT\_INCLUDE\_FONT\_PADDING = 1049 | 设置是否在首行和尾行增加间距以避免文字截断。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置是否在首行和尾行增加间距以避免文字截断。true表示开启增加间距，false表示关闭增加间距。默认值：false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否在首行和尾行增加间距。true表示增加间距，false表示不增加间距。  **起始版本：** 23 |
| NODE\_TEXT\_FALLBACK\_LINE\_SPACING = 1050 | 针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：支持行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。默认值：false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。  **起始版本：** 23 |
| NODE\_TEXT\_MARQUEE\_OPTIONS = 1051 | 文本跑马灯模式配置项，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本跑马灯模式配置，参数类型为[ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本跑马灯模式配置，参数类型为[ArkUI\_TextMarqueeOptions](capi-arkui-nativemodule-arkui-textmarqueeoptions.md)。  **起始版本：** 23 |
| NODE\_TEXT\_DIRECTION = 1052 | 文本排版方向。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本的排版方向，取[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。  **起始版本：** 23 |
| NODE\_TEXT\_SELECTED\_DRAG\_PREVIEW\_STYLE = 1053 | 用于设置文本选中状态下的拖拽预览样式。  设置属性[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。  返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .object：文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。  **起始版本：** 23 |
| NODE\_SPAN\_CONTENT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SPAN = 2000 | 文本内容属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示[span](ts-basic-components-span.md)的文本内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示span的文本内容。 |
| NODE\_SPAN\_TEXT\_BACKGROUND\_STYLE = 2001 | 文本背景色属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32 表示文本背景颜色，0xargb格式，形如0xFFFF0000 表示红色。  第二个参数为文本背景圆角设置，支持如下两种设置方式：  - .value[1].f32：四个方向的圆角半径统一设置，单位为vp。  - .value[1].f32：设置左上角圆角半径，单位为vp。  .value[2].f32：设置右上角圆角半径，单位为vp。  .value[3].f32：设置左下角圆角半径，单位为vp。  .value[4].f32：设置右下角圆角半径，单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：文本背景颜色，0xargb格式。  .value[1].f32：左上角圆角半径，单位为vp。  .value[2].f32：右上角圆角半径，单位为vp。  .value[3].f32：左下角圆角半径，单位为vp。  .value[4].f32：右下角圆角半径，单位为vp。 |
| NODE\_SPAN\_BASELINE\_OFFSET = 2002 | 文本基线的偏移量属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：偏移量数值，单位为fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：偏移量数值，单位为fp。 |
| NODE\_IMAGE\_SPAN\_SRC = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE\_SPAN = 3000 | imageSpan组件图片地址属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示imageSpan的图片地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示imageSpan的图片地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置。 |
| NODE\_IMAGE\_SPAN\_VERTICAL\_ALIGNMENT = 3001 | 图片基于文本的对齐方式属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示图片基于文本的对齐方式，取[ArkUI\_ImageSpanAlignment](capi-native-type-h.md#arkui_imagespanalignment)枚举值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示图片基于文本的对齐方式，取[ArkUI\_ImageSpanAlignment](capi-native-type-h.md#arkui_imagespanalignment)枚举值。 |
| NODE\_IMAGE\_SPAN\_ALT = 3002 | imageSpan组件占位图地址属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示image组件占位图地址(不支持gif类型图源)。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示image组件占位图地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |
| NODE\_IMAGE\_SPAN\_BASELINE\_OFFSET = 3003 | imageSpan组件的基线偏移量属性，支持属性设置，属性重置和属性获取接口。偏移量数值为正数时向上偏移，负数时向下偏移，默认值0，单位为fp。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：偏移量数值，单位为fp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：偏移量数值，单位为fp。  **起始版本：** 13 |
| NODE\_IMAGE\_SPAN\_COLOR\_FILTER = 3004 | 图片滤镜效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 ~ .value[19].f32：表示滤镜矩阵数组。  .size：表示滤镜数组大小为5x4。  .object：颜色滤波器指针，参数类型为[OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)。  .object和.size参数只能二选一，不可同时设置。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 ~ .value[19].f32：表示滤镜矩阵数组。  .size：表示滤镜数组大小为5x4。  .object：颜色滤波器指针，参数类型为[OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md)。  **起始版本：** 22 |
| NODE\_IMAGE\_SPAN\_SUPPORT\_SVG2 = 3005 | 通过启用SVG新解析能力开关设置SVG解析功能支持的范围，支持属性设置，属性重置，属性获取接口。ImageSpan组件创建后，不支持动态修改该属性的值。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用SVG新解析能力开关。true：支持SVG解析新能力；false：保持原有SVG解析能力。  默认值：false  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用SVG新解析能力开关。  **起始版本：** 22 |
| NODE\_IMAGE\_SRC = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE = 4000 | [image](ts-basic-components-image.md)组件设置图片地址属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示image组件地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示image组件地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |
| NODE\_IMAGE\_OBJECT\_FIT = 4001 | 图片填充效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示图片填充效果，取[ArkUI\_ObjectFit](capi-native-type-h.md#arkui_objectfit)枚举值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示图片填充效果，取[ArkUI\_ObjectFit](capi-native-type-h.md#arkui_objectfit)枚举值。 |
| NODE\_IMAGE\_INTERPOLATION = 4002 | 图片插值效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示插值效果，取[ArkUI\_ImageInterpolation](capi-native-type-h.md#arkui_imageinterpolation)枚举值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示插值效果，取[ArkUI\_ImageInterpolation](capi-native-type-h.md#arkui_imageinterpolation)枚举值。 |
| NODE\_IMAGE\_OBJECT\_REPEAT = 4003 | 图片重复样式属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示图片重复样式，取[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)枚举值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示图片重复样式，取[ArkUI\_ImageRepeat](capi-native-type-h.md#arkui_imagerepeat)枚举值。 |
| NODE\_IMAGE\_COLOR\_FILTER = 4004 | 图片滤镜效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 ~ .value[19].f32 表示滤镜矩阵数组。  .size 表示滤镜数组大小 5x4。  .object 颜色滤波器指针，参数类型为OH\_Drawing\_ColorFilter。  .object和.size参数只能二选一，不可同时设置。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 ~ .value[19].f32 表示滤镜矩阵数组。  .size 表示滤镜数组大小 5x4。  .object 颜色滤波器指针，参数类型为OH\_Drawing\_ColorFilter。 |
| NODE\_IMAGE\_AUTO\_RESIZE = 4005 | 图源自动缩放属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示是否缩放布尔值，默认值：false。false表示关闭图源自动缩放，true表示开启图源自动缩放。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示是否缩放布尔值。 |
| NODE\_IMAGE\_ALT = 4006 | 占位图地址属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示image组件占位图地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置，不支持网络图片。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string 表示image组件占位图地址。  .object 表示 PixelMap 图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。 |
| NODE\_IMAGE\_DRAGGABLE = 4007 | 图片拖拽效果属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示是否支持拖拽，设置为true表示支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示是否支持拖拽。 |
| NODE\_IMAGE\_RENDER\_MODE = 4008 | 图片渲染模式属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 参数类型[ArkUI\_ImageRenderMode](capi-native-type-h.md#arkui_imagerendermode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 参数类型[ArkUI\_ImageRenderMode](capi-native-type-h.md#arkui_imagerendermode)。 |
| NODE\_IMAGE\_FIT\_ORIGINAL\_SIZE = 4009 | 设置图片的显示尺寸是否跟随图源尺寸，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32，设置图片的显示尺寸是否跟随图源尺寸，1表示跟随，0表示不跟随，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32，1表示图片的显示尺寸跟随图源尺寸，0表示图片的显示尺寸不跟随图源尺寸。 |
| NODE\_IMAGE\_FILL\_COLOR = 4010 | 设置填充颜色，设置后填充颜色会覆盖在图片上，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：填充色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：填充色数值，0xargb格式。 |
| NODE\_IMAGE\_RESIZABLE = 4011 | 设置图像拉伸时，可调整大小的图像选项。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 图片左部拉伸时，保持不变距离。单位vp。  .value[1].f32 图片上部拉伸时，保持不变距离。单位vp。  .value[2].f32 图片右部拉伸时，保持不变距离。单位vp。  .value[3].f32 图片下部拉伸时，保持不变距离。单位vp。与NODE\_IMAGE\_ANTIALIASED一起使用时，NODE\_IMAGE\_ANTIALIASED属性设置不生效。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32 图片左部拉伸时，保持不变距离。单位vp。  .value[1].f32 图片上部拉伸时，保持不变距离。单位vp。  .value[2].f32 图片右部拉伸时，保持不变距离。单位vp。  .value[3].f32 图片下部拉伸时，保持不变距离。单位vp。 |
| NODE\_IMAGE\_SYNC\_LOAD = 4012 | 图源同步加载属性，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示是否同步，默认值：false。false表示异步加载图片，true表示同步加载图片。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 表示是否同步。  **起始版本：** 20 |
| NODE\_IMAGE\_SOURCE\_SIZE = 4013 | 设置图片解码尺寸，仅在目标尺寸小于图源尺寸时生效。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示图片解码的宽，单位px。  .value[1].i32：表示图片解码的高，单位px。当任意参数小于等于0时，属性设置失败并返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode)函数参数异常。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示图片解码的宽，单位px。  .value[1].i32：表示图片解码的高，单位px。  **起始版本：** 21 |
| NODE\_IMAGE\_IMAGE\_MATRIX = 4014 | 设置图片的变换矩阵属性。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0...15].f32：4x4矩阵通过长度为16的浮点数数组来表示。当参数个数小于16，属性设置失败并返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode)函数参数异常；当参数个数大于16，只取前16个数据。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0...15].f32：4x4矩阵通过长度为16的浮点数数组来表示。  **起始版本：** 21 |
| NODE\_IMAGE\_MATCH\_TEXT\_DIRECTION = 4015 | 设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：图片是否跟随系统语言方向，默认值为false。false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：图片是否跟随系统语言方向。false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向。  **起始版本：** 21 |
| NODE\_IMAGE\_COPY\_OPTION = 4016 | 设置图片的拷贝方式。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：支持图片拷贝的方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)，默认值为ARKUI\_COPY\_OPTIONS\_NONE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：支持图片拷贝的方式[ArkUI\_CopyOptions](capi-native-type-h.md#arkui_copyoptions)。  **起始版本：** 21 |
| NODE\_IMAGE\_ENABLE\_ANALYZER = 4017 | 设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否为图片开启AI分析，默认值为false。false表示组件不支持AI分析，true表示组件支持AI分析。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否为图片开启AI分析。false表示组件不支持AI分析，true表示组件支持AI分析。  **起始版本：** 21 |
| NODE\_IMAGE\_DYNAMIC\_RANGE\_MODE = 4018 | 定义图片显示动态范围属性，指定图像渲染的动态范围模式（例如：SDR/HDR）。支持设置、重置和获取接口，用于匹配显示设备能力，确保图像明暗与色彩的准确呈现。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：动态范围类型[ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode)，默认值为ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：动态范围类型[ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode)。  **起始版本：** 21 |
| NODE\_IMAGE\_HDR\_BRIGHTNESS = 4019 | 定义图片HDR模式下的亮度属性，用于控制高动态范围显示的亮度参数。支持设置、重置和获取接口，确保HDR图像亮部与暗部细节的精准呈现。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：可设置的亮度值，取值范围[0, 1]。小于0和大于1.0时取1。0表示图片按照SDR亮度显示，1表示图片按照当前允许的最高HDR亮度显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：可设置的亮度值，取值范围[0, 1]。  **起始版本：** 21 |
| NODE\_IMAGE\_ORIENTATION = 4020 | 设置图像内容的显示方向。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：期望的图像内容显示方向[ArkUI\_Orientation](capi-native-type-h.md#arkui_imagerotateorientation)，默认值为ARKUI\_ORIENTATION\_UP。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：期望的图像内容显示方向[ArkUI\_Orientation](capi-native-type-h.md#arkui_imagerotateorientation)。  **起始版本：** 21 |
| NODE\_IMAGE\_SUPPORT\_SVG2 = 4021 | 通过启用SVG新解析能力开关设置SVG解析功能支持的范围，支持属性设置，属性重置，属性获取接口。Image组件创建后，不支持动态修改该属性的值。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用SVG新解析能力开关。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用SVG新解析能力开关。  **起始版本：** 21 |
| NODE\_IMAGE\_CONTENT\_TRANSITION = 4022 | 设置图像变化时的转场动效，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义转场动效，参数类型[ArkUI\_ContentTransitionEffect](i-arkui-nativemodule-arkui-contenttransitioneffect.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义转场动效，参数类型[ArkUI\_ContentTransitionEffect](i-arkui-nativemodule-arkui-contenttransitioneffect.md)。  **起始版本：** 21 |
| NODE\_IMAGE\_ALT\_PLACEHOLDER = 4023 | 支持加载过程中的占位图的配置，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：表示image组件加载过程中的占位图地址。  .object：表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置，不支持网络图片。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：表示image组件加载过程中的占位图地址。  .object：表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。  **起始版本：** 22 |
| NODE\_IMAGE\_ALT\_ERROR = 4024 | 支持加载失败时的占位图的配置，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：表示image组件加载失败时的占位图地址。  .object：表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)；  .object参数和.string参数二选一，不可同时设置，不支持网络图片。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：表示image组件加载失败时的占位图地址。  .object：表示PixelMap图片数据，参数类型为[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)。  **起始版本：** 22 |
| NODE\_IMAGE\_ANTIALIASED = 4025 | 支持设置位图图片边缘抗锯齿的配置，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示是否开启位图图片边缘抗锯齿，默认值：false。false表示不开启抗锯齿，true表示开启抗锯齿。与NODE\_IMAGE\_RESIZABLE一起使用时，该属性不生效。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示是否开启位图图片边缘抗锯齿。false表示不开启抗锯齿，true表示开启抗锯齿。  **起始版本：** 23 |
| NODE\_TOGGLE\_SELECTED\_COLOR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TOGGLE = 5000 | 组件打开状态的背景颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式。 |
| NODE\_TOGGLE\_SWITCH\_POINT\_COLOR = 5001 | Switch类型的圆形滑块颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：圆形滑块颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：圆形滑块颜色数值，0xargb格式。 |
| NODE\_TOGGLE\_VALUE = 5002 | Switch类型的开关值，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置开关的值，true表示开启。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置开关的值。 |
| NODE\_TOGGLE\_UNSELECTED\_COLOR = 5003 | 组件关闭状态的背景颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式。 |
| NODE\_LOADING\_PROGRESS\_COLOR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LOADING\_PROGRESS = 6000 | 加载进度条前景色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：前景颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：前景颜色数值，0xargb格式。 |
| NODE\_LOADING\_PROGRESS\_ENABLE\_LOADING = 6001 | LoadingProgress动画显示属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false时不显示动画，true时可以显示动画。默认值为true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：0时不显示动画，1时可以显示动画。 |
| NODE\_TEXT\_INPUT\_PLACEHOLDER = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_INPUT = 7000 | 单行文本输入框的默认提示文本内容属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认提示文本的内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认提示文本的内容。 |
| NODE\_TEXT\_INPUT\_TEXT = 7001 | 单行文本输入框的默认文本内容属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认文本的内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认文本的内容。 |
| NODE\_TEXT\_INPUT\_CARET\_COLOR = 7002 | 光标颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：光标颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：光标颜色数值，0xargb格式。 |
| NODE\_TEXT\_INPUT\_CARET\_STYLE = 7003 | 光标风格属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：光标宽度数值，单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：光标宽度数值，单位为vp。 |
| NODE\_TEXT\_INPUT\_SHOW\_UNDERLINE = 7004 | 单行文本输入框下划线属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示不展示下划线，true表示展示下划线。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：0表示不展示下划线，1表示展示下划线。 |
| NODE\_TEXT\_INPUT\_MAX\_LENGTH = 7005 | 输入框支持的最大文本数属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：最大文本数的数字，无单位。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：最大文本数的数字。 |
| NODE\_TEXT\_INPUT\_ENTER\_KEY\_TYPE = 7006 | 回车键类型属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)，默认值为ARKUI\_ENTER\_KEY\_TYPE\_DONE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)。 |
| NODE\_TEXT\_INPUT\_PLACEHOLDER\_COLOR = 7007 | 无输入时默认提示文本的颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式。 |
| NODE\_TEXT\_INPUT\_PLACEHOLDER\_FONT = 7008 | 无输入时默认提示文本的字体配置（包括大小、字重、样式、字体列表）属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32：可选字体大小数值，默认值16.0，单位为fp；  .value[1]?.i32：可选字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL；  .value[2]?.i32：可选字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL；  ?.string: 字体族内容，多个字体族之间使用逗号分隔，形如“字重；字体族1，字体族2”。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：字体大小数值，单位为fp；  .value[1].i32：字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)；  .value[2].i32：字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)；  .string: 字体族内容，多个字体族之间使用逗号分隔。 |
| NODE\_TEXT\_INPUT\_ENABLE\_KEYBOARD\_ON\_FOCUS = 7009 | 聚焦时是否绑定输入法属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示聚焦不拉起输入法，true表示拉起。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：0表示聚焦不拉起输入法，1表示拉起。 |
| NODE\_TEXT\_INPUT\_TYPE = 7010 | 输入框的类型属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：输入框类型枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)，默认值为ARKUI\_TEXTINPUT\_TYPE\_NORMAL。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：输入框类型枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)。 |
| NODE\_TEXT\_INPUT\_SELECTED\_BACKGROUND\_COLOR = 7011 | 输入框文本选中时的背景色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式。 |
| NODE\_TEXT\_INPUT\_SHOW\_PASSWORD\_ICON = 7012 | 密码输入模式时是否显示末尾图标属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示不显示图标，true表示显示图标，默认值为false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：0表示不显示图标，1表示显示图标。 |
| NODE\_TEXT\_INPUT\_EDITING = 7013 | 控制单行文本输入框编辑态属性，支持属性设置。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示退出编辑态，true表示维持现状。  属性获取方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示退出编辑态，true表示维持现状。 |
| NODE\_TEXT\_INPUT\_CANCEL\_BUTTON = 7014 | 单行文本右侧清除按钮样式属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：按钮样式[ArkUI\_CancelButtonStyle](capi-native-type-h.md#arkui_cancelbuttonstyle)，默认值为ARKUI\_CANCELBUTTON\_STYLE\_INPUT；  .value[1]?.f32：图标大小数值，单位为vp；  .value[2]?.u32：按钮图标颜色数值，0xargb格式，形如 0xFFFF0000 表示红色；  ?.string：按钮图标地址，入参内容为图片本地地址，例如 /pages/icon.png。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：按钮样式[ArkUI\_CancelButtonStyle](capi-native-type-h.md#arkui_cancelbuttonstyle)；  .value[1].f32：图标大小数值，单位为vp；  .value[2].u32：按钮图标颜色数值，0xargb格式；  .string：按钮图标地址。 |
| NODE\_TEXT\_INPUT\_TEXT\_SELECTION = 7015 | 单行文本设置文本选中并高亮的区域，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：选中文本的起始位置；  .value[1].i32：选中文本的终止位置；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：选中文本的起始位置；  .value[1].i32：选中文本的终止位置； |
| NODE\_TEXT\_INPUT\_UNDERLINE\_COLOR = 7016 | 开启下划线时，支持配置下划线颜色。主题配置的默认下划线颜色为'0x33182431'。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：typing，必填，键入时下划线颜色，0xargb类型；  .value[1].u32：normal，必填，非特殊状态时下划线颜色，0xargb类型；  .value[2].u32：error，必填，错误时下划线颜色，0xargb类型；  .value[3].u32：disable，必填，禁用时下划线颜色，0xargb类型；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：typing，键入时下划线颜色，0xargb类型；  .value[1].u32：normal，非特殊状态时下划线颜色，0xargb类型；  .value[2].u32：error，错误时下划线颜色，0xargb类型；  .value[3].u32：disable，禁用时下划线颜色，0xargb类型； |
| NODE\_TEXT\_INPUT\_ENABLE\_AUTO\_FILL = 7017 | 设置是否启用自动填充。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否启用自动填充，默认值true。  true表示启用，false表示不启用。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否启用自动填充。 |
| NODE\_TEXT\_INPUT\_CONTENT\_TYPE = 7018 | 自动填充类型。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。 |
| NODE\_TEXT\_INPUT\_PASSWORD\_RULES = 7019 | 定义生成密码的规则。在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 定义生成密码的规则。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 定义生成密码的规则。 |
| NODE\_TEXT\_INPUT\_SELECT\_ALL = 7020 | 设置当初始状态，是否全选文本。不支持内联模式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否全选文本，默认值：false。  true表示会全选文本，false表示不会全选文本。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否全选文本。 |
| NODE\_TEXT\_INPUT\_INPUT\_FILTER = 7021 | 通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 正则表达式。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 正则表达式。 |
| NODE\_TEXT\_INPUT\_STYLE = 7022 | 设置输入框为默认风格或内联输入风格。内联输入风格只支持输入框类型的枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_NORMAL。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 参数类型[ArkUI\_TextInputStyle](capi-native-type-h.md#arkui_textinputstyle)。默认值为ARKUI\_TEXTINPUT\_STYLE\_DEFAULT。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 参数类型[ArkUI\_TextInputStyle](capi-native-type-h.md#arkui_textinputstyle)。 |
| NODE\_TEXT\_INPUT\_CARET\_OFFSET = 7023 | 设置或获取光标所在位置信息。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  设置输入光标的位置。  .value[0].i32： 从字符串开始到光标所在位置的字符长度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  返回当前光标所在位置信息。在当前帧更新光标位置同时调用该接口，该接口不生效。  .value[0].i32：光标所在位置的索引值。  .value[1].f32：光标相对输入框的x坐标位值。  .value[2].f32：光标相对输入框的y坐标位值。 |
| NODE\_TEXT\_INPUT\_CONTENT\_RECT = 7024 | 获取已编辑文本内容区域相对组件的位置和大小。属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：水平方向横坐标。  .value[1].f32：竖直方向纵坐标。  .value[2].f32：内容宽度大小。  .value[3].f32：内容高度大小。 |
| NODE\_TEXT\_INPUT\_CONTENT\_LINE\_COUNT = 7025 | 获取已编辑文本内容的行数。属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].i32：已编辑文本内容行数。 |
| NODE\_TEXT\_INPUT\_SELECTION\_MENU\_HIDDEN = 7026 | 设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。默认值false。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为false时，显示系统文本选择菜单。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。 |
| NODE\_TEXT\_INPUT\_BLUR\_ON\_SUBMIT = 7027 | 设置输入框在submit状态下，触发回车键是否失焦。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否失焦。默认值true。  false表示触发回车键后不失焦，true表示触发回车键后失焦。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否失焦。 |
| NODE\_TEXT\_INPUT\_CUSTOM\_KEYBOARD = 7028 | 设置自定义键盘。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。  .value[0]?.i32：设置自定义键盘是否支持避让功能，默认值false。  true表示支持避让，false表示不支持避让。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。  .value[0].i32：设置自定义键盘是否支持避让功能。 |
| NODE\_TEXT\_INPUT\_WORD\_BREAK = 7029 | 文本断行规则属性，仅在内联输入风格编辑态生效，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。默认值ARKUI\_WORD\_BREAK\_BREAK\_WORD。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。 |
| NODE\_TEXT\_INPUT\_NUMBER\_OF\_LINES = 7031 | 设置该属性后，通过该属性计算[TextInput](ts-basic-components-textinput.md)组件的高度。 例如：设置numberOfLines为3时，组件将默认显示足够容纳3行文本内容的高度。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置numberOfLines的值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置numberOfLines的值。 |
| NODE\_TEXT\_INPUT\_LETTER\_SPACING = 7032 | 设置该属性后，通过该属性调整[TextInput](ts-basic-components-textinput.md)组件的字符间距。接口支持设置，重置以及获取该属性。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 设置[letterSpacing](ts-basic-components-text.md#letterspacing)的值，默认单位fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 获取letterSpacing的值，默认单位fp。  **起始版本：** 15 |
| NODE\_TEXT\_INPUT\_ENABLE\_PREVIEW\_TEXT = 7033 | 设置[TextInput](ts-basic-components-textinput.md)组件是否开启输入预上屏。接口支持设置，重置以及获取该属性。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置是否开启输入预上屏。默认值true。  false表示不开启输入预上屏，true表示开启输入预上屏。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 获取是否开启输入预上屏。  **起始版本：** 15 |
| NODE\_TEXT\_INPUT\_HALF\_LEADING = 7034 | 设置文本将行间距平分至行的顶部与底部。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置文本是否将行间距平分至行的顶部与底部。默认值false。  true表示将行间距平分至行的顶部与底部，false表示不平分。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置文本是否将行间距平分至行的顶部与底部。  **起始版本：** 18 |
| NODE\_TEXT\_INPUT\_KEYBOARD\_APPEARANCE = 7035 | 设置输入框拉起的键盘样式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。默认值ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE。  **起始版本：** 15 |
| NODE\_TEXT\_INPUT\_ENABLE\_FILL\_ANIMATION = 7036 | 设置是否启用自动填充动效。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用自动填充动效。  true表示启用，false表示不启用。  默认值true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用自动填充动效。启用之后，仅输入框类型的枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_PASSWORD、ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD或ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD的输入框在进行自动填充时动效可生效。  **起始版本：** 20 |
| NODE\_TEXT\_INPUT\_SHOW\_KEYBOARD\_ON\_FOCUS = 7030 | 设置输入框获取焦点时是否弹出键盘，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否弹出键盘。false表示获取焦点时不弹出键盘，true表示获取焦点时弹出键盘。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否弹出键盘。 |
| NODE\_TEXT\_INPUT\_LINE\_HEIGHT = 7037 | 设置输入框文本的高度，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本的高度的数字。默认值是自适应字体大小。设置为undefined时，文本的高度设置为5。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本的高度的数字。  **起始版本：** 20 |
| NODE\_TEXT\_INPUT\_ENABLE\_SELECTED\_DATA\_DETECTOR = 7038 | 开启选中词文本识别。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：开启选中词文本识别，true表示开启识别，false表示关闭识别。默认值：true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启选中词文本识别。  **起始版本：** 22 |
| NODE\_TEXT\_INPUT\_SHOW\_COUNTER = 7040 | 设置输入的字符数超过阈值时是否显示计数器并设置计数器样式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启计数器。值为true表示开启计数器，值为false表示不开启计数器。  .value[1]?.f32：可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]，小数时向下取整，若超出取值范围，则接口属性设置不生效。  .value[2]?.i32：输入字符超出限制时高亮边框，true表示高亮边框，false表示为不高亮边框。  .object：计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为 [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启计数器。  .value[1].f32：可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]。  .value[2].i32：输入字符超出限制时高亮边框，true表示高亮边框，false表示为不高亮边框，默认高亮。  .object：计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。  **起始版本：** 22 |
| NODE\_TEXT\_INPUT\_TEXT\_CONTENT\_CONTROLLER\_BASE = 7041 | 用于设置或获取文本输入控制器。  设置属性[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本内容基础控制器。参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。  返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .object：文本内容基础控制器。参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。  **起始版本：** 23 |
| NODE\_TEXT\_INPUT\_COMPRESS\_LEADING\_PUNCTUATION = 7044 | 设置输入字符行首标点压缩开关，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否打开行首标点压缩开关。  true表示开启行首标点压缩，false表示关闭行首标点压缩。默认值false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否打开行首标点压缩开关。  **起始版本：** 23 |
| NODE\_TEXT\_INPUT\_INCLUDE\_FONT\_PADDING = 7045 | 设置单行输入框内文字是否在首行顶部和尾行底部增加间距以避免文字截断。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置输入框内文字是否在首行顶部和尾行底部增加间距以避免文字截断。true表示开启增加间距，false表示关闭增加间距。默认值：false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否在首行顶部和尾行底部增加间距。true表示增加间距，false表示不增加间距。  **起始版本：** 23 |
| NODE\_TEXT\_INPUT\_FALLBACK\_LINE\_SPACING = 7046 | 针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：支持行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。默认值：false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。  **起始版本：** 23 |
| NODE\_TEXT\_INPUT\_DIRECTION = 7047 | 单行输入框的文本排版方向。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本的排版方向，取[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。  **起始版本：** 23 |
| NODE\_TEXT\_INPUT\_SELECTED\_DRAG\_PREVIEW\_STYLE = 7048 | 用于设置文本输入框内文本选中状态下的拖拽预览样式。  设置属性[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。  返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .object：文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。  **起始版本：** 23 |
| NODE\_TEXT\_AREA\_PLACEHOLDER = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_AREA = 8000 | 多行文本输入框的默认提示文本内容属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认提示文本的内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认提示文本的内容。 |
| NODE\_TEXT\_AREA\_TEXT = 8001 | 多行文本输入框的默认文本内容属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认文本的内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认文本的内容。 |
| NODE\_TEXT\_AREA\_MAX\_LENGTH = 8002 | 输入框支持的最大文本数属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：最大文本数的数字。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：最大文本数的数字。 |
| NODE\_TEXT\_AREA\_PLACEHOLDER\_COLOR = 8003 | 无输入时默认提示文本的颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式。 |
| NODE\_TEXT\_AREA\_PLACEHOLDER\_FONT = 8004 | 无输入时默认提示文本的字体配置（包括大小、字重、样式、字体列表）属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.f32：可选字体大小数值，默认值16.0，单位为fp；  .value[1]?.i32：可选字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL；  .value[2]?.i32：可选字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL；  ?.string: 字体族内容，多个字体族之间使用逗号分隔，形如“字重；字体族1，字体族2”。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：字体大小数值，单位为fp；  .value[1].i32：字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)；  .value[2].i32：字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)；  .string: 字体族内容，多个字体族之间使用逗号分隔。 |
| NODE\_TEXT\_AREA\_CARET\_COLOR = 8005 | 光标颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景色数值，0xargb格式。 |
| NODE\_TEXT\_AREA\_EDITING = 8006 | 控制多行文本输入框编辑态属性，支持属性设置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示退出编辑态，true表示维持现状。  属性获取方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示退出编辑态，true表示维持现状。 |
| NODE\_TEXT\_AREA\_TYPE = 8007 | 输入框的类型属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：输入框类型枚举[ArkUI\_TextAreaType](capi-native-type-h.md#arkui_textareatype)，默认值为ARKUI\_TEXTAREA\_TYPE\_NORMAL。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：输入框类型枚举[ArkUI\_TextAreaType](capi-native-type-h.md#arkui_textareatype)。 |
| NODE\_TEXT\_AREA\_SHOW\_COUNTER = 8008 | 设置输入的字符数超过阈值时是否显示计数器并设置计数器样式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启计数器，值为true时为开启。默认值false。  .value[1]?.f32：可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]，小数时向下取整，若超出取值范围，则接口属性设置不生效。  .value[2]?.i32：输入字符超出限制时是否高亮边框。true表示高亮边框，false表示不高亮边框。默认值true。  .object：计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启计数器，值为true时开启。  .value[1].f32：可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]。  .value[2].i32：输入字符超出限制时是否高亮边框，值为true时高亮边框。  .object：计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |
| NODE\_TEXT\_AREA\_SELECTION\_MENU\_HIDDEN = 8009 | 设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。默认值false。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为false时，显示系统文本选择菜单。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。 |
| NODE\_TEXT\_AREA\_BLUR\_ON\_SUBMIT = 8010 | 设置多行输入框在submit状态下，触发回车键是否失焦。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否失焦。false表示触发回车键后不失焦，true表示触发回车键后失焦。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否失焦。 |
| NODE\_TEXT\_AREA\_INPUT\_FILTER = 8011 | 通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 正则表达式。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 正则表达式。 |
| NODE\_TEXT\_AREA\_SELECTED\_BACKGROUND\_COLOR = 8012 | 设置文本选中底板颜色，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式。 |
| NODE\_TEXT\_AREA\_ENTER\_KEY\_TYPE = 8013 | 设置输入法回车键类型，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)，默认值为ARKUI\_ENTER\_KEY\_TYPE\_DONE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)。 |
| NODE\_TEXT\_AREA\_ENABLE\_KEYBOARD\_ON\_FOCUS = 8014 | 设置TextArea通过点击以外的方式获焦时，是否绑定输入法，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示聚焦不拉起输入法，true表示拉起，默认值为true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：0表示聚焦不拉起输入法，1表示拉起。 |
| NODE\_TEXT\_AREA\_CARET\_OFFSET = 8015 | 设置或获取光标所在位置信息。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  设置输入光标的位置。  .value[0].i32： 从字符串开始到光标所在位置的字符长度。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  返回当前光标所在位置信息。在当前帧更新光标位置同时调用该接口，该接口不生效。  .value[0].i32：光标所在位置的索引值。  .value[1].f32：光标相对输入框的x坐标位值。  .value[2].f32：光标相对输入框的y坐标位值。 |
| NODE\_TEXT\_AREA\_CONTENT\_RECT = 8016 | 获取已编辑文本内容区域相对组件的位置和大小。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：水平方向横坐标。  .value[1].f32：竖直方向纵坐标。  .value[2].f32：内容宽度大小。  .value[3].f32：内容高度大小。 |
| NODE\_TEXT\_AREA\_CONTENT\_LINE\_COUNT = 8017 | 获取已编辑文本内容的行数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：已编辑文本内容行数。 |
| NODE\_TEXT\_AREA\_TEXT\_SELECTION = 8018 | 组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：选中文本的起始位置；  .value[1].i32：选中文本的终止位置；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：选中文本的起始位置；  .value[1].i32：选中文本的终止位置； |
| NODE\_TEXT\_AREA\_ENABLE\_AUTO\_FILL = 8019 | 设置是否启用自动填充。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否启用自动填充，默认值true。  true表示启用，false表示不启用。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否启用自动填充。 |
| NODE\_TEXT\_AREA\_CONTENT\_TYPE = 8020 | 自动填充类型。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。 |
| NODE\_TEXT\_AREA\_NUMBER\_OF\_LINES = 8022 | 设置该属性后，通过该属性计算TextArea组件的高度。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置numberOfLines的值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置numberOfLines的值。 |
| NODE\_TEXT\_AREA\_LETTER\_SPACING = 8023 | 设置该属性后，通过该属性调整TextArea组件的字符间距。接口支持设置，重置以及获取该属性。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 设置[letterSpacing](ts-basic-components-text.md#letterspacing)的值，默认单位fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 获取[letterSpacing](ts-basic-components-text.md#letterspacing)的值，默认单位fp。  **起始版本：** 15 |
| NODE\_TEXT\_AREA\_ENABLE\_PREVIEW\_TEXT = 8024 | 设置TextArea组件是否开启输入预上屏。接口支持设置，重置以及获取该属性。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置是否开启输入预上屏。false表示不开启输入预上屏，true表示开启输入预上屏。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 获取是否开启输入预上屏。  **起始版本：** 15 |
| NODE\_TEXT\_AREA\_HALF\_LEADING = 8025 | 设置文本将行间距平分至行的顶部与底部。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置文本是否将行间距平分至行的顶部与底部。默认值false。  true表示将行间距平分至行的顶部与底部，false表示不平分。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 设置文本是否将行间距平分至行的顶部与底部。  **起始版本：** 18 |
| NODE\_TEXT\_AREA\_KEYBOARD\_APPEARANCE = 8026 | 设置输入框拉起的键盘样式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。  **起始版本：** 15 |
| NODE\_TEXT\_AREA\_MAX\_LINES = 8027 | 设置输入框内联模式编辑态时文本可显示的最大行数，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：内联输入风格编辑态时文本可显示的最大行数。内联模式下，默认值是3，  非内联模式下，默认值是+∞，不限制最大行数。设置为undefined时，最大行数设置为5。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：最大行数的数字。  **起始版本：** 20 |
| NODE\_TEXT\_AREA\_LINE\_SPACING = 8028 | 设置输入框文本的行间距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本的行间距的数字。默认值是0，单位fp。设置为undefined时，行间距设置为5。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本的行间距的数字，单位fp。  **起始版本：** 20 |
| NODE\_TEXT\_AREA\_MIN\_LINES = 8029 | 设置节点的最小行数。支持属性设置、属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：最小行数的数字。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：最小行数的数字。  **起始版本：** 20 |
| NODE\_TEXT\_AREA\_MAX\_LINES\_WITH\_SCROLL = 8030 | 设置支持滚动时节点的最大行数。支持属性设置、属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：支持滚动时的最大行数的数字。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：支持滚动时的最大行数的数字。  **起始版本：** 20 |
| NODE\_TEXT\_AREA\_SHOW\_KEYBOARD\_ON\_FOCUS = 8021 | 设置输入框获取焦点时是否弹出键盘，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否弹出键盘。默认值true。  false表示获取焦点时不弹出键盘，true表示获取焦点时弹出键盘。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否弹出键盘。 |
| NODE\_TEXT\_AREA\_LINE\_HEIGHT = 8031 | 设置输入框文本的高度，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本的高度的数字。默认值是自适应字体大小，单位fp。设置为undefined时，文本的高度设置为5。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本的高度的数字，单位fp。  **起始版本：** 20 |
| NODE\_TEXT\_AREA\_BAR\_STATE = 8032 | 定义文本输入框滚动条状态。支持属性设置、属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本控制滚动条状态。参数类型为[ArkUI\_BarState](capi-native-type-h.md#arkui_barstate)。默认值为ARKUI\_BAR\_STATE\_AUTO。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：文本控制滚动条状态。参数类型为[ArkUI\_BarState](capi-native-type-h.md#arkui_barstate)。  **起始版本：** 22 |
| NODE\_TEXT\_AREA\_ENABLE\_SELECTED\_DATA\_DETECTOR = 8033 | 开启选中词文本识别。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：开启选中词文本识别，true表示开启识别，false表示关闭识别。默认值：true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启选中词文本识别。  **起始版本：** 22 |
| NODE\_TEXT\_AREA\_SCROLL\_BAR\_COLOR = 8035 | 设置输入框滚动条颜色，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：滚动条颜色数值。0xargb类型。默认值：0x66182431，显示为灰色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：滚动条颜色数值。  **起始版本：** 22 |
| NODE\_TEXT\_AREA\_CUSTOM\_KEYBOARD = 8036 | 设置文本输入框的自定义键盘。支持属性设置、属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。  .value[0]?.i32：设置自定义键盘是否支持避让功能。  true表示支持避让，false表示不支持避让。  默认值：false  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。  .value[0].i32：设置自定义键盘是否支持避让功能。  **起始版本：** 22 |
| NODE\_TEXT\_AREA\_TEXT\_CONTENT\_CONTROLLER\_BASE = 8037 | 用于设置或获取文本区域控制器。  设置属性[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本内容基础控制器，参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。  获取属性时[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：文本内容基础控制器，参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。  **起始版本：** 23 |
| NODE\_TEXT\_AREA\_COMPRESS\_LEADING\_PUNCTUATION = 8040 | 设置输入字符行首标点压缩开关，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否打开行首标点压缩开关。  true表示开启行首标点压缩，false表示关闭行首标点压缩。默认值false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否打开行首标点压缩开关。  **起始版本：** 23 |
| NODE\_TEXT\_AREA\_INCLUDE\_FONT\_PADDING = 8041 | 设置多行输入框内文字是否在首行和尾行增加间距以避免文字截断。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置输入框内文字是否在首行和尾行增加间距以避免文字截断。true表示开启增加间距，false表示关闭增加间距。默认值：false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：输入框内文字是否在首行和尾行增加间距。true表示增加间距，false表示不增加间距。  **起始版本：** 23 |
| NODE\_TEXT\_AREA\_FALLBACK\_LINE\_SPACING = 8042 | 针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：支持行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。默认值：false。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否开启行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。  **起始版本：** 23 |
| NODE\_TEXT\_AREA\_DIRECTION = 8044 | 多行输入框的文本排版方向。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本的排版方向，取[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。  **起始版本：** 23 |
| NODE\_TEXT\_AREA\_SELECTED\_DRAG\_PREVIEW\_STYLE = 8045 | 用于设置多行文本输入框内文本选中状态下的拖拽预览样式。  设置属性[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。  返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .object：文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。  **起始版本：** 23 |
| NODE\_BUTTON\_LABEL = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_BUTTON = 9000 | button按钮的文本内容属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认文本的内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：默认文本的内容。 |
| NODE\_BUTTON\_TYPE = 9001 | Button按钮的样式属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置Button按钮的样式，参数类型[ArkUI\_ButtonType](capi-native-type-h.md#arkui_buttontype)，默认值为ARKUI\_BUTTON\_TYPE\_CAPSULE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：获取Button按钮的样式，参数类型[ArkUI\_ButtonType](capi-native-type-h.md#arkui_buttontype)，默认值为ARKUI\_BUTTON\_TYPE\_CAPSULE。 |
| NODE\_BUTTON\_MIN\_FONT\_SCALE = 9002 | Button按钮的最小字体缩放倍数属性，支持属性设置，属性重置和属性获取。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 设置Button按钮的最小字体缩放倍数，默认单位fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 获取Button按钮的最小字体缩放倍数，默认单位fp。  **起始版本：** 18 |
| NODE\_BUTTON\_MAX\_FONT\_SCALE = 9003 | Button按钮的最大字体缩放倍数属性，支持属性设置，属性重置和属性获取。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 设置Button按钮的最大字体缩放倍数，默认单位fp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 获取Button按钮的最大字体缩放倍数，默认单位fp。  **起始版本：** 18 |
| NODE\_PROGRESS\_VALUE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_PROGRESS = 10000 | 进度条的当前进度值属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度条当前值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度条当前值。 |
| NODE\_PROGRESS\_TOTAL = 10001 | 进度条的总长属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度条总长。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度条总长。 |
| NODE\_PROGRESS\_COLOR = 10002 | 进度条显示进度值的颜色属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色数值，0xargb格式。 |
| NODE\_PROGRESS\_TYPE = 10003 | 进度条的类型属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：进度条类型枚举值[ArkUI\_ProgressType](capi-native-type-h.md#arkui_progresstype)，默认值为ARKUI\_PROGRESS\_TYPE\_LINEAR。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：进度条类型枚举值[ArkUI\_ProgressType](capi-native-type-h.md#arkui_progresstype)。 |
| NODE\_PROGRESS\_LINEAR\_STYLE = 10004 | 线性进度条样式设置，支持属性设置，属性重置和属性获取接口，如果进度条类型不是线性样式则不生效。  .object：使用[ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)对象设置组件样式。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_ProgressLinearStyleOption](arkui-nativemodule-arkui-progresslinearstyleoption.md)对象获取组件样式。  **起始版本：** 15 |
| NODE\_CHECKBOX\_SELECT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX = 11000 | [CheckBox](ts-basic-components-checkbox.md)多选框是否选中，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：1表示选中，0表示不选中。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：1表示选中，0表示不选中。 |
| NODE\_CHECKBOX\_SELECT\_COLOR = 11001 | [CheckBox](ts-basic-components-checkbox.md)多选框选中状态颜色，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：多选框选中状态颜色, 类型为0xargb，如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：多选框选中状态颜色, 类型为0xargb，如0xFF1122FF。 |
| NODE\_CHECKBOX\_UNSELECT\_COLOR = 11002 | [CheckBox](ts-basic-components-checkbox.md)多选框非选中状态边框颜色，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：边框颜色, 类型为0xargb，如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：边框颜色, 类型为0xargb，如0xFF1122FF。 |
| NODE\_CHECKBOX\_MARK = 11003 | [CheckBox](ts-basic-components-checkbox.md)多选框内部图标样式，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：边框颜色, 类型为0xargb，如0xFF1122FF；  .value[1]?.f32：可选，内部图标大小，单位vp；  .value[2]?.f32：可选，内部图标粗细，单位vp，默认值2。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：边框颜色, 类型为0xargb，如0xFF1122FF；  .value[1].f32：内部图标大小，单位vp；  .value[2].f32：内部图标粗细，单位vp，默认值2。 |
| NODE\_CHECKBOX\_SHAPE = 11004 | CheckBox组件形状, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：组件形状，参数类型[ArkUI\_CheckboxShape](capi-native-type-h.md#arkui_checkboxshape)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：组件形状，参数类型[ArkUI\_CheckboxShape](capi-native-type-h.md#arkui_checkboxshape)。 |
| NODE\_CHECKBOX\_NAME = 11005 | 定义复选框的名称, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 组件名称。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 组件名称。  **起始版本：** 15 |
| NODE\_CHECKBOX\_GROUP = 11006 | 定义复选框的组的名称, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 组件名称。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 组件名称。  **起始版本：** 15 |
| NODE\_XCOMPONENT\_ID = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_XCOMPONENT = 12000 | XComponent组件ID属性，支持属性设置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: ID的内容。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: ID的内容。 |
| NODE\_XCOMPONENT\_TYPE = 12001 | XComponent组件的类型，仅支持属性获取接口。  XComponent组件的类型需要在组件创建时通过[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)中的ARKUI\_NODE\_XCOMPONENT或者ARKUI\_NODE\_XCOMPONENT\_TEXTURE明确，不允许后续修改。  使用[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口尝试修改XComponent组件的类型时会发生绘制内容异常。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：字体样式[ArkUI\_XComponentType](capi-native-type-h.md#arkui_xcomponenttype)。 |
| NODE\_XCOMPONENT\_SURFACE\_SIZE = 12002 | XComponent组件的宽高，仅支持属性获取接口。  使用[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)接口尝试修改XComponent组件的宽高时设置不会生效。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：宽数值，单位为px；  .value[1].u32：高数值，单位为px。 |
| NODE\_XCOMPONENT\_SURFACE\_RECT = 12003 | 设置XComponent组件持有Surface的显示区域，支持属性设置和获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: Surface显示区域相对于XComponent组件左上角的x轴坐标, 单位为px。  .value[1].i32: Surface显示区域相对于XComponent组件左上角的y轴坐标, 单位为px。  .value[2].i32: Surface显示区域的宽度, 单位为px。  .value[3].i32: Surface显示区域的高度, 单位为px。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: Surface显示区域相对于XComponent组件左上角的x轴坐标, 单位为px。  .value[1].i32: Surface显示区域相对于XComponent组件左上角的y轴坐标, 单位为px。  .value[2].i32: Surface显示区域的宽度, 单位为px。  .value[3].i32: Surface显示区域的高度, 单位为px。  **起始版本：** 18 |
| NODE\_XCOMPONENT\_ENABLE\_ANALYZER = 12004 | 设置XComponent组件是否支持图像分析，支持属性设置和获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 是否支持图像分析，1表示支持图像分析，0表示不支持图像分析，默认值：0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 是否支持图像分析，1表示支持图像分析，0表示不支持图像分析，默认值：0。  **起始版本：** 18 |
| NODE\_DATE\_PICKER\_LUNAR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_DATE\_PICKER = 13000 | 设置日期选择器组件的日期是否显示农历，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否显示农历，默认值false。false表示不展示农历，true表示展示农历。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否显示农历。 |
| NODE\_DATE\_PICKER\_START = 13001 | 设置日期选择器组件选择器的起始日期，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 日期，默认值"1970-1-1"。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 日期。 |
| NODE\_DATE\_PICKER\_END = 13002 | 设置日期选择器组件选择器的结束日期，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 日期，默认值"2100-12-31"。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 日期。 |
| NODE\_DATE\_PICKER\_SELECTED = 13003 | 设置日期选择器组件选中项的日期，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 日期，默认值"2024-01-22"。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 日期。 |
| NODE\_DATE\_PICKER\_DISAPPEAR\_TEXT\_STYLE = 13004 | 设置日期选择器组件的所有选项中最上和最下两个选项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_DATE\_PICKER\_TEXT\_STYLE = 13005 | 设置日期选择器组件的所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_DATE\_PICKER\_SELECTED\_TEXT\_STYLE = 13006 | 设置日期选择器组件的选中项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_DATE\_PICKER\_MODE = 13007 | 设置要显示的日期选项列。DatePicker显示不同样式的日期列，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：显示的日期列类型。参数类型[ArkUI\_DatePickerMode](capi-native-type-h.md#arkui_datepickermode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：显示的日期列类型。参数类型[ArkUI\_DatePickerMode](capi-native-type-h.md#arkui_datepickermode)。  **起始版本：** 18 |
| NODE\_DATE\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK = 13008 | 设置是否开启触控反馈。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：是否开启触控反馈。默认值：true，true表示开启触控反馈，false则表示不开启触控反馈。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32：是否开启触控反馈。  **起始版本：** 18 |
| NODE\_DATE\_PICKER\_CAN\_LOOP = 13009 | Picker组件可循环滚动属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示不可循环，true表示可循环。默认值：true，设置异常值时使用默认值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].i32：0表示不可循环，1表示可循环。  说明：可循环情况下，年份随着月份的循环滚动进行联动加减，月份随着日的循环滚动进行联动加减。  不可循环情况下，年/月/日到达本列的顶部或底部时，无法再进行滚动，年/月/日之间也无法再联动加减。  **起始版本：** 20 |
| NODE\_TIME\_PICKER\_USE\_MILITARY\_TIME = 14001 | 设置时间选择组件展示时间是否为24小时制，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否为24小时制，默认值：false。false表示展示时间为12小时制，true表示展示时间为24小时制。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 是否为24小时制。 |
| NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE = 14002 | 设置时间选择组件所有选项中最上和最下两个选项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_TIME\_PICKER\_TEXT\_STYLE = 14003 | 设置时间选择组件所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_TIME\_PICKER\_SELECTED\_TEXT\_STYLE = 14004 | 设置时间选择组件选中项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_TIME\_PICKER\_SELECTED = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TIME\_PICKER = 14000 | 设置时间选择器组件的选中项时间，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 时间。默认值：当前系统时间。格式：仅支持时、分输入（例：23:59/23-59）。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 时间。默认值：当前系统时间。格式：时、分、秒（例：23,59,1）。 |
| NODE\_TIME\_PICKER\_START = 14005 | 设置时间选择器组件的起始时间，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 时间。默认值："0:0:0"。格式：仅支持时、分输入（例：12:59/12-59）。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 时间。默认值："0:0:0"。格式：时、分、秒（例：12:59:0）。  **起始版本：** 18 |
| NODE\_TIME\_PICKER\_END = 14006 | 设置时间选择器组件的结束日期，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 时间。默认值："23:59:59"。格式：仅支持时、分输入（例：23:59/23-59）。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 时间。默认值："23:59:59"。格式：时、分、秒（例：23:59:0）。  **起始版本：** 18 |
| NODE\_TIME\_PICKER\_ENABLE\_CASCADE = 14007 | 在设置12小时制时，上午和下午的标识会根据小时数自动切换，支持属性设置、重置和获取。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 在12小时制时，设置上午和下午的标识是否会根据小时数自动切换，默认值：false。false表示不自动切换，true表示自动切换。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 在12小时制时，设置上午和下午的标识是否会根据小时数自动切换。  **起始版本：** 18 |
| NODE\_TEXT\_PICKER\_OPTION\_RANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_PICKER = 15000 | 设置滑动选择文本选择器的选择列表，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：使用的选择器类型[ArkUI\_TextPickerRangeType](capi-native-type-h.md#arkui_textpickerrangetype)，默认值为ARKUI\_TEXTPICKER\_RANGETYPE\_SINGLE；  ?.string：针对不同选择器类型有如下输入范式：  1：单列选择器，入参格式为用分号分隔的一组字符串；  2：多列选择器，支持多对纯文本字符串对，多对之间使用分号分隔，每对内部使用逗号分隔；  ?.object：针对不同选择器类型有如下输入范式：  1：单列支持图片的选择器，输入结构体为[ARKUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md)；  2：多列联动选择器，输入结构体为[ARKUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：使用的选择器类型[ArkUI\_TextPickerRangeType](capi-native-type-h.md#arkui_textpickerrangetype)；  ?.string：针对不同选择器类型有如下输出范式：  1：单列选择器，输出格式为用分号分隔的一组字符串；  2：多列选择器，输出多对纯文本字符串对，多对之间使用分号分隔，每对内部使用逗号分隔； |
| NODE\_TEXT\_PICKER\_OPTION\_SELECTED = 15001 | 设置滑动选择文本内容的组件默认选中项在数组中的索引值，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：索引值，如存在多个索引值则逐个添加。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：索引值，如存在多个索引值则逐个添加； |
| NODE\_TEXT\_PICKER\_OPTION\_VALUE = 15002 | 设置滑动选择文本内容的组件默认选中项的值，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：选中项的值，如存在多个值则逐个添加，用分号分隔。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：选中项的值，如存在多个值则逐个添加，用分号分隔； |
| NODE\_TEXT\_PICKER\_DISAPPEAR\_TEXT\_STYLE = 15003 | 设置滑动选择文本内容的组件所有选项中最上和最下两个选项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型  入参2： 文本大小，数字类型，单位fp  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")  入参4： 文本字体列表，使用 ',' 进行分割  入参5： 文本样式，字符串枚举("normal", "italic")  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型  参数2： 文本大小，数字类型，单位fp  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")  参数4： 文本字体列表，使用 ',' 进行分割  参数5： 文本样式，字符串枚举("normal", "italic")  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_TEXT\_PICKER\_TEXT\_STYLE = 15004 | 设置滑动选择文本内容的组件所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_TEXT\_PICKER\_SELECTED\_TEXT\_STYLE = 15005 | 设置滑动选择文本内容的组件选中项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型；  入参2： 文本大小，数字类型，单位fp；  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")；  入参4： 文本字体列表，使用 ',' 进行分割；  入参5： 文本样式，字符串枚举("normal", "italic")；  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string： 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型；  参数2： 文本大小，数字类型，单位fp；  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")；  参数4： 文本字体列表，使用 ',' 进行分割；  参数5： 文本样式，字符串枚举("normal", "italic")；  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |
| NODE\_TEXT\_PICKER\_SELECTED\_INDEX = 15006 | 设置滑动选择文本内容的组件默认选中项在数组中的索引值，支持属性设置，属性重置和属性获取接口。[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数类型：  .value[0...].i32：默认选中项在数组中的索引值数组。 |
| NODE\_TEXT\_PICKER\_CAN\_LOOP = 15007 | Picker组件可循环滚动属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：false表示不可循环，true表示可循环。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].i32：0表示不可循环，1表示可循环。 |
| NODE\_TEXT\_PICKER\_DEFAULT\_PICKER\_ITEM\_HEIGHT = 15008 | Picker各选择项的高度属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子项高度属性，单位为vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32：子项高度属性，单位为vp。 |
| NODE\_TEXT\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK = 15010 | 设置是否开启触控反馈。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：是否开启触控反馈。默认值：true，true表示开启触控反馈，false则表示不开启触控反馈。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32：是否开启触控反馈。  **起始版本：** 18 |
| NODE\_TEXT\_PICKER\_SELECTED\_BACKGROUND\_STYLE = 15011 | 设置选中项的背景颜色和边框圆角。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景颜色，采用 0xARGB 格式，例如，**0xFF1122FF**。  1：.value[1].f32：四个角的圆角半径，单位为VP。  2：.value[1].f32：左上角的圆角半径，单位为VP。  .value[2].f32：右上角的圆角半径，单位为VP。  .value[3].f32：左下角的圆角半径，单位为VP。  .value[4].f32：右下角的圆角半径，单位为VP。  默认值：背景颜色：0x0C182431；圆角半径：24.0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景颜色，采用 0xARGB 格式，例如，**0xFF1122FF**。  .value[1].f32：左上角的圆角半径，单位为VP。  .value[2].f32：右上角的圆角半径，单位为VP。  .value[3].f32：左下角的圆角半径，单位为VP。  .value[4].f32：右下角的圆角半径，单位为VP。  **起始版本：** 20 |
| NODE\_CALENDAR\_PICKER\_HINT\_RADIUS = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CALENDAR\_PICKER = 16000 | 设置日历选中态底板圆角半径的参数，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 日历选中态底板圆角半径，默认值：16.0，单位为vp，表示底板样式为圆形。当输入参数为0.0时表示底板样式为直角矩形；当输入参数为(0.0, 16.0)时，底板样式为圆角矩形；当输入参数为负数或大于16.0时，恢复成默认值16.0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 日历选中态底板圆角半径，默认值：16.0，单位为vp，表示底板样式为圆形。取值范围[0.0, 16.0]，其中取值为0.0表示底板样式为直角矩形。 |
| NODE\_CALENDAR\_PICKER\_SELECTED\_DATE = 16001 | 设置日历选择选中日期的参数，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32： 选中的年。  .value[1].u32： 选中的月。  .value[2].u32： 选中的日。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32： 选中的年。  .value[1].u32： 选中的月。  .value[2].u32： 选中的日。 |
| NODE\_CALENDAR\_PICKER\_EDGE\_ALIGNMENT = 16002 | 设置日历选择器与入口组件的对齐方式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 对齐方式类型，参数类型[ArkUI\_CalendarAlignment](capi-native-type-h.md#arkui_calendaralignment)。  .value[1]?.f32： 按照对齐方式对齐后，选择器相对入口组件的x轴方向相对偏移。  .value[2]?.f32： 按照对齐方式对齐后，选择器相对入口组件的y轴方向相对偏移。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 对齐方式类型，参数类型[ArkUI\_CalendarAlignment](capi-native-type-h.md#arkui_calendaralignment)。  .value[1].f32： 按照对齐方式对齐后，选择器相对入口组件的x轴方向相对偏移。  .value[2].f32： 按照对齐方式对齐后，选择器相对入口组件的y轴方向相对偏移。 |
| NODE\_CALENDAR\_PICKER\_TEXT\_STYLE = 16003 | 设置日历选择器入口区的文本颜色、字号、字体粗细。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.u32： 入口区的文本颜色。  .value[1]?.f32： 入口区的文本字号，单位为fp。  .value[2]?.i32： 入口区的文本字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32： 入口区的文本颜色。  .value[1].f32： 入口区的文本字号，单位为fp。  .value[2].i32： 入口区的文本字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |
| NODE\_CALENDAR\_PICKER\_START = 16004 | 设置日历选择器的开始日期，支持属性设置，属性重置和属性获取接口。设置属性时的参数格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  .string: 日期。值的格式如 "1970-1-1"。  获取属性时的返回值格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  .string: 日期。  **起始版本：** 18 |
| NODE\_CALENDAR\_PICKER\_END = 16005 | 设置日历选择器的结束日期，支持属性设置，属性重置和属性获取接口。设置属性时的参数格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  .string: 日期。值的格式如 "2100-12-31"。  获取属性时的返回值格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  .string: 日期。  **起始版本：** 18 |
| NODE\_CALENDAR\_PICKER\_DISABLED\_DATE\_RANGE = 16006 | 设置日历选择器的禁用日期区间，支持属性设置，属性重置和属性获取接口。设置属性时的参数格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  .string: 禁用日期区间字符串。禁用日期区间："第一个区间开始日期,第一个区间结束日期,第二个区间开始日期,第二个区间结束日期,...,第n个区间开始日期,第n个区间结束日期"。  设置的禁用日期区间格式："1910-01-01,1910-12-31,2020-01-01,2020-12-31"。  获取属性时的返回值格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  .string: 禁用日期区间字符串。  **起始版本：** 19 |
| NODE\_CALENDAR\_PICKER\_MARK\_TODAY = 16007 | 设置日历选择器在系统当前日期时，是否保持高亮显示，支持属性设置，属性重置和属性获取接口。设置属性时的参数格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  value[0].i32: 日历选择器在系统当前日期时，是否保持高亮显示，默认值：false。false表示不保持高亮显示，true表示保持高亮显示。  获取属性时的返回值格式为[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)：  value[0].i32: 日历选择器在系统当前日期时，是否保持高亮显示。  **起始版本：** 19 |
| NODE\_SLIDER\_BLOCK\_COLOR = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SLIDER = 17000 | Slider滑块的颜色，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：滑块的颜色, 类型为0xargb，如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：滑块的颜色, 类型为0xargb，如0xFF1122FF。 |
| NODE\_SLIDER\_TRACK\_COLOR = 17001 | Slider滑轨的背景颜色，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：背景颜色, 类型为0xargb，如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：背景颜色, 类型为0xargb，如0xFF1122FF。 |
| NODE\_SLIDER\_SELECTED\_COLOR = 17002 | Slider滑轨的已滑动部分颜色，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32：已滑动部分颜色, 类型为0xargb，如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：已滑动部分颜色, 类型为0xargb，如0xFF1122FF。 |
| NODE\_SLIDER\_SHOW\_STEPS = 17003 | 设置是否显示步长刻度值，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：是否显示步长刻度值，1表示显示，0表示不显示，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否显示步长刻度值，1表示显示，0表示不显示，默认值为0。 |
| NODE\_SLIDER\_BLOCK\_STYLE = 17004 | Slider滑块形状参数，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：形状参数。参数类型[ArkUI\_SliderBlockStyle](capi-native-type-h.md#arkui_sliderblockstyle)。  .string? 可选值，根据形状参数而定。  ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE: 滑块图片资源。如/pages/common/icon.png。  ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE: 滑块使用自定义形状，此时设置的滑块形状中的宽高值并不代表滑块的实际大小，而是由设置的宽高值按比例缩放，以确保滑块可以正常显示。  共有5种类型：  1.rect类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_RECTANGLE；  .value[2].f32：矩形宽度；  .value[3].f32：矩形高度；  .value[4].f32：矩形圆角宽度；  .value[5].f32：矩形圆角高度；  2.circle类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_CIRCLE；  .value[2].f32：圆形宽度；  .value[3].f32：圆形高度；  3.ellipse类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_ELLIPSE；  .value[2].f32：椭圆形宽度；  .value[3].f32：椭圆形高度；  4.path类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_PATH；  .value[2].f32：路径宽度；  .value[3].f32：路径高度；  .string：路径绘制的命令字符串；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：形状参数。参数类型[ArkUI\_SliderBlockStyle](capi-native-type-h.md#arkui_sliderblockstyle)。  .string? 可选值，根据形状参数而定。  ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE: 滑块图片资源。如/pages/common/icon.png。  ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE: 滑块使用的自定义形状。  共有5种类型：  1.rect类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_RECTANGLE；  .value[2].f32：矩形宽度；  .value[3].f32：矩形高度；  .value[4].f32：矩形圆角宽度；  .value[5].f32：矩形圆角高度；  2.circle类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_CIRCLE；  .value[2].f32：圆形宽度；  .value[3].f32：圆形高度；  3.ellipse类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_ELLIPSE；  .value[2].f32：椭圆形宽度；  .value[3].f32：椭圆形高度；  4.path类型：  .value[1].i32：裁剪类型，参数类型[ArkUI\_ShapeType](capi-native-type-h.md#arkui_shapetype)，ARKUI\_SHAPE\_TYPE\_PATH；  .value[2].f32：路径宽度；  .value[3].f32：路径高度；  .string：路径绘制的命令字符串； |
| NODE\_SLIDER\_VALUE = 17005 | slider进度值，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：进度值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度值。 |
| NODE\_SLIDER\_MIN\_VALUE = 17006 | slider最小值，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：进度值的最小值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度值的最小值。 |
| NODE\_SLIDER\_MAX\_VALUE = 17007 | slider最大值，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：进度值的最大值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：进度值的最大值。 |
| NODE\_SLIDER\_STEP = 17008 | Slider滑动步长，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：滑动步长，取值范围：[0.01, 100]。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：滑动步长，取值范围：[0.01, 100]。 |
| NODE\_SLIDER\_DIRECTION = 17009 | Slider滑动条滑动方向，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：显示样式，参数类型[ArkUI\_SliderDirection](capi-native-type-h.md#arkui_sliderdirection)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：显示样式，参数类型[ArkUI\_SliderDirection](capi-native-type-h.md#arkui_sliderdirection)。 |
| NODE\_SLIDER\_REVERSE = 17010 | Slider滑动条取值范围是否反向，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：是否反向，1表示反向，0表示不反向。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否反向，1表示反向，0表示不反向。 |
| NODE\_SLIDER\_STYLE = 17011 | Slider的滑块与滑轨显示样式，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：显示样式，参数类型[ArkUI\_SliderStyle](capi-native-type-h.md#arkui_sliderstyle)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：显示样式，参数类型[ArkUI\_SliderStyle](capi-native-type-h.md#arkui_sliderstyle)。 |
| NODE\_SLIDER\_TRACK\_THICKNESS = 17012 | Slider滑块的滑轨粗细属性，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：滑轨的粗细，单位为vp；当参数NODE\_SLIDER\_STYLE的值设置为ARKUI\_SLIDER\_STYLE\_OUT\_SET时为4.0vp，设置为ARKUI\_SLIDER\_STYLE\_IN\_SET时为20.0vp  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：滑轨的粗细，单位为vp； |
| NODE\_SLIDER\_ENABLE\_HAPTIC\_FEEDBACK = 17013 | 设置是否开启触控反馈。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：是否开启触控反馈。默认值：true，true表示开启触控反馈，false则表示不开启触控反馈。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32：是否开启触控反馈。  开启触控反馈时，需要在工程的module.json5的requestPermissions字段中增加"name": "ohos.permission.VIBRATE"，开启振动权限。  **起始版本：** 18 |
| NODE\_SLIDER\_PREFIX = 17014 | 在Slider组件的前端设置自定义组件。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object: 参数类型 [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。前缀组件将放置在Slider组件的起始位置，通常在LTR布局的左侧。  **起始版本：** 20 |
| NODE\_SLIDER\_SUFFIX = 17015 | 在Slider组件的后端设置自定义组件。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object: 参数类型 [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。后缀组件将放置在Slider组件的尾侧位置，通常在LTR布局的右侧。  **起始版本：** 20 |
| NODE\_SLIDER\_BLOCK\_LINEAR\_GRADIENT\_COLOR = 17016 | Slider滑块的颜色，支持属性设置，属性重置和属性获取。属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定相对比例位置处的渐变色颜色，设置非法颜色直接跳过：  - colors：渐变色颜色。  - stops：渐变位置。  - size：颜色个数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定相对比例位置处的渐变色颜色：  - colors：渐变色颜色。  - stops：渐变位置。  - size：颜色个数。  **起始版本：** 21 |
| NODE\_SLIDER\_TRACK\_LINEAR\_GRADIENT\_COLOR = 17017 | Slider滑轨的背景颜色，支持属性设置，属性重置和属性获取。属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定相对比例位置处的渐变色颜色，设置非法颜色直接跳过：  - colors：渐变色颜色。  - stops：渐变位置。  - size：颜色个数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定相对比例位置处的渐变色颜色：  - colors：渐变色颜色。  - stops：渐变位置。  - size：颜色个数。  **起始版本：** 21 |
| NODE\_SLIDER\_SELECTED\_LINEAR\_GRADIENT\_COLOR = 17018 | Slider滑轨的已滑动部分颜色，支持属性设置，属性重置和属性获取。属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定相对比例位置处的渐变色颜色，设置非法颜色直接跳过：  - colors：渐变色颜色。  - stops：渐变位置。  - size：颜色个数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: 参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。指定相对比例位置处的渐变色颜色：  - colors：渐变色颜色。  - stops：渐变位置。  - size：颜色个数。  **起始版本：** 21 |
| NODE\_RADIO\_CHECKED = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_RADIO = 18000 | 设置单选框的选中状态，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：单选框的选中状态，默认值false。值为true时，单选框被选中。值为false时，单选框不被选中。属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：单选框的选中状态。 |
| NODE\_RADIO\_STYLE = 18001 | 设置单选框选中状态和非选中状态的样式，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0]?.u32：开启状态底板颜色, 类型为0xargb，默认值为0xFF007DFF。  .value[1]?.u32：关闭状态描边颜色, 类型为0xargb，默认值为0xFF182431。  .value[2]?.u32：开启状态内部圆饼颜色, 类型为0xargb，默认值为0xFFFFFFFF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：开启状态底板颜色, 类型为0xargb，默认值为0xFF007DFF。  .value[1].u32：关闭状态描边颜色, 类型为0xargb，默认值为0xFF182431。  .value[2].u32：开启状态内部圆饼颜色, 类型为0xargb，默认值为0xFFFFFFF。 |
| NODE\_RADIO\_VALUE = 18002 | 设置当前单选框的值，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 单选框的值.  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 单选框的值. |
| NODE\_RADIO\_GROUP = 18003 | 设置当前单选框的所属群组名称，相同group的Radio只能有一个被选中，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 当前单选框的所属群组名称.  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 当前单选框的所属群组名称. |
| NODE\_CHECKBOX\_GROUP\_NAME = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX\_GROUP = 21000 | 定义复选框组的名称, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 组件名称。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 组件名称。  **起始版本：** 15 |
| NODE\_CHECKBOX\_GROUP\_SELECT\_ALL = 21001 | [CheckBoxGroup](ts-basic-components-checkboxgroup.md)多选框组是否全选, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32: 是否设置全选1表示选中，0表示不选中。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 1表示选中，0表示不选中。  **起始版本：** 15 |
| NODE\_CHECKBOX\_GROUP\_SELECTED\_COLOR = 21002 | [CheckBoxGroup](ts-basic-components-checkboxgroup.md)多选框选中状态颜色, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32: CheckBoxGroup多选框选中状态颜色, 0xARGB格式。例如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32: CheckBoxGroup多选框选中状态颜色, 0xARGB格式。例如0xFF1122FF。  **起始版本：** 15 |
| NODE\_CHECKBOX\_GROUP\_UNSELECTED\_COLOR = 21003 | [CheckBoxGroup](ts-basic-components-checkboxgroup.md)多选框未选中边框颜色, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32: 边框颜色, 类型为0xargb，如0xFF1122FF。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32: 边框颜色, 类型为0xargb，如0xFF1122FF。  **起始版本：** 15 |
| NODE\_CHECKBOX\_GROUP\_MARK = 21004 | [CheckBoxGroup](ts-basic-components-checkboxgroup.md)多选框内部图标样式, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].u32: 边框颜色, 类型为0xargb，如0xFF1122FF；  .value[1]?.f32: 可选，内部图标大小，单位vp；  .value[2]?.f32: 可选，内部图标粗细，单位vp，默认值2。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32: 边框颜色, 类型为0xargb，如0xFF1122FF；  .value[1]?.f32: 可选，内部图标大小，单位vp；  .value[2]?.f32: 可选，内部图标粗细，单位vp，默认值2。  **起始版本：** 15 |
| NODE\_CHECKBOX\_GROUP\_SHAPE = 21005 | [CheckBoxGroup](ts-basic-components-checkboxgroup.md)组件形状, 支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32: 组件形状，参数类型[ArkUI\_CheckboxShape](capi-native-type-h.md#arkui_checkboxshape)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 组件形状，参数类型[ArkUI\_CheckboxShape](capi-native-type-h.md#arkui_checkboxshape)。  **起始版本：** 15 |
| NODE\_STACK\_ALIGN\_CONTENT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_STACK = 1000000 | 设置子组件在容器内的对齐方式，支持属性设置，属性重置和属性获取接口。该属性与通用属性NODE\_ALIGNMENT同时设置时，后设置的属性生效。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 对齐方式，数据类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)，默认值ARKUI\_ALIGNMENT\_CENTER。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32： 对齐方式，数据类型[ArkUI\_Alignment](capi-native-type-h.md#arkui_alignment)。 |
| NODE\_SCROLL\_BAR\_DISPLAY\_MODE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SCROLL = 1002000 | 设置滚动条状态，支持属性设置，属性重置和属性获取接口。[List](ts-container-list.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 12开始支持，[Grid](ts-container-grid.md)从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-native-type-h.md#arkui_scrollbardisplaymode)，List、Grid、Scroll组件默认值为[ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_AUTO](capi-native-type-h.md#arkui_scrollbardisplaymode)，WaterFlow组件默认值为[ARKUI\_SCROLL\_BAR\_DISPLAY\_MODE\_OFF](capi-native-type-h.md#arkui_scrollbardisplaymode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：滚动条状态，数据类型[ArkUI\_ScrollBarDisplayMode](capi-native-type-h.md#arkui_scrollbardisplaymode)。 |
| NODE\_SCROLL\_BAR\_WIDTH = 1002001 | 设置滚动条的宽度，支持属性设置，属性重置和属性获取接口。[List](ts-container-list.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 12开始支持，[Grid](ts-container-grid.md)从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：滚动条宽度，单位vp，默认值4。  取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：滚动条宽度，单位vp。 |
| NODE\_SCROLL\_BAR\_COLOR = 1002002 | 设置滚动条的颜色，支持属性设置，属性重置和属性获取接口。[List](ts-container-list.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 12开始支持，[Grid](ts-container-grid.md)从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .data[0].u32：滚动条颜色，0xargb类型。默认值：0x66182431  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .data[0].u32：滚动条颜色，0xargb类型。 |
| NODE\_SCROLL\_SCROLL\_DIRECTION = 1002003 | 设置滚动方向，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：滚动方向，数据类型[ArkUI\_ScrollDirection](capi-native-type-h.md#arkui_scrolldirection)，默认值[ARKUI\_SCROLL\_DIRECTION\_VERTICAL](capi-native-type-h.md#arkui_scrolldirection)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：滚动方向，数据类型[ArkUI\_ScrollDirection](capi-native-type-h.md#arkui_scrolldirection)。 |
| NODE\_SCROLL\_EDGE\_EFFECT = 1002004 | 设置边缘滑动效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect)，Grid、Scroll、WaterFlow组件默认值为[ARKUI\_EDGE\_EFFECT\_NONE](capi-native-type-h.md#arkui_edgeeffect)，List组件默认值为[ARKUI\_EDGE\_EFFECT\_SPRING](capi-native-type-h.md#arkui_edgeeffect)；  .value[1]?.i32：可选值，组件内容大小小于组件自身时，设置是否开启滑动效果，开启为1，关闭为0，List、Grid、WaterFlow组件默认值为0，Scroll组件默认值为1；  .value[2]?.i32：边缘效果生效的方向，参数类型[ArkUI\_EffectEdge](capi-native-type-h.md#arkui_effectedge)，默认值[ARKUI\_EFFECT\_EDGE\_START](capi-native-type-h.md#arkui_effectedge) | [ARKUI\_EFFECT\_EDGE\_END](capi-native-type-h.md#arkui_effectedge)。  该参数从API version 18开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect)；  .value[1].i32：组件内容大小小于组件自身时，设置是否开启滑动效果，开启为1，关闭为0；  .value[2].i32：边缘效果生效的方向，参数类型[ArkUI\_EffectEdge](capi-native-type-h.md#arkui_effectedge)。该参数从API version 18开始支持。 |
| NODE\_SCROLL\_ENABLE\_SCROLL\_INTERACTION = 1002005 | 设置是否支持滚动手势，当设置为0时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。  List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持滚动手势，默认值1。1：支持滚动手势，0：不支持滚动手势。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持滚动手势。 |
| NODE\_SCROLL\_FRICTION = 1002006 | 设置摩擦系数，手动滑动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。  List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：摩擦系数，默认值：非可穿戴设备为0.6，可穿戴设备为0.9。取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：摩擦系数。 |
| NODE\_SCROLL\_SNAP = 1002007 | 设置[Scroll](ts-container-scroll.md)组件的限位滚动模式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Scroll组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-native-type-h.md#arkui_scrollsnapalign)，默认值[ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE](capi-native-type-h.md#arkui_scrollsnapalign)；  .value[1].i32：在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在开头和第一页间自由滑动，设置为false后，允许Scroll在开头和第一页间自由滑动，默认值true。该参数仅在限位点为多个时生效；  .value[2].i32：在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在最后一页和末尾间自由滑动，设置为false后，允许Scroll在最后一页和末尾间自由滑动，默认值true。该参数仅在限位点为多个时生效；  .value[3...].f32：Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量。可以1个或多个。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Scroll组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-native-type-h.md#arkui_scrollsnapalign)；  .value[1].i32： 在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在开头和第一页间自由滑动，设置为false后，允许Scroll在开头和第一页间自由滑动，默认值true。该参数仅在限位点为多个时生效；  .value[2].i32：在Scroll组件限位滚动模式下，该参数设置为true后，不允许Scroll在最后一页和末尾间自由滑动，设置为false后，允许Scroll在最后一页和末尾间自由滑动，默认值true。该参数仅在限位点为多个时生效；  .value[3...].f32：Scroll组件限位滚动时的限位点，限位点即为Scroll组件能滑动停靠的偏移量。 |
| NODE\_SCROLL\_NESTED\_SCROLL = 1002008 | 嵌套滚动选项，支持属性设置，属性重置和属性获取。List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：可滚动组件往末尾端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-native-type-h.md#arkui_scrollnestedmode)。  .value[1].i32：可滚动组件往起始端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-native-type-h.md#arkui_scrollnestedmode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：可滚动组件往末尾端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-native-type-h.md#arkui_scrollnestedmode)。  .value[1].i32：可滚动组件往起始端滚动时的嵌套滚动，参数类型[ArkUI\_ScrollNestedMode](capi-native-type-h.md#arkui_scrollnestedmode)。 |
| NODE\_SCROLL\_OFFSET = 1002009 | [Scroll](ts-container-scroll.md)滑动到指定位置，支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：水平滑动偏移，单位为vp。取值范围：当值小于0时按0处理，表示不带动画的滚动。值大于0表示带动画的滚动，默认滚动到起始位置后停止。可通过设置ScrollOptions中的animation参数，使滚动在越界时启动回弹动画。  .value[1].f32：垂直滑动偏移，单位为vp。取值范围：当值小于0时按0处理，表示不带动画的滚动。值大于0表示带动画的滚动，默认滚动到起始位置后停止。可通过设置animation参数，使滚动在越界时启动回弹动画。  .value[2]?.i32：可选值，滚动时长，单位为毫秒，默认值1000。  .value[3]?.i32：可选值，滚动曲线，参数类型[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)。默认值为[ARKUI\_CURVE\_EASE](capi-native-type-h.md#arkui_animationcurve)。  .value[4]?.i32：可选值，是否使能默认弹簧动效，默认值为0不使能。  .value[5]?.i32：可选值，设置动画滚动到边界是否转换为越界回弹动画，默认值为0不转换越界回弹动画。  .value[6]?.i32：可选值，设置滚动是否可以停留在越界位置，默认值为0不停留在越界位置。该参数从API version 20开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：水平滑动偏移，单位为vp。  .value[1].f32：垂直滑动偏移，单位为vp。 |
| NODE\_SCROLL\_EDGE = 1002010 | [Scroll](ts-container-scroll.md)滚动到容器边缘位置，支持属性设置，属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：容器边缘位置，参数类型[ArkUI\_ScrollEdge](capi-native-type-h.md#arkui_scrolledge)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：容器是否位于边缘，-1：表示未处于边缘，如果处于边缘状态，参数类型[ArkUI\_ScrollEdge](capi-native-type-h.md#arkui_scrolledge)。 |
| NODE\_SCROLL\_ENABLE\_PAGING = 1002011 | 设置是否支持滑动翻页，支持属性设置，属性重置和属性获取接口。如果同时设置了滑动翻页[enablePaging](ts-container-scroll.md#enablepaging11)和限位滚动[scrollSnap](ts-container-scroll.md#scrollsnap10)，则[scrollSnap](ts-container-scroll.md#scrollsnap10)优先生效，[enablePaging](ts-container-scroll.md#enablepaging11)不生效。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持滑动翻页，默认值0。0：不支持滑动翻页，1：支持滑动翻页。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持滑动翻页。0：不支持滑动翻页，1：支持滑动翻页。 |
| NODE\_SCROLL\_PAGE = 1002012 | 滚动到下一页或者上一页。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 是否向下翻页。0表示向下翻页，1表示向上翻页。  .value[1]?.i32 是否开启翻页动画效果。1有动画，0无动画。默认值：0。 |
| NODE\_SCROLL\_BY = 1002013 | 滑动指定距离。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：水平方向滚动距离，默认单位为vp;  .value[1].f32：竖直方向滚动距离，默认单位为vp。 |
| NODE\_SCROLL\_FLING = 1002014 | 滚动类组件按传入的初始速度进行惯性滚动。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：惯性滚动的初始速度，默认单位为vp/s。值设置为0，视为异常值，本次滚动不生效。如果值为正数，则向下滚动；如果值为负数，则向上滚动。  **起始版本：** 13 |
| NODE\_SCROLL\_FADING\_EDGE = 1002015 | 设置滚动类组件边缘渐隐效果。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果，默认值0。  .value[1]?.f32：边缘渐隐效果长度。单位：vp，默认值：32。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否使能边缘渐隐效果。0表示关闭边缘效果，1表示开启边缘效果。  .value[1].f32：边缘渐隐效果长度。单位：vp。  **起始版本：** 14 |
| NODE\_SCROLL\_SIZE = 1002016 | 获取滚动类组件所有子组件全展开尺寸。属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：滚动类组件所有子组件全展开的宽度，默认单位为vp。  .value[1].f32：滚动类组件所有子组件全展开的高度，默认单位为vp。  设置NODE\_PADDING、NODE\_MARGIN或NODE\_BORDER\_WIDTH后，NODE\_PADDING、NODE\_MARGIN或NODE\_BORDER\_WIDTH在单位vp转换成单位px时会进行像素取整，返回值根据取整后的值计算。  **起始版本：** 14 |
| NODE\_SCROLL\_CONTENT\_START\_OFFSET = 1002017 | 设置滚动类组件内容起始端偏移量。[List](ts-container-list.md)组件从API version 15开始支持，[Grid](ts-container-grid.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 内容起始端偏移量，单位vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 内容起始端偏移量，单位vp；  **起始版本：** 15 |
| NODE\_SCROLL\_CONTENT\_END\_OFFSET = 1002018 | 设置滚动类组件内容末尾端偏移量。[List](ts-container-list.md)组件从API version 15开始支持，[Grid](ts-container-grid.md)/[Scroll](ts-container-scroll.md)/[WaterFlow](ts-container-waterflow.md)从API version 22开始支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 内容末尾端偏移量，单位vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32： 内容末尾端偏移量，单位vp；  **起始版本：** 15 |
| NODE\_SCROLL\_FLING\_SPEED\_LIMIT = 1002019 | 限制跟手滑动结束后，Fling动效开始时的最大初始速度。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：Fling动效开始时的最大初始速度，单位：vp/s。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：Fling动效开始时的最大初始速度。  **起始版本：** 18 |
| NODE\_SCROLL\_CLIP\_CONTENT = 1002020 | 设置滚动容器的内容层裁剪区域。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：内容裁剪模式，参数类型[ArkUI\_ContentClipMode](capi-native-type-h.md#arkui_contentclipmode)。[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)组件默认值为[ARKUI\_CONTENT\_CLIP\_MODE\_BOUNDARY](capi-native-type-h.md#arkui_contentclipmode)，[List](ts-container-list.md)、[WaterFlow](ts-container-waterflow.md)组件默认值为[ARKUI\_CONTENT\_CLIP\_MODE\_CONTENT\_ONLY](capi-native-type-h.md#arkui_contentclipmode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：内容裁剪模式，参数类型[ArkUI\_ContentClipMode](capi-native-type-h.md#arkui_contentclipmode)。  **起始版本：** 18 |
| NODE\_SCROLL\_BACK\_TO\_TOP = 1002021 | 设置滚动容器是否在点击状态栏时回到顶部。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否回到顶部，1表示回到顶部，0表示保持当前位置不变，默认值：API version 18之前：0。API version 18及以后：滚动方向是水平方向时为0，是垂直方向时为1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否回到顶部。  **起始版本：** 15 |
| NODE\_SCROLL\_BAR\_MARGIN = 1002022 | 设置滚动条的边距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置滚动条起始边距，默认值为0，单位：vp。  .value[1].f32：设置滚动条末尾边距，默认值为0，单位：vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：滚动条起始边距，单位：vp。  .value[1].f32：滚动条末尾边距，单位：vp。  **起始版本：** 20 |
| NODE\_SCROLL\_MAX\_ZOOM\_SCALE = 1002023 | 设置滚动内容最大缩放比例。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置内容最大缩放比例。默认值：1  取值范围：(0, +∞)，小于或等于0时按默认值1处理。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：获取内容最大缩放比例。  **起始版本：** 20 |
| NODE\_SCROLL\_MIN\_ZOOM\_SCALE = 1002024 | 设置滚动内容最小缩放比例。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置内容最小缩放比例，默认值：1  取值范围：(0, NODE\_SCROLL\_MAX\_ZOOM\_SCALE]，小于或等于0时按默认值1处理，大于NODE\_SCROLL\_MAX\_ZOOM\_SCALE时按NODE\_SCROLL\_MAX\_ZOOM\_SCALE处理。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：获取内容最小缩放比例。  **起始版本：** 20 |
| NODE\_SCROLL\_ZOOM\_SCALE = 1002025 | 设置滚动内容缩放比例。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：设置内容缩放比例，默认值：1  取值范围：(0, +∞)，小于或等于0时按默认值1处理。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：获取内容缩放比例。  **起始版本：** 20 |
| NODE\_SCROLL\_ENABLE\_BOUNCES\_ZOOM = 1002026 | 设置是否支持过缩放回弹效果。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持过缩放回弹效果，0：不支持，1：支持。默认值：1  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持过缩放回弹效果，0：不支持，1：支持。  **起始版本：** 20 |
| NODE\_LIST\_DIRECTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST = 1003000 | 设置[List](capi-native-node-h.md#arkui_nodetype)组件排列方向。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件排列方向，数据类型[ArkUI\_Axis](capi-native-type-h.md#arkui_axis)，默认值ARKUI\_AXIS\_VERTICAL。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件排列方向，数据类型[ArkUI\_Axis](capi-native-type-h.md#arkui_axis)。 |
| NODE\_LIST\_STICKY = 1003001 | 配合[ListItemGroup](ts-container-listitemgroup.md)组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。数据类型[ArkUI\_StickyStyle](capi-native-type-h.md#arkui_stickystyle)，默认值ARKUI\_STICKY\_STYLE\_NONE。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：配合ListItemGroup组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。数据类型[ArkUI\_StickyStyle](capi-native-type-h.md#arkui_stickystyle)。 |
| NODE\_LIST\_SPACE = 1003002 | 设置列表项间距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件主轴方向的间隔。默认值0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件主轴方向的间隔。 |
| NODE\_LIST\_NODE\_ADAPTER = 1003003 | List组件适配器，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。 |
| NODE\_LIST\_CACHED\_COUNT = 1003004 | List组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：配合List组件Adapter使用，设置adapter中的缓存数量。  .value[1]?.i32：是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 15开始支持。  .value[2]?.i32: 设置List最大缓存数量，默认值与第一个参数相同。该参数从API version 22开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：adapter中的缓存数量。  .value[1].i32：是否显示缓存节点，0：不显示，1：显示。该参数从API version 15开始支持。  .value[2]?.i32: List最大缓存数量。该参数从API version 22开始支持。 |
| NODE\_LIST\_SCROLL\_TO\_INDEX = 1003005 | 滑动到指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：要滑动到的目标元素在当前容器中的索引值。  .value[1]?.i32：设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。  .value[2]?.i32：指定滑动到的元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-native-type-h.md#arkui_scrollalignment), 默认值：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-native-type-h.md#arkui_scrollalignment)。  .value[3]?.f32：额外偏移量，默认值：0，单位：vp。该参数从API version 15开始支持。 |
| NODE\_LIST\_ALIGN\_LIST\_ITEM = 1003006 | 设置List交叉轴方向宽度大于ListItem交叉轴宽度 \* lanes时，ListItem在List交叉轴方向的布局方式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：交叉轴方向的布局方式。参数类型[ArkUI\_ListItemAlign](capi-native-type-h.md#arkui_listitemalignment)。默认值：ARKUI\_LIST\_ITEM\_ALIGNMENT\_START  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：交叉轴方向的布局方式。参数类型[ArkUI\_ListItemAlign](capi-native-type-h.md#arkui_listitemalignment)。 |
| NODE\_LIST\_CHILDREN\_MAIN\_SIZE = 1003007 | 设置List子组件默认主轴尺寸。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  object：参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。 |
| NODE\_LIST\_INITIAL\_INDEX = 1003008 | 设置当前List初次加载时视口起始位置显示的item的索引值，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：当前List初次加载时视口起始位置显示的item的索引值。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：当前List初次加载时视口起始位置显示的item的索引值。 |
| NODE\_LIST\_DIVIDER = 1003009 | 设置ListItem分割线样式，默认无分割线，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：分割线颜色，0xargb类型，默认值为0x08000000；  .value[1].f32：分割线宽，默认值：0，单位vp；  .value[2].f32：分割线距离列表侧边起始端的距离，默认值：0，单位vp；  .value[3].f32：分割线距离列表侧边结束端的距离，默认值：0，单位vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：分割线颜色，0xargb类型；  .value[1].f32：分割线宽；  .value[2].f32：分割线距离列表侧边起始端的距离，单位vp；  .value[3].f32： 分割线距离列表侧边结束端的距离，单位vp。 |
| NODE\_LIST\_SCROLL\_TO\_INDEX\_IN\_GROUP = 1003010 | 滑动到指定[ListItemGroup](ts-container-listitemgroup.md)中指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：要滑动到的目标[ListItemGroup](ts-container-listitemgroup.md)在当前[List](ts-container-list.md)中的索引值。  .value[1].i32：要滑动到的目标[ListItem](ts-container-listitem.md)在[ListItemGroup](ts-container-listitemgroup.md)中的索引值。  .value[2]?.i32：设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0  .value[3]?.i32：指定滑动到的元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-native-type-h.md#arkui_scrollalignment)。默认值：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-native-type-h.md#arkui_scrollalignment)  **起始版本：** 15 |
| NODE\_LIST\_LANES = 1003011 | 设置List列数（List垂直滚动时表示列数，水平滚动时表示行数），支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：List列数，如果设置了最大最小列宽，则设置列数不生效；默认值：1，取值范围：[1, +∞)，设置异常值时使用默认值。  .value[1]?.f32：最小列宽，单位vp；  .value[2]?.f32：最大列宽，单位vp；  .value[3]?.f32：列间距，默认值：0，单位vp；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：当前List列数；  .value[1].f32： 最小列宽，单位vp；  .value[2].f32： 最大列宽，单位vp；  .value[3].f32： 列间距，单位vp。  **起始版本：** 15 |
| NODE\_LIST\_SCROLL\_SNAP\_ALIGN = 1003012 | 设置List限位对齐模式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-native-type-h.md#arkui_scrollsnapalign)，默认值[ARKUI\_SCROLL\_SNAP\_ALIGN\_NONE](capi-native-type-h.md#arkui_scrollsnapalign)；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件限位滚动时的对齐方式，数据类型[ArkUI\_ScrollSnapAlign](capi-native-type-h.md#arkui_scrollsnapalign)；  **起始版本：** 15 |
| NODE\_LIST\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION = 1003013 | 设置List显示区域外插入或删除数据是否保持可见内容位置不变。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。  **起始版本：** 15 |
| NODE\_LIST\_STACK\_FROM\_END = 1003014 | 设置List从末尾开始布局。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置List是否从末尾开始布局。0表示从顶部开始布局，1表示从末尾开始布局，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置List是否从末尾开始布局。0表示从顶部开始布局，1表示从末尾开始布局，默认值为0。  **起始版本：** 19 |
| NODE\_LIST\_FOCUS\_WRAP\_MODE = 1003015 | List组件走焦换行模式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。默认值：ARKUI\_FOCUS\_WRAP\_MODE\_DEFAULT  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32:List组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。  **起始版本：** 20 |
| NODE\_LIST\_SYNC\_LOAD = 1003016 | List组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件是否同步加载子节点。0：分帧加载，1：同步加载，默认值为1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件是否同步加载子节点。0：分帧加载，1：同步加载。  **起始版本：** 20 |
| NODE\_LIST\_SCROLL\_SNAP\_ANIMATION\_SPEED = 1003017 | List组件限位滚动动画速度，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件限位滚动动画速度，数据类型[ArkUI\_ScrollSnapAnimationSpeed](capi-native-type-h.md#arkui_scrollsnapanimationspeed)。默认值：ARKUI\_SCROLL\_SNAP\_ANIMATION\_NORMAL。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件限位滚动动画速度，数据类型[ArkUI\_ScrollSnapAnimationSpeed](capi-native-type-h.md#arkui_scrollsnapanimationspeed)。  **起始版本：** 22 |
| NODE\_LIST\_LANES\_ITEMFILLPOLICY = 1003018 | List组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)；  .value[1]?.f32：列间距，单位vp。默认值：0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)；  .value[1].f32：列间距，单位vp。  **起始版本：** 22 |
| NODE\_LIST\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING = 1003019 | 设置当前List组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件是否支持空分支。0：不支持，1：支持。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：List组件是否支持空分支。0：不支持，1：支持。  **起始版本：** 23 |
| NODE\_SWIPER\_LOOP = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SWIPER = 1001000 | Swiper是否开启循环，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制是否开启循环，0表示不循环，1表示循环，默认值为1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制是否开启循环，0表示不循环，1表示循环，默认值为1。 |
| NODE\_SWIPER\_AUTO\_PLAY = 1001001 | Swiper子组件是否自动播放，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制子组件是否自动播放，0表示不自动播放，1表示自动播放，默认值为0。  .value[1]?.i32：手指按下是否停止自动播放，0表示停止，1表示不停止，默认值为0。该参数从API version 16开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制子组件是否自动播放，0表示不自动播放，1表示自动播放，默认值为0。  .value[1].i32：手指按下是否停止自动播放，0表示停止，1表示不停止。该参数从API version 16开始支持。 |
| NODE\_SWIPER\_SHOW\_INDICATOR = 1001002 | Swiper是否显示导航点指示器，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否显示导航点指示器，0表示不显示导航点指示器，1表示显示导航点指示器，默认值为1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否显示导航点指示器，0表示不显示导航点指示器，1表示显示导航点指示器，默认值为1。 |
| NODE\_SWIPER\_INTERVAL = 1001003 | 设置Swiper自动播放时播放的时间间隔，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：使用自动播放时播放的时间间隔，单位为毫秒。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：使用自动播放时播放的时间间隔，单位为毫秒。 |
| NODE\_SWIPER\_VERTICAL = 1001004 | 设置Swiper是否为纵向滑动，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否为纵向滑动，0表示横向滑动，1表示纵向滑动，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否为纵向滑动，0表示横向滑动，1表示纵向滑动，默认值为0。 |
| NODE\_SWIPER\_DURATION = 1001005 | 设置Swiper子组件切换的动画时长，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件切换的动画时长，单位为毫秒, 默认值为400。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件切换的动画时长，单位为毫秒, 默认值为400。 |
| NODE\_SWIPER\_CURVE = 1001006 | 设置Swiper的动画曲线，支持属性设置，属性重置和属性获取接口。未设置或未重置该属性时，动画曲线为[interpolatingSpring](js-apis-curve.md#curvesinterpolatingspring10)(-1, 1, 328, 34)；设置该属性异常时，取默认值ARKUI\_CURVE\_LINEAR。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置动画曲线参数，参数类型[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)，默认值为ARKUI\_CURVE\_LINEAR。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置动画曲线参数，参数类型[ArkUI\_AnimationCurve](capi-native-type-h.md#arkui_animationcurve)，默认值为ARKUI\_CURVE\_LINEAR。 |
| NODE\_SWIPER\_ITEM\_SPACE = 1001007 | 设置Swiper子组件与子组件之间间隙，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件与子组件之间间隙数值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件与子组件之间间隙数值。 |
| NODE\_SWIPER\_INDEX = 1001008 | 设置Swiper当前在容器中显示的子组件的索引值，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件的索引值。  .value[1]?.i32：跳转动画模式，参数类型[ArkUI\_SwiperAnimationMode](capi-native-type-h.md#arkui_swiperanimationmode)。仅当次调用有效。  该参数从API version 15开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件的索引值。 |
| NODE\_SWIPER\_DISPLAY\_COUNT = 1001009 | 设置Swiper一页内元素显示个数，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：视窗内显示的子元素个数。  .value[1]?.i32：是否按组翻页，0：按子元素翻页，1：视窗内显示的子元素按组翻页，默认值：0。  .string?: 此参数只能设置为“auto”。当设置为“auto”时，value[] 参数将被忽略。  该参数从API version 19开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：视窗内显示的子元素个数。  .value[1].i32：是否按组翻页。该参数从API version 19开始支持。 |
| NODE\_SWIPER\_DISABLE\_SWIPE = 1001010 | 设置Swiper禁用组件滑动切换功能，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否禁用组件滑动切换功能，0表示不禁用滑动切换功能，1表示禁用滑动切换功能，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否禁用组件滑动切换功能，0表示不禁用滑动切换功能，1表示禁用滑动切换功能，默认值为0。 |
| NODE\_SWIPER\_SHOW\_DISPLAY\_ARROW = 1001011 | 设置Swiper是否显示导航点箭头，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置是否显示导航点箭头，参数类型[ArkUI\_SwiperArrow](capi-native-type-h.md#arkui_swiperarrow)，默认值为ARKUI\_SWIPER\_ARROW\_HIDE。  .?object：显示导航箭头时设置箭头样式，参数类型为[ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)。该参数从API version 19开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置是否显示导航点箭头，参数类型[ArkUI\_SwiperArrow](capi-native-type-h.md#arkui_swiperarrow)，  .object：箭头样式，参数类型为[ArkUI\_SwiperArrowStyle](capi-arkui-nativemodule-arkui-swiperarrowstyle.md)。该参数从API version 19开始支持。 |
| NODE\_SWIPER\_EDGE\_EFFECT\_MODE = 1001012 | 设置Swiper的边缘滑动效果，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect)，  默认值为ARKUI\_EDGE\_EFFECT\_SPRING。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: 边缘滑动效果，参数类型[ArkUI\_EdgeEffect](capi-native-type-h.md#arkui_edgeeffect)， |
| NODE\_SWIPER\_NODE\_ADAPTER = 1001013 | swiper组件适配器，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。 |
| NODE\_SWIPER\_CACHED\_COUNT = 1001014 | swiper组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：配合swiper组件Adapter使用，设置adapter中的缓存数量  .value[1]?.i32：是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 19开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：adapter中的缓存数量。  .value[1].i32：是否显示缓存节点，0：不显示，1：显示。该参数从API version 19开始支持。 |
| NODE\_SWIPER\_PREV\_MARGIN = 1001015 | 设置 Swiper 组件的前边距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：前边距数值，单位为vp，默认值为0。  .value[1]?.i32：是否忽略空白，1表示忽略空白，0表示不忽略空白。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：前边距数值，单位为vp。.value[1].i32：是否忽略空白，1表示忽略空白，0表示不忽略空白。 |
| NODE\_SWIPER\_NEXT\_MARGIN = 1001016 | 设置 Swiper 组件的后边距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：后边距数值，单位为vp，默认值为0。  .value[1]?.i32：是否忽略空白，1表示忽略空白，0表示不忽略空白。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：后边距数值，单位为vp。.value[1].i32：是否忽略空白，1表示忽略空白，0表示不忽略空白。 |
| NODE\_SWIPER\_INDICATOR = 1001017 | 设置 Swiper 组件的导航指示器类型，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置导航指示器的类型，参数类型[ArkUI\_SwiperIndicatorType](capi-native-type-h.md#arkui_swiperindicatortype)。  .object：导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT时参数类型为[ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)。  导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT时参数类型为[ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)。  ArkUI\_SwiperDigitIndicator类型从API version 19开始支持属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：导航指示器的类型，参数类型[ArkUI\_SwiperIndicatorType](capi-native-type-h.md#arkui_swiperindicatortype)。  .object：导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DOT时参数类型为[ArkUI\_SwiperIndicator](capi-arkui-nativemodule-arkui-swiperindicator.md)。  导航指示器的类型为ARKUI\_SWIPER\_INDICATOR\_TYPE\_DIGIT时参数类型为[ArkUI\_SwiperDigitIndicator](capi-arkui-nativemodule-arkui-swiperdigitindicator.md)。  ArkUI\_SwiperDigitIndicator类型从API version 19开始支持 |
| NODE\_SWIPER\_NESTED\_SCROLL = 1001018 | 设置Swiper组件和父组件的嵌套滚动模式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Swiper组件和父组件的嵌套滚动模式，参数类型[ArkUI\_SwiperNestedScrollMode](capi-native-type-h.md#arkui_swipernestedscrollmode)  默认值为：ARKUI\_SWIPER\_NESTED\_SRCOLL\_SELF\_ONLY  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Swiper组件和父组件的嵌套滚动模式，参数类型[ArkUI\_SwiperNestedScrollMode](capi-native-type-h.md#arkui_swipernestedscrollmode) |
| NODE\_SWIPER\_SWIPE\_TO\_INDEX = 1001019 | 设置swiper组件翻至指定页面。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：指定页面在Swiper中的索引值。  .value[1]?.i32：设置翻至指定页面时是否有动效。1表示有动效，0表示没有动效, 默认值：0。 |
| NODE\_SWIPER\_INDICATOR\_INTERACTIVE = 1001020 | 设置禁用组件导航点交互功能。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置禁用组件导航点交互功能，设置为true时表示导航点可交互，设置为false时表示导航点不可交互，默认值true。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置禁用组件导航点交互功能。 |
| NODE\_SWIPER\_PAGE\_FLIP\_MODE = 1001021 | 设置组件鼠标滚轮翻页模式。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置组件鼠标滚轮翻页模式，参数类型[ArkUI\_PageFlipMode](capi-native-type-h.md#arkui_pageflipmode)。  属性获取方法返回值[ArkUI\_PageFlipMode](capi-native-type-h.md#arkui_pageflipmode)格式：  .value[0].i32：鼠标滚轮翻页模式。  **起始版本：** 15 |
| NODE\_SWIPER\_AUTO\_FILL = 1001022 | 设置Swiper一页内元素显示个数根据元素最小宽度自适应，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：元素显示最小宽度，单位：vp。  .value[1]?.i32：是否按组翻页，0：按子元素翻页，1：视窗内显示的子元素按组翻页，默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：元素显示最小宽度，单位：vp。  .value[1].i32：是否按组翻页。  **起始版本：** 19 |
| NODE\_SWIPER\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION = 1001023 | 设置Swiper显示区域外插入或删除数据是否保持可见内容位置不变。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Swiper显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Swiper显示区域外插入或删除数据是否保持可见内容位置不变。0表示不保持可见内容位置，1表示保持可见内容位置，默认值为0。  **起始版本：** 20 |
| NODE\_SWIPER\_ITEMFILLPOLICY = 1001024 | Swiper组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)；  .value[1]?.i32：是否按组翻页，0：按子元素翻页，1：视窗内显示的子元素按组翻页，默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)；  .value[1].i32：是否按组翻页。  **起始版本：** 22 |
| NODE\_LIST\_ITEM\_SWIPE\_ACTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST\_ITEM = 1004000 | 设置ListItem的划出组件，支持属性设置，属性重置，属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)对象构造。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_ListItemSwipeActionOption](arkui-nativemodule-arkui-listitemswipeactionoption.md)对象构造。 |
| NODE\_LIST\_ITEM\_GROUP\_SET\_HEADER = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST\_ITEM\_GROUP = 1005000 | 设置 ListItemGroup 头部组件，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup头部组件。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup头部组件。 |
| NODE\_LIST\_ITEM\_GROUP\_SET\_FOOTER = 1005001 | 设置 ListItemGroup 尾部组件，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup尾部组件。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)对象作为ListItemGroup尾部组件。 |
| NODE\_LIST\_ITEM\_GROUP\_SET\_DIVIDER = 1005002 | 设置ListItem分割线样式，默认无分割线，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色，0xargb类型，默认值为0x08000000；  .value[1].f32：分割线宽，默认值：0，单位vp；  .value[2].f32：分割线距离列表侧边起始端的距离，默认值：0，单位vp；  .value[3].f32：分割线距离列表侧边结束端的距离，默认值：0，单位vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：颜色，0xargb类型；  .value[1].f32：分割线宽，单位vp；  .value[2].f32：分割线距离列表侧边起始端的距离，单位vp；  .value[3].f32：分割线距离列表侧边结束端的距离，单位vp。 |
| NODE\_LIST\_ITEM\_GROUP\_CHILDREN\_MAIN\_SIZE = 1005003 | 设置ListItemGroup子组件默认主轴尺寸。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  object：参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数格式为[ArkUI\_ListChildrenMainSize](capi-arkui-nativemodule-arkui-listchildrenmainsize.md)。 |
| NODE\_LIST\_ITEM\_GROUP\_NODE\_ADAPTER = 1005004 | [ListItemGroup](ts-container-listitemgroup.md)组件适配器，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。  **起始版本：** 15 |
| NODE\_COLUMN\_ALIGN\_ITEMS = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_COLUMN = 1006000 | 设置Column子组件在水平方向上的对齐格式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在水平方向上的对齐格式，数据类型[ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment)，  默认值ARKUI\_HORIZONTAL\_ALIGNMENT\_CENTER。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在水平方向上的对齐格式，数据类型[ArkUI\_HorizontalAlignment](capi-native-type-h.md#arkui_horizontalalignment)。 |
| NODE\_COLUMN\_JUSTIFY\_CONTENT = 1006001 | 设置Column子组件在垂直方向上的对齐格式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在垂直方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，  默认值ARKUI\_FLEX\_ALIGNMENT\_START。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在垂直方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)。 |
| NODE\_LINEAR\_LAYOUT\_SPACE = 1006002 | 设置Column或Row子组件的间距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件之间的间距，单位vp，默认值：0。  取值范围：[0, +∞)  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：子组件之间的间距，单位vp。  **起始版本：** 23 |
| NODE\_LINEAR\_LAYOUT\_REVERSE = 1006003 | 设置Column或Row中沿主轴方向的子组件排列是否反向，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：主轴方向的子组件排列是否反向，默认值：false。值为true时，子组件在垂直方向上反转排列。值为false时，子组件在垂直方向上正序排列。  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：主轴方向的子组件排列是否反向。  **起始版本：** 23 |
| NODE\_ROW\_ALIGN\_ITEMS = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_ROW = 1007000 | 设置Row子组件在垂直方向上的对齐格式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在垂直方向上的对齐格式，数据类型[ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment)，  默认值ARKUI\_VERTICAL\_ALIGNMENT\_CENTER。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在垂直方向上的对齐格式，数据类型[ArkUI\_VerticalAlignment](capi-native-type-h.md#arkui_verticalalignment)。 |
| NODE\_ROW\_JUSTIFY\_CONTENT = 1007001 | 设置Row子组件在水平方向上的对齐格式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在水平方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，  默认值ARKUI\_FLEX\_ALIGNMENT\_START。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在水平方向上的对齐格式，数据类型[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)。 |
| NODE\_FLEX\_OPTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_FLEX = 1008000 | 设置Flex属性，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0]?.i32：子组件在Flex容器上排列的方向[ArkUI\_FlexDirection](capi-native-type-h.md#arkui_flexdirection)，默认值为ARKUI\_FLEX\_DIRECTION\_ROW；  .value[1]?.i32：排列规则[ArkUI\_FlexWrap](capi-native-type-h.md#arkui_flexwrap)，默认值为ARKUI\_FLEX\_WRAP\_NO\_WRAP；  .value[2]?.i32：主轴上的对齐格式[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，默认值为ARKUI\_FLEX\_ALIGNMENT\_START；  .value[3]?.i32：交叉轴上的对齐格式[ArkUI\_ItemAlignment](capi-native-type-h.md#arkui_itemalignment)，默认值为ARKUI\_ITEM\_ALIGNMENT\_START；  .value[4]?.i32：交叉轴中有额外的空间时，多行内容的对齐方式[ArkUI\_FlexAlignment](capi-native-type-h.md#arkui_flexalignment)，默认值为ARKUI\_FLEX\_ALIGNMENT\_START；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：子组件在Flex容器上排列的方向的枚举值；  .value[1].i32：排列规则的枚举值；  .value[2].i32：主轴上的对齐格式的枚举值；  .value[3].i32：交叉轴上的对齐格式的枚举值；  .value[4].i32：交叉轴中有额外的空间时，多行内容的对齐方式的枚举值； |
| NODE\_FLEX\_SPACE = 1008001 | 设置Flex容器内子组件的间距，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：Flex容器主轴方向的间距，单位vp，默认值：0。  取值范围：[0, +∞)  设置异常值时，按默认值显示。  .value[1].f32：Flex容器交叉轴方向的间距，单位vp，默认值：0。  取值范围：[0, +∞)  设置异常值时，按默认值显示。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：Flex容器主轴方向的间距，单位vp。  .value[1].f32：Flex容器交叉轴方向的间距，单位vp。  **起始版本：** 23 |
| NODE\_REFRESH\_REFRESHING = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_REFRESH = 1009000 | 设置组件是否正在刷新，支持属性设置，属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：参数类型为1或者0，1表示正在刷新，0表示不在刷新。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：参数类型为1或者0，1表示正在刷新，0表示不在刷新。 |
| NODE\_REFRESH\_CONTENT = 1009001 | 设置下拉区域的自定义内容，支持属性设置和重置。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| NODE\_REFRESH\_PULL\_DOWN\_RATIO = 1009002 | 设置下拉跟手系数，支持属性设置，属性重置和属性获取接口。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：下拉跟手系数,有效值为0-1之间的值。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：下拉跟手系数,有效值为0-1之间的值。 |
| NODE\_REFRESH\_OFFSET = 1009003 | 设置触发刷新的下拉偏移量，支持属性设置，属性重置和属性获取接口。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：下拉偏移量，单位vp， 默认值：64vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：下拉偏移量，单位vp， 默认值：64vp。 |
| NODE\_REFRESH\_PULL\_TO\_REFRESH = 1009004 | 设置当下拉距离超过[refreshOffset](ts-container-refresh.md#refreshoffset12)时是否触发刷新，支持属性设置，属性重置和属性获取接口。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：是否触发刷新。支持取值为0或1，其中1为触发刷新，0为不触发刷新。默认值：1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否触发刷新，1为触发刷新，0为不触发刷新。 |
| NODE\_REFRESH\_MAX\_PULL\_DOWN\_DISTANCE = 1009005 | 设置刷新的最大下拉距离。此属性可以根据需要通过api进行属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的参数格式：  .value[0].f32：最大下拉距离，单位：vp。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .value[0].f32：最大下拉距离，单位：vp。  **起始版本：** 20 |
| NODE\_REFRESH\_PULL\_UP\_TO\_CANCEL\_REFRESH = 1009006 | 设置上划是否取消刷新。支持属性设置，属性重置和属性获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的参数格式：  .value[0].i32：上划是否取消刷新。支持取值为0或1，其中0为上划不取消刷新，1为上划取消刷新。默认值：1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)的格式：  .value[0].i32：上划是否取消刷新。0为上划不取消刷新，1为上划取消刷新。  **起始版本：** 23 |
| NODE\_WATER\_FLOW\_LAYOUT\_DIRECTION = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_WATER\_FLOW = 1010000 | 定义瀑布流组件布局主轴方向，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32 主轴方向，参数类型[ArkUI\_FlexDirection](capi-native-type-h.md#arkui_flexdirection)。默认值[ARKUI\_FLEX\_DIRECTION\_COLUMN](capi-native-type-h.md#arkui_flexdirection)  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32 主轴方向，参数类型[ArkUI\_FlexDirection](capi-native-type-h.md#arkui_flexdirection)。 |
| NODE\_WATER\_FLOW\_COLUMN\_TEMPLATE = 1010001 | 设置当前瀑布流组件布局列的数量，不设置时默认1列，支持属性设置、重置和获取。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用[columnsTemplate](ts-container-waterflow.md#columnstemplate)('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string：布局列的数量。默认值：'1fr'  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：布局列的数量。 |
| NODE\_WATER\_FLOW\_ROW\_TEMPLATE = 1010002 | 设置当前瀑布流组件布局行的数量，不设置时默认1行，支持属性设置、重置和获取。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用[rowsTemplate](ts-container-waterflow.md#rowstemplate)('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string：布局行的数量。默认值：'1fr'  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string：布局行的数量。 |
| NODE\_WATER\_FLOW\_COLUMN\_GAP = 1010003 | 设置列与列的间距，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：列与列的间距，默认值：0，单位vp。取值范围：[0, +∞)  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：列与列的间距，单位vp。 |
| NODE\_WATER\_FLOW\_ROW\_GAP = 1010004 | 设置行与行的间距，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：行与行的间距，默认值：0，单位vp。取值范围：[0, +∞)  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：行与行的间距，单位vp。 |
| NODE\_WATER\_FLOW\_SECTION\_OPTION = 1010005 | 设置FlowItem分组配置信息，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。  .object：参数格式为[ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_WaterFlowSectionOption](pi-arkui-nativemodule-arkui-waterflowsectionoption.md)。 |
| NODE\_WATER\_FLOW\_NODE\_ADAPTER = 1010006 | [WaterFlow](ts-container-waterflow.md)组件适配器，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。 |
| NODE\_WATER\_FLOW\_CACHED\_COUNT = 1010007 | [WaterFlow](ts-container-waterflow.md)组件Adapter缓存数量，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：配合waterFlow组件Adapter使用，设置adapter中的缓存数量  .value[1]?.i32：是否显示缓存节点，0：不显示，1：显示，默认值：0。该参数从API version 16开始支持。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：adapter中的缓存数量。  .value[1].i32：是否显示缓存节点，0：不显示，1：显示。该参数从API version 16开始支持。 |
| NODE\_WATER\_FLOW\_FOOTER = 1010008 | 设置瀑布流组件末尾的自定义显示组件。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| NODE\_WATER\_FLOW\_SCROLL\_TO\_INDEX = 1010009 | 滑动到指定index。开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。    属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：要滑动到的目标元素在当前容器中的索引值。  .value[1]?.i32：设置滑动到列表项在列表中的索引值时是否有动效，1表示有动效，0表示没有动效。默认值：0。  .value[2]?.i32：指定滑动到的元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-native-type-h.md#arkui_scrollalignment)。默认值为：[ARKUI\_SCROLL\_ALIGNMENT\_START](capi-native-type-h.md#arkui_scrollalignment)。  .value[3]?.f32：滑动到目标元素后的额外偏移量，默认值：0，单位：vp。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。该参数从API version 23开始支持。 |
| NODE\_WATER\_FLOW\_ITEM\_CONSTRAINT\_SIZE = 1010010 | 设置当前瀑布流子组件的约束尺寸属性，组件布局时，进行尺寸范围限制，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：最小宽度，使用-1表示不设置；  .value[1].f32：最大宽度，使用-1表示不设置；  .value[2].f32：最小高度，使用-1表示不设置；  .value[3].f32：最大高度，使用-1表示不设置；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：最小宽度，使用-1表示不设置；  .value[1].f32：最大宽度，使用-1表示不设置；  .value[2].f32：最小高度，使用-1表示不设置；  .value[3].f32：最大高度，使用-1表示不设置； |
| NODE\_WATER\_FLOW\_LAYOUT\_MODE = 1010011 | 定义瀑布流组件布局模式，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：布局模式，参数类型[ArkUI\_WaterFlowLayoutMode](capi-native-type-h.md#arkui_waterflowlayoutmode)，默认值：[ARKUI\_WATER\_FLOW\_LAYOUT\_MODE\_ALWAYS\_TOP\_DOWN](capi-native-type-h.md#arkui_waterflowlayoutmode)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：布局模式，参数类型[ArkUI\_WaterFlowLayoutMode](capi-native-type-h.md#arkui_waterflowlayoutmode)。  **起始版本：** 18 |
| NODE\_WATER\_FLOW\_SYNC\_LOAD = 1010012 | WaterFlow组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：WaterFlow组件是否同步加载子节点。0：分帧加载，1：同步加载。默认值：1  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：WaterFlow组件是否同步加载子节点。0：分帧加载，1：同步加载。  **起始版本：** 20 |
| NODE\_WATER\_FLOW\_COLUMN\_TEMPLATE\_ITEMFILLPOLICY = 1010013 | WaterFlow组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。  **起始版本：** 22 |
| NODE\_RELATIVE\_CONTAINER\_GUIDE\_LINE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_RELATIVE\_CONTAINER = 1012000 | 设置RelativeContainer容器内的辅助线，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: RelativeContainer容器内的辅助线：  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: RelativeContainer容器内的辅助线： |
| NODE\_RELATIVE\_CONTAINER\_BARRIER = 1012001 | 设置RelativeContainer容器内的屏障，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: RelativeContainer容器内的辅助线：  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: RelativeContainer容器内的屏障： |
| NODE\_GRID\_COLUMN\_TEMPLATE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID = 1013000 | 设置当前Grid组件布局列的数量，不设置时默认1列，支持属性设置、重置和获取。例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。可使用[columnsTemplate](ts-container-grid.md#columnstemplate)('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 布局列的数量。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 布局列的数量。 |
| NODE\_GRID\_ROW\_TEMPLATE = 1013001 | 设置当前Grid布局行的数量或最小行高值，不设置时默认1行，支持属性设置、重置和获取。例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。可使用[rowsTemplate](ts-container-grid.md#rowstemplate)('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .string: 布局行的数量。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .string: 布局行的数量。 |
| NODE\_GRID\_COLUMN\_GAP = 1013002 | 设置列与列的间距，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：列与列的间距，默认值：0，单位vp。取值范围：[0, +∞)  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：列与列的间距，单位vp。 |
| NODE\_GRID\_ROW\_GAP = 1013003 | 设置行与行的间距，支持属性设置、重置和获取。属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].f32：行与行的间距，默认值：0，单位vp。取值范围：[0, +∞)  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32：行与行的间距，单位vp。 |
| NODE\_GRID\_NODE\_ADAPTER = 1013004 | [Grid](ts-container-grid.md)组件适配器，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：使用[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)对象作为适配器。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)。 |
| NODE\_GRID\_CACHED\_COUNT = 1013005 | [Grid](ts-container-grid.md)组件适配器缓存数量，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：配合Grid组件适配器使用，设置[ArkUI\_NodeAdapter](capi-arkui-nativemodule-arkui-nodeadapter8h.md)的缓存数量。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件适配器的缓存数量。 |
| NODE\_GRID\_FOCUS\_WRAP\_MODE = 1013006 | [Grid](ts-container-grid.md)组件走焦换行模式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。默认值：[FOCUS\_WRAP\_MODE\_DEFAULT](capi-native-type-h.md#arkui_focuswrapmode)  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32: Grid组件走焦换行模式，参数类型[ArkUI\_FocusWrapMode](capi-native-type-h.md#arkui_focuswrapmode)。  **起始版本：** 20 |
| NODE\_GRID\_SYNC\_LOAD = 1013007 | [Grid](ts-container-grid.md)组件是否同步加载子节点，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否同步加载子节点。0：分帧加载，1：同步加载。默认值：1  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否同步加载子节点。0：分帧加载，1：同步加载。  **起始版本：** 20 |
| NODE\_GRID\_ALIGN\_ITEMS = 1013008 | 设置Grid中[GridItem](ts-container-griditem.md)的对齐方式，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid中GridItem的对齐方式，参数类型[ArkUI\_GridItemAlignment](capi-native-type-h.md#arkui_griditemalignment)。默认值：[GRID\_ITEM\_ALIGNMENT\_DEFAULT](capi-native-type-h.md#arkui_griditemalignment)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid中GridItem的对齐方式，参数类型[ArkUI\_GridItemAlignment](capi-native-type-h.md#arkui_griditemalignment)。  **起始版本：** 22 |
| NODE\_GRID\_LAYOUT\_OPTIONS = 1013009 | 设置Grid布局选项，支持属性设置，属性重置和属性获取接口。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .object：参数格式为[ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：返回值格式为[ArkUI\_GridLayoutOptions](capi-arkui-nativemodule-arkui-gridlayoutoptions.md)。  **起始版本：** 22 |
| NODE\_GRID\_COLUMN\_TEMPLATE\_ITEMFILLPOLICY = 1013010 | Grid组件的响应式列数布局策略，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：在不同断点规格下的列数，数据类型[ArkUI\_ItemFillPolicy](capi-native-type-h.md#arkui_itemfillpolicy)。  **起始版本：** 22 |
| NODE\_GRID\_EDIT\_MODE = 1013011 | Grid组件是否进入编辑模式，进入编辑模式可以通过NODE\_GRID\_ON\_ITEM\_DRAG\_START事件拖拽GridItem。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否进入编辑模式。0：不可编辑，1：可以编辑。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否进入编辑模式。0：不可编辑，1：可以编辑。  **起始版本：** 23 |
| NODE\_GRID\_DRAG\_ANIMATION = 1013012 | Grid组件是否启用GridItem拖拽动画。支持属性设置，属性重置和属性获取接口。  仅在滚动模式下（只设置NODE\_GRID\_ROW\_TEMPLATE、NODE\_GRID\_COLUMN\_TEMPLATE其中一个）支持动画。  仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否启用GridItem拖拽动画。0：不启用，1：启用。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否启用GridItem拖拽动画。0：不启用，1：启用。  **起始版本：** 23 |
| NODE\_GRID\_MULTI\_SELECTABLE = 1013013 | Grid组件是否启用鼠标框选。支持属性设置，属性重置和属性获取接口。  启用后在Grid范围内鼠标框选会触发GridItem的NODE\_GRID\_ITEM\_EVENT\_ON\_SELECT事件。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否启用鼠标框选。0：不启用，1：启用。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否启用鼠标框选。0：不启用，1：启用。  **起始版本：** 23 |
| NODE\_GRID\_SCROLL\_TO\_INDEX = 1013014 | 滑动到指定index。  开启动效时，会对经过的所有子组件进行加载和布局计算，当大量加载子组件时会导致性能问题。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：要滑动到的目标元素在当前容器中的索引值。  .value[1]?.i32：设置滑动到目标元素时是否有动效，1表示有动效，0表示没有动效。默认值：0。  .value[2]?.i32：指定滑动到的目标元素与当前容器的对齐方式，参数类型[ArkUI\_ScrollAlignment](capi-native-type-h.md#arkui_scrollalignment)。默认值：ARKUI\_SCROLL\_ALIGNMENT\_AUTO。  .value[3]?.f32：滑动到目标元素后的额外偏移量，默认值：0，单位：vp。如果值为正数，则向底部额外偏移；如果值为负数，则向顶部额外偏移。  **起始版本：** 23 |
| NODE\_GRID\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING = 1013015 | 设置当前Grid组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否支持空分支。0：不支持，1：支持。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：Grid组件是否支持空分支。0：不支持，1：支持。  **起始版本：** 23 |
| NODE\_GRID\_ITEM\_STYLE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID\_ITEM = 1014000 | 设置GridItem样式，支持属性设置，属性重置和属性获取。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：GridItem样式，参数类型[ArkUI\_GridItemStyle](capi-native-type-h.md#arkui_griditemstyle)。默认值：[GRID\_ITEM\_STYLE\_NONE](capi-native-type-h.md#arkui_griditemstyle)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：GridItem样式，参数类型[ArkUI\_GridItemStyle](capi-native-type-h.md#arkui_griditemstyle)。  **起始版本：** 22 |
| NODE\_GRID\_ITEM\_SELECTABLE = 1014001 | 设置GridItem是否可以被鼠标框选。支持属性设置，属性重置和属性获取接口。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：GridItem是否可以被鼠标框选。0：不可以，1：可以。默认值：1  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：GridItem是否可以被鼠标框选。0：不可以，1：可以。  **起始版本：** 23 |
| NODE\_GRID\_ITEM\_SELECTED = 1014002 | 设置GridItem选中状态。支持属性设置，属性重置和属性获取接口。  属性设置方法[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)参数格式：  .value[0].i32：GridItem选中状态。0：未选中，1：已选中。默认值：0  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：GridItem选中状态。0：未选中，1：已选中。  **起始版本：** 23 |
| NODE\_TEXT\_PICKER\_COLUMN\_WIDTHS = 15009 | 设置每一个选择项列宽，支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].f32: 设置的第1个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。  .value[1]?.f32: 设置的第2个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。  .value[2]?.f32: 设置的第3个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。  ...  .value[n]?.f32: 设置的第n+1个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  value[0].f32: 第1列宽度，总宽度的百分比。  value[1].f32: 第2列宽度，总宽度的百分比。  value[2].f32: 第3列宽度，总宽度的百分比。  ...  value[n].f32: 第n+1列宽度，总宽度的百分比。  **起始版本：** 18 |
| NODE\_IMAGE\_ANIMATOR\_IMAGES = ARKUI\_NODE\_IMAGE\_ANIMATOR \* MAX\_NODE\_SCOPE\_NUM = 19000 | 设置帧动画组件的图片帧信息集合。不支持动态更新。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .size：图片帧的数量；  .object：图片帧数组，参数类型为[ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)数组；  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .size：图片帧的数量；  .object：图片帧数组，参数类型为[ArkUI\_ImageAnimatorFrameInfo](pi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)数组； |
| NODE\_IMAGE\_ANIMATOR\_STATE = 19001 | 控制帧动画组件的播放状态。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制动画的播放状态，参数类型为[ArkUI\_AnimationStatus](capi-native-type-h.md#arkui_animationstatus)，默认值为初始状态。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：控制动画的播放状态，参数类型为[ArkUI\_AnimationStatus](capi-native-type-h.md#arkui_animationstatus)。 |
| NODE\_IMAGE\_ANIMATOR\_DURATION = 19002 | 设置帧动画的播放时长，当数组中任意一帧图片单独设置了duration属性后，该属性设置无效。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：播放时长，单位为毫秒，默认值1000。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：播放时长，单位为毫秒，默认值1000。 |
| NODE\_IMAGE\_ANIMATOR\_REVERSE = 19003 | 设置帧动画的播放方向。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：播放方向，0表示从第一张图片播放到最后一张，1表示从最后一张图片播放到第一张，默认值为0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：播放方向，0表示从第一张图片播放到最后一张，1表示从最后一张图片播放到第一张。 |
| NODE\_IMAGE\_ANIMATOR\_FIXED\_SIZE = 19004 | 设置图片大小是否固定为组件大小。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置图片大小是否固定为组件大小，1表示图片大小与组件大小一致。0表示每一张图片的width、height、top和left都要单独设置，默认值为1。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：设置图片大小是否固定为组件大小，1表示图片大小与组件大小一致。0表示每一张图片的width、height、top和left都要单独设置。 |
| NODE\_IMAGE\_ANIMATOR\_FILL\_MODE = 19005 | 设置帧动画在当前播放方向下，动画开始前和结束后的状态。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：当前播放方向下，动画开始前和结束后的状态，参数类型为[ArkUI\_AnimationFillMode](capi-native-type-h.md#arkui_animationfillmode)，默认值为ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：当前播放方向下，动画开始前和结束后的状态，参数类型为[ArkUI\_AnimationFillMode](capi-native-type-h.md#arkui_animationfillmode)。 |
| NODE\_IMAGE\_ANIMATOR\_ITERATION = 19006 | 设置帧动画的播放次数。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：播放次数。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：播放次数。 |
| NODE\_EMBEDDED\_COMPONENT\_WANT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_EMBEDDED\_COMPONENT = 1016000 | 定义用于启动EmbeddedAbility的want。支持属性设置。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: EmbeddedComponent的want参数。参数类型为[AbilityBase\_Want](capi-arkui-nativemodule-abilitybase-want.md)。默认值为nullptr。  **起始版本：** 20 |
| NODE\_EMBEDDED\_COMPONENT\_OPTION = 1016001 | EmbeddedComponent的选项。支持属性设置。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object: EmbeddedComponent的选项列表，参数类型为[ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md)。  **起始版本：** 20 |
| NODE\_PICKER\_OPTION\_SELECTED\_INDEX = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_PICKER | 定义选择器数据选择范围内默认选中项的索引。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：索引值。  默认值：0。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].u32：索引值。  **起始版本：** 23 |
| NODE\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK = 1018001 | 定义是否启用触感反馈。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用触感反馈。  - true：表示启用反馈。  - false：表示不启用。  默认值：true，开启后，是否存在触控反馈取决于系统硬件支持情况。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否启用反馈。  **起始版本：** 23 |
| NODE\_PICKER\_CAN\_LOOP = 1018002 | 定义选择器是否支持滚动循环。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持滚动循环。  - true：表示支持滚动循环。  - false：表示不支持。  默认值：true。  如果子组件的个数小于8个，无论设置为true还是false，都不会循环滚动。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .value[0].i32：是否支持滚动循环。值为**true**表示支持滚动循环，**false**表示不支持。  **起始版本：** 23 |
| NODE\_PICKER\_SELECTION\_INDICATOR = 1018003 | 设置选择指示器的类型和参数。支持属性设置，属性重置和属性获取接口。  属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数类型为[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)。  属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式：  .object：参数类型为[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)。  **起始版本：** 23 |

### ArkUI\_NodeEventType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeEventType
```

**描述：**

提供NativeNode组件支持的事件类型定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NODE\_TOUCH\_EVENT = 0 | 手势事件类型。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。 |
| NODE\_EVENT\_ON\_APPEAR = 1 | 挂载事件。触发该事件的条件：组件挂载显示时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_EVENT\_ON\_DISAPPEAR = 2 | 卸载事件。触发该事件的条件 ：组件卸载时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_EVENT\_ON\_AREA\_CHANGE = 3 | 组件区域变化事件触发该事件的条件：组件区域变化时触发该回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含12个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：表示过去目标元素的宽度，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示过去目标元素的高度，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[2].f32**：表示过去目标元素左上角相对父元素左上角的位置的x轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[3].f32**：表示过去目标元素左上角相对父元素左上角的位置的y轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[4].f32**：表示过去目标元素目标元素左上角相对页面左上角的位置的x轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[5].f32**：表示过去目标元素目标元素左上角相对页面左上角的位置的y轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[6].f32**：表示最新目标元素的宽度，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[7].f32**：表示最新目标元素的高度，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[8].f32**：表示最新目标元素左上角相对父元素左上角的位置的x轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[9].f32**：表示最新目标元素左上角相对父元素左上角的位置的y轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[10].f32**：表示最新目标元素目标元素左上角相对页面左上角的位置的x轴坐标，类型为number，单位vp。  **ArkUI\_NodeComponentEvent.data[11].f32**：表示最新目标元素目标元素左上角相对页面左上角的位置的y轴坐标，类型为number，单位vp。 |
| NODE\_ON\_FOCUS = 4 | 获焦事件。触发该事件的条件：组件获焦时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_ON\_BLUR = 5 | 失去焦点事件。触发该事件的条件：组件失去焦点时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_ON\_CLICK = 6 | 组件点击事件。触发该事件的条件：组件被点击时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含8个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：点击位置相对于被点击元素原始区域左上角的X坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：点击位置相对于被点击元素原始区域左上角的Y坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[2].f32**：事件时间戳。触发事件时距离系统启动的时间间隔，单位微秒。  **ArkUI\_NodeComponentEvent.data[3].i32**：事件输入设备，1表示鼠标，2表示触屏，4表示按键。  **ArkUI\_NodeComponentEvent.data[4].f32**：点击位置相对于应用窗口左上角的X坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[5].f32**：点击位置相对于应用窗口左上角的Y坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[6].f32**：点击位置相对于应用屏幕左上角的X坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[7].f32**：点击位置相对于应用屏幕左上角的Y坐标，单位vp。 |
| NODE\_ON\_TOUCH\_INTERCEPT = 7 | 组件自定义事件拦截。触发该事件的条件：组件被触摸时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。 |
| NODE\_EVENT\_ON\_VISIBLE\_AREA\_CHANGE = 8 | 组件可见区域变化事件。触发该事件的条件：组件可见面积与自身面积的比值接近设置的阈值时触发回调，注册事件前需先使用NODE\_VISIBLE\_AREA\_CHANGE\_RATIO配置阈值。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：组件可见面积与自身面积的比值与上次变化相比的情况，变大为1，变小为0。  **ArkUI\_NodeComponentEvent.data[1].f32**：触发回调时组件可见面积与自身面积的比值。 |
| NODE\_ON\_HOVER = 9 | 鼠标进入或退出组件事件。触发该事件的条件：鼠标进入或退出组件时触发回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：鼠标是否悬浮在组件上，鼠标进入时为1，退出时为0。 |
| NODE\_ON\_MOUSE = 10 | 组件点击事件。触发该事件的条件：组件被鼠标按键点击或者鼠标在组件上悬浮移动时触发该回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。 |
| NODE\_EVENT\_ON\_ATTACH = 11 | 上树事件。触发该事件的条件：组件上树时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_EVENT\_ON\_DETACH = 12 | 下树事件。触发该事件的条件：组件下树时触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_ON\_ACCESSIBILITY\_ACTIONS = 13 | 无障碍支持操作事件触发。触发该事件的条件：已设置无障碍操作类型，并进行相应操作。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数:  **ArkUI\_NodeComponentEvent.data[0].u32**: 触发回调的操作类型，参数类型[ArkUI\_AccessibilityActionType](capi-native-type-h.md#arkui_accessibilityactiontype)。 |
| NODE\_ON\_PRE\_DRAG = 14 | 在拖拽行为开始之前告诉侦听器详细的交互状态。触发该事件的条件：组件可拖拽，当长按浮起/松手/发起拖拽时，回调触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：对应[ArkUI\_PreDragStatus](capi-drag-and-drop-h.md#arkui_predragstatus)。 |
| NODE\_ON\_DRAG\_START = 15 | 用户已移动足够距离，即将发起拖拽。触发该事件的条件：长按拖动产生足够位移距离时触发。  事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)。 |
| NODE\_ON\_DRAG\_ENTER = 16 | 用户拖拽进入当前组件范围。触发该事件的条件: 拖拽对象进入监听了该事件的组件边界时触发。  事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)。 |
| NODE\_ON\_DRAG\_MOVE = 17 | 用户拖拽在当前组件范围内移动。触发该事件的条件: 拖拽对象在监听了该事件的组件范围内移动时触发。  事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)。 |
| NODE\_ON\_DRAG\_LEAVE = 18 | 用户拖拽从当前组件范围离开。触发该事件的条件: 拖拽对象离开监听了该事件的组件边界时触发。  事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)。 |
| NODE\_ON\_DROP = 19 | 当用户在组件上方松手时，该组件上可通过该回调拿到拖拽数据进行处理。触发该事件的条件: 拖拽对象并在组件上方松手时触发。  事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)。 |
| NODE\_ON\_DRAG\_END = 20 | 拖拽发起方可通过注册该回调感知拖拽结束后的结果。触发该事件的条件：用户松手，拖拽行为结束时触发。事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_DragEvent](capi-arkui-nativemodule-arkui-dragevent.md)。 |
| NODE\_ON\_KEY\_EVENT = 21 | 绑定该方法的组件获焦后，按键动作触发该回调。触发该事件的条件：由外设键盘等设备与获焦窗口交互触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  **起始版本：** 14 |
| NODE\_ON\_KEY\_PRE\_IME = 22 | 绑定该方法的组件获焦后，按键动作在响应输入法前优先触发该回调。该回调的返回值为true时，视作该按键事件已被消费，后续的事件回调（keyboardShortcut、输入法事件、onKeyEvent）会被拦截，不再触发。触发该事件的条件：由外设键盘等设备与获焦窗口交互触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  **起始版本：** 14 |
| NODE\_ON\_FOCUS\_AXIS = 23 | 绑定该方法的组件获焦后，收到焦点轴事件时触发该回调。触发该事件的条件：由游戏手柄与获焦组件交互触发此回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。  **起始版本：** 15 |
| NODE\_DISPATCH\_KEY\_EVENT = 24 | 组件按键事件重新派发事件。当组件节点接收到按键事件时，将触发此回调函数，而非将事件分发给其子节点。  当事件回调发生时，[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  **起始版本：** 15 |
| NODE\_ON\_AXIS = 25 | 绑定该方法的组件收到轴事件时触发该回调。当绑定组件接收到轴事件时，会触发该事件回调。  事件发生时，[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md) 对象中的联合类型为[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。  **起始版本：** 17 |
| NODE\_ON\_HOVER\_EVENT = 27 | 定义鼠标指针移至组件上方或远离组件时触发的事件。当鼠标指针移到组件上方或远离组件时触发该事件。  当事件回调发生时，[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合类型为[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。  **起始版本：** 17 |
| NODE\_ON\_CLICK\_EVENT = 26 | 绑定该方法的组件被点击时触发此回调。当绑定组件被点击时，将触发此事件回调。  当发生事件回调，[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合类型是[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。  **起始版本：** 18 |
| NODE\_VISIBLE\_AREA\_APPROXIMATE\_CHANGE\_EVENT = 28 | 设置限制回调间隔的NODE\_EVENT\_ON\_VISIBLE\_AREA\_CHANGE事件的回调。触发该事件的条件：组件可见面积与自身面积的比值接近设置的阈值时触发回调，注册事件前需先使用NODE\_VISIBLE\_AREA\_APPROXIMATE\_CHANGE\_RATIO 配置阈值和更新间隔。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：组件可见面积与自身面积的比值与上次变化相比的情况，变大为1，变小为0。  **ArkUI\_NodeComponentEvent.data[1].f32**：触发回调时组件可见面积与自身面积的比值。  **起始版本：** 17 |
| NODE\_ON\_HOVER\_MOVE = 29 | 定义悬浮事件。当手写笔设备指针悬停在组件内时会触发该事件。  事件回调发生时, 可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。  **起始版本：** 15 |
| NODE\_ON\_SIZE\_CHANGE = 30 | 定义尺寸变化事件。当组件尺寸发生变化时会触发该事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含4个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**: 尺寸组件变化前的宽度。  **ArkUI\_NodeComponentEvent.data[1].f32**: 尺寸组件变化前的高度。  **ArkUI\_NodeComponentEvent.data[2].f32**: 尺寸组件变化后的宽度。  **ArkUI\_NodeComponentEvent.data[3].f32**: 尺寸组件变化后的高度。  **起始版本：** 21 |
| NODE\_ON\_COASTING\_AXIS\_EVENT = 31 | 定义惯性滚动轴事件。当用户在触控板上使用双指滑动一定距离并快速抬手时，系统会根据手指抬起时的速度，按照一定的衰减曲线持续构造事件。您可以监听此类事件来处理常规滚动轴事件之后的抛滑效果。  当事件回调发生时，可以通过[OH\_ArkUI\_NodeEvent\_GetInputEvent](capi-native-node-h.md#oh_arkui_nodeevent_getinputevent)从[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获得[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)对象。并通过[OH\_ArkUI\_UIInputEvent\_GetCoastingAxisEvent](capi-ui-input-event-h.md#oh_arkui_uiinputevent_getcoastingaxisevent)从[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)对象中获取[ArkUI\_CoastingAxisEvent](capi-arkui-nativemodule-arkui-coastingaxisevent.md)对象，使用OH\_ArkUI\_CoastingAxisEvent\_XXX系列接口可以从该对象中获取更多信息。  **起始版本：** 22 |
| NODE\_ON\_CHILD\_TOUCH\_TEST = 32 | 定义子组件的预触摸测试。调用此事件以指定如何对当前组件的子组件执行触摸测试。该事件在组件被触摸时触发。  当事件回调发生时，可以通过[OH\_ArkUI\_NodeEvent\_GetTouchTestInfo](capi-native-node-h.md#oh_arkui_nodeevent_gettouchtestinfo)从[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获得[ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)对象。并通过[OH\_ArkUI\_TouchTestInfo\_GetTouchTestInfoList](capi-ui-input-event-h.md#oh_arkui_touchtestinfo_gettouchtestinfolist)从[ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)对象中获取触摸测试信息中的触摸测试信息项列表，使用[OH\_ArkUI\_TouchTestInfoItem\_GetXXX](capi-ui-input-event-h.md#oh_arkui_touchtestinfoitem_getx)系列接口可以获取更多信息。使用[OH\_ArkUI\_TouchTestInfo\_SetTouchResultStrategy](capi-ui-input-event-h.md#oh_arkui_touchtestinfo_settouchresultstrategy)设置触摸测试策略。使用[OH\_ArkUI\_TouchTestInfo\_SetTouchResultId](capi-ui-input-event-h.md#oh_arkui_touchtestinfo_settouchresultid)设置命中测试过程中需要作用的子组件。  **起始版本：** 22 |
| NODE\_TEXT\_ON\_DETECT\_RESULT\_UPDATE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT = 1000 | 文本设置TextDataDetectorConfig且识别成功时，触发onDetectResultUpdate回调。触发该事件的条件：文本设置TextDataDetectorConfig且识别成功后。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：表示文本识别的结果，Json格式。 |
| NODE\_TEXT\_SPAN\_ON\_LONG\_PRESS = 1001 | Span组件长按事件。组件被长按时触发此回调。  事件回调发生时，可从事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中获取[ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)。  **起始版本：** 20 |
| NODE\_IMAGE\_ON\_COMPLETE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE = 4000 | 图片加载成功事件。触发该事件的条件 ：图片数据加载成功和解码成功均触发该回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含9个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示加载状态，0表示数据加载成功，1表示解码成功。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示图片的宽度，单位px。  **ArkUI\_NodeComponentEvent.data[2].f32**：表示图片的高度，单位px。  **ArkUI\_NodeComponentEvent.data[3].f32**：表示当前组件的宽度，单位px。  **ArkUI\_NodeComponentEvent.data[4].f32**：表示当前组件的高度，单位px。  **ArkUI\_NodeComponentEvent.data[5].f32**：图片绘制区域相对组件X轴位置，单位px。  **ArkUI\_NodeComponentEvent.data[6].f32**：图片绘制区域相对组件Y轴位置，单位px。  **ArkUI\_NodeComponentEvent.data[7].f32**：图片绘制区域宽度，单位px。  **ArkUI\_NodeComponentEvent.data[8].f32**：图片绘制区域高度，单位px。 |
| NODE\_IMAGE\_ON\_ERROR = 4001 | 图片加载失败事件。触发该事件的条件：图片加载异常时触发该回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**错误码信息：  401: 图片路径参数异常，无法获取到图片数据。  103101: 图片格式不支持。 |
| NODE\_IMAGE\_ON\_SVG\_PLAY\_FINISH = 4002 | SVG图片动效播放完成事件。触发该事件的条件：带动效的SVG图片动画结束时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_IMAGE\_ON\_DOWNLOAD\_PROGRESS = 4003 | 定义图片下载过程中触发事件。触发该事件的条件 ：页面组件下载网页图片时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数:  **ArkUI\_NodeComponentEvent.data[0].u32**: 到目前为止已下载的字节数。  **ArkUI\_NodeComponentEvent.data[1].u32**: 要下载图片的总字节数。 |
| NODE\_TOGGLE\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TOGGLE = 5000 | 开关状态发生变化时触发给事件。触发该事件的条件：开关状态发生变化。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：当前开关状态，1表示开，0表示关。 |
| NODE\_TEXT\_INPUT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_INPUT = 7000 | TextInput输入内容发生变化时触发该事件。触发该事件的条件：输入内容发生变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：输入的文本内容。 |
| NODE\_TEXT\_INPUT\_ON\_SUBMIT = 7001 | TextInput按下输入法回车键触发该事件。触发该事件的条件：按下输入法回车键。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：输入法回车键类型。 |
| NODE\_TEXT\_INPUT\_ON\_CUT = 7002 | 长按输入框内部区域弹出剪贴板后，点击剪切板剪切按钮，触发该回调。触发该事件的条件：长按输入框内部区域弹出剪贴板后，点击剪切板剪切按钮。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：剪切的文本内容。 |
| NODE\_TEXT\_INPUT\_ON\_PASTE = 7003 | 长按输入框内部区域弹出剪贴板后，点击剪切板粘贴按钮，触发该回调。触发该事件的条件：长按输入框内部区域弹出剪贴板后，点击剪切板粘贴按钮。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：粘贴的文本内容。 |
| NODE\_TEXT\_INPUT\_ON\_TEXT\_SELECTION\_CHANGE = 7004 | 文本选择的位置发生变化时，触发该回调。触发该事件的条件：文本选择的位置发生变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示所选文本的起始位置。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示所选文本的结束位置。 |
| NODE\_TEXT\_INPUT\_ON\_EDIT\_CHANGE = 7005 | 输入状态变化时，触发该回调。触发该事件的条件：输入状态变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：true表示正在输入。 |
| NODE\_TEXT\_INPUT\_ON\_INPUT\_FILTER\_ERROR = 7006 | 设置NODE\_TEXT\_INPUT\_INPUT\_FILTER，正则匹配失败时触发。触发该事件的条件：正则匹配失败时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：表示正则匹配失败时，被过滤的内容。 |
| NODE\_TEXT\_INPUT\_ON\_CONTENT\_SCROLL = 7007 | 文本内容滚动时，触发该回调。触发该事件的条件：文本内容滚动时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示文本在内容区的横坐标偏移。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示文本在内容区的纵坐标偏移。 |
| NODE\_TEXT\_INPUT\_ON\_CONTENT\_SIZE\_CHANGE = 7008 | TextInput输入内容发生变化时触发该事件。触发该事件的条件：输入内容发生变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：表示文本的宽度。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示文本的高度。 |
| NODE\_TEXT\_INPUT\_ON\_WILL\_INSERT = 7009 | 定义在将要输入时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过[OH\_ArkUI\_NodeEvent\_GetNumberValue](capi-native-node-h.md#oh_arkui_nodeevent_getnumbervalue)获取到index为0的value.f32：插入的值的位置信息。  通过[OH\_ArkUI\_NodeEvent\_GetStringValue](capi-native-node-h.md#oh_arkui_nodeevent_getstringvalue)获取到index为0的buffer字符串：插入的值。 |
| NODE\_TEXT\_INPUT\_ON\_DID\_INSERT = 7010 | 定义在输入完成时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过[OH\_ArkUI\_NodeEvent\_GetNumberValue](capi-native-node-h.md#oh_arkui_nodeevent_getnumbervalue)获取到index为0的value.f32：插入的值的位置信息。  通过[OH\_ArkUI\_NodeEvent\_GetStringValue](capi-native-node-h.md#oh_arkui_nodeevent_getstringvalue)获取到index为0的buffer字符串：插入的值。 |
| NODE\_TEXT\_INPUT\_ON\_WILL\_DELETE = 7011 | 定义在将要删除时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过[OH\_ArkUI\_NodeEvent\_GetNumberValue](capi-native-node-h.md#oh_arkui_nodeevent_getnumbervalue)获取到index为0的value.f32：删除的值的位置信息。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为1的value.i32：删除值的方向，0为向后删除，1为向前删除。  通过[OH\_ArkUI\_NodeEvent\_GetStringValue](capi-native-node-h.md#oh_arkui_nodeevent_getstringvalue)获取到index为0的buffer字符串：删除的值。 |
| NODE\_TEXT\_INPUT\_ON\_DID\_DELETE = 7012 | 定义在删除完成时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过[OH\_ArkUI\_NodeEvent\_GetNumberValue](capi-native-node-h.md#oh_arkui_nodeevent_getnumbervalue)获取到index为0的value.f32：删除的值的位置信息。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为1的value.i32：删除值的方向，0为向后删除，1为向前删除。  通过[OH\_ArkUI\_NodeEvent\_GetStringValue](capi-native-node-h.md#oh_arkui_nodeevent_getstringvalue)获取到index为0的buffer字符串：删除的值。 |
| NODE\_TEXT\_INPUT\_ON\_CHANGE\_WITH\_PREVIEW\_TEXT = 7013 | 定义TextInput组件在内容改变时（包含预上屏内容），触发回调的枚举值。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)。  [ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)包含参数：  **ArkUI\_TextChangeEvent.pStr**: TextInput的内容。  **ArkUI\_TextChangeEvent.pExtendStr**: TextInput的预上屏内容。  **ArkUI\_TextChangeEvent.number**: TextInput的预上屏起始位置。  **起始版本：** 15 |
| NODE\_TEXT\_INPUT\_ON\_WILL\_CHANGE = 7014 | 定义TextInput组件在内容将要改变时（包含预上屏内容），触发回调的枚举值。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)。  [ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)包含参数：  **ArkUI\_TextChangeEvent.pStr**：TextInput的内容。  **ArkUI\_TextChangeEvent.pExtendStr**：TextInput的预上屏内容。  **ArkUI\_TextChangeEvent.number**：TextInput的预上屏起始位置。  **起始版本：** 20 |
| NODE\_TEXT\_AREA\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_AREA = 8000 | 输入内容发生变化时，触发该回调。触发该事件的条件：输入内容发生变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：当前输入的文本内容。 |
| NODE\_TEXT\_AREA\_ON\_PASTE = 8001 | 长按输入框内部区域弹出剪贴板后，点击剪切板粘贴按钮，触发该回调。触发该事件的条件：长按输入框内部区域弹出剪贴板后，点击剪切板粘贴按钮。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：粘贴的文本内容。 |
| NODE\_TEXT\_AREA\_ON\_TEXT\_SELECTION\_CHANGE = 8002 | 文本选择的位置发生变化时，触发该回调。触发该事件的条件：文本选择的位置发生变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示所选文本的起始位置。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示所选文本的结束位置。 |
| NODE\_TEXT\_AREA\_ON\_EDIT\_CHANGE = 8003 | 输入状态变化时，触发该回调。触发该事件的条件：输入状态变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：true表示正在输入。 |
| NODE\_TEXT\_AREA\_ON\_SUBMIT = 8004 | TextArea按下输入法回车键触发该事件。触发该事件的条件：按下输入法回车键。keyType为ARKUI\_ENTER\_KEY\_TYPE\_NEW\_LINE时不触发  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：输入法回车键类型。 |
| NODE\_TEXT\_AREA\_ON\_INPUT\_FILTER\_ERROR = 8005 | 设置NODE\_TEXT\_AREA\_INPUT\_FILTER，正则匹配失败时触发。触发该事件的条件：正则匹配失败时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  [ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)中包含1个参数：  **ArkUI\_StringAsyncEvent.pStr**：表示正则匹配失败时，被过滤的内容。 |
| NODE\_TEXT\_AREA\_ON\_CONTENT\_SCROLL = 8006 | 文本内容滚动时，触发该回调。触发该事件的条件：文本内容滚动时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示文本在内容区的横坐标偏移。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示文本在内容区的纵坐标偏移。 |
| NODE\_TEXT\_AREA\_ON\_CONTENT\_SIZE\_CHANGE = 8007 | TextArea输入内容发生变化时触发该事件。触发该事件的条件：输入内容发生变化时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：表示文本的宽度。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示文本的高度。 |
| NODE\_TEXT\_AREA\_ON\_WILL\_INSERT = 8008 | 定义在将要输入时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为0的value.f32：插入的值的位置信息。  通过OH\_ArkUI\_NodeEvent\_GetStringValue获取到index为0的buffer字符串：插入的值。 |
| NODE\_TEXT\_AREA\_ON\_DID\_INSERT = 8009 | 定义在输入完成时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为0的value.f32：插入的值的位置信息。  通过OH\_ArkUI\_NodeEvent\_GetStringValue获取到index为0的buffer字符串：插入的值。 |
| NODE\_TEXT\_AREA\_ON\_WILL\_DELETE = 8010 | 定义在将要删除时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为0的value.f32：删除的值的位置信息。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为1的value.i32：删除值的方向，0为向后删除，1为向前删除。  通过OH\_ArkUI\_NodeEvent\_GetStringValue获取到index为0的buffer字符串：删除的值。 |
| NODE\_TEXT\_AREA\_ON\_DID\_DELETE = 8011 | 定义在删除完成时，触发回调的枚举值。事件回调发生时，事件参数为[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为0的value.f32：删除的值的位置信息。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为1的value.i32：删除值的方向，0为向后删除，1为向前删除。  通过OH\_ArkUI\_NodeEvent\_GetStringValue获取到index为0的buffer字符串：删除的值。 |
| NODE\_TEXT\_AREA\_ON\_CHANGE\_WITH\_PREVIEW\_TEXT = 8012 | 定义[TextArea](ts-basic-components-textarea.md)组件在内容改变时（包含预上屏内容），触发回调的枚举值。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)。  [ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)包含参数：  **ArkUI\_TextChangeEvent.pStr**: TextArea的内容。  **ArkUI\_TextChangeEvent.pExtendStr**: TextArea的预上屏内容。  **ArkUI\_TextChangeEvent.number**: TextArea的预上屏起始位置。  **起始版本：** 15 |
| NODE\_TEXT\_AREA\_ON\_WILL\_CHANGE = 8013 | 定义TextArea组件在内容将要改变时（包含预上屏内容），触发回调的枚举值。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)。  [ArkUI\_TextChangeEvent](capi-arkui-nativemodule-arkui-textchangeevent.md)包含参数：  **ArkUI\_TextChangeEvent.pStr**：TextArea的内容。  **ArkUI\_TextChangeEvent.pExtendStr**：TextArea的预上屏内容。  **ArkUI\_TextChangeEvent.number**：TextArea的预上屏起始位置。  **起始版本：** 20 |
| NODE\_CHECKBOX\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX = 11000 | 定义ARKUI\_NODE\_CHECKBOX当选中状态发生变化时，触发该回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  **ArkUI\_NodeComponentEvent.data[0].i32**1:表示已选中, 0: 表示未选中。 |
| NODE\_DATE\_PICKER\_EVENT\_ON\_DATE\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_DATE\_PICKER = 13000 | 定义ARKUI\_NODE\_DATE\_PICKER列表组件的滚动触摸事件枚举值。触发该事件的条件：选择日期时触发该事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示选中时间的年。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示选中时间的月，取值范围：[0-11]。  **ArkUI\_NodeComponentEvent.data[2].i32**：表示选中时间的天。 |
| NODE\_TIME\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TIME\_PICKER = 14000 | 定义ARKUI\_NODE\_TIME\_PICKER列表组件的滚动触摸事件枚举值。触发该事件的条件：选择时间时触发该事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示选中时间的时，取值范围：[0-23]。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示选中时间的分，取值范围：[0-59]。 |
| NODE\_TEXT\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_TEXT\_PICKER = 15000 | 定义ARKUI\_NODE\_TEXT\_PICKER列表组件的滚动触摸事件枚举值。触发该事件的条件 ：选择文本时触发该事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0...11].i32**表示选中数据的维度。 |
| NODE\_TEXT\_PICKER\_EVENT\_ON\_SCROLL\_STOP = 15001 | 定义ARKUI\_NODE\_TEXT\_PICKER列表组件的滚动触摸事件枚举值。触发该事件的条件 ：滑动选择文本项停止时触发该事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0...11].i32**表示选中数据的维度。  **起始版本：** 14 |
| NODE\_CALENDAR\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CALENDAR\_PICKER = 16000 | 定义NODE\_CALENDAR\_PICKER选中日期时触发的事件。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  **ArkUI\_NodeComponent.data[0].u32**选中的年。  **ArkUI\_NodeComponent.data[1].u32**选中的月。  **ArkUI\_NodeComponent.data[2].u32**选中的日。 |
| NODE\_SLIDER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SLIDER = 17000 | 定义ARKUI\_NODE\_SLIDER拖动或点击时触发事件回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：当前滑动进度值。  **ArkUI\_NodeComponentEvent.data[1].i32**：事件触发的相关状态值 |
| NODE\_RADIO\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_RADIO = 18000 | 定义ARKUI\_NODE\_RADIO拖动或点击时触发事件回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：单选框的状态。 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_START = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_IMAGE\_ANIMATOR = 19000 | 定义帧动画开始的状态回调。触发该事件的条件：  1、帧动画开始播放时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_PAUSE = 19001 | 定义帧动画播放暂停时的状态回调。触发该事件的条件：  1、帧动画暂停播放时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_REPEAT = 19002 | 定义帧动画c重复播放时的状态回调。触发该事件的条件：  1、帧动画重复播放时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_CANCEL = 19003 | 定义帧动画返回最初状态时的状态回调。触发该事件的条件：  1、帧动画返回最初状态时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_IMAGE\_ANIMATOR\_EVENT\_ON\_FINISH = 19004 | 定义帧动画播放完成时或者停止播放时的状态回调。触发该事件的条件：  1、帧动画播放完成时或停止播放时。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_CHECKBOX\_GROUP\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_CHECKBOX\_GROUP = 21000 | 定义ARKUI\_NODE\_CHECKBOX\_GROUP的选中状态或群组内的[Checkbox](ts-basic-components-checkbox.md)的选中状态发生变化时，触发该回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_StringAsyncEvent](capi-arkui-nativemodule-arkui-stringasyncevent.md)。  **ArkUI\_StringAsyncEvent.pStr**Name: 被选中的checkbox的名字;Status:0: 表示群组多选择框全部选择。1: 群组多选择框部分选择。2: 群组多选择框全部没有选择。  **起始版本：** 15 |
| NODE\_SWIPER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SWIPER = 1001000 | 定义ARKUI\_NODE\_SWIPER当前元素索引变化时触发事件回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示当前显示元素的索引。 |
| NODE\_SWIPER\_EVENT\_ON\_ANIMATION\_START = 1001001 | 定义ARKUI\_NODE\_SWIPER切换动画开始时触发回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含5个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示当前显示元素的索引。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示切换动画目标元素的索引。  **ArkUI\_NodeComponentEvent.data[2].f32**：表示主轴方向上当前显示元素相对Swiper起始位置的位移。  **ArkUI\_NodeComponentEvent.data[3].f32**：表示主轴方向上目标元素相对Swiper起始位置的位移。  **ArkUI\_NodeComponentEvent.data[4].f32**：表示离手速度。 |
| NODE\_SWIPER\_EVENT\_ON\_ANIMATION\_END = 1001002 | 定义ARKUI\_NODE\_SWIPER切换动画结束是触发回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示当前显示元素的索引。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示主轴方向上当前显示元素相对Swiper起始位置的位移。 |
| NODE\_SWIPER\_EVENT\_ON\_GESTURE\_SWIPE = 1001003 | 定义ARKUI\_NODE\_SWIPER在页面跟手滑动过程中，逐帧触发该回调。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：表示当前显示元素的索引。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示主轴方向上当前显示元素相对Swiper起始位置的位移。 |
| NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL = 1001004 | 定义ARKUI\_NODE\_SWIPER监听[Swiper](ts-container-swiper.md)页面滑动事件。使用说明 ：  1. 设置NODE\_SWIPER\_DISPLAY\_COUNT属性为'auto'时，该接口不生效。  2. 循环场景下，设置prevMargin和nextMargin属性，使得Swiper前后端显示同一页面时，该接口不生效。  3. 在页面滑动过程中，会对视窗内所有页面逐帧触发ContentDidScrollCallback回调。  例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。  4. 设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，  则会对同组中所有页面触发回调。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含4个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：Swiper组件的索引，和[onChange](ts-container-swiper.md#onchange)事件中的index值变化保持一致。  **ArkUI\_NodeComponentEvent.data[1].i32**：视窗内某个页面的索引。  **ArkUI\_NodeComponentEvent.data[2].f32**：页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。  **ArkUI\_NodeComponentEvent.data[3].f32**：主轴方向上页面的长度。 |
| NODE\_SWIPER\_EVENT\_ON\_SELECTED = 1001005 | 定义当ARKUI\_NODE\_SWIPER选中元素改变时触发回调。触发该事件的条件：  1、滑动离手时满足翻页阈值，开始切换动画时。  2、通过NODE\_SWIPER\_INDEX或NODE\_SWIPER\_SWIPE\_TO\_INDEX切换页面时。  事件回调发生时, 事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md) 中包含1个参数:  **ArkUI\_NodeComponentEvent.data[0].i32**: 表示当前选中元素的索引。  **起始版本：** 18 |
| NODE\_SWIPER\_EVENT\_ON\_UNSELECTED = 1001006 | 定义当ARKUI\_NODE\_SWIPER页面切换事件回调。满足以下任一条件，即可触发该事件：  1. 滑动离手时满足翻页阈值，并且开始切换动画。  2. 通过NODE\_SWIPER\_INDEX或NODE\_SWIPER\_SWIPE\_TO\_INDEX切换页面。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md) 中包含1个参数:  **ArkUI\_NodeComponentEvent.data[0].i32**: 表示将要隐藏元素的索引。  **起始版本：** 18 |
| NODE\_SWIPER\_EVENT\_ON\_CONTENT\_WILL\_SCROLL = 1001007 | 定义ARKUI\_NODE\_SWIPER滑动行为拦截事件。使用说明: 在页面滑动前, [ContentWillScrollCallback](ts-container-swiper.md#contentwillscrollcallback15) 回调会触发。  事件回调发生时， 事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数:  **ArkUI\_NodeComponentEvent.data[0].i32**: 当前显示元素的索引。修改该值作为拦截本次事件的结果，设置为0表示拦截，设置为1表示不拦截。  **ArkUI\_NodeComponentEvent.data[1].i32**: 切换动画目标元素的索引。  **ArkUI\_NodeComponentEvent.data[2].f32**: 每帧的滑动偏移量。正数表示向后滑动（例如从index=1到index=0），负数表示向前滑动（例如从index=0到index=1）。  **起始版本：** 15 |
| NODE\_SWIPER\_EVENT\_ON\_SCROLL\_STATE\_CHANGED = 1001008 | 定义ARKUI\_NODE\_SWIPER滑动状态变化事件。触发该事件的条件 ：  Swiper在跟手滑动、离手动画、停止三种滑动状态变化时触发。事件回调发生时， 事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数:  **ArkUI\_NodeComponentEvent.data[0].i32**: 当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。  **起始版本：** 20 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_SCROLL = 1002000 | 定义滚动容器组件的滚动事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：表示距离上一次事件触发的X轴增量。  **ArkUI\_NodeComponentEvent.data[1].f32**：表示距离上一次事件触发的Y轴增量。 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_FRAME\_BEGIN = 1002001 | 定义滚动容器组件的每帧滚动开始事件枚举值。List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。  触发该事件的条件 ：  1. 滚动组件触发滚动时触发，包括键鼠操作等其他触发滚动的输入设置。  2. 调用控制器接口时不触发。  3. 越界回弹不触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：表示即将发生的滚动量。  **ArkUI\_NodeComponentEvent.data[1].i32**：表示当前滚动状态。  **::ArkUI\_NodeComponentEvent**中包含1个返回值：  **ArkUI\_NodeComponentEvent.data[0].f32**：事件处理函数中可根据应用场景计算实际需要的滚动量并存于data[0].f32中，Scroll将按照返回值的实际滚动量进行滚动。 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_SCROLL = 1002002 | 定义滚动容器组件的滑动前触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含4个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，内容向左滚动时偏移量为正，向右滚动时偏移量为负，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：每帧滚动的偏移量，内容向上滚动时偏移量为正，向下滚动时偏移量为负，单位vp。  **ArkUI\_NodeComponentEvent.data[2].i32**：当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。  **ArkUI\_NodeComponentEvent.data[3].i32**：当前滚动的来源，参数类型[ArkUI\_ScrollSource](capi-native-type-h.md#arkui_scrollsource)。 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_SCROLL = 1002003 | 定义滚动容器组件的滑动时触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，内容向左滚动时偏移量为正，向右滚动时偏移量为负，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：每帧滚动的偏移量，内容向上滚动时偏移量为正，向下滚动时偏移量为负，单位vp。  **ArkUI\_NodeComponentEvent.data[2].i32**：当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_START = 1002004 | 定义滚动容器组件的滚动开始事件枚举值。List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。  触发该事件的条件 ：  1. 滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用后开始，带过渡动效。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_STOP = 1002005 | 定义滚动容器组件的滚动停止事件枚举值。List/Scroll/WaterFlow从API version 12开始支持，Grid从API version 22开始支持。  触发该事件的条件 ：  1. 滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用后停止，带过渡动效。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_EDGE = 1002006 | 定义滚动容器组件的滚动边缘事件枚举值。触发该事件的条件 ：  1. 滚动组件滚动到边缘时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数。  **ArkUI\_NodeComponentEvent.data[0].i32**：表示当前碰到的是上下左右哪个边。 |
| NODE\_SCROLL\_EVENT\_ON\_REACH\_START = 1002007 | 定义滚动容器组件到达起始位置时触发回调。触发该事件的条件 ：  1. 组件到达起始位置时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_SCROLL\_EVENT\_ON\_REACH\_END = 1002008 | 定义滚动容器组件到达末尾位置时触发回调。触发该事件的条件 ：  1. 组件到底末尾位置时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_STOP\_DRAGGING = 1002009 | 定义滚动容器组件拖划即将离手回调。触发该事件的条件：  滚动容器组件拖划即将离手时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：滑动离手速度，单位vp/s。  **起始版本：** 20 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_ZOOM = 1002010 | 定义Scroll组件缩放回调。触发该事件的条件：Scroll组件缩放每帧完成时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：当前缩放比例。  **起始版本：** 20 |
| NODE\_SCROLL\_EVENT\_ON\_ZOOM\_START = 1002011 | 定义Scroll组件缩放开始回调。触发该事件的条件：Scroll组件缩放开始时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。  **起始版本：** 20 |
| NODE\_SCROLL\_EVENT\_ON\_ZOOM\_STOP = 1002012 | 定义[Scroll](ts-container-scroll.md)组件缩放停止回调。触发该事件的条件：Scroll组件缩放停止时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。  **起始版本：** 20 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_START\_DRAGGING = 1002013 | 定义滚动容器组件拖划即将开始回调。触发该事件的条件：滚动容器组件拖划即将开始时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。  **起始版本：** 21 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_STOP\_DRAGGING = 1002014 | 定义滚动容器组件拖划结束回调。触发该事件的条件：滚动容器组件拖划结束后触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：拖划结束后是否触发滑动动画。  **起始版本：** 21 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_START\_FLING = 1002015 | 定义滚动容器组件滑动动画即将开始回调。触发该事件的条件：滚动容器组件滑动动画即将开始时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。  **起始版本：** 21 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_STOP\_FLING = 1002016 | 定义滚动容器组件滑动动画结束回调。触发该事件的条件：滚动容器组件滑动动画结束后触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数。  **起始版本：** 21 |
| NODE\_LIST\_ON\_SCROLL\_INDEX = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_LIST = 1003000 | 定义ARKUI\_NODE\_LIST](#arkui\_nodetype)有子组件划入或划出List显示区域时触发事件枚举值。触发该事件的条件 ：  列表初始化时会触发一次，List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：List显示区域内第一个子组件的索引值。  **ArkUI\_NodeComponentEvent.data[1].i32**：List显示区域内最后一个子组件的索引值。  **ArkUI\_NodeComponentEvent.data[2].i32**：List显示区域内中间位置子组件的索引值。 |
| NODE\_LIST\_ON\_WILL\_SCROLL = 1003001 | 定义[ARKUI\_NODE\_LIST](capi-native-node-h.md#arkui_nodetype)组件的滑动前触发事件枚举值。触发该事件的条件：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，list内容向上滚动时偏移量为正，向下滚动时偏移量为负。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。  **ArkUI\_NodeComponentEvent.data[2].i32**：当前滚动的来源，参数类型[ArkUI\_ScrollSource](capi-native-type-h.md#arkui_scrollsource)。 |
| NODE\_LIST\_ON\_DID\_SCROLL = 1003002 | 定义[ARKUI\_NODE\_LIST](capi-native-node-h.md#arkui_nodetype)组件的滑动时触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，list内容向上滚动时偏移量为正，向下滚动时偏移量为负。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前滑动状态。 |
| NODE\_LIST\_ON\_SCROLL\_VISIBLE\_CONTENT\_CHANGE = 1003003 | 定义ARKUI\_NODE\_LIST当前显示内容发生改变的时候触发事件枚举值。触发该事件的条件 ：  列表初始化时会触发一次，List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。计算触发条件时，每一个[ListItem](ts-container-listitem.md)、[ListItemGroup](ts-container-listitemgroup.md)中的[header](ts-container-listitemgroup.md#listitemgroupoptions对象说明)或[footer](ts-container-listitemgroup.md#listitemgroupoptions对象说明)都算一个子组件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含6个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：List显示区域内第一个子组件的索引值。  **ArkUI\_NodeComponentEvent.data[1].i32**：List显示区域起始端在ListItemGroup中的区域。类型为[ArkUI\_ListItemGroupArea](capi-native-type-h.md#arkui_listitemgrouparea)。  **ArkUI\_NodeComponentEvent.data[2].i32**：List显示区域起始端在ListItemGroup中的ListItem索引号，如果List显示区域起始端不在ListItem上，该值为-1。  **ArkUI\_NodeComponentEvent.data[3].i32**：List显示区域内最后一个子组件的索引值。  **ArkUI\_NodeComponentEvent.data[4].i32**：List显示区域末尾端在ListItemGroup中的区域。类型为[ArkUI\_ListItemGroupArea](capi-native-type-h.md#arkui_listitemgrouparea)。  **ArkUI\_NodeComponentEvent.data[5].i32**：List显示区域末尾端在ListItemGroup中的ListItem索引号，如果List显示区域末尾端不在ListItem上，该值为-1。  **起始版本：** 15 |
| NODE\_REFRESH\_STATE\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_REFRESH = 1009000 | 定义ARKUI\_NODE\_REFRESH刷新状态变更触发该事件。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：刷新状态。  0：Inactive，默认未下拉状态。  1：Drag，下拉中，下拉距离小于刷新距离。若此时松手，组件进入Inactive状态；若此时继续下拉使下拉距离超过刷新距离，组件进入OverDrag状态。  2：OverDrag，下拉中，下拉距离超过刷新距离。若此时松手，组件进入Refresh状态；若此时上滑使下拉距离小于刷新距离，组件进入Drag状态。  3：Refresh，下拉结束，回弹至刷新距离，进入刷新中状态。  4：Done，刷新结束，返回初始状态（顶部）。 |
| NODE\_REFRESH\_ON\_REFRESH = 1009001 | 定义ARKUI\_NODE\_REFRESH进入刷新状态时触发该事件。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中不包含参数： |
| NODE\_REFRESH\_ON\_OFFSET\_CHANGE = 1009002 | 定义ARKUI\_NODE\_REFRESH下拉距离发生变化时触发该事件。事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：下拉距离。 |
| NODE\_ON\_WILL\_SCROLL = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_WATER\_FLOW = 1010000 | 定义ARKUI\_NODE\_WATER\_FLOW组件的滑动前触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，内容向上滚动时偏移量为正，向下滚动时偏移量为负。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。  **ArkUI\_NodeComponentEvent.data[2].i32**：当前滚动的来源，参数类型[ArkUI\_ScrollSource](capi-native-type-h.md#arkui_scrollsource)。 |
| NODE\_WATER\_FLOW\_ON\_DID\_SCROLL = 1010001 | 定义ARKUI\_NODE\_WATER\_FLOW组件的滑动时触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，内容向上滚动时偏移量为正，向下滚动时偏移量为负。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前滑动状态。 |
| NODE\_WATER\_FLOW\_ON\_SCROLL\_INDEX = 1010002 | 定义ARKUI\_NODE\_WATER\_FLOW当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发事件枚举值。触发该事件的条件 ：  瀑布流显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：当前显示的WaterFlow起始位置的索引值。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前显示的瀑布流终止位置的索引值。 |
| NODE\_GRID\_ON\_SCROLL\_INDEX = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID = 1013000 | 定义ARKUI\_NODE\_GRID有子组件滑入或滑出Grid显示区域时触发事件枚举值。触发该事件的条件 ：  Grid初始化时会触发一次，Grid显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：Grid显示区域内第一个子组件的索引值。  **ArkUI\_NodeComponentEvent.data[1].i32**：Grid显示区域内最后一个子组件的索引值。  **起始版本：** 22 |
| NODE\_GRID\_ON\_WILL\_SCROLL = 1013001 | 定义ARKUI\_NODE\_GRID组件的滑动前触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，Grid内容向上滚动时偏移量为正，向下滚动时偏移量为负。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。  **ArkUI\_NodeComponentEvent.data[2].i32**：当前滚动的来源，参数类型[ArkUI\_ScrollSource](capi-native-type-h.md#arkui_scrollsource)。  **起始版本：** 22 |
| NODE\_GRID\_ON\_DID\_SCROLL = 1013002 | 定义ARKUI\_NODE\_GRID组件的滑动时触发事件枚举值。触发该事件的条件 ：  1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。  2. 通过滚动控制器API接口调用。  3. 越界回弹。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：每帧滚动的偏移量，Grid内容向上滚动时偏移量为正，向下滚动时偏移量为负。  **ArkUI\_NodeComponentEvent.data[1].i32**：当前滑动状态，参数类型[ArkUI\_ScrollState](capi-native-type-h.md#arkui_scrollstate)。  **起始版本：** 22 |
| NODE\_GRID\_ON\_SCROLL\_BAR\_UPDATE = 1013003 | 定义ARKUI\_NODE\_GRID组件每帧布局结束时，触发用于设置滚动条的位置及长度的事件枚举值。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为0的value.i32：当前显示的网格起始位置的索引值。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为1的value.f32：当前显示的网格起始位置元素相对网格显示起始位置的偏移，单位vp。  **起始版本：** 22 |
| NODE\_GRID\_ON\_ITEM\_DRAG\_START = 1013004 | 定义ARKUI\_NODE\_GRID组件拖拽子组件开始事件枚举值。  触发该事件的条件：  1. 设置NODE\_GRID\_EDIT\_MODE为1。  2. 在Grid子组件上长按并拖动产生足够位移距离时触发。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为0的value.f32：当前拖拽点相对Grid组件的x坐标，单位vp。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为1的value.f32：当前拖拽点相对Grid组件的y坐标，单位vp。  通过OH\_ArkUI\_NodeEvent\_GetNumberValue获取到index为2的value.i32：被拖拽子组件在Grid组件中的索引值。  可通过OH\_ArkUI\_NodeEvent\_SetReturnNumberValue设置返回值。  返回值中index为0的value.i32表示是否可以拖拽，0表示不可以拖拽，1表示可以拖拽。  **起始版本：** 23 |
| NODE\_GRID\_ON\_ITEM\_DRAG\_ENTER = 1013005 | 定义拖拽子组件进入当前Grid组件范围事件枚举值。  触发该事件的条件：  通过NODE\_GRID\_ON\_ITEM\_DRAG\_START事件成功拖拽的子组件进入当前Grid组件范围。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含2个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：当前拖拽点相对Grid组件的x坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：当前拖拽点相对Grid组件的y坐标，单位vp。  **起始版本：** 23 |
| NODE\_GRID\_ON\_ITEM\_DRAG\_MOVE = 1013006 | 定义拖拽子组件在当前Grid组件范围内移动事件枚举值。  触发该事件的条件：  通过NODE\_GRID\_ON\_ITEM\_DRAG\_START事件成功拖拽的子组件进入当前Grid组件范围。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含4个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：当前拖拽点相对Grid组件的x坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：当前拖拽点相对Grid组件的y坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[2].i32**：被拖拽子组件在被拖拽Grid组件中的索引值。  **ArkUI\_NodeComponentEvent.data[3].i32**：被拖拽子组件当前位置在当前Grid组件中的索引值。  **起始版本：** 23 |
| NODE\_GRID\_ON\_ITEM\_DRAG\_LEAVE = 1013007 | 定义拖拽子组件离开当前Grid组件范围事件枚举值。  触发该事件的条件：  通过NODE\_GRID\_ON\_ITEM\_DRAG\_START事件成功拖拽的子组件离开当前Grid组件范围。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含3个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：当前拖拽点相对Grid组件的x坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：当前拖拽点相对Grid组件的y坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[2].i32**：被拖拽子组件在被拖拽Grid组件中的索引值。  **起始版本：** 23 |
| NODE\_GRID\_ON\_ITEM\_DROP = 1013008 | 定义松手释放拖拽子组件事件枚举值。  触发该事件的条件：  松手释放通过NODE\_GRID\_ON\_ITEM\_DRAG\_START事件成功拖拽的子组件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含5个参数：  **ArkUI\_NodeComponentEvent.data[0].f32**：当前拖拽点相对Grid组件的x坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[1].f32**：当前拖拽点相对Grid组件的y坐标，单位vp。  **ArkUI\_NodeComponentEvent.data[2].i32**：被拖拽子组件在被拖拽Grid组件中的索引值。  **ArkUI\_NodeComponentEvent.data[3].i32**：被拖拽子组件当前位置在当前Grid组件中的索引值。  **ArkUI\_NodeComponentEvent.data[4].i32**：被拖拽子组件是否成功释放，1表示释放位置在Grid组件范围内，0表示释放位置在Grid组件范围外。  **起始版本：** 23 |
| NODE\_GRID\_ITEM\_ON\_SELECT = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_GRID\_ITEM = 1014000 | 定义ARKUI\_NODE\_GRID\_ITEM组件选中状态变化事件枚举值。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：0：未选中，1：已选中。  **起始版本：** 23 |
| NODE\_PICKER\_EVENT\_ON\_CHANGE = MAX\_NODE\_SCOPE\_NUM \* ARKUI\_NODE\_PICKER | 定义Picker容器组件中选择某项时触发的事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：选中项的值。  **起始版本：** 23 |
| NODE\_PICKER\_EVENT\_ON\_SCROLL\_STOP = 1018001 | 定义Picker容器组件中选择某项且滚动停止时触发的事件。  事件回调发生时，事件参数[ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)对象中的联合体类型为[ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)。  [ArkUI\_NodeComponentEvent](capi-arkui-nativemodule-arkui-nodecomponentevent.md)中包含1个参数：  **ArkUI\_NodeComponentEvent.data[0].i32**：选中项的值。  **起始版本：** 23 |

### ArkUI\_NodeDirtyFlag

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeDirtyFlag
```

**描述：**

自定义组件调用**::[markDirty](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#markdirty)**时，传递重新执行测量、布局或者绘制的标识类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NODE\_NEED\_MEASURE = 1 | 重新测量大小。该flag类型触发时，同时也默认会触发重新布局。 |
| NODE\_NEED\_LAYOUT = 2 | 重新布局位置。 |
| NODE\_NEED\_RENDER = 3 | 重新进行绘制。 |

### ArkUI\_NodeCustomEventType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeCustomEventType
```

**描述：**

定义自定义组件事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_MEASURE = 1 << 0 | 自定义测量类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_LAYOUT = 1 << 1 | 自定义布局类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW = 1 << 2 | 自定义内容层绘制类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_FOREGROUND\_DRAW = 1 << 3 | 自定义前景绘制类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_OVERLAY\_DRAW = 1 << 4 | 自定义浮层绘制类型。 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_FRONT = 1 << 5 | 自定义内容层前景绘制类型。  **起始版本：** 20 |
| ARKUI\_NODE\_CUSTOM\_EVENT\_ON\_DRAW\_BEHIND = 1 << 6 | 自定义内容层背景绘制类型。  **起始版本：** 20 |

### ArkUI\_NodeAdapterEventType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeAdapterEventType
```

**描述：**

定义节点适配器事件枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NODE\_ADAPTER\_EVENT\_WILL\_ATTACH\_TO\_NODE = 1 | 组件和adapter关联时产生该事件。 |
| NODE\_ADAPTER\_EVENT\_WILL\_DETACH\_FROM\_NODE = 2 | 组件和adapter取消关联时产生该事件。 |
| NODE\_ADAPTER\_EVENT\_ON\_GET\_NODE\_ID = 3 | Adapter需要添加新元素时获取新元素的唯一标识符时产生该事件。 |
| NODE\_ADAPTER\_EVENT\_ON\_ADD\_NODE\_TO\_ADAPTER = 4 | Adapter需要添加新元素时获取新元素的内容时产生该事件。 |
| NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER = 5 | Adapter将元素移除时产生该事件。 |

### ArkUI\_NodeContentEventType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NodeContentEventType
```

**描述：**

定义NodeContent事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NODE\_CONTENT\_EVENT\_ON\_ATTACH\_TO\_WINDOW = 0 | 上树事件。 |
| NODE\_CONTENT\_EVENT\_ON\_DETACH\_FROM\_WINDOW = 1 | 下树事件。 |

### ArkUI\_InspectorErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_InspectorErrorCode
```

**描述：**

[inspector](../harmonyos-guides/arkts-inspector-overview.md)错误码的枚举。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_INSPECTOR\_NATIVE\_RESULT\_SUCCESSFUL = 0 | 成功。 |
| ARKUI\_INSPECTOR\_NATIVE\_RESULT\_BAD\_PARAMETER = -1 | 参数错误。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_NodeEvent\_GetEventType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeEventType OH_ArkUI_NodeEvent_GetEventType(ArkUI_NodeEvent* event)
```

**描述：**

获取组件事件类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeEventType](capi-native-node-h.md#arkui_nodeeventtype) | ArkUI\_NodeEventType 组件事件类型。 |

### OH\_ArkUI\_NodeEvent\_GetTargetId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeEvent_GetTargetId(ArkUI_NodeEvent* event)
```

**描述：**

获取事件自定义标识ID。该事件ID在调用[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)函数时作为参数传递进来，可应用于同一事件入口函数[registerNodeEventReceiver](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeeventreceiver)分发逻辑。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | int32\_t 事件自定义标识ID。 |

### OH\_ArkUI\_NodeEvent\_GetNodeHandle()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_NodeEvent_GetNodeHandle(ArkUI_NodeEvent* event)
```

**描述：**

获取触发该事件的组件对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | ArkUI\_NodeHandle 触发该组件的组件对象。 |

### OH\_ArkUI\_NodeEvent\_GetInputEvent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_UIInputEvent* OH_ArkUI_NodeEvent_GetInputEvent(ArkUI_NodeEvent* event)
```

**描述：**

获取组件事件中的输入事件（如触碰事件）数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_UIInputEvent\*](capi-arkui-eventmodule-arkui-uiinputevent.md) | ArkUI\_UIInputEvent 输入事件数据指针。 |

### OH\_ArkUI\_NodeEvent\_GetNodeComponentEvent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeComponentEvent* OH_ArkUI_NodeEvent_GetNodeComponentEvent(ArkUI_NodeEvent* event)
```

**描述：**

获取组件事件中的数字类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeComponentEvent\*](capi-arkui-nativemodule-arkui-nodecomponentevent.md) | ArkUI\_NodeComponentEvent 数字类型数据指针。 |

### OH\_ArkUI\_NodeEvent\_GetStringAsyncEvent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_StringAsyncEvent* OH_ArkUI_NodeEvent_GetStringAsyncEvent(ArkUI_NodeEvent* event)
```

**描述：**

获取组件事件中的字符串数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_StringAsyncEvent\*](capi-arkui-nativemodule-arkui-stringasyncevent.md) | ArkUI\_StringAsyncEvent 字符串数据指针。 |

### OH\_ArkUI\_NodeEvent\_GetTextChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TextChangeEvent* OH_ArkUI_NodeEvent_GetTextChangeEvent(ArkUI_NodeEvent* event)
```

**描述：**

获取组件事件中的ArkUI\_TextChangeEvent数据。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针，不应为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextChangeEvent\*](capi-arkui-nativemodule-arkui-textchangeevent.md) | 返回ArkUI\_TextChangeEvent对象的指针。 |

### OH\_ArkUI\_NodeEvent\_GetUserData()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_NodeEvent_GetUserData(ArkUI_NodeEvent* event)
```

**描述：**

获取组件事件中的用户自定义数据。该自定义参数在调用[registerNodeEvent](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)函数时作为参数传递进来，可应用于事件触发时的业务逻辑处理。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | void 用户自定义数据指针。 |

### OH\_ArkUI\_NodeEvent\_GetNumberValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeEvent_GetNumberValue(ArkUI_NodeEvent* event, int32_t index, ArkUI_NumberValue* value)
```

**描述：**

获取组件回调事件的数字类型参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |
| int32\_t index | 返回值索引。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)\* value | 具体返回值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 组件事件中参数长度超限。  [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 组件事件中不存在该数据。 |

### OH\_ArkUI\_NodeEvent\_GetStringValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeEvent_GetStringValue(ArkUI_NodeEvent* event, int32_t index, char** string, int32_t* stringSize)
```

**描述：**

获取组件回调事件的字符串类型参数，字符串数据仅在事件回调过程中有效，需要在事件回调外使用建议进行额外拷贝处理。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |
| int32\_t index | 返回值索引。 |
| char\*\* string | 字符串数组的指针。 |
| int32\_t\* stringSize | 字符串数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INDEX\_OUT\_OF\_RANGE](capi-native-type-h.md#arkui_errorcode) 组件事件中参数长度超限。  [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 组件事件中不存在该数据。 |

### OH\_ArkUI\_NodeEvent\_SetReturnNumberValue()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeEvent_SetReturnNumberValue(ArkUI_NodeEvent* event, ArkUI_NumberValue* value, int32_t size)
```

**描述：**

设置组件回调事件的返回值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* event | 组件事件指针。 |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)\* value | 事件数字类型数组。 |
| int32\_t size | 数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_NODE\_EVENT\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 组件事件中不存在该数据。 |

### OH\_ArkUI\_NodeAdapter\_Create()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeAdapterHandle OH_ArkUI_NodeAdapter_Create()
```

**描述：**

创建组件适配器对象。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) | 组件适配器对象。 |

### OH\_ArkUI\_NodeAdapter\_Dispose()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_NodeAdapter_Dispose(ArkUI_NodeAdapterHandle handle)
```

**描述：**

销毁组件适配器对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |

### OH\_ArkUI\_NodeAdapter\_SetTotalNodeCount()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_SetTotalNodeCount(ArkUI_NodeAdapterHandle handle, uint32_t size)
```

**描述：**

设置Adapter中的元素总数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| uint32\_t size | 元素数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeAdapter\_GetTotalNodeCount()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_NodeAdapter_GetTotalNodeCount(ArkUI_NodeAdapterHandle handle)
```

**描述：**

获取Adapter中的元素总数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | Adapter中的元素总数。 |

### OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_RegisterEventReceiver(
2. ArkUI_NodeAdapterHandle handle, void* userData, void (*receiver)(ArkUI_NodeAdapterEvent* event))
```

**描述：**

注册Adapter相关回调事件。在相关回调事件不需要之后，需要执行[OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver](capi-native-node-h.md#oh_arkui_nodeadapter_unregistereventreceiver)接口注销相关回调事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| void\* userData | 自定义数据。 |
| receiver | 事件接收回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeAdapter\_UnregisterEventReceiver()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_NodeAdapter_UnregisterEventReceiver(ArkUI_NodeAdapterHandle handle)
```

**描述：**

注销Adapter相关回调事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |

### OH\_ArkUI\_NodeAdapter\_ReloadAllItems()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_ReloadAllItems(ArkUI_NodeAdapterHandle handle)
```

**描述：**

通知Adapter进行全量元素变化。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeAdapter\_ReloadItem()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_ReloadItem(
2. ArkUI_NodeAdapterHandle handle, uint32_t startPosition, uint32_t itemCount)
```

**描述：**

通知Adapter进行局部元素变化。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| uint32\_t startPosition | 元素变化起始位置。 |
| uint32\_t itemCount | 元素变化数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR NodeAdapter需要添加监听器。 |

### OH\_ArkUI\_NodeAdapter\_RemoveItem()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_RemoveItem(
2. ArkUI_NodeAdapterHandle handle, uint32_t startPosition, uint32_t itemCount)
```

**描述：**

通知Adapter进行局部元素删除。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| uint32\_t startPosition | 元素删除起始位置。 |
| uint32\_t itemCount | 元素删除数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR NodeAdapter需要添加监听器。 |

### OH\_ArkUI\_NodeAdapter\_InsertItem()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_InsertItem(
2. ArkUI_NodeAdapterHandle handle, uint32_t startPosition, uint32_t itemCount)
```

**描述：**

通知Adapter进行局部元素插入。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| uint32\_t startPosition | 元素插入起始位置。 |
| uint32\_t itemCount | 元素插入数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR NodeAdapter需要添加监听器。 |

### OH\_ArkUI\_NodeAdapter\_MoveItem()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_MoveItem(ArkUI_NodeAdapterHandle handle, uint32_t from, uint32_t to)
```

**描述：**

通知Adapter进行局部元素移位。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| uint32\_t from | 元素移位起始位置。 |
| uint32\_t to | 元素移位结束位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR NodeAdapter需要添加监听器。 |

### OH\_ArkUI\_NodeAdapter\_GetAllItems()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapter_GetAllItems(ArkUI_NodeAdapterHandle handle, ArkUI_NodeHandle** items, uint32_t* size)
```

**描述：**

获取存储在Adapter中的所有元素。接口调用会返回元素的数组对象指针，该指针指向的内存数据需要开发者手动释放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterHandle](capi-arkui-nativemodule-arkui-nodeadapter8h.md) handle | 组件适配器对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\*\* items | 适配器内节点数组。 |
| uint32\_t\* size | 元素数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  ERROR\_CODE\_NATIVE\_IMPL\_NODE\_ADAPTER\_NO\_LISTENER\_ERROR NodeAdapter需要添加监听器。 |

### OH\_ArkUI\_NodeAdapterEvent\_GetUserData()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_NodeAdapterEvent_GetUserData(ArkUI_NodeAdapterEvent* event)
```

**描述：**

获取注册事件时传入的自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 用户自定义数据的指针。 |

### OH\_ArkUI\_NodeAdapterEvent\_GetType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeAdapterEventType OH_ArkUI_NodeAdapterEvent_GetType(ArkUI_NodeAdapterEvent* event)
```

**描述：**

获取事件类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeAdapterEventType](capi-native-node-h.md#arkui_nodeadaptereventtype) | 事件类型。 |

### OH\_ArkUI\_NodeAdapterEvent\_GetRemovedNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_NodeAdapterEvent_GetRemovedNode(ArkUI_NodeAdapterEvent* event)
```

**描述：**

获取需要销毁的事件中待销毁的元素。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 待销毁的元素。 |

### OH\_ArkUI\_NodeAdapterEvent\_GetItemIndex()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_NodeAdapterEvent_GetItemIndex(ArkUI_NodeAdapterEvent* event)
```

**描述：**

获取适配器事件时需要操作的元素序号。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 元素序号。 |

### OH\_ArkUI\_NodeAdapterEvent\_GetHostNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_NodeAdapterEvent_GetHostNode(ArkUI_NodeAdapterEvent* event)
```

**描述：**

获取使用该适配器的滚动类容器节点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 适配器的滚动类容器节点。 |

### OH\_ArkUI\_NodeAdapterEvent\_SetItem()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapterEvent_SetItem(ArkUI_NodeAdapterEvent* event, ArkUI_NodeHandle node)
```

**描述：**

设置需要新增到Adapter中的组件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 待添加的组件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeAdapterEvent\_SetNodeId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeAdapterEvent_SetNodeId(ArkUI_NodeAdapterEvent* event, int32_t id)
```

**描述：**

设置生成的组件标识。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeAdapterEvent](capi-arkui-nativemodule-arkui-nodeadapterevent.md)\* event | 适配器事件对象。 |
| int32\_t id | 设置返回的组件标识。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeCustomEvent\_GetLayoutConstraintInMeasure()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_LayoutConstraint* OH_ArkUI_NodeCustomEvent_GetLayoutConstraintInMeasure(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取测算过程中的约束尺寸。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_LayoutConstraint](capi-arkui-nativemodule-arkui-layoutconstraint.md)\* | 约束尺寸指针。 |

### OH\_ArkUI\_NodeCustomEvent\_GetPositionInLayout()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_IntOffset OH_ArkUI_NodeCustomEvent_GetPositionInLayout(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取在布局阶段期望自身相对父组件的位置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md) | 期望自身相对父组件的位置。 |

### OH\_ArkUI\_NodeCustomEvent\_GetDrawContextInDraw()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_DrawContext* OH_ArkUI_NodeCustomEvent_GetDrawContextInDraw(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取绘制上下文。请开发者在使用完成后及时释放获取的绘制上下文。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_DrawContext\*](capi-arkui-nativemodule-arkui-drawcontext.md) | 绘制上下文。 |

### OH\_ArkUI\_NodeCustomEvent\_GetEventTargetId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeCustomEvent_GetEventTargetId(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取自定义事件ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 自定义事件ID。 |

### OH\_ArkUI\_NodeCustomEvent\_GetUserData()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_NodeCustomEvent_GetUserData(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取自定义事件参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 自定义事件参数。 |

### OH\_ArkUI\_NodeCustomEvent\_GetNodeHandle()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_NodeCustomEvent_GetNodeHandle(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取组件对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 组件对象。 |

### OH\_ArkUI\_NodeCustomEvent\_GetEventType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeCustomEventType OH_ArkUI_NodeCustomEvent_GetEventType(ArkUI_NodeCustomEvent* event)
```

**描述：**

通过自定义组件事件获取事件类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeCustomEventType](capi-native-node-h.md#arkui_nodecustomeventtype) | 组件自定义事件类型。 |

### OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanMeasureInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeCustomEvent_GetCustomSpanMeasureInfo(ArkUI_NodeCustomEvent* event, ArkUI_CustomSpanMeasureInfo* info)
```

**描述：**

通过自定义组件事件获取自定义段落组件的测量信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |
| [ArkUI\_CustomSpanMeasureInfo](api-arkui-nativemodule-arkui-customspanmeasureinfo.md)\* info | 需要获取的测量信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_NodeCustomEvent\_SetCustomSpanMetrics()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeCustomEvent_SetCustomSpanMetrics(ArkUI_NodeCustomEvent* event, ArkUI_CustomSpanMetrics* metrics)
```

**描述：**

通过自定义组件事件设置自定义段落的度量指标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |
| [ArkUI\_CustomSpanMetrics](capi-arkui-nativemodule-arkui-customspanmetrics.md)\* metrics | 需要获取的度量指标信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### OH\_ArkUI\_NodeCustomEvent\_GetCustomSpanDrawInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeCustomEvent_GetCustomSpanDrawInfo(ArkUI_NodeCustomEvent* event, ArkUI_CustomSpanDrawInfo* info)
```

**描述：**

通过自定义组件事件获取自定义段落组件的绘制信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeCustomEvent](capi-arkui-nativemodule-arkui-nodecustomevent.md)\* event | 自定义组件事件。 |
| [ArkUI\_CustomSpanDrawInfo](capi-arkui-nativemodule-arkui-customspandrawinfo.md)\* info | 需要获取的绘制信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  异常原因：传入参数验证失败，参数不能为空。 |

### ArkUI\_NodeContentCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*ArkUI_NodeContentCallback)(ArkUI_NodeContentEvent* event)
```

**描述：**

定义NodeContent事件的回调函数类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentEvent](capi-arkui-nativemodule-arkui-nodecontentevent.md)\* event | NodeContent事件指针。 |

### OH\_ArkUI\_NodeContent\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeContent_RegisterCallback(ArkUI_NodeContentHandle content, ArkUI_NodeContentCallback callback)
```

**描述：**

注册NodeContent事件函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) content | 需要注册事件的NodeContent对象。 |
| [ArkUI\_NodeContentCallback](capi-native-node-h.md#arkui_nodecontentcallback) callback | 事件触发时需要执行的函数回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeContentEvent\_GetEventType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeContentEventType OH_ArkUI_NodeContentEvent_GetEventType(ArkUI_NodeContentEvent* event)
```

**描述：**

获取触发NodeContent事件的事件类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentEvent](capi-arkui-nativemodule-arkui-nodecontentevent.md)\* event | NodeContent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeContentEventType](capi-native-node-h.md#arkui_nodecontenteventtype) | NodeContent事件类型。 |

### OH\_ArkUI\_NodeContentEvent\_GetNodeContentHandle()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeContentHandle OH_ArkUI_NodeContentEvent_GetNodeContentHandle(ArkUI_NodeContentEvent* event)
```

**描述：**

获取触发事件的NodeContent对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentEvent](capi-arkui-nativemodule-arkui-nodecontentevent.md)\* event | NodeContent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) | 返回触发事件的NodeContent对象。 |

### OH\_ArkUI\_NodeContent\_SetUserData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeContent_SetUserData(ArkUI_NodeContentHandle content, void* userData)
```

**描述：**

在NodeContent对象上保存自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) content | 需要保存自定义数据的NodeContent对象。 |
| void\* userData | 要保存的自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeContent\_GetUserData()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_NodeContent_GetUserData(ArkUI_NodeContentHandle content)
```

**描述：**

获取在NodeContent对象上保存的自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) content | 需要保存自定义数据的NodeContent对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 自定义数据。 |

### OH\_ArkUI\_NodeContent\_AddNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeContent_AddNode(ArkUI_NodeContentHandle content, ArkUI_NodeHandle node)
```

**描述：**

将一个ArkUI组件节点添加到对应的NodeContent对象下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) content | 需要被添加节点的NodeContent对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被添加的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](capi-native-type-h.md#arkui_errorcode) 子节点已经被接纳。从API version 22开始支持。 |

### OH\_ArkUI\_NodeContent\_RemoveNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeContent_RemoveNode(ArkUI_NodeContentHandle content, ArkUI_NodeHandle node)
```

**描述：**

删除NodeContent对象下的一个ArkUI组件节点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) content | 需要被删除节点的NodeContent对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被删除的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeContent\_InsertNode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeContent_InsertNode(ArkUI_NodeContentHandle content, ArkUI_NodeHandle node, int32_t position)
```

**描述：**

将一个ArkUI组件节点插入到对应的NodeContent对象的特定位置下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeContentHandle](capi-arkui-nativemodule-arkui-nodecontent8h.md) content | 需要被插入节点的NodeContent对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要被插入的节点。 |
| int32\_t position | 需要被插入的位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](capi-native-type-h.md#arkui_errorcode) 子节点已经被接纳。从API version 22开始支持。 |

### OH\_ArkUI\_NodeUtils\_GetLayoutSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetLayoutSize(ArkUI_NodeHandle node, ArkUI_IntSize* size)
```

**描述：**

获取组件布局区域的大小。布局区域大小不包含图形变化属性，如缩放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntSize](capi-arkui-nativemodule-arkui-intsize.md)\* size | 组件handle的绘制区域尺寸，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetLayoutPosition()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetLayoutPosition(ArkUI_NodeHandle node, ArkUI_IntOffset* localOffset)
```

**描述：**

获取组件布局区域相对父组件的位置。布局区域相对位置不包含图形变化属性，如平移。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* localOffset | 组件handle相对父组件的偏移值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetLayoutPositionInWindow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetLayoutPositionInWindow(ArkUI_NodeHandle node, ArkUI_IntOffset* globalOffset)
```

**描述：**

获取组件布局区域相对窗口的位置。布局区域相对位置不包含图形变化属性，如平移。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* globalOffset | 组件handle相对窗口的偏移值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetLayoutPositionInScreen()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetLayoutPositionInScreen(ArkUI_NodeHandle node, ArkUI_IntOffset* screenOffset)
```

**描述：**

获取组件布局区域相对屏幕的位置。布局区域相对位置不包含图形变化属性，如平移。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* screenOffset | 组件handle相对屏幕的偏移值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetLayoutPositionInGlobalDisplay()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetLayoutPositionInGlobalDisplay(ArkUI_NodeHandle node, ArkUI_IntOffset* offset)
```

**描述：**

获取组件相对于全局屏幕的偏移。布局区域相对位置不包含图形变化属性，如平移。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* offset | 组件handle相对屏幕的偏移值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInWindow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetPositionWithTranslateInWindow(ArkUI_NodeHandle node, ArkUI_IntOffset* translateOffset)
```

**描述：**

获取组件在窗口中的位置，包含了图形平移变化属性。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* translateOffset | 组件handle自身，父组件及祖先节点的偏移累计值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetPositionWithTranslateInScreen()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetPositionWithTranslateInScreen(ArkUI_NodeHandle node, ArkUI_IntOffset* translateOffset)
```

**描述：**

获取组件在屏幕中的位置，包含了图形平移变化属性。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* translateOffset | 组件handle自身，父组件及祖先节点的偏移累计值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_AddCustomProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_NodeUtils_AddCustomProperty(ArkUI_NodeHandle node, const char* name, const char* value)
```

**描述：**

设置组件的自定义属性。该接口仅在主线程生效。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| const char\* name | 自定义属性的名称。不允许传入空指针。 |
| const char\* value | 对应key参数名称的自定义属性的值。不允许传入空指针。 |

### OH\_ArkUI\_NodeUtils\_RemoveCustomProperty()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_NodeUtils_RemoveCustomProperty(ArkUI_NodeHandle node, const char* name)
```

**描述：**

移除组件已设置的自定义属性。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| const char\* name | 自定义属性的名称。 |

### OH\_ArkUI\_NodeUtils\_GetCustomProperty()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetCustomProperty(ArkUI_NodeHandle node, const char* name, ArkUI_CustomProperty** handle)
```

**描述：**

获取组件的自定义属性的值。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针。 |
| const char\* name | 自定义属性的名称。 |
| [ArkUI\_CustomProperty](capi-arkui-nativemodule-arkui-customproperty.md)\*\* handle | 获取的对应key参数名称的自定义属性的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetParentInPageTree()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_NodeUtils_GetParentInPageTree(ArkUI_NodeHandle node)
```

**描述：**

获取父节点，可获取由ArkTs创建的组件节点。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 组件的指针，如果没有返回NULL。 |

### OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetActiveChildrenInfo(ArkUI_NodeHandle head, ArkUI_ActiveChildrenInfo** handle)
```

**描述：**

获取某个节点所有活跃的子节点。Span将不会被计入子节点的统计中。在LazyForEach场景中，推荐使用[OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode](capi-native-node-h.md#oh_arkui_nodeutils_getchildwithexpandmode)接口进行遍历。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) head | 传入需要获取的节点。 |
| [ArkUI\_ActiveChildrenInfo](capi-arkui-nativemodule-arkui-activechildreninfo.md)\*\* handle | 对应head节点子节点信息的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetCurrentPageRootNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_NodeHandle OH_ArkUI_NodeUtils_GetCurrentPageRootNode(ArkUI_NodeHandle node)
```

**描述：**

获取当前页面的根节点。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) | 根节点的指针，如果没有返回NULL。 |

### OH\_ArkUI\_NodeUtils\_IsCreatedByNDK()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ArkUI_NodeUtils_IsCreatedByNDK(ArkUI_NodeHandle node)
```

**描述：**

获取组件是否由C-API创建的标签。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 节点是否由C-API创建的Tag，true代表由C-API创建，false代表非C-API创建。 |

### OH\_ArkUI\_NodeUtils\_GetNodeType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetNodeType(ArkUI_NodeHandle node)
```

**描述：**

获取节点的类型。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 节点的类型，具体已开放类型参考[ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype)，未开放结点返回-1。 |

### OH\_ArkUI\_NodeUtils\_GetWindowInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetWindowInfo(ArkUI_NodeHandle node, ArkUI_HostWindowInfo** info)
```

**描述：**

获取节点所属的窗口信息。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点对象。 |
| [ArkUI\_HostWindowInfo](capi-arkui-nativemodule-arkui-hostwindowinfo.md)\*\* info | 窗口信息。使用[OH\_ArkUI\_HostWindowInfo\_Destroy](capi-native-type-h.md#oh_arkui_hostwindowinfo_destroy)释放内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-native-type-h.md#arkui_errorcode) 节点未挂载到节点树上。 |

### OH\_ArkUI\_NodeUtils\_MoveTo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_MoveTo(ArkUI_NodeHandle node, ArkUI_NodeHandle target_parent, int32_t index)
```

**描述：**

将节点移动到目标父节点下，作为子节点。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 待移动的节点对象。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) target\_parent | 目标父节点指针。 |
| int32\_t index | 转移后的节点下标，如果下标值为非法值，则添加在目标父节点的最后一位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。  [ARKUI\_ERROR\_CODE\_NODE\_IS\_ADOPTED](capi-native-type-h.md#arkui_errorcode) 子节点已经被接纳。从API version 22开始支持。 |

### OH\_ArkUI\_NativeModule\_InvalidateAttributes()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_InvalidateAttributes(ArkUI_NodeHandle node)
```

**描述：**

在当前帧触发节点属性更新。

当前节点的属性在构建阶段之后被修改，这些改动不会立即生效，而是会延迟到下一帧统一处理。

此功能会强制当前帧内的即时节点更新，确保同步应用渲染效果。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 待更新的节点对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_List\_CloseAllSwipeActions()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_List_CloseAllSwipeActions(ArkUI_NodeHandle node, void* userData, void (*onFinish)(void* userData))
```

**描述：**

收起展开状态下的ListItem。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 需要注册事件的节点对象。 |
| void\* userData | 自定义事件参数，当事件触发时在回调参数中携带回来。 |
| onFinish | 在收起动画完成后触发的回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_ATTRIBUTE\_OR\_EVENT\_NOT\_SUPPORTED](capi-native-type-h.md#arkui_errorcode) 组件不支持该事件。 |

### OH\_ArkUI\_GetContextByNode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ContextHandle OH_ArkUI_GetContextByNode(ArkUI_NodeHandle node)
```

**描述：**

获取当前节点所在页面的UI的上下文实例对象指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) | UI的上下文实例对象指针。 |

### OH\_ArkUI\_RegisterSystemColorModeChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RegisterSystemColorModeChangeEvent(ArkUI_NodeHandle node,void* userData, void (*onColorModeChange)(ArkUI_SystemColorMode colorMode, void* userData))
```

**描述：**

注册系统深浅色变更事件。同一组件仅能注册一个系统深浅变更回调。示例请参考：[监听组件事件](../harmonyos-guides/ndk-listen-to-component-events.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| void\* userData | 自定义事件参数，当事件触发时在回调参数中携带回来。 |
| onColorModeChange | 事件触发后的回调。[ArkUI\_SystemColorMode](capi-native-type-h.md#arkui_systemcolormode)用于定义系统深浅色模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_UnregisterSystemColorModeChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_UnregisterSystemColorModeChangeEvent(ArkUI_NodeHandle node)
```

**描述：**

注销系统深浅色变更事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

### OH\_ArkUI\_RegisterSystemFontStyleChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RegisterSystemFontStyleChangeEvent(ArkUI_NodeHandle node,void* userData, void (*onFontStyleChange)(ArkUI_SystemFontStyleEvent* event, void* userData))
```

**描述：**

注册系统字体变更事件。同一组件仅能注册一个系统字体变更回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| void\* userData | 自定义事件参数，当事件触发时在回调参数中携带回来。 |
| onFontStyleChange | 事件触发后的回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_UnregisterSystemFontStyleChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_UnregisterSystemFontStyleChangeEvent(ArkUI_NodeHandle node)
```

**描述：**

注销系统字体变更事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

### OH\_ArkUI\_SystemFontStyleEvent\_GetFontSizeScale()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SystemFontStyleEvent_GetFontSizeScale(const ArkUI_SystemFontStyleEvent* event)
```

**描述：**

获取系统字体变更事件的字体大小值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_SystemFontStyleEvent](capi-arkui-nativemodule-arkui-systemfontstyleevent.md)\* event | 表示指向当前系统字体变更事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 更新后的系统字体大小缩放系数。默认值：1.0。 |

### OH\_ArkUI\_SystemFontStyleEvent\_GetFontWeightScale()

PhonePC/2in1TabletTVWearable

```
1. float OH_ArkUI_SystemFontStyleEvent_GetFontWeightScale(const ArkUI_SystemFontStyleEvent* event)
```

**描述：**

获取系统字体变更事件的字体粗细值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_SystemFontStyleEvent](capi-arkui-nativemodule-arkui-systemfontstyleevent.md)\* event | 表示指向当前系统字体变更事件的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 更新后的系统字体粗细缩放系数。默认值：1.0。 |

### OH\_ArkUI\_RegisterLayoutCallbackOnNodeHandle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RegisterLayoutCallbackOnNodeHandle(ArkUI_NodeHandle node,void* userData, void (*onLayoutCompleted)(void* userData))
```

**描述：**

注册指定节点的布局完成回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定需要注册回调函数的目标节点。 |
| void\* userData | 执行回调函数时传给回调函数的用户自定义参数。 |
| onLayoutCompleted | 布局完成时的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_RegisterDrawCallbackOnNodeHandle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RegisterDrawCallbackOnNodeHandle(ArkUI_NodeHandle node,void* userData, void (*onDrawCompleted)(void* userData))
```

**描述：**

注册指定节点的绘制完成回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定需要注册回调函数的目标节点。 |
| void\* userData | 执行回调函数时传给回调函数的用户自定义参数。 |
| onDrawCompleted | 绘制完成时的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_UnregisterLayoutCallbackOnNodeHandle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_UnregisterLayoutCallbackOnNodeHandle(ArkUI_NodeHandle node)
```

**描述：**

取消注册指定节点的布局完成回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定需要取消注册回调函数的目标节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_UnregisterDrawCallbackOnNodeHandle()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_UnregisterDrawCallbackOnNodeHandle(ArkUI_NodeHandle node)
```

**描述：**

取消注册指定节点的绘制完成回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定需要取消注册回调函数的目标节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 参数错误。 |

### OH\_ArkUI\_GetNodeSnapshot()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_GetNodeSnapshot(ArkUI_NodeHandle node, ArkUI_SnapshotOptions* snapshotOptions,OH_PixelmapNative** pixelmap)
```

**描述：**

获取给定组件的截图，若节点不在组件树上或尚未渲染，截图操作将会失败。当pixelmap不再使用时，应通过调用[OH\_PixelmapNative\_Release](capi-pixelmap-native-h.md#oh_pixelmapnative_release)来释放。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 截图的目标节点。 |
| [ArkUI\_SnapshotOptions](capi-arkui-nativemodule-arkui-snapshotoptions.md)\* snapshotOptions | 给定的截图配置，为空时表示默认配置。  截图配置包括缩放属性，色彩空间和动态范围模式配置，从API version 23开始新增支持色彩空间和动态范围模式配置。  其中缩放属性取值为：大于0的浮点数，默认值为1.0。  色彩空间取值为：3（RGB色域为Display P3类型）、4（RGB色域为SRGB类型）、27（RGB色域为DISPLAY BT2020类型），默认值为4。  动态范围模式取值为：[ArkUI\_DynamicRangeMode](capi-native-type-h.md#arkui_dynamicrangemode)，默认值为ARKUI\_DYNAMIC\_RANGE\_MODE\_STANDARD。 |
| [OH\_PixelmapNative\*](capi-arkui-nativemodule-oh-pixelmapnative8h.md)\* pixelmap | 通过系统创建的Pixelmap指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_INTERNAL\_ERROR](capi-native-type-h.md#arkui_errorcode) 截图失败，将返回空指针。  [ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_TIMEOUT](capi-native-type-h.md#arkui_errorcode) 截图超时。  [ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_MODE\_NOT\_SUPPORTED](capi-native-type-h.md#arkui_errorcode) 不支持截图配置中的色彩空间或动态范围模式。  [ARKUI\_ERROR\_CODE\_COMPONENT\_SNAPSHOT\_AUTO\_NOT\_SUPPORTED](capi-native-type-h.md#arkui_errorcode) 离屏节点截图不支持色彩空间或动态范围模式的isAuto参数设置为true。 |

### OH\_ArkUI\_NodeUtils\_GetAttachedNodeHandleById()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetAttachedNodeHandleById(const char* id, ArkUI_NodeHandle* node)
```

**描述：**

根据用户id获取目标节点。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* id | 目标节点的id。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\* node | 目标节点的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetNodeHandleByUniqueId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetNodeHandleByUniqueId(const uint32_t uniqueId, ArkUI_NodeHandle* node)
```

**描述：**

通过uniqueId获取节点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const uint32\_t uniqueId | 目标节点的uniqueId。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\* node | 目标节点的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 方法参数错误。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。 |

### OH\_ArkUI\_NodeUtils\_GetNodeUniqueId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetNodeUniqueId(ArkUI_NodeHandle node, int32_t* uniqueId)
```

**描述：**

获取目标节点的uniqueId。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI节点指针。 |
| int32\_t\* uniqueId | 目标节点的uniqueId。组件标识ID只读，且进程内唯一，若该节点存在，返回该节点的uniqueId值；否则返回-1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 方法参数错误。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。 |

### OH\_ArkUI\_NativeModule\_AdoptChild()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_AdoptChild(ArkUI_NodeHandle node, ArkUI_NodeHandle child)
```

**描述：**

当前节点接纳目标节点为附属节点。被接纳的节点不能已有父节点。调用该接口实际上不会将其添加为子节点，而是仅允许其接收对应子节点的生命周期回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针，指定待接纳节点的父节点。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) child | ArkUI\_NodeHandle指针，指定待被接纳的子节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。  [ARKUI\_ERROR\_CODE\_NODE\_HAS\_PARENT](capi-native-type-h.md#arkui_errorcode) 被接纳的节点已有父节点。  [ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_BE\_ADOPTED](capi-native-type-h.md#arkui_errorcode) 节点无法被接纳为附属节点。  [ARKUI\_ERROR\_CODE\_NODE\_CAN\_NOT\_ADOPT\_TO](capi-native-type-h.md#arkui_errorcode) 节点无法接纳其它附属节点。 |

### OH\_ArkUI\_NativeModule\_RemoveAdoptedChild()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_RemoveAdoptedChild(ArkUI_NodeHandle node, ArkUI_NodeHandle child)
```

**描述：**

移除被接纳的目标附属节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI\_NodeHandle指针，父节点。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) child | ArkUI\_NodeHandle指针，将要被移除的子节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。  [ARKUI\_ERROR\_CODE\_NODE\_IS\_NOT\_IN\_ADOPTED\_CHILDREN](capi-native-type-h.md#arkui_errorcode) 节点不是被目标节点接纳的附属节点。 |

### OH\_ArkUI\_NativeModule\_IsInRenderState()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_IsInRenderState(ArkUI_NodeHandle node, bool* isInRenderState)
```

**描述：**

获取节点是否处于渲染状态，如果一个节点的对应[RenderNode](js-apis-arkui-rendernode.md)在渲染树上，则处于渲染状态。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | ArkUI节点指针。 |
| bool\* isInRenderState | 节点是否处于渲染状态。true：处于渲染状态；false：不处于渲染状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 方法参数异常。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。 |

### OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_SetCrossLanguageOption(ArkUI_NodeHandle node, ArkUI_CrossLanguageOption* option)
```

**描述：**

设置目标节点跨语言设置属性的能力。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点的指针。 |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)\* option | 跨语言配置项 [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetCrossLanguageOption(ArkUI_NodeHandle node, ArkUI_CrossLanguageOption* option)
```

**描述：**

获取目标节点跨语言设置属性的配置项。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点的指针。 |
| [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)\* option | 跨语言配置项 [ArkUI\_CrossLanguageOption](capi-arkui-nativemodule-arkui-crosslanguageoption.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetFirstChildIndexWithoutExpand()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetFirstChildIndexWithoutExpand(ArkUI_NodeHandle node, uint32_t* index)
```

**描述：**

获取目标节点在树上的第一个子节点的下标。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点的指针。 |
| uint32\_t\* index | 子节点的下标值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetLastChildIndexWithoutExpand()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetLastChildIndexWithoutExpand(ArkUI_NodeHandle node, uint32_t* index)
```

**描述：**

获取目标节点在树上的最后一个子节点的下标。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点的指针。 |
| uint32\_t\* index | 子节点的下标值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetChildWithExpandMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetChildWithExpandMode(ArkUI_NodeHandle node, int32_t position,ArkUI_NodeHandle* subnode, uint32_t expandMode)
```

**描述：**

用不同的展开模式获取对应下标的子节点。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点的指针。 |
| int32\_t position | 对应子节点的下标。 |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)\* subnode | 获取子节点的指针。 |
| uint32\_t expandMode | 节点遍历展开方式。 [ArkUI\_ExpandMode](capi-native-type-h.md#arkui_expandmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NodeUtils\_GetPositionToParent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NodeUtils_GetPositionToParent(ArkUI_NodeHandle node, ArkUI_IntOffset* globalOffset)
```

**描述：**

获取目标节点相对于父节点的偏移值，单位：px。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* globalOffset | 目标节点相对父节点的偏移值，单位：px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_AddSupportedUIStates()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_AddSupportedUIStates(ArkUI_NodeHandle node, int32_t uiStates,void (statesChangeHandler)(int32_t currentStates, void* userData), bool excludeInner, void* userData)
```

**描述：**

设置组件支持的[多态样式](ts-universal-attributes-polymorphic-style.md)状态。为了更高效地处理，需传入所关注的状态值及对应的状态处理函数，当关注的状态发生时，处理函数会被执行。可在回调中根据当前状态调整UI样式。当在同一个节点上多次调用该方法时，将以最后一次传入的状态及处理函数为准。有些类型的组件节点，系统内部已有对某些状态的默认处理。例如，Button组件默认具备对PRESSED状态的样式变化，当在此类组件上使用此方法自定义状态处理时，会先应用系统默认样式变化，再执行自定义的样式处理，最终效果为两者叠加。可以通过指定excludeInner为true来禁用系统内部的默认样式效果，但这通常取决于系统内部实现规范是否允许。当调用该函数时，传入的statesChangeHandler函数会立即执行一次，且无需特意注册对NORMAL状态的监听，只要注册了非NORMAL状态，当状态从任意状态变化回NORMAL时，系统都会进行回调，以便应用进行样式复原。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| int32\_t uiStates | 目标节点需要处理的目标UI状态。所有目标UI状态的组合结果可以通过“|”操作来计算。例如：targetUIStates = ArkUI\_UIState::PRESSED | ArkUI\_UIState::FOCUSED。 |
| void (statesChangeHandler)(int32\_t currentStates, void\* userData) | UI状态改变处理函数。返回当前UI状态，该值是所有当前状态枚举值“|”计算的结果，可以通过执行“&”操作来确定状态。例如：if (currentStates & ArkUI\_UIState::PRESSED == ArkUI\_UIState::PRESSED)。但是，对于正常状态检查，应直接使用等号。例如：if (currentStates == ArkUI\_UIState::NORMAL) |
| bool excludeInner | 禁止内部默认状态样式的标志。​​true​​表示禁用系统内部的默认样式，false表示不禁用。 |
| void\* userData | onDrawCompleted回调函数中使用的自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_RemoveSupportedUIStates()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_RemoveSupportedUIStates(ArkUI_NodeHandle node, int32_t uiStates)
```

**描述：**

删除注册的状态处理。当通过OH\_ArkUI\_AddSupportedUIStates注册的状态都被删除时，所注册的stateChangeHandler也不会再被执行。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| int32\_t uiStates | 节点需要删除的目标UI状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_RunTaskInScope()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_RunTaskInScope(ArkUI_ContextHandle uiContext, void* userData, void(*callback)(void* userData))
```

**描述：**

在目标UI上下文中执行传入的自定义回调函数。示例请参考：[在NDK中保证多实例场景功能正常](../harmonyos-guides/ndk-scope-task.md)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | 表示目标UI上下文的指针。 |
| void\* userData | 开发者自定义数据指针，以便在回调函数中处理自定义数据，开发者需自行保证自定义函数被执行时的数据有效性。 |
| void(\*callback)(void\* userData) | 开发者自定义回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。  [ARKUI\_ERROR\_CODE\_UI\_CONTEXT\_INVALID](capi-native-type-h.md#arkui_errorcode) UIContext对象无效。  [ARKUI\_ERROR\_CODE\_CALLBACK\_INVALID](capi-native-type-h.md#arkui_errorcode) 回调函数无效。 |

### OH\_ArkUI\_PostAsyncUITask()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PostAsyncUITask(ArkUI_ContextHandle context, void* asyncUITaskData,
2. void (*asyncUITask)(void* asyncUITaskData), void (*onFinish)(void* asyncUITaskData))
```

**描述：**

将asyncUITask函数提交至ArkUI框架提供的非UI线程中执行，asyncUITask函数执行完毕后，在UI线程调用onFinish函数。

适用于多线程创建UI组件的场景，开发者可使用此接口在非UI线程创建UI组件，随后在UI线程将创建完成的组件挂载至主树上。

**起始版本：** 22

**参数:**

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | UI实例对象指针。 |
| void\* asyncUITaskData | 开发者自定义数据指针，作为asyncUITask和onFinish的入参。可以传入空指针。 |
| asyncUITask | 在非UI线程执行的函数。 |
| onFinish | asyncUITask执行完成后，在UI线程执行的函数。可以传入空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) context对象无效或asyncUITask为空指针。 |

### OH\_ArkUI\_PostUITask()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PostUITask(ArkUI_ContextHandle context, void* taskData, void (*task)(void* taskData))
```

**描述：**

将task函数提交至UI线程中执行。

适用于多线程创建UI组件的场景，当开发者在自建的线程中创建UI组件时，可以使用此接口将创建完成的组件挂载到UI线程的主树上。

**起始版本：** 22

**参数:**

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | UI实例对象指针。 |
| void\* taskData | 开发者自定义数据指针，作为task的入参。可以传入空指针。 |
| task | 在UI线程执行的函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) context对象无效或task为空指针。 |

### OH\_ArkUI\_PostUITaskAndWait()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_PostUITaskAndWait(ArkUI_ContextHandle context, void* taskData, void (*task)(void* taskData))
```

**描述：**

将task函数提交至UI线程中执行，调用此接口的线程将阻塞，直至task函数执行完成。在UI线程调用此接口等同于同步调用task函数。

适用于多线程创建UI组件的场景，当开发者在多线程创建组件过程中需要调用仅支持UI线程的函数时，使用此接口返回UI线程调用函数，调用完成后继续多线程创建组件。

当UI线程负载较高时，调用此接口的非UI线程可能长时间阻塞，影响多线程创建UI组件的性能，不建议频繁使用。

**起始版本：** 22

**参数:**

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) context | UI实例对象指针。 |
| void\* taskData | 开发者自定义数据指针，作为task的入参。可以传入空指针。 |
| task | 在UI线程执行的函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) context对象无效或task为空指针。 |

### OH\_ArkUI\_NativeModule\_RegisterCommonEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_RegisterCommonEvent(ArkUI_NodeHandle node, ArkUI_NodeEventType eventType, void* userData, void (*callback)(ArkUI_NodeEvent* event))
```

**描述：**

注册目标节点的基础事件回调。

当前支持的事件类型如下: 参考[ArkUI\_NodeEventType](capi-native-node-h.md#arkui_nodeeventtype)中的NODE\_ON\_CLICK\_EVENT、NODE\_TOUCH\_EVENT、NODE\_EVENT\_ON\_APPEAR、NODE\_EVENT\_ON\_DISAPPEAR、NODE\_ON\_KEY\_EVENT、NODE\_ON\_FOCUS、NODE\_ON\_BLUR、NODE\_ON\_HOVER、NODE\_ON\_MOUSE、NODE\_ON\_SIZE\_CHANGE。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| [ArkUI\_NodeEventType](capi-native-node-h.md#arkui_nodeeventtype) eventType | 事件类型。 |
| void\* userData | 开发者自定义的数据指针，以便在回调函数中处理自定义数据，需确保自定义函数执行时数据有效。 |
| callback | 开发者自定义的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE](capi-native-type-h.md#arkui_errorcode) 暂不支持该事件类型。 |

### OH\_ArkUI\_NativeModule\_UnregisterCommonEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_UnregisterCommonEvent(ArkUI_NodeHandle node, ArkUI_NodeEventType eventType)
```

**描述：**

注销目标节点的基础事件回调。

当前支持的事件类型请参考[OH\_ArkUI\_NativeModule\_RegisterCommonEvent](capi-native-node-h.md#oh_arkui_nativemodule_registercommonevent)。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| [ArkUI\_NodeEventType](capi-native-node-h.md#arkui_nodeeventtype) eventType | 事件类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_NODE\_UNSUPPORTED\_EVENT\_TYPE](capi-native-type-h.md#arkui_errorcode) 暂不支持该事件类型。 |

### OH\_ArkUI\_NativeModule\_RegisterCommonVisibleAreaApproximateChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_RegisterCommonVisibleAreaApproximateChangeEvent(ArkUI_NodeHandle node, float* ratios, int32_t size, float expectedUpdateInterval, void* userData, void (*callback)(ArkUI_NodeEvent* event))
```

**描述：**

注册限制回调间隔的可见区域变化的基础事件回调。

**起始版本：** 21

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |
| float\* ratios | 阈值数组，表示组件的可见区域。 |
| int32\_t size | 阈值数组的大小。 |
| float expectedUpdateInterval | 开发人员预期的计算间隔。 |
| void\* userData | 开发者自定义的数据指针，以便在回调函数中处理自定义数据，需确保自定义函数执行时数据有效。 |
| callback | 开发者自定义的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_NativeModule\_UnregisterCommonVisibleAreaApproximateChangeEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_UnregisterCommonVisibleAreaApproximateChangeEvent(ArkUI_NodeHandle node)
```

**描述：**

注销限制回调间隔的可见区域变化的基础事件回调。

**起始版本：** 21

**参数:**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 目标节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Swiper\_FinishAnimation()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_FinishAnimation(ArkUI_NodeHandle node)
```

**描述：**

停止指定的Swiper节点正在执行的翻页动画。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_SetForceDarkConfig()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_SetForceDarkConfig(ArkUI_ContextHandle uiContext, bool forceDark, ArkUI_NodeType nodeType, uint32_t (*colorInvertFunc)(uint32_t color))
```

**描述：**

为组件和实例设置反色算法。详细介绍请参考：[利用反色能力快速适配深色模式](../harmonyos-guides/ui-dark-light-color-adaptation.md#利用反色能力快速适配深色模式)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md) uiContext | UI实例对象指针。  如果该值为null，则该功能适用于整个应用进程。 |
| bool forceDark | 是否使用反色能力。取值为true：组件使用反色能力，取值为false：组件不使用反色能力。 |
| [ArkUI\_NodeType](capi-native-node-h.md#arkui_nodetype) nodeType | 指定使用反色能力生效组件范围。  ARKUI\_NODE\_UNDEFINED代表对所有组件类型生效。 |
| colorInvertFunc | 开发者自定义反色算法函数。  如果该值为nullptr，则对组件使用系统默认反色算法，即三原色取反。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) CAPI初始化错误。  [ARKUI\_ERROR\_CODE\_FORCE\_DARK\_CONFIG\_INVALID](capi-native-type-h.md#arkui_errorcode) 反色能力入参错误。 |

### OH\_ArkUI\_NodeEvent\_GetTouchTestInfo()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_TouchTestInfo* OH_ArkUI_NodeEvent_GetTouchTestInfo(ArkUI_NodeEvent* nodeEvent)
```

**描述：**

获取组件事件中的触摸测试信息。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeEvent](capi-arkui-nativemodule-arkui-nodeevent.md)\* nodeEvent | 组件事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)\* | 返回指向[ArkUI\_TouchTestInfo](capi-arkui-nativemodule-arkui-touchtestinfo.md)对象的指针。若传入的参数无效或并非触摸测试信息，则返回null。 |

### OH\_ArkUI\_NativeModule\_ConvertPositionToWindow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_ConvertPositionToWindow(ArkUI_NodeHandle currentNode, ArkUI_IntOffset localPosition, ArkUI_IntOffset* windowPosition)
```

**描述：**

将点的坐标从指定节点的坐标系转换至当前窗口的坐标系。节点的坐标系考虑节点本身的变换，例如，节点A的变换效果为向左平移100，会使得其坐标系中的点的坐标也向左平移100。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/H43oCbIHQrOkCl9uoqVuYw/zh-cn_image_0000002552960506.png?HW-CC-KV=V1&HW-CC-Date=20260428T000348Z&HW-CC-Expire=86400&HW-CC-Sign=B6C6C091A84364E5F57C2B8D6E55C71B04C8F31C335FB1A450161FC7974D5BAD)

如上图所示，将指定节点坐标系中的坐标(x0, y0)转换成窗口坐标系的坐标，结果为(x1, y1)。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) currentNode | 指定节点。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md) localPosition | 点在指定节点坐标系中的坐标，单位：px。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* windowPosition | 指向接收转换后坐标（位于当前窗口坐标系中，单位：px）的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-native-type-h.md#arkui_errorcode) 节点未挂载到节点树上。 |

### OH\_ArkUI\_NativeModule\_ConvertPositionFromWindow()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_NativeModule_ConvertPositionFromWindow(ArkUI_NodeHandle targetNode, ArkUI_IntOffset windowPosition, ArkUI_IntOffset* localPosition)
```

**描述：**

将点的坐标从当前窗口的坐标系转换至目标节点的坐标系。节点的坐标系考虑节点本身的变换，例如，节点A的变换效果为向左平移100，会使得其坐标系中的点的坐标也向左平移100。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/7vPOQGbOQ5ubgGaAvhH_Jw/zh-cn_image_0000002583480507.png?HW-CC-KV=V1&HW-CC-Date=20260428T000348Z&HW-CC-Expire=86400&HW-CC-Sign=9625BAE061B3F82E159B65BE4F1DFCF6F55E92590713744F4FF2297DBF80BD3C)

如上图所示，将窗口坐标系中的坐标(x1, y1)转换成目标节点坐标系的坐标，结果为(x0, y0)。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) targetNode | 目标节点。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md) windowPosition | 点在当前窗口坐标系中的坐标，单位：px。 |
| [ArkUI\_IntOffset](capi-arkui-nativemodule-arkui-intoffset.md)\* localPosition | 指向接收转换后坐标（位于目标节点坐标系中，单位：px）的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_NODE\_NOT\_ON\_MAIN\_TREE](capi-native-type-h.md#arkui_errorcode) 节点未挂载到节点树上。 |

### OH\_ArkUI\_Swiper\_StartFakeDrag()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_StartFakeDrag(ArkUI_NodeHandle node, bool* isSuccessful)
```

**描述**

启动Swiper节点的模拟拖拽操作。调用[OH\_ArkUI\_Swiper\_FakeDragBy](capi-native-node-h.md#oh_arkui_swiper_fakedragby)模拟拖拽动作。调用[OH\_ArkUI\_Swiper\_StopFakeDrag](capi-native-node-h.md#oh_arkui_swiper_stopfakedrag)停止模拟拖拽。

模拟拖拽操作可以被真实拖拽操作打断。如果需要在模拟拖拽期间忽略用户的拖拽事件，请使用[NODE\_SWIPER\_DISABLE\_SWIPE](capi-native-node-h.md#arkui_nodeattributetype)。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| bool\* isSuccessful | 模拟拖拽操作是否成功启动。如果模拟拖拽操作成功启动，则返回true。  如果Swiper尚未准备好启动模拟拖拽操作，或者真实拖拽或模拟拖拽操作已在进行中，则返回false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Swiper\_FakeDragBy()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_FakeDragBy(ArkUI_NodeHandle node, float offset, bool* isConsumedOffset)
```

**描述**

通过设置Swiper节点的偏移量模拟拖拽效果。该接口调用前，必须先调用[OH\_ArkUI\_Swiper\_StartFakeDrag](capi-native-node-h.md#oh_arkui_swiper_startfakedrag)启动模拟拖拽。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| float offset | 需要拖拽的偏移量。单位是vp。 |
| bool\* isConsumedOffset | 是否消耗偏移量触发拖拽。如果消耗偏移量触发拖拽，则返回true。  如果未处于模拟拖拽进度，或者未消耗任何偏移量，则返回false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Swiper\_StopFakeDrag()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_StopFakeDrag(ArkUI_NodeHandle node, bool* isSuccessful)
```

**描述**

停止对Swiper节点的模拟拖拽。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| bool\* isSuccessful | 模拟拖拽操作是否成功停止。如果模拟拖拽成功停止，则返回true。  如果Swiper尚未准备好停止模拟拖拽，或者没有正在进行的模拟拖拽，则返回false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Swiper\_IsFakeDragging()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_IsFakeDragging(ArkUI_NodeHandle node, bool* isFakeDragging)
```

**描述**

获取Swiper节点的模拟拖拽状态。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| bool\* isFakeDragging | 是否处于模拟拖拽状态。如果正在进行模拟拖拽操作，则返回true，否则返回false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Swiper\_ShowPrevious()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_ShowPrevious(ArkUI_NodeHandle node)
```

**描述**

显示Swiper节点的上一页。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_Swiper\_ShowNext()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_Swiper_ShowNext(ArkUI_NodeHandle node)
```

**描述**

显示Swiper节点的下一页。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
