---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-treeview
title: TreeView
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > TreeView
category: harmonyos-references
scraped_at: 2026-04-28T08:02:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8fc0598062c763882bb71d6c6a661faddae35f014490683317e6a3a1a5610d38
---

树视图作为一种分层显示的列表，适合显示嵌套结构。拥有父列表项和子列表项，可展开或折叠。

用于效率型应用，如备忘录、电子邮件、图库中的侧边导航栏中。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果TreeView设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到TreeView本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议TreeView设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TreeView } from "@kit.ArkUI";
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## TreeView

PhonePC/2in1TabletTVWearable

TreeView({ treeController: TreeController })

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| treeController | [TreeController](ohos-arkui-advanced-treeview.md#treecontroller) | 是 | 树视图节点信息。 |

## TreeController

PhonePC/2in1TabletTVWearable

树视图组件的控制器，可以将此对象绑定至树视图组件，然后通过它控制树的节点信息，同一个控制器不可以控制多个树视图组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### addNode

PhonePC/2in1TabletTVWearable

addNode(nodeParam?: NodeParam): TreeController

点击某个节点后，调用该方法可以触发新增孩子节点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nodeParam | [NodeParam](ohos-arkui-advanced-treeview.md#nodeparam) | 否 | 节点信息，用于指定新增节点的属性。如果不传该参数，在当前选中的节点下添加一个标题为“新建文件夹”节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TreeController](ohos-arkui-advanced-treeview.md#treecontroller) | 树视图组件的控制器。 |

### removeNode

PhonePC/2in1TabletTVWearable

removeNode(): void

点击某个节点后，调用该方法可以触发删除该节点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### modifyNode

PhonePC/2in1TabletTVWearable

modifyNode(): void

点击某个节点后，调用该方法可以触发修改该节点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### buildDone

PhonePC/2in1TabletTVWearable

buildDone(): void

建立树视图。节点增加完毕后，必须调用该方法，触发树信息的保存。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### refreshNode

PhonePC/2in1TabletTVWearable

refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void

更新树视图。调用该方法，更新当前节点的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parentId | number | 是 | 父节点Id。  取值范围：大于等于-1。 |
| parentSubTitle | [ResourceStr](ts-types.md#resourcestr) | 是 | 父节点副文本。 |
| currentSubtitle | [ResourceStr](ts-types.md#resourcestr) | 是 | 当前节点副文本。 |

## NodeParam

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| parentNodeId | number | 否 | 是 | 父节点Id。  取值范围：大于等于-1。  默认值：-1，根节点id值为-1。若设置数值小于-1，做不生效处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| currentNodeId | number | 否 | 是 | 当前子节点Id。  取值范围：大于等于-1。  不能为根节点id，不能为null，否则会抛出异常。且不能设置两个相同的currentNodeId。  默认值：-1  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isFolder | boolean | 否 | 是 | 是否是目录。  默认值：false  true：是目录，false：不是目录。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标。  默认值：空字符串  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolIconStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol图标，优先级大于icon。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| selectedIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 选中图标。  默认值：空字符串  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolSelectedIconStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol选中图标，优先级大于selectedIcon。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| editIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 编辑图标。  默认值：空字符串  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| symbolEditIconStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | Symbol编辑图标，优先级大于editIcon。  默认值：undefined  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 主标题。  默认值：空字符串  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 副标题。  默认值：空字符串  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| container | () => void | 否 | 是 | 绑定在节点上的右键子组件，子组件由@Builder修饰。  默认值：() => void  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## TreeListenerManager

PhonePC/2in1TabletTVWearable

树视图组件的监听器，可以将此对象绑定至树视图组件，然后通过它监听树的节点的变化，同一个监听器不可以控制多个树视图组件。

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

### getInstance

PhonePC/2in1TabletTVWearable

static getInstance(): TreeListenerManager

获取监听管理器单例对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [TreeListenerManager](ohos-arkui-advanced-treeview.md#treelistenermanager) | 返回获取到的监听管理器单例对象。 |

### getTreeListener

PhonePC/2in1TabletTVWearable

getTreeListener(): TreeListener

获取监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**返回值**:

| 类型 | 说明 |
| --- | --- |
| [TreeListener](ohos-arkui-advanced-treeview.md#treelistener) | 返回获取到的监听器。 |

## TreeListener

PhonePC/2in1TabletTVWearable

树视图组件的监听器，可以将此对象绑定至树视图组件，然后通过它监听树的节点的变化，同一个监听器不可以控制多个树视图组件。

### on

PhonePC/2in1TabletTVWearable

on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void;

注册监听。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TreeListenType](ohos-arkui-advanced-treeview.md#treelistentype) | 是 | 监听类型。 |
| callback | (callbackParam: [CallbackParam](ohos-arkui-advanced-treeview.md#callbackparam)) => void | 是 | 节点信息。 |

### once

PhonePC/2in1TabletTVWearable

once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void;

注册一次监听。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TreeListenType](ohos-arkui-advanced-treeview.md#treelistentype) | 是 | 监听类型。 |
| callback | (callbackParam: [CallbackParam](ohos-arkui-advanced-treeview.md#callbackparam)) => void | 是 | 节点信息。 |

### off

PhonePC/2in1TabletTVWearable

off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void;

取消监听。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TreeListenType](ohos-arkui-advanced-treeview.md#treelistentype) | 是 | 监听类型。 |
| callback | (callbackParam: [CallbackParam](ohos-arkui-advanced-treeview.md#callbackparam)) => void | 否 | 节点信息。传入时取消对应的节点信息的监听，否则取消该类型的所有节点信息的监听。 |

## TreeListenType

PhonePC/2in1TabletTVWearable

定义树视图节点的监听事件类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NODE\_CLICK | "NodeClick" | 监听节点点击事件。 |
| NODE\_ADD | "NodeAdd" | 监听节点增加事件。 |
| NODE\_DELETE | "NodeDelete" | 监听节点删除事件。 |
| NODE\_MODIFY | "NodeModify" | 监听节点修改事件。 |
| NODE\_MOVE | "NodeMove" | 监听节点移动事件。 |

## CallbackParam

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentNodeId | number | 否 | 否 | 返回当前子节点id。  取值范围：大于等于0。 |
| parentNodeId | number | 否 | 是 | 返回当前父节点id。  取值范围：大于等于-1。  默认值：-1 |
| childIndex | number | 否 | 是 | 返回子索引。  取值范围：大于等于-1。  默认值：-1 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置简单树视图）

通过树视图组件的控制器对树的节点进行新增、删除、重命名，展示新增不同参数节点的实现效果。

```
1. import { TreeController, TreeListener, TreeListenerManager, TreeListenType, NodeParam, TreeView, CallbackParam } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TreeViewDemo {
6. private treeController: TreeController = new TreeController();
7. private treeListener: TreeListener = TreeListenerManager.getInstance().getTreeListener();
8. @State clickId: number = 0;

10. aboutToDisappear(): void {
11. this.treeListener.off(TreeListenType.NODE_CLICK, undefined);
12. this.treeListener.off(TreeListenType.NODE_ADD, undefined);
13. this.treeListener.off(TreeListenType.NODE_DELETE, undefined);
14. this.treeListener.off(TreeListenType.NODE_MOVE, undefined);
15. }

17. @Builder menuBuilder1() {
18. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
19. Text('新增').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
20. .onClick((event: ClickEvent) => {
21. this.treeController.addNode();
22. })
23. Divider()
24. Text('删除').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
25. .onClick((event: ClickEvent) => {
26. this.treeController.removeNode();
27. })
28. Divider()
29. Text('重命名').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
30. .onClick((event: ClickEvent) => {
31. this.treeController.modifyNode();
32. })
33. }.width(100).border({width: 1, color: 0x80808a, radius: '16dp'})
34. }

36. aboutToAppear(): void {
37. this.treeListener.on(TreeListenType.NODE_CLICK, (callbackParam: CallbackParam) => {
38. this.clickId = callbackParam.currentNodeId;
39. })
40. this.treeListener.on(TreeListenType.NODE_ADD, (callbackParam: CallbackParam) => {
41. this.clickId = callbackParam.currentNodeId;
42. })
43. this.treeListener.on(TreeListenType.NODE_DELETE, (callbackParam: CallbackParam) => {
44. this.clickId = callbackParam.currentNodeId;
45. })
46. this.treeListener.once(TreeListenType.NODE_MOVE, (callbackParam: CallbackParam) => {
47. this.clickId = callbackParam.currentNodeId;
48. })

50. let normalResource: Resource = $r('sys.media.ohos_ic_normal_white_grid_folder');
51. let selectedResource: Resource = $r('sys.media.ohos_ic_public_select_all');
52. let editResource: Resource = $r('sys.media.ohos_ic_public_edit');
53. let nodeParam: NodeParam = { parentNodeId:-1, currentNodeId: 1, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
54. editIcon: editResource, primaryTitle: "目录1验证悬浮框自适应效果是否OK",
55. secondaryTitle: "6" };
56. this.treeController
57. .addNode(nodeParam)
58. .addNode({parentNodeId:1, currentNodeId: 2, isFolder: false, primaryTitle: "项目1_1" })
59. .addNode({ parentNodeId:-1, currentNodeId: 7, isFolder: true, primaryTitle: "目录2" })
60. .addNode({ parentNodeId:-1, currentNodeId: 23, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
61. editIcon: editResource, primaryTitle: "目录3" })
62. .addNode({ parentNodeId:-1, currentNodeId: 24, isFolder: false, primaryTitle: "项目4" })
63. .addNode({ parentNodeId:-1, currentNodeId: 31, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
64. editIcon: editResource, primaryTitle: "目录5", secondaryTitle: "0" })
65. .addNode({ parentNodeId:-1, currentNodeId: 32, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
66. editIcon: editResource, primaryTitle: "目录6", secondaryTitle: "0" })
67. .addNode({ parentNodeId:32, currentNodeId: 35, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
68. editIcon: editResource, primaryTitle: "目录6-1", secondaryTitle: "0" })
69. .addNode({ parentNodeId:-1, currentNodeId: 33, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
70. editIcon: editResource, primaryTitle: "目录7", secondaryTitle: "0" })
71. .addNode({ parentNodeId:33, currentNodeId: 34, isFolder: false, primaryTitle: "项目8" })
72. .addNode({ parentNodeId:-1, currentNodeId: 36, isFolder: false, primaryTitle: "项目9" })
73. .buildDone();
74. this.treeController.refreshNode(-1, "父节点", "子节点");
75. }

77. build() {
78. Column(){
79. SideBarContainer(SideBarContainerType.Embed)
80. {
81. TreeView({ treeController: this.treeController })
82. Row() {
83. Divider().vertical(true).strokeWidth(2).color(0x000000).lineCap(LineCapStyle.Round)
84. Column({ space: 30 }) {
85. Text('ClickId=' + this.clickId).fontSize('16fp')
86. Button('Add', { type: ButtonType.Normal, stateEffect: true })
87. .borderRadius(8).backgroundColor(0x317aff).width(90)
88. .onClick((event: ClickEvent) => {
89. this.treeController.addNode();
90. })
91. Button('Modify', { type: ButtonType.Normal, stateEffect: true })
92. .borderRadius(8).backgroundColor(0x317aff).width(90)
93. .onClick((event: ClickEvent) => {
94. this.treeController.modifyNode();
95. })
96. Button('Remove', { type: ButtonType.Normal, stateEffect: true })
97. .borderRadius(8).backgroundColor(0x317aff).width(120)
98. .onClick((event: ClickEvent) => {
99. this.treeController.removeNode();
100. })
101. }.height('100%').width('70%').alignItems(HorizontalAlign.Start).margin(10)
102. }
103. }
104. .focusable(true)
105. .showControlButton(false)
106. .showSideBar(true)
107. }
108. }}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/jRFQQfKBRIyGx8DcACJQ4w/zh-cn_image_0000002583480139.png?HW-CC-KV=V1&HW-CC-Date=20260428T000242Z&HW-CC-Expire=86400&HW-CC-Sign=33ED9A49157EC8250D8D34A9E30913F9F06B33446F256D2BDC0644DB898D4BBE)

### 示例2（设置Symbol类型图标）

从API version 18开始，该示例通过设置NodeParam的属性symbolIconStyle、symbolEditIconStyle、symbolSelectedIconStyle，展示了自定义Symbol类型图标。

```
1. import { TreeController, TreeListener, TreeListenerManager, TreeListenType, NodeParam, TreeView, CallbackParam,
2. SymbolGlyphModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TreeViewDemo {
7. private treeController: TreeController = new TreeController();
8. private treeListener: TreeListener = TreeListenerManager.getInstance().getTreeListener();
9. @State clickNodeId: number = 0;

11. aboutToDisappear(): void {
12. this.treeListener.off(TreeListenType.NODE_CLICK, undefined);
13. this.treeListener.off(TreeListenType.NODE_ADD, undefined);
14. this.treeListener.off(TreeListenType.NODE_DELETE, undefined);
15. this.treeListener.off(TreeListenType.NODE_MOVE, undefined);
16. }

18. @Builder menuBuilder1() {
19. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
20. Text('新增').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
21. .onClick((event: ClickEvent) => {
22. this.treeController.addNode();
23. })
24. Divider()
25. Text('删除').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
26. .onClick((event: ClickEvent) => {
27. this.treeController.removeNode();
28. })
29. Divider()
30. Text('重命名').fontSize(16).width(100).height(30).textAlign(TextAlign.Center)
31. .onClick((event: ClickEvent) => {
32. this.treeController.modifyNode();
33. })
34. }.width(100).border({width: 1, color: 0x80808a, radius: '16dp'})
35. }

37. aboutToAppear(): void {
38. this.treeListener.on(TreeListenType.NODE_CLICK, (callbackParam: CallbackParam) => {
39. this.clickNodeId = callbackParam.currentNodeId;
40. })
41. this.treeListener.on(TreeListenType.NODE_ADD, (callbackParam: CallbackParam) => {
42. this.clickNodeId = callbackParam.currentNodeId;
43. })
44. this.treeListener.on(TreeListenType.NODE_DELETE, (callbackParam: CallbackParam) => {
45. this.clickNodeId = callbackParam.currentNodeId;
46. })
47. this.treeListener.once(TreeListenType.NODE_MOVE, (callbackParam: CallbackParam) => {
48. this.clickNodeId = callbackParam.currentNodeId;
49. })

51. let normalResource: Resource = $r('sys.symbol.house');
52. let selectedResource: Resource = $r('sys.symbol.car');
53. let editResource: Resource = $r('sys.symbol.calendar');
54. let normalSymbolResource: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Red]);
55. let selectedSymbolResource: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor([Color.Blue]);
56. let editSymbolResource: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.cake')).fontColor([Color.Pink]);
57. let nodeParam: NodeParam = { parentNodeId:-1, currentNodeId: 1, isFolder: true, icon: normalResource, selectedIcon: selectedResource,
58. editIcon: editResource, primaryTitle: "目录1",
59. secondaryTitle: "6" };
60. this.treeController
61. .addNode(nodeParam)
62. .addNode({parentNodeId:1, currentNodeId: 2, isFolder: false, primaryTitle: "项目1_1" })
63. .addNode({ parentNodeId:-1, currentNodeId: 7, isFolder: true, primaryTitle: "目录2" })
64. .addNode({ parentNodeId:-1, currentNodeId: 23, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
65. selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
66. symbolEditIconStyle: editSymbolResource, primaryTitle: "目录3" })
67. .addNode({ parentNodeId:-1, currentNodeId: 24, isFolder: false, primaryTitle: "项目4" })
68. .addNode({ parentNodeId:-1, currentNodeId: 31, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
69. selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
70. symbolEditIconStyle: editSymbolResource, primaryTitle: "目录5", secondaryTitle: "0" })
71. .addNode({ parentNodeId:-1, currentNodeId: 32, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
72. selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
73. symbolEditIconStyle: editSymbolResource, primaryTitle: "目录6", secondaryTitle: "0" })
74. .addNode({ parentNodeId:32, currentNodeId: 35, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
75. selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
76. symbolEditIconStyle: editSymbolResource, primaryTitle: "目录6-1", secondaryTitle: "0" })
77. .addNode({ parentNodeId:-1, currentNodeId: 33, isFolder: true, icon: normalResource, symbolIconStyle: normalSymbolResource,
78. selectedIcon: selectedResource, symbolSelectedIconStyle: selectedSymbolResource, editIcon: editResource,
79. symbolEditIconStyle: editSymbolResource, primaryTitle: "目录7", secondaryTitle: "0" })
80. .addNode({ parentNodeId:33, currentNodeId: 34, isFolder: false, primaryTitle: "项目8" })
81. .addNode({ parentNodeId:-1, currentNodeId: 36, isFolder: false, primaryTitle: "项目9" })
82. .buildDone();
83. this.treeController.refreshNode(-1, "父节点", "子节点");
84. }

86. build() {
87. Column(){
88. SideBarContainer(SideBarContainerType.Embed)
89. {
90. TreeView({ treeController: this.treeController })
91. Row() {
92. Divider().vertical(true).strokeWidth(2).color(0x000000).lineCap(LineCapStyle.Round)
93. Column({ space: 30 }) {
94. Text('ClickNodeId=' + this.clickNodeId).fontSize('16fp')
95. Button('Add', { type: ButtonType.Normal, stateEffect: true })
96. .borderRadius(8).backgroundColor(0x317aff).width(90)
97. .onClick((event: ClickEvent) => {
98. this.treeController.addNode();
99. })
100. Button('Modify', { type: ButtonType.Normal, stateEffect: true })
101. .borderRadius(8).backgroundColor(0x317aff).width(90)
102. .onClick((event: ClickEvent) => {
103. this.treeController.modifyNode();
104. })
105. Button('Remove', { type: ButtonType.Normal, stateEffect: true })
106. .borderRadius(8).backgroundColor(0x317aff).width(120)
107. .onClick((event: ClickEvent) => {
108. this.treeController.removeNode();
109. })
110. }.height('100%').width('80%').alignItems(HorizontalAlign.Start).margin(10)
111. }
112. }
113. .focusable(true)
114. .showControlButton(false)
115. .showSideBar(true)
116. }
117. }}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/AaXRwHuWQy6MKS2HHvAOrg/zh-cn_image_0000002552800490.png?HW-CC-KV=V1&HW-CC-Date=20260428T000242Z&HW-CC-Expire=86400&HW-CC-Sign=40A25254439EF21973928343596B9457B2B6ED80949F1390F8B2CB76919929DA)
