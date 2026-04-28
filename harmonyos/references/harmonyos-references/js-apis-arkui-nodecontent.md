---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontent
title: NodeContent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > NodeContent
category: harmonyos-references
scraped_at: 2026-04-28T08:00:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4db481f0cffd6263159cd294eb7a27386bd3f778769aaca477ad98639deb425f
---

NodeContent是ArkUI提供的[ContentSlot](ts-components-contentslot.md)的管理器。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* NodeContent对象不支持使用JSON序列化。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { NodeContent } from '@kit.ArkUI';
```

## NodeContent

PhonePC/2in1TabletTVWearable

NodeContent是节点内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor()

节点内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { nativeNode } from 'libNativeNode.so'; // 开发者自己实现的so
2. import { NodeContent } from '@kit.ArkUI';

4. @Component
5. struct Parent {
6. private nodeContent: Content = new NodeContent();

8. aboutToAppear() {
9. // 通过C-API创建节点，并添加到管理器nodeContent上
10. nativeNode.createNativeNode(this.nodeContent);
11. }

13. build() {
14. Column() {
15. // 显示nodeContent管理器里存放的Native侧的组件
16. ContentSlot(this.nodeContent)
17. }
18. }
19. }
```

上述代码中so的实现可参考[Native XComponent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeXComponentSample)。

### addFrameNode12+

PhonePC/2in1TabletTVWearable

addFrameNode(node: FrameNode): void

根据参数将FrameNode添加到NodeContent中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 需要添加的FrameNode。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted." |

### removeFrameNode12+

PhonePC/2in1TabletTVWearable

removeFrameNode(node: FrameNode): void

根据参数将FrameNode从NodeContent中删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | 需要删除的FrameNode。 |

**示例：**

添加删除NodeContent中的FrameNode节点。

```
1. // xxx.ets
2. import { NodeContent, typeNode } from '@kit.ArkUI';

4. class NodeContentCtrl {
5. content: NodeContent;
6. textNode: Array<typeNode.Text> = new Array();
7. uiContext: UIContext;
8. width: number;

10. constructor(uiContext: UIContext) {
11. this.content = new NodeContent();
12. this.uiContext = uiContext;
13. this.width = Infinity;
14. }

16. AddNode() {
17. let node = typeNode.createNode(this.uiContext, "Text");
18. node.initialize("ContentText:" + this.textNode.length).fontSize(20);
19. this.textNode.push(node);
20. this.content.addFrameNode(node);
21. }

23. RemoveNode() {
24. let node = this.textNode.pop();
25. this.content.removeFrameNode(node);
26. }

28. RemoveFront() {
29. let node = this.textNode.shift();
30. this.content.removeFrameNode(node);
31. }

33. GetContent(): NodeContent {
34. return this.content;
35. }
36. }

38. @Entry
39. @Component
40. struct Index {
41. @State message: string = 'Hello World';
42. controller = new NodeContentCtrl(this.getUIContext());

44. build() {
45. Row() {
46. Column() {
47. ContentSlot(this.controller.GetContent())
48. Button("AddToSlot")
49. .onClick(() => {
50. this.controller.AddNode();
51. })
52. Button("RemoveBack")
53. .onClick(() => {
54. this.controller.RemoveNode();
55. })
56. Button("RemoveFront")
57. .onClick(() => {
58. this.controller.RemoveFront();
59. })
60. }
61. .width('100%')
62. }
63. .height('100%')
64. }
65. }
```
