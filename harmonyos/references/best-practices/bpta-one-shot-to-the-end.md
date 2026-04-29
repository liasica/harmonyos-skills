---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-one-shot-to-the-end
title: 一镜到底动效
breadcrumb: 最佳实践 > 动画与转场 > 一镜到底动效
category: best-practices
scraped_at: 2026-04-29T14:10:44+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c417ade85faa86881bbaefd95f7aac63fe9fca01307e0f608f3c9e99799e6ff3
---

## 概述

一镜到底动效是页面切换时对相同或者相似的两个元素做的一种位置、大小等属性匹配的过渡动画效果，有助于提升用户操作任务的效率，增强视觉的流畅感，同时也增强动效的品质感，是转场设计中重点推荐的技法。如下例所示，在点击图片后，该图片消失，同时在另一个位置出现新的图片，二者之间内容相同，可以对它们添加一镜到底动效。图1为不添加一镜到底动效的效果，图2为添加一镜到底动效的效果，一镜到底的效果能够让二者的出现消失产生联动，使得内容切换过程显得灵动自然而不生硬。

| 不添加一镜到底动效 | 添加一镜到底动效 |
| --- | --- |
|  |  |

## 实现原理

一镜到底动效中整个页面会以一种平滑的方式从一个场景过渡到另一个场景。这种转场效果常用于展示不同页面之间的关联性，能够给用户带来流畅的视觉体验。

根据场景，可以将一镜到底动效分为两类：

* 共享元素

  共享元素一般是转场前后持续存在的界面元素，即上文提到的持续元素，是在转场发生后希望用户关注到的焦点元素，它增强了转场的连续感。如下图，搜索框是共享元素。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/viKSHMm1S-icCVabgOG-Fg/zh-cn_image_0000002193851792.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=F65F834C9D9FDFC8EE2EF4542752A5767A86C72E1F0536D6CBFFC3596BA39D5C)
* 共享容器

  当一组元素在过渡时包含明确的边界，可使用容器来让转换过程有连续感。容器通过大小、高度、圆角等属性进行补间过渡转换，容器内的元素可通过淡入淡出或共享元素的手法进行过渡。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/TmrJogTKTqqRo1bn-wnyDQ/zh-cn_image_0000002229451681.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=BA405CE420F42D4885B7A2623437AEF163FEF8F1E09B06CB23F26EE8E5350EE7)

根据场景，可以将本文的案例分为以下两类。

| 场景分类 | 场景案例 | 实现方式 |
| --- | --- | --- |
| 共享元素转场 | [图片展开：双指放大](bpta-one-shot-to-the-end.md#li1714143812118) | 属性动画+节点迁移 |
| [图片展开：查看大图](bpta-one-shot-to-the-end.md#li1837152813249) | geometryTransition()+位移缩放 |
| [图片移动：半模态](bpta-one-shot-to-the-end.md#li3497202554819) | 属性动画+节点迁移 |
| [图标（搜索框、头像等）展开](bpta-one-shot-to-the-end.md#li3497202554819) | geometryTransition()+显示动画 |
| 共享容器转场 | [卡片展开](bpta-one-shot-to-the-end.md#section11650141951719) | Navigation自定义动画+位移缩放 |
| [列表展开](bpta-one-shot-to-the-end.md#section11650141951719) | geometryTransition()+显示动画 |
| [“图书”翻页展开一镜到底](bpta-one-shot-to-the-end.md#section268511598185) | Navigation自定义动画+旋转 |
| [视频展开](bpta-one-shot-to-the-end.md#section1347263162416) | Navigation自定义动画+节点迁移 |

一镜到底动效的实现需要转场能力和动画能力组合使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/Tb7EkONSSKeAJT6XSTH32A/zh-cn_image_0000002194011368.png?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=1F5FE220C564576C23851AA0822B988D3841C7ACB968A9F477931B28D7AE5426)

其中组件转场有三种方式实现，开发者可以根据需要选择合适的方式实现：

| 方式 | 特点 | 适用场景 |
| --- | --- | --- |
| [使用容器进行节点迁移](bpta-one-shot-to-the-end.md#section1922264051914) | 通过使用NodeController，将组件从一个容器迁移到另一个容器，在开始迁移时，需要根据前后两个布局的位置大小等信息对组件添加位移及缩放，确保迁移开始时组件能够对齐初始布局，避免出现视觉上的跳变现象。之后再添加动画将位移及缩放等属性复位，实现组件从初始布局到目标布局的一镜到底过渡效果。 | 适用于新建对象开销大的场景，如视频直播组件点击转为全屏等。 |
| [使用geometryTransition()共享元素转场](bpta-one-shot-to-the-end.md#section117061757174220) | 利用系统能力，转场前后两个组件调用geometryTransition()接口绑定同一id，同时将转场逻辑置于animateTo动画闭包内，这样系统侧会自动为二者添加一镜到底的过渡效果。 | 此方式适用于创建新节点开销小的场景。 |
| [使用Navigation自定义动画转场](bpta-one-shot-to-the-end.md#section1168010819268) | 进行路由跳转，customNavContentTransition事件提供自定义转场动画的能力。 | 适用于页面切换转场，如标题页和详情页之间的转场。 |

### 使用容器进行节点迁移

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)作为一个占位容器组件，主要是用于自定义节点以及自定义节点树的显示和复用。NodeController提供了一系列生命周期回调，通过[makeNode()](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)回调返回一个 [FrameNode](../harmonyos-references/js-apis-arkui-framenode.md#framenode-1)节点树的根节点。将[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点树挂载到对应的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)下。同时提供了[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)、[aboutToDisappear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)、[aboutToResize()](../harmonyos-references/js-apis-arkui-nodecontroller.md#abouttoresize)、[onTouchEvent()](../harmonyos-references/js-apis-arkui-nodecontroller.md#ontouchevent)、[rebuild()](../harmonyos-references/js-apis-arkui-nodecontroller.md#rebuild)五个回调方法用于监听对应的NodeContainer的状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/yj0r466pS-urKbZ0V5Xckg/zh-cn_image_0000002229451661.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=2C9AD146F30665AF3E2DB8A5A07362C68509FCC2293C3870734C2F7F705659AE)

举个简单的例子，例如上图，卡片状态可以分为两个形态，折叠态和展开态。开发者可以将折叠态和展开态分为两个节点NodeContainer1和NodeContainer2来控制二者之间的相互切换。NodeController触发onRemove()方法使NodeContainer1下树，调用update()方法更新卡片的展开状态，节点迁移至NodeContainer2，并触发动画。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/3C7CKrNUQUCYFQ10Ky1PSA/zh-cn_image_0000002455271744.png?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=8293BEF54452090B20BB6B9121A31A78A43AFE7DA9779BCA934D466C64A05CED)

### 使用geometryTransition()共享元素转场

[geometryTransition()](../harmonyos-references/ts-transition-animation-geometrytransition.md)接口用于组件内隐式共享元素转场，在视图状态切换过程中提供丝滑的上下文继承过渡体验。

geometryTransition()的使用方式为对需要添加一镜到底动效的两个组件使用geometryTransition()接口绑定同一id，这样在其中一个组件消失同时另一个组件创建出现的时候，系统会对二者添加一镜到底动效。

geometryTransition()绑定两个对象的实现方式使得geometryTransition()区别于其他方法，最适合用于两个不同对象之间完成一镜到底。

### 使用Navigation自定义动画转场

Navigation通过[customNavContentTransition()](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)事件提供自定义转场动画的能力，通过如下三步可以定义一个自定义的转场动画。

1. 构建一个自定义转场动画工具类CustomNavigationUtils，通过一个Map管理各个页面自定义动画对象CustomTransition，页面在创建的时候将自己的自定义转场动画对象注册进去，销毁的时候解注册。
2. 实现一个转场协议对象[NavigationAnimatedTransition](../harmonyos-references/ts-basic-components-navigation.md#navigationanimatedtransition11)，其中timeout属性表示转场结束的超时时间，默认为1000ms，transition属性为自定义的转场动画方法，开发者要在这里实现自己的转场动画逻辑，系统会在转场开始时调用该方法，onTransitionEnd为转场结束时的回调。
3. 调用customNavContentTransition()方法，返回实现的转场协议对象，如果返回undefined，则使用系统默认转场。

## 元素转场案例

### 图片展开一镜到底

* 双指放大转场

  图片使用双指放大转场显示图片详情页。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/u1vvEWNNQXO74HDhoervBg/zh-cn_image_0000002194011400.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=8C1C5E7C39E699998BF46B91977851625508920602EAC550F980E2D85004DFAB)

  通过NodeContainer组件实现跨节点迁移，通过手势捏合来控制节点的上下树，达成一镜到底动效。

  1. 小图模式和大图模式分别为两个页面，通过监听expand值来进行页面切换。

     ```
     1. @StorageProp('expand') @Watch('goToPageTwo') num1: number = 0;
     2. // ...

     4. aboutToAppear(): void {
     5. if (!getMyNode()) {
     6. createMyNode(this.getUIContext(), false);
     7. }
     8. this.imageGalleryNodeController = getMyNode();
     9. }
     ```

     [PinchToShareImagePageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/PinchToShareImage/PinchToShareImagePageOne.ets#L28-L49)
  2. 创建NodeContainer节点类。

     ```
     1. export class ImageGalleryNodeController extends NodeController {
     2. private rootNode: BuilderNode<[Params]> | null = null;
     3. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ImageGalleryBuilder);
     4. private isExpand: boolean = false;

     6. constructor(isExpand: boolean) {
     7. super();
     8. this.isExpand = isExpand;
     9. }

     11. makeNode(uiContext: UIContext): FrameNode | null {
     12. if (this.rootNode === null) {
     13. this.rootNode = new BuilderNode(uiContext);
     14. this.rootNode.build(this.wrapBuilder, { isExpand: this.isExpand });
     15. }
     16. return this.rootNode.getFrameNode();
     17. }

     19. init(uiContext: UIContext) {
     20. this.rootNode = new BuilderNode(uiContext);
     21. this.rootNode.build(this.wrapBuilder, { isExpand: this.isExpand });
     22. }

     24. update(isExpand: boolean) {
     25. if (this.rootNode !== null) {
     26. this.rootNode.update({ isExpand });
     27. }
     28. }
     29. }
     ```

     [ImageGalleryNode.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/PinchToShareImage/ImageGalleryNode.ets#L58-L87)
  3. 在小图界面当对图片进行双指捏合操作时，改变isExpand值。

     ```
     1. PinchGesture()
     2. .onActionStart((event: GestureEvent) => {
     3. this.offsetY = getTranslateToFullScreen(this.getUIContext(), 'swiper')?.offsetY || 0
     4. this.imageHeight = this.getUIContext().vp2px(Number(event.target.area.height))
     5. this.imageWidth = this.getUIContext().vp2px(Number(event.target.area.width))
     6. this.status = Status.PINCHING;
     7. this.updateCenter([this.getUIContext().vp2px(event.pinchCenterX),
     8. this.getUIContext().vp2px(event.pinchCenterY)])
     9. this.updateTranslateAccordingToCenter();
     10. this.startGestureScale = this.imageScale;
     11. this.gestureCount++;
     12. })
     13. .onActionUpdate((event: GestureEvent) => {
     14. this.imageScale = this.startGestureScale * event.scale;
     15. if (!this.isExpand && this.imageScale >= 1) {
     16. this.onExpand();
     17. }
     18. this.updateExtremeOffset();
     19. })
     ```

     [ImageWithGesture.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/PinchToShareImage/ImageWithGesture.ets#L368-L386)
  4. 当expand值更改时，页面进行切换到大图页面，完成一镜到底页面切换。

     ```
     1. NavDestination() {
     2. NodeContainer(this.imageGalleryNodeController)
     3. }
     4. .mode(NavDestinationMode.DIALOG)
     5. .height('100%')
     6. .width('100%')
     7. .hideTitleBar(true)
     8. .onReady((context: NavDestinationContext) => {
     9. this.pageInfo = context.pathStack;
     10. const param = context.pathInfo?.param as Record<string, Object>;
     11. this.onBack = param['onBack'] as () => void;
     12. })
     13. .onBackPressed(() => {
     14. AppStorage.setOrCreate('reset', new Date());
     15. this.getUIContext().animateTo({ duration: 300, curve: Curve.EaseIn }, () => {
     16. this.backToPageOne();
     17. })
     18. return true;
     19. })
     ```

     [PinchToShareImagePageTwo.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/PinchToShareImage/PinchToShareImagePageTwo.ets#L46-L64)
* 查看大图转场

  比如图片在九宫格中显示，点击查看大图，同时还支持手势下拉返回到九宫格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/noWH8Oe-Rmq_Y92_Ar4M2g/zh-cn_image_0000002193851824.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=10AB2A1B966A0781BCA65D71901FF554DA81C377447C7416B7EE0A98208AFBE7)

  设置geometryTransition属性将图片首页和大图页面的图片绑定同一id值，结合属性动画效果实现一镜到底效果。核心代码如下：

  1. 首页通过网格布局实现三行三列图片布局，并给每个图片设置geometryTransition属性，绑定唯一id值，绑定共享的两个图片组件。

     ```
     1. NavDestination() {
     2. Column() {
     3. Grid(this.scroller) {
     4. ForEach(this.data, (item: number) => {
     5. GridItem() {
     6. if (this.clickedIndex !== item || (this.isFirstPageShow)) {
     7. Image($r(`app.media.img_${item % 9}`))
     8. .width('100%')
     9. .height('100%')
     10. .objectFit(ImageFit.Cover)
     11. .id('item2_' + item)
     12. .onClick(() => {
     13. this.onItemClick(item);
     14. })
     15. .geometryTransition(this.clickedIndex === item ? 'app.media.img_' + item.toString() : '')
     16. .transition(TransitionEffect.opacity(0.99))
     17. }
     18. }
     19. .width(this.getUIContext().px2vp(381))
     20. .height(this.getUIContext().px2vp(381))
     21. }, (item: number) => item + '')
     22. }
     23. .rowsTemplate('1fr 1fr 1fr')
     24. .columnsTemplate('1fr 1fr 1fr')
     25. .columnsGap(2)
     26. .rowsGap(2)
     27. .size({
     28. width: this.getUIContext().px2vp(1169),
     29. height: this.getUIContext().px2vp(1169)
     30. })
     31. .margin({ top: 16 })
     32. }
     33. }
     34. .title('View larger picture')
     35. .height('100%')
     36. .width('100%')
     37. .onReady((context: NavDestinationContext) => {
     38. this.pageInfo = context.pathStack;
     39. })
     ```

     [ShowLargeImageWithGesturePageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/ShowLargeImageWithGesture/ShowLargeImageWithGesturePageOne.ets#L71-L110)
  2. 通过属性动画来进行小图和大图页面的切换，同时为了避免触发Navigation的转场动画，在pushPath()的时候把动画选项设置成了false。

     ```
     1. onItemClick(index: number): void {
     2. let param: Record<string, Object> = {};
     3. this.needFollow = false;
     4. this.clickedIndex = index;
     5. param['selectedIndex'] = this.clickedIndex;
     6. param['onIndexChange'] = (index: number) => {
     7. this.onIndexChange(index);
     8. };
     9. param['onBackToFirstPage'] = () => {
     10. this.onBack();
     11. }

     13. this.getUIContext().animateTo({
     14. duration: 250,
     15. curve: Curve.EaseIn,
     16. }, () => {
     17. this.pageInfo.pushPath({ name: 'ShowLargeImageWithGesturePageTwo', param: param }, false);
     18. this.isFirstPageShow = false;
     19. })
     20. }
     ```

     [ShowLargeImageWithGesturePageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/ShowLargeImageWithGesture/ShowLargeImageWithGesturePageOne.ets#L37-L57)
* 半模态转场

  图片从页面向半模态弹窗中转场显示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/bBMv2AQnTg2JjXjFIkCvHA/zh-cn_image_0000002193851788.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=96AE55AADB1B0A846C260584419AEBB90A752900D042E467D75AF3951F6A9DF8)

  利用NodeContainer组件实现跨节点迁移，将半模态SheetOptions()中的mode设置为SheetMode.EMBEDDED，该模式下新起的页面可以覆盖在半模态弹窗上，页面返回后该半模态依旧存在，半模态面板内容不丢失。通过属性动画，展示组件从初始界面至半模态页面的一镜到底动效，并在动画结束时关闭页面，并将该组件迁移至半模态页面。

  1. 创建NodeContainer节点类。

     ```
     1. export class MyNodeController extends NodeController {
     2. // ...
     3. }
     ```

     [CustomComponent.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/SemiModalImage/CustomComponent.ets#L27-L75)
  2. 首页图片绑定半模态弹窗，并通过bindContentCover设置模态转场动画。

     ```
     1. NavDestination() {
     2. Column() {
     3. Image($r('app.media.flower'))
     4. .opacity(this.opacityDegree)
     5. .width('90%')
     6. .id('origin')
     7. .enabled(this.isEnabled)
     8. .onClick(() => {
     9. this.originInfo = this.calculateData('origin');
     10. this.scaleValue = this.originInfo.scale;
     11. this.translateX = this.originInfo.translateX;
     12. this.translateY = this.originInfo.translateY;
     13. this.clipWidth = this.originInfo.clipWidth;
     14. this.clipHeight = this.originInfo.clipHeight;
     15. this.radius = 0;
     16. this.opacityDegree = 0;
     17. this.isShowSheet = true;
     18. this.isShowOverlay = true;
     19. // Set the artwork to non-interactive interrupt resistant.
     20. this.isEnabled = false;
     21. })
     22. }
     23. .width('100%')
     24. .height('100%')
     25. .padding({ top: 16 })
     26. .alignItems(HorizontalAlign.Center)
     27. .bindSheet(this.isShowSheet, this.mySheet(), {
     28. mode: SheetMode.EMBEDDED,
     29. height: this.bindSheetHeight,
     30. onDisappear: () => {
     31. // Ensure that the state is correct when the half-mode disappears.
     32. this.isShowImage = false;
     33. this.isShowSheet = false;
     34. // Set a mirror at the end of the animation to enter the trigger state.
     35. this.isAnimating = false;
     36. // The artwork becomes interoperable again.
     37. this.isEnabled = true;
     38. }
     39. })
     40. .bindContentCover(this.isShowOverlay, this.overlayNode(), {
     41. // The modal page is set to no transition
     42. transition: TransitionEffect.IDENTITY
     43. })
     44. }
     45. .backgroundColor('#F1F3F5')
     46. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
     47. .title('half mode')
     ```

     [Index.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/SemiModalImage/Index.ets#L165-L212)
  3. 点击首页图片后将图片节点迁移至半模态，当半模态完成布局之后，触发onLayoutComplete()函数，获取到图片初始位置和半模态位置，通过自定义显示动画完成一镜到底的效果。

     ```
     1. aboutToAppear(): void {
     2. // Set the layout of the image on the half mode to complete the callback.
     3. let onLayoutComplete: () => void = (): void => {
     4. // Grab the layout information when the target image layout is complete.
     5. this.targetInfo = this.calculateData('target');
     6. // Only half modes are correctly laid out and a mirror is triggered when there is no animation at this time.
     7. if (this.targetInfo.scale !== 0 && this.targetInfo.clipWidth !== 0 && this.targetInfo.clipHeight !== 0 &&
     8. !this.isAnimating) {
     9. this.isAnimating = true;
     10. // Property animation for long-take of a modal page.
     11. this.getUIContext().animateTo({
     12. duration: 1000,
     13. curve: Curve.Friction,
     14. onFinish: () => {
     15. // Custom node subtree on overlay page.
     16. this.isShowOverlay = false;
     17. // Custom nodes on the semi-modal tree, thus completing node migration.
     18. this.isShowImage = true;
     19. }
     20. }, () => {
     21. this.scaleValue = AppStorage.get('currentBreakpoint') === 'md' ? 0.382 : this.targetInfo.scale;
     22. this.translateX = AppStorage.get('currentBreakpoint') === 'md' ? 93.5 : this.targetInfo.translateX;
     23. this.clipWidth = AppStorage.get('currentBreakpoint') === 'md' ? 525 : this.targetInfo.clipWidth;
     24. this.clipHeight = AppStorage.get('currentBreakpoint') === 'md' ? 785 : this.targetInfo.clipHeight;
     25. // Fixed height differences due to half-mode height and scaling.
     26. this.translateY = this.targetInfo.translateY +
     27. (this.getUIContext().px2vp(WindowUtils.windowHeight_px) - this.bindSheetHeight -
     28. this.getUIContext().px2vp(WindowUtils.navigationIndicatorHeight_px) -
     29. this.getUIContext().px2vp(WindowUtils.topAvoidAreaHeight_px)) -
     30. (AppStorage.get('currentBreakpoint') === 'md' ? 134.3 : 0);
     31. // Fixed differences in rounded corners due to scaling.
     32. this.radius = this.sheetRadius / this.scaleValue;
     33. })
     34. // The artwork goes from transparent to animated.
     35. this.getUIContext().animateTo({
     36. duration: 2000,
     37. curve: Curve.Friction,
     38. }, () => {
     39. this.opacityDegree = 1;
     40. })
     41. }
     42. };
     43. // Open layout listening.
     44. this.listener.on('layout', onLayoutComplete);
     45. }
     ```

     [Index.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ImageLongTakeTransition/SemiModalImage/Index.ets#L63-L108)

### 图标（搜索框、头像等）展开一镜到底

搜索框点击后，转场到搜索结果页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/0SKw3kH2QJSunMDnWYXGkg/zh-cn_image_0000002229337185.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=BEE257974C4EEA02EB88B90D5A20B909CCAF21E93B2B0E386740AFE4351FC6A8)

将搜索框首页与搜索框页面的Search组件同时设置geometryTransition属性，并绑定同一id值。设置显式动画和transition属性的转场效果，实现搜索框的一镜到底效果。

1. 搜索框首页在Search组件添加geometryTransition属性，并绑定id值，禁用掉Navigation本身转场的动画。

   ```
   1. // Search animation
   2. private showSearchPage(): void {
   3. this.transitionEffect = TransitionEffect.OPACITY;
   4. this.getUIContext().animateTo({
   5. curve: curves.interpolatingSpring(0, 1, 342, 38)
   6. }, () => {
   7. this.pageInfos.pushPath({ name: 'SearchLongTakeTransitionPageTwo' }, false);
   8. })
   9. }
   ```

   [SearchLongTakeTransitionPageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/SearchLongTakeTransition/SearchLongTakeTransitionPageOne.ets#L73-L81)
2. 搜索页面中的Search组件添加geometryTransition()，并添加与搜索框首页中的同一id值。

   ```
   1. Search({ placeholder: 'Search' })
   2. .height(40)
   3. .placeholderColor($r('sys.color.mask_secondary'))
   4. .width('100%')
   5. // set geometry transition
   6. .geometryTransition('SEARCH_ONE_SHOT_DEMO_TRANSITION_ID', { follow: true })
   7. .backgroundColor('#0D000000')
   8. .defaultFocus(false)
   9. .focusOnTouch(false)
   10. .focusable(false)
   ```

   [SearchLongTakeTransitionPageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/SearchLongTakeTransition/SearchLongTakeTransitionPageOne.ets#L36-L45)

## 容器转场案例

### 卡片、列表展开一镜到底

在瀑布流或列表流布局中，当用户点击其中一个卡片或列表项时，应用将执行平滑的转场动画，引导用户从概览页面切换到详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/31NMvRkESAWspIXUypg5vg/zh-cn_image_0000002194011396.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=97CB8C493313F4FFA8E216C91B7C67D7106550922BB03AB75AD5436B4FE67CCF)

使用WaterFlow()和LazyForEach()实现卡片列表瀑布流。利用Navigation的自定义导航转场动画能力，通过customNavContentTransition()配置列表页与详情页的自定义导航转场动画，结合componentSnapshot()将卡片进行截图避免跳转页面白屏。

1. 卡片列表页使用WaterFlow和LazyForEach实现页面布局。

   ```
   1. private onColumnClicked(indexValue: string): void {
   2. let param: Record<string, Object> = {};
   3. let clickedIndex = parseInt(indexValue);
   4. param['indexValue'] = clickedIndex;
   5. this.clickedIndex = clickedIndex;
   6. // Click the card to get the corresponding screenshot and save it.
   7. this.getUIContext()
   8. .getComponentSnapshot()
   9. .get('FlowItem_' + indexValue, (error: BusinessError, pixelMap: image.PixelMap) => {
   10. if (error) {
   11. hilog.error(0x0000, 'CardLongTakePageOne',
   12. `componentSnapshot.get error, reason: Code is ${error.code}, message is ${error.message}`);
   13. // If the screenshot fails, go to the default left/right transition. In this case, the pop-up page will not receive clickedComponentId parameter, and the registration process will not proceed.
   14. // At that time from and to the animation are undefined, will go in customNavContentTransition transitions by default.
   15. this.pageInfos.pushPath({ name: 'CardLongTakeTransitionPageTwo', param: param });
   16. return;
   17. } else {
   18. hilog.info(0x0000, 'CardLongTakePageOne', 'componentSnapshot.get success!');
   19. // If the screenshot is successful, then go to a custom mirror in the end transition.
   20. param['clickedComponentId'] = CardUtil.getFlowItemIdByIndex(indexValue);
   21. param['doDefaultTransition'] = () => {
   22. this.doFinishTransition();
   23. };
   24. SnapShotImage.pixelMap = pixelMap;
   25. this.pageInfos.pushPath({ name: 'CardLongTakeTransitionPageTwo', param: param });
   26. this.dataSource.getData(this.clickedIndex).isVisible = Visibility.Hidden;
   27. }
   28. })
   29. }
   ```

   [CardLongTakeTransitionPageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/CardLongTakeTransition/CardLongTakeTransitionPageOne.ets#L103-L132)
2. 卡片详情页通过Navigation自定义动画实现一镜到底。这里套了两层Stack()，因为要放截图，以及把原来的详情页内容转移过来。缩放、translate属性设置在Stack()这层上实现边界动画，透明度属性设置在截图上实现内容过渡。在onReady()里面注册自定义动画，通过id对动画属性进行初始化。

   ```
   1. // Try to register a custom transition animation to restore the page properties to their normal state in case of an exception.
   2. tryRegisterCustomTransition(clickedCardId: string): void {
   3. try {
   4. // First initialize some transition information.
   5. this.longTakeAnimationProperties.init(clickedCardId, this.prePageDoFinishTransition);
   6. CustomTransition.getInstance().registerNavParam(this.pageId, 2000,
   7. (transitionProxy: NavigationTransitionProxy) => {
   8. this.longTakeAnimationProperties.doAnimation(transitionProxy);
   9. });
   10. hilog.info(0x0000, 'CardLongTakePageTwo', 'register successes');
   11. } catch (error) {
   12. let err = error as BusinessError;
   13. hilog.error(0x0000, 'CardLongTakePageTwo', `this is error:code=${err.code}, message=${err.message}`);
   14. this.longTakeAnimationProperties.setFinalStatus();
   15. }
   16. }

   18. // ...

   20. build() {
   21. NavDestination() {
   22. // Stack needs to set the alignContent to TopStart, otherwise the screenshot and content will be repositioned with the height as it changes.
   23. Stack({ alignContent: Alignment.TopStart }) {
   24. Stack({ alignContent: Alignment.TopStart }) {
   25. // Used to display a screenshot of the card clicked on the previous page.
   26. Image(this.snapShotImage)
   27. .size(this.longTakeAnimationProperties.snapShotSize)
   28. .objectFit(ImageFit.Auto)
   29. .opacity(this.longTakeAnimationProperties.snapShotOpacity)
   30. // eslint-disable-next-line @performance/hp-arkui-image-async-load
   31. .syncLoad(true)// The position here gives the distance from the screenshot position to the expanded page image position.
   32. .position({
   33. x: this.longTakeAnimationProperties.snapShotPositionX,
   34. y: this.longTakeAnimationProperties.snapShotPositionY
   35. })

   37. // The pop-up page originally displays the content, adding transparency to control its display during animation.
   38. DetailPageContent({
   39. indexValue: this.indexValue,
   40. pageInfos: this.pageInfos,
   41. onBackPressed: () => {
   42. this.onBackPressed()
   43. },
   44. SharedComponentId: CardUtil.getPostPageImageId(this.clickedCardId)
   45. })
   46. .size({
   47. width: '100%',
   48. height: '100%'
   49. })
   50. .opacity(this.longTakeAnimationProperties.postPageOpacity)
   51. }
   52. .width('100%')
   53. .position({
   54. x: this.longTakeAnimationProperties.positionXValue,
   55. y: this.longTakeAnimationProperties.positionYValue
   56. })
   57. }
   58. .scale({
   59. x: this.longTakeAnimationProperties.scaleValue,
   60. y: this.longTakeAnimationProperties.scaleValue
   61. })
   62. .translate({
   63. x: this.longTakeAnimationProperties.translateX,
   64. y: this.longTakeAnimationProperties.translateY
   65. })
   66. .width(this.longTakeAnimationProperties.clipWidth)
   67. .height(this.longTakeAnimationProperties.clipHeight)
   68. .borderRadius(this.longTakeAnimationProperties.radius)
   69. .expandSafeArea([SafeAreaType.SYSTEM])
   70. .backgroundColor($r('app.color.water_flow_background_color'))
   71. .clip(true)
   72. }
   73. .backgroundColor(this.longTakeAnimationProperties.navDestinationBgColor)
   74. .GestureStyles()
   75. .hideTitleBar(true)
   76. .onReady((context: NavDestinationContext) => {
   77. this.pageInfos = context.pathStack;
   78. let param = context.pathInfo?.param as Record<string, Object>;
   79. let clickedCardId = param['clickedComponentId'] as string;
   80. this.indexValue = param['indexValue'] as number;
   81. this.prePageDoFinishTransition = param['doDefaultTransition'] as () => void;
   82. if (context.navDestinationId && clickedCardId) {
   83. this.pageId = context.navDestinationId;
   84. this.clickedCardId = clickedCardId;
   85. this.tryRegisterCustomTransition(clickedCardId);
   86. }
   87. })
   88. .onBackPressed(() => {
   89. return this.onBackPressed();
   90. })
   91. .onDisAppear(() => {
   92. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   93. })
   94. }

   96. // ...
   ```

   [CardLongTakeTransitionPageTwo.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/CardLongTakeTransition/CardLongTakeTransitionPageTwo.ets#L61-L205)

列表一镜到底效果图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bpWb1QH6SXSNCTolyb7RLw/zh-cn_image_0000002229451697.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=00720D9606CA108623E5A4E45FF9DD991846208DC9E150E7574E31975B43EF39)

将列表项与详情页面同时设置geometryTransition属性，并绑定同一id值。每个列表项设置显式动画和transition属性的转场效果，实现列表展开的一镜到底效果。

1. 列表页面中每一个列表项设置geometryTransition属性，并绑定当前列表的id值。

   ```
   1. @Component
   2. export struct MyButton {
   3. @Prop listContent: ListContent;
   4. @Prop indexValue: string;
   5. @State scaleValue: number = 1;

   7. build() {
   8. Column({ space: 10 }) {
   9. Row({ space: 5 }) {
   10. Line()
   11. .startPoint([0, 0])
   12. .endPoint([0, 20])
   13. .strokeWidth(5)
   14. .stroke(Color.Yellow)
   15. .strokeLineCap(LineCapStyle.Round)
   16. Text(this.listContent.title)
   17. .fontWeight(FontWeight.Medium)
   18. .fontSize(16)
   19. }

   21. Text(this.listContent.content)
   22. .fontColor(Color.Grey)
   23. .maxLines(1)
   24. .textOverflow({ overflow: TextOverflow.Ellipsis })
   25. .fontSize(14)
   26. }
   27. .alignItems(HorizontalAlign.Start)
   28. .padding({
   29. left: 20,
   30. right: 20,
   31. top: 20,
   32. bottom: 20
   33. })
   34. .width('91%')
   35. .backgroundColor(Color.White)
   36. .clip(true)
   37. .borderRadius(20)
   38. .scale({
   39. x: this.scaleValue,
   40. y: this.scaleValue
   41. })
   42. .geometryTransition(this.indexValue, { follow: true })
   43. .onTouch((event?: TouchEvent) => {
   44. this.onTouchProcess(event);
   45. })
   46. .onClick(() => {
   47. this.onButtonClicked?.(this.indexValue);
   48. })
   49. }

   51. onButtonClicked: (index: string) => void = (_index: string) => {
   52. };

   54. private onTouchProcess(event?: TouchEvent): void {
   55. if (!event) {
   56. return;
   57. }
   58. if (event.type === TouchType.Down) {
   59. this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 350, 35) }, () => {
   60. this.scaleValue = 0.95;
   61. })
   62. } else if (event.type === TouchType.Up) {
   63. this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 350, 35) }, () => {
   64. this.scaleValue = 1;
   65. })
   66. } else if (event.type === TouchType.Cancel) {
   67. this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 350, 35) }, () => {
   68. this.scaleValue = 1;
   69. })
   70. }
   71. }
   72. }
   ```

   [ListLongTakeTransitionPageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ListLongTakeTransition/ListLongTakeTransitionPageOne.ets#L125-L197)
2. 列表详情页中的容器组件Column组件设置geometryTransition属性，并绑定对应列表项的id值，完成一镜到底效果。

   ```
   1. NavDestination() {
   2. Column({ space: 20 }) {
   3. Text(this.param.title)
   4. .fontSize(30)
   5. .fontWeight(FontWeight.Medium)
   6. Text(this.param.content)
   7. .fontColor($r('sys.color.password_icon_focus_color'))
   8. .lineHeight(28)
   9. .fontSize(16)
   10. }
   11. .alignItems(HorizontalAlign.Start)
   12. .clip(true)
   13. .size({
   14. width: '100%',
   15. height: '100%'
   16. })
   17. .geometryTransition(this.param.geometryId)
   18. }
   19. .padding({
   20. top: 46,
   21. left: 16,
   22. right: 16
   23. })
   24. .backgroundColor(Constants.DEFAULT_BG_COLOR)
   25. .transition(TransitionEffect.OPACITY)
   26. .hideTitleBar(true)
   27. .backgroundColor(Color.Transparent)
   28. .onReady((context: NavDestinationContext) => {
   29. this.pageInfos = context.pathStack;
   30. this.param = (context.pathInfo.param as ListDetailPageExtraInfo);
   31. })
   32. .onBackPressed(() => {
   33. this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 342, 38) }, () => {
   34. this.pageInfos.pop(false);
   35. })
   36. return true;
   37. })
   ```

   [ListLongTakeTransitionPageTwo.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/ListLongTakeTransition/ListLongTakeTransitionPageTwo.ets#L32-L69)

### “图书”翻页展开一镜到底

阅读类应用中，点击一本“图书”的图标后，模拟图书翻页展开的效果，转场到书本内容页面，同时支持手势返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/FymWUTaYRtKgoJUSgKTEkA/zh-cn_image_0000002229337193.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=C7A4B1FE4FF57A22A49408E358697266FCBA94C670804118618FC047444252B8)

利用Navigation的自定义导航转场动画能力，通过customNavContentTransition()配置书籍页与详情页的自定义导航转场动画实现图书翻页一镜到底效果。使用rotate属性实现书籍翻页的旋转效果。

1. 书架页面通过Grid组件实现书架第一行书籍布局，使用Swiper()组件实现书架第一行书籍布局。

   ```
   1. build() {
   2. NavDestination() {
   3. Scroll() {
   4. Column({ space: 12 }) {
   5. // A mirror returns to the first position.
   6. Grid() {
   7. ForEach(this.dataSource, (item: BookItem, index: number) => {
   8. GridItem() {
   9. Image($r(item.coverImageUrl))
   10. .id(item.id)
   11. .width('100%')
   12. .onClick(() => {
   13. this.onColumnClicked(item.id, item.coverImageUrl, this.dataSource[0].id, () => {
   14. this.dataSource.sort((a, b) => b.timestamp - a.timestamp);
   15. })
   16. this.dataSource[index].timestamp = Number(new Date());
   17. })
   18. }
   19. .width(this.columnWidth)
   20. }, (item: BookItem) => JSON.stringify(item))
   21. }
   22. .padding({
   23. left: 12,
   24. right: 12,
   25. top: 12
   26. })
   27. .columnsTemplate(this.columnType)
   28. .columnsGap(10)
   29. .rowsGap(10)

   31. // A mirror is returned to its original position.
   32. Column({ space: 12 }) {
   33. Text('Recently read')
   34. .fontSize(16)
   35. .fontWeight(FontWeight.Medium)
   36. .fontColor(Color.Gray)
   37. Swiper(this.swiperController) {
   38. ForEach(this.recentData, (item: BookItem) => {
   39. GridItem() {
   40. Image($r(item.coverImageUrl))
   41. .id(item.id)
   42. .onClick(() => {
   43. this.onColumnClicked(item.id, item.coverImageUrl);
   44. })
   45. }
   46. }, (item: BookItem) => JSON.stringify(item))
   47. }
   48. .indicator(false)
   49. .displayCount(3)
   50. .loop(false)
   51. .itemSpace(10)
   52. }
   53. .padding({
   54. left: 12,
   55. right: 12
   56. })
   57. .alignItems(HorizontalAlign.Start)
   58. }
   59. }
   60. }
   61. // ...
   62. }

   64. // ...

   66. private onColumnClicked(bookId: string, bookCoverUrl: string, toBookId?: string, prePageCallback?: () => void): void {
   67. try {
   68. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   69. const fromCardItemInfo: RectInfoInPx =
   70. ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), bookId);
   71. let param: Record<string, Object> = {};
   72. param['fromCardItemInfo'] = fromCardItemInfo;
   73. param['bookCoverUrl'] = bookCoverUrl;
   74. if (toBookId) {
   75. const toCardItemInfo: RectInfoInPx =
   76. ComponentAttrUtils.getRectInfoById(WindowUtils.window.getUIContext(), toBookId);
   77. param['toCardItemInfo'] = toCardItemInfo;
   78. }
   79. if (prePageCallback) {
   80. param['prePageCallback'] = prePageCallback;
   81. }
   82. this.pageInfos.pushPath({ name: 'BookFlipLongTakeTransitionPageTwo', param: param });
   83. } catch (err) {
   84. let error = err as BusinessError;
   85. hilog.error(0x0000, 'BookFlipLongTakeTransitionPageOne',
   86. `onColumnClicked failed. error code=${error.code}, message=${error.message}`);
   87. }
   88. }
   ```

   [BookFlipLongTakeTransitionPageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/BookFlipLongTakeTransition/BookFlipLongTakeTransitionPageOne.ets#L70-L187)
2. 书籍详情页通过Navigation自定义动画实现一镜到底。

   ```
   1. NavDestination() {
   2. Stack() {
   3. Column() {
   4. Text($r('app.string.DetailPage_text'))
   5. .fontColor($r('sys.color.password_icon_focus_color'))
   6. .lineHeight(28)
   7. .fontSize(16)
   8. }
   9. .width(AppStorage.get('currentBreakpoint') === 'md' ? '75%' : '100%')
   10. .height('100%')
   11. .alignItems(HorizontalAlign.Start)
   12. .padding({
   13. left: 16,
   14. right: 16,
   15. top: 46
   16. })

   18. if (!this.doDefaultTransition) {
   19. Image($r(this.bookCoverUrl))
   20. .objectFit(ImageFit.Cover)
   21. // eslint-disable-next-line @performance/hp-arkui-image-async-load
   22. .syncLoad(true)
   23. .rotate({
   24. x: 0,
   25. y: 1,
   26. z: 0,
   27. angle: this.bookFlipLongTakeTransitionProperties.coverRotateAngle,
   28. centerX: 0,
   29. centerY: '50%'
   30. })
   31. .scale({
   32. x: this.bookFlipLongTakeTransitionProperties.coverScale,
   33. centerX: 0,
   34. centerY: '50%'
   35. })
   36. }
   37. }
   38. .scale({
   39. x: this.bookFlipLongTakeTransitionProperties.scaleValue,
   40. y: this.bookFlipLongTakeTransitionProperties.scaleValue
   41. })
   42. .translate({
   43. x: this.bookFlipLongTakeTransitionProperties.translateX,
   44. y: this.bookFlipLongTakeTransitionProperties.translateY
   45. })
   46. .width(this.bookFlipLongTakeTransitionProperties.clipWidth)
   47. .height(this.bookFlipLongTakeTransitionProperties.clipHeight)
   48. .backgroundColor('#DEDFDF')
   49. }
   50. .backgroundColor(this.bookFlipLongTakeTransitionProperties.navDestinationBgColor)
   51. .GestureStyles()
   52. .hideTitleBar(true)
   53. .onReady((context: NavDestinationContext) => {
   54. this.pageInfos = context.pathStack;
   55. let param = context.pathInfo?.param as Record<string, Object>;
   56. this.bookCoverUrl = param['bookCoverUrl'] as string;
   57. this.fromCardItemInfo = param['fromCardItemInfo'] as RectInfoInPx;
   58. this.toCardItemInfo = (param['toCardItemInfo'] || param['fromCardItemInfo']) as RectInfoInPx;
   59. this.prePageCallback = param['prePageCallback'] as () => void;
   60. if (context.navDestinationId) {
   61. this.pageId = context.navDestinationId;
   62. }
   63. CustomTransition.getInstance()
   64. .registerNavParam(this.pageId, 500, (transitionProxy: NavigationTransitionProxy) => {
   65. this.bookFlipLongTakeTransitionProperties.doAnimation(transitionProxy, this.fromCardItemInfo,
   66. this.toCardItemInfo);
   67. }, () => {
   68. this.bookFlipLongTakeTransitionProperties.onInteractiveFinish();
   69. }, () => {
   70. this.bookFlipLongTakeTransitionProperties.onInteractive(
   71. this.fromCardItemInfo, this.toCardItemInfo);
   72. });
   73. })
   74. .onBackPressed(() => {
   75. return this.onBackPressed();
   76. })
   77. .onDisAppear(() => {
   78. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   79. })
   ```

   [BookFlipLongTakeTransitionPageTwo.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/BookFlipLongTakeTransition/BookFlipLongTakeTransitionPageTwo.ets#L80-L159)

### 视频展开一镜到底

视频组件从一个页面向目标页面的转场，在一镜到底的过程中，视频需要持续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Yj4kUqHFTHqySTI7N-whMQ/zh-cn_image_0000002193851796.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061036Z&HW-CC-Expire=86400&HW-CC-Sign=F4036ADC78402CBA69989EACA747E0E679F298B05ED650AF9DE9A2284EE40524)

使用WaterFlow()和LazyForEach()实现卡片列表瀑布流。利用NodeController实现组件的跨节点迁移，通过customNavContentTransition配置概览页与视频详情的自定义导航转场动画，给节点的迁移过程赋予一镜到底效果。

1. 创建NodeController节点类。

   ```
   1. export class MyNodeController extends NodeController {
   2. // ...
   3. }
   ```

   [NodeController.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/VideoLongTakeTransition/NodeController.ets#L32-L96)
2. 视频首页使用WaterFlow()和LazyForEach()实现页面布局，点击视频后将视频节点迁移至视频播放页面，通过Navigation自定义动画完成一镜到底的效果。

   ```
   1. NavDestination() {
   2. WaterFlow() {
   3. LazyForEach(this.dataSource, (_: CardAttr, index: number) => {
   4. FlowItem() {
   5. VideoCardComponent({
   6. isPlaying: false,
   7. index,
   8. onColumnClicked: (prePageCallback) => {
   9. this.onColumnClicked(`xComponent_${index}`, prePageCallback)
   10. }
   11. })
   12. }
   13. .width('100%')
   14. .borderRadius(10)
   15. .clip(true)
   16. .id('FlowItem_' + index.toString())
   17. }, (item: string) => item)
   18. }
   19. .edgeEffect(EdgeEffect.Spring)
   20. .onScrollIndex((first: number) => {
   21. this.scrollFirstIndex = first;
   22. })
   23. .padding(12)
   24. .columnsTemplate(this.columnType)
   25. .columnsGap(12)
   26. .rowsGap(10)
   27. .width('100%')
   28. .height('100%')
   29. }
   30. .backgroundColor(Constants.DEFAULT_BG_COLOR)
   31. .title(getResourceString(this.getUIContext(), $r('app.string.video_title'), this))
   32. .onReady((context: NavDestinationContext) => {
   33. this.pageInfos = context.pathStack;
   34. if (context.navDestinationId) {
   35. this.pageId = context.navDestinationId;
   36. }
   37. })
   38. .onDisAppear(() => {
   39. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   40. })
   ```

   [CustomNavigationPageOne.ets](https://gitcode.com/harmonyos_samples/transitions-collection/blob/master/entry/src/main/ets/feature/VideoLongTakeTransition/CustomNavigation/CustomNavigationPageOne.ets#L50-L90)

## 示例代码

* [实现转场动效功能合集](https://gitcode.com/harmonyos_samples/transitions-collection)
