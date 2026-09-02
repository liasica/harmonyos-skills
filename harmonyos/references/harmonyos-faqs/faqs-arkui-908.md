---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-908
title: 使用NodeController加载不同模板函数
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用NodeController加载不同模板函数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ed5443235e9530dcf66e06578a3136429e9e878714e10717b383ea33d5e17e9
---

## 问题现象

当存在多个不同效果的UI模板时，除了在组件内使用if渲染机制去处理不同显示效果外，是否存在更简洁、高效的写法？

## 背景知识

* [NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)用于实现自定义节点的创建、显示、更新等操作，并负责将自定义节点挂载到[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)上。NodeContainer是一个自定义占位组件，接受一个NodeController的实例接口。
* [BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)是挂载系统组件的自定义节点。
* [FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)表示组件树的实体节点。NodeController可通过BuilderNode持有的FrameNode将其挂载到NodeContainer上。

## 解决方案

使用NodeController创建自定义节点，将模板函数挂载到该节点中，并根据需要调用其中的模板函数。调用不同UI模板的逻辑在模板函数中执行，可以提高代码复用性，同时防止组件内使用if渲染机制造成性能浪费。

1. 使用Builder函数构建显示模板，其中参数抽出使用一个单独的类Params实现，并通过参数决定显示具体的UI模板。
2. 使用NodeController创建自定义节点，使用wrapBuilder方法封装模板函数，挂载到BuilderNode上。再通过FrameNode将BuilderNode挂载到NodeContainer上。
3. 创建自定义节点实例，根据id决定自定义节点的UI模板，同时将实例存入nodeMap中。
4. 在build构建函数中使用NodeContainer。

* 定义模板函数及其参数类：

  ```ts
  declare class Params {
    id: string;
    isButton: boolean;
  }

  @Builder
  export function myBuilder(param: Params) {
    myComponent({ params: param });
  }

  @Component
  struct myComponent {
    params ?: Params;

    build() {
      if (this.params!.isButton) {
        ButtonBuilder();
      } else {
        TextBuilder();
      }
    }
  }

  @Builder
  function ButtonBuilder() {
    Flex() {
      Button(`This is a Button`, {
        type: ButtonType.Normal,
        stateEffect: true
      }).fontSize(12).borderRadius(8).backgroundColor(0x317aff);
    }.height(100).width(200);
  }

  @Builder
  function TextBuilder() {
    Flex() {
      Text(`This is a Text`).fontSize(16);
    }.height(100).width(200);
  }
  ```
* 使用NodeController构建自定义节点：

  ```ts
  // 自定义节点
  export class MyNodeController extends NodeController {
    private rootNode: FrameNode | null = null;
    private adNode: BuilderNode<[Params]> | null = null;
    private uiContext ?: UIContext;

    // 当NodeContainer进行绘制时，会调用makeNode()方法，将构建好的rootNode返回实现组件上树。
    makeNode(): FrameNode | null {
      if (this.rootNode != null) {
        return this.rootNode;
      }
      return null;
    }

    // 初始化过程，通过判断queryById获取的Type是否为'button'来决定myBuilder调用哪种模板
    init(uiContext: UIContext, id: string, Type: string) {
      this.uiContext = uiContext;
      this.rootNode = new FrameNode(this.uiContext);
      this.adNode = new BuilderNode(this.uiContext);
      this.adNode.build(wrapBuilder(myBuilder), { id: id, isButton: Type === 'button' });
      this.rootNode.getRenderNode()?.appendChild(this.adNode.getFrameNode()?.getRenderNode());
    }
  }
  ```
* 创建自定义节点实例和构建nodeMap：

  ```ts
  let nodeMap: Map<string, MyNodeController | undefined> = new Map();

  // 在组件中执行，通过组件中获取的参数创建MyNodeController实例
  const getAdNodeController = (uiContext: UIContext, id: string): MyNodeController | undefined => {
    let baseNode = new MyNodeController();
    nodeMap.set(id, baseNode);
    baseNode.init(uiContext, id, queryById(id));
    return nodeMap.get(id);
  };

  // 假设id能被2整除则为Button，否则为Text
  function queryById(id: string): string {
    if (Number(id) % 2 === 0) {
      return 'button';
    } else {
      return 'text';
    }
  }
  ```
* 调用NodeContainer：

  ```ts
  export class CardData {
    private id: string = '';

    constructor(id: string) {
      this.id = id;
    }

    public getId(): string {
      return this.id;
    }
  }

  @Entry
  @Component
  struct NodeControllerDemo {
    private data: CardData[] = [
      new CardData('1'), // Text
      new CardData('2')// Button
    ];

    build() {
      Flex({}) {
        List({ space: 3 }) {
          ForEach(this.data, (item: CardData) => {
            ListItem() {
              NodeContainer(getAdNodeController(this.getUIContext(), item.getId())).width('100%');
            };
          }, (item: CardData) => item.getId());
        }
        .width('100%')
        .height('100%');
      }.padding({
        left: 35,
        right: 35,
        top: 35
      }).height(200).width('100%');
    }
  }
  ```
* 完整示例代码如下：

  ```ts
  import { UIContext } from '@ohos.arkui.UIContext';
  import { NodeController, BuilderNode, FrameNode } from '@ohos.arkui.node';

  declare class Params {
    id: string;
    isButton: boolean;
  }

  @Builder
  export function myBuilder(param: Params) {
    myComponent({ params: param });
  }

  @Component
  struct myComponent {
    params ?: Params;

    build() {
      if (this.params!.isButton) {
        ButtonBuilder();
      } else {
        TextBuilder();
      }
    }
  }

  @Builder
  function ButtonBuilder() {
    Flex() {
      Button(`This is a Button`, {
        type: ButtonType.Normal,
        stateEffect: true
      }).fontSize(12).borderRadius(8).backgroundColor(0x317aff);
    }.height(100).width(200);
  }

  @Builder
  function TextBuilder() {
    Flex() {
      Text(`This is a Text`).fontSize(16);
    }.height(100).width(200);
  }

  // 自定义节点
  export class MyNodeController extends NodeController {
    private rootNode: FrameNode | null = null;
    private adNode: BuilderNode<[Params]> | null = null;
    private uiContext ?: UIContext;

    // 当NodeContainer进行绘制时，会调用makeNode()方法，将构建好的rootNode返回实现组件上树。
    makeNode(): FrameNode | null {
      if (this.rootNode != null) {
        return this.rootNode;
      }
      return null;
    }

    // 初始化过程，通过判断queryById获取的Type是否为'button'来决定myBuilder调用哪种模板
    init(uiContext: UIContext, id: string, Type: string) {
      this.uiContext = uiContext;
      this.rootNode = new FrameNode(this.uiContext);
      this.adNode = new BuilderNode(this.uiContext);
      this.adNode.build(wrapBuilder(myBuilder), { id: id, isButton: Type === 'button' });
      this.rootNode.getRenderNode()?.appendChild(this.adNode.getFrameNode()?.getRenderNode());
    }
  }

  let nodeMap: Map<string, MyNodeController | undefined> = new Map();

  // 在组件中执行，通过组件中获取的参数创建MyNodeController实例
  const getAdNodeController = (uiContext: UIContext, id: string): MyNodeController | undefined => {
    let baseNode = new MyNodeController();
    nodeMap.set(id, baseNode);
    baseNode.init(uiContext, id, queryById(id));
    return nodeMap.get(id);
  };

  // 假设id能被2整除则为Button，否则为Text
  function queryById(id: string): string {
    if (Number(id) % 2 === 0) {
      return 'button';
    } else {
      return 'text';
    }
  }

  export class CardData {
    private id: string = '';

    constructor(id: string) {
      this.id = id;
    }

    public getId(): string {
      return this.id;
    }
  }

  @Entry
  @Component
  struct NodeControllerDemo {
    private data: CardData[] = [
      new CardData('1'), // Text
      new CardData('2')// Button
    ];

    build() {
      Flex({}) {
        List({ space: 3 }) {
          ForEach(this.data, (item: CardData) => {
            ListItem() {
              NodeContainer(getAdNodeController(this.getUIContext(), item.getId())).width('100%');
            };
          }, (item: CardData) => item.getId());
        }
        .width('100%')
        .height('100%');
      }.padding({
        left: 35,
        right: 35,
        top: 35
      }).height(200).width('100%');
    }
  }
  ```
