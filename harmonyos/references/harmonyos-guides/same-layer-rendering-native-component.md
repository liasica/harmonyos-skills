---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/same-layer-rendering-native-component
title: 同层渲染原生组件
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 同层渲染 > 同层渲染原生组件
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:10+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:a1c35c1849e9cce91858dca12c13ab60a156e7f3acdfcc6edcb06eb87ad08f4e
---

## 概述

在使用[Web](../harmonyos-references/ts-basic-components-web.md)组件加载H5页面时，经常会有输入框、视频的场景，这些场景在H5中的组件性能体验欠佳。想要更加流畅的体验，必须要将原生组件放到Web组件上。在以下场景应在Web组件上使用原生组件：

* 需要高性能，流畅体验。
* 需要使用原生组件功能。
* 原生组件已经实现，复用以减少开发成本。

目前要实现在Web组件上使用原生组件（详情查看[组件介绍](ui-js-building-ui-component.md)）有两种方案：

方案一：直接使用[Stack](../harmonyos-references/ts-container-stack.md)将组件堆叠到H5页面上。

方案二：使用同层渲染，使用Web组件和原生组件交互的方式，将原生组件替代Web组件中部分组件，提升交互体验和性能。

以上两种方案经过性能对比后，同层渲染比非同层渲染的性能要更好。

## 什么是同层渲染

[同层渲染](web-same-layer.md)是一种混合渲染技术，通过将原生组件嵌入到Web组件的DOM树中同一层级，实现原生组件与Web组件的无缝集成。

同层渲染和非同层渲染的区别如下：

* 非同层渲染：通过Z轴的层级关系堆叠在Web组件页面上。此方式实现方式简单，用于原生组件大小位置固定场景。
* 同层渲染：通过同层渲染的方式直接渲染到H5页面Embed标签区域上。此方式实现相对复杂，用于原生组件大小位置需要跟随Web组件页面变化场景。

**图1** 同层渲染和非同层渲染区别

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/1KWGP9qFTd-NKPt49WbVHw/zh-cn_image_0000002712244332.png)

## 场景示例

以下分别采用非同层渲染和同层渲染的两种方式，加载相同的商城组件到相同的H5页面上，并抓取Trace对比两者之间的区别，页面效果与场景实例源码的核心部分如下：

**图2** 页面效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/7aEci2xbRA6rxBNwoSEApw/zh-cn_image_0000002742003285.png)

提供承载的H5页面代码如下：

```html
<div>
    <div id="bodyId">
        <!-- On the H5 interface, the same layer elements are identified by the embedded tag, and the native components are rendered to the location of the embedded tag on the H5 page on the application side.-->
        <embed id="nativeSearch" type = "native/component" width="100%" height="100%" src="view"/>
    </div>
</div>
```

商品数据代码如下：

```ts
export const PRODUCT_DATA: Array<ProductDataModel> = [
  new ProductDataModel(0, $r('app.media.nativeembed_product000'), $r('app.string.nativeembed_product_title000'),
    $r("app.string.nativeembed_product_price000")),
  new ProductDataModel(1, $r('app.media.nativeembed_product001'), $r('app.string.nativeembed_product_title001'),
    $r('app.string.nativeembed_product_price001')),
  new ProductDataModel(2, $r('app.media.nativeembed_product002'), $r('app.string.nativeembed_product_title002'),
    $r('app.string.nativeembed_product_price002')),
  new ProductDataModel(4, $r('app.media.nativeembed_product003'), $r('app.string.nativeembed_product_title004'),
    $r('app.string.nativeembed_product_price004')),
  new ProductDataModel(0, $r('app.media.nativeembed_product000'), $r('app.string.nativeembed_product_title000'),
    $r("app.string.nativeembed_product_price000")),
  new ProductDataModel(1, $r('app.media.nativeembed_product001'), $r('app.string.nativeembed_product_title001'),
    $r('app.string.nativeembed_product_price001')),
  new ProductDataModel(2, $r('app.media.nativeembed_product002'), $r('app.string.nativeembed_product_title002'),
    $r('app.string.nativeembed_product_price002')),
  new ProductDataModel(4, $r('app.media.nativeembed_product003'), $r('app.string.nativeembed_product_title004'),
    $r('app.string.nativeembed_product_price004')),
  new ProductDataModel(0, $r('app.media.nativeembed_product000'), $r('app.string.nativeembed_product_title000'),
    $r("app.string.nativeembed_product_price000")),
  new ProductDataModel(1, $r('app.media.nativeembed_product001'), $r('app.string.nativeembed_product_title001'),
    $r('app.string.nativeembed_product_price001')),
  new ProductDataModel(2, $r('app.media.nativeembed_product002'), $r('app.string.nativeembed_product_title002'),
    $r('app.string.nativeembed_product_price002')),
  new ProductDataModel(4, $r('app.media.nativeembed_product003'), $r('app.string.nativeembed_product_title004'),
    $r('app.string.nativeembed_product_price004')),
  new ProductDataModel(0, $r('app.media.nativeembed_product000'), $r('app.string.nativeembed_product_title000'),
    $r("app.string.nativeembed_product_price000")),
  new ProductDataModel(1, $r('app.media.nativeembed_product001'), $r('app.string.nativeembed_product_title001'),
    $r('app.string.nativeembed_product_price001')),
  new ProductDataModel(2, $r('app.media.nativeembed_product002'), $r('app.string.nativeembed_product_title002'),
    $r('app.string.nativeembed_product_price002')),
  new ProductDataModel(4, $r('app.media.nativeembed_product003'), $r('app.string.nativeembed_product_title004'),
    $r('app.string.nativeembed_product_price004')),
];
```

商城组件代码如下：

```ts
@Component
struct SearchComponent {
  @Prop searchWidth: number;
  @Prop searchHeight: number;

  build() {
    Column({ space: 8 }) {
      Text($r('app.string.nativeembed_mall'))
        .fontSize(16)
      Row() {
        Image($r('app.media.nativeembed_search_icon'))
          .width(14)
          .margin({ left: 14 })
        Text($r('app.string.nativeembed_search_text_placeholder'))
          .fontSize(14)
          .opacity(0.6)
          .fontColor('#000000')
          .margin({ left: 14})
      }
      .width('100%')
      .margin(4)
      .height(36)
      .backgroundColor(Color.White)
      .borderRadius(18)
      .onClick(() => {
        this.getUIContext().getPromptAction().showToast({
          message: $r('app.string.nativeembed_prompt_text')
        });
      })
      Grid() {
        ForEach(PRODUCT_DATA, (item: ProductDataModel, index: number) => {
          GridItem() {
            Column({ space: 8 }) {
              Image(item.uri)
                .width(100)
                .height(100)
              Row({ space: 8 }) {
                Text(item.title)
                  .fontSize(12)
                Text(item.price)
                  .fontSize(12)
              }
            }
            .backgroundColor(Color.White)
            .alignItems(HorizontalAlign.Center)
            .justifyContent(FlexAlign.Center)
            .width('100%')
            .borderRadius(12)
            .padding({ bottom: 12 })
          }
        }, (item: ProductDataModel) => `${item.id}`)
      }
      .columnsTemplate('1fr 1fr')
      .rowsGap(8)
      .columnsGap(8)
      .width('100%')
      .height('90%')
      .backgroundColor('#F1F3F5')
    }
    .padding(10)
    .width(this.searchWidth)
    .height(this.searchHeight)
  }
}
```

## Web组件首次加载原生组件方案对比

首先的想法是，将原生组件内容使用H5实现，直接用Web组件加载页面。但是，用H5开发页面时，需要使用到JS和CSS，甚至一些前端框架进行页面的开发，并且动效和体验都不如原生组件。因此采用同层渲染和非同层渲染两种方案进行对比。

### 使用非同层渲染

底层使用空白的H5页面，用任意标签进行占位，然后在H5页面上方层叠一个原生组件。原生组件需要在Web组件加载完成后，获取到标签大小位置后，在对应位置展示。

需要在H5侧添加getEmbedSize()方法来获取元素大小，代码如下：

```js
function getEmbedSize() {
    let doc = document.getElementById('nativeSearch');
    return {
      width: doc.offsetWidth,
      height: doc.offsetHeight,
    }
}
```

使用Stack层叠Web组件和SearchComponent组件，代码如下：

```ts
import { PRODUCT_DATA } from '../mock/GoodsMock';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct NonSameLayerRendering {
  @State searchWidth: number = 0;
  @State searchHeight: number = 0;
  @State isWebInit: boolean = false;
  browserTabController: WebviewController = new webview.WebviewController(); // WebviewController controller

  build() {
    Stack() {
      Web({ src: $rawfile('nativeembed_view.html'), controller: this.browserTabController })
        .backgroundColor('#F1F3F5')
        .onPageEnd(() => {
          this.browserTabController.runJavaScript(
            'getEmbedSize()',
            (error, result) => {
              if (result) {
                interface EmbedSize {
                  width: number,
                  height: number
                }
                let embedSize = JSON.parse(result) as EmbedSize;
                this.searchWidth = embedSize.width;
                this.searchHeight = embedSize.height;
                this.isWebInit = true;
              }
            });
        })
      if (this.isWebInit){
        Column() {
          // Because it needs to be displayed according to the actual size of the Web, it needs to wait for the width and height to be obtained after the Web is initialized, and then it needs to be layered on the Web
          SearchComponent({ searchWidth: this.searchWidth, searchHeight: this.searchHeight })
        }
        .zIndex(10)
      }
    }
  }
}

/**
 * Set the data class of the item
 */
class ProductDataModel {
  id: number;
  uri: ResourceStr;
  title: ResourceStr;
  price: ResourceStr;

  constructor(id: number, uri: ResourceStr, title: ResourceStr, price: ResourceStr) {
    this.id = id;
    this.uri = uri;
    this.title = title;
    this.price = price;
  }
}

@Component
struct SearchComponent {
  @Prop searchWidth: number;
  @Prop searchHeight: number;

  build() {
    Column({ space: 8 }) {
      Text($r('app.string.nativeembed_mall'))
        .fontSize(16)
      Row() {
        Image($r('app.media.nativeembed_search_icon'))
          .width(14)
          .margin({ left: 14 })
        Text($r('app.string.nativeembed_search_text_placeholder'))
          .fontSize(14)
          .opacity(0.6)
          .fontColor('#000000')
          .margin({ left: 14})
      }
      .width('100%')
      .margin(4)
      .height(36)
      .backgroundColor(Color.White)
      .borderRadius(18)
      .onClick(() => {
        this.getUIContext().getPromptAction().showToast({
          message: $r('app.string.nativeembed_prompt_text')
        });
      })
      Grid() {
        ForEach(PRODUCT_DATA, (item: ProductDataModel, index: number) => {
          GridItem() {
            Column({ space: 8 }) {
              Image(item.uri)
                .width(100)
                .height(100)
              Row({ space: 8 }) {
                Text(item.title)
                  .fontSize(12)
                Text(item.price)
                  .fontSize(12)
              }
            }
            .backgroundColor(Color.White)
            .alignItems(HorizontalAlign.Center)
            .justifyContent(FlexAlign.Center)
            .width('100%')
            .borderRadius(12)
            .padding({ bottom: 12 })
          }
        }, (item: ProductDataModel) => `${item.id}`)
      }
      .columnsTemplate('1fr 1fr')
      .rowsGap(8)
      .columnsGap(8)
      .width('100%')
      .height('90%')
      .backgroundColor('#F1F3F5')
    }
    .padding(10)
    .width(this.searchWidth)
    .height(this.searchHeight)
  }
}
```

上述的方案只是限于底层H5网页比较简单，如果H5页面比较复杂，就会发现原生组件是很难去定位，而且在性能上，Web组件是整体渲染的，即使被原生组件遮住的部分也需要渲染消耗性能。

### 使用同层渲染

同层渲染简单来说就是，底层使用空白的H5页面，用Embed标签进行占位，ArkTS使用NodeContainer来占位，最后将Web侧的surfaceId和原生组件绑定，渲染在NodeContainer上。这里给出一些大致步骤：

1. 用Stack组件层叠NodeContainer和Web组件，并开启enableNativeEmbedMode模式。
2. 因为要使用NodeContainer，所以封装一个继承自NodeController的类SearchNodeController。
3. 使用Web组件加载nativeembed\_view.html文件，Web组件解析到Embed标签后，通过onNativeEmbedLifecycleChange()接口上报Embed标签创建消息通知到应用侧。
4. 在步骤3的回调内，根据embed.status，将配置传入searchNodeController后，执行rebuild()方法重新触发其makeNode()方法。
5. makeNode()方法触发后，NodeContainer组件获取到BuilderNode对象，页面出现原生组件。

```ts
    import { PRODUCT_DATA } from '../viewmodel/GoodsViewModel';
    import { ProductDataModel } from '../model/GoodsModel';
    import { BuilderNode, FrameNode, NodeController, NodeRenderType } from '@kit.ArkUI';
    import { webview } from '@kit.ArkWeb';
    
    // Margin vertical
    const MARGIN_VERTICAL: number = 8;
    // Font weight
    const FONT_WEIGHT: number = 500;
    // Placeholder
    const PLACEHOLDER: ResourceStr = $r('app.string.embed_search');
    
    declare class Params {
      width: number;
      height: number;
    }
    
    declare class NodeControllerParams {
      surfaceId: string;
      type: string;
      renderType: NodeRenderType;
      embedId: string;
      width: number;
      height: number;
    }
    
    class SearchNodeController extends NodeController {
      private rootNode: BuilderNode<[Params]> | undefined | null = null;
      private embedId: string = "";
      private surfaceId: string = "";
      private renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
      private componentWidth: number = 0;
      private componentHeight: number = 0;
      private componentType: string = "";
    
      /**
       * 设置渲染参数
       *
       * @param params 渲染参数
       */
      setRenderOption(params: NodeControllerParams): void {
        this.surfaceId = params.surfaceId;
        this.renderType = params.renderType;
        this.embedId = params.embedId;
        this.componentWidth = params.width;
        this.componentHeight = params.height;
        this.componentType = params.type;
      }
    
      /**
       * 创建节点
       *
       * @param uiContext UIContext
       * @returns 节点
       */
      makeNode(uiContext: UIContext): FrameNode | null {
        this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId, type: this.renderType });
        if (this.componentType === 'native/component') {
          this.rootNode.build(wrapBuilder(searchBuilder), { width: this.componentWidth, height: this.componentHeight });
        }
        return this.rootNode.getFrameNode();
      }
    
      setBuilderNode(rootNode: BuilderNode<Params[]> | null): void {
        this.rootNode = rootNode;
      }
    
      getBuilderNode(): BuilderNode<[Params]> | undefined | null {
        return this.rootNode;
      }
    
      updateNode(arg: Object): void {
        this.rootNode?.update(arg);
      }
    
      getEmbedId(): string {
        return this.embedId;
      }
    
      postEvent(event: TouchEvent | undefined): boolean {
        return this.rootNode?.postTouchEvent(event) as boolean;
      }
    }
    @Component
    struct SearchComponent {
      @Prop params: Params;
      controller: SearchController = new SearchController()
    
      build() {
        Column({ space: MARGIN_VERTICAL }) {
          Text($r("app.string.embed_mall"))
            .fontSize($r('app.string.ohos_id_text_size_body4'))
            .fontWeight(FONT_WEIGHT)
            .fontFamily('HarmonyHeiTi-Medium')
          Row() {
            Search({ placeholder: PLACEHOLDER, controller: this.controller })
              .backgroundColor(Color.White)
          }
          .width($r("app.string.embed_full_percent"))
          .margin($r("app.integer.embed_row_margin"))
    
          Grid() {
            ForEach(PRODUCT_DATA, (item: ProductDataModel, index: number) => {
              GridItem() {
                Column({ space: MARGIN_VERTICAL }) {
                  Image(item.imageRes).width($r("app.integer.embed_image_size"))
                  Row({ space: MARGIN_VERTICAL }) {
                    Text(item.title)
                      .fontSize($r('app.string.ohos_id_text_size_body1'))
                      .width(100)
                      .maxLines(1)
                      .textOverflow({ overflow: TextOverflow.Ellipsis })
                    Text(item.price)
                      .fontSize($r('app.string.ohos_id_text_size_body1'))
                      .width(50)
                      .maxLines(1)
                  }
                }
                .backgroundColor($r('app.color.ohos_id_color_background'))
                .alignItems(HorizontalAlign.Center)
                .justifyContent(FlexAlign.Center)
                .width($r("app.string.embed_full_percent"))
                .height($r("app.string.embed_full_percent"))
                .borderRadius($r('app.string.ohos_id_corner_radius_default_m'))
              }
            }, (item: ProductDataModel, index: number) => index.toString())
          }
          .columnsTemplate('1fr 1fr')
          .rowsTemplate('1fr 1fr 1fr')
          .rowsGap($r('app.string.ohos_id_elements_margin_vertical_m'))
          .columnsGap($r('app.string.ohos_id_elements_margin_vertical_m'))
          .width($r("app.string.embed_full_percent"))
          .height($r("app.string.embed_sixty_percent"))
          .backgroundColor($r('app.color.ohos_id_color_sub_background'))
        }
        .padding($r('app.string.ohos_id_card_margin_start'))
        .width(this.params.width)
        .height(this.params.height)
      }
    }
    @Builder
    function searchBuilder(params: Params) {
      SearchComponent({ params: params })
        .backgroundColor($r('app.color.ohos_id_color_sub_background'))
    }
    
    @Entry
    @Component
    struct Index {
      browserTabController: WebviewController = new webview.WebviewController();
      @State componentIdArr: Array<string> = [];
      private nodeControllerMap: Map<string, SearchNodeController> = new Map();
    
      build() {
        Stack() {
          ForEach(this.componentIdArr, (componentId: string) => {
            NodeContainer(this.nodeControllerMap.get(componentId));
          }, (embedId: string) => embedId)
          Web({ src: $rawfile("embed_view.html"), controller: this.browserTabController })
            .backgroundColor($r('app.color.ohos_id_color_sub_background'))
            .zoomAccess(false)
            .enableNativeEmbedMode(true)
            .onNativeEmbedLifecycleChange((embed) => {
              const componentId = embed.info?.id?.toString() as string
              if (embed.status === NativeEmbedStatus.CREATE) {
                let nodeController = new SearchNodeController();
                nodeController.setRenderOption({
                  surfaceId: embed.surfaceId as string,
                  type: embed.info?.type as string,
                  renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                  embedId: embed.embedId as string,
                  width: this.getUIContext().px2vp(embed.info?.width),
                  height: this.getUIContext().px2vp(embed.info?.height)
                });
                nodeController.rebuild();
                this.nodeControllerMap.set(componentId, nodeController);
                this.componentIdArr.push(componentId);
              } else if (embed.status === NativeEmbedStatus.UPDATE) {
                let nodeController = this.nodeControllerMap.get(componentId);
                nodeController?.updateNode({
                  text: 'update',
                  width: this.getUIContext().px2vp(embed.info?.width),
                  height: this.getUIContext().px2vp(embed.info?.height)
                } as ESObject);
                nodeController?.rebuild();
              } else {
                let nodeController = this.nodeControllerMap.get(componentId);
                nodeController?.setBuilderNode(null);
                nodeController?.rebuild();
              }
            })
            .onNativeEmbedGestureEvent((touch) => {
              this.componentIdArr.forEach((componentId: string) => {
                let nodeController = this.nodeControllerMap.get(componentId);
                if (nodeController?.getEmbedId() === touch.embedId) {
                  nodeController?.postEvent(touch.touchEvent);
                }
              })
            })
        }
      }
    }
```

## Web组件加载原生组件性能收益对比

本节以Web组件加载原生组件的场景，抓取Trace图进行分析。下面的Trace图上的红线处Web组件加载完成，蓝线处原生组件加载显示完成。

### 使用非同层渲染加载

\*\*图3 \*\*非同层渲染的Trace图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/dEz2wjekTWe8YPdof-CW8g/zh-cn_image_0000002712404298.png)

非同层渲染的分析：

* 在应用侧，红蓝线之间为测量和计算布局，图片加载被延后到了蓝线之外。
* 在render\_service侧，蓝线之后每一帧ReceiveVsync的耗时大幅增加。

### 使用同层渲染加载

**图4** 同层渲染的Trace图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/yfY1iArMSYOoa3FzJze77w/zh-cn_image_0000002742123247.png)

同层渲染的分析：

* 在应用侧，红蓝线之间由于NodeContainer的原因，组件布局的测量和绘制划分成了两部分，同时将图片加载提前到了红蓝线之间。
* 在render\_service侧，每一帧ReceiveVsync的耗时无明显变化。

### 页面加载场景总结

下表为各种方法完成原生组件加载（蓝线）前后几帧render\_service侧的耗时对比（-1为完成前一帧，1为完成后一帧，以此类推）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/0jLSx5OASpGXtNoQBDqRCA/zh-cn_image_0000002712244334.png)

从此表格可以看出，非同层渲染会导致render\_service侧每帧耗时大幅提升，同层渲染相比起非同层渲染，并不影响render\_service侧的每帧耗时。

## 列表滑动场景性能收益对比

本节以列表滑动场景，抓取Trace图进行分析。在此场景下，对比同层渲染和非同层渲染的每一帧的结构如下所示：

### 使用非同层渲染

**图5** 非同层渲染滑动时单帧图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/9WH1m3d-TjWdMImboBF6_Q/zh-cn_image_0000002742003287.png)

非同层渲染的分析：

* ReceiveVsync表示渲染服务接收到垂直同步信号（Vsync）的事件，此标记的出现意味着渲染服务开始响应新一帧的绘制任务。所以上图表示单帧的渲染绘制情况。
* 单帧ReceiveVsync渲染耗时5ms。

### 使用同层渲染

**图6** 同层渲染滑动时单帧图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/LdQl2dQZSzSWlnChJxvBjQ/zh-cn_image_0000002712404300.png)

同层渲染的分析：

* 同场景下，单帧ReceiveVsync渲染耗时1ms。

### 列表滑动场景总结

非同层渲染的render\_service每一帧的耗时大幅增加，结论与“[页面加载场景总结](same-layer-rendering-native-component.md#页面加载场景总结)”一致，再次验证了同样的结果。

## 总结

在Web组件中渲染原生组件时，采用同层渲染方式比起非同层渲染可以将图片渲染提前到原生组件加载完成前，且同层渲染将位于同一个图层的元素一起渲染，降低绘制任务，提升了性能。同时使用同层渲染可以实现更多功能，比如根据尺寸调整组件大小等功能，从而避免繁琐操作。

## 示例代码

* [基于ArkWeb实现系统原生组件渲染至H5页面上](https://gitcode.com/HarmonyOS_Samples/arkweb-same-level-rendering)
