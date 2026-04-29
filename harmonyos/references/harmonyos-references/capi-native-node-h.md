---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h
title: native_node.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h
category: harmonyos-references
scraped_at: 2026-04-29T13:54:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:04e7b4d2433ed196ef6f6a2aa0652977146195fd5e7f312b3e30ac6b456e0f2a
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
| [基础属性](capi-native-node-h-nodeattributetype-base.md) | 定义ArkUI在Native侧可以设置的基础属性集合，包含背景、背景图片样式和组件标识等属性设置。 |
| [通用属性](capi-native-node-h-nodeattributetype-common.md) | 定义ArkUI在Native侧可以设置的通用属性样式集合。 |
| [布局属性](i-native-node-h-nodeattributetype-layoutattributes.md) | 定义ArkUI在Native侧可以设置的布局相关属性集合，包含尺寸、百分比尺寸、内外边距、边框、位置、对齐、方向、约束、Flex参数、布局规则及布局类组件相关属性设置。 |
| [布局类组件相关属性](pi-native-node-h-nodeattributetype-layoutcomponent.md) | 定义ArkUI在Native侧可以设置的布局类组件相关属性集合。 |
| [动效、视效相关属性](capi-native-node-h-nodeattributetype-animator.md) | 定义ArkUI在Native侧可以设置的动效、视效相关属性样式集合，包含图形变换、渐变、阴影、模糊和转场等属性设置。 |
| [交互类相关属性](capi-native-node-h-nodeattributetype-interaction.md) | 定义ArkUI在Native侧可以设置的交互类相关属性集合，包含触摸测试、响应热区、焦点控制、安全区域扩展、可见区域监听和走焦等属性设置。 |
| [表单类组件相关属性](capi-native-node-h-nodeattributetype-form.md) | 定义ArkUI在Native侧可以设置的表单类组件相关属性样式集合，包含Toggle、Button、CheckBox、CheckBoxGroup、Slider、Radio等组件属性设置。 |
| [滚动容器类组件相关属性](ative-node-h-nodeattributetype-scrollablecontainer.md) | 定义ArkUI在Native侧可以设置的滚动容器类组件相关属性样式集合，包含Scroll、List、ListItem、ListItemGroup、Refresh、WaterFlow、Grid、GridItem等组件属性设置。 |
| [导航类组件相关属性](de-h-nodeattributetype-navigationrelatedcomponents.md) | 定义ArkUI在Native侧可以设置的导航类组件相关属性样式集合，包含Swiper组件属性设置。 |
| [信息展示类组件相关属性](native-node-h-nodeattributetype-informationdisplay.md) | 定义ArkUI在Native侧可以设置信息展示类组件相关属性样式集合，包含LoadingProgress、Progress等组件属性设置。 |
| [信息选择类组件相关属性](tive-node-h-nodeattributetype-informationselection.md) | 定义ArkUI在Native侧可以设置信息选择类组件相关属性样式集合，包含DatePicker、TimePicker、TextPicker、CalendarPicker等组件属性设置。 |
| [无障碍相关属性](capi-native-node-h-nodeattributetype-accessibility.md) | 定义ArkUI在Native侧可以设置的无障碍相关属性集合，包含无障碍文本、说明、模式、状态、信息等属性设置。 |
| [文本显示类组件相关属性](capi-native-node-h-nodeattributetype-text.md) | 定义ArkUI在Native侧可以设置的文本类组件相关属性样式集合，包含Text、Span、ImageSpan等组件属性设置。 |
| [文本输入类组件相关属性](-native-node-h-nodeattributetype-textinputcategory.md) | 定义ArkUI在Native侧可以设置的文本输入类组件相关属性样式集合，包含TextInput组件属性设置。 |
| [图类组件相关属性](capi-native-node-h-nodeattributetype-image.md) | 定义ArkUI在Native侧可以设置的图类组件相关属性样式集合，包含Image和ImageAnimator组件属性设置。 |
| [X-Component组件相关属性](capi-native-node-h-nodeattributetype-xcomponent.md) | 定义ArkUI在Native侧可以设置的XComponent组件相关属性集合。 |
| [EmbeddedComponent组件相关属性](-native-node-h-nodeattributetype-embeddedcomponent.md) | 定义ArkUI在Native侧可以设置的EmbeddedComponent组件相关属性样式集合。 |
| [其他](capi-native-node-h-nodeattributetype-other.md) | 定义ArkUI在Native侧可以设置的其他属性样式集合，包含组件交互、获焦、离屏渲染和点击距离等属性设置。 |

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/XCPHrRlOSCGxbowkDohJdQ/zh-cn_image_0000002558607372.png?HW-CC-KV=V1&HW-CC-Date=20260429T055409Z&HW-CC-Expire=86400&HW-CC-Sign=7594C9A4A95949A3BF31C3C3DBCC7AF9A9451CF603C5325A0B3EBDF4EC77D7C7)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/RuPxX9H7Sve-Dixna_cVWQ/zh-cn_image_0000002589326901.png?HW-CC-KV=V1&HW-CC-Date=20260429T055409Z&HW-CC-Expire=86400&HW-CC-Sign=B3C9CB525BB66DA7727150F69A693F4BC79EE4018466443900E528BD811C30E6)

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

* **[ArkUI\_NodeAttributeType（基础属性）](capi-native-node-h-nodeattributetype-base.md)**
* **[ArkUI\_NodeAttributeType（通用属性）](capi-native-node-h-nodeattributetype-common.md)**
* **[ArkUI\_NodeAttributeType（布局属性）](i-native-node-h-nodeattributetype-layoutattributes.md)**
* **[ArkUI\_NodeAttributeType（布局类组件相关属性）](pi-native-node-h-nodeattributetype-layoutcomponent.md)**
* **[ArkUI\_NodeAttributeType（动效、视效相关属性）](capi-native-node-h-nodeattributetype-animator.md)**
* **[ArkUI\_NodeAttributeType（交互类相关属性）](capi-native-node-h-nodeattributetype-interaction.md)**
* **[ArkUI\_NodeAttributeType（表单类组件相关属性）](capi-native-node-h-nodeattributetype-form.md)**
* **[ArkUI\_NodeAttributeType（滚动容器类组件相关属性）](ative-node-h-nodeattributetype-scrollablecontainer.md)**
* **[ArkUI\_NodeAttributeType（导航类组件相关属性）](de-h-nodeattributetype-navigationrelatedcomponents.md)**
* **[ArkUI\_NodeAttributeType（信息展示类组件相关属性）](native-node-h-nodeattributetype-informationdisplay.md)**
* **[ArkUI\_NodeAttributeType（信息选择类组件相关属性）](tive-node-h-nodeattributetype-informationselection.md)**
* **[ArkUI\_NodeAttributeType（无障碍相关属性）](capi-native-node-h-nodeattributetype-accessibility.md)**
* **[ArkUI\_NodeAttributeType（文本显示类组件相关属性）](capi-native-node-h-nodeattributetype-text.md)**
* **[ArkUI\_NodeAttributeType（文本输入类组件相关属性）](-native-node-h-nodeattributetype-textinputcategory.md)**
* **[ArkUI\_NodeAttributeType（图类组件相关属性）](capi-native-node-h-nodeattributetype-image.md)**
* **[ArkUI\_NodeAttributeType（XComponent组件相关属性）](capi-native-node-h-nodeattributetype-xcomponent.md)**
* **[ArkUI\_NodeAttributeType（EmbeddedComponent组件相关属性）](-native-node-h-nodeattributetype-embeddedcomponent.md)**
* **[ArkUI\_NodeAttributeType（其他）](capi-native-node-h-nodeattributetype-other.md)**
