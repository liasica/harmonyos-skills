---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-same-layer
title: 同层渲染
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 同层渲染
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24a527b76f5f0285561e9fd57dc3a145d4f7a884e00478cde336916f6c15b70d
---

在系统中，应用可以使用Web组件加载Web网页。当非系统框架的UI组件功能或性能不如系统组件时，可使用同层渲染技术，通过ArkUI组件渲染这些组件（简称为同层组件）。

## 使用场景

### Web网页

小程序的地图组件，可以使用ArkUI的XComponent组件渲染来提升性能。小程序的输入框组件，可以使用ArkUI的TextInput组件渲染，达到与系统应用一致的输入体验。

* 在网页侧，应用开发者可将<embed>、<object>的网页UI组件（简称为同层标签），按一定规则进行同层渲染，详细规格见同层渲染规格小节。
* 在应用侧，应用开发者可以通过Web组件的同层渲染事件上报接口，感知到H5同层标签的生命周期以及输入事件，进行同层渲染组件的相应业务逻辑处理。
* 在应用侧，应用开发者可以使用ArkUI的NodeContainer等接口，构建H5同层标签对应的同层渲染组件。可支持同层渲染的ArkUI常用组件包括：[TextInput](../harmonyos-references/ts-basic-components-textinput.md), [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md), [Canvas](../harmonyos-references/ts-components-canvas-canvas.md), [Video](../harmonyos-references/ts-media-components-video.md), [Web](../harmonyos-references/arkts-basic-components-web.md)。具体规格可参见[同层渲染规格小节](web-same-layer.md#规格约束)。

### 三方UI框架

Flutter提供了PlatformView与Texture抽象组件，这些组件可使用系统组件渲染，用于支持Flutter组件功能不足的部分。Weex2.0框架的Camera、Video和Canvas组件可以使用系统组件渲染，以增强功能和性能。

* 在三方框架页面侧，由于Flutter、Weex等三方框架不在操作系统范围内，本文不列举可被同层渲染的三方框架UI组件的范围与使用方式。
* 在应用侧，应用开发者可以使用ArkUI的NodeContainer等接口，构建三方框架同层标签对应的同层渲染组件。可支持同层渲染的ArkUI常用组件包括：[TextInput](../harmonyos-references/ts-basic-components-textinput.md), [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md), [Canvas](../harmonyos-references/ts-components-canvas-canvas.md), [Video](../harmonyos-references/ts-media-components-video.md), [Web](../harmonyos-references/arkts-basic-components-web.md)。具体规格可参见[同层渲染规格](web-same-layer.md#规格约束)。

## 整体架构

ArkWeb同层渲染特性主要提供两种能力：同层标签生命周期和事件命中转发处理。

同层标签生命周期主要关联前端标签（<embed>/<object>），同时命中到同层标签的事件会被上报到开发者侧，由开发者分发到对应组件树。整体框架如下图所示：

**图1** 同层渲染整体架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Lgb6nbSCT0ehjkXhp4jhCw/zh-cn_image_0000002589244541.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=FE60C24109ECC321D068447CCF6916579C6F8E8BA04309CABED6595DCB3C179C)

## 规格约束

### 可被同层渲染的ArkUI组件

以下规格对Web网页和三方框架场景均生效。

**支持的组件范围:**

* 基础组件：[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md), [Blank](../harmonyos-references/ts-basic-components-blank.md), [Button](../harmonyos-references/ts-basic-components-button.md), [CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md), [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md), [CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md), [ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md), [DataPanel](../harmonyos-references/ts-basic-components-datapanel.md), [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md), [Divider](../harmonyos-references/ts-basic-components-divider.md), [Gauge](../harmonyos-references/ts-basic-components-gauge.md), [Hyperlink](../harmonyos-references/ts-container-hyperlink.md), [Image](../harmonyos-references/ts-basic-components-image.md), [ImageAnimator](../harmonyos-references/ts-basic-components-imageanimator.md), [ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md), [LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md), [Marquee](../harmonyos-references/ts-basic-components-marquee.md), [PatternLock](../harmonyos-references/ts-basic-components-patternlock.md), [Progress](../harmonyos-references/ts-basic-components-progress.md), [QRCode](../harmonyos-references/ts-basic-components-qrcode.md), [Radio](../harmonyos-references/ts-basic-components-radio.md), [Rating](../harmonyos-references/ts-basic-components-rating.md), [Refresh](../harmonyos-references/ts-container-refresh.md), [ScrollBar](../harmonyos-references/ts-container-scroll.md), [Search](../harmonyos-references/ts-basic-components-search.md), [Span](../harmonyos-references/ts-basic-components-span.md), [Select](../harmonyos-references/ts-basic-components-select.md), [Slider](../harmonyos-references/ts-basic-components-slider.md), [Text](../harmonyos-references/ts-basic-components-text.md), [TextArea](../harmonyos-references/ts-basic-components-textarea.md), [TextClock](../harmonyos-references/ts-basic-components-textclock.md), [TextInput](../harmonyos-references/ts-basic-components-textinput.md), [TextPicker](../harmonyos-references/ts-basic-components-textpicker.md), [TextTimer](../harmonyos-references/ts-basic-components-texttimer.md), [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md), [Toggle](../harmonyos-references/ts-basic-components-toggle.md)
* 容器类组件：[Badge](../harmonyos-references/ts-container-badge.md), [Column](../harmonyos-references/ts-container-column.md), [ColumnSplit](../harmonyos-references/ts-container-columnsplit.md), [Counter](../harmonyos-references/ts-container-counter.md), [Flex](../harmonyos-references/ts-container-flex.md), [GridCol](../harmonyos-references/ts-container-gridcol.md), [GridRow](../harmonyos-references/ts-container-gridrow.md), [Grid](../harmonyos-references/ts-container-grid.md), [GridItem](../harmonyos-references/ts-container-griditem.md)，[List](../harmonyos-references/ts-container-list.md), [ListItem](../harmonyos-references/ts-container-listitem.md), [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md), [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md), [Row](../harmonyos-references/ts-container-row.md), [RowSplit](../harmonyos-references/ts-container-rowsplit.md), [Scroll](../harmonyos-references/ts-container-scroll.md), [Stack](../harmonyos-references/ts-container-stack.md), [Swiper](../harmonyos-references/ts-container-swiper.md), [Tabs](../harmonyos-references/ts-container-tabs.md), [TabContent](../harmonyos-references/ts-container-tabcontent.md), [NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md), [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md), [Stepper](../harmonyos-references/ts-basic-components-stepper.md), [StepperItem](../harmonyos-references/ts-basic-components-stepperitem.md), [WaterFlow](../harmonyos-references/ts-container-waterflow.md), [FlowItem](../harmonyos-references/ts-container-flowitem.md)
* 自绘制类组件：[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md), [Canvas](../harmonyos-references/ts-components-canvas-canvas.md), [Video](../harmonyos-references/ts-media-components-video.md), [Web](../harmonyos-references/arkts-basic-components-web.md)
* 命令式自定义绘制节点：[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md), [ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md), [ContentSlot](../harmonyos-references/ts-components-contentslot.md), [FrameNode](../harmonyos-references/js-apis-arkui-framenode.md), [Graphics](../harmonyos-references/js-apis-arkui-graphics.md), [NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md), [RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md), [XComponentNode](../harmonyos-references/js-apis-arkui-xcomponentnode.md), [AttributeUpdater](../harmonyos-references/js-apis-arkui-attributeupdater.md), [CAPI](../harmonyos-references/capi-arkui-nativemodule.md)（支持同层渲染的组件范围同ArkTS）

**支持的组件通用属性与事件:**

* 不支持的通用属性：[分布式迁移标识](../harmonyos-references/ts-universal-attributes-restoreid.md)，[特效绘制合并](../harmonyos-references/ts-universal-attributes-use-effect.md)。
* 其他未明确标注不支持的属性与事件及组件能力，均默认支持。

### Web网页的同层渲染标签

此规格仅针对Web网页，不适用于三方框架场景。

如果应用需要在Web组件加载的网页中使用同层渲染，需要按照以下规格将网页中的<embed>、<object>标签指定为同层渲染组件。

**支持的H5标签：**

* 支持<embed>标签：在开启同层渲染后，仅支持type类型为native前缀的标签识别为同层组件，不支持自定义属性。
* 支持<object>标签：在开启同层渲染后，支持将非标准MIME type的object标签识别为同层组件，支持通过param/value的自定义属性解析。
* 不支持W3C规范标准标签（如<input>、<video>）定义为同层标签。
* 不支持同时配置<object>标签和<embed>标签作为同层标签。
* 标签类型只支持英文字符，不区分大小写。

**同层标签支持的css属性：**

display，position，z-index，visibility，opacity, background-color，background-image，width，height，padding，padding-left，padding-top，padding-right，padding-bottom，margin，margin-left，margin-top，margin-right，margin-bottom，border-width，border-style，border-color，border-left-width，border-left-style，border-left-color，border-top-width，border-top-style，border-top-color，border-right-width，border-right-style，border-right-color，border-bottom-width，border-bottom-style，border-bottom-color，border-left，border-right，border-top，border-bottom，border，border-top-left-radius，border-top-right-radius，border-bottom-left-radius，border-bottom-right-radius，border-radius，transition，transform（仅支持translate/scale，scale对应参数只支持大于等于0的值）

除上面支持的css属性范围，其他的css属性均不保证符合预期，比如transform属性中的rotate，skew等。

**同层标签的生命周期管理：**

当同层标签生命周期变化时触发[onNativeEmbedLifecycleChange()](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedlifecyclechange11)回调。

* 支持创建、销毁、位置宽高变化。
* 支持同层组件所在Web页面进入前进后退缓存。

**同层标签的输入事件分发处理：**

* 支持触摸事件TouchEvent的DOWN/UP/MOVE/CANCEL。支持[配置触摸事件消费结果](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedgestureevent11)，默认为应用侧消费。
* 不支持同层标签所在的应用页面缩放和[initialScale](../harmonyos-references/arkts-basic-components-web-attributes.md#initialscale9)、[zoom](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoom)、[zoomIn](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomin)、[zoomOut](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomout)等缩放接口。
* 暂不支持鼠标、键盘、触摸板事件上报。
* 支持默认将鼠标和触摸板左键事件（MousePress/MouseRelease/MouseMOVE）转换为触摸事件（TouchDOWN/TouchUP/TouchMOVE）上报。

**同层标签的可见状态变化：**

当同层标签可见状态变化时触发[onNativeEmbedVisibilityChange](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedvisibilitychange12)回调。

* 支持同层标签相对于视口的可见状态上报。
* 默认不支持由于同层标签CSS样式或尺寸变化导致的可见状态变化上报，具体规格参考[onNativeEmbedVisibilityChange](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedvisibilitychange12)。

**同层渲染<object>标签内嵌param元素状态变化：**

当同层渲染<object>内嵌标签param元素变化时触发[onNativeEmbedObjectParamChange()](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedobjectparamchange21)回调。

* 支持上报param元素的增加、修改、删除三种状态变化。
* 接口每次最多上报500个param元素变化信息，超出部分将分多次上报。
* 详细上报信息参考[NativeEmbedParamDataInfo](../harmonyos-references/arkts-basic-components-web-i.md#nativeembedparamdatainfo21)。

**约束限制：**

* Web页面内同层标签数量应控制在5个以内。超过5个，渲染性能将会下降。
* 受GPU限制，同层标签最大高度不超过8000px，最大纹理大小为8000px。
* 开启同层渲染后，Web组件打开的所有Web页面将不支持同步渲染模式[RenderMode](../harmonyos-references/arkts-basic-components-web-e.md#rendermode12)。
* Video组件：在非全屏Video变为全屏时，Video组件变为非纹理导出模式，视频播放状态保持延续；恢复为非全屏时，变为纹理导出模式，视频播放状态保持延续。
* Web组件：仅支持一层同层渲染嵌套，不支持多层同层渲染嵌套。输入事件只支持滑动、点击、长按，不支持拖拽、旋转、缩放。
* 涉及界面交互的ArkUI组件（如TextInput等）：建议在页面布局中使用Stack包裹同层组件容器与BuilderNode，并使两者位置一致，NodeContainer要与<embed>/<object>标签对齐，以保障组件正常交互。如两者位置不一致，可能出现的问题有：TextInput/TextArea等附属的文本选择框位置错位（如下图）、LoadingProgress/Marquee等组件的动画启停与组件可见状态不匹配。

  **图2** 未使用Stack包裹，TextInput的位置错位

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/3OYDOa4FQrakgVS4ql6xtA/zh-cn_image_0000002558764736.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=3855FE4C3B6028F895EEC24B724035CDA6103E53731C8FE7B285E40BD09FA330)

  **图3** 使用Stack包裹，TextInput的位置正常

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Sw0iF9YrQZGzz6CuSOqBkQ/zh-cn_image_0000002558605080.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=22B1E2D588D485A57E110CA1DF6B1F575E761ADC59F5056EADACEFE0FE895617)

## Web页面中同层渲染输入框

在Web页面中，可以使用ArkUI系统的TextInput组件进行同层渲染。此处利用同层渲染展示三个输入框，渲染效果图如下：

**图4** 同层渲染输入框

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/dCU8ecHKRr-EOv2gUjW99w/zh-cn_image_0000002589324605.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=339F400E5799CF9DC423BB1F7148FB2F468924FF42E927B7752E4AEE994E64FC)

1. 在Web页面中标记需要同层渲染的HTML标签。

   同层渲染支持<embed>/<object>两种标签。type类型可任意指定，两个字符串参数均不区分大小写，ArkWeb内核将会统一转换为小写。其中，tag字符串使用全字符串匹配，type使用字符串前缀匹配。

   若开发者不使用该接口或该接口接收的为非法字符串（空字符串）时，ArkWeb内核将使用默认设置，即"embed" + "native/"前缀模式。若指定类型与w3c定义的<embed>或<object>标准类型重合，如registerNativeEmbedRule("object", "application/pdf")，ArkWeb将遵循w3c标准行为，不会将其识别为同层标签。

   * 采用<embed>标签。

     ```
     1. <!--HAP's src/main/resources/rawfile/text.html-->
     2. <!DOCTYPE html>
     3. <html>
     4. <head>
     5. <title>同层渲染html</title>
     6. <meta name="viewport">
     7. </head>

     9. <body style="background:white">

     11. <embed id = "input1" type="native/view" style="width: 100%; height: 100px; margin: 30px; margin-top: 600px"/>

     13. <embed id = "input2" type="native/view2" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"/>

     15. <embed id = "input3" type="native/view3" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"/>

     17. </body>
     18. </html>
     ```
   * 采用<object>标签。

     需要使用registerNativeEmbedRule注册object标签。

     ```
     1. // ...
     2. Web({src: $rawfile("text.html"), controller: this.browserTabController})
     3. // 注册同层标签为"object"，类型为"test"前缀。
     4. .registerNativeEmbedRule("object", "test")
     5. // ...
     ```

     与registerNativeEmbedRule相对应的前端页面代码，类型可使用"test"及以"test"为前缀的字串。

     ```
     1. <!--HAP's src/main/resources/rawfile/text2.html-->
     2. <!DOCTYPE html>
     3. <html>
     4. <head>
     5. <title>同层渲染html</title>
     6. <meta name="viewport">
     7. </head>

     9. <body style="background:white">

     11. <object id = "input1" type="test/input" style="width: 100%; height: 100px; margin: 30px; margin-top: 600px"></object>

     13. <object id = "input2" type="test/input" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"></object>

     15. <object id = "input3" type="test/input" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"></object>

     17. </body>
     18. </html>
     ```
2. 在应用侧开启同层渲染功能。

   同层渲染功能默认不开启，如果要使用同层渲染的功能，可通过[enableNativeEmbedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#enablenativeembedmode11)来开启。

   ```
   1. // xxx.ets
   2. import { webview } from '@kit.ArkWeb';
   3. @Entry
   4. @Component
   5. struct WebComponent {
   6. controller: webview.WebviewController = new webview.WebviewController();

   8. build() {
   9. Column() {
   10. Web({ src: 'www.example.com', controller: this.controller })
   11. // 配置同层渲染开关开启。
   12. .enableNativeEmbedMode(true)
   13. }
   14. }
   15. }
   ```
3. 创建自定义组件。

   同层渲染功能开启后，展示在对应区域的系统组件。

   ```
   1. @Component
   2. struct TextInputComponent {
   3. @Prop params: Params
   4. @State bkColor: Color = Color.White

   6. build() {
   7. Column() {
   8. TextInput({text: '', placeholder: 'please input your word...'})
   9. .placeholderColor(Color.Gray)
   10. .id(this.params?.elementId)
   11. .placeholderFont({size: 13, weight: 400})
   12. .caretColor(Color.Gray)
   13. .width(this.params?.width)
   14. .height(this.params?.height)
   15. .fontSize(14)
   16. .fontColor(Color.Black)
   17. }
   18. //自定义组件中的最外层容器组件宽高应该为同层标签的宽高。
   19. .width(this.params.width)
   20. .height(this.params.height)
   21. }
   22. }

   24. @Builder
   25. function TextInputBuilder(params:Params) {
   26. TextInputComponent({params: params})
   27. .width(params.width)
   28. .height(params.height)
   29. .backgroundColor(Color.White)
   30. }
   ```
4. 创建节点控制器。

   用于控制和反馈对应NodeContainer上的节点行为。

   ```
   1. class MyNodeController extends NodeController {
   2. private rootNode: BuilderNode<[Params]> | undefined | null;
   3. private embedId_: string = "";
   4. private surfaceId_: string = "";
   5. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
   6. private width_: number = 0;
   7. private height_: number = 0;
   8. private type_: string = "";
   9. private isDestroy_: boolean = false;

   11. setRenderOption(params: NodeControllerParams) {
   12. this.surfaceId_ = params.surfaceId;
   13. this.renderType_ = params.renderType;
   14. this.embedId_ = params.embedId;
   15. this.width_ = params.width;
   16. this.height_ = params.height;
   17. this.type_ = params.type;
   18. }

   20. // 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
   21. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
   22. makeNode(uiContext: UIContext): FrameNode | null {
   23. if (this.isDestroy_) { // rootNode为null。
   24. return null;
   25. }
   26. if (!this.rootNode) {// rootNode 为undefined时。
   27. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
   28. if(this.rootNode) {
   29. this.rootNode.build(wrapBuilder(TextInputBuilder), {  textOne: "myTextInput", width: this.width_, height: this.height_  })
   30. return this.rootNode.getFrameNode();
   31. }else{
   32. return null;
   33. }
   34. }
   35. // 返回FrameNode节点。
   36. return this.rootNode.getFrameNode();
   37. }

   39. updateNode(arg: Object): void {
   40. this.rootNode?.update(arg);
   41. }

   43. getEmbedId(): string {
   44. return this.embedId_;
   45. }

   47. setDestroy(isDestroy: boolean): void {
   48. this.isDestroy_ = isDestroy;
   49. if (this.isDestroy_) {
   50. this.rootNode = null;
   51. }
   52. }

   54. postEvent(event: TouchEvent | undefined): boolean {
   55. return this.rootNode?.postTouchEvent(event) as boolean
   56. }
   57. }
   ```
5. 监听同层渲染的生命周期变化。

   开启该功能后，当网页中存在同层渲染支持的标签时，ArkWeb内核会触发由[onNativeEmbedLifecycleChange](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedlifecyclechange11)注册的回调函数。

   开发者则需要调用[onNativeEmbedLifecycleChange](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedlifecyclechange11)来监听同层渲染标签的生命周期变化。

   ```
   1. build() {
   2. Row() {
   3. Column() {
   4. Stack() {
   5. ForEach(this.componentIdArr, (componentId: string) => {
   6. NodeContainer(this.nodeControllerMap.get(componentId))
   7. .position(this.positionMap.get(componentId))
   8. .width(this.widthMap.get(componentId))
   9. .height(this.heightMap.get(componentId))
   10. }, (embedId: string) => embedId)
   11. // Web组件加载本地text.html页面。
   12. Web({src: $rawfile("text.html"), controller: this.browserTabController})
   13. // 配置同层渲染开关开启。
   14. .enableNativeEmbedMode(true)
   15. // 注册同层标签为<object>，类型为"test"前缀。
   16. .registerNativeEmbedRule("object", "test")
   17. // 获取<embed>标签的生命周期变化数据。
   18. .onNativeEmbedLifecycleChange((embed) => {
   19. console.info("NativeEmbed surfaceId" + embed.surfaceId);
   20. // 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id。
   21. const componentId = embed.info?.id?.toString() as string
   22. if (embed.status == NativeEmbedStatus.CREATE) {
   23. console.info("NativeEmbed create" + JSON.stringify(embed.info));
   24. // 创建节点控制器、设置参数。
   25. let nodeController = new MyNodeController()
   26. // embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp。
   27. nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
   28. type : embed.info?.type as string,
   29. renderType : NodeRenderType.RENDER_TYPE_TEXTURE,
   30. embedId : embed.embedId as string,
   31. width : this.uiContext.px2vp(embed.info?.width),
   32. height : this.uiContext.px2vp(embed.info?.height)})
   33. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
   34. nodeController.setDestroy(false);
   35. //根据web传入的embed的id属性作为key，将nodeController存入Map。
   36. this.nodeControllerMap.set(componentId, nodeController);
   37. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
   38. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
   39. this.positionMap.set(componentId, this.edges);
   40. // 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器,需要将push动作放在set之后。
   41. this.componentIdArr.push(componentId)
   42. } else if (embed.status == NativeEmbedStatus.UPDATE) {
   43. let nodeController = this.nodeControllerMap.get(componentId);
   44. console.info("NativeEmbed update" + JSON.stringify(embed));
   45. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
   46. this.positionMap.set(componentId, this.edges);
   47. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
   48. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
   49. interface UpdateNodeParams {
   50. textOne: string;
   51. width: number;
   52. height: number;
   53. }
   54. const updateParams: UpdateNodeParams = {
   55. textOne: 'update',
   56. width: this.uiContext.px2vp(embed.info?.width),
   57. height: this.uiContext.px2vp(embed.info?.height)
   58. }
   59. nodeController?.updateNode(updateParams);
   60. } else if (embed.status == NativeEmbedStatus.DESTROY) {
   61. console.info("NativeEmbed destroy" + JSON.stringify(embed));
   62. let nodeController = this.nodeControllerMap.get(componentId);
   63. nodeController?.setDestroy(true);
   64. this.nodeControllerMap.delete(componentId);
   65. this.positionMap.delete(componentId);
   66. this.widthMap.delete(componentId);
   67. this.heightMap.delete(componentId);
   68. this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
   69. } else {
   70. console.info("NativeEmbed status" + embed.status);
   71. }
   72. })
   73. }.height("80%")
   74. }
   75. }
   76. }
   ```
6. 同层渲染手势事件。

   开启该功能后，每当在同层渲染的区域进行触摸操作时，ArkWeb内核会触发[onNativeEmbedGestureEvent](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedgestureevent11)注册的回调函数。

   开发者则需要调用[onNativeEmbedGestureEvent](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedgestureevent11)来监听同层渲染区域的手势事件。

   ```
   1. build() {
   2. Row() {
   3. Column() {
   4. Stack() {
   5. ForEach(this.componentIdArr, (componentId: string) => {
   6. NodeContainer(this.nodeControllerMap.get(componentId))
   7. .position(this.positionMap.get(componentId))
   8. .width(this.widthMap.get(componentId))
   9. .height(this.heightMap.get(componentId))
   10. }, (embedId: string) => embedId)
   11. // Web组件加载本地text.html页面。
   12. Web({src: $rawfile("text.html"), controller: this.browserTabController})
   13. // 配置同层渲染开关开启。
   14. .enableNativeEmbedMode(true)
   15. // 获取<embed>标签的生命周期变化数据。
   16. .onNativeEmbedLifecycleChange((embed) => {
   17. // 生命周期变化实现。
   18. })
   19. .onNativeEmbedGestureEvent((touch) => {
   20. console.info("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
   21. this.componentIdArr.forEach((componentId: string) => {
   22. let nodeController = this.nodeControllerMap.get(componentId);
   23. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
   24. if(nodeController?.getEmbedId() == touch.embedId) {
   25. let ret = nodeController?.postEvent(touch.touchEvent)
   26. if(ret) {
   27. console.info("onNativeEmbedGestureEvent success " + componentId);
   28. } else {
   29. console.info("onNativeEmbedGestureEvent fail " + componentId);
   30. }
   31. if(touch.result) {
   32. // 通知Web组件手势事件消费结果。
   33. touch.result.setGestureEventResult(ret);
   34. }
   35. }
   36. })
   37. })
   38. }
   39. }
   40. }
   41. }
   ```
7. 同层渲染鼠标事件

   开启该功能后，在同层渲染的区域进行下述动作时，ArkWeb内核会触发[onNativeEmbedMouseEvent](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedmouseevent20)注册的回调函数：

   * 使用鼠标左键、中键、右键进行点击或长按。
   * 使用触摸板进行对应鼠标左键、中键、右键点击长按的操作。

   开发者则需要调用[onNativeEmbedMouseEvent](../harmonyos-references/arkts-basic-components-web-events.md#onnativeembedmouseevent20)来监听同层渲染区域的鼠标事件。

   ```
   1. build() {
   2. Row() {
   3. Column() {
   4. Stack() {
   5. ForEach(this.componentIdArr, (componentId: string) => {
   6. NodeContainer(this.nodeControllerMap.get(componentId))
   7. .position(this.positionMap.get(componentId))
   8. .width(this.widthMap.get(componentId))
   9. .height(this.heightMap.get(componentId))
   10. }, (embedId: string) => embedId)
   11. // Web组件加载本地text.html页面。
   12. Web({src: $rawfile("text.html"), controller: this.browserTabController})
   13. // 配置同层渲染开关开启。
   14. .enableNativeEmbedMode(true)
   15. // 获取<embed>标签的生命周期变化数据。
   16. .onNativeEmbedLifecycleChange((embed) => {
   17. // 生命周期变化实现。
   18. })
   19. .onNativeEmbedGestureEvent((touch) => {
   20. // 处理同层渲染手势事件。
   21. })
   22. .onNativeEmbedMouseEvent((mouse) => {
   23. console.info("NativeEmbed onNativeEmbedMouseEvent" + JSON.stringify(mouse.mouseEvent));
   24. this.componentIdArr.forEach((componentId: string) => {
   25. let nodeController = this.nodeControllerMap.get(componentId);
   26. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
   27. if(nodeController?.getEmbedId() == mouse.embedId) {
   28. let ret = nodeController?.postInputEvent(mouse.mouseEvent)
   29. if(ret) {
   30. console.info("onNativeEmbedMouseEvent success " + componentId);
   31. } else {
   32. console.info("onNativeEmbedMouseEvent fail " + componentId);
   33. }
   34. if(mouse.result) {
   35. // 通知Web组件鼠标事件消费结果。
   36. mouse.result.setMouseEventResult(ret);
   37. }
   38. }
   39. })
   40. })
   41. }
   42. }
   43. }
   44. }
   ```

**完整示例：**

使用前请在module.json5中添加网络权限，添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.INTERNET"
4. }
5. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseSameLayerRender/entry/src/main/module.json5#L65-L71)

应用侧代码。

```
1. import { webview } from '@kit.ArkWeb';
2. import { UIContext } from '@kit.ArkUI';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';

5. @Observed
6. declare class Params{
7. public elementId: string
8. public textOne: string
9. public textTwo: string
10. public width: number
11. public height: number
12. }

14. declare class NodeControllerParams {
15. public surfaceId: string
16. public type: string
17. public renderType: NodeRenderType
18. public embedId: string
19. public width: number
20. public height: number
21. }

23. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
24. class MyNodeController extends NodeController {
25. private rootNode: BuilderNode<[Params]> | undefined | null;
26. private embedId_: string = '';
27. private surfaceId_: string = '';
28. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
29. private width_: number = 0;
30. private height_: number = 0;
31. private type_: string = '';
32. private isDestroy_: boolean = false;

34. setRenderOption(params: NodeControllerParams) {
35. this.surfaceId_ = params.surfaceId;
36. this.renderType_ = params.renderType;
37. this.embedId_ = params.embedId;
38. this.width_ = params.width;
39. this.height_ = params.height;
40. this.type_ = params.type;
41. }

43. // 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
44. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
45. makeNode(uiContext: UIContext): FrameNode | null {
46. if (this.isDestroy_) { // rootNode为null。
47. return null;
48. }
49. if (!this.rootNode) { // rootNode 为undefined时。
50. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
51. if (this.rootNode) {
52. this.rootNode.build(
53. wrapBuilder(textInputBuilder), {  textOne: 'myTextInput', width: this.width_, height: this.height_  });
54. return this.rootNode.getFrameNode();
55. }else{
56. return null;
57. }
58. }
59. // 返回FrameNode节点。
60. return this.rootNode.getFrameNode();
61. }

63. updateNode(arg: Object): void {
64. this.rootNode?.update(arg);
65. }

67. getEmbedId(): string {
68. return this.embedId_;
69. }

71. setDestroy(isDestroy: boolean): void {
72. this.isDestroy_ = isDestroy;
73. if (this.isDestroy_) {
74. this.rootNode = null;
75. }
76. }

78. postEvent(event: TouchEvent | undefined): boolean {
79. return this.rootNode?.postTouchEvent(event) as boolean;
80. }

82. postInputEvent(event: MouseEvent | undefined): boolean {
83. return this.rootNode?.postInputEvent(event) as boolean;
84. }
85. }

87. @Component
88. struct TextInputComponent {
89. @Prop params: Params;
90. @State bkColor: Color = Color.White;

92. build() {
93. Column() {
94. TextInput({text: '', placeholder: 'please input your word...'})
95. .placeholderColor(Color.Gray)
96. .id(this.params?.elementId)
97. .placeholderFont({size: 13, weight: 400})
98. .caretColor(Color.Gray)
99. .fontSize(14)
100. .fontColor(Color.Black)
101. }
102. //自定义组件中的最外层容器组件宽高应该为同层标签的宽高。
103. .width(this.params.width)
104. .height(this.params.height)
105. }
106. }

108. // @Builder中为动态组件的具体组件内容。
109. @Builder
110. function textInputBuilder(params:Params) {
111. TextInputComponent({params: params})
112. .backgroundColor(Color.White)
113. }

115. @Entry
116. @Component
117. struct Page{
118. browserTabController: WebviewController = new webview.WebviewController()
119. private nodeControllerMap: Map<string, MyNodeController> = new Map();
120. @State componentIdArr: Array<string> = [];
121. @State widthMap: Map<string, number> = new Map();
122. @State heightMap: Map<string, number> = new Map();
123. @State positionMap: Map<string, Edges> = new Map();
124. @State edges: Edges = {};
125. uiContext: UIContext = this.getUIContext();

127. build() {
128. Row() {
129. Column() {
130. Stack() {
131. ForEach(this.componentIdArr, (componentId: string) => {
132. NodeContainer(this.nodeControllerMap.get(componentId))
133. .position(this.positionMap.get(componentId))
134. .width(this.widthMap.get(componentId))
135. .height(this.heightMap.get(componentId))
136. }, (embedId: string) => embedId)
137. // Web组件加载本地test2.html页面。
138. Web({src: $rawfile('test2.html'), controller: this.browserTabController})
139. // 注册同层标签为'object'，类型为'test'前缀
140. .registerNativeEmbedRule('object', 'test')
141. // 配置同层渲染开关开启。
142. .enableNativeEmbedMode(true)
143. // 获取embed标签的生命周期变化数据。
144. .onNativeEmbedLifecycleChange((embed) => {
145. console.info('NativeEmbed surfaceId' + embed.surfaceId);
146. // 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id。
147. const componentId = embed.info?.id?.toString() as string;
148. if (embed.status === NativeEmbedStatus.CREATE) {
149. console.info('NativeEmbed create' + JSON.stringify(embed.info));
150. // 创建节点控制器、设置参数。
151. let nodeController = new MyNodeController();
152. // embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp。
153. nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
154. type : embed.info?.type as string,
155. renderType : NodeRenderType.RENDER_TYPE_TEXTURE,
156. embedId : embed.embedId as string,
157. width : this.uiContext.px2vp(embed.info?.width),
158. height : this.uiContext.px2vp(embed.info?.height)});
159. this.edges = {
160. left: `${embed.info?.position?.x as number}px`,
161. top: `${embed.info?.position?.y as number}px`
162. };
163. nodeController.setDestroy(false);
164. //根据web传入的embed的id属性作为key，将nodeController存入Map。
165. this.nodeControllerMap.set(componentId, nodeController);
166. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
167. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
168. this.positionMap.set(componentId, this.edges);
169. // 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器,需要将push动作放在set之后。
170. this.componentIdArr.push(componentId);
171. } else if (embed.status === NativeEmbedStatus.UPDATE) {
172. let nodeController = this.nodeControllerMap.get(componentId);
173. console.info('NativeEmbed update' + JSON.stringify(embed));
174. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`};
175. this.positionMap.set(componentId, this.edges);
176. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
177. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
178. interface UpdateNodeParams {
179. textOne: string;
180. width: number;
181. height: number;
182. }
183. const updateParams: UpdateNodeParams = {
184. textOne: 'update',
185. width: this.uiContext.px2vp(embed.info?.width),
186. height: this.uiContext.px2vp(embed.info?.height)
187. }
188. nodeController?.updateNode(updateParams);
189. } else if (embed.status === NativeEmbedStatus.DESTROY) {
190. console.info('NativeEmbed destroy' + JSON.stringify(embed));
191. let nodeController = this.nodeControllerMap.get(componentId);
192. nodeController?.setDestroy(true);
193. this.nodeControllerMap.delete(componentId);
194. this.positionMap.delete(componentId);
195. this.widthMap.delete(componentId);
196. this.heightMap.delete(componentId);
197. this.componentIdArr = this.componentIdArr.filter((value: string) => value != componentId);
198. } else {
199. console.info('NativeEmbed status' + embed.status);
200. }
201. })
202. // 获取同层渲染组件触摸事件信息。
203. .onNativeEmbedGestureEvent((touch) => {
204. console.info('NativeEmbed onNativeEmbedGestureEvent' + JSON.stringify(touch.touchEvent));
205. this.componentIdArr.forEach((componentId: string) => {
206. let nodeController = this.nodeControllerMap.get(componentId);
207. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
208. if (nodeController?.getEmbedId() === touch.embedId) {
209. let ret = nodeController?.postEvent(touch.touchEvent);
210. if (ret) {
211. console.info('onNativeEmbedGestureEvent success ' + componentId);
212. } else {
213. console.info('onNativeEmbedGestureEvent fail ' + componentId);
214. }
215. if (touch.result) {
216. // 通知Web组件手势事件消费结果。
217. touch.result.setGestureEventResult(ret);
218. }
219. }
220. })
221. })
222. .onNativeEmbedMouseEvent((mouse) => {
223. console.info('NativeEmbed onNativeEmbedMouseEvent' + JSON.stringify(mouse.mouseEvent));
224. this.componentIdArr.forEach((componentId: string) => {
225. let nodeController = this.nodeControllerMap.get(componentId);
226. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
227. if (nodeController?.getEmbedId() === mouse.embedId) {
228. let ret = nodeController?.postInputEvent(mouse.mouseEvent);
229. if (ret) {
230. console.info('onNativeEmbedMouseEvent success ' + componentId);
231. } else {
232. console.info('onNativeEmbedMouseEvent fail ' + componentId);
233. }
234. if (mouse.result) {
235. // 通知Web组件鼠标事件消费结果。
236. mouse.result.setMouseEventResult(ret);
237. }
238. }
239. })
240. })
241. }
242. }
243. }
244. }
245. }
```

## 绘制XComponent+AVPlayer和Button组件

* 应用侧代码组件使用示例。

  ```
  1. // 创建NodeController
  2. import { webview } from '@kit.ArkWeb';
  3. import { UIContext, NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';
  4. import { AVPlayerDemo } from './PlayerDemo';

  6. @Observed
  7. declare class Params {
  8. public textOne : string
  9. public textTwo : string
  10. public width : number
  11. public height : number
  12. }

  14. declare class NodeControllerParams {
  15. public surfaceId : string
  16. public type : string
  17. public renderType : NodeRenderType
  18. public embedId : string
  19. public width : number
  20. public height : number
  21. }

  23. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
  24. class MyNodeController extends NodeController {
  25. private rootNode: BuilderNode<[Params]> | undefined | null;
  26. private embedId_ : string = '';
  27. private surfaceId_ : string = '';
  28. private renderType_ :NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  29. private width_ : number = 0;
  30. private height_ : number = 0;
  31. private type_ : string = '';
  32. private isDestroy_ : boolean = false;

  34. setRenderOption(params : NodeControllerParams) {
  35. this.surfaceId_ = params.surfaceId;
  36. this.renderType_ = params.renderType;
  37. this.embedId_ = params.embedId;
  38. this.width_ = params.width;
  39. this.height_ = params.height;
  40. this.type_ = params.type;
  41. }
  42. // 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
  43. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
  44. makeNode(uiContext: UIContext): FrameNode | null{
  45. if (this.isDestroy_) { // rootNode为null。
  46. return null;
  47. }
  48. if (!this.rootNode) { // rootNode 为undefined时。
  49. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_});
  50. if (this.type_ === 'native/video') {
  51. this.rootNode.build(
  52. wrapBuilder(videoBuilder), {textOne: 'myButton', width : this.width_, height : this.height_});
  53. } else {
  54. // other
  55. }
  56. }
  57. // 返回FrameNode节点。
  58. return this.rootNode.getFrameNode();
  59. }

  61. updateNode(arg: Object): void {
  62. this.rootNode?.update(arg);
  63. }
  64. getEmbedId() : string {
  65. return this.embedId_;
  66. }

  68. setDestroy(isDestroy : boolean) : void {
  69. this.isDestroy_ = isDestroy;
  70. if (this.isDestroy_) {
  71. this.rootNode = null;
  72. }
  73. }

  75. postEvent(event: TouchEvent | undefined) : boolean {
  76. return this.rootNode?.postTouchEvent(event) as boolean;
  77. }

  79. postInputEvent(event: MouseEvent | undefined): boolean {
  80. return this.rootNode?.postInputEvent(event) as boolean;
  81. }
  82. }

  84. @Component
  85. struct VideoComponent {
  86. @ObjectLink params: Params;
  87. @State bkColor: Color = Color.Red;
  88. mXComponentController: XComponentController = new XComponentController();
  89. @State playerChanged: boolean = false;
  90. player?: AVPlayerDemo;

  92. build() {
  93. Column() {
  94. Button(this.params.textOne);

  96. XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.mXComponentController})
  97. .border({width: 1, color: Color.Red})
  98. .onLoad(() => {
  99. this.player = new AVPlayerDemo();
  100. this.player.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());
  101. this.playerChanged = !this.playerChanged;
  102. this.player.avPlayerLiveDemo();
  103. })
  104. .width(300)
  105. .height(200)
  106. }
  107. //自定义组件中的最外层容器组件宽高应该为同层标签的宽高。
  108. .width(this.params.width)
  109. .height(this.params.height)
  110. }
  111. }
  112. // @Builder中为动态组件的具体组件内容。
  113. @Builder
  114. function videoBuilder(params: Params) {
  115. VideoComponent({ params: params })
  116. .backgroundColor(Color.Gray)
  117. }

  119. @Entry
  120. @Component
  121. struct WebIndex {
  122. browserTabController: WebviewController = new webview.WebviewController();
  123. private nodeControllerMap: Map<string, MyNodeController> = new Map();
  124. @State componentIdArr: Array<string> = [];
  125. @State widthMap: Map<string, number> = new Map();
  126. @State heightMap: Map<string, number> = new Map();
  127. @State positionMap: Map<string, Edges> = new Map();
  128. @State edges: Edges = {};
  129. uiContext: UIContext = this.getUIContext();

  131. aboutToAppear() {
  132. // 配置web开启调试模式。
  133. webview.WebviewController.setWebDebuggingAccess(true);
  134. }

  136. build(){
  137. Row() {
  138. Column() {
  139. Stack() {
  140. ForEach(this.componentIdArr, (componentId: string) => {
  141. NodeContainer(this.nodeControllerMap.get(componentId))
  142. .position(this.positionMap.get(componentId))
  143. .width(this.widthMap.get(componentId))
  144. .height(this.heightMap.get(componentId))
  145. }, (embedId: string) => embedId)
  146. // Web组件加载本地test.html页面。
  147. Web({ src: $rawfile('test3.html'), controller: this.browserTabController })
  148. // 配置同层渲染开关开启。
  149. .enableNativeEmbedMode(true)
  150. // 获取<embed>标签的生命周期变化数据。
  151. .onNativeEmbedLifecycleChange((embed) => {
  152. console.info('NativeEmbed surfaceId' + embed.surfaceId);
  153. // 1. 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id。
  154. const componentId = embed.info?.id?.toString() as string;
  155. if (embed.status === NativeEmbedStatus.CREATE) {
  156. console.info('NativeEmbed create' + JSON.stringify(embed.info));
  157. // 创建节点控制器，设置参数。
  158. let nodeController = new MyNodeController();
  159. // 1. embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp。
  160. nodeController.setRenderOption({
  161. surfaceId : embed.surfaceId as string, type : embed.info?.type as string,
  162. renderType : NodeRenderType.RENDER_TYPE_TEXTURE, embedId : embed.embedId as string,
  163. width : this.uiContext.px2vp(embed.info?.width), height : this.uiContext.px2vp(embed.info?.height)});
  164. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`};
  165. nodeController.setDestroy(false);
  166. // 根据web传入的embed的id属性作为key，将nodeController存入map。
  167. this.nodeControllerMap.set(componentId, nodeController);
  168. this.widthMap.set(componentId,  this.uiContext.px2vp(embed.info?.width));
  169. this.heightMap.set(componentId,  this.uiContext.px2vp(embed.info?.height));
  170. this.positionMap.set(componentId, this.edges);
  171. // 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器，需要将push动作放在set之后。
  172. this.componentIdArr.push(componentId);
  173. } else if (embed.status === NativeEmbedStatus.UPDATE) {
  174. let nodeController = this.nodeControllerMap.get(componentId);
  175. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`};
  176. this.positionMap.set(componentId, this.edges);
  177. this.widthMap.set(componentId,  this.uiContext.px2vp(embed.info?.width));
  178. this.heightMap.set(componentId,  this.uiContext.px2vp(embed.info?.height));
  179. interface UpdateNodeParams {
  180. textOne: string;
  181. width: number;
  182. height: number;
  183. }
  184. const updateParams: UpdateNodeParams = {
  185. textOne: 'update',
  186. width: this.uiContext.px2vp(embed.info?.width),
  187. height: this.uiContext.px2vp(embed.info?.height)
  188. }
  189. nodeController?.updateNode(updateParams);
  190. } else if (embed.status === NativeEmbedStatus.DESTROY) {
  191. let nodeController = this.nodeControllerMap.get(componentId);
  192. nodeController?.setDestroy(true);
  193. this.nodeControllerMap.delete(componentId);
  194. this.positionMap.delete(componentId);
  195. this.widthMap.delete(componentId);
  196. this.heightMap.delete(componentId);
  197. this.componentIdArr = this.componentIdArr.filter((value: string) => value != componentId);
  198. } else {
  199. console.info('NativeEmbed status' + embed.status);
  200. }
  201. })// 获取同层渲染组件触摸事件信息。
  202. .onNativeEmbedGestureEvent((touch) => {
  203. console.info('NativeEmbed onNativeEmbedGestureEvent' + JSON.stringify(touch.touchEvent));
  204. this.componentIdArr.forEach((componentId: string) => {
  205. let nodeController = this.nodeControllerMap.get(componentId);
  206. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
  207. if (nodeController?.getEmbedId() === touch.embedId) {
  208. let ret = nodeController?.postEvent(touch.touchEvent);
  209. if (ret) {
  210. console.info('onNativeEmbedGestureEvent success ' + componentId);
  211. } else {
  212. console.info('onNativeEmbedGestureEvent fail ' + componentId);
  213. }
  214. if (touch.result) {
  215. // 通知Web组件手势事件消费结果。
  216. touch.result.setGestureEventResult(ret);
  217. }
  218. }
  219. })
  220. })
  221. .onNativeEmbedMouseEvent((mouse) => {
  222. console.info('NativeEmbed onNativeEmbedMouseEvent' + JSON.stringify(mouse.mouseEvent));
  223. this.componentIdArr.forEach((componentId: string) => {
  224. let nodeController = this.nodeControllerMap.get(componentId);
  225. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
  226. if(nodeController?.getEmbedId() === mouse.embedId) {
  227. let ret = nodeController?.postInputEvent(mouse.mouseEvent);
  228. if(ret) {
  229. console.info('onNativeEmbedMouseEvent success ' + componentId);
  230. } else {
  231. console.info('onNativeEmbedMouseEvent fail ' + componentId);
  232. }
  233. if(mouse.result) {
  234. // 通知Web组件鼠标事件消费结果。
  235. mouse.result.setMouseEventResult(ret);
  236. }
  237. }
  238. })
  239. })
  240. }
  241. }
  242. }
  243. }
  244. }
  ```

  [DrawXCompAVPBtn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseSameLayerRender/entry/src/main/ets/pages/DrawXCompAVPBtn.ets#L16-L252)
* 应用侧代码示例，视频播放，使用时需替换为正确的视频链接地址。

  ```
  1. import { media } from '@kit.MediaKit';
  2. import { BusinessError } from '@ohos.base';

  4. export class AVPlayerDemo {
  5. private count: number = 0;
  6. private surfaceId: string = ''; // surfaceId用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法。
  7. private isSeek: boolean = true; // 用于区分模式是否支持seek操作。

  9. setSurfaceID(id: string){
  10. console.log('setSurfaceID : ' + id);
  11. this.surfaceId = id;
  12. }
  13. // 注册avplayer回调函数。
  14. setAVPlayerCallback(avPlayer: media.AVPlayer) {
  15. // seek操作结果回调函数。
  16. avPlayer.on('seekDone', (seekDoneTime: number) => {
  17. console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
  18. })
  19. // error回调监听函数，当avplayer在操作过程中出现错误时，调用reset接口触发重置流程。
  20. avPlayer.on('error', (err: BusinessError) => {
  21. console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
  22. avPlayer.reset();
  23. })
  24. // 状态机变化回调函数。
  25. avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
  26. switch (state) {
  27. case 'idle': // 成功调用reset接口后触发该状态机上报。
  28. console.info('AVPlayer state idle called.');
  29. avPlayer.release(); // 调用release接口销毁实例对象。
  30. break;
  31. case 'initialized': // avplayer 设置播放源后触发该状态上报。
  32. console.info('AVPlayer state initialized called.');
  33. avPlayer.surfaceId = this.surfaceId; // 设置显示画面，当播放的资源为纯音频时无需设置。
  34. avPlayer.prepare();
  35. break;
  36. case 'prepared': // prepared调用成功后上报该状态机。
  37. console.info('AVPlayer state prepared called.');
  38. avPlayer.play(); // 调用播放接口开始播放。
  39. break;
  40. case 'playing': // play成功调用后触发该状态机上报。
  41. console.info('AVPlayer state playing called.');
  42. if(this.count !== 0) {
  43. if (this.isSeek) {
  44. console.info('AVPlayer start to seek.');
  45. avPlayer.seek(avPlayer.duration); // seek到视频末尾。
  46. } else {
  47. // 当播放模式不支持seek操作时继续播放到结尾。
  48. console.info('AVPlayer wait to play end.');
  49. }
  50. } else {
  51. avPlayer.pause(); // 调用暂停接口暂停播放。
  52. }
  53. this.count++;
  54. break;
  55. case 'paused': // pause成功调用后触发该状态机上报。
  56. console.info('AVPlayer state paused called.');
  57. avPlayer.play(); // 再次播放接口开始播放。
  58. break;
  59. case 'completed': //播放接口后触发该状态机上报。
  60. console.info('AVPlayer state completed called.');
  61. avPlayer.stop(); // 调用播放接口。
  62. break;
  63. case 'stopped': // stop接口后触发该状态机上报。
  64. console.info('AVPlayer state stopped called.');
  65. avPlayer.reset(); // 调用reset接口初始化avplayer状态。
  66. break;
  67. case 'released': //播放接口后触发该状态机上报。
  68. console.info('AVPlayer state released called.');
  69. break;
  70. default:
  71. break;
  72. }
  73. })
  74. }

  76. // 通过url设置网络地址来实现播放直播码流。
  77. async avPlayerLiveDemo(){
  78. try {
  79. // 创建avPlayer实例对象。
  80. let avPlayer: media.AVPlayer = await media.createAVPlayer();
  81. // 创建状态机变化回调函数。
  82. this.setAVPlayerCallback(avPlayer);
  83. this.isSeek = false; // 不支持seek操作。
  84. // 使用时需要自行替换视频链接。
  85. avPlayer.url = 'xxx/demo.mp4';
  86. } catch (error) {
  87. console.error('Failed to create or play video: ', error);
  88. }
  89. }
  90. }
  ```

  [PlayerDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseSameLayerRender/entry/src/main/ets/pages/PlayerDemo.ets#L16-L103)
* 前端页面示例。

  ```
  1. <!--HAP's src/main/resources/rawfile/test3.html-->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <title>同层渲染测试html</title>
  6. <meta name="viewport">
  7. </head>
  8. <body>
  9. <div>
  10. <div id="bodyId">
  11. <embed id="nativeVideo" type = "native/video" width="1000" height="1500" src="test" style = "background-color:red"/>
  12. </div>
  13. </div>
  14. </body>
  15. </html>
  ```
* 实现效果：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/f5sBql1DRKOOIRIL06uEvA/zh-cn_image_0000002589244543.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=1C52DECC54A1C58111563290C8D3F2DB87A5F3757B3951C9CB7D8707DA92B6AC)

## 同层标签设置为最高层级

同层渲染支持私有属性arkwebnativestyle，该属性仅在开启同层渲染后的<embed>和<object>中生效，该属性的display属性用于控制同层标签的显示层级，使其高于其他Web元素。如果多个同层标签都设置了arkwebnativestyle的display属性，并且属性相同，则它们的层级顺序将遵循W3C标准层级排序规则：先比较z-index属性值，当z-index相同时，按照元素在DOM中的先后顺序排序。display属性取值说明如下：

| display取值 | 说明 |
| --- | --- |
| overlay | 设置同层标签层级高于其他Web元素。 |
| overlay-infinity | 设置同层标签层级高于其他Web元素和设置overlay的同层标签。 |

* 应用侧代码：

```
1. import { webview } from '@kit.ArkWeb';
2. import { UIContext } from '@kit.ArkUI';
3. import { NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';

5. @Observed
6. declare class Params{
7. public elementId: string
8. public textOne: string
9. public textTwo: string
10. public width: number
11. public height: number
12. }

14. declare class NodeControllerParams {
15. public surfaceId: string
16. public type: string
17. public renderType: NodeRenderType
18. public embedId: string
19. public width: number
20. public height: number
21. }

23. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
24. class MyNodeController extends NodeController {
25. private rootNode: BuilderNode<[Params]> | undefined | null;
26. private embedId_: string = '';
27. private surfaceId_: string = '';
28. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
29. private width_: number = 0;
30. private height_: number = 0;
31. private type_: string = '';
32. private isDestroy_: boolean = false;

34. setRenderOption(params: NodeControllerParams) {
35. this.surfaceId_ = params.surfaceId;
36. this.renderType_ = params.renderType;
37. this.embedId_ = params.embedId;
38. this.width_ = params.width;
39. this.height_ = params.height;
40. this.type_ = params.type;
41. }

43. // 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
44. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
45. makeNode(uiContext: UIContext): FrameNode | null {
46. if (this.isDestroy_) { // rootNode为null。
47. return null;
48. }
49. if (!this.rootNode) {// rootNode 为undefined时。
50. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
51. if (this.type_ === 'native/view1') {
52. this.rootNode.build(
53. wrapBuilder(textInputBuilder1), {  textOne: 'myTextInput', width: this.width_, height: this.height_  });
54. return this.rootNode.getFrameNode();
55. } else if (this.type_ === 'native/view2') {
56. this.rootNode.build(
57. wrapBuilder(textInputBuilder2), {  textOne: 'myTextInput', width: this.width_, height: this.height_  });
58. return this.rootNode.getFrameNode();
59. } else{
60. return null;
61. }
62. }
63. // 返回FrameNode节点。
64. return this.rootNode.getFrameNode();
65. }

67. updateNode(arg: Object): void {
68. this.rootNode?.update(arg);
69. }

71. getEmbedId(): string {
72. return this.embedId_;
73. }

75. setDestroy(isDestroy: boolean): void {
76. this.isDestroy_ = isDestroy;
77. if (this.isDestroy_) {
78. this.rootNode = null;
79. }
80. }

82. postEvent(event: TouchEvent | undefined): boolean {
83. return this.rootNode?.postTouchEvent(event) as boolean;
84. }
85. }

87. @Component
88. struct TextInputComponent1 {
89. @Prop params: Params;
90. @State bkColor: Color = Color.White;

92. build() {
93. Column() {
94. Text('display:overlay-infinity')
95. TextInput({text: '', placeholder: 'please input your word...'})
96. .placeholderColor(Color.Gray)
97. .id(this.params?.elementId)
98. .placeholderFont({size: 13, weight: 400})
99. .caretColor(Color.Gray)
100. .fontSize(14)
101. .fontColor(Color.Black)
102. }
103. // 自定义组件中的最外层容器组件宽高应该为同层标签的宽高。
104. .width(this.params.width)
105. .height(this.params.height)
106. }
107. }

109. // @Builder中为动态组件的具体组件内容。
110. @Builder
111. function textInputBuilder1(params:Params) {
112. TextInputComponent1({params: params})
113. .backgroundColor(Color.Pink)
114. }

116. @Component
117. struct TextInputComponent2 {
118. @Prop params: Params;
119. @State bkColor: Color = Color.White;

121. build() {
122. Column() {
123. Text('display:overlay')
124. TextInput({text: '', placeholder: 'please input your word...'})
125. .placeholderColor(Color.Gray)
126. .id(this.params?.elementId)
127. .placeholderFont({size: 13, weight: 400})
128. .caretColor(Color.Gray)
129. .fontSize(14)
130. .fontColor(Color.Black)
131. }
132. // 自定义组件中的最外层容器组件宽高应该为同层标签的宽高。
133. .width(this.params.width)
134. .height(this.params.height)
135. }
136. }

139. // @Builder中为动态组件的具体组件内容。
140. @Builder
141. function textInputBuilder2(params:Params) {
142. TextInputComponent2({params: params})
143. .backgroundColor(Color.Gray)
144. }

146. @Entry
147. @Component
148. struct Page{
149. browserTabController: webview.WebviewController = new webview.WebviewController();
150. private nodeControllerMap: Map<string, MyNodeController> = new Map();
151. @State componentIdArr: Array<string> = [];
152. @State widthMap: Map<string, number> = new Map();
153. @State heightMap: Map<string, number> = new Map();
154. @State positionMap: Map<string, Edges> = new Map();
155. @State edges: Edges = {};
156. uiContext: UIContext = this.getUIContext();

158. build() {
159. Row() {
160. Column() {
161. Stack() {
162. ForEach(this.componentIdArr, (componentId: string) => {
163. NodeContainer(this.nodeControllerMap.get(componentId))
164. .position(this.positionMap.get(componentId))
165. .width(this.widthMap.get(componentId))
166. .height(this.heightMap.get(componentId))
167. }, (embedId: string) => embedId)
168. // Web组件加载本地test4.html页面。
169. Web({src: $rawfile('test4.html'), controller: this.browserTabController})
170. // 配置同层渲染开关开启。
171. .enableNativeEmbedMode(true)
172. // 获取<embed>标签的生命周期变化数据。
173. .onNativeEmbedLifecycleChange((embed) => {
174. console.info('NativeEmbed surfaceId' + embed.surfaceId);
175. // 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id。
176. const componentId = embed.info?.id?.toString() as string
177. if (embed.status === NativeEmbedStatus.CREATE) {
178. console.info('NativeEmbed create' + JSON.stringify(embed.info));
179. // 创建节点控制器、设置参数。
180. let nodeController = new MyNodeController();
181. // embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp。
182. nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
183. type : embed.info?.type as string,
184. renderType : NodeRenderType.RENDER_TYPE_TEXTURE,
185. embedId : embed.embedId as string,
186. width : this.uiContext.px2vp(embed.info?.width),
187. height : this.uiContext.px2vp(embed.info?.height)});
188. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`};
189. nodeController.setDestroy(false);
190. // 根据web传入的embed的id属性作为key，将nodeController存入Map。
191. this.nodeControllerMap.set(componentId, nodeController);
192. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
193. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
194. this.positionMap.set(componentId, this.edges);
195. // 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器,需要将push动作放在set之后。
196. this.componentIdArr.push(componentId);
197. } else if (embed.status === NativeEmbedStatus.UPDATE) {
198. let nodeController = this.nodeControllerMap.get(componentId);
199. console.info('NativeEmbed update' + JSON.stringify(embed));
200. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`};
201. this.positionMap.set(componentId, this.edges);
202. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
203. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
204. interface UpdateNodeParams {
205. textOne: string;
206. width: number;
207. height: number;
208. }
209. const updateParams: UpdateNodeParams = {
210. textOne: 'update',
211. width: this.uiContext.px2vp(embed.info?.width),
212. height: this.uiContext.px2vp(embed.info?.height)
213. }
214. nodeController?.updateNode(updateParams);
215. } else if (embed.status === NativeEmbedStatus.DESTROY) {
216. console.info('NativeEmbed destroy' + JSON.stringify(embed));
217. let nodeController = this.nodeControllerMap.get(componentId);
218. nodeController?.setDestroy(true);
219. this.nodeControllerMap.delete(componentId);
220. this.positionMap.delete(componentId);
221. this.widthMap.delete(componentId);
222. this.heightMap.delete(componentId);
223. this.componentIdArr = this.componentIdArr.filter((value: string) => value != componentId);
224. } else {
225. console.info('NativeEmbed status' + embed.status);
226. }
227. })// 获取同层渲染组件触摸事件信息。
228. .onNativeEmbedGestureEvent((touch) => {
229. console.info('NativeEmbed onNativeEmbedGestureEvent' + JSON.stringify(touch.touchEvent));
230. this.componentIdArr.forEach((componentId: string) => {
231. let nodeController = this.nodeControllerMap.get(componentId);
232. // 将获取到的同层区域的事件发送到该区域embedId对应的nodeController上。
233. if (nodeController?.getEmbedId() === touch.embedId) {
234. let ret = nodeController?.postEvent(touch.touchEvent);
235. if (ret) {
236. console.info('onNativeEmbedGestureEvent success ' + componentId);
237. } else {
238. console.info('onNativeEmbedGestureEvent fail ' + componentId);
239. }
240. if (touch.result) {
241. // 通知Web组件手势事件消费结果。
242. touch.result.setGestureEventResult(ret);
243. }
244. }
245. })
246. })
247. .border({width: 2, color: Color.Gray})
248. .height('50%')
249. }
250. }
251. }
252. }
253. }
```

* 前端页面示例：

  示例代码使用<embed>标签，若使用<object>标签，请在ets侧注册<object>标签及type类型。

  ```
  1. <!--HAP's src/main/resources/rawfile/test4.html-->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <title>同层渲染html</title>
  6. <meta name="viewport" content="initial-scale=1.0">
  7. </head>
  8. <body>
  9. <div>
  10. <div id = "test" style = "position: absolute; z-index: 9999; text-align: center; background-color: rgb(61, 157, 180); top: 40px; left: 30px; width: 300px; height: 120px">
  11. z-index: 9999
  12. </div>

  14. <embed id = "input1" type = "native/view1" arkwebnativestyle = "display:overlay-infinity" style = "position: absolute; top: 60px; left: 50px; width: 300px; height: 100px">

  16. <embed id = "input2" type = "native/view2" arkwebnativestyle = "display:overlay" style = "position: absolute; top: 150px; left: 40px; width: 300px; height: 100px">
  17. </div>
  18. </body>
  19. </html>
  ```
* 实现效果：

  未设置arkwebnativestyle的display属性：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/lvtIKwrWSiOqaeW5rdvHBw/zh-cn_image_0000002558764738.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=2F0F4C925B4D6524F8C55B7739CBBE38A326AEF4E860B87D36BA98CE78909A5C)

  设置arkwebnativestyle的display属性：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/JJkuG9bcSzSF7CwonmgGHQ/zh-cn_image_0000002558605082.png?HW-CC-KV=V1&HW-CC-Date=20260429T052928Z&HW-CC-Expire=86400&HW-CC-Sign=F9888638425D465011B872373618FF6A732126D07FB3233BCBF10191BC31542E)

## 同层渲染纹理贴图对齐方式

ArkWeb同层渲染场景下的私有属性arkwebnativestyle，仅在开启同层渲染后的<embed>和<object>标签中生效，从API version 23开始，增加属性object-fit:stretch（默认值，纹理按同层标签bounds尺寸拉伸对齐），object-fit:none（纹理不拉伸，左顶角对齐）两种配置，用于控制单个同层标签的纹理对齐方式以实现灵活展示效果，适用于同层标签宽高动态变化的场景，可解决标签宽高改变时出现的短暂纹理拉伸问题。

属性取值说明如下：

| 属性取值 | 说明 |
| --- | --- |
| object-fit:stretch | 默认值，纹理按同层标签bounds尺寸拉伸对齐。 |
| object-fit:none | 纹理不拉伸，左顶角对齐。 |

* 应用侧代码：

  ```
  1. // 创建NodeController
  2. import { webview } from '@kit.ArkWeb';
  3. import { UIContext } from '@kit.ArkUI';
  4. import { NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';

  6. @Observed
  7. declare class Params{
  8. elementId: string
  9. textOne: string
  10. textTwo: string
  11. width: number
  12. height: number
  13. }

  15. declare class NodeControllerParams {
  16. surfaceId: string
  17. type: string
  18. renderType: NodeRenderType
  19. embedId: string
  20. width: number
  21. height: number
  22. }

  24. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
  25. class MyNodeController extends NodeController {
  26. private rootNode: BuilderNode<[Params]> | undefined | null;
  27. private embedId_: string = "";
  28. private surfaceId_: string = "";
  29. private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  30. private width_: number = 0;
  31. private height_: number = 0;
  32. private type_: string = "";
  33. private isDestroy_: boolean = false;

  35. setRenderOption(params: NodeControllerParams) {
  36. this.surfaceId_ = params.surfaceId;
  37. this.renderType_ = params.renderType;
  38. this.embedId_ = params.embedId;
  39. this.width_ = params.width;
  40. this.height_ = params.height;
  41. this.type_ = params.type;
  42. }

  44. // 必须要重写的方法，用于构建节点数、返回节点数挂载在对应NodeContainer中。
  45. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
  46. makeNode(uiContext: UIContext): FrameNode | null {
  47. if (this.isDestroy_) { // rootNode为null。
  48. return null;
  49. }
  50. if (!this.rootNode) {// rootNode 为undefined时。
  51. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
  52. if(this.rootNode) {
  53. this.rootNode.build(wrapBuilder(ImageBuilder), {  textOne: "myImage", width: this.width_, height: this.height_  })
  54. return this.rootNode.getFrameNode();
  55. }else{
  56. return null;
  57. }
  58. }
  59. // 返回FrameNode节点。
  60. return this.rootNode.getFrameNode();
  61. }

  63. updateNode(arg: Object): void {
  64. this.rootNode?.update(arg);
  65. }

  67. getEmbedId(): string {
  68. return this.embedId_;
  69. }

  71. setDestroy(isDestroy: boolean): void {
  72. this.isDestroy_ = isDestroy;
  73. if (this.isDestroy_) {
  74. this.rootNode = null;
  75. }
  76. }

  78. postEvent(event: TouchEvent | undefined): boolean {
  79. return this.rootNode?.postTouchEvent(event) as boolean
  80. }

  82. postInputEvent(event: MouseEvent | undefined): boolean {
  83. return this.rootNode?.postInputEvent(event) as boolean
  84. }
  85. }

  87. @Component
  88. struct ImageComponent {
  89. @Prop params: Params
  90. private imageOne: Resource = $rawfile('demo.PNG');
  91. @State src: Resource = this.imageOne

  93. build() {
  94. Column(){
  95. Image(this.src)
  96. }
  97. .width(this.params.width)
  98. .height(this.params.height)
  99. }
  100. }

  103. // @Builder中为动态组件的具体组件内容。
  104. @Builder
  105. function ImageBuilder(params:Params) {
  106. ImageComponent({params: params})
  107. }

  109. @Entry
  110. @Component
  111. struct Page{
  112. browserTabController: WebviewController = new webview.WebviewController()
  113. private nodeControllerMap: Map<string, MyNodeController> = new Map();
  114. @State componentIdArr: Array<string> = [];
  115. @State widthMap: Map<string, number> = new Map();
  116. @State heightMap: Map<string, number> = new Map();
  117. @State positionMap: Map<string, Edges> = new Map();
  118. @State edges: Edges = {};
  119. uiContext: UIContext = this.getUIContext();

  121. build() {
  122. Row() {
  123. Column() {
  124. Stack() {
  125. ForEach(this.componentIdArr, (componentId: string) => {
  126. NodeContainer(this.nodeControllerMap.get(componentId))
  127. .position(this.positionMap.get(componentId))
  128. .width(this.widthMap.get(componentId))
  129. .height(this.heightMap.get(componentId))
  130. }, (embedId: string) => embedId)
  131. // Web组件加载本地text.html页面。
  132. Web({src: $rawfile("test.html"), controller: this.browserTabController})
  133. // 配置同层渲染开关开启。
  134. .enableNativeEmbedMode(true)
  135. // 获取<embed>标签的生命周期变化数据。
  136. .onNativeEmbedLifecycleChange((embed) => {
  137. console.info("NativeEmbed surfaceId" + embed.surfaceId);
  138. // 如果使用embed.info.id作为映射nodeController的key，请在h5页面显式指定id。
  139. const componentId = embed.info?.id?.toString() as string
  140. if (embed.status == NativeEmbedStatus.CREATE) {
  141. console.info("NativeEmbed create" + JSON.stringify(embed.info));
  142. // 创建节点控制器、设置参数。
  143. let nodeController = new MyNodeController()
  144. // embed.info.width和embed.info.height单位是px格式，需要转换成ets侧的默认单位vp。
  145. nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
  146. type : embed.info?.type as string,
  147. renderType : NodeRenderType.RENDER_TYPE_TEXTURE,
  148. embedId : embed.embedId as string,
  149. width : this.uiContext.px2vp(embed.info?.width),
  150. height : this.uiContext.px2vp(embed.info?.height)})
  151. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
  152. nodeController.setDestroy(false);
  153. //根据web传入的embed的id属性作为key，将nodeController存入Map。
  154. this.nodeControllerMap.set(componentId, nodeController);
  155. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
  156. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
  157. this.positionMap.set(componentId, this.edges);
  158. // 将web传入的embed的id属性存入@State状态数组变量中，用于动态创建nodeContainer节点容器,需要将push动作放在set之后。
  159. this.componentIdArr.push(componentId)
  160. } else if (embed.status == NativeEmbedStatus.UPDATE) {
  161. let nodeController = this.nodeControllerMap.get(componentId);
  162. console.info("NativeEmbed update" + JSON.stringify(embed));
  163. this.edges = {left: `${embed.info?.position?.x as number}px`, top: `${embed.info?.position?.y as number}px`}
  164. this.positionMap.set(componentId, this.edges);
  165. this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
  166. this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
  167. interface UpdateNodeParams {
  168. textOne: string;
  169. width: number;
  170. height: number;
  171. }
  172. const updateParams: UpdateNodeParams = {
  173. textOne: 'update',
  174. width: this.uiContext.px2vp(embed.info?.width),
  175. height: this.uiContext.px2vp(embed.info?.height)
  176. }
  177. nodeController?.updateNode(updateParams);
  178. } else if (embed.status == NativeEmbedStatus.DESTROY) {
  179. console.info("NativeEmbed destroy" + JSON.stringify(embed));
  180. let nodeController = this.nodeControllerMap.get(componentId);
  181. nodeController?.setDestroy(true);
  182. this.nodeControllerMap.delete(componentId);
  183. this.positionMap.delete(componentId);
  184. this.widthMap.delete(componentId);
  185. this.heightMap.delete(componentId);
  186. this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
  187. } else {
  188. console.info("NativeEmbed status" + embed.status);
  189. }
  190. })
  191. }
  192. }
  193. }
  194. }
  195. }
  ```
* 前端页面示例：

  示例代码使用<embed>标签，若使用<object>标签，请在ets侧注册<object>标签及type类型。

  ```
  1. <!--HAP's src/main/resources/rawfile/test.html-->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <title>同层渲染测试html</title>
  6. </head>
  7. <body>
  8. <div>
  9. <!-- 属性设置为object-fit:none，纹理不拉伸，左顶角对齐。-->
  10. <embed id="nativeVideo"
  11. type="native/camera"
  12. arkwebnativestyle="object-fit:none"/>
  13. </div>
  14. </body>
  15. </html>
  ```

## 常见问题

### 同层渲染组件被拉伸该如何解决？

* 组件高度过大

  受GPU限制，同层标签存在8000px的高度限制，如果html5中同层标签高度过高，会存在组件被拉伸的情况，这时需要将同层标签的高度设为8000px以下。
* 自定义组件宽高未指定为同层渲染标签的宽高

  自定义的同层渲染组件宽高需要与同层标签的宽高保持一致，示例如下：

  ```
  1. @Component
  2. struct TextInputComponent {
  3. @Prop params: Params
  4. @State bkColor: Color = Color.White

  6. build() {
  7. Column() {
  8. TextInput({text: '', placeholder: 'please input your word...'})
  9. .fontColor(Color.Black)
  10. }
  11. // 自定义组件中的最外层容器组件宽高应该为同层标签的宽高。
  12. .width(this.params.width)
  13. .height(this.params.height)
  14. }
  15. }
  ```

### 如何将同层渲染组件捕获到的事件透传到web前端？

同层渲染手势事件通过[setGestureEventResult()](../harmonyos-references/arkts-basic-components-web-eventresult.md#setgestureeventresult14)设置手势事件消费结果，可以选择系统组件侧或ArkWeb侧消费手势事件。如果要实现系统组件侧和ArkWeb侧同时消费手势事件，可以在[setGestureEventResult()](../harmonyos-references/arkts-basic-components-web-eventresult.md#setgestureeventresult14)中将stopPropagation设置为false，即系统组件侧消费的同时可以将手势事件向上冒泡给ArkWeb。

### 同层渲染页面显示该插件不支持该如何解决？

* 同层渲染开关[enableNativeEmbedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#enablenativeembedmode11)未开启

  使用同层渲染技术需要显式开启同层渲染开关

  ```
  1. Web({ src: $rawfile("text.html"), controller: this.controller })
  2. // 配置同层渲染开关开启。
  3. .enableNativeEmbedMode(true)
  ```
* 同层标签使用有误

  如果使用<embed>标签，需要显式书写embed，并且type类型以"native/"开头；如果使用<object>标签，需要注册<object>标签及type类型。

### 涉及界面交互的ArkUI组件（如TextInput等）光标与输入框错位该如何解决？

首先，需使用Stack包裹同层组件容器和BuilderNode。其次，同层组件容器NodeContainer应与同层标签的位置绑定。示例如下：

```
1. ForEach(this.componentIdArr, (componentId: string) => {
2. NodeContainer(this.nodeControllerMap.get(componentId))
3. // 同层组件容器应与同层标签的宽高和位置绑定。
4. .position(this.positionMap.get(componentId))
5. .width(this.widthMap.get(componentId))
6. .height(this.heightMap.get(componentId))
7. }, (embedId: string) => embedId)
```
