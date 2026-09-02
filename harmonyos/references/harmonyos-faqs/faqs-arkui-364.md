---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-364
title: 如何实现组件动态上下树
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现组件动态上下树
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:34c45eebfeac8fdc960da8d1b2e939edd4465b62260fe0717e03bc7d40bd3ab5
---

可以通过ArkUI的NodeController模块，创建控制器管理绑定的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md#nodecontainer-1)组件，通过NodeController的rebuild()方法进行回调的触发，从而实现组件动态上下树，具体请参考如下代码：

```ts
import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

declare class Params {
  text: string;
}

@Builder
function textInputBuilder(params: Params) {
  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceEvenly }) {
    Text(params.text)
      .fontSize(12)
    Button(`This is a Button`, { type: ButtonType.Normal, stateEffect: true })
      .fontSize(12)
      .borderRadius(8)
      .backgroundColor(0x317aff)
  }
  .height(100)
  .width(200)
}

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null; // Create root node
  private wrappedTextInputBuilder: WrappedBuilder<[Params]> = wrapBuilder(textInputBuilder);
  private buildNode: BuilderNode<[Params]> | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext); // Root node initialization
    this.buildNode = new BuilderNode(uiContext);
    const rootRenderNode = this.rootNode.getRenderNode(); // Get rendering nodes
    if (rootRenderNode !== null) {
      this.buildNode.build(this.wrappedTextInputBuilder, { text: 'This is a Text' });
      const childNode = this.buildNode.getFrameNode()?.getRenderNode();
      if (childNode) {
        rootRenderNode.appendChild(childNode); // Add new child nodes after rendering nodes
        console.info('rootRenderNode.appendChild');
      }
    }
    return this.rootNode;
  }
}

@Entry
@Component
struct RenderNode_pages {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceEvenly }) {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .height(500)
        .width(330)

      Button(`Adding a Node`, { type: ButtonType.Normal, stateEffect: true })
        .fontSize(12)
        .borderRadius(8)
        .backgroundColor(0x317aff)
        .onClick(() => {
          this.myNodeController.rebuild();
        })
    }
    .padding({ left: 35, right: 35, top: 35 })
    .height(500)
    .width(500)
  }
}
```

**参考链接**

[rebuild](../harmonyos-references/js-apis-arkui-nodecontroller.md#rebuild)
