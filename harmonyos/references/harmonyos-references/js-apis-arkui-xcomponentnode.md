---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-xcomponentnode
title: XComponentNode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > XComponentNode
category: harmonyos-references
scraped_at: 2026-04-29T13:51:03+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:0e96ca024e0ee317dcc74e5900b154c9da01af12d0bf193ff80768ba039f42ae
---

提供XComponent节点XComponentNode，表示组件树中的[XComponent](ts-basic-components-xcomponent.md)组件，用于[EGL](egl.md)/[OpenGL ES](opengles.md)和媒体数据写入，并支持动态修改节点渲染类型。

说明

从API version 12开始废弃，建议使用[类型为XComponent的typeNode](js-apis-arkui-framenode.md#xcomponent12)的方式实现。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

当前不支持在预览器中使用XComponentNode。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { XComponentNode } from "@kit.ArkUI";
```

## XComponentNode(deprecated)

PhonePC/2in1TabletTVWearable

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, options: RenderOptions, id: string, type: XComponentType, libraryName?: string)

XComponentNode的构造函数。

说明

从API version 11开始支持，从API version 12开始废弃，建议使用[createNode](js-apis-arkui-framenode.md#createnodexcomponent12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | UI上下文，获取方式可参考[UIContext获取方法](js-apis-arkui-node.md#uicontext获取方法)。 |
| options | [RenderOptions](js-apis-arkui-buildernode.md#renderoptions) | 是 | XComponentNode的构造可选参数。 |
| id | string | 是 | XComponent的唯一标识，支持最大的字符串长度128。详见[XComponent](ts-basic-components-xcomponent.md)组件。 |
| type | [XComponentType](ts-appendix-enums.md#xcomponenttype10) | 是 | 用于指定XComponent组件类型。详见[XComponent](ts-basic-components-xcomponent.md)组件。 |
| libraryName | string | 否 | Native层编译输出动态库名称。详见[XComponent](ts-basic-components-xcomponent.md)组件。 |

说明

需要显式指定[RenderOptions](js-apis-arkui-buildernode.md#renderoptions)中的selfIdealSize，否则XComponentNode内容大小为空，不显示任何内容。

### onCreate(deprecated)

PhonePC/2in1TabletTVWearable

onCreate(event?: Object): void

XComponentNode加载完成时触发该回调。

说明

从API version 11开始支持，从API version 12开始废弃，建议使用[onLoad](ts-basic-components-xcomponent.md#onload)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Object | 否 | 获取XComponent实例对象的context，context上挂载的方法由开发者在C++层定义。 |

### onDestroy(deprecated)

PhonePC/2in1TabletTVWearable

onDestroy(): void

XComponentNode销毁时触发该回调。

说明

从API version 11开始支持，从API version 12开始废弃，建议使用[onDestroy](ts-basic-components-xcomponent.md#ondestroy)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### changeRenderType(deprecated)

PhonePC/2in1TabletTVWearable

changeRenderType(type: NodeRenderType): boolean

修改XComponentNode的渲染类型。

说明

从API version 11开始支持，从API version 12开始废弃，建议使用[appendChild](js-apis-arkui-framenode.md#appendchild12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [NodeRenderType](js-apis-arkui-buildernode.md#noderendertype) | 是 | 需要修改的渲染类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 修改渲染类型是否成功。  true：修改渲染类型成功；false：修改渲染类型失败。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. import { NodeController, FrameNode, XComponentNode, NodeRenderType, UIContext} from '@kit.ArkUI'

3. class XComponentNodeController extends NodeController {
4. private xComponentNode: MyXComponentNode | null = null;
5. private soName: string = "tetrahedron_napi" // 该 so 由开发者通过 NAPI 编写并生成

7. constructor() {
8. super();
9. }

11. makeNode(context: UIContext): FrameNode | null {
12. this.xComponentNode = new MyXComponentNode(context, {
13. selfIdealSize: { width: 200, height: 200 }
14. }, "xComponentId", XComponentType.SURFACE, this.soName);
15. return this.xComponentNode;
16. }

18. changeRenderType(renderType: NodeRenderType): void {
19. if (this.xComponentNode) {
20. this.xComponentNode.changeRenderType(renderType);
21. }
22. }
23. }

25. class MyXComponentNode extends XComponentNode {
26. onCreate(event: Object) {
27. // do something when XComponentNode has created
28. }

30. onDestroy() {
31. // do something when XComponentNode is destroying
32. }
33. }

35. @Entry
36. @Component
37. struct Index {
38. build() {
39. Row() {
40. Column() {
41. NodeContainer(new XComponentNodeController())
42. }
43. .width('100%')
44. .height('100%')
45. }
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/3_0_IuNaQHuTA-EpQCRTcA/zh-cn_image_0000002589245793.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055102Z&HW-CC-Expire=86400&HW-CC-Sign=5380B43CA47E6C95A4D1EC652BBB9F103993C5C7C935EDDF624D794990CBEA9A)
