---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode
title: BuilderNode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > BuilderNode
category: harmonyos-references
scraped_at: 2026-04-28T08:00:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4e9d3788a50d1e7fb6c1924e7dca769b6386de696bbf0f67d0512cf53200159
---

提供能够挂载系统组件的自定义节点BuilderNode。BuilderNode仅可作为叶子节点使用。使用方式参考[BuilderNode开发指南](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md)。最佳实践请参考[组件动态创建-组件动态添加、更新和删除](../best-practices/bpta-ui-dynamic-operations.md#section153921947151012)。

与BuilderNode相比，ReactiveBuilderNode能通过多参数的无状态UI方法@Builder生成组件树。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 若传入的Builder的根节点为语法节点（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)/[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)/[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)/[ContentSlot](../harmonyos-guides/arkts-rendering-control-contentslot.md)…）、[Span](ts-basic-components-span.md)、[ContainerSpan](ts-basic-components-containerspan.md)、[SymbolSpan](ts-basic-components-symbolspan.md)或自定义组件，将额外生成一个[FrameNode](js-apis-arkui-framenode.md)，在节点树中显示为“BuilderProxyNode”，这会导致树结构变化，影响某些测试的传递过程。详情参见[BuilderNode内的BuilderProxyNode导致树结构发生变化](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode内的builderproxynode导致树结构发生变化)。
* 如果在跨页面复用BuilderNode时显示异常，可参考[跨页面复用注意事项](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#跨页面复用注意事项)。
* 当前不支持在预览器中使用BuilderNode。
* BuilderNode下的自定义组件支持使用[@Prop装饰器](../harmonyos-guides/arkts-prop.md)。不支持使用[@Link装饰器](../harmonyos-guides/arkts-link.md)来跨越BuilderNode同步外界的数据和状态。
* 如果BuilderNode的子节点是自定义组件，不支持该自定义组件使用[@Reusable装饰器](../harmonyos-guides/arkts-reusable.md)，详细内容参见[BuilderNode在子自定义组件中使用@Reusable装饰器](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode在子自定义组件中使用reusable装饰器)。
* 从API version 12开始，自定义组件支持接收[LocalStorage](../harmonyos-guides/arkts-localstorage.md)实例。可以通过[传递LocalStorage实例](../harmonyos-guides/arkts-localstorage.md#自定义组件接收localstorage实例)来使用LocalStorage相关的装饰器[@LocalStorageProp](../harmonyos-guides/arkts-localstorage.md#localstorageprop)、[@LocalStorageLink](../harmonyos-guides/arkts-localstorage.md#localstoragelink)。
* 从API version 20开始，通过配置[BuildOptions](js-apis-arkui-buildernode.md#buildoptions12)，内部自定义组件的[@Consume](../harmonyos-guides/arkts-provide-and-consume.md)支持接收所在页面的[@Provide](../harmonyos-guides/arkts-provide-and-consume.md)数据。
* 其余装饰器行为未定义，不建议使用。
* 仅支持在自定义组件中使用[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)。
* BuilderNode对象不支持使用JSON序列化。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { BuilderNode, ReactiveBuilderNode, RenderOptions, NodeRenderType } from '@kit.ArkUI';
```

## NodeRenderType

PhonePC/2in1TabletTVWearable

节点渲染类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RENDER\_TYPE\_DISPLAY | 0 | 表示该节点将被显示到屏幕上。 |
| RENDER\_TYPE\_TEXTURE | 1 | 表示该节点将被导出为纹理。 |

说明

* RENDER\_TYPE\_TEXTURE类型目前仅在[BuilderNode](js-apis-arkui-buildernode.md#buildernode-1)持有组件树的根节点为自定义组件时以及[XComponentNode](js-apis-arkui-xcomponentnode.md)中设置生效。
* 在[BuilderNode](js-apis-arkui-buildernode.md#buildernode-1)的情况下，目前在作为根节点的自定义组件中支持纹理导出的有以下组件：[Badge](ts-container-badge.md)、[Blank](ts-basic-components-blank.md)、[Button](ts-basic-components-button.md)、[CanvasGradient](ts-components-canvas-canvasgradient.md)、[CanvasPattern](ts-components-canvas-canvaspattern.md)、[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)、[Canvas](ts-components-canvas-canvas.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Checkbox](ts-basic-components-checkbox.md)、[Circle](ts-drawing-components-circle.md)、[ColumnSplit](ts-container-columnsplit.md)、[Column](ts-container-column.md)、[ContainerSpan](ts-basic-components-containerspan.md)、[Counter](ts-container-counter.md)、[DataPanel](ts-basic-components-datapanel.md)、[Divider](ts-basic-components-divider.md)、[Ellipse](ts-drawing-components-ellipse.md)、[Flex](ts-container-flex.md)、[Gauge](ts-basic-components-gauge.md)、[Hyperlink](ts-container-hyperlink.md)、[ImageBitmap](ts-components-canvas-imagebitmap.md)、[ImageData](ts-components-canvas-imagedata.md)、[Image](ts-basic-components-image.md)、[Line](ts-drawing-components-line.md)、[LoadingProgress](ts-basic-components-loadingprogress.md)、[Marquee](ts-basic-components-marquee.md)、[Matrix2D](ts-components-canvas-matrix2d.md)、[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)、[OffscreenCanvas](ts-components-offscreencanvas.md)、[Path2D](ts-components-canvas-path2d.md)、[Path](ts-drawing-components-path.md)、[PatternLock](ts-basic-components-patternlock.md)、[Polygon](ts-drawing-components-polygon.md)、[Polyline](ts-drawing-components-polyline.md)、[Progress](ts-basic-components-progress.md)、[QRCode](ts-basic-components-qrcode.md)、[Radio](ts-basic-components-radio.md)、[Rating](ts-basic-components-rating.md)、[Rect](ts-drawing-components-rect.md)、[RelativeContainer](ts-container-relativecontainer.md)、[RowSplit](ts-container-rowsplit.md)、[Row](ts-container-row.md)、[Shape](ts-drawing-components-shape.md)、[Slider](ts-basic-components-slider.md)、[Span](ts-basic-components-span.md)、[Stack](ts-container-stack.md)、[TextArea](ts-basic-components-textarea.md)、[TextClock](ts-basic-components-textclock.md)、[TextInput](ts-basic-components-textinput.md)、[TextTimer](ts-basic-components-texttimer.md)、[Text](ts-basic-components-text.md)、[Toggle](ts-basic-components-toggle.md)、[Video](ts-media-components-video.md)（不含全屏播放能力）、[Web](arkts-basic-components-web.md)、[XComponent](ts-basic-components-xcomponent.md)。
* 从API version 12开始，新增以下组件支持纹理导出：[DatePicker](ts-basic-components-datepicker.md)、[ForEach](ts-rendering-control-foreach.md)、[Grid](ts-container-grid.md)、[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[LazyForEach](ts-rendering-control-lazyforeach.md)、[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)、[Swiper](ts-container-swiper.md)、[TimePicker](ts-basic-components-timepicker.md)、[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)修饰的自定义组件、[NodeContainer](ts-basic-components-nodecontainer.md)以及[NodeContainer](ts-basic-components-nodecontainer.md)下挂载的[FrameNode](js-apis-arkui-framenode.md)和[RenderNode](js-apis-arkui-rendernode.md)。
* 使用方式可参考[同层渲染绘制](../harmonyos-guides/web-same-layer.md)。

## RenderOptions

PhonePC/2in1TabletTVWearable

创建BuilderNode时的可选参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selfIdealSize | [Size](js-apis-arkui-graphics.md#size) | 否 | 是 | 节点的理想大小。  默认值：{ width: 0, height: 0 } |
| type | [NodeRenderType](js-apis-arkui-buildernode.md#noderendertype) | 否 | 是 | 节点的渲染类型。  默认值：NodeRenderType.RENDER\_TYPE\_DISPLAY |
| surfaceId | string | 否 | 是 | 纹理接收方的surfaceId。纹理接收方一般为[OH\_NativeImage](capi-oh-nativeimage-oh-nativeimage.md)。  surfaceId仅当type为NodeRenderType.RENDER\_TYPE\_TEXTURE时生效。  默认值："" |

## BuildOptions12+

PhonePC/2in1TabletTVWearable

build的可选参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nestingBuilderSupported | boolean | 否 | 是 | 是否支持Builder嵌套Builder进行使用。其中，true表示支持，false表示不支持。  默认值：false  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| localStorage20+ | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 否 | 是 | 给当前BuilderNode设置LocalStorage，挂载在此BuilderNode下的自定义组件共享该LocalStorage。如果自定义组件构造函数同时也传入LocalStorage，优先使用构造函数中传入的LocalStorage。  默认值：null  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| enableProvideConsumeCrossing20+ | boolean | 否 | 是 | 定义BuilderNode内[状态管理V1](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)自定义组件的[@Consume](../harmonyos-guides/arkts-provide-and-consume.md)变量是否与BuilderNode外部的[@Provide](../harmonyos-guides/arkts-provide-and-consume.md)变量双向同步，BuilderNode内[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)自定义组件的[@Consumer](../harmonyos-guides/arkts-new-provider-and-consumer.md)变量是否与BuilderNode外部的[@Provider](../harmonyos-guides/arkts-new-provider-and-consumer.md)变量双向同步。  从API version 20开始支持状态管理V1自定义组件的双向同步，从API version 22开始支持状态管理V2自定义组件的双向同步。  true表示支持，false表示不支持。  默认值：false  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## InputEventType20+

PhonePC/2in1TabletTVWearable

type InputEventType = TouchEvent | MouseEvent | AxisEvent

[postInputEvent](js-apis-arkui-buildernode.md#postinputevent20)的参数，定义要发送的输入事件类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 触摸事件。 |
| [MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明) | 鼠标事件。 |
| [AxisEvent](ts-universal-events-axis.md#axisevent) | 轴事件。 |

## BuilderNode

PhonePC/2in1TabletTVWearable

class BuilderNode<Args extends Object[]>

BuilderNode支持通过无状态的UI方法[@Builder](../harmonyos-guides/arkts-builder.md)生成组件树，并持有组件树的根节点。不支持定义为状态变量。BuilderNode中持有的FrameNode仅用于将该BuilderNode作为子节点挂载到其他FrameNode上。对BuilderNode持有的FrameNode进行属性设置与子节点操作可能会产生未定义行为，因此不建议通过BuilderNode的[getFrameNode](js-apis-arkui-buildernode.md#getframenode)方法和[FrameNode](js-apis-arkui-framenode.md)的[getRenderNode](js-apis-arkui-framenode.md#getrendernode)方法获取RenderNode，并通过[RenderNode](js-apis-arkui-rendernode.md)的接口对其进行属性设置与子节点操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, options?: RenderOptions)

当将BuilderNode生成的内容嵌入到其它RenderNode中显示时，需要显式指定RenderOptions中的selfIdealSize，否则Builder内的节点默认父组件布局约束为[0, 0]。该场景下，若不设置selfIdealSize则认为BuilderNode中子树的根节点大小为[0, 0]。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | UI上下文，获取方式可参考[UIContext获取方法](js-apis-arkui-node.md#uicontext获取方法)。 |
| options | [RenderOptions](js-apis-arkui-buildernode.md#renderoptions) | 否 | BuilderNode的构造可选参数。  默认值：undefined |

说明

uiContext的入参需要为一个有效的值，即UI上下文正确，如果传入非法值或者未设置，会导致创建失败。

### build

PhonePC/2in1TabletTVWearable

build(builder: WrappedBuilder<Args>, arg?: Object): void

依照传入的对象创建组件树，并持有组件树的根节点。无状态的UI方法[@Builder](../harmonyos-guides/arkts-builder.md)最多拥有一个根节点。

支持自定义组件。

说明

* @Builder嵌套使用的时候需要保证内外的@Builder方法的入参对象一致。
* 最外层的@Builder只支持一个入参。
* build的参数是值传递，需要使用[update](js-apis-arkui-buildernode.md#update)接口进行更新。
* 需要操作BuilderNode中的对象时，需要保证其引用不被回收。当BuilderNode对象被虚拟机回收之后，它的[FrameNode](js-apis-arkui-framenode.md)、[RenderNode](js-apis-arkui-rendernode.md)对象也会与后端节点解引用。即从BuilderNode中获取的FrameNode对象不对应任何一个节点。
* BuilderNode对象会持有实体节点的引用。如果不需要使用BuilderNode前端对象管理后端节点，可以调用[dispose](js-apis-arkui-buildernode.md#dispose12)接口，实现前后端对象的解绑。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [WrappedBuilder<Args>](../harmonyos-guides/arkts-wrapbuilder.md) | 是 | 创建对应节点树的时候所需的无状态UI方法[@Builder](../harmonyos-guides/arkts-builder.md)。 |
| arg | Object | 否 | builder的入参。当前仅支持一个入参，且入参对象类型与@Builder定义的入参类型保持一致。  默认值：undefined |

### build12+

PhonePC/2in1TabletTVWearable

build(builder: WrappedBuilder<Args>, arg: Object, options: BuildOptions): void

依照传入的对象创建组件树，并持有组件树的根节点。无状态的UI方法[@Builder](../harmonyos-guides/arkts-builder.md)最多拥有一个根节点。

支持自定义组件。相比[build(builder: WrappedBuilder<Args>, arg?: Object)](js-apis-arkui-buildernode.md#build)接口，本接口支持builder的配置参数，用于判断是否支持@Builder中嵌套@Builder。

说明

* @Builder进行创建和更新的规格参考[@Builder](../harmonyos-guides/arkts-builder.md)。
* 最外层的@Builder只支持一个入参。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [WrappedBuilder<Args>](../harmonyos-guides/arkts-wrapbuilder.md) | 是 | 创建对应节点树的时候所需的无状态UI方法[@Builder](../harmonyos-guides/arkts-builder.md)。 |
| arg | Object | 是 | builder的入参。当前仅支持一个入参，且入参对象类型与@Builder定义的入参类型保持一致。 |
| options | [BuildOptions](js-apis-arkui-buildernode.md#buildoptions12) | 是 | builder的配置参数，判断是否支持@Builder中嵌套@Builder的行为。 |

**示例：**

```
1. import { BuilderNode, NodeContent } from "@kit.ArkUI";

3. // 定义传递参数的接口
4. interface ParamsInterface {
5. text: string;
6. func: Function;
7. }

9. @Builder
10. function buildTextWithFunc(fun: Function) {
11. Text(fun())
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .margin({ bottom: 36 })
15. }

17. @Builder
18. function buildText(params: ParamsInterface) {
19. Column() {
20. Text(params.text)
21. .fontSize(50)
22. .fontWeight(FontWeight.Bold)
23. .margin({ bottom: 36 })
24. buildTextWithFunc(params.func)
25. }
26. }

29. @Entry
30. @Component
31. struct Index {
32. @State message: string = "HELLO";
33. private content: NodeContent = new NodeContent();

35. build() {
36. Row() {
37. Column() {
38. Button('addBuilderNode')
39. .onClick(() => {
40. let buildNode = new BuilderNode<[ParamsInterface]>(this.getUIContext());
41. // 创建节点树
42. buildNode.build(wrapBuilder<[ParamsInterface]>(buildText), {
43. text: this.message, func: () => {
44. return "FUNCTION";
45. }
46. }, { nestingBuilderSupported: true });
47. this.content.addFrameNode(buildNode.getFrameNode());
48. buildNode.dispose();
49. })
50. ContentSlot(this.content)
51. }
52. .id("column")
53. .width('100%')
54. .height('100%')
55. }
56. .height('100%')
57. }
58. }
```

### getFrameNode

PhonePC/2in1TabletTVWearable

getFrameNode(): FrameNode | null

获取BuilderNode中的[FrameNode](js-apis-arkui-framenode.md)。在BuilderNode执行build操作之后，才会生成FrameNode。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md) | null | 一个FrameNode对象。若该BuilderNode不包含FrameNode，则返回空对象null。 |

**示例1：**

BuilderNode作为[NodeContainer](ts-basic-components-nodecontainer.md)的根节点返回。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from "@kit.ArkUI";

3. // 定义传递参数的类
4. class Params {
5. text: string = "";
6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column() {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({bottom: 36})
18. }
19. }

21. // 继承NodeController实现自定义textNode控制器
22. class TextNodeController extends NodeController {
23. private textNode: BuilderNode<[Params]> | null = null;
24. private message: string = "DEFAULT";

26. constructor(message: string) {
27. super();
28. this.message = message;
29. }

31. makeNode(context: UIContext): FrameNode | null {
32. this.textNode = new BuilderNode(context);
33. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
34. // 返回当前BuilderNode包含的FrameNode
35. return this.textNode.getFrameNode();
36. }
37. }

39. @Entry
40. @Component
41. struct Index {
42. @State message: string = "hello";

44. build() {
45. Row() {
46. Column() {
47. NodeContainer(new TextNodeController(this.message))
48. .width('100%')
49. .height(100)
50. .backgroundColor('#FFF0F0F0')
51. }
52. .width('100%')
53. .height('100%')
54. }
55. .height('100%')
56. }
57. }
```

**示例2：**

BuilderNode的[FrameNode](js-apis-arkui-framenode.md)挂到其它FrameNode下。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from "@kit.ArkUI";

3. // 定义传递参数的类
4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 36 })
19. }
20. }

22. // 继承NodeController实现自定义textNode控制器
23. class TextNodeController extends NodeController {
24. private rootNode: FrameNode | null = null;
25. private textNode: BuilderNode<[Params]> | null = null;
26. private message: string = "DEFAULT";

28. constructor(message: string) {
29. super();
30. this.message = message;
31. }

33. makeNode(context: UIContext): FrameNode | null {
34. this.rootNode = new FrameNode(context);
35. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
36. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
37. if (this.rootNode !== null) {
38. // 将BuilderNode的FrameNode挂至其他FrameNode
39. this.rootNode.appendChild(this.textNode?.getFrameNode());
40. }

42. return this.rootNode;
43. }
44. }

46. @Entry
47. @Component
48. struct Index {
49. @State message: string = "hello";

51. build() {
52. Row() {
53. Column() {
54. NodeContainer(new TextNodeController(this.message))
55. .width('100%')
56. .height(100)
57. .backgroundColor('#FFF0F0F0')
58. }
59. .width('100%')
60. .height('100%')
61. }
62. .height('100%')
63. }
64. }
```

**示例3：**

BuilderNode的[RenderNode](js-apis-arkui-rendernode.md)挂到其它RenderNode下。由于RenderNode不传递布局约束，不推荐通过该方式挂载节点。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext, RenderNode } from "@kit.ArkUI";
2. // 自定义传递参数的类
3. class Params {
4. text: string = "";

6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column() {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 36 })
18. }
19. }

21. // 继承NodeController实现自定义textNode控制器
22. class TextNodeController extends NodeController {
23. private rootNode: FrameNode | null = null;
24. private textNode: BuilderNode<[Params]> | null = null;
25. private message: string = "DEFAULT";

27. constructor(message: string) {
28. super();
29. this.message = message;
30. }

32. makeNode(context: UIContext): FrameNode | null {
33. this.rootNode = new FrameNode(context);
34. let renderNode = new RenderNode();
35. renderNode.clipToFrame = false;
36. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
37. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
38. const textRenderNode = this.textNode?.getFrameNode()?.getRenderNode();

40. const rootRenderNode = this.rootNode.getRenderNode();
41. if (rootRenderNode !== null) {
42. rootRenderNode.appendChild(renderNode);
43. // 将BuilderNode的RenderNode挂至其他RenderNode
44. renderNode.appendChild(textRenderNode);
45. }

47. return this.rootNode;
48. }
49. }

51. @Entry
52. @Component
53. struct Index {
54. @State message: string = "hello";

56. build() {
57. Row() {
58. Column() {
59. NodeContainer(new TextNodeController(this.message))
60. .width('100%')
61. .height(100)
62. .backgroundColor('#FFF0F0F0')
63. }
64. .width('100%')
65. .height('100%')
66. }
67. .height('100%')
68. }
69. }
```

### update

PhonePC/2in1TabletTVWearable

update(arg: Object): void

根据提供的参数更新BuilderNode，该参数与[build](js-apis-arkui-buildernode.md#build)方法调用时传入的参数类型相同。对自定义组件进行update的时候需要在自定义组件中将使用的变量定义为[@Prop](../harmonyos-guides/arkts-prop.md)类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arg | Object | 是 | 用于更新BuilderNode的参数，和[build](js-apis-arkui-buildernode.md#build)调用时传入的参数类型一致。 |

**示例：**

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from "@kit.ArkUI";

3. // 自定义传递参数的类
4. class Params {
5. text: string = "";
6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. // 自定义组件
12. @Component
13. struct TextBuilder {
14. @Prop message: string = "TextBuilder";

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. .margin({bottom: 36})
23. .backgroundColor(Color.Gray)
24. }
25. }
26. }
27. }

29. @Builder
30. function buildText(params: Params) {
31. Column() {
32. Text(params.text)
33. .fontSize(50)
34. .fontWeight(FontWeight.Bold)
35. .margin({ bottom: 36 })
36. TextBuilder({message: params.text}) // 自定义组件
37. }
38. }

40. // 继承NodeController实现自定义textNode控制器
41. class TextNodeController extends NodeController {
42. private rootNode: FrameNode | null = null;
43. private textNode: BuilderNode<[Params]> | null = null;
44. private message: string = "";

46. constructor(message: string) {
47. super();
48. this.message = message;
49. }

51. makeNode(context: UIContext): FrameNode | null {
52. this.textNode = new BuilderNode(context);
53. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
54. return this.textNode.getFrameNode();
55. }

57. // 根据传入参数更新BuilderNode
58. update(message: string) {
59. if (this.textNode !== null) {
60. this.textNode.update(new Params(message));
61. }
62. }
63. }

65. @Entry
66. @Component
67. struct Index {
68. @State message: string = "hello";
69. private textNodeController: TextNodeController = new TextNodeController(this.message);
70. private count = 0;

72. build() {
73. Row() {
74. Column() {
75. NodeContainer(this.textNodeController)
76. .width('100%')
77. .height(200)
78. .backgroundColor('#FFF0F0F0')
79. Button('Update')
80. .onClick(() => {
81. this.count += 1;
82. const message = "Update " + this.count.toString();
83. this.textNodeController.update(message);
84. })
85. }
86. .width('100%')
87. .height('100%')
88. }
89. .height('100%')
90. }
91. }
```

### postTouchEvent

PhonePC/2in1TabletTVWearable

postTouchEvent(event: TouchEvent): boolean

将原始事件派发到某个BuilderNode创建出的FrameNode上。

postTouchEvent是从组件树的中间节点往下分发，需要变换到父组件坐标系才能分发成功，参考下图。

OffsetA为buildNode相对于父组件的偏移量，可以通过FrameNode中的[getPositionToParent](js-apis-arkui-framenode.md#getpositiontoparent12)获取。OffsetB为point点相对于buildNode的偏移量，可以通过[TouchEvent](ts-universal-events-touch.md#touchevent对象说明) 获取。OffsetC为OffsetA与OffsetB的和，是传给postTouchEvent的最终结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/2ozvvGfrToWuULXwQLMd9g/zh-cn_image_0000002583439475.png?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=3353E67FF0071E87FB0B91AC665D5D62E7330C9C6FD0CD5AD215CFA1F37FA71B)

说明

* 传入的坐标值需要转换为px，如果builderNode有仿射变换，则需要再叠加仿射变换。
* 在[webview](arkts-apis-webview.md)中，内部已经处理过坐标系变换，可以将TouchEvent事件直接下发。
* 同一时间戳，postTouchEvent只能调用一次。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 触摸事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 派发事件是否成功。true为已命中响应事件的组件，false为未命中任何可响应事件的组件。  **说明：**  如果未按照预期命中组件，需要确认以下几点：  1.坐标系是否转换正确。  2.组件是否可交互状态。  3.是否绑定事件。 |

**示例：**

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. // 自定义传递参数的类
4. class Params {
5. text: string = "this is a text";
6. }

8. @Builder
9. function ButtonBuilder(params: Params) {
10. Column() {
11. Button(`button ` + params.text)
12. .borderWidth(2)
13. .backgroundColor(Color.Orange)
14. .width("100%")
15. .height("100%")
16. .gesture(
17. TapGesture()
18. .onAction((event: GestureEvent) => {
19. console.info("TapGesture");
20. })
21. )
22. }
23. .width(500)
24. .height(300)
25. .backgroundColor(Color.Gray)
26. }

28. // 继承NodeController实现自定义UI控制器
29. class MyNodeController extends NodeController {
30. private rootNode: BuilderNode<[Params]> | null = null;
31. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ButtonBuilder);

33. makeNode(uiContext: UIContext): FrameNode | null {
34. this.rootNode = new BuilderNode(uiContext);
35. this.rootNode.build(this.wrapBuilder, { text: "this is a string" });
36. return this.rootNode.getFrameNode();
37. }

39. // 坐标转换示例
40. postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
41. if (this.rootNode == null) {
42. return false;
43. }
44. let node: FrameNode | null = this.rootNode.getFrameNode();
45. let offsetX: number | null | undefined = node?.getPositionToParent().x;
46. let offsetY: number | null | undefined = node?.getPositionToParent().y;

48. let changedTouchLen = event.changedTouches.length;
49. for (let i = 0; i < changedTouchLen; i++) {
50. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
51. event.changedTouches[i].x = uiContext.vp2px(offsetX + event.changedTouches[i].x);
52. event.changedTouches[i].y = uiContext.vp2px(offsetY + event.changedTouches[i].y);
53. }
54. }
55. // 将事件派发至BuilderNode创建的FrameNode上，result记录派发是否成功
56. let result = this.rootNode.postTouchEvent(event);
57. console.info(`result ${result}`);
58. return result;
59. }
60. }

62. @Entry
63. @Component
64. struct MyComponent {
65. private nodeController: MyNodeController = new MyNodeController();

67. build() {
68. Column() {
69. NodeContainer(this.nodeController)
70. .height(300)
71. .width(500)

73. Column()
74. .width(500)
75. .height(300)
76. .backgroundColor(Color.Pink)
77. .onTouch((event) => {
78. if (event != undefined) {
79. this.nodeController.postTouchEvent(event, this.getUIContext());
80. }
81. })
82. }
83. }
84. }
```

### dispose12+

PhonePC/2in1TabletTVWearable

dispose(): void

立即释放当前BuilderNode对象对[实体节点](../harmonyos-guides/arkts-user-defined-node.md#基本概念)的引用关系。关于BuilderNode的解绑场景请参见[节点解绑](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

说明

当BuilderNode对象调用dispose之后，会与后端实体节点解除引用关系。若前端对象BuilderNode无法释放，容易导致内存泄漏。建议在不再需要对该BuilderNode对象进行操作时，开发者主动调用dispose释放后端节点，以减少引用关系的复杂性，降低内存泄漏的风险。具体场景可见[BuilderNode前后端循环引用导致的内存泄漏问题](../harmonyos-guides/arkts-user-defined-node-faq.md#buildernode前后端循环引用导致的内存泄漏问题)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

```
1. import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

3. // 自定义组件
4. @Component
5. struct TestComponent {
6. build() {
7. Column() {
8. Text('This is a BuilderNode.')
9. .fontSize(16)
10. .fontWeight(FontWeight.Bold)
11. }
12. .width('100%')
13. .backgroundColor(Color.Gray)
14. }

16. aboutToAppear() {
17. console.info('aboutToAppear');
18. }

20. aboutToDisappear() {
21. console.info('aboutToDisappear');
22. }
23. }

25. @Builder
26. function buildComponent() {
27. TestComponent()
28. }

30. // 继承NodeController实现自定义UI控制器
31. class MyNodeController extends NodeController {
32. private rootNode: FrameNode | null = null;
33. private builderNode: BuilderNode<[]> | null = null;

35. makeNode(uiContext: UIContext): FrameNode | null {
36. this.rootNode = new FrameNode(uiContext);
37. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
38. this.builderNode.build(new WrappedBuilder(buildComponent));

40. const rootRenderNode = this.rootNode!.getRenderNode();
41. if (rootRenderNode !== null) {
42. rootRenderNode.size = { width: 200, height: 200 };
43. rootRenderNode.backgroundColor = 0xff00ff00;
44. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
45. }

47. return this.rootNode;
48. }

50. // 解除当前builderNode与后端实体的引用关系
51. dispose() {
52. if (this.builderNode !== null) {
53. this.builderNode.dispose();
54. }
55. }

57. removeBuilderNode() {
58. const rootRenderNode = this.rootNode!.getRenderNode();
59. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
60. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
61. }
62. }
63. }

65. @Entry
66. @Component
67. struct Index {
68. private myNodeController: MyNodeController = new MyNodeController();

70. build() {
71. Column({ space: 4 }) {
72. NodeContainer(this.myNodeController)
73. Button('BuilderNode dispose')
74. .onClick(() => {
75. this.myNodeController.removeBuilderNode();
76. this.myNodeController.dispose();
77. })
78. .width('100%')
79. }
80. }
81. }
```

### reuse12+

PhonePC/2in1TabletTVWearable

reuse(param?: Object): void

触发BuilderNode中的自定义组件的复用。组件复用请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。关于BuilderNode的解绑场景请参见[节点解绑](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | Object | 否 | 用于复用BuilderNode的参数。该参数将直接用于BuilderNode中所有顶层自定义组件的复用，应该包含每个自定义组件的构造函数参数所需内容，否则，会导致未定义行为。调用此方法将同步触发内部自定义组件的[aboutToReuse](ts-custom-component-lifecycle.md#abouttoreuse10)生命周期回调，并将该参数作为回调的入参。默认值为undefined，此时BuilderNode中的自定义组件将直接使用构造时的数据源。 |

### recycle12+

PhonePC/2in1TabletTVWearable

recycle(): void

触发BuilderNode中自定义组件的回收。自定义组件的回收是组件复用机制中的环节，具体信息请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。

说明

BuilderNode通过reuse和recycle完成其内外自定义组件之间的复用事件传递，具体使用场景请参见[BuilderNode调用reuse和recycle接口实现节点复用能力](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

```
1. import { FrameNode, NodeController, BuilderNode, UIContext } from "@kit.ArkUI";

3. const TEST_TAG: string = "Reuse+Recycle";

5. // 自定义管理数据的类
6. class MyDataSource {
7. private dataArray: string[] = [];
8. private listener: DataChangeListener | null = null;

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number) {
15. return this.dataArray[index];
16. }

18. public pushData(data: string) {
19. this.dataArray.push(data);
20. }

22. public reloadListener(): void {
23. this.listener?.onDataReloaded();
24. }

26. public registerDataChangeListener(listener: DataChangeListener): void {
27. this.listener = listener;
28. }

30. public unregisterDataChangeListener(): void {
31. this.listener = null;
32. }
33. }

35. // 自定义传递参数的类
36. class Params {
37. item: string = '';

39. constructor(item: string) {
40. this.item = item;
41. }
42. }

44. @Builder
45. function buildNode(param: Params = new Params("hello")) {
46. Row() {
47. Text(`C${param.item} -- `)
48. ReusableChildComponent2({ item: param.item }) // 该自定义组件在BuilderNode中无法被正确复用
49. }
50. }

52. // 继承NodeController实现自定义UI控制器
53. class MyNodeController extends NodeController {
54. public builderNode: BuilderNode<[Params]> | null = null;
55. public item: string = "";

57. makeNode(uiContext: UIContext): FrameNode | null {
58. if (this.builderNode == null) {
59. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 300, height: 200 } });
60. this.builderNode.build(wrapBuilder<[Params]>(buildNode), new Params(this.item));
61. }
62. return this.builderNode.getFrameNode();
63. }
64. }

66. // 被回收复用的自定义组件，其状态变量会更新，而子自定义组件ReusableChildComponent3中的状态变量也会更新，但BuilderNode会阻断这一传递过程
67. @Reusable
68. @Component
69. struct ReusableChildComponent {
70. @Prop item: string = '';
71. @Prop switch: string = '';
72. private controller: MyNodeController = new MyNodeController();

74. aboutToAppear() {
75. this.controller.item = this.item;
76. }

78. aboutToRecycle(): void {
79. console.info(`${TEST_TAG} ReusableChildComponent aboutToRecycle ${this.item}`);

81. // 当开关为open，通过BuilderNode的reuse接口和recycle接口传递给其下的自定义组件，例如ReusableChildComponent2，完成复用
82. if (this.switch === 'open') {
83. this.controller?.builderNode?.recycle();
84. }
85. }

87. aboutToReuse(params: object): void {
88. console.info(`${TEST_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}`);

90. // 当开关为open，通过BuilderNode的reuse接口和recycle接口传递给其下的自定义组件，例如ReusableChildComponent2，完成复用
91. if (this.switch === 'open') {
92. this.controller?.builderNode?.reuse(params);
93. }
94. }

96. build() {
97. Row() {
98. Text(`A${this.item}--`)
99. ReusableChildComponent3({ item: this.item })
100. NodeContainer(this.controller);
101. }
102. }
103. }

105. // 自定义组件
106. @Component
107. struct ReusableChildComponent2 {
108. @Prop item: string = "false";

110. aboutToReuse(params: Record<string, object>) {
111. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToReuse ${JSON.stringify(params)}`);
112. }

114. aboutToRecycle(): void {
115. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToRecycle ${this.item}`);
116. }

118. build() {
119. Row() {
120. Text(`D${this.item}`)
121. .fontSize(20)
122. .backgroundColor(Color.Yellow)
123. .margin({ left: 10 })
124. }.margin({ left: 10, right: 10 })
125. }
126. }

128. @Component
129. struct ReusableChildComponent3 {
130. @Prop item: string = "false";

132. aboutToReuse(params: Record<string, object>) {
133. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToReuse ${JSON.stringify(params)}`);
134. }

136. aboutToRecycle(): void {
137. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToRecycle ${this.item}`);
138. }

140. build() {
141. Row() {
142. Text(`B${this.item}`)
143. .fontSize(20)
144. .backgroundColor(Color.Yellow)
145. .margin({ left: 10 })
146. }.margin({ left: 10, right: 10 })
147. }
148. }

151. @Entry
152. @Component
153. struct Index {
154. @State data: MyDataSource = new MyDataSource();

156. aboutToAppear() {
157. for (let i = 0; i < 100; i++) {
158. this.data.pushData(i.toString());
159. }
160. }

162. build() {
163. Column() {
164. List({ space: 3 }) {
165. LazyForEach(this.data, (item: string) => {
166. ListItem() {
167. ReusableChildComponent({
168. item: item,
169. switch: 'open' // 将open改为close可观察到，BuilderNode不通过reuse和recycle接口传递复用时，BuilderNode内部的自定义组件的行为表现
170. })
171. }
172. }, (item: string) => item)
173. }
174. .width('100%')
175. .height('100%')
176. }
177. }
178. }
```

### updateConfiguration12+

PhonePC/2in1TabletTVWearable

updateConfiguration(): void

传递[系统环境变化](js-apis-app-ability-configuration.md)事件，触发节点的全量更新。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

updateConfiguration接口用于通知对象更新，更新所使用的系统环境由应用当前的系统环境变化决定。

**示例：**

```
1. import { NodeController, BuilderNode, FrameNode, UIContext, FrameCallback } from "@kit.ArkUI";
2. import { AbilityConstant, Configuration, ConfigurationConstant, EnvironmentCallback } from '@kit.AbilityKit';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. // 自定义组件
13. @Component
14. struct TextBuilder {
15. // 作为自定义组件中需要更新的属性，数据类型为基础属性，定义为@Prop
16. @Prop message: string = "TextBuilder";

18. build() {
19. Row() {
20. Column() {
21. Text(this.message)
22. .fontSize(50)
23. .fontWeight(FontWeight.Bold)
24. .margin({ bottom: 36 })
25. }
26. }
27. }
28. }

30. @Builder
31. function buildText(params: Params) {
32. Column() {
33. Text(params.text)
34. .fontSize(50)
35. .fontWeight(FontWeight.Bold)
36. .margin({ bottom: 36 })
37. TextBuilder({ message: params.text }) // 自定义组件
38. }.backgroundColor($r('sys.color.ohos_id_color_background'))
39. }

41. // 继承NodeController实现自定义textNode控制器
42. class TextNodeController extends NodeController {
43. private textNode: BuilderNode<[Params]> | null = null;
44. private message: string = "";

46. constructor(message: string) {
47. super();
48. this.message = message;
49. }

51. makeNode(context: UIContext): FrameNode | null {
52. return this.textNode?.getFrameNode() ? this.textNode?.getFrameNode() : null;
53. }

55. createNode(context: UIContext) {
56. this.textNode = new BuilderNode(context);
57. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
58. builderNodeMap.push(this.textNode);
59. }

61. deleteNode() {
62. let node = builderNodeMap.pop();
63. node?.dispose();
64. }

66. update(message: string) {
67. if (this.textNode !== null) {
68. // 调用update进行更新
69. this.textNode.update(new Params(message));
70. }
71. }
72. }

74. // 记录创建的自定义节点对象
75. const builderNodeMap: Array<BuilderNode<[Params]>> = new Array();

77. class MyFrameCallback extends FrameCallback {
78. onFrame() {
79. updateColorMode();
80. }
81. }

83. function updateColorMode() {
84. builderNodeMap.forEach((value, index) => {
85. // 通知BuilderNode环境变量改变，触发深浅色切换
86. value.updateConfiguration();
87. })
88. }

90. @Entry
91. @Component
92. struct Index {
93. @State message: string = "hello";
94. private textNodeController: TextNodeController = new TextNodeController(this.message);
95. private count = 0;

97. aboutToAppear(): void {
98. let environmentCallback: EnvironmentCallback = {
99. onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
100. console.info('onMemoryLevel');
101. },
102. onConfigurationUpdated: (config: Configuration): void => {
103. console.info(`onConfigurationUpdated ${JSON.stringify(config)}`);
104. this.getUIContext()?.postFrameCallback(new MyFrameCallback());
105. }
106. };
107. // 注册监听回调
108. this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
109. // 设置应用深浅色跟随系统
110. this.getUIContext()
111. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
112. // 创建自定义节点并添加至builderNodeMap
113. this.textNodeController.createNode(this.getUIContext());
114. }

116. aboutToDisappear(): void {
117. // 移除map中的引用，并将自定义节点释放
118. this.textNodeController.deleteNode();
119. }

121. build() {
122. Row() {
123. Column() {
124. NodeContainer(this.textNodeController)
125. .width('100%')
126. .height(200)
127. .backgroundColor('#FFF0F0F0')
128. Button('Update')
129. .onClick(() => {
130. this.count += 1;
131. const message = "Update " + this.count.toString();
132. this.textNodeController.update(message);
133. })
134. Button('切换深色')
135. .onClick(() => {
136. this.getUIContext()
137. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
138. })
139. Button('设置浅色')
140. .onClick(() => {
141. this.getUIContext()
142. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
143. })
144. }
145. .width('100%')
146. .height('100%')
147. }
148. .height('100%')
149. }
150. }
```

### isDisposed20+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前BuilderNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

该示例演示了BuilderNode释放节点前后分别使用[isDisposed](js-apis-arkui-buildernode.md#isdisposed20)接口验证节点的状态，释放节点前节点调用isDisposed接口返回true，释放节点后节点调用isDisposed接口返回false。

```
1. import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';

3. // 自定义组件
4. @Component
5. struct TestComponent {
6. build() {
7. Column() {
8. Text('This is a BuilderNode.')
9. .fontSize(25)
10. .fontWeight(FontWeight.Bold)
11. }
12. .width('100%')
13. .height(30)
14. .backgroundColor(Color.Gray)
15. }

17. aboutToAppear() {
18. console.info('aboutToAppear');
19. }

21. aboutToDisappear() {
22. console.info('aboutToDisappear');
23. }
24. }

26. @Builder
27. function buildComponent() {
28. TestComponent()
29. }

31. // 继承NodeController实现自定义UI控制器
32. class MyNodeController extends NodeController {
33. private rootNode: FrameNode | null = null;
34. private builderNode: BuilderNode<[]> | null = null;

36. makeNode(uiContext: UIContext): FrameNode | null {
37. this.rootNode = new FrameNode(uiContext);
38. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
39. this.builderNode.build(new WrappedBuilder(buildComponent));

41. const rootRenderNode = this.rootNode!.getRenderNode();
42. if (rootRenderNode !== null) {
43. rootRenderNode.size = { width: 300, height: 300 };
44. rootRenderNode.backgroundColor = 0xffd5d5d5;
45. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
46. }

48. return this.rootNode;
49. }

51. // 释放当前builderNode
52. dispose() {
53. if (this.builderNode !== null) {
54. this.builderNode.dispose();
55. }
56. }

58. // 检验当前builderNode是否已被释放
59. isDisposed(): string {
60. if (this.builderNode !== null) {
61. if (this.builderNode.isDisposed()) {
62. return 'builderNode isDisposed is true';
63. } else {
64. return 'builderNode isDisposed is false';
65. }
66. }
67. return 'builderNode is null';
68. }

70. removeBuilderNode() {
71. const rootRenderNode = this.rootNode!.getRenderNode();
72. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
73. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
74. }
75. }
76. }

78. @Entry
79. @Component
80. struct Index {
81. @State text: string = ''
82. private myNodeController: MyNodeController = new MyNodeController();

84. build() {
85. Column({ space: 4 }) {
86. NodeContainer(this.myNodeController)
87. Button('BuilderNode dispose')
88. .onClick(() => {
89. this.myNodeController.removeBuilderNode();
90. this.myNodeController.dispose();
91. this.text = '';
92. })
93. .width(200)
94. .height(50)
95. Button('BuilderNode isDisposed')
96. .onClick(() => {
97. this.text = this.myNodeController.isDisposed();
98. })
99. .width(200)
100. .height(50)
101. Text(this.text)
102. .fontSize(25)
103. }
104. .width('100%')
105. .height('100%')
106. }
107. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/n0nLx1Y9QKic0uROLKxW4Q/zh-cn_image_0000002552959430.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=6C0639F29E93327BCE68A9213FA4CFA806DA5148FAB09C71C41DAE4903B95BB2)

### postInputEvent20+

PhonePC/2in1TabletTVWearable

postInputEvent(event: InputEventType): boolean

将事件分发到目标节点。

offsetA为builderNode相对于父组件的偏移，offsetB为命中位置相对于builderNode的偏移，offsetC为offsetA+offsetB，最终输入给postInputEvent中的window信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/YcEwEIviQU20WNK8tbr_Wg/zh-cn_image_0000002583479431.png?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=DA5417D3A5FF74607CE8C8FAC30B755448FBEE95F202CFDD826D233022FCAB91)

说明

* 传入的坐标值需要转换为px，坐标转换示例可以参考下面示例代码。
* 鼠标左键点击事件将转换为触摸事件，转发时应注意不在外层同时绑定触摸事件与鼠标事件，否则可能导致坐标偏移。这是由于在事件转换过程中，SourceType不会发生变化，规格可查看[onTouch](ts-universal-events-touch.md#ontouch)。
* 注入事件为[轴事件](ts-universal-events-axis.md#axisevent)时，由于轴事件中缺少旋转轴信息，因此注入的事件无法触发[rotate旋转手势](ts-basic-gestures-rotationgesture.md)。
* 转发的事件会在被分发到的目标组件所在的子树里做touchtest，并触发对应手势，原始事件也会触发当前组件所在组件树中的手势。不保证两类手势的竞争结果。
* 如果是开发者构造的事件，必填字段必须赋值，比如触摸事件的touches字段，轴事件的scrollStep字段。要保证事件的完整，比如触摸事件的[TouchType](ts-appendix-enums.md#touchtype)中DOWN和UP字段都要有，防止出现未定义行为。
* [webview](arkts-apis-webview.md)已经处理过坐标系变换，可以将事件直接下发。
* postTouchEvent接口需要提供手势坐标相对于post事件对端内的局部坐标，postInputEvent接口需要提供手势坐标相对于post事件对端内的窗口坐标。
* 不建议同一个事件转发多次。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InputEventType](js-apis-arkui-buildernode.md#inputeventtype20) | 是 | 用于透传的输入事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 事件是否被成功派发。如果事件派发成功，则返回true；否则，返回false。 |

**示例：**

请参考[示例1（BuilderNode中鼠标事件）](js-apis-arkui-buildernode.md#示例1buildernode中鼠标事件)、[示例2（BuilderNode中触摸事件）](js-apis-arkui-buildernode.md#示例2buildernode中触摸事件)、[示例3（BuilderNode中轴事件）](js-apis-arkui-buildernode.md#示例3buildernode中轴事件)。

### inheritFreezeOptions20+

PhonePC/2in1TabletTVWearable

inheritFreezeOptions(enabled: boolean): void

查询当前BuilderNode对象是否设置为继承父组件中自定义组件的冻结策略。如果设置继承状态为false，则BuilderNode对象的冻结策略为false。在这种情况下，节点在不活跃状态下不会被冻结。

说明

BuilderNode设置inheritFreezeOptions为true，且父组件为自定义组件、BuilderNode、ComponentContent、ReactiveBuilderNode或ReactiveComponentContent时，会继承父组件的冻结策略。当子组件为自定义组件时，其冻结策略不会传递给子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | BuilderNode对象是否设置为继承父组件中自定义组件的冻结策略。true为继承父组件中自定义组件的冻结策略，false为不继承父组件中自定义组件的冻结策略。 |

**示例：**

该示例演示了BuilderNode设置继承状态为True，继承父自定义组件的冻结策略，在不活跃的时候进行冻结，切换为活跃状态解冻，更新缓存的数据。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. // 自定义传递参数的类
4. class Params {
5. count: number = 0;

7. constructor(count: number) {
8. this.count = count;
9. }
10. }

12. @Builder
13. // builder组件
14. function buildText(params: Params) {

16. Column() {
17. TextBuilder({ message: params.count })
18. }
19. }

21. // 继承NodeController实现自定义textNode控制器
22. class TextNodeController extends NodeController {
23. private rootNode: FrameNode | null = null;
24. private textNode: BuilderNode<[Params]> | null = null;
25. private count: number = 0;

27. makeNode(context: UIContext): FrameNode | null {
28. this.rootNode = new FrameNode(context);
29. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
30. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.count)); // 创建BuilderNode节点
31. this.textNode.inheritFreezeOptions(true); // 设置BuilderNode的冻结继承状态为true
32. if (this.rootNode !== null) {
33. this.rootNode.appendChild(this.textNode.getFrameNode()); // 将BuilderNode上树
34. }
35. return this.rootNode;
36. }

38. update(): void {
39. if (this.textNode !== null) {
40. this.count += 1;
41. this.textNode.update(new Params(this.count)); // 更新BuilderNode中的数据，可以触发Log
42. }

44. }
45. }

47. const textNodeController: TextNodeController = new TextNodeController();

49. @Entry
50. @Component
51. struct MyNavigationTestStack {
52. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
53. @State message: number = 0;
54. @State logNumber: number = 0;

56. @Builder
57. PageMap(name: string) {
58. if (name === 'pageOne') {
59. pageOneStack({ message: this.message, logNumber: this.logNumber })
60. } else if (name === 'pageTwo') {
61. pageTwoStack({ message: this.message, logNumber: this.logNumber })
62. }
63. }

65. build() {
66. Column() {
67. Button('update builderNode') // 点击更新BuildrNode
68. .onClick(() => {
69. textNodeController.update();
70. })
71. Navigation(this.pageInfo) {
72. Column() {
73. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
74. .width('80%')
75. .height(40)
76. .margin(20)
77. .onClick(() => {
78. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
79. })
80. }
81. }.title('NavIndex')
82. .navDestination(this.PageMap)
83. .mode(NavigationMode.Stack)
84. }
85. }
86. }

88. @Component
89. struct pageOneStack { // 页面一
90. @Consume('pageInfo') pageInfo: NavPathStack;
91. @State index: number = 1;
92. @Link message: number;
93. @Link logNumber: number;

95. build() {
96. NavDestination() {
97. Column() {
98. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
99. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule }) // 切换至页面二
100. .width('80%')
101. .height(40)
102. .margin(20)
103. .onClick(() => {
104. this.pageInfo.pushPathByName('pageTwo', null);
105. })
106. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // 返回主页面
107. .width('80%')
108. .height(40)
109. .margin(20)
110. .onClick(() => {
111. this.pageInfo.pop();
112. })
113. }.width('100%').height('100%')
114. }.title('pageOne')
115. .onBackPressed(() => {
116. this.pageInfo.pop();
117. return true;
118. })
119. }
120. }

122. @Component
123. struct pageTwoStack { // 页面二
124. @Consume('pageInfo') pageInfo: NavPathStack;
125. @State index: number = 2;
126. @Link message: number;
127. @Link logNumber: number;

129. build() {
130. NavDestination() {
131. Column() {
132. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
133. Text('BuilderNode处于冻结')
134. .fontWeight(FontWeight.Bold)
135. .margin({ top: 48, bottom: 48 })
136. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // 返回至页面一
137. .width('80%')
138. .height(40)
139. .margin(20)
140. .onClick(() => {
141. this.pageInfo.pop();
142. })
143. }.width('100%').height('100%')
144. }.title('pageTwo')
145. .onBackPressed(() => {
146. this.pageInfo.pop();
147. return true;
148. })
149. }
150. }

152. @Component({ freezeWhenInactive: true })
153. // 设置冻结策略为不活跃冻结
154. struct NavigationContentMsgStack {
155. @Link message: number;
156. @Link index: number;
157. @Link logNumber: number;

159. build() {
160. Column() {
161. if (this.index === 1) {
162. NodeContainer(textNodeController)
163. }
164. }
165. }
166. }

168. @Component({ freezeWhenInactive: true })
169. // 设置冻结策略为不活跃冻结
170. struct TextBuilder {
171. @Prop @Watch("info") message: number = 0;
172. @State count: number = 0;

174. info() {
175. this.count++;
176. console.info(`freeze-test TextBuilder message callback change time ${this.count}`); // 根据message内容变化来打印日志来判断是否冻结
177. console.info(`freeze-test TextBuilder message callback change massage ${this.message}`); // 根据message内容变化来打印日志来判断是否冻结
178. }

180. build() {
181. Row() {
182. Column() {
183. Text(`文本更新内容： ${this.message}`)
184. .fontWeight(FontWeight.Bold)
185. .margin({ top: 48, bottom: 48 })
186. Text(`文本更新次数： ${this.count}`)
187. .fontWeight(FontWeight.Bold)
188. .margin({ top: 48, bottom: 48 })
189. }
190. }
191. }
192. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/q4BHw0WVQtW5EFDdSOV8zA/zh-cn_image_0000002552799782.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=F4BBD0C42B48276CB10EF4181E2EE41E72A3E214BACE76AB092EFB818CDDD502)

## ReactiveBuilderNode22+

PhonePC/2in1TabletTVWearable

ReactiveBuilderNode支持通过无状态的UI方法[@Builder](../harmonyos-guides/arkts-builder.md)生成组件树，并持有该组件树的根节点，不支持定义为状态变量。ReactiveBuilderNode中持有的[FrameNode](js-apis-arkui-framenode.md)仅用于将此ReactiveBuilderNode作为子节点挂载到其他FrameNode上。对ReactiveBuilderNode持有的FrameNode进行属性设置与子节点操作可能会导致未定义行为，因此不建议通过ReactiveBuilderNode的[getFrameNode](js-apis-arkui-buildernode.md#getframenode)方法和[FrameNode](js-apis-arkui-framenode.md)节点的[getRenderNode](js-apis-arkui-framenode.md#getrendernode)方法获取RenderNode，并通过[RenderNode](js-apis-arkui-rendernode.md)的接口对其进行属性设置与子节点操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor22+

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, options?: RenderOptions)

用于构造ReactiveBuilderNode类。当将ReactiveBuilderNode生成的内容嵌入到其它[RenderNode](js-apis-arkui-rendernode.md)中显示时，需要显式指定[RenderOptions](js-apis-arkui-buildernode.md#renderoptions)中的[selfIdealSize](js-apis-arkui-buildernode.md#renderoptions)，否则ReactiveBuilderNode内的节点默认父组件布局约束为[0, 0]。调用此接口，若不设置selfIdealSize则认为ReactiveBuilderNode中子树的根节点大小为[0, 0]。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | UI上下文，获取方式可参考[UIContext获取方法](js-apis-arkui-node.md#uicontext获取方法)。uiContext需要为一个有效的值，即UI上下文正确，如果传入非法值或者未设置，会导致创建失败。 |
| options | [RenderOptions](js-apis-arkui-buildernode.md#renderoptions) | 否 | ReactiveBuilderNode的构造可选参数，参数用于构造节点的理想大小和节点的渲染类型。  默认值：undefined |

### build22+

PhonePC/2in1TabletTVWearable

build(builder: WrappedBuilder<Args>, config: BuildOptions, ...args: Args): void

依照传入的对象创建组件树，并持有组件树的根节点。无状态的UI方法[@Builder](../harmonyos-guides/arkts-builder.md)最多拥有一个根节点。

支持自定义组件。

说明

@Builder进行创建和更新的规格参考[@Builder](../harmonyos-guides/arkts-builder.md)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [WrappedBuilder<Args>](../harmonyos-guides/arkts-wrapbuilder.md) | 是 | 创建对应节点树时所需的无状态UI方法[@Builder](../harmonyos-guides/arkts-builder.md)。 |
| config | [BuildOptions](js-apis-arkui-buildernode.md#buildoptions12) | 是 | 作用是配置Builder的构建行为，BuildOptions中所有属性都是可选的，默认值为BuildOptions中对应的默认值。 |
| ...args | Args | 否 | builder的入参，用于构造WrappedBuilder对象封装的builder函数。支持多个入参。默认值为undefined。 |

**示例：**

该示例演示了如何使用ReactiveBuilderNode的build接口动态创建响应式UI组件树，通过数据绑定实现UI内容的动态更新。

```
1. import { ReactiveBuilderNode, NodeContent, Binding, MutableBinding, UIUtils} from '@kit.ArkUI';

3. // Builder函数，用于构建显示多个数据的UI组件
4. @Builder
5. function buildText(age: Binding<number>, name: MutableBinding<string>, count: number) {
6. Column() {
7. Text(age.value.toString());
8. Text(name.value);
9. Text(count.toString());
10. }
11. }

13. @Entry
14. @Component
15. struct Index {
16. private content: NodeContent = new NodeContent();
17. private age: number = 10;
18. private grades: number = 100;

20. build() {
21. Row() {
22. Column() {
23. Text()
24. // 点击时动态创建并添加ReactiveBuilderNode
25. Button('add ReactiveBuilderNode').onClick(
26. () => {
27. // 创建ReactiveBuilderNode实例，泛型参数指定三个参数的类型
28. let node = new ReactiveBuilderNode<[Binding<number>, MutableBinding<string>, number]>(this.getUIContext());

30. // 构建节点内容，传入builder函数和参数
31. node.build(
32. wrapBuilder<[Binding<number>, Binding<string>, number]>(buildText),  // 包装builder函数
33. {},
34. UIUtils.makeBinding<number>(() => {
35. return this.age
36. }),
37. UIUtils.makeBinding<string>(() => 'Hello World'),
38. this.grades
39. );
40. // 将构建好的FrameNode添加到内容容器中显示
41. this.content.addFrameNode(node.getFrameNode());
42. })
43. ContentSlot(this.content)
44. }
45. .id('column')
46. .width('100%')
47. .height('100%')
48. }
49. .height('100%')
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/yMSzQYKxT1WGoUxloo6KMA/zh-cn_image_0000002583439477.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=9EF51A49E3824CB835F9865D7AEB0EDFD747663776C2233FC74DBC3C0620C591)

### getFrameNode22+

PhonePC/2in1TabletTVWearable

getFrameNode(): FrameNode | null

获取ReactiveBuilderNode中的[FrameNode](js-apis-arkui-framenode.md)。在ReactiveBuilderNode执行build操作之后，才会生成FrameNode。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md) | null | FrameNode对象。若该ReactiveBuilderNode不包含FrameNode，则返回空对象null。 |

**示例：**

该示例演示了如何使用getFrameNode接口获取ReactiveBuilderNode构建的FrameNode节点，并通过NodeContent动态管理UI节点。

```
1. import { ReactiveBuilderNode, NodeContent, Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

3. // Builder函数，构建包含文本和按钮的UI组件
4. @Builder
5. function buildText(age: Binding<number>, name: MutableBinding<string>, count: number) {
6. Column() {
7. Text(age.value.toString());
8. Text(name.value);
9. Text(count.toString());
10. Button('click').onClick(() => {
11. name.value = 'new name';
12. });
13. }
14. }

16. interface GeneratedObjectLiteralInterface_1 {
17. age: number;
18. name: string;
19. count: number;
20. }

22. @Entry
23. @Component
24. struct Index {
25. private content: NodeContent = new NodeContent();  // 动态节点内容容器
26. @State params: GeneratedObjectLiteralInterface_1 = {  // 状态数据对象
27. age: 10,
28. name: 'Hello World',
29. count: 100
30. };

32. // 扩展Builder
33. @Builder
34. extendBlank(age: Binding<number>) {
35. Row() {
36. Blank();
37. Text(`age: ${age.value}, blank`);
38. }
39. .height(20)
40. }

42. build() {
43. Row() {
44. Column() {
45. Text()
46. // 直接使用buildText Builder构建静态内容
47. buildText(UIUtils.makeBinding<number>(() => {
48. return this.params.age
49. }),
50. UIUtils.makeBinding<string>(() => this.params.name, val => {
51. this.params.name = this.params.name + '+1';
52. }),
53. this.params.count)
54. // 使用extendBlank Builder构建扩展内容
55. this.extendBlank(UIUtils.makeBinding<number>(() => {
56. return this.params.age
57. }))

59. // 动态添加ReactiveBuilderNode
60. Button('add ReactiveBuilderNode').onClick(
61. () => {
62. // 创建ReactiveBuilderNode实例
63. let node = new ReactiveBuilderNode<[Binding<number>, MutableBinding<string>, number]>(this.getUIContext());

65. // 构建节点内容
66. node.build(
67. wrapBuilder<[Binding<number>, Binding<string>, number]>(buildText),
68. {},
69. UIUtils.makeBinding<number>(() => {
70. return this.params.age
71. }),
72. UIUtils.makeBinding<string>(() => this.params.name, val => {
73. this.params.name = val;
74. }),
75. this.params.count
76. );
77. this.content.addFrameNode(node.getFrameNode());
78. })
79. ContentSlot(this.content)
80. }
81. .id('column')
82. .width('100%')
83. .height('100%')
84. }
85. .height('100%')
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/aEI6jCwsQkGvGvXwCtdu5w/zh-cn_image_0000002552959432.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=A5CC57D720CAFE0F8FAE4A54F14EE9A43EF10F476E1D1C3FDF417BB00EE6C7A2)

### postTouchEvent22+

PhonePC/2in1TabletTVWearable

postTouchEvent(event: TouchEvent): boolean

将原始事件派发到某个ReactiveBuilderNode创建的FrameNode上。

postTouchEvent是从组件树的中间节点往下分发，需要变换到父组件坐标系才能分发成功，参考下图。

OffsetA为buildNode相对于父组件的偏移量，可以通过FrameNode中的[getPositionToParent](js-apis-arkui-framenode.md#getpositiontoparent12)获取。OffsetB为point点相对于buildNode的偏移量，可以通过[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)获取。OffsetC为OffsetA与OffsetB的和，是传给postTouchEvent的最终结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/s05_tFeLTRySMaEyAyAbMg/zh-cn_image_0000002583439475.png?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=7EF7175C283A8858C8D2D45D9B0169636269CD8E7EE795974D3F72DC47A60613)

说明

传入的坐标值需要转换为px，如果builderNode有仿射变换，则需要再叠加仿射变换。

在[webview](arkts-apis-webview.md)中，内部已经处理过坐标系变换，可以将TouchEvent事件直接下发。

同一时间戳，postTouchEvent只能调用一次。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 触摸事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 派发事件是否成功。true：已命中响应事件的组件；false：未命中任何可响应事件的组件。  **说明：**  如果未按照预期命中组件，需要确认：  1.坐标系是否转换正确。  2.组件是否可交互状态。  3.是否绑定事件。 |

**示例：**

该示例实现了通过ReactiveBuilderNode构建的按钮组件与外部容器的触摸事件联动，演示了自定义节点中触摸事件的坐标转换与跨节点传递机制。

当触摸下方蓝色区域时，触摸事件会经过坐标转换后传递给上方的ReactiveBuilderNode按钮，触发按钮的触摸反馈和日志输出，实现了触摸事件的跨节点精准传递。

```
1. import { NodeController, ReactiveBuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. @Builder
4. function ButtonBuilder() {
5. Column() {
6. Button(`Button`)
7. .borderWidth(2)
8. .backgroundColor(Color.Gray)
9. .width('100%')
10. .height('100%')
11. .gesture(
12. TapGesture()
13. .onAction((event: GestureEvent) => {
14. console.info('TapGesture');
15. })
16. )
17. .onTouch(() => {
18. console.info(`postTouchEvent Success`);
19. })
20. }
21. .width(500)
22. .height(300)
23. .backgroundColor(Color.Gray)
24. }

26. // 继承NodeController实现自定义UI控制器
27. class MyNodeController extends NodeController {
28. private rootNode: ReactiveBuilderNode<[]> | null = null;
29. private wrapBuilder: WrappedBuilder<[]> = wrapBuilder(ButtonBuilder);

31. makeNode(uiContext: UIContext): FrameNode | null {
32. this.rootNode = new ReactiveBuilderNode(uiContext);
33. this.rootNode.build(this.wrapBuilder, {});
34. return this.rootNode.getFrameNode();
35. }

37. // 坐标转换示例
38. postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
39. if (this.rootNode == null) {
40. return false;
41. }
42. let node: FrameNode | null = this.rootNode.getFrameNode();
43. let offsetX: number | null | undefined = node?.getPositionToParent().x;
44. let offsetY: number | null | undefined = node?.getPositionToParent().y;

46. let changedTouchLen = event.changedTouches.length;
47. for (let i = 0; i < changedTouchLen; i++) {
48. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
49. event.changedTouches[i].x = uiContext.vp2px(offsetX + event.changedTouches[i].x);
50. event.changedTouches[i].y = uiContext.vp2px(offsetY + event.changedTouches[i].y);
51. }
52. }
53. let result = this.rootNode.postTouchEvent(event);
54. console.info(`result ${result}`);
55. return result;
56. }
57. }

59. @Entry
60. @Component
61. struct MyComponent {
62. private nodeController: MyNodeController = new MyNodeController();

64. build() {
65. Column() {
66. NodeContainer(this.nodeController)
67. .height(300)
68. .width(500)

70. Column()
71. .width(500)
72. .height(300)
73. .backgroundColor('#ADD8E6')
74. .onTouch((event) => {
75. if (event != undefined) {
76. this.nodeController.postTouchEvent(event, this.getUIContext());
77. }
78. })
79. }
80. }
81. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/GJ6qxwpHTiOPIYi_NEVpxw/zh-cn_image_0000002583479433.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=3CEA5D4EAB83713A27C8E9B4A25C98FB7E7028A5F217FE04BA0042A25C5D64BB)

### dispose22+

PhonePC/2in1TabletTVWearable

dispose(): void

立即释放当前ReactiveBuilderNode对象对[实体节点](../harmonyos-guides/arkts-user-defined-node.md#基本概念)的引用关系。关于ReactiveBuilderNode的解绑场景请参见[节点解绑](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

说明

当ReactiveBuilderNode对象调用dispose之后，会与后端实体节点解除引用关系。若前端对象ReactiveBuilderNode无法释放，容易导致内存泄漏。建议在不再需要对该ReactiveBuilderNode对象进行操作时，开发者主动调用dispose释放后端节点，以减少引用关系的复杂性，降低内存泄漏的风险。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例演示了如何通过dispose接口实现ReactiveBuilderNode组件的动态移除与资源释放。

```
1. import { FrameNode, NodeController, ReactiveBuilderNode } from '@kit.ArkUI';

3. @Component
4. struct TestComponent {
5. build() {
6. Column() {
7. Text('This is a ReactiveBuilderNode.')
8. .fontSize(16)
9. .fontWeight(FontWeight.Bold)
10. }
11. .width('100%')
12. .backgroundColor(Color.Gray)
13. }

15. aboutToAppear() {
16. console.info('aboutToAppear');
17. }

19. aboutToDisappear() {
20. console.info('aboutToDisappear');
21. }
22. }

24. @Builder
25. function buildComponent() {
26. TestComponent()
27. }

29. // 自定义节点控制器，管理ReactiveBuilderNode和FrameNode
30. class MyNodeController extends NodeController {
31. private rootNode: FrameNode | null = null;
32. private builderNode: ReactiveBuilderNode<[]> | null = null;

34. makeNode(uiContext: UIContext): FrameNode | null {
35. // 创建根FrameNode
36. this.rootNode = new FrameNode(uiContext);
37. this.builderNode = new ReactiveBuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
38. // 构建ReactiveBuilderNode内容
39. this.builderNode.build(new WrappedBuilder(buildComponent), {});

41. const rootRenderNode = this.rootNode!.getRenderNode();
42. if (rootRenderNode !== null) {
43. rootRenderNode.size = { width: 200, height: 200 };
44. rootRenderNode.backgroundColor = 0xff666666;
45. // 将ReactiveBuilderNode的RenderNode添加到根节点
46. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
47. }

49. return this.rootNode;
50. }

52. // 释放资源的方法
53. dispose() {
54. if (this.builderNode !== null) {
55. this.builderNode.dispose(); // 释放ReactiveBuilderNode资源
56. }
57. }

59. // 移除BuilderNode的方法
60. removeBuilderNode() {
61. const rootRenderNode = this.rootNode!.getRenderNode();
62. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
63. // 从根节点移除BuilderNode的RenderNode
64. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
65. }
66. }
67. }

69. @Entry
70. @Component
71. struct Index {
72. private myNodeController: MyNodeController = new MyNodeController();

74. build() {
75. Column({ space: 4 }) {
76. NodeContainer(this.myNodeController)
77. // 移除并释放ReactiveBuilderNode
78. Button('ReactiveBuilderNode dispose')
79. .onClick(() => {
80. this.myNodeController.removeBuilderNode();
81. this.myNodeController.dispose();
82. })
83. .width('70%')
84. }
85. .width('100%')
86. .height('100%')
87. .justifyContent(FlexAlign.Center)
88. .alignItems(HorizontalAlign.Center)
89. }
90. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/bx6nNDFBRUyYuTYexnw1ZQ/zh-cn_image_0000002552799784.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=1CF292EF1BEC63BF1AD68A29E2A9A557BF27BE387ECC0629D0352C609085DF1A)

### reuse22+

PhonePC/2in1TabletTVWearable

reuse(param?: Object): void

触发ReactiveBuilderNode中的自定义组件的复用。组件复用请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。关于ReactiveBuilderNode的解绑场景请参见[节点解绑](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

ReactiveBuilderNode通过reuse和[recycle](js-apis-arkui-buildernode.md#recycle22)完成其内外自定义组件之间的复用事件传递，具体使用场景请参见[BuilderNode调用reuse和recycle接口实现节点复用能力](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | Object | 否 | 用于复用[ReactiveBuilderNode](js-apis-arkui-buildernode.md#reactivebuildernode22)的参数。该参数将直接用于[ReactiveBuilderNode](js-apis-arkui-buildernode.md#reactivebuildernode22)中所有顶层自定义组件的复用，应该包含每个自定义组件的构造函数参数所需内容，否则，会导致未定义行为。调用此方法将同步触发内部自定义组件的[aboutToReuse](ts-custom-component-lifecycle.md#abouttoreuse10)生命周期回调，并将该参数作为回调的入参。默认值为undefined，此时ReactiveBuilderNode中的自定义组件将直接使用构造时的数据源。 |

**示例：**

请参考[recycle](js-apis-arkui-buildernode.md#recycle22)中的示例。

### recycle22+

PhonePC/2in1TabletTVWearable

recycle(): void

触发ReactiveBuilderNode中自定义组件的回收。自定义组件的回收是组件复用机制中的环节，具体信息请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。

ReactiveBuilderNode通过[reuse](js-apis-arkui-buildernode.md#reuse22)和recycle完成其内外自定义组件之间的复用事件传递，具体使用场景请参见[BuilderNode调用reuse和recycle接口实现节点复用能力](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例展示了在长列表场景下，如何使用ReactiveBuilderNode的reuse和recycle接口实现组件复用机制，优化列表滚动的性能表现。

```
1. import { FrameNode, NodeController, ReactiveBuilderNode, UIContext } from '@kit.ArkUI';

3. const TEST_TAG: string = 'Reuse+Recycle';

5. // 自定义数据源类，用于管理列表数据
6. class MyDataSource {
7. private dataArray: string[] = [];
8. private listener: DataChangeListener | null = null;

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number) {
15. return this.dataArray[index];
16. }

18. public pushData(data: string) {
19. this.dataArray.push(data);
20. }

22. public reloadListener(): void {
23. this.listener?.onDataReloaded();
24. }

26. // 注册数据变化监听器
27. public registerDataChangeListener(listener: DataChangeListener): void {
28. this.listener = listener;
29. }

31. public unregisterDataChangeListener(): void {
32. this.listener = null;
33. }
34. }

36. // 构建器函数，用于创建列表项UI
37. @Builder
38. function buildNode(text: string) {
39. Row() {
40. Text(`C${text} -- `)
41. ReusableChildComponent2({ item: text }) // 嵌套可复用组件
42. }
43. }

45. // 自定义节点控制器，管理ReactiveBuilderNode
46. class MyNodeController extends NodeController {
47. public builderNode: ReactiveBuilderNode<[string]> | null = null;
48. public item: string = '';

50. // 创建节点方法
51. makeNode(uiContext: UIContext): FrameNode | null {
52. if (this.builderNode == null) {
53. // 创建ReactiveBuilderNode并设置理想尺寸
54. this.builderNode = new ReactiveBuilderNode(uiContext, { selfIdealSize: { width: 300, height: 200 } });
55. // 使用构建器函数构建节点内容
56. this.builderNode.build(wrapBuilder<[string]>(buildNode), {}, this.item);
57. }
58. return this.builderNode.getFrameNode();
59. }
60. }

62. @Reusable
63. @Component
64. struct ReusableChildComponent {
65. @Prop item: string = '';
66. @Prop switch: string = '';
67. private controller: MyNodeController = new MyNodeController();

69. aboutToAppear() {
70. this.controller.item = this.item; // 初始化控制器数据
71. }

73. // 组件回收时的生命周期回调
74. aboutToRecycle(): void {
75. console.info(`${TEST_TAG} ReusableChildComponent aboutToRecycle ${this.item}`);

77. // 当开关打开时，触发builderNode的回收
78. if (this.switch === 'open') {
79. this.controller?.builderNode?.recycle();
80. }
81. }

83. // 组件复用时的生命周期回调
84. aboutToReuse(params: object): void {
85. console.info(`${TEST_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}`);

87. // 当开关打开时，触发builderNode的复用
88. if (this.switch === 'open') {
89. this.controller?.builderNode?.reuse(params);
90. }
91. }

93. build() {
94. Row() {
95. Text(`A${this.item}--`)
96. ReusableChildComponent3({ item: this.item })
97. NodeContainer(this.controller); // 包含NodeContainer用于显示自定义节点
98. }
99. }
100. }

102. @Component
103. struct ReusableChildComponent2 {
104. @Prop item: string = 'false';

106. // 复用时的回调
107. aboutToReuse(params: Record<string, object>) {
108. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToReuse ${JSON.stringify(params)}`);
109. }

111. // 回收时的回调
112. aboutToRecycle(): void {
113. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToRecycle ${this.item}`);
114. }

116. build() {
117. Row() {
118. Text(`D${this.item}`)
119. .fontSize(20)
120. .backgroundColor(Color.Yellow)
121. .margin({ left: 10 })
122. }.margin({ left: 10, right: 10 })
123. }
124. }

126. @Component
127. struct ReusableChildComponent3 {
128. @Prop item: string = 'false';

130. // 复用时的回调
131. aboutToReuse(params: Record<string, object>) {
132. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToReuse ${JSON.stringify(params)}`);
133. }

135. // 回收时的回调
136. aboutToRecycle(): void {
137. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToRecycle ${this.item}`);
138. }

140. build() {
141. Row() {
142. Text(`B${this.item}`)
143. .fontSize(20)
144. .backgroundColor(Color.Yellow)
145. .margin({ left: 10 })
146. }.margin({ left: 10, right: 10 })
147. }
148. }

151. @Entry
152. @Component
153. struct Index {
154. @State data: MyDataSource = new MyDataSource();

156. aboutToAppear() {
157. // 初始化列表数据
158. for (let i = 0; i < 100; i++) {
159. this.data.pushData(i.toString());
160. }
161. }

163. build() {
164. Column() {
165. // 使用LazyForEach渲染长列表，支持组件复用
166. List({ space: 3 }) {
167. LazyForEach(this.data, (item: string) => {
168. ListItem() {
169. ReusableChildComponent({
170. item: item,
171. switch: 'open' // 开启复用回收功能
172. })
173. }
174. }, (item: string) => item)
175. }
176. .width('100%')
177. .height('100%')
178. }
179. }
180. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/3bC4_eRETaO2i0C0lL9QQA/zh-cn_image_0000002583439479.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=E8D7133945528A8055789214EF678F15C18E293205C0F6F7B43AF237A47D684E)

### updateConfiguration22+

PhonePC/2in1TabletTVWearable

updateConfiguration(): void

传递[系统环境变化](js-apis-app-ability-configuration.md)事件，触发节点的全量更新。可用于通知对象更新，是否更新所使用的系统环境由应用当前的系统环境变化决定。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例展示了如何使用updateConfiguration接口响应系统环境变化，实现ReactiveBuilderNode构建的UI节点的动态更新。

```
1. import { NodeController, ReactiveBuilderNode, FrameNode, UIContext, FrameCallback, Binding, UIUtils } from '@kit.ArkUI';
2. import { AbilityConstant, Configuration, ConfigurationConstant, EnvironmentCallback } from '@kit.AbilityKit';

4. // 自定义组件
5. @Component
6. struct TextBuilder {
7. // 作为自定义组件中需要更新的属性，数据类型为基础属性，定义为@Prop
8. @Prop message: string = 'TextBuilder';

10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(20)
15. .fontWeight(FontWeight.Bold)
16. .margin({ bottom: 30 })
17. }
18. .justifyContent(FlexAlign.Center)
19. .alignItems(HorizontalAlign.Center)
20. .width('100%')
21. }
22. .width('100%')
23. }
24. }

26. @Builder
27. function buildText(text: Binding<string>) {
28. Column() {
29. Text(text.value)
30. .fontSize(20)
31. .fontWeight(FontWeight.Bold)
32. .margin({ bottom: 15 })
33. TextBuilder({ message: text.value }) // 自定义组件
34. }
35. .backgroundColor($r('sys.color.ohos_id_color_background'))
36. .justifyContent(FlexAlign.Center)
37. .alignItems(HorizontalAlign.Center)
38. .width('100%')
39. .height('100%')
40. }

42. // 继承NodeController实现自定义textNode控制器
43. class TextNodeController extends NodeController {
44. private textNode: ReactiveBuilderNode<[Binding<string>]> | null = null;
45. private message: string = '';

47. constructor(message: string) {
48. super();
49. this.message = message;
50. }

52. makeNode(context: UIContext): FrameNode | null {
53. return this.textNode?.getFrameNode() ? this.textNode?.getFrameNode() : null;
54. }

56. createNode(context: UIContext) {
57. this.textNode = new ReactiveBuilderNode(context);
58. this.textNode.build(wrapBuilder<[Binding<string>]>(buildText), {},
59. UIUtils.makeBinding<string>(() => this.message, val => {
60. this.message = val;
61. }));
62. builderNodeMap.push(this.textNode);
63. }

65. deleteNode() {
66. let node = builderNodeMap.pop();
67. node?.dispose();
68. }

70. update(message: string) {
71. this.message = message
72. this.textNode?.flushState();
73. }
74. }

76. // 记录创建的自定义节点对象
77. const builderNodeMap: Array<ReactiveBuilderNode<[text: Binding<string>]>> = new Array();

79. class MyFrameCallback extends FrameCallback {
80. onFrame() {
81. updateColorMode();
82. }
83. }

85. function updateColorMode() {
86. builderNodeMap.forEach((value, index) => {
87. // 通知BuilderNode环境变量改变，触发深浅色切换
88. value.updateConfiguration();
89. })
90. }

92. @Entry
93. @Component
94. struct Index {
95. @State message: string = 'hello';
96. private textNodeController: TextNodeController = new TextNodeController(this.message);
97. private count = 0;

99. aboutToAppear(): void {
100. let environmentCallback: EnvironmentCallback = {
101. onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
102. console.info('onMemoryLevel');
103. },
104. onConfigurationUpdated: (config: Configuration): void => {
105. console.info(`onConfigurationUpdated ${JSON.stringify(config)}`);
106. this.getUIContext()?.postFrameCallback(new MyFrameCallback());
107. }
108. };
109. // 注册监听回调
110. this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
111. // 设置应用深浅色跟随系统
112. this.getUIContext()
113. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
114. // 创建自定义节点并添加至builderNodeMap
115. this.textNodeController.createNode(this.getUIContext());
116. }

118. aboutToDisappear(): void {
119. // 移除builderNodeMap中的引用，并将自定义节点释放
120. this.textNodeController.deleteNode();
121. }

123. build() {
124. Row() {
125. Column({ space: 12 }) {
126. NodeContainer(this.textNodeController)
127. .width('100%')
128. .height(70)
129. .backgroundColor('#FFF0F0F0')
130. Button('Update')
131. .onClick(() => {
132. this.count += 1;
133. const message = 'Update ' + this.count.toString();
134. this.textNodeController.update(message);
135. })
136. Button('设置深色')
137. .onClick(() => {
138. this.getUIContext()
139. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
140. })
141. Button('设置浅色')
142. .onClick(() => {
143. this.getUIContext()
144. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
145. })
146. }
147. .width('100%')
148. .height('100%')
149. }
150. .height('100%')
151. }
152. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/JB1nmsLLS0a1GBAVCgbq0Q/zh-cn_image_0000002552959434.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=F4595C781DE7CE2B57F68E8E2167478143C2ECB2CCE6E462581AA6034B699690)

### flushState22+

PhonePC/2in1TabletTVWearable

flushState(): void

根据提供的参数更新ReactiveBuilderNode。当ReactiveBuilderNode中[WrappedBuilder](../harmonyos-guides/arkts-wrapbuilder.md)对象封装的builder函数中使用的绑定参数是由V1装饰器（如@Observed）装饰的类实例时，需要在此类数据变更后手动调用此方法以更新数据，当使用V2装饰器（如@ObservedV2）装饰的类实例时，支持自动更新，无需手动调用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例展示了flushState接口在V1和V2装饰器下的不同使用方式，演示了ReactiveBuilderNode在不同数据响应机制下的更新策略。

```
1. import { ReactiveBuilderNode, NodeContent, Binding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function buildText(age: Binding<number>) {
5. Column() {
6. Text(`age: ${age.value}`);
7. }
8. }

10. // 使用V2装饰器的类，支持自动状态更新
11. @ObservedV2
12. class GeneratedObjectLiteralInterface_1 {
13. constructor(age: number) {
14. this.age = age;
15. }

17. @Trace age: number = 0;
18. }

20. // 使用普通类（V1装饰器风格），需要手动触发更新
21. class GeneratedObjectLiteralInterface_2 {
22. constructor(age: number) {
23. this.age = age;
24. }

26. age: number = 0;
27. }

29. @Entry
30. @ComponentV2
31. struct Index {
32. private content: NodeContent = new NodeContent();
33. params: GeneratedObjectLiteralInterface_1 = new GeneratedObjectLiteralInterface_1(25);
34. params2: GeneratedObjectLiteralInterface_2 = new GeneratedObjectLiteralInterface_2(25);
35. private node1: ReactiveBuilderNode<[Binding<number>]> | null = null

37. build() {
38. Row() {
39. Scroll() {
40. Column({ space: 12 }) {
41. // 创建使用V2装饰器的ReactiveBuilderNode
42. Button('绑定参数由V2装饰器装饰').onClick(
43. () => {
44. let node =
45. new ReactiveBuilderNode<[Binding<number>]>(this.getUIContext());
46. node.build(
47. wrapBuilder<[Binding<number>]>(buildText),
48. {},
49. UIUtils.makeBinding<number>(() => {
50. return this.params.age;
51. })
52. );
53. this.content.addFrameNode(node.getFrameNode());
54. })
55. // 创建使用V1装饰器的ReactiveBuilderNode
56. Button('绑定参数由V1装饰器装饰').onClick(
57. () => {
58. this.node1 =
59. new ReactiveBuilderNode<[Binding<number>]>(this.getUIContext());
60. this.node1.build(
61. wrapBuilder<[Binding<number>]>(buildText),
62. {},
63. UIUtils.makeBinding<number>(() => {
64. return this.params2.age;
65. })
66. );
67. this.content.addFrameNode(this.node1.getFrameNode());
68. })
69. Button('change age - V2可自动更新').onClick(() => {
70. this.params.age += 1; // V2装饰器会自动检测变化并更新UI
71. })
72. Button('change age - V1需手动更新').onClick(() => {
73. this.params2.age += 1;
74. // 对于V1装饰器的数据，需要手动调用flushState来触发UI更新
75. this.node1?.flushState();
76. })
77. // 显示动态创建的内容
78. ContentSlot(this.content)
79. }
80. .id("column")
81. .width('100%')
82. }
83. .scrollable(ScrollDirection.Vertical)
84. .scrollBar(BarState.On)
85. .scrollBarColor(Color.Gray)
86. .scrollBarWidth(10)
87. }
88. .height('100%')
89. }
90. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Gev7AcYOTPipoVw01ik_jA/zh-cn_image_0000002583479435.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=2D122AF6C8F3076B69579FEA4AAC17F59BDD7C8E6D9F55EECD6006B18D48A102)

### postInputEvent22+

PhonePC/2in1TabletTVWearable

postInputEvent(event: InputEventType): boolean

将输入事件分发到ReactiveBuilderNode管理的目标节点。

offsetA为builderNode相对于父组件的偏移，offsetB为命中位置相对于builderNode的偏移，offsetC为offsetA+offsetB，最终输入给postInputEvent当中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/4Fo4DYLWTieJ-JzsRPDWcQ/zh-cn_image_0000002583439475.png?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=62C3B69D4CD2C99A99906239ACD16C637E873F6BD09AFAC7EAFC5F701B79C8AB)

说明

传入的坐标值需要转换为px，坐标转换示例可以参考下面示例代码。

鼠标左键点击事件将转换为触摸事件，转发时应注意不在外层且绑定触摸事件与鼠标事件，否则可能导致坐标偏移。这是由于在事件转换过程中，SourceType不会发生变化，规格可查看[onTouch](ts-universal-events-touch.md#ontouch)。

注入事件为[轴事件](ts-universal-events-axis.md#axisevent)时，由于轴事件中缺少旋转轴信息，因此注入的事件无法触发[rotate旋转手势](ts-basic-gestures-rotationgesture.md)。

转发的事件会在被分发到的目标组件所在的子树里做触摸测试（TouchTest），并触发对应手势，原始事件也会触发当前组件所在组件树中的手势。不保证两类手势的竞争结果。

如果是开发者构造的事件，必填字段必须赋值，比如触摸事件的touches字段、轴事件的scrollStep字段，同时要保证事件的完整，比如触摸事件的[TouchType](ts-appendix-enums.md#touchtype)中DOWN和UP字段都要有，防止出现未定义行为。

[webview](arkts-apis-webview.md)已经处理过坐标系变换，可以将事件直接下发。

postTouchEvent接口需要提供手势坐标相对于输入事件对端内的局部坐标，postInputEvent接口需要提供手势坐标相对于输入事件对端内的窗口坐标。

不建议同一个事件转发多次。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InputEventType](js-apis-arkui-buildernode.md#inputeventtype20) | 是 | 待分发的输入事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 事件是否被成功分发。如果事件分发成功，则返回true；否则，返回false。 |

**示例：**

请参考[示例13（ReactiveBuilderNode中鼠标事件）](js-apis-arkui-buildernode.md#示例13reactivebuildernode中鼠标事件)、[示例14（ReactiveBuilderNode中触摸事件）](js-apis-arkui-buildernode.md#示例14reactivebuildernode中触摸事件)、[示例15（ReactiveBuilderNode中轴事件）](js-apis-arkui-buildernode.md#示例15reactivebuildernode中轴事件)。

### inheritFreezeOptions22+

PhonePC/2in1TabletTVWearable

inheritFreezeOptions(enabled: boolean): void

查询当前ReactiveBuilderNode对象是否设置为继承父组件中自定义组件的冻结策略。如果设置继承状态为false，则ReactiveBuilderNode对象的冻结策略为false。在这种情况下，节点在不活跃状态下不会被冻结。

说明

ReactiveBuilderNode设置inheritFreezeOptions为true，且父组件为自定义组件、BuilderNode、ComponentContent、ReactiveBuilderNode或ReactiveComponentContent时，会继承父组件的冻结策略。当子组件为自定义组件时，其冻结策略不会传递给子组件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | ReactiveBuilderNode对象是否设置为继承父组件中自定义组件的冻结策略。true为继承父组件中自定义组件的冻结策略，false为不继承父组件中自定义组件的冻结策略。 |

**示例：**

该示例演示了ReactiveBuilderNode设置继承状态为true时，继承父自定义组件的冻结策略。在页面跳转走不活跃时进行冻结，页面切换回来为活跃状态解冻，更新缓存的数据。

```
1. import { ReactiveBuilderNode, FrameNode, NodeController, Binding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. function buildText(count: Binding<number>) {
5. Column() {
6. TextBuilder({ message: count.value })
7. }
8. }

10. // 自定义节点控制器（逻辑不变）
11. class TextNodeController extends NodeController {
12. private rootNode: FrameNode | null = null;
13. private textNode: ReactiveBuilderNode<[Binding<number>]> | null = null;
14. private count: number = 0; // 内部计数状态

16. makeNode(context: UIContext): FrameNode | null {
17. this.rootNode = new FrameNode(context);
18. this.textNode = new ReactiveBuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
19. // 构建节点内容
20. this.textNode.build(wrapBuilder<[Binding<number>]>(buildText), {}, UIUtils.makeBinding<number>(() => {
21. return this.count
22. }));
23. // 启用冻结继承选项，当父组件冻结时自动冻结
24. this.textNode.inheritFreezeOptions(true);
25. // 将ReactiveBuilderNode添加到根节点
26. if (this.rootNode !== null) {
27. this.rootNode.appendChild(this.textNode.getFrameNode());
28. }
29. return this.rootNode;
30. }

32. update(): void {
33. if (this.textNode !== null) {
34. this.count += 1; // 增加计数
35. this.textNode.flushState();
36. }
37. }
38. }

40. const textNodeController: TextNodeController = new TextNodeController();

42. @Entry
43. @Component
44. struct MyNavigationTestStack {
45. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
46. @State message: number = 0;
47. @State logNumber: number = 0;

49. @Builder
50. PageMap(name: string) {
51. if (name === 'pageOne') {
52. pageOneStack({ message: $message, logNumber: $logNumber })
53. } else if (name === 'pageTwo') {
54. pageTwoStack({ message: $message, logNumber: $logNumber })
55. }
56. }

58. @Builder
59. CustomTitle() {
60. Text('NavIndex')
61. .fontSize(20)
62. .fontColor(Color.Black)
63. .fontWeight(FontWeight.Normal)
64. }

66. build() {
67. Column() {
68. Button('update builderNode')
69. .fontSize(18)
70. .onClick(() => {
71. textNodeController.update();
72. })

74. Navigation(this.pageInfo) {
75. Column() {
76. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
77. .fontSize(18)
78. .width('80%')
79. .height(40)
80. .margin(10)
81. .onClick(() => {
82. this.pageInfo.pushPath({ name: 'pageOne' });
83. })
84. }
85. }
86. .title(this.CustomTitle)
87. .navDestination(this.PageMap)
88. .mode(NavigationMode.Stack)
89. }
90. .width('100%')
91. .height('100%')
92. .padding(10)
93. }
94. }

96. @Component
97. struct pageOneStack { // 页面一
98. @Consume('pageInfo') pageInfo: NavPathStack;
99. @State index: number = 1;
100. @Link message: number;
101. @Link logNumber: number;

103. build() {
104. NavDestination() {
105. Column() {
106. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })

108. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
109. .fontSize(18)
110. .width('80%')
111. .height(40)
112. .margin(8)
113. .onClick(() => {
114. this.pageInfo.pushPathByName('pageTwo', null);
115. })

117. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
118. .fontSize(18)
119. .width('80%')
120. .height(40)
121. .margin(8)
122. .onClick(() => {
123. this.pageInfo.pop();
124. })
125. }
126. .width('100%')
127. .height('100%')
128. }
129. .title('pageOne')
130. .onBackPressed(() => {
131. this.pageInfo.pop();
132. return true;
133. })
134. }
135. }

137. @Component
138. struct pageTwoStack { // 页面二
139. @Consume('pageInfo') pageInfo: NavPathStack;
140. @State index: number = 2;
141. @Link message: number;
142. @Link logNumber: number;

144. build() {
145. NavDestination() {
146. Column({ space: 8 }) {
147. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })

149. Text('BuilderNode处于冻结状态')
150. .fontSize(18)
151. .fontWeight(FontWeight.Bold)
152. .margin({ top: 16, bottom: 16 })

154. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
155. .fontSize(18)
156. .width('80%')
157. .height(40)
158. .margin(8)
159. .onClick(() => {
160. this.pageInfo.pop();
161. })
162. }
163. .width('100%')
164. .height('100%')
165. }
166. .title('pageTwo')
167. .onBackPressed(() => {
168. this.pageInfo.pop();
169. return true;
170. })
171. }
172. }

174. @Component({ freezeWhenInactive: true })
175. // 启用非活动时冻结
176. struct NavigationContentMsgStack {
177. @Link message: number;
178. @Link index: number;
179. @Link logNumber: number;

181. build() {
182. Column() {
183. if (this.index === 1) {
184. NodeContainer(textNodeController)
185. .margin({ bottom: 5 })
186. }
187. }
188. }
189. }

191. // 文本构建器组件，支持冻结
192. @Component({ freezeWhenInactive: true })
193. struct TextBuilder {
194. @Prop @Watch('info') message: number = 0;
195. @State count: number = 0;

197. info() {
198. this.count++;
199. console.info(`freeze-test TextBuilder message callback change time ${this.count}`);
200. console.info(`freeze-test TextBuilder message callback change massage ${this.message}`);
201. }

203. build() {
204. Row() {
205. Column() {
206. Text(`文本更新内容： ${this.message}`)
207. .fontSize(18)
208. .fontWeight(FontWeight.Bold)
209. .margin({ top: 16, bottom: 16 })

211. Text(`文本更新次数： ${this.count}`)
212. .fontSize(18)
213. .fontWeight(FontWeight.Bold)
214. .margin({ top: 16, bottom: 16 })
215. }
216. }
217. }
218. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/tEabB1PXQayhIuIUDWLIiQ/zh-cn_image_0000002552799786.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=873EDFECAE543E69F1048D8B4CABA8CAA59894E78DB23BFAB3A513647320E931)

### isDisposed22+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前ReactiveBuilderNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。因为在节点dispose后可能仍存在被调用dispose接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

参考[isDisposed](js-apis-arkui-buildernode.md#isdisposed20)示例。

该示例演示了ReactiveBuilderNode释放节点前后分别使用[isDisposed](js-apis-arkui-buildernode.md#isdisposed22)接口验证节点的状态，释放节点前节点调用isDisposed接口返回true，释放节点后节点调用isDisposed接口返回false。

```
1. import { FrameNode, NodeController, ReactiveBuilderNode } from '@kit.ArkUI';

3. @Component
4. struct TestComponent {
5. build() {
6. Column() {
7. Text('This is a BuilderNode.')
8. .fontSize(25)
9. .fontWeight(FontWeight.Bold)
10. }
11. .width('100%')
12. .height(30)
13. .backgroundColor(Color.Gray)
14. }

16. aboutToAppear() {
17. console.info('aboutToAppear');
18. }

20. aboutToDisappear() {
21. console.info('aboutToDisappear');
22. }
23. }

25. @Builder
26. function buildComponent() {
27. TestComponent()
28. }

30. // 继承NodeController实现自定义UI控制器
31. class MyNodeController extends NodeController {
32. private rootNode: FrameNode | null = null; // 根FrameNode容器
33. private builderNode: ReactiveBuilderNode<[]> | null = null; // ReactiveBuilderNode实例

35. makeNode(uiContext: UIContext): FrameNode | null {
36. this.rootNode = new FrameNode(uiContext);
37. this.builderNode = new ReactiveBuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
38. // 构建ReactiveBuilderNode内容，使用WrappedBuilder包装Builder函数
39. this.builderNode.build(new WrappedBuilder(buildComponent), {});

41. const rootRenderNode = this.rootNode!.getRenderNode();
42. if (rootRenderNode !== null) {
43. rootRenderNode.size = { width: 300, height: 50 };
44. rootRenderNode.backgroundColor = 0xffd5d5d5;
45. // 将ReactiveBuilderNode的RenderNode添加到根节点
46. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
47. }

49. return this.rootNode;
50. }

52. // 释放资源的方法
53. dispose() {
54. if (this.builderNode !== null) {
55. this.builderNode.dispose(); // 释放ReactiveBuilderNode资源
56. }
57. }

59. // 检查节点是否已释放的方法
60. isDisposed(): string {
61. if (this.builderNode !== null) {
62. if (this.builderNode.isDisposed()) {
63. return 'builderNode isDisposed is true';
64. } else {
65. return 'builderNode isDisposed is false';
66. }
67. }
68. return 'builderNode is null';
69. }

71. removeBuilderNode() {
72. const rootRenderNode = this.rootNode!.getRenderNode();
73. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
74. // 从根节点移除BuilderNode的RenderNode
75. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
76. }
77. }
78. }

80. @Entry
81. @Component
82. struct Index {
83. @State text: string = '' // 状态变量，用于显示节点状态信息
84. private myNodeController: MyNodeController = new MyNodeController();

86. build() {
87. Column({ space: 4 }) {
88. NodeContainer(this.myNodeController)
89. Button('BuilderNode dispose')
90. .onClick(() => {
91. this.myNodeController.removeBuilderNode();
92. this.myNodeController.dispose(); // 释放资源
93. this.text = '';
94. })
95. .width(200)
96. .height(50)
97. Button('BuilderNode isDisposed')
98. .onClick(() => {
99. this.text = this.myNodeController.isDisposed();
100. })
101. .width(200)
102. .height(50)
103. // 显示节点状态信息
104. Text(this.text)
105. .fontSize(20)
106. }
107. .width('100%')
108. .height('100%')
109. }
110. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/8MRPMOk1TKmhVgSGc2cHMw/zh-cn_image_0000002583439481.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=CFB2B5476362C83D74778094CF89C2B6E5CC5A5B398F6AA8FF25963525969538)

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（BuilderNode中鼠标事件）

该示例演示了在自定义组件中截获鼠标事件并进行坐标转换的完整流程。组件通过[onMouse](ts-universal-mouse-key.md#onmouse)回调读取本地x/y，再结合FrameNode.[getPositionToParent](js-apis-arkui-framenode.md#getpositiontoparent12)()得到的偏移量，调用vp2px将相对坐标转换为像素坐标，更新[MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)的windowX/windowY、displayX/displayY。最后通过rootNode.[postInputEvent](js-apis-arkui-buildernode.md#postinputevent20)(event)将转换后的鼠标事件分发给子节点进行处理。

```
1. import { NodeController, BuilderNode, FrameNode, PromptAction, UIContext, InputEventType } from '@kit.ArkUI';

3. // 自定义参数传递的类
4. class Params {
5. text: string = "this is a text"
6. uiContext: UIContext | null = null
7. }

9. @Builder
10. function ButtonBuilder(params: Params) {
11. Column() {
12. Button(params.text)
13. .borderWidth(2)
14. .align(Alignment.Center)
15. .backgroundColor(Color.Orange)
16. .fontSize(20)
17. .width("45%")
18. .height("30%")
19. .offset({ x: 60, y: 100 })
20. .borderRadius('50%')
21. .onMouse((event) => {
22. let promptAction: PromptAction = params.uiContext!.getPromptAction();
23. promptAction.showToast({
24. message: 'onMouse',
25. duration: 3000
26. });
27. console.info('onMouse')
28. })
29. .onTouch((event) => {
30. let promptAction: PromptAction = params.uiContext!.getPromptAction();
31. promptAction.showToast({
32. message: 'onTouch',
33. duration: 3000
34. });
35. console.info('onTouch')
36. })
37. }
38. .width(500)
39. .height(300)
40. .backgroundColor(Color.Gray)
41. }

43. // 继承NodeController实现自定义UI控制器
44. class MyNodeController extends NodeController {
45. private rootNode: BuilderNode<[Params]> | null = null;
46. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ButtonBuilder);

48. makeNode(uiContext: UIContext): FrameNode | null {
49. this.rootNode = new BuilderNode(uiContext);
50. this.rootNode.build(this.wrapBuilder, { text: "This is a string", uiContext })
51. return this.rootNode.getFrameNode();
52. }

54. postMouseEvent(event: InputEventType, uiContext: UIContext): boolean {
55. if (this.rootNode == null) {
56. return false;
57. }
58. // 读取本地x、y与buildNode相对于父组件的偏移量，转换为像素坐标
59. let node: FrameNode | null = this.rootNode.getFrameNode();
60. let offsetX: number | null | undefined = node?.getPositionToParent().x;
61. let offsetY: number | null | undefined = node?.getPositionToParent().y;

63. let mouseEvent = event as MouseEvent;
64. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
65. mouseEvent.windowX = uiContext.vp2px(offsetX + mouseEvent.x);
66. mouseEvent.windowY = uiContext.vp2px(offsetY + mouseEvent.y);
67. }
68. // 将鼠标事件派发至BuilderNode创建的FrameNode上，result记录派发是否成功
69. let result = this.rootNode.postInputEvent(event);
70. return result;
71. }

73. postTouchEvent(event: InputEventType, uiContext: UIContext): boolean {
74. if (this.rootNode == null) {
75. return false;
76. }
77. // 读取本地x、y与buildNode相对于父组件的偏移量，转换为像素坐标
78. let node: FrameNode | null = this.rootNode.getFrameNode();
79. let offsetX: number | null | undefined = node?.getPositionToParent().x;
80. let offsetY: number | null | undefined = node?.getPositionToParent().y;

82. let touchEvent = event as TouchEvent;
83. let changedTouchLen = touchEvent.changedTouches.length;
84. for (let i = 0; i < changedTouchLen; i++) {
85. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
86. touchEvent.changedTouches[i].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches[i].x);
87. touchEvent.changedTouches[i].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches[i].y);
88. }
89. }
90. let touchesLen = touchEvent.touches.length;
91. for (let i = 0; i < touchesLen; i++) {
92. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
93. touchEvent.touches[i].windowX = uiContext.vp2px(offsetX + touchEvent.touches[i].x);
94. touchEvent.touches[i].windowY = uiContext.vp2px(offsetY + touchEvent.touches[i].y);
95. }
96. }
97. // 将触摸事件派发至BuilderNode创建的FrameNode上，result记录派发是否成功
98. let result = this.rootNode.postInputEvent(event);
99. return result;
100. }
101. }

103. @Entry
104. @Component
105. struct MyComponent {
106. private nodeController: MyNodeController = new MyNodeController();

108. build() {
109. Stack() {
110. NodeContainer(this.nodeController)
111. .height(300)
112. .width(500)
113. Column()
114. .width(500)
115. .height(300)
116. .backgroundColor(Color.Transparent)
117. .onMouse((event) => {
118. if (event != undefined) {
119. this.nodeController.postMouseEvent(event, this.getUIContext());
120. }
121. })
122. .onTouch((event) => {
123. if (event != undefined) {
124. this.nodeController.postTouchEvent(event, this.getUIContext());
125. }
126. })
127. }.offset({ top: 100 })
128. }
129. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bCwnpQaRSLGUX4Bk11AHbA/zh-cn_image_0000002552959436.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=4DF029A5D581CF1557FA5F912FB03F4E70A3C42030F5570B7123173CB9F8362E)

### 示例2（BuilderNode中触摸事件）

该示例演示了在自定义组件中截获触摸事件并对触点坐标进行转换的完整流程。在[onTouch](ts-universal-events-touch.md#ontouch)回调中，遍历[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)的changedTouches和touches数组，对每个触点的x/y加上组件偏移量并调用vp2px转换为像素，更新各自的windowX/windowY、displayX/displayY。最后同样通过rootNode.postInputEvent(event)将转换后的触摸事件分发给子节点处理。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

3. // 自定义传递参数的类
4. class Params {
5. text: string = "this is a text"
6. uiContext: UIContext | null = null
7. }

9. @Builder
10. function ButtonBuilder(params: Params) {
11. Column() {
12. Button(params.text)
13. .borderWidth(2)
14. .align(Alignment.Center)
15. .backgroundColor(Color.Orange)
16. .fontSize(20)
17. .width("45%")
18. .height("30%")
19. .offset({ x: 60, y: 100 })
20. .borderRadius('50%')
21. .onTouch((event) => {
22. let promptAction: PromptAction = params.uiContext!.getPromptAction();
23. promptAction.showToast({
24. message: 'onTouch',
25. duration: 3000
26. });
27. console.info('onTouch')
28. })
29. }
30. .width(500)
31. .height(300)
32. .backgroundColor(Color.Gray)
33. }

35. // 继承NodeController实现自定义UI控制器
36. class MyNodeController extends NodeController {
37. private rootNode: BuilderNode<[Params]> | null = null;
38. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ButtonBuilder);

40. makeNode(uiContext: UIContext): FrameNode | null {
41. this.rootNode = new BuilderNode(uiContext);
42. this.rootNode.build(this.wrapBuilder, { text: "This is a string", uiContext })
43. return this.rootNode.getFrameNode();
44. }

46. postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
47. if (this.rootNode == null) {
48. return false;
49. }
50. // 读取本地x、y与buildNode相对于父组件的偏移量，转换为像素坐标
51. let node: FrameNode | null = this.rootNode.getFrameNode();
52. let offsetX: number | null | undefined = node?.getPositionToParent().x;
53. let offsetY: number | null | undefined = node?.getPositionToParent().y;

55. // 只转发原始事件，不转发鼠标模拟的触摸事件
56. if (event.source == SourceType.TouchScreen) {
57. let touchEvent = event as TouchEvent;
58. let changedTouchLen = touchEvent.changedTouches.length;
59. for (let i = 0; i < changedTouchLen; i++) {
60. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
61. touchEvent.changedTouches[i].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches[i].x);
62. touchEvent.changedTouches[i].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches[i].y);
63. }
64. }
65. let touchesLen = touchEvent.touches.length;
66. for (let i = 0; i < touchesLen; i++) {
67. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
68. touchEvent.touches[i].windowX = uiContext.vp2px(offsetX + touchEvent.touches[i].x);
69. touchEvent.touches[i].windowY = uiContext.vp2px(offsetY + touchEvent.touches[i].y);
70. }
71. }
72. }

74. // 将触摸事件派发至BuilderNode创建的FrameNode上，result记录派发是否成功
75. let result = this.rootNode.postInputEvent(event);
76. return result;
77. }
78. }

80. @Entry
81. @Component
82. struct MyComponent {
83. private nodeController: MyNodeController = new MyNodeController();

85. build() {
86. Stack() {
87. NodeContainer(this.nodeController)
88. .height(300)
89. .width(500)
90. Column()
91. .width(500)
92. .height(300)
93. .backgroundColor(Color.Transparent)
94. .onTouch((event) => {
95. if (event != undefined) {
96. this.nodeController.postInputEvent(event, this.getUIContext());
97. }
98. })
99. }.offset({ top: 100 })
100. }
101. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/qIUVoLxjTiaiak6Hneo2vg/zh-cn_image_0000002583479437.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=9D64FA5241A427C25E89C5B74E15627B6282B88629947D73F2EAD33C42B4D4AF)

### 示例3（BuilderNode中轴事件）

该示例演示了在自定义组件中截获滚轮或触控板轴事件并进行坐标转换的完整流程。在[onAxisEvent](ts-universal-events-axis.md#onaxisevent)回调中，先获取事件的相对x/y，再加上组件偏移量后调用vp2px转换为像素，更新AxisEvent的windowX/windowY、displayX/displayY，最后通过rootNode.postInputEvent(event)将转换后的轴事件分发给子节点进行处理。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

3. // 自定义传递参数的类
4. class Params {
5. text: string = "this is a text"
6. uiContext: UIContext | null = null
7. }

9. @Builder
10. function ButtonBuilder(params: Params) {
11. Column() {
12. Button(params.text)
13. .borderWidth(2)
14. .align(Alignment.Center)
15. .backgroundColor(Color.Orange)
16. .fontSize(20)
17. .width("45%")
18. .height("30%")
19. .offset({ x: 60, y: 100 })
20. .borderRadius('50%')
21. .onAxisEvent((event) => {
22. let promptAction: PromptAction = params.uiContext!.getPromptAction();
23. promptAction.showToast({
24. message: 'onAxisEvent',
25. duration: 3000
26. });
27. console.info('onAxisEvent')
28. })
29. }
30. .width(500)
31. .height(300)
32. .backgroundColor(Color.Gray)
33. }

35. // 继承NodeController实现自定义UI控制器
36. class MyNodeController extends NodeController {
37. private rootNode: BuilderNode<[Params]> | null = null;
38. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ButtonBuilder);

40. makeNode(uiContext: UIContext): FrameNode | null {
41. this.rootNode = new BuilderNode(uiContext);
42. this.rootNode.build(this.wrapBuilder, { text: "This is a string", uiContext })
43. return this.rootNode.getFrameNode();
44. }

46. postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
47. if (this.rootNode == null) {
48. return false;
49. }
50. // 读取本地x、y与buildNode相对于父组件的偏移量，转换为像素坐标
51. let node: FrameNode | null = this.rootNode.getFrameNode();
52. let offsetX: number | null | undefined = node?.getPositionToParent().x;
53. let offsetY: number | null | undefined = node?.getPositionToParent().y;

55. let axisEvent = event as AxisEvent;
56. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
57. axisEvent.windowX = uiContext.vp2px(offsetX + axisEvent.x);
58. axisEvent.windowY = uiContext.vp2px(offsetY + axisEvent.y);
59. }
60. // 将轴事件派发至BuilderNode创建的FrameNode上，result记录派发是否成功
61. let result = this.rootNode.postInputEvent(event);
62. return result;
63. }
64. }

66. @Entry
67. @Component
68. struct MyComponent {
69. private nodeController: MyNodeController = new MyNodeController();

71. build() {
72. Stack() {
73. NodeContainer(this.nodeController)
74. .height(300)
75. .width(500)
76. Column()
77. .width(500)
78. .height(300)
79. .backgroundColor(Color.Transparent)
80. .onAxisEvent((event) => {
81. if (event != undefined) {
82. this.nodeController.postInputEvent(event, this.getUIContext());
83. }
84. })
85. }.offset({ top: 100 })
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/5H90Dh2uTXC4ftthRxlQwg/zh-cn_image_0000002552799788.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=C6E023506502D1851370A98AE43370C25046B8ED1721ADCF6D85CAD0EB2BA277)

### 示例4（BuilderNode共享localStorage）

该示例演示了如何在BuilderNode通过build方法传入外部[localStorage](ts-state-management.md#localstorage9)，此时挂载在BuilderNode的所有自定义组件共享该localStorage。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. // 自定义传递参数的类
4. class Params {
5. text: string = ""

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. let globalBuilderNode: BuilderNode<[Params]> | null = null;

14. @Builder
15. function buildText(params: Params) {
16. Column() {
17. Text('BuildNodeContentArea')
18. .fontSize(25)
19. CustomComp()
20. }
21. }

23. // 继承NodeController实现自定义textNode控制器
24. class TextNodeController extends NodeController {
25. private rootNode: FrameNode | null = null;

27. makeNode(context: UIContext): FrameNode | null {
28. this.rootNode = new FrameNode(context);
29. if (globalBuilderNode === null) {
30. globalBuilderNode = new BuilderNode(context);
31. // 传入外部localStorage，共享给挂载在当前BuilderNode的所有自定义组件
32. globalBuilderNode.build(wrapBuilder<[Params]>(buildText), new Params('builder node text'),
33. { localStorage: localStorage1 })
34. }
35. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
36. return this.rootNode;
37. }
38. }

40. // 创建LocalStorage并设置初始值
41. let localStorage1: LocalStorage = new LocalStorage();
42. localStorage1.setOrCreate('PropA', 'PropA');

44. @Entry(localStorage1)
45. @Component
46. struct Index {
47. private controller: TextNodeController = new TextNodeController();
48. @LocalStorageLink('PropA') PropA: string = 'Hello World';

50. build() {
51. Row() {
52. Column() {
53. Text(this.PropA)
54. NodeContainer(this.controller)
55. Button('changeLocalstorage').onClick(() => {
56. localStorage1.set('PropA', 'AfterChange')
57. })
58. }
59. }
60. }
61. }

63. @Component
64. struct CustomComp {
65. @LocalStorageLink('PropA') PropA: string = 'Hello World';

67. build() {
68. Row() {
69. Column() {
70. Text(this.PropA)
71. }
72. }
73. }
74. }
```

### 示例5（BuilderNode支持内部@Consume接收外部的@Provide数据）

设置BuilderNode的[BuildOptions](js-apis-arkui-buildernode.md#buildoptions12)中enableProvideConsumeCrossing为true，以实现BuilderNode内部自定义组件的@Consume与所在自定义组件的@Provide双向同步。

```
1. import { BuilderNode, NodeContent } from '@kit.ArkUI';

3. // 自定义组件
4. @Component
5. struct ConsumeChild {
6. // 与外部的@Provider装饰的状态变量双向同步
7. @Consume @Watch("ChangeData") message: string = ""

9. ChangeData() {
10. console.info(`ChangeData ${this.message}`);
11. }

13. build() {
14. Column() {
15. Text(this.message)
16. .fontWeight(FontWeight.Bold)
17. .fontSize(20)
18. Button("Click to change message to append C")
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. // 修改Consume的变量
22. this.message = this.message + "C"
23. })
24. }
25. }
26. }

28. @Builder
29. function CreateText(textMessage: string) {
30. Column() {
31. Text(textMessage)
32. .fontWeight(FontWeight.Bold)
33. .fontSize(20)
34. ConsumeChild()
35. }
36. }

38. @Entry
39. @Component
40. struct Index {
41. // 与内部的@Consumer装饰的状态变量双向同步
42. @Provide message: string = 'Hello World';
43. private content: NodeContent = new NodeContent();
44. private builderNode: BuilderNode<[string]> = new BuilderNode<[string]>(this.getUIContext());

46. aboutToAppear(): void {
47. // 设置enableProvideConsumeCrossing为true，支持BuilderNode内部自定义组件ConsumeChild的@Consume变量与其所在页面中的@Provide变量双向同步
48. this.builderNode.build(wrapBuilder(CreateText), "Test Consume", { enableProvideConsumeCrossing: true })
49. this.content.addFrameNode(this.builderNode.getFrameNode())
50. }

52. build() {
53. Column() {
54. Text(this.message)
55. .fontWeight(FontWeight.Bold)
56. .fontSize(20)
57. Button("Click to change message to append I")
58. .fontWeight(FontWeight.Bold)
59. .onClick(() => {
60. this.message = this.message + "I";
61. })
62. Column() {
63. ContentSlot(this.content)
64. }
65. }
66. .height('100%')
67. .width('100%')
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/xG8gpd1bTYSkzYTGDDBG9A/zh-cn_image_0000002583439483.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=00554B5A380810202704309C142CCDC69809A5DBFDCE88396E7AF100FE4EBBAE)

### 示例6（BuilderNode支持内部@Consumer接收外部的@Provider数据）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

设置BuilderNode的[BuildOptions](js-apis-arkui-buildernode.md#buildoptions12)中enableProvideConsumeCrossing为true，以实现BuilderNode内部自定义组件的@Consumer变量与所在自定义组件的@Provider装饰的状态变量双向同步。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. // @Consumer挂载在BuilderNode下
6. addChildChild();
7. }

9. class TextNodeControllerAdd extends NodeController {
10. builderNode: BuilderNode<[]> | null = null;
11. private uiContext: UIContext | null = null;

13. constructor() {
14. super();
15. }

17. makeNode(context: UIContext): FrameNode | null {
18. console.info('TextNodeControllerAdd makeNode');
19. this.builderNode = new BuilderNode(context);
20. // 构建builderNode，enableProvideConsumeCrossing设置为true
21. this.builderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
22. return this.builderNode.getFrameNode();
23. }
24. }

26. @ComponentV2
27. struct addChildChild {
28. @Consumer() content: string = 'default value';

30. @Monitor('content')
31. consumeWatch() {
32. console.info(`Consumer change ${this.content}`);
33. }

35. build() {
36. Column() {
37. Text(`Test: ${this.content}`);
38. Button('change consumer')
39. .onClick(() => {
40. // 修改@Consumer的变量
41. this.content += ' Consumer';
42. })
43. }
44. }
45. }

47. @Entry
48. @ComponentV2
49. struct AddChild {
50. // 与@Consumer装饰的状态变量双向同步
51. @Provider() content: string = 'Index: hello world';

53. @Monitor('content')
54. providerWatch() {
55. console.info(`Provider change ${this.content}`);
56. }

58. controllerIndex: TextNodeControllerAdd = new TextNodeControllerAdd();

60. build() {
61. Column() {
62. Text(`Provider: ${this.content}`)
63. Button('change Provider')
64. .onClick(() => {
65. // 修改@Provider的变量
66. this.content += ' Provider';
67. })
68. // 通过NodeContainer连接BuilderNode节点
69. NodeContainer(this.controllerIndex);
70. }
71. .width('100%')
72. .height('100%')
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/mrSvMDnrTZ2J3nVnO-U7Gw/zh-cn_image_0000002552959438.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=C7EC2E1F6873ADDAC8A4D23E1C0A1F18FF3E5ADADB9EFE5340D8B100A0F9494B)

### 示例7（BuilderNode上下树时的同步关系变化）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

该示例演示了BuilderNode挂载到组件树和从组件树卸载时，@Consumer与@Provider的同步关系变化。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. TestRemove();
6. }

8. let globalBuilderNode: BuilderNode<[]> | null = null;

10. class TextNodeController extends NodeController {
11. private rootNode: FrameNode | null = null;
12. private uiContext: UIContext | null = null;

14. constructor() {
15. super();
16. }

18. makeNode(context: UIContext): FrameNode | null {
19. this.rootNode = new FrameNode(context);
20. this.uiContext = context;
21. return this.rootNode;
22. }

24. addBuilderNode(): void {
25. if (globalBuilderNode === null && this.uiContext) {
26. globalBuilderNode = new BuilderNode(this.uiContext);
27. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
28. }
29. if (this.rootNode && globalBuilderNode) {
30. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
31. }
32. }

34. removeBuilderNode(): void {
35. if (this.rootNode && globalBuilderNode) {
36. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
37. }
38. }

40. disposeNode(): void {
41. if (this.rootNode && globalBuilderNode) {
42. globalBuilderNode.dispose();
43. }
44. }
45. }

47. @Entry
48. @ComponentV2
49. struct RemoChildDisconnectProvider {
50. @Provider() content: string = 'Index: hello world';

52. @Monitor('content')
53. providerWatch() {
54. console.info(`Provider change ${this.content}`);
55. }

57. controllerIndex: TextNodeController = new TextNodeController();

59. build() {
60. Column({ space: 8 }) {
61. Text(`Provider: ${this.content}`)
62. Button('add child')
63. .onClick(() => {
64. this.controllerIndex.addBuilderNode();
65. })

67. Button('remove child')
68. .onClick(() => {
69. this.controllerIndex.removeBuilderNode();
70. })

72. Button('dispose child')
73. .onClick(() => {
74. this.controllerIndex.disposeNode();
75. })

77. Button('change Provider')
78. .onClick(() => {
79. // 修改@Provider的变量
80. this.content += 'Pro';
81. })
82. NodeContainer(this.controllerIndex);
83. }
84. .width('100%')
85. .height('100%')
86. }
87. }

89. @ComponentV2
90. struct TestRemove {
91. @Consumer() content: string = 'default value';

93. @Monitor('content')
94. consumerWatch() {
95. console.info(`Consumer change ${this.content}`);
96. }

98. aboutToDisappear() {
99. console.info(`TestRemove aboutToDisappear`);
100. }

102. build() {
103. Column() {
104. Text(`Consumer ${this.content}`)

106. Button('change content')
107. .onClick(() => {
108. // 修改@Consumer的变量
109. this.content += 'content';
110. })
111. }
112. }
113. }
```

### 示例8（BuilderNode上树后再上另一棵树时的同步关系变化）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

该示例演示了BuilderNode挂载到组件树后，再挂载到另一个组件树时，@Consumer与@Provider的同步关系变化。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. ConsumerChild();
6. }

8. let globalBuilderNode: BuilderNode<[]> | null = null;

10. class TextNodeController extends NodeController {
11. private rootNode: FrameNode | null = null;
12. private uiContext: UIContext | null = null;

14. constructor() {
15. super();
16. }

18. makeNode(context: UIContext): FrameNode | null {
19. this.rootNode = new FrameNode(context);
20. this.uiContext = context;
21. return this.rootNode;
22. }

24. addBuilderNode(): void {
25. if (globalBuilderNode === null && this.uiContext) {
26. globalBuilderNode = new BuilderNode(this.uiContext);
27. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
28. }
29. if (this.rootNode && globalBuilderNode) {
30. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
31. }
32. }

34. removeBuilderNode(): void {
35. if (this.rootNode && globalBuilderNode) {
36. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
37. }
38. }
39. }

41. @Entry
42. @ComponentV2
43. struct AddRemoveAddToAnother {
44. @Provider() content: string = 'Index: hello world';

46. @Monitor('content')
47. providerWatch() {
48. console.info(`Provider change ${this.content}`);
49. }

51. controllerIndex: TextNodeController = new TextNodeController();

53. build() {
54. Column({ space: 8 }) {
55. Text(`Index Provider: ${this.content}`)

57. Button('add child')
58. .onClick(() => {
59. this.controllerIndex.addBuilderNode();
60. })

62. Button('change Index Provide')
63. .onClick(() => {
64. // 修改@Provider的变量
65. this.content += 'Pro';
66. })

68. NodeContainer(this.controllerIndex);
69. ChildHasProvide({ controllerIndex: this.controllerIndex });
70. }
71. .width('100%')
72. .height('100%')
73. }
74. }

76. @ComponentV2
77. struct ChildHasProvide {
78. @Provider('content') content: string = 'Child: hello world';

80. @Monitor('content')
81. providerWatch() {
82. console.info(`Provider change ${this.content}`);
83. }

85. @Param private controllerIndex: TextNodeController | undefined = undefined;
86. controllerIndexChild: TextNodeController = new TextNodeController();

88. build() {
89. Column({ space: 8 }) {
90. Text(`Child Provider: ${this.content}`)

92. Button('change Child Provide')
93. .onClick(() => {
94. // 修改@Provider的变量
95. this.content += 'Pro';
96. })

98. Button('change View')
99. .onClick(() => {
100. this.controllerIndex?.removeBuilderNode();
101. this.controllerIndexChild.addBuilderNode();
102. })
103. NodeContainer(this.controllerIndexChild);
104. }
105. }
106. }

108. @ComponentV2
109. struct ConsumerChild {
110. @Consumer() content: string = 'default value';

112. @Monitor('content')
113. consumerWatch() {
114. console.info(`Consumer change ${this.content}`);
115. }

117. build() {
118. Column() {
119. Text(`Consumer: ${this.content}`)

121. Button('change content')
122. .onClick(() => {
123. // 修改@Consumer的变量
124. this.content += 'content';
125. })
126. }
127. }
128. }
```

### 示例9（BuilderNode互相嵌套的场景下的同步关系变化）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

该示例演示了BuilderNode互相嵌套场景下@Consumer和@Provider的同步关系变化。

```
1. import { BuilderNode, FrameNode, NodeContent, NodeController } from '@kit.ArkUI';

3. let content: NodeContent = new NodeContent();

5. @Builder
6. function buildText() {
7. Column() {
8. BuildNodeToBuildNodeChild().border({ width: 2, color: Color.Pink, radius: 5 });
9. ContentSlot(content);
10. }
11. }

13. @Builder
14. function buildText2() {
15. Column() {
16. BuildNodeToBuildNodeChild().border({ width: 2, color: Color.Pink, radius: 5 });
17. }
18. }

20. let globalBuilderNode: BuilderNode<[]> | null = null;
21. let globalBuilderNode2: BuilderNode<[]> | null = null;

23. class TextNodeControllerAdd extends NodeController {
24. private rootNode: FrameNode | null = null;
25. private uiContext: UIContext | null = null;

27. constructor() {
28. super();
29. }

31. makeNode(context: UIContext): FrameNode | null {
32. this.rootNode = new FrameNode(context);
33. this.uiContext = context;
34. // 仅返回FrameNode，未执行build
35. return this.rootNode;
36. }

38. addBuilderNode(): void {
39. if (globalBuilderNode === null && this.uiContext) {
40. globalBuilderNode = new BuilderNode(this.uiContext);
41. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
42. }
43. if (this.rootNode && globalBuilderNode) {
44. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
45. }
46. }

48. removeBuilderNode(): void {
49. if (this.rootNode && globalBuilderNode) {
50. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
51. }
52. }
53. }

55. @Entry
56. @ComponentV2
57. struct BuildNodeToBuildNode {
58. @Provider() content: string = 'Index: hello world';

60. @Monitor('content')
61. providerWatch() {
62. console.info(`Provider change ${this.content}`);
63. }

65. controllerIndex: TextNodeControllerAdd = new TextNodeControllerAdd();

67. build() {
68. Column({ space: 8 }) {
69. Text(`Provider: ${this.content}`)
70. Button('add child')
71. .onClick(() => {
72. this.controllerIndex.addBuilderNode();
73. })
74. // builderNode嵌套builderNode
75. Button('add to NodeContent')
76. .onClick(() => {
77. globalBuilderNode2 = new BuilderNode(this.getUIContext());
78. globalBuilderNode2.build(wrapBuilder<[]>(buildText2), undefined, { enableProvideConsumeCrossing: true });
79. content.addFrameNode(globalBuilderNode2.getFrameNode());
80. })
81. Button('change Provider')
82. .onClick(() => {
83. // 修改@Provider的变量
84. this.content += 'Pro';
85. })
86. NodeContainer(this.controllerIndex);
87. }
88. .width('100%')
89. .height('100%')
90. }
91. }

93. @ComponentV2
94. struct BuildNodeToBuildNodeChild {
95. // 在未上树的时候，Test组件无View的父亲，该节点为离屏节点。@Consumer找不到对应@Provider，使用默认值
96. @Consumer() content: string = 'default value';

98. @Monitor('content')
99. consumerWatch() {
100. console.info(`Consumer change ${this.content}`);
101. }

103. build() {
104. Column() {
105. Text(`Test: ${this.content}`)

107. Button('change content')
108. .onClick(() => {
109. // 修改@Consumer的变量
110. this.content += 'content';
111. })
112. }
113. }
114. }
```

### 示例10（BuilderNode下的@Consumer所在组件还有其他子组件时的同步关系）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

该示例演示了当@Consumer所在的自定义组件在BuilderNode下且该自定义组件存在子组件时，@Consumer和@Provider之间的同步关系。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. NestedComponentChild();
6. }

8. let globalBuilderNode: BuilderNode<[]> | null = null;

10. class TextNodeController extends NodeController {
11. private rootNode: FrameNode | null = null;
12. private uiContext: UIContext | null = null;

14. constructor() {
15. super();
16. }

18. makeNode(context: UIContext): FrameNode | null {
19. this.rootNode = new FrameNode(context);
20. this.uiContext = context;
21. return this.rootNode;
22. }

24. addBuilderNode(): void {
25. if (globalBuilderNode === null && this.uiContext) {
26. globalBuilderNode = new BuilderNode(this.uiContext);
27. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
28. }
29. if (this.rootNode && globalBuilderNode) {
30. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
31. }
32. }

34. removeBuilderNode(): void {
35. if (this.rootNode && globalBuilderNode) {
36. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
37. }
38. }

40. disposeNode(): void {
41. if (this.rootNode && globalBuilderNode) {
42. globalBuilderNode.dispose();
43. }
44. }
45. }

47. @Entry
48. @ComponentV2
49. struct NestedComponent {
50. @Provider() content: string = 'Index: hello world';

52. @Monitor('content')
53. providerWatch() {
54. console.info(`Provider change ${this.content}`);
55. }

57. controllerIndex: TextNodeController = new TextNodeController();

59. build() {
60. Column({ space: 8 }) {
61. Text(`Provider: ${this.content}`)

63. Button('add child')
64. .onClick(() => {
65. this.controllerIndex.addBuilderNode();
66. })

68. Button('remove child')
69. .onClick(() => {
70. this.controllerIndex.removeBuilderNode();
71. })

73. Button('dispose child')
74. .onClick(() => {
75. this.controllerIndex.disposeNode();
76. })

78. Button('change Provider')
79. .onClick(() => {
80. // 修改@Provider的变量
81. this.content += 'Pro';
82. })
83. NodeContainer(this.controllerIndex);
84. }
85. .width('100%')
86. .height('100%')
87. }
88. }

90. @ComponentV2
91. struct NestedComponentChild {
92. @Consumer() content: string = 'default value';

94. @Monitor('content')
95. consumerWatch() {
96. console.info(`Consumer change ${this.content}`);
97. }

99. aboutToDisappear() {
100. console.info(`TestRemove aboutToDisappear`);
101. }

103. build() {
104. Column() {
105. Text(`Consumer: ${this.content}`)

107. Button('change content')
108. .onClick(() => {
109. // 修改@Consumer的变量
110. this.content += 'content';
111. })
112. NestedComponentChildChld({ content: this.content, addContent: () => this.content += 'content' });
113. }
114. }
115. }

117. @ComponentV2
118. struct NestedComponentChildChld {
119. // 在未上树的时候，Test组件无View的父亲，该节点为离屏节点。@Consumer找不到对应@Provider，使用默认值
120. @Param @Require content: string;
121. @Event addContent: () => void;

123. @Monitor('content')
124. paramEventWatch() {
125. console.info(`ParamEvent change ${this.content}`);
126. }

128. build() {
129. Column() {
130. Text(`Param: ${this.content}`)

132. Button('change content')
133. .onClick(() => {
134. this.addContent();
135. })
136. }
137. }
138. }
```

### 示例11（组件树为@Provider-@Consumer-BuilderNode-@Consumer时的同步关系）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

该示例演示了组件树为@Provider-@Consumer-BuilderNode-@Consumer的情况时，@Consumer和@Provider之间的同步关系。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @ObservedV2
4. class Ob {
5. @Trace a: number = 0;
6. }

8. @Builder
9. function buildText() {
10. NestedComponentChild();
11. }

13. let globalBuilderNode: BuilderNode<[]> | null = null;

15. class TextNodeController extends NodeController {
16. private rootNode: FrameNode | null = null;
17. private uiContext: UIContext | null = null;

19. constructor() {
20. super();
21. }

23. makeNode(context: UIContext): FrameNode | null {
24. this.rootNode = new FrameNode(context);
25. this.uiContext = context;
26. return this.rootNode;
27. }

29. addBuilderNode(): void {
30. if (globalBuilderNode === null && this.uiContext) {
31. globalBuilderNode = new BuilderNode(this.uiContext);
32. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
33. }
34. if (this.rootNode && globalBuilderNode) {
35. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
36. }
37. }

39. removeBuilderNode(): void {
40. if (this.rootNode && globalBuilderNode) {
41. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
42. }
43. }

45. disposeNode(): void {
46. if (this.rootNode && globalBuilderNode) {
47. globalBuilderNode.dispose();
48. }
49. }
50. }

52. @Entry
53. @ComponentV2
54. // 与@Consumer装饰的状态变量双向同步
55. struct ProvideConsumeBuilderNodeConsume {
56. @Provider() content: Ob = new Ob();

58. @Monitor('content')
59. providerWatch() {
60. console.info(`Provider change ${this.content.a}`);
61. }

63. build() {
64. Column({ space: 8 }) {
65. Text(`Provide: ${this.content.a}`)

67. Button('Change Provider a')
68. .onClick(() => {
69. this.content.a++;
70. })
71. Button('Change Provider Whole')
72. .onClick(() => {
73. this.content.a = 0;
74. })
75. ProvideConsumeBuilderNodeConsumeChild();
76. }
77. .width('100%')
78. .height('100%')
79. }
80. }

82. // 组件树为@Provider-@Consumer-BuilderNode-@Consumer结构
83. @ComponentV2
84. struct ProvideConsumeBuilderNodeConsumeChild {
85. @Consumer() content: Ob = new Ob();

87. @Monitor('content')
88. consumerWatch() {
89. console.info(`ProvideConsumeBuilderNodeConsumeChild change ${this.content.a}`);
90. }

92. controllerIndex: TextNodeController = new TextNodeController();

94. build() {
95. Column({ space: 8 }) {
96. Text(`Consumer: ${this.content.a}`)
97. Button('add child')
98. .onClick(() => {
99. this.controllerIndex.addBuilderNode();
100. })

102. Button('remove child')
103. .onClick(() => {
104. this.controllerIndex.removeBuilderNode();
105. })

107. Button('dispose child')
108. .onClick(() => {
109. this.controllerIndex.disposeNode();
110. })

112. Button('change consumer a')
113. .onClick(() => {
114. this.content.a++;
115. })
116. Button('change consumer whole')
117. .onClick(() => {
118. this.content.a = 0;
119. })
120. NodeContainer(this.controllerIndex);
121. }
122. .width('100%')
123. .height('100%')
124. }
125. }

127. @ComponentV2
128. struct NestedComponentChild {
129. @Consumer() content: Ob = new Ob();

131. @Monitor('content')
132. consumer1Watch() {
133. console.info(`Consumer change ${this.content.a}`);
134. }

136. aboutToDisappear() {
137. console.info(`TestRemove aboutToDisappear`);
138. }

140. build() {
141. Column({ space: 8 }) {
142. Text(`Consumer under builder node: ${this.content.a}`)

144. Button('Consumer change content')
145. .onClick(() => {
146. this.content.a++;
147. })
148. }
149. }
150. }
```

### 示例12（组件树为@Provider-BuilderNode-@Provider-@Consumer时的同步关系）

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

该示例演示了组件树为@Provider-BuilderNode-@Provider-@Consumer的情况时，@Consumer和@Provider之间的同步关系。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @ObservedV2
4. class Ob {
5. @Trace a: number = 0;
6. }

8. @Builder
9. function buildText() {
10. Provider2();
11. }

13. let globalBuilderNode: BuilderNode<[]> | null = null;

15. class TextNodeController extends NodeController {
16. private rootNode: FrameNode | null = null;
17. private uiContext: UIContext | null = null;

19. constructor() {
20. super();
21. }

23. makeNode(context: UIContext): FrameNode | null {
24. this.rootNode = new FrameNode(context);
25. this.uiContext = context;
26. return this.rootNode;
27. }

29. addBuilderNode(): void {
30. if (globalBuilderNode === null && this.uiContext) {
31. globalBuilderNode = new BuilderNode(this.uiContext);
32. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
33. }
34. if (this.rootNode && globalBuilderNode) {
35. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
36. }
37. }

39. removeBuilderNode(): void {
40. if (this.rootNode && globalBuilderNode) {
41. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
42. }
43. }

45. disposeNode(): void {
46. if (this.rootNode && globalBuilderNode) {
47. globalBuilderNode.dispose();
48. }
49. }
50. }

52. // 组件树为@Provider-BuilderNode-@Provider-@Consumer结构
53. @Entry
54. @ComponentV2
55. struct Provider1 {
56. // 与@Consumer装饰的状态变量双向同步
57. @Provider() content: Ob = new Ob();

59. @Monitor('content')
60. providerWatch() {
61. console.info(`Provider change ${this.content.a}`);
62. }

64. controllerIndex: TextNodeController = new TextNodeController();

66. build() {
67. Column({ space: 8 }) {
68. Text(`Provider1: ${this.content.a}`)

70. Button('Change Provider1 a')
71. .onClick(() => {
72. this.content.a++;
73. })
74. Button('Change Provider1 Whole')
75. .onClick(() => {
76. this.content.a = 0;
77. })
78. Button('add child')
79. .onClick(() => {
80. this.controllerIndex.addBuilderNode();
81. })

83. Button('remove child')
84. .onClick(() => {
85. this.controllerIndex.removeBuilderNode();
86. })

88. Button('dispose child')
89. .onClick(() => {
90. this.controllerIndex.disposeNode();
91. })
92. NodeContainer(this.controllerIndex);
93. }
94. .width('100%')
95. .height('100%')
96. }
97. }

99. @ComponentV2
100. struct Provider2 {
101. @Provider() content: Ob = new Ob();

103. @Monitor('content')
104. consumerWatch() {
105. console.info(`Provider2 change ${this.content.a}`);
106. }

108. controllerIndex: TextNodeController = new TextNodeController();

110. build() {
111. Column() {
112. Text(`Provider2: ${this.content.a}`)

114. Button('change Provider2 a')
115. .onClick(() => {
116. this.content.a++;
117. })
118. Button('change Provider2 whole')
119. .onClick(() => {
120. this.content.a = 0;
121. })
122. defaultConsumer();
123. }
124. .width('100%')
125. .height('100%')
126. }
127. }

129. @ComponentV2
130. struct defaultConsumer {
131. @Consumer() content: Ob = new Ob();

133. @Monitor('content')
134. consumer1Watch() {
135. console.info(`Consumer change ${this.content.a}`);
136. }

138. aboutToDisappear() {
139. console.info(`TestRemove aboutToDisappear`);
140. }

142. build() {
143. Column() {
144. Text(`Consumer under builder node:: ${this.content.a}`)

146. Button('Consumer change ++')
147. .onClick(() => {
148. this.content.a++;
149. })
150. }
151. }
152. }
```

### 示例13（ReactiveBuilderNode中鼠标事件）

从API version 22版本开始支持。

该示例演示了在自定义组件中截获鼠标事件并进行坐标转换的完整流程。组件通过[onMouse](ts-universal-mouse-key.md#onmouse)回调读取本地x/y坐标，再结合FrameNode.[getPositionToParent](js-apis-arkui-framenode.md#getpositiontoparent12)()得到的偏移量，调用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)将相对坐标转换为像素坐标，更新[MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)的windowX/windowY、displayX/displayY。最后通过rootNode.[postInputEvent](js-apis-arkui-buildernode.md#postinputevent20)将转换后的鼠标事件分发给子节点进行处理。

```
1. import { NodeController, ReactiveBuilderNode, FrameNode, PromptAction, UIContext, InputEventType } from '@kit.ArkUI';

3. @Builder
4. function ButtonBuilder(text: string, uiContext: UIContext) {
5. Column() {
6. Button(text)
7. .borderWidth(2)
8. .align(Alignment.Center)
9. .backgroundColor(Color.Orange)
10. .fontSize(15)
11. .width('45%')
12. .height('30%')
13. .offset({ y: 70 })
14. // 鼠标事件处理
15. .onMouse((event) => {
16. let promptAction: PromptAction = uiContext!.getPromptAction();
17. promptAction.showToast({
18. message: 'onMouse',
19. duration: 3000
20. });
21. console.info('onMouse')
22. })
23. // 触摸事件处理
24. .onTouch((event) => {
25. let promptAction: PromptAction = uiContext!.getPromptAction();
26. promptAction.showToast({
27. message: 'onTouch',
28. duration: 3000
29. });
30. console.info('onTouch')
31. })
32. }
33. .width(500)
34. .height(200)
35. .backgroundColor(Color.Gray)
36. }

38. // 继承NodeController实现自定义UI控制器
39. class MyNodeController extends NodeController {
40. private rootNode: ReactiveBuilderNode<[text: string, uiContext: UIContext]> | null = null;
41. private wrapBuilder: WrappedBuilder<[text: string, uiContext: UIContext]> = wrapBuilder(ButtonBuilder);

43. makeNode(uiContext: UIContext): FrameNode | null {
44. this.rootNode = new ReactiveBuilderNode(uiContext);
45. this.rootNode.build(this.wrapBuilder, {}, 'onMouse', uiContext)
46. return this.rootNode.getFrameNode();
47. }

49. postMouseEvent(event: InputEventType, uiContext: UIContext): boolean {
50. if (this.rootNode == null) {
51. return false;
52. }
53. let node: FrameNode | null = this.rootNode.getFrameNode();
54. // 获取节点相对于父组件的偏移量
55. let offsetX: number | null | undefined = node?.getPositionToParent().x;
56. let offsetY: number | null | undefined = node?.getPositionToParent().y;

58. let mouseEvent = event as MouseEvent;
59. // 坐标转换：将事件坐标转换为节点坐标系
60. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
61. mouseEvent.windowX = uiContext.vp2px(offsetX + mouseEvent.x);
62. mouseEvent.windowY = uiContext.vp2px(offsetY + mouseEvent.y);
63. }
64. // 调用postInputEvent将转换后的事件传递给ReactiveBuilderNode
65. let result = this.rootNode.postInputEvent(event);
66. return result;
67. }

69. // 处理触摸事件的方法
70. postTouchEvent(event: InputEventType, uiContext: UIContext): boolean {
71. if (this.rootNode == null) {
72. return false;
73. }
74. let node: FrameNode | null = this.rootNode.getFrameNode();
75. // 获取节点相对于父组件的偏移量
76. let offsetX: number | null | undefined = node?.getPositionToParent().x;
77. let offsetY: number | null | undefined = node?.getPositionToParent().y;

79. let touchEvent = event as TouchEvent;
80. // 转换changedTouches数组中的所有触摸点坐标
81. let changedTouchLen = touchEvent.changedTouches.length;
82. for (let i = 0; i < changedTouchLen; i++) {
83. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
84. touchEvent.changedTouches[i].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches[i].x);
85. touchEvent.changedTouches[i].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches[i].y);
86. }
87. }
88. // 转换touches数组中的所有触摸点坐标
89. let touchesLen = touchEvent.touches.length;
90. for (let i = 0; i < touchesLen; i++) {
91. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
92. touchEvent.touches[i].windowX = uiContext.vp2px(offsetX + touchEvent.touches[i].x);
93. touchEvent.touches[i].windowY = uiContext.vp2px(offsetY + touchEvent.touches[i].y);
94. }
95. }
96. // 调用postInputEvent将转换后的事件传递给ReactiveBuilderNode
97. let result = this.rootNode.postInputEvent(event);
98. return result;
99. }
100. }

102. @Entry
103. @Component
104. struct MyComponent {
105. private nodeController: MyNodeController = new MyNodeController();

107. build() {
108. Stack() {
109. NodeContainer(this.nodeController)
110. .height(300)
111. .width(500)
112. Column()
113. .width(500)
114. .height(300)
115. .margin({ top: 500 })
116. .backgroundColor(Color.Transparent)
117. // 捕获鼠标事件并传递给自定义节点
118. .onMouse((event) => {
119. if (event != undefined) {
120. this.nodeController.postMouseEvent(event, this.getUIContext());
121. }
122. })
123. // 捕获触摸事件并传递给自定义节点
124. .onTouch((event) => {
125. if (event != undefined) {
126. this.nodeController.postTouchEvent(event, this.getUIContext());
127. }
128. })
129. }.offset({ top: 180 })
130. }
131. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/j9FCch2ESgOH2vPkr8sp3g/zh-cn_image_0000002583479439.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=219ADA31AF4C3DBCEB87143E3C4917A331452122A2080AE887F7CEDCC98246FF)

### 示例14（ReactiveBuilderNode中触摸事件）

从API version 22版本开始支持。

该示例演示了在自定义组件中截获触摸事件并对触点坐标进行转换的完整流程。在[onTouch](ts-universal-events-touch.md#ontouch)回调中，遍历[TouchEvent](ts-universal-events-touch.md#touchevent对象说明)的changedTouches和touches数组，对每个触点的x/y坐标加上组件偏移量并调用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)转换为像素，更新各自的windowX/windowY、displayX/displayY。最后同样通过rootNode.[postInputEvent](js-apis-arkui-buildernode.md#postinputevent20)将转换后的触摸事件分发给子节点处理。

```
1. import { NodeController, ReactiveBuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

3. @Builder
4. function ButtonBuilder(text: string, uiContext: UIContext) {
5. Column() {
6. Button(text)
7. .borderWidth(2)
8. .align(Alignment.Center)
9. .backgroundColor(Color.Orange)
10. .fontSize(15)
11. .width('45%')
12. .height('30%')
13. .offset({ y: 70 })
14. // 触摸事件处理
15. .onTouch((event) => {
16. let promptAction: PromptAction = uiContext!.getPromptAction();
17. promptAction.showToast({
18. message: 'onTouch',
19. duration: 3000
20. });
21. console.info('onTouch')
22. })
23. }
24. .width(500)
25. .height(200)
26. .backgroundColor(Color.Gray)
27. }

29. class MyNodeController extends NodeController {
30. private rootNode: ReactiveBuilderNode<[text: string, uiContext: UIContext]> | null = null;
31. private wrapBuilder: WrappedBuilder<[text: string, uiContext: UIContext]> =
32. wrapBuilder<[text: string, uiContext: UIContext]>(ButtonBuilder);

34. makeNode(uiContext: UIContext): FrameNode | null {
35. this.rootNode = new ReactiveBuilderNode(uiContext);
36. // 构建ReactiveBuilderNode，传递按钮文本和UI上下文
37. this.rootNode.build(this.wrapBuilder, {}, 'onTouch', uiContext)
38. return this.rootNode.getFrameNode();
39. }

41. postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
42. if (this.rootNode == null) {
43. return false;
44. }
45. let node: FrameNode | null = this.rootNode.getFrameNode();
46. // 获取节点相对于父组件的偏移量
47. let offsetX: number | null | undefined = node?.getPositionToParent().x;
48. let offsetY: number | null | undefined = node?.getPositionToParent().y;

50. if (event.source == SourceType.TouchScreen) {
51. let touchEvent = event as TouchEvent;
52. // 转换changedTouches数组中的所有触摸点坐标
53. let changedTouchLen = touchEvent.changedTouches.length;
54. for (let i = 0; i < changedTouchLen; i++) {
55. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
56. touchEvent.changedTouches[i].windowX = uiContext.vp2px(offsetX + touchEvent.changedTouches[i].x);
57. touchEvent.changedTouches[i].windowY = uiContext.vp2px(offsetY + touchEvent.changedTouches[i].y);
58. }
59. }
60. // 转换touches数组中的所有触摸点坐标
61. let touchesLen = touchEvent.touches.length;
62. for (let i = 0; i < touchesLen; i++) {
63. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
64. touchEvent.touches[i].windowX = uiContext.vp2px(offsetX + touchEvent.touches[i].x);
65. touchEvent.touches[i].windowY = uiContext.vp2px(offsetY + touchEvent.touches[i].y);
66. }
67. }
68. }

70. // 调用postInputEvent将转换后的事件传递给ReactiveBuilderNode
71. let result = this.rootNode.postInputEvent(event);
72. return result;
73. }
74. }

76. @Entry
77. @Component
78. struct MyComponent {
79. private nodeController: MyNodeController = new MyNodeController();

81. build() {
82. Stack() {
83. NodeContainer(this.nodeController)
84. .height(300)
85. .width(500)
86. Column()
87. .width(500)
88. .height(300)
89. .margin({ top: 600 })
90. .backgroundColor(Color.Transparent)
91. // 捕获触摸事件并传递给自定义节点
92. .onTouch((event) => {
93. if (event != undefined) {
94. this.nodeController.postInputEvent(event, this.getUIContext());
95. }
96. })
97. }.offset({ top: 180 })
98. }
99. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/H0lYhx5qT9mueXRTheIX_g/zh-cn_image_0000002552799790.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=CDEC9C866510227DE783266D45F4844AC5C1E06F76E84E10CB831AC6B967DC80)

### 示例15（ReactiveBuilderNode中轴事件）

从API version 22版本开始支持。

该示例演示了在自定义组件中截获滚轮或触控板轴事件并进行坐标转换的完整流程。在[onAxisEvent](ts-universal-events-axis.md#onaxisevent)回调中，先获取事件的相对x/y坐标，再加上组件偏移量后调用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)转换为像素，更新AxisEvent的windowX/windowY、displayX/displayY，最后通过rootNode.[postInputEvent](js-apis-arkui-buildernode.md#postinputevent20)将转换后的轴事件分发给子节点进行处理。

```
1. import { NodeController, ReactiveBuilderNode, FrameNode, UIContext, PromptAction, InputEventType } from '@kit.ArkUI';

3. @Builder
4. function ButtonBuilder(text: string, uiContext: UIContext) {
5. Column() {
6. Button(text)
7. .borderWidth(2)
8. .align(Alignment.Center)
9. .backgroundColor(Color.Orange)
10. .fontSize(15)
11. .width("45%")
12. .height("30%")
13. .offset({ y: 80 })
14. .onAxisEvent((event) => {
15. let promptAction: PromptAction = uiContext!.getPromptAction();
16. promptAction.showToast({
17. message: 'onAxisEvent', // 显示轴事件触发提示
18. duration: 3000
19. });
20. console.info('onAxisEvent')
21. })
22. }
23. .width(500)
24. .height(200)
25. .backgroundColor(Color.Gray)
26. }

28. // 继承NodeController实现自定义UI控制器
29. class MyNodeController extends NodeController {
30. private rootNode: ReactiveBuilderNode<[text: string, uiContext: UIContext]> | null = null;
31. private wrapBuilder: WrappedBuilder<[text: string, uiContext: UIContext]> =
32. wrapBuilder<[text: string, uiContext: UIContext]>(ButtonBuilder);

34. makeNode(uiContext: UIContext): FrameNode | null {
35. this.rootNode = new ReactiveBuilderNode(uiContext);
36. // 构建ReactiveBuilderNode，传递按钮文本和UI上下文
37. this.rootNode.build(this.wrapBuilder, {}, 'onAxisEvent', uiContext)
38. return this.rootNode.getFrameNode();
39. }

41. // 轴事件处理方法
42. postInputEvent(event: InputEventType, uiContext: UIContext): boolean {
43. if (this.rootNode == null) {
44. return false;
45. }
46. // 读取本地x、y与buildNode相对于父组件的偏移量，转换为像素坐标
47. let node: FrameNode | null = this.rootNode.getFrameNode();
48. let offsetX: number | null | undefined = node?.getPositionToParent().x;
49. let offsetY: number | null | undefined = node?.getPositionToParent().y;

51. let axisEvent = event as AxisEvent;
52. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
53. axisEvent.windowX = uiContext.vp2px(offsetX + axisEvent.x);
54. axisEvent.windowY = uiContext.vp2px(offsetY + axisEvent.y);
55. }
56. // 调用postInputEvent将转换后的事件传递给ReactiveBuilderNode
57. let result = this.rootNode.postInputEvent(event);
58. return result;
59. }
60. }

62. @Entry
63. @Component
64. struct MyComponent {
65. private nodeController: MyNodeController = new MyNodeController();

67. build() {
68. Stack() {
69. NodeContainer(this.nodeController)
70. .height(300)
71. .width(500)
72. Column()
73. .width(500)
74. .height(300)
75. .margin({ top: 600 })
76. .backgroundColor(Color.Transparent)
77. // 捕获轴事件并传递给自定义节点
78. .onAxisEvent((event) => {
79. if (event != undefined) {
80. // 调用轴事件处理方法
81. this.nodeController.postInputEvent(event, this.getUIContext());
82. }
83. })
84. }.offset({ top: 180 })
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/OCina5zlQ0WGn6zB9Rg1Zg/zh-cn_image_0000002583439485.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000033Z&HW-CC-Expire=86400&HW-CC-Sign=7EF4C4A7BDD3F3DB5183777493AF2EFB3E2EB08415D9AF378308114D0A2D605E)
