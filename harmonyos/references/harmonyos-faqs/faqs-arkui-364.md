---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-364
title: 如何实现组件动态上下树
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现组件动态上下树
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cb6cad44d8b1a80b2e4e6def2c2789541320f77f610d23589d8932729993d69a
---

可以通过ArkUI的NodeController模块，创建控制器管理绑定的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md#nodecontainer-1)组件，通过NodeController的rebuild()方法进行回调的触发，从而实现组件动态上下树，具体请参考如下代码：

```
1. import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

3. declare class Params {
4. text: string;
5. }

7. @Builder
8. function textInputBuilder(params: Params) {
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
22. private rootNode: FrameNode | null = null; // Create root node
23. private wrappedTextInputBuilder: WrappedBuilder<[Params]> = wrapBuilder(textInputBuilder);
24. private buildNode: BuilderNode<[Params]> | null = null;

26. makeNode(uiContext: UIContext): FrameNode | null {
27. this.rootNode = new FrameNode(uiContext); // Root node initialization
28. this.buildNode = new BuilderNode(uiContext);
29. const rootRenderNode = this.rootNode.getRenderNode(); // Get rendering nodes
30. if (rootRenderNode !== null) {
31. this.buildNode.build(this.wrappedTextInputBuilder, { text: 'This is a Text' });
32. const childNode = this.buildNode.getFrameNode()?.getRenderNode();
33. if (childNode) {
34. rootRenderNode.appendChild(childNode); // Add new child nodes after rendering nodes
35. console.info('rootRenderNode.appendChild');
36. }
37. }
38. return this.rootNode;
39. }
40. }

42. @Entry
43. @Component
44. struct RenderNode_pages {
45. private myNodeController: MyNodeController = new MyNodeController();

47. build() {
48. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {
49. NodeContainer(this.myNodeController)
50. .borderWidth(1)
51. .height(500)
52. .width(330)

54. Button(`Adding a Node`, { type: ButtonType.Normal, stateEffect: true })
55. .fontSize(12)
56. .borderRadius(8)
57. .backgroundColor(0x317aff)
58. .onClick(() => {
59. this.myNodeController.rebuild();
60. })
61. }
62. .padding({ left: 35, right: 35, top: 35 })
63. .height(500)
64. .width(500)
65. }
66. }
```

[ImplementDynamicComponentTreeUpAndDown.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementDynamicComponentTreeUpAndDown.ets#L21-L87)

**参考链接**

[rebuild](../harmonyos-references/js-apis-arkui-nodecontroller.md#rebuild)
