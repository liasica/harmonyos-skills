---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-159
title: 使用Web组件的同层渲染，同层组件无法触发Web组件的滚动
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 使用Web组件的同层渲染，同层组件无法触发Web组件的滚动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d72b62e596081ee6ac9bd15068a22975d3f2e671f6781d17ffd6e6755306c01d
---

## 问题现象

使用Web组件的同层渲染，触摸同层组件上下移动时无法触发Web组件的滚动，而其他位置可以正常滚动。

问题代码示例参考如下：

```ts
Web({ src: $rawfile("embed_view.html"), controller: this.browserTabController })
  // ...
  .onNativeEmbedGestureEvent((touch) => {
    console.info(`NativeEmbed onNativeEmbedGestureEvent ${JSON.stringify(touch.touchEvent)}`);
    this.componentIdArr.forEach((componentId: string) => {
      let nodeController = this.nodeControllerMap.get(componentId);
      if (nodeController?.getEmbedId() == touch.embedId) {
        let ret = nodeController?.postEvent(touch.touchEvent);
        if (ret) {
          console.info(`onNativeEmbedGestureEvent success ${componentId}`);
        } else {
          console.error(`onNativeEmbedGestureEvent failed ${componentId}`);
        }
        if (touch.result) {
          // 通知Web组件手势事件消费结果。
          touch.result.setGestureEventResult(ret);
        }
      }
    });
  });
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Q53qJd9gTJ2ZEXsIsfx0OA/zh-cn_image_0000002628899164.png "点击放大")

## 背景知识

[Web组件](../harmonyos-references/ts-basic-components-web.md)的[同层渲染](../harmonyos-guides/web-same-layer.md)可以在非ArkTS框架的UI组件功能或性能不如ArkTS组件时使用。当手指触摸到Web的同层标签时，可以触发Web组件的[onNativeEmbedGestureEvent](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedgestureevent11)事件，事件参数NativeEmbedTouchInfo的[EventResult](../harmonyos-references/arkts-basic-components-web-eventresult.md)用于通知Web组件手势事件的消费结果，该消费结果可以通过[setGestureEventResult](../harmonyos-references/arkts-basic-components-web-eventresult.md#setgestureeventresult12)进行设置。

## 问题定位

1. 查看日志，触摸同层组件GridItem时，onNativeEmbedGestureEvent回调的日志正常打印。
2. 长按并拖动GridItem，相关日志被打印，手势组合可识别。
3. 排查代码，ret为true并传入setGestureEventResult，设置同层组件消费手势，Web不消费手势。

## 分析结论

onNativeEmbedGestureEvent回调中设置了同层组件消费手势，Web无法消费滑动手势，导致无法触发Web的滚动。

## 修改建议

1. 可以通过修改setGestureEventResult的参数为false，让手势事件被Web组件消费。

   ```ts
   // 触摸同层组件触发Web组件滚动
   touch.result.setGestureEventResult(false);
   ```
2. 当同层组件本身有手势事件需要响应，可以根据手势动作动态修改setGestureEventResult的参数。

   ```ts
   if (AppStorage.get('longPressPan')) {
     // 当同层组件本身有手势事件(如长按手势)需要响应，可以根据手势动作动态修改参数
     // 此时触摸同层组件不触发Web组件滚动
     touch.result.setGestureEventResult(ret, false);
   } else {
     // 触摸同层组件触发Web组件滚动
     touch.result.setGestureEventResult(false);
   }
   ```

完整示例参考如下：

```ts
import { webview } from '@kit.ArkWeb';
import { UIContext } from '@kit.ArkUI';
import { NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';
import { JSON } from '@kit.ArkTS';

@Observed
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

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | undefined | null;
  private embedId_: string = '';
  private surfaceId_: string = '';
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: number = 0;
  private height_: number = 0;
  private isDestroy_: boolean = false;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.embedId_ = params.embedId;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.isDestroy_) {
      return null;
    }
    if (!this.rootNode) {
      this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
      if (this.rootNode) {
        this.rootNode.build(wrapBuilder(TextBuilder), { width: this.width_, height: this.height_ });
        return this.rootNode.getFrameNode();
      } else {
        return null;
      }
    }
    return this.rootNode.getFrameNode();
  }

  updateNode(arg: Object): void {
    this.rootNode?.update(arg);
  }

  getEmbedId(): string {
    return this.embedId_;
  }

  setDestroy(isDestroy: boolean): void {
    this.isDestroy_ = isDestroy;
    if (this.isDestroy_) {
      this.rootNode = null;
    }
  }

  postEvent(event: TouchEvent | undefined): boolean {
    return this.rootNode?.postTouchEvent(event) as boolean;
  }
}

@Component
struct TextComponent {
  itemArr: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
  @Prop params: Params;

  build() {
    Column() {
      Grid() {
        ForEach(this.itemArr, (num: number) => {
          GridItem() {
            Text('Item' + num)
              .fontSize('18fp');
          }
          .height(100)
          .borderWidth(1)
          .borderColor(Color.Gray)
          .gesture(
            GestureGroup(GestureMode.Sequence,
              LongPressGesture({ repeat: true })
                .tag('longPress')
                .onAction(() => {
                  // 长按动作
                  console.info('Long Press.');
                }),
              PanGesture({ fingers: 1, direction: null, distance: 0 })
                .tag('pan')
                .onActionStart(() => {
                  // 开始拖动
                  AppStorage.setOrCreate('longPressPan', true);
                  console.info('Pan Start.');
                })
                .onActionEnd(() => {
                  // 结束拖动
                  AppStorage.setOrCreate('longPressPan', false);
                  console.info('Pan End.');
                })
            )
          );
        });
      }
      .height('100%')
      .width('100%')
      .padding({ top: 10, bottom: 10 })
      .columnsTemplate('1fr 1fr')
      .columnsGap(5)
      .rowsGap(5);
    }
    .width(this.params.width)
    .height(this.params.height);
  }
}

@Builder
function TextBuilder(params: Params) {
  TextComponent({ params: params })
    .width(params.width)
    .height(params.height)
    .backgroundColor(Color.White);
}

@Entry
@Component
struct Index {
  browserTabController: WebviewController = new webview.WebviewController();
  private nodeControllerMap: Map<string, MyNodeController> = new Map();
  @State componentIdArr: Array<string> = [];
  @State widthMap: Map<string, number> = new Map();
  @State heightMap: Map<string, number> = new Map();
  @State positionMap: Map<string, Edges> = new Map();
  @State edges: Edges = {};
  uiContext: UIContext = this.getUIContext();

  build() {
    Row() {
      Column() {
        Stack() {
          ForEach(this.componentIdArr, (componentId: string) => {
            NodeContainer(this.nodeControllerMap.get(componentId))
              .position(this.positionMap.get(componentId))
              .width(this.widthMap.get(componentId))
              .height(this.heightMap.get(componentId));
          }, (embedId: string) => embedId);
          // Web组件加载本地html页面。
          Web({ src: $rawfile('embed_view.html'), controller: this.browserTabController })
            .fileAccess(false)
            .geolocationAccess(false)
            .enableNativeEmbedMode(true)
            .onNativeEmbedLifecycleChange((embed) => {
              console.info(`NativeEmbed surfaceId ${embed.surfaceId}`);
              const componentId = embed.info?.id?.toString() as string;
              if (embed.status == NativeEmbedStatus.CREATE) {
                console.info(`NativeEmbed create ${JSON.stringify(embed.info)}`);
                let nodeController = new MyNodeController();
                nodeController.setRenderOption({
                  surfaceId: embed.surfaceId as string,
                  type: embed.info?.type as string,
                  renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                  embedId: embed.embedId as string,
                  width: this.uiContext.px2vp(embed.info?.width),
                  height: this.uiContext.px2vp(embed.info?.height)
                });
                this.edges =
                  { left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px` };
                nodeController.setDestroy(false);
                this.nodeControllerMap.set(componentId, nodeController);
                this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                this.positionMap.set(componentId, this.edges);
                this.componentIdArr.push(componentId);
              } else if (embed.status == NativeEmbedStatus.UPDATE) {
                let nodeController = this.nodeControllerMap.get(componentId);
                console.info(`NativeEmbed update ${JSON.stringify(embed)}`);
                this.edges =
                  { left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px` };
                this.positionMap.set(componentId, this.edges);
                this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                nodeController?.updateNode({
                  textOne: 'update',
                  width: this.uiContext.px2vp(embed.info?.width),
                  height: this.uiContext.px2vp(embed.info?.height)
                } as ESObject);
              } else if (embed.status == NativeEmbedStatus.DESTROY) {
                console.info(`NativeEmbed destroy ${JSON.stringify(embed)}`);
                let nodeController = this.nodeControllerMap.get(componentId);
                nodeController?.setDestroy(true);
                this.nodeControllerMap.delete(componentId);
                this.positionMap.delete(componentId);
                this.widthMap.delete(componentId);
                this.heightMap.delete(componentId);
                this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
              } else {
                console.info(`NativeEmbed status ${embed.status}`);
              }
            })
            // 获取同层渲染组件触摸事件信息。
            .onNativeEmbedGestureEvent((touch) => {
              console.info(`NativeEmbed onNativeEmbedGestureEvent ${JSON.stringify(touch.touchEvent)}`);
              this.componentIdArr.forEach((componentId: string) => {
                let nodeController = this.nodeControllerMap.get(componentId);
                if (nodeController?.getEmbedId() == touch.embedId) {
                  let ret = nodeController?.postEvent(touch.touchEvent);
                  if (ret) {
                    console.info(`onNativeEmbedGestureEvent success ${componentId}`);
                  } else {
                    console.error(`onNativeEmbedGestureEvent failed ${componentId}`);
                  }
                  if (touch.result) {
                    if (AppStorage.get('longPressPan')) {
                      // 当同层组件本身有手势事件(如长按手势)需要响应，可以根据手势动作动态修改参数
                      // 此时触摸同层组件不触发Web组件滚动
                      touch.result.setGestureEventResult(ret, false);
                    } else {
                      // 触摸同层组件触发Web组件滚动
                      touch.result.setGestureEventResult(false);
                    }
                  }
                }
              });
            })
            .expandSafeArea([SafeAreaType.SYSTEM]);
        };
      }
      .width('100%')
      .alignItems(HorizontalAlign.Center);
    };
  }
}
```

```html
<!--embed_view.html-->
<!Document>
<html>
<head>
    <title>同层渲染测试html</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
</head>
<body>
<div>
    <div id="bodyId">
        <div class="top"></div>
        <div align="center">
            <embed id="embed1" type = "native/component" width="92%" height="54%" src="view"/>
        </div>
        <div class="bottom"></div>
    </div>
</div>
<script>
    let nativeEmbed = {
      // 判断设备是否支持touch事件
      touch:('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch,
      nativeEmbed : document.getElementById('embed1'),

      // 事件
      events:{
        nativeEmbed:document.getElementById('embed1'),
        handleEvent:function(event){ },
      },

      // 初始化
      init:function(){
        let self = this;
        self.nativeEmbed.addEventListener('touchstart', self.events, false); // addEventListener第二个参数可以传一个对象，会调用该对象的handleEvent属性
      }
    };

    nativeEmbed.init();
</script>

</body>
</html>
<style>
    .top{
        width:100%;
        height:500px;
        background-color:#f1f3f5
    }
    .bottom{
        width:100%;
        height:1000px;
        background-color:#f1f3f5
    }
</style>
```

## 常见FAQ

Q：同层渲染时对html文件中div进行transform: rotate(30deg)旋转之后，为什么Web页面中的Slider组件无法滑动了？

A：参考文档[Web网页的同层渲染标签](../harmonyos-guides/web-same-layer.md#web网页的同层渲染标签)可以看到，同层标签支持的css属性暂不支持transform属性中的rotate，使用[布局分析](../harmonyos-guides/ide-arkui-inspector.md)ArkUI Inspector看到虽然当前页面样式已旋转，但内部并没有旋转，Slider组件仍在原先的位置，因此无法滑动。

Q：Web组件同层渲染时，渲染的UI组件内又包含了一个Web组件，请问内层Web组件内是否有方法获取外层Web的window对象，类似前端iframe的window.parent方法？

A：目前同层渲染不支持内层Web获取到外层Web的window对象。
