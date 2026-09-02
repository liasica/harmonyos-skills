---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1063
title: 使用Swiper实现图片的一镜到底转场效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用Swiper实现图片的一镜到底转场效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:decda9ed97239bf4359b4decba3a74638f3663cba0da28ace9bb018fdd4a77bf
---

## 问题现象

如下代码中，oneBuilder和twoBuilder的图片元素如何在Swiper组件实现一镜到底的过渡效果？

```ts
@Entry
@Component
struct Demo {

  @Builder
  twoBuilder() {
    Column() {
      Image($r('app.media.app_image'))
        .height(58)
        .width(58)
        .objectFit(ImageFit.Auto)
        .margin({ right: 8, left: 8, top: 8 })
        .aspectRatio(1)
        .geometryTransition('cover') // 绑定标识符
    }
  }

  @Builder
  oneBuilder() {
    Column() {
      Image($r('app.media.app_image'))
        .height(230)
        .width(230)
        .objectFit(ImageFit.Auto)
        .margin({ right: 8, left: 8, top: 8 })
        .aspectRatio(1)
        .geometryTransition('cover', { follow: true }) // 绑定标识符
    }
  }

  build() {
    Column() {
      Swiper() {
        this.oneBuilder()
        this.twoBuilder()
      }
      .onChange((index: number) => {

      })
      .indicator(false)
      .displayCount(1, true)
      .clip(false)
      .loop(false)
      .autoPlay(false)
      .height('100%')
      .hitTestBehavior(HitTestMode.Transparent)
    }
    .padding({
      top: 55,
    })
    .size({ width: '100%', height: '100%' })
    .backgroundColor('#0d000000')
  }
}
```

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。
* [NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)：基础组件，用于挂载自定义节点（如FrameNode或BuilderNode），并通过[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)动态控制节点的上树和下树。
* [translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)：根据Swiper的实时偏移量，设置组件的平移属性，以实现组件的同步移动。

## 解决方案

该转场动效为交互式动画，需在Swiper滑动过程中实时绘制动画效果。实现方案如下：通过NodeContainer的节点迁移机制管理动画元素。监听Swiper的onContentDidScroll事件，获取实时偏移量。根据滑动位置position动态设置容器的平移量，以规避因状态变量更新导致的动画延迟。

1. 通过继承并实现NodeController类，以管理图片节点的自定义创建和显示等操作。同时需要重写NodeController的makeNode()方法。该方法会在NodeController实例绑定到NodeContainer时被调用，并将返回的节点挂载到NodeContainer上。

   ```ts
   class TransNodeController extends NodeController {
     private node?: BuilderNode<[Object]>;
     private listener: TransListener;

     constructor(listener: TransListener) {
       super();
       this.listener = listener;
     }

     makeNode(): FrameNode | null {
       return this.node?.getFrameNode() ?? null;
     }

     onAttach(): void {
       this.rebuild();
     }

     // 移动节点
     moveTo(target: TransNodeController) {
       this.detach();
       target.attach();
     }

     getPositionToWindow() {
       return this.node?.getFrameNode()?.getPositionToWindow();
     }

     attach(rebuild: boolean = true) {
       this.node = this.listener.onAttach();
       if (rebuild) {
         this.rebuild();
       }
     }

     detach() {
       if (this.node && this.listener.onDetach) {
         this.listener.onDetach(this.node);
       }
       this.node = undefined;
       this.rebuild();
     }

     hasNode() {
       return this.node != undefined;
     }
   }
   ```
2. 监听Swiper页面的滑动事件，获取实时偏移量，并结合NodeContainer的节点迁移与绘制动画，实现NodeContainer中图片节点的“一镜到底”式动态转场效果。

   ```ts
   .onContentDidScroll((selectedIndex, index, position) => {
     if (this.lastPositionToWindowX == 0) {
       this.lastPositionToWindowX = this.swiperInfos[selectedIndex].controller.getPositionToWindow()?.x ?? 0;
     }
     if (index == 1) {
       if (position >= 0 && position <= 1) {
         if (position < 0.99) {
           this.moveNode(0, 1);
         } else {
           this.moveNode(1, 0);
         }
         this.imageWidth = this.min_width + position * (this.max_width - this.min_width);
         this.swiperInfos[index].transNodeTranslate = 0;
       } else {
         this.swiperInfos[index].transNodeTranslate = position * 100;
       }
     } else if (index == 0) {
       if (position > 0) {
         this.swiperInfos[index].transNodeTranslate = position * 100;
       }
     }
     this.swiperInfos[index].translate = position * 100;
   })
   ```

   完整代码示例参考：

   ```ts
   import { BuilderNode, NodeController } from '@kit.ArkUI';

   //实现NodeController，用于自定义节点的创建、显示等操作的管理
   class TransNodeController extends NodeController {
     private node?: BuilderNode<[Object]>;
     private listener: TransListener;

     constructor(listener: TransListener) {
       super();
       this.listener = listener;
     }

     makeNode(): FrameNode | null {
       return this.node?.getFrameNode() ?? null;
     }

     onAttach(): void {
       this.rebuild();
     }

     // 移动节点
     moveTo(target: TransNodeController) {
       this.detach();
       target.attach();
     }

     getPositionToWindow() {
       return this.node?.getFrameNode()?.getPositionToWindow();
     }

     attach(rebuild: boolean = true) {
       this.node = this.listener.onAttach();
       if (rebuild) {
         this.rebuild();
       }
     }

     detach() {
       if (this.node && this.listener.onDetach) {
         this.listener.onDetach(this.node);
       }
       this.node = undefined;
       this.rebuild();
     }

     hasNode() {
       return this.node != undefined;
     }
   }

   interface TransListener {
     onAttach: () => BuilderNode<[Object]>;
     onDetach?: (node: BuilderNode<[Object]>) => void;
   }

   class TransNodeInfo {
     builder: () => void;

     constructor(builder: () => void) {
       this.builder = builder;
     }
   }

   @Component
   struct TransNodeContent {
     @BuilderParam builder: () => void = this.defaultBuilder;

     @Builder
     defaultBuilder() {
     }

     build() {
       Stack() {
         this.builder();
       }
     }
   }

   @Builder
   function TransNodeContentBuilder(info: TransNodeInfo) {
     TransNodeContent({ builder: info.builder });
   }

   @ObservedV2
   class SwiperItemInfo {
     controller: TransNodeController;

     constructor(controller: TransNodeController) {
       this.controller = controller;
     }

     // UI属性
     @Trace translate: number = 0;
     @Trace transNodeTranslate: number = 0;
   }

   @Entry
   @Component
   struct SwiperTransitionDemo {
     // 图片大小原始比例
     @State imageWidth: number = 1;
     // 最大宽度比和最小宽度比
     private max_width: number = 1;
     private min_width: number = 0.3;
     // 图片位置
     private lastPositionToWindowX: number = 0;
     // 共享图片builder node对象
     private transNode = new BuilderNode<[TransNodeContent]>(this.getUIContext());
     // node controller对象
     private swiperInfos: SwiperItemInfo[] = [
       new SwiperItemInfo(new TransNodeController({ onAttach: () => this.transNode })),
       new SwiperItemInfo(new TransNodeController({ onAttach: () => this.transNode }))
     ];

     aboutToAppear(): void {
       // 提前创建组件，提升页面响应速度
       this.transNode.build(wrapBuilder<[TransNodeInfo]>(TransNodeContentBuilder), new TransNodeInfo(() => {
         this.imageBuilder();
       }));
       this.swiperInfos[0].controller.attach(false);
       this.swiperInfos[1].translate = 100;
     }

     @Builder
     imageBuilder() {
       Image($r('app.media.startIcon'))
         .width('90%')
         .scale({
           x: this.imageWidth,
           y: this.imageWidth,
           centerX: 0,
           centerY: 0
         })
         .objectFit(ImageFit.Auto)
         .margin({ right: 8, left: 8, top: 8 })
         .aspectRatio(1)
         .geometryTransition('cover', { follow: true }) // 绑定标识符
     }

     @Builder
     oneBuilder(info: SwiperItemInfo, index: number) {
       // 使用堆叠容器，转场图片放到页面之上
       Stack() {
         Column() {
           // 内容区域
           Text('测试')
             .visibility(index === 0 ? Visibility.Hidden : Visibility.Visible)
             .padding({ top: 30, left: 30 })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(index === 0 ? Color.White : Color.Orange)
         .translate({ x: `${info.translate}%` })

         // 使用NodeContainer显示自定义节点
         NodeContainer(info.controller)
           .width('100%')
           .position({ x: 8, y: 8 })
           .translate({ x: `${info.transNodeTranslate}%` }) // 设置平移。
       }
       .position({ x: 0, y: 0 })
     }

     moveNode(src: number, dst: number) {
       if (!this.swiperInfos[dst].controller.hasNode()) {
         this.swiperInfos[src].controller.moveTo(this.swiperInfos[dst].controller);
       }
     }

     build() {
       Column() {
         Swiper() {
           ForEach(this.swiperInfos, (item: SwiperItemInfo, index) => {
             this.oneBuilder(item, index);
           }, (item: number) => Date.now() + '_' + item);
         }
         .indicator(false)
         .displayCount(1, true)
         .clip(false)
         .loop(false)
         .autoPlay(false)
         .width('100%')
         .height('100%')
         .effectMode(EdgeEffect.None)
         .hitTestBehavior(HitTestMode.Transparent)
         // 监听Swiper页面滑动事件，获取实时偏移量绘制动画。
         .onContentDidScroll((selectedIndex, index, position) => {
           if (this.lastPositionToWindowX == 0) {
             this.lastPositionToWindowX = this.swiperInfos[selectedIndex].controller.getPositionToWindow()?.x ?? 0;
           }
           if (index == 1) {
             if (position >= 0 && position <= 1) {
               if (position < 0.99) {
                 this.moveNode(0, 1);
               } else {
                 this.moveNode(1, 0);
               }
               this.imageWidth = this.min_width + position * (this.max_width - this.min_width);
               this.swiperInfos[index].transNodeTranslate = 0;
             } else {
               this.swiperInfos[index].transNodeTranslate = position * 100;
             }
           } else if (index == 0) {
             if (position > 0) {
               this.swiperInfos[index].transNodeTranslate = position * 100;
             }
           }
           this.swiperInfos[index].translate = position * 100;
         })

       }
       .padding({
         top: 55,
       })
       .size({ width: '100%', height: '100%' })
       .backgroundColor('#0d000000');
     }
   }
   ```
