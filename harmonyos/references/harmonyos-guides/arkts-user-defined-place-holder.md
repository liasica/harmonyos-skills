---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-place-holder
title: 自定义占位节点
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 自定义占位节点
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:327a393a5dfa08c34cc7d5e49482b13bcd04bb4fd4426695928cd4ffd62a7e53
---

ArkUI提供了系统组件[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)和[ContentSlot](../harmonyos-references/ts-components-contentslot.md)作为自定义节点的占位节点。主要用于自定义节点以及自定义节点树的显示。

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)作为容器节点存在，具备通用属性，是UI节点。[ContentSlot](arkts-rendering-control-contentslot.md)只是一个语法节点，无通用属性，不参与布局和渲染。支持混合模式开发，当容器是ArkTS组件，子组件在Native侧创建时，推荐使用ContentSlot占位组件。具体使用参考[ContentSlot](../harmonyos-references/ts-components-contentslot.md)的接口文档说明。

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)是用来占位的系统组件，主要用于自定义节点以及自定义节点树的显示，支持组件的通用属性，对通用属性的处理请参考默认左上角对齐的[Stack](../harmonyos-references/ts-container-stack.md)组件。

[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)提供了一系列生命周期回调，通过[makeNode](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)回调返回一个[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点树的根节点。将[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点树挂载到对应的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)下。同时提供了[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)、[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)、[aboutToResize](../harmonyos-references/js-apis-arkui-nodecontroller.md#abouttoresize)、[onTouchEvent](../harmonyos-references/js-apis-arkui-nodecontroller.md#ontouchevent)四个回调方法用于监听对应的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)的状态，以及[rebuild](../harmonyos-references/js-apis-arkui-nodecontroller.md#rebuild)方法用于主动触发[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)重新回调[makeNode](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)以更新子节点。

每个生命周期的回调的具体含义参考[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)的接口文档说明。

**说明** 

* NodeContainer下仅支持挂载自定义的FrameNode节点以及BuilderNode创建的组件树的根节点。
* 从API Version 12开始支持的接口，可以通过FrameNode的查询接口返回系统组件的代理节点，代理节点可以作为makeNode的返回值进行返回，但代理节点无法成功挂载在组件树上，最终的显示结果为代理节点挂载失败。
* 需要保证一个节点只能作为一个父节点的子节点去使用，否则可能存在显示异常或者功能异常，尤其是页面路由场景或者动效场景。例如，如果通过NodeController将同一个节点挂载在多个NodeContainer上，仅一个占位容器下会显示节点，且多个NodeContainer的可见性、透明度等影响子组件状态的属性更新均会影响被挂载的子节点。

## 基本概念

* 自定义节点：使用ArkUI提供的接口，以命令式创建的节点。包括自定义组件节点（[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)）、自定义渲染节点（[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)）、自定义声明式节点（[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)）、[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)等。
* 自定义节点树：根节点为自定义节点的节点树。
* 声明式节点树：根节点为声明式节点的节点树。
* 节点树：一种常见的数据结构，用于表示节点的层级关系。
* 占位节点：用于在声明式节点树上为自定义节点树预留位置的节点，主要包括NodeContainer和ContentSlot。鉴于页面的主树采用声明式节点树，因此，唯有借助占位节点，才能将命令式构建的自定义节点成功挂载至声明式节点树上。

## 使用NodeContainer挂载自定义节点

通过NodeController在NodeContainer下挂载自定义节点。

```typescript
// common.ets
import { BuilderNode, UIContext } from '@kit.ArkUI';

class Params {
  public text: string = 'this is a text';
}

let buttonNode: BuilderNode<[Params]> | null = null;

@Builder
function buttonBuilder(params: Params) {
  Column() {
    Button(params.text)
      .fontSize(12)
      .borderRadius(8)
      .borderWidth(2)
      .backgroundColor(Color.Orange)
  }
}

export function createNode(uiContext: UIContext) {
  buttonNode = new BuilderNode<[Params]>(uiContext);
  buttonNode.build(wrapBuilder(buttonBuilder), { text: 'This is a Button' });
  return buttonNode;
}

export function getOrCreateNode(uiContext: UIContext): BuilderNode<[Params]> | null {
  if (buttonNode?.getFrameNode() && buttonNode?.getFrameNode()?.getUniqueId() != -1) {
    return buttonNode;
  } else {
    return createNode(uiContext);
  }
}
```

```typescript
// Index.ets
import { FrameNode, NodeController, Size, UIContext } from '@kit.ArkUI';
import { getOrCreateNode } from './Common';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0xF811
const TAG = '[Sample_ArkTSUserPlaceHolder]';

class MyNodeController extends NodeController {
  private isShow: boolean = false;

  constructor(isShow: boolean) {
    super();
    this.isShow = isShow;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    if (!this.isShow) {
      return null;
    }
    let frameNode = getOrCreateNode(uiContext)?.getFrameNode();
    return frameNode ? frameNode : null;
  }

  aboutToResize(size: Size) {
    hilog.info(DOMAIN, TAG,' aboutToResize width : ' + size.width + ' height : ' + size.height);
  }

  aboutToAppear() {
    hilog.info(DOMAIN, TAG,' aboutToAppear');
  }

  aboutToDisappear() {
    hilog.info(DOMAIN, TAG,' aboutToDisappear');
  }

  onTouchEvent(event: TouchEvent) {
    hilog.info(DOMAIN, TAG,' onTouchEvent');
  }

  toShow() {
    this.isShow = true;
    this.rebuild();
  }

  toHide() {
    this.isShow = false;
    this.rebuild();
  }
}

@Entry
@Component
struct Index {
  private myNodeController1: MyNodeController = new MyNodeController(true);
  private myNodeController2: MyNodeController = new MyNodeController(false);

  build() {
    Column() {
      NodeContainer(this.myNodeController1)
        .width('100%')
        .height('40%')
        .backgroundColor(Color.Brown)
      NodeContainer(this.myNodeController2)
        .width('100%')
        .height('40%')
        .backgroundColor(Color.Gray)
      Button('Change the place of button')
        .onClick(() => {
          // 先在原始占位节点中下树
          // 后在新的占位节点中上树
          // 保证自定义节点仅作为一个节点的子节点存在
          this.myNodeController1.toHide();
          this.myNodeController2.toShow();
        })
    }
    .padding({ left: 35, right: 35, top: 35 })
    .width('100%')
    .height('100%')
  }
}
```

## NodeContainer和ContentSlot添加子节点布局差异

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)是一个容器节点，布局参考左上角对齐的[Stack](../harmonyos-references/ts-container-stack.md)组件，不会按照父容器的布局规则进行布局。[ContentSlot](../harmonyos-references/ts-components-contentslot.md)只是一个语法节点，不参与布局，添加的子节点会按照父容器的布局规则进行布局。

```typescript
import { FrameNode, NodeContent, NodeController, typeNode, UIContext } from '@kit.ArkUI';

class NodeContentCtrl {
  public content: NodeContent
  public textNode: Array<typeNode.Text> = [];
  public uiContext: UIContext
  public width: number

  constructor(uiContext: UIContext) {
    this.content = new NodeContent();
    this.uiContext = uiContext;
    this.width = Infinity;
  }

  AddNode() {
    let node = typeNode.createNode(this.uiContext, 'Text');
    node.initialize('ContentText:' + this.textNode.length).fontSize(20);
    this.textNode.push(node);
    this.content.addFrameNode(node);
  }

  RemoveNode() {
    let node = this.textNode.pop();
    this.content.removeFrameNode(node);
  }

  RemoveFront() {
    let node = this.textNode.shift();
    this.content.removeFrameNode(node);
  }

  GetContent(): NodeContent {
    return this.content;
  }
}

class MyNodeController extends NodeController {
  public rootNode: FrameNode | null = null;
  public textNode: Array<typeNode.Text> = [];

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    return this.rootNode;
  }

  AddNode(frameNode: FrameNode | null, uiContext: UIContext) {
    let node = typeNode.createNode(uiContext, 'Text');
    node.initialize('ControllerText:' + this.textNode.length).fontSize(20);
    this.textNode.push(node);
    frameNode?.appendChild(node);
  }

  RemoveNode(frameNode: FrameNode | null) {
    let node = this.textNode.pop();
    frameNode?.removeChild(node);
  }

  RemoveFront(frameNode: FrameNode | null) {
    let node = this.textNode.shift();
    frameNode?.removeChild(node);
  }
}

@Entry
@Component
struct Index {
  controller = new NodeContentCtrl(this.getUIContext());
  myNodeController = new MyNodeController();

  build() {
    Row() {
      Column() {
        ContentSlot(this.controller.GetContent())
        Button('AddToSlot')
          .onClick(() => {
            this.controller.AddNode();
          })
          .margin(10)
        Button('RemoveBack')
          .onClick(() => {
            this.controller.RemoveNode();
          })
          .margin(10)
        Button('RemoveFront')
          .onClick(() => {
            this.controller.RemoveFront();
          })
          .margin(10)
      }
      .width('50%')

      Column() {
        NodeContainer(this.myNodeController)
        Button('AddToNodeContainer')
          .onClick(() => {
            this.myNodeController.AddNode(this.myNodeController.rootNode, this.getUIContext());
          })
          .margin(10)
        Button('RemoveBack')
          .onClick(() => {
            this.myNodeController.RemoveNode(this.myNodeController.rootNode);
          })
          .margin(10)
        Button('RemoveFront')
          .onClick(() => {
            this.myNodeController.RemoveFront(this.myNodeController.rootNode);
          })
          .margin(10)
      }
      .width('50%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/RUj-HWJcQ5SZond2dSlh1A/zh-cn_image_0000002706673886.gif)
