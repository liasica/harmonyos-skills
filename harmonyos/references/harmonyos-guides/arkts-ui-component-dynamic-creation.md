---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-component-dynamic-creation
title: 组件动态创建
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 组件动态创建
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:39abba76137f060c083f9578f98fe3f0814d368d3652b227bcb1a79a47abdca0
---

## 概述

为了解决页面、组件加载缓慢的问题，ArkUI框架提供了动态操作以实现组件预创建，并允许应用在运行时根据实际需要加载渲染相应的组件。动态操作包含动态创建组件（动态添加组件）、动态卸载组件（动态删除组件）等相关操作。动态创建组件指在非build生命周期中进行组件创建，即在build生命周期前提前创建组件。通过动态创建组件，不但可以节省组件创建的时间，提升用户体验，还可以将独立的逻辑进行封装，有助于应用模块化开发。动态卸载组件是对动态创建的组件进行卸载、删除。

## 组件预创建原理

在声明式范式中，组件仅在build环节中被创建，开发者无法在其他生命周期阶段进行组件的创建，从而引起页面加载慢等问题。与声明式范式不同，ArkUI框架提供的UI动态操作支持组件的预创建。组件预创建可以满足开发者在非build生命周期中进行组件创建，创建后的组件可以进行属性设置、布局计算等操作。之后在页面加载时进行使用，可以极大提升页面响应速度。

如下图所示，利用组件预创建机制，可以利用动画执行过程空闲时间进行组件预创建和属性设置。在动画结束后，再进行属性和布局的更新，节省了组件创建的时间，从而加快了页面渲染。

**图 1** 组件预创建原理图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/nEzLeOeFSpCoc6Wsz-BwRQ/zh-cn_image_0000002706833836.jpg)

## FrameNode自定义节点在动态布局场景下的优势

### 减少自定义组件创建开销

在采用声明式开发范式中，若使用ArkUI的自定义组件对节点树中的每个节点进行定义，往往会遇到节点创建效率低下的问题。

这主要是因为每个节点在ArkTS引擎中都需要分配内存空间来存储应用程序的自定义组件和状态变量。在节点创建过程中，还必须执行组件ID、组件闭包以及状态变量之间的依赖关系收集等操作。

相比之下，使用ArkUI的[自定义组件节点 (FrameNode)](arkts-user-defined-arktsnode-framenode.md)，可以避免创建自定义组件对象和状态变量对象，无需进行依赖收集，从而显著提升组件创建的速度。

### 组件更新更快

在动态布局类框架的更新场景中，通常存在一个由树形数据结构ViewModelA创建的UI组件树TreeA。当需要使用新的数据结构ViewModelB来更新TreeA时，尽管声明式开发范式可以实现数据驱动的自动更新，但这一过程中却伴随着大量的diff操作，如下图所示。对于ArkTS引擎而言，在对一个复杂组件树（深度超过30层，包含100至200个组件）执行diff算法时，几乎无法在120Hz的刷新率下保持满帧运行。然而，使用ArkUI的FrameNode扩展，框架能够自主掌控更新流程，实现高效的按需剪枝。特别是针对那些仅服务于少数特定业务的动态布局框架，利用这一扩展，可以实现快速的更新操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zXMhuDDnSNOdYoe0FCf3vw/zh-cn_image_0000002736312945.png)

### 直接操作组件树

使用声明式开发范式还存在组件树结构更新操作困难的痛点，比如将组件树中的一个子树从当前子节点完整移到另一个子节点，使用声明式开发范式无法直接调整组件实例的结构关系，只能通过重新渲染整棵组件树的方式实现上述操作。而使用ArkUI的FrameNode扩展，则可以通过操作FrameNode来很方便的操控该子树，将其移植到另一个节点，这样只会进行局部渲染刷新，性能更优。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/4waC455QRWejKO54nRJ0tA/zh-cn_image_0000002706673902.png)

## 组件动态添加、更新和删除：

### 动态添加组件

动态添加组件包括以下步骤：

1. 创建自定义节点。
2. 实现[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)，用于自定义节点的创建、显示、更新等操作的管理，并负责将自定义节点挂载到[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md#nodecontainer-1)上。
3. 实现NodeController的makeNode()方法，makeNode()会在NodeController实例绑定NodeContainer的时候进行回调，并将返回的节点挂载至NodeContainer。
4. 使用NodeContainer显示自定义节点。

* 创建自定义节点

  首先，准备好需要挂载的节点，代码如下所示。

  ```ts
  import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

  class Params {
    text: string = 'Hello World';
    constructor(text: string) {
      this.text = text;
    }
  }

  @Builder
  function testBuilder(params: Params) {
    Column() {
      Text(params.text)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .margin({bottom: 36})
    }
  }
  // ...
  ```
* 实现NodeController

  NodeController为抽象类，需要继承并实现NodeController，代码如下所示。

  ```ts
  // ...
  class TextNodeController extends NodeController {
    private textNode: BuilderNode<[Params]> | null = null;
    private message: string = '';

    constructor(message: string) {
      super();
      this.message = message;
    }

    makeNode(context: UIContext): FrameNode | null {
      return null;
    }
  }
  ```
* 实现NodeController的makeNode()方法

  首先，使用构造函数创建BuilderNode实例。创建BuilderNode对象的时候必须要传入对应的UIContext对象。若BuilderNode作为RenderNode的子节点存在，要求设置RenderOptions的selfIdealSize属性。

  然后，使用BuilderNode的build()方法，构建组件树。方法build()需要传入两个参数，第一个参数为通过wrapBuilder()封装的全局@Builder方法。第二个参数为对应的@Builder方法所需的参数对象。若@Builder方法不带参数或者存在默认参数，则build()的第二个参数可以不设置。

  ```ts
  // ...
  class TextNodeController extends NodeController {
    private textNode: BuilderNode<[Params]> | null = null;
    private message: string = '';

    constructor(message: string) {
      super();
      this.message = message;
    }

    makeNode(context: UIContext): FrameNode | null {
      this.textNode = new BuilderNode(context);
      this.textNode.build(wrapBuilder<[Params]>(testBuilder), new Params(this.message));
      return this.textNode.getFrameNode();
    }
  }
  ```
* 显示自定义节点

  显示自定义节点依赖声明式渲染容器NodeContainer以及对应的控制类NodeController。

  NodeController的makeNode()方法返回的节点会显示在对应的NodeContainer中。由于makeNode()需要返回的为一个FrameNode，因此如果预期显示BuilderNode的时候需要调用对应的BuilderNode的getFrameNode()方法，获取其根节点，详细代码如上TextNodeController中所示。

  然后，在页面内新增声明式渲染容器NodeContainer，创建工具类NodeController。通过NodeController将MakeNode中返回的节点在声明式渲染容器中进行显示。

  ```ts
  // ...
  @Entry
  @Component
  struct Index {
    @State message: string = "hello";
    private textNodeController: TextNodeController = new TextNodeController(this.message);

    build() {
      Row() {
        Column() {
          NodeContainer(this.textNodeController)
            .width('100%')
            .height(100)
            .backgroundColor('#FFF0F0F0')
        }
        .width('100%')
        .height('100%')
      }
      .height('100%')
    }
  }
  ```
* 更新自定义节点

  更新自定义节点，可参考BuilderNode的[update()](../harmonyos-references/js-apis-arkui-buildernode.md#update)方法。

### 动态删除组件

通过条件控制语句可以将NodeContainer节点进行移除或者显示。如示例代码，将this.isShow更改为false则将节点从界面上移除。

```ts
// ...
@Entry
@Component
struct Index {
  @State message: string = "hello";
  @State isShow: boolean = true;
  private textNodeController: TextNodeController = new TextNodeController(this.message);

  build() {
    Row() {
      Column() {
        if (this.isShow) {
          NodeContainer(this.textNodeController)
            .width('100%')
            .height(100)
            .backgroundColor('#FFF0F0F0')
        }
        Button('isShow')
          .onClick(() => {
            this.isShow = false;
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

### 动态更新组件

动态将NodeContainer上的节点替换，依赖于NodeController的makeNode()和rebuild()方法。rebuild方法会触发makeNode的回调，刷新NodeContainer上显示的节点；makeNode()方法返回的为null，则移除NodeContainer下挂载的节点。

```ts
// ...

class TextNodeController extends NodeController {
  private textNode: BuilderNode<[Params]> | null = null;
  private message: string = '';

  constructor(message: string) {
    super();
    this.message = message;
  }

  makeNode(context: UIContext): FrameNode | null {
    if (this.textNode == null) {
      this.textNode = new BuilderNode(context);
      this.textNode.build(wrapBuilder<[Params]>(testBuilder), new Params(this.message));
    }

    return this.textNode.getFrameNode();
  }

  replaceBuilderNode(newNode: BuilderNode<Object[]>) {
    this.textNode = newNode;
    this.rebuild();
  }
}

// ...
```

开发者可以根据实际情况创建新的节点，参考示例代码如下所示：

```ts
// ...
@Entry
@Component
struct Index {
  @State message: string = "hello";
  @State isShow: boolean = true;
  private textNodeController: TextNodeController = new TextNodeController(this.message);
  // private count = 0;

  build() {
    Row() {
      Column() {
        if (this.isShow) {
          NodeContainer(this.textNodeController)
            .width('100%')
            .height(100)
            .backgroundColor('#FFF0F0F0')
        }
        Button('replaceNode')
          .onClick(() => {
            this.textNodeController.replaceBuilderNode(this.buildNewNode());
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }

  buildNewNode(): BuilderNode<[Params]> {
    let uiContext: UIContext = this.getUIContext();
    let message = 'newNode';
    let textNode = new BuilderNode<[Params]>(uiContext);
    textNode.build(wrapBuilder<[Params]>(testBuilder), new Params(message))
    return textNode;
  }
}
```

### NodeController生命周期

NodeController用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。下面，对其常用生命周期函数进行说明。

* makeNode()：必须要重写的方法，用于构建节点树、返回节点挂载在对应NodeContainer中。在对应NodeContainer创建绑定当前NodeController的时候调用、或者通过rebuild()方法调用刷新。
* aboutToResize()：当controller对应的NodeContainer在Measure的时候进行回调，入参为节点的布局大小。
* aboutToAppear()：当controller对应的NodeContainer在onAppear()的时候进行回调。
* aboutToDisappear()：当controller对应的NodeContainer在onDisappear()的时候进行回调。
* onTouchEvent()：当NodeController绑定的NodeContainer收到Touch事件时触发此回调。

```ts
 export abstract class NodeController {
   abstract makeNode(uiContext: UIContext): FrameNode | null;
   aboutToResize?(size: Size): void;
   aboutToAppear?(): void;
   aboutToDisappear?(): void;
   abstract rebuild(): void;
   onTouchEvent?(event: TouchEvent): void;
 }
```

## 列表流广告组件实践案例

### 场景描述

App广告有一种场景是列表流广告，即在应用的列表流中穿插展示广告条目，旨在将广告无缝融入用户的浏览体验中，使其看起来像是正常的内容（广告条目需要加标记区别展示），从而吸引用户的注意力并提高参与度，例如新闻列表中的广告条目、商品列表中的广告条目等。

这种广告的布局和内容在开发阶段不确定（可能是图文、视频等形式中的一种），其通常是在运行阶段，依赖服务器下发的数据进行逻辑映射后，再执行布局的构建、内容的加载显示。所以在实际的开发中，应用需要使用动态创建组件的能力去实现该列表流广告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/NEnMPLjtTzSMvi7-G26Xbw/zh-cn_image_0000002736432993.png)

### 实现方案

1. 使用列表数据构建List布局，根据数据类型分别执行对应逻辑，如果是广告类型，使用NodeContainer进行预占位。
2. 当NodeContainer渲染时，发起请求获取广告信息等数据。解析数据明确广告类型后，构建具体的广告布局，比如图文布局、视频布局等。
3. 布局构建完成后，返回rootNode实现组件上树，最后在容器中渲染显示。

### 开发步骤

1. 加载列表数据：模拟从服务器端获取列表数据，分别生成列表数据对象和广告数据对象。

   ```ts
   aboutToAppear() {
     for (let i = 0; i <= 100; i++) {
       let id = i.toString();
       if (i % 7 === 6) {
         this.data.pushData(new CardData(true, id));
         try {
           this.idList.add(id);
         } catch (error) {
           let err = error as BusinessError
           if (err.code) {
             hilog.error(0x0000, 'ImperativeView', 'Failed to add id. Cause: %{public}s', JSON.stringify(err) ?? '');
           }
         }
       } else {
         this.data.pushData(new CardData(false, id));
       }
     }
   }
   ```

   示例代码中用CardData(true, id)表示广告数据对象。

   ```ts
   export class CardData {
     private id: string = '';
     private mIsAdCard: boolean = false;

     constructor(isAdCard: boolean, id: string) {
       this.mIsAdCard = isAdCard;
       this.id = id;
     }
     // ...
   }
   ```
2. 构建广告组件：封装广告组件AdComponent，它通过模拟获取的广告类型去判断，进一步构建图文广告组件，或视频广告组件。

   ```ts
   @Builder
   export function adBuilder(param: AdParams) {
     AdComponent({ params: param });
   }

   @Component
   struct AdComponent {
     params ?: AdParams;
     closeAdDialogController: CustomDialogController = new CustomDialogController({
       builder: CloseAdDialog({
         adId: this.params!.id
       }),
       backgroundBlurStyle: BlurStyle.COMPONENT_THICK,
     });

     build() {
       if (this.params!.isVideo) {
         videoAdBuilder(this.closeAdDialogController);
       } else {
         picAdBuilder(this.closeAdDialogController);
       }
     }
   }
   ```
3. 广告占位节点逻辑：实现占位结点AdNodeController，它继承自NodeController，其中的initAd()方法通过this.adNode.build()接口将广告组件添加到rootNode上。当NodeContainer进行绘制时，会调用makeNode()方法，将构建好的rootNode返回实现组件上树。

   ```ts
   export class AdNodeController extends NodeController {
     private rootNode: FrameNode | null = null;
     private adNode: BuilderNode<[AdParams]> | null = null;
     private isRemove: boolean = false;
     private uiContext ?: UIContext;

     makeNode(): FrameNode | null {
       if (this.isRemove) {
         return null;
       }
       if (this.rootNode != null) {
         return this.rootNode;
       }
       return null;
     }

     initAd(uiContext: UIContext, id: string, adType: string) {
       this.uiContext = uiContext;
       this.rootNode = new FrameNode(this.uiContext);
       this.adNode = new BuilderNode(this.uiContext);
       this.adNode.build(wrapBuilder(adBuilder), { id: id, isVideo: adType === 'video' });
       this.rootNode.getRenderNode()?.appendChild(this.adNode.getFrameNode()?.getRenderNode());
     }

     remove() {
       this.isRemove = true;
     }
   }
   ```
4. 加载广告布局：getAdNodeController()方法是通过queryAdById()模拟广告类型信息的获取，并在完成信息获取后构建相应的NodeController。

   ```ts
   export const getAdNodeController = (uiContext: UIContext, id: string): AdNodeController | undefined => {
     let baseNode = new AdNodeController();
     nodeMap.set(id, baseNode);
     baseNode.initAd(uiContext, id, queryAdById(id));
     return nodeMap.get(id);
   }

   function queryAdById(id: string): string {
     if (Number(id) % 2 === 0) {
       return 'pic';
     } else {
       return 'video';
     }
   }
   ```
5. 列表及广告项布局：在ListItem布局逻辑中，需要判断该项是否为广告节点：若是广告项，通过getAdNodeController()方法预埋NodeContainer容器占位；若不是，通过CardComponent()进行列表内容项的布局及渲染。

   ```ts
   List({ space: 3 }) {
     LazyForEach(this.data, (item: CardData) => {
       ListItem() {
         if (item.isAdCard()) {
           NodeContainer(getAdNodeController(this.getUIContext(), item.getId())).width($r('app.string.percent_100'));
         } else {
           CardComponent({ cardData: item });
         }
       }
       .margin({
         left: $r('app.string.spacing_xxl'),
         right: $r('app.string.spacing_xxl')
       })
     }, (item: CardData) => item.getId())
   }
   .width($r('app.string.percent_100'))
   .height($r('app.string.percent_100'))
   .cachedCount(5)
   ```
6. 关闭/屏蔽广告功能：广告组件需要提供关闭功能，当点击确认屏蔽按钮后，通过node.remove()通知AdNodeController标记该广告移除，设置this.isRemove为true，再通过node.rebuild()接口触发组件重绘，此时系统会再次执行makeNode接口，根据this.isRemove标记返回null结点，实现广告组件下树。

   ```ts
   Button($r('app.string.text_dialog_shield'))
     .onClick(() => {
       let node: AdNodeController | undefined = nodeMap.get(this.adId);
       if (node !== undefined) {
         node.remove();
         node.rebuild();
       }
       this.dialogController.close();
     })
   ```

## 动态生成页面实践案例

### 场景描述

下面使用视频首页刷新图片资源作为场景，来介绍如何使用ArkUI的FrameNode来实现动态布局。

### ArkUI的声明式扩展使用

一个简化的动态布局类框架的DSL一般会使用JSON、XML等数据交换格式来描述UI，下面使用JSON为例进行说明。本案例相关核心字段含义如下表所示：

| 标签 | 含义 |
| --- | --- |
| type | 描述UI组件的类型，通常与原生组件存在一一对应的关系，也可能是封装的某种组件。 |
| content | 文本，图片类组件的内容。 |
| css | 描述UI组件的布局特性。 |
| children | 当前组件的子组件。 |

1. 定义视频应用首页UI描述数据，在resources/rawfile目录下创建structure.json文件，内容如下。

   ```ts
   {
     "type": "Column",
     "css": {
       "width": "100%"
     },
     "children": [
       // ...
     ]
   }
   ```
2. 定义相应数据结构用于接收UI描述数据，代码示例如下。

   ```ts
   class VM {
     type?: string;
     content?: string;
     css?: ESObject;
     children?: VM[];
     id?: string;
   }
   ```
3. 自定义DSL解析逻辑，且使用carouselNodes保存轮播图节点，方便后续操作节点更新，代码示例如下。

   ```ts
   let carouselNodes: typeNode.Image[] = [];

   function FrameNodeFactory(vm: VM, context: UIContext): FrameNode | null {
     if (vm.type === "Column") {
       let node = typeNode.createNode(context, "Column");
       setColumnNodeAttr(node, vm.css);
       vm.children?.forEach(kid => {
         let child = FrameNodeFactory(kid, context);
         node.appendChild(child);
       });
       return node;
     } else if (vm.type === "Row") {
       // ...
     } else if (vm.type === "Swiper") {
       // ...
     } else if (vm.type === "Image") {
       // ...
     } else if (vm.type === "Text") {
       // ...
     }
     return null;
   }

   function setColumnNodeAttr(node: typeNode.Column, css: ESObject) {
     node.attribute.width(css.width);
     node.attribute.height(css.height);
     node.attribute.backgroundColor(css.backgroundColor);
     node.attribute.justifyContent(FlexAlign.End);

       if (css.alignItems === "HorizontalAlign.Start") {
       node.attribute.alignItems(HorizontalAlign.Start);
     }
     if (css.padding !== undefined) {
       node.attribute.padding(css.padding as Padding);
     }
     if (css.margin !== undefined) {
       node.attribute.margin(css.margin as Padding);
     }
   }

   function setRowNodeAttr(node: typeNode.Row, css: ESObject) {
     node.attribute.width(css.width);
     node.attribute.height(css.height);
     if (css.padding !== undefined) {
       node.attribute.padding(css.padding as Padding);
     }
     if (css.margin !== undefined) {
       node.attribute.margin(css.margin as Padding);
     }
     node.attribute.justifyContent(FlexAlign.SpaceBetween);
   }
   ```
4. 使用NodeContainer组件嵌套ArkUI的FrameNode扩展和ArkUI的声明式语法。

   ```ts
   class ImperativeController extends NodeController {
     // ...
     makeNode(uiContext: UIContext): FrameNode | null {
       return frameNodeFactory(data, uiContext);
     }
   }

   @Component
   export struct ImperativePage {
     private controller: ImperativeController = new ImperativeController();

     build() {
       Column() {
         NodeContainer(this.controller)
       }
       .height('100%')
       .width('100%')
       .backgroundColor(Color.Black)
     }
   }
   ```

### 性能对比

以场景示例中的两种方案实现，通过DevEco Studio的Profile工具抓取Trace进行性能分析比对。

1. 以上示例场景在声明式开发范式下的完成时延为13.7ms（根据设备和场景不同，数据会有差异，本数据仅供参考），如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/PHpsaYjPSAmaVbCV3bd8mA/zh-cn_image_0000002706833838.png)
2. 以上示例场景在FrameNode扩展模式下的完成时延为6.1ms（根据设备和场景不同，数据会有差异，本数据仅供参考），如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/dYmlRajpS_SIzExyrXa3PQ/zh-cn_image_0000002736312947.png)

## 示例代码

* [实现组件的动态创建功能](https://gitcode.com/harmonyos_samples/DynamicComponent)
