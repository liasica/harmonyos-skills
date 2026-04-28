---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer
title: NodeContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义占位组件 > NodeContainer
category: harmonyos-references
scraped_at: 2026-04-28T08:02:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:13ff4360a82408f716321f2c2c17e66971d523d2947c12ee077f7b226732ba6b
---

基础组件，用于挂载自定义节点（如[FrameNode](js-apis-arkui-framenode.md)或[BuilderNode](js-apis-arkui-buildernode.md)），并通过[NodeController](js-apis-arkui-nodecontroller.md)动态控制节点的上树和下树。组件不支持尾随添加子节点，接受一个[NodeController](js-apis-arkui-nodecontroller.md)实例接口，需与NodeController组合使用。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件下仅支持挂载自定义节点[FrameNode](js-apis-arkui-framenode.md)或者是[BuilderNode](js-apis-arkui-buildernode.md)中获取的根节点FrameNode。

不支持挂载查询获得的系统组件[代理节点](js-apis-arkui-framenode.md#ismodifiable12)。

当前不支持使用[动态属性设置](ts-universal-attributes-attribute-modifier.md)。

该组件下的节点树构建时会使用UI实例[UIContext](arkts-apis-uicontext-uicontext.md)，实例切换时可能会因实例不匹配，导致所绑定[NodeController](js-apis-arkui-nodecontroller.md)的[makeNode](js-apis-arkui-nodecontroller.md#makenode)回调方法的入参为undefined，因此该组件当前不支持跨实例的节点复用。

该组件未销毁时，不会主动触发挂载节点的下树。

## 子组件

PhonePC/2in1TabletTVWearable

不支持子组件。

## 接口

PhonePC/2in1TabletTVWearable

### NodeContainer

PhonePC/2in1TabletTVWearable

NodeContainer(controller: NodeController)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [NodeController](js-apis-arkui-nodecontroller.md) | 是 | NodeController用于控制NodeContainer中的节点的上树和下树，反映NodeContainer容器的生命周期。 |

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

通过NodeController挂载BuilderNode节点。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. declare class Params {
4. text: string
5. }

7. @Builder
8. function buttonBuilder(params: Params) {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {
10. Text(params.text)
11. .fontSize(12)
12. Button(`This is a Button`, { type: ButtonType.Normal, stateEffect: true })
13. .fontSize(12)
14. .borderRadius(8)
15. .backgroundColor(0x317aff)
16. }
17. .height(100)
18. .width(200)
19. }

21. class MyNodeController extends NodeController {
22. private rootNode: BuilderNode<[Params]> | null = null;
23. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

25. makeNode(uiContext: UIContext): FrameNode | null {
26. if (this.rootNode === null) {
27. this.rootNode = new BuilderNode(uiContext);
28. this.rootNode.build(this.wrapBuilder, { text: "This is a Text" })
29. }
30. return this.rootNode.getFrameNode();
31. }
32. }

35. @Entry
36. @Component
37. struct Index {
38. private baseNode: MyNodeController = new MyNodeController()

40. build() {
41. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {
42. Text("This is a NodeContainer contains a text and a button ")
43. .fontSize(9)
44. .fontColor(0xCCCCCC)
45. NodeContainer(this.baseNode)
46. .borderWidth(1)
47. .onClick(() => {
48. console.info("click event");
49. })
50. }
51. .padding({ left: 35, right: 35, top: 35 })
52. .height(200)
53. .width(300)
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/r061eLBHSf2ddwhzDljwLA/zh-cn_image_0000002552800440.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000227Z&HW-CC-Expire=86400&HW-CC-Sign=4E3E1F6ED4F4F5A3952F7493D31282BA05AA1E18EF429755268C245ECF611330)
