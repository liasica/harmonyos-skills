---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-459
title: FrameNode的isAttached接口是否可以判断FrameNode节点出现在屏幕上
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > FrameNode的isAttached接口是否可以判断FrameNode节点出现在屏幕上
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0ca7389fe1b40fec725489ad89a990775055163da61e36e95f54aca9ebfc72b5
---

FrameNode的isAttached接口原本设计是节点是否被挂载到主节点树上，与其是否出现在屏幕上无关，不在屏幕上的节点也可能已挂载到主树上（例如用ForEach构建List场景），不建议使用该接口进行判断。

如果当前想判断节点是否被挂载到主节点树上，可以使用以下替代方案：

```ts
import { FrameNode, NodeController, UIContext } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  rootNode: FrameNode | null = null;
  node1: FrameNode | null = null;
  node2: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);
    this.node1 = new FrameNode(uiContext);
    this.node1.commonAttribute.id('node1'); // Set id
    this.node2 = new FrameNode(uiContext);
    this.node2.commonAttribute.id('node2'); // Set id
    this.rootNode.appendChild(this.node1); // Node1 on the main tree, node2 not on the main tree.
    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
      Button('Click')
        .onClick(() => {
          // If the node cannot be obtained through getAttachedFrameNodeById, it indicates that the node has not been mounted to the main tree.
          console.info(`node1 is attached to main tree: ${(this.getUIContext().getAttachedFrameNodeById('node1') !==
            null)}`);
          console.info(`node2 is attached to main tree: ${(this.getUIContext().getAttachedFrameNodeById('node2') !==
            null)}`);
        })
    }
  }
}
```
