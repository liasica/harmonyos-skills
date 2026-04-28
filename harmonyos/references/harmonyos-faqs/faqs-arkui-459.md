---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-459
title: FrameNode的isAttached接口是否可以判断FrameNode节点出现在屏幕上
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > FrameNode的isAttached接口是否可以判断FrameNode节点出现在屏幕上
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b6a0d68dd39f532f34e236185b5acc5fbcfcd3a59aefd8fa6c069b75f84b69ea
---

FrameNode的isAttached接口原本设计是节点是否被挂载到主节点树上，与其是否出现在屏幕上无关，不在屏幕上的节点也可能已挂载到主树上（例如用ForEach构建List场景），不建议使用该接口进行判断。

如果当前想判断节点是否被挂载到主节点树上，可以使用以下替代方案：

```
1. import { FrameNode, NodeController, UIContext } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. rootNode: FrameNode | null = null;
5. node1: FrameNode | null = null;
6. node2: FrameNode | null = null;

8. makeNode(uiContext: UIContext): FrameNode | null {
9. this.rootNode = new FrameNode(uiContext);
10. this.node1 = new FrameNode(uiContext);
11. this.node1.commonAttribute.id('node1'); // Set id
12. this.node2 = new FrameNode(uiContext);
13. this.node2.commonAttribute.id('node2'); // Set id
14. this.rootNode.appendChild(this.node1); // Node1 on the main tree, node2 not on the main tree.
15. return this.rootNode;
16. }
17. }

19. @Entry
20. @Component
21. struct Index {
22. myNodeController: MyNodeController = new MyNodeController();

24. build() {
25. Column() {
26. NodeContainer(this.myNodeController)
27. Button('Click')
28. .onClick(() => {
29. // If the node cannot be obtained through getAttachedFrameNodeById, it indicates that the node has not been mounted to the main tree.
30. console.info(`node1 is attached to main tree: ${(this.getUIContext().getAttachedFrameNodeById('node1') !==
31. null)}`);
32. console.info(`node2 is attached to main tree: ${(this.getUIContext().getAttachedFrameNodeById('node2') !==
33. null)}`);
34. })
35. }
36. }
37. }
```

[FrameNodeJudgmentNode.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FrameNodeJudgmentNode.ets#L21-L58)
