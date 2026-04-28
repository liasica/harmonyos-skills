---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-unified-drag-and-drop
title: 统一拖拽
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 统一拖拽
category: best-practices
scraped_at: 2026-04-28T08:22:10+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:99e63403ecc7f846568d28dfd51bb1d9810fd9efb041576235546f099075b0b0
---

## 概述

拖拽操作是一种直观且高效的数据传输方式，它允许用户通过手势（如用手指、鼠标或触控笔按住并移动）在应用程序之间及其内部进行数据传输。拖拽功能不仅操作便捷，还能与多种系统能力深度融合，从而拓展出更为广泛的应用场景。例如，跨设备拖拽功能使得用户能够在不同设备间无缝传输数据，而跨窗口拖拽则提高了多任务处理的灵活性。此外，基于拖拽操作还可以开发出更多创新性应用场景，如AI智能识别、水印添加等，这些创新性的功能统称为“统一拖拽”。

拖拽过程中的数据传输基于统一数据管理框架（Unified Data Management Framework，UDMF）实现，UDMF为多对多跨应用数据共享场景提供了[标准化数据通路](../harmonyos-references/js-apis-data-unifieddatachannel.md)和[标准化数据结构](../harmonyos-references/js-apis-data-uniformdatastruct.md)。统一数据对象[UnifiedData](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifieddata)提供了封装一组数据记录的方法，其中数据记录[UnifiedRecord](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifiedrecord)可为一条HTML记录、一条图片记录等。UnifiedRecord支持调用[addEntry()](../harmonyos-references/js-apis-data-unifieddatachannel.md#addentry15)接口在当前数据记录中添加指定数据类型和内容的数据，通过此方法增加的数据类型和内容代表同一内容的不同表现形式。例如，对于一段文字，可以构造html和text两种样式的entry。通过这种方式，接收方能够按需选择接收。

本文结合不同的场景，提供具体的示例方案，帮助开发者更好地理解和应用拖拽技术。

通过设置组件的拖拽响应，可以自定义拖出数据、拖入数据和拖拽背板图，实现如下场景：

* [拖拽图像增加水印](bpta-unified-drag-and-drop.md#section197593813453)：为拖拽的图像添加水印，水印内容为图像的拖拽时间。开发者可以在应用时根据需求自定义水印内容，例如标记拖拽图片的来源信息，为图像管理与溯源提供便利。
* [自定义拖拽背板图](bpta-unified-drag-and-drop.md#section350662014143)：将拖拽过程中的背板图设置为自定义数据内容。开发者可根据个性化需求打造独特的拖拽视觉效果。
* [AI识别拖拽内容](bpta-unified-drag-and-drop.md#section4125035104613)：通过在接收拖拽内容时增加AI识别功能，使得只能显示文字的组件可以接收图片拖拽并显示图片中的文字信息。开发者可以将此能力应用于拖拽识图搜索。

对于文件的拖拽，可以分为在线文件拖拽和本地文件拖拽：

* [在线文件拖拽保存](bpta-unified-drag-and-drop.md#section17176101812472)：拖拽在线的文件，落入方根据业务需要选择是否将文件下载到本地。
* [本地文件拖拽保存](bpta-unified-drag-and-drop.md#section722512624716)：拖拽本地的文件，落入方调用[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取数据，根据需要选择是否将文件保存到落入方沙箱路径。

对于图文混排内容的拖拽，可以使用Text组件、RichEditor组件呈现图文混排的内容，在拖拽时构造多条UnifiedRecord记录。在落入方接收多条Record记录。为了适配落入方不同的接收格式，可以为UnifiedRecord构造多条entry数据，在落入方根据需要解析出不同的entry数据。

* [基于Text组件的图文混排拖拽](bpta-unified-drag-and-drop.md#section164891641978)：基于Text组件呈现图文混排内容，落入方基于UDMF多Record接收数据。
* [基于RichEditor组件的图文混排拖拽](bpta-unified-drag-and-drop.md#section85351118482)：基于RichEditor组件呈现图文混排内容，落入方基于UDMF多Record接收数据。
* [基于UDMF多Entry的图文混排拖拽](bpta-unified-drag-and-drop.md#section5352104013812)：基于RichEditor组件呈现图文混排内容，拖出方手动构造UDMF多Entry数据，落入方基于UDMF多Record接收数据，并适配UDMF多Entry数据的接收。

将拖拽框架与系统的分屏能力、键鼠穿越能力、小艺及中转站结合，可以实现如下场景：

* [分屏拖拽](bpta-unified-drag-and-drop.md#section35671536195312)：演示了分屏拖拽的功能，可以在分屏中打开两个不同的应用，实现跨应用拖拽。
* [跨设备拖拽](bpta-unified-drag-and-drop.md#section15501112385010)：演示了基于键鼠穿越能力的跨设备拖拽，可以在平板和2in1设备中使用此功能以直观便捷地交换数据。
* [拖入小艺和中转站](bpta-unified-drag-and-drop.md#section1289155519508)：演示了小艺和中转站与拖拽框架结合的能力，可以利用中转站暂存拖拽内容或进行跨设备拖拽，也可以利用小艺的AI对话式分析能力处理拖拽内容。

## 开发流程

[拖拽的流程](../design-guides/hmi-scenes-drag-0000001795410277.md#section1417334354817)可以分为三部分：发起拖拽、拖拽中和释放拖拽。其中，拖出方通过[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)和[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)等接口处理拖出数据，拖入方通过[allowDrop()](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)和[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)等接口处理拖入数据，拖拽数据使用UDMF统一数据对象[UnifiedData](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifieddata)进行封装。

**表1** 拖拽流程展示

| 发起拖拽 | 拖拽中 | 释放拖拽 |
| --- | --- | --- |
|  |  |  |

### 发起拖拽

[默认支持拖出能力的组件](../harmonyos-references/ts-universal-events-drag-drop.md)，如[Search](../harmonyos-references/ts-basic-components-search.md)、[Hyperlink](../harmonyos-references/ts-container-hyperlink.md)等，在拖出时会使用组件的默认拖出响应。其中[Search](../harmonyos-references/ts-basic-components-search.md)组件默认拖拽内容为选中的文字，[Hyperlink](../harmonyos-references/ts-container-hyperlink.md)组件默认拖拽内容为超链接地址。如果想自定义组件的拖拽内容，需要在组件的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中将自定义数据封装成[UnifiedData](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifieddata)数据对象，通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setData()](../harmonyos-references/ts-universal-events-drag-drop.md#setdata10)接口设置拖出数据。对于其他非默认组件或自定义组件，如果想实现其拖出功能，需要将组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性设置为true，并自定义组件的拖拽内容。以RichEditor组件为例：

```
1. RichEditor({ controller: this.sourceController })
2. // ...
3. .onDragStart((event) => {
4. try {
5. const selection = this.sourceController.getSelection();
6. // construct drag data
7. this.buildUnifiedRecords(selection);
8. event.setData(this.unifiedData);
9. } catch (error) {
10. const err = error as BusinessError;
11. hilog.error(0x0000, TAG, `%{public}s`, err.code, err.message);
12. }
13. })
14. // ...
```

[MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L275-L316)

可以在[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中处理拖拽信息，例如为图片添加水印，详情见[拖拽图像增加水印](bpta-unified-drag-and-drop.md#section197593813453)。

### 拖拽中

通过标准手势发起拖拽后，系统会默认将组件本身的截图作为[拖拽背板图](../harmonyos-guides/arkts-common-events-drag-event.md#拖拽背板图)。如果想自定义拖拽背板图，需要在组件的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调中设置[DragItemInfo](../harmonyos-references/ts-universal-events-drag-drop.md#dragiteminfo)，传入自定义背板图。此外，可以在拖拽目标组件上注册[onDragMove()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove)监听，并在回调函数中实时获取拖拽过程中的信息，如拖拽点的坐标等。以Image组件为例，示例代码如下：

自定义拖拽背板图

```
1. Image($r('app.media.mount'))
2. // ...
3. .onDragStart(() => {
4. let dragItemInfo: DragItemInfo = {
5. pixelMap: this.pixelMap,
6. builder: () => {
7. this.pixelMapBuilder()
8. },
9. };
10. return dragItemInfo;
11. })
12. // ...
```

[Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L99-L142)

可以将拖拽背板图设置为自定义的图片或者文字，详情见[自定义拖拽背板图](bpta-unified-drag-and-drop.md#section350662014143)。

获取拖拽移动中的坐标等信息

```
1. Column() {
2. // ...
3. }
4. // ...
5. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
6. .onDrop((event?: DragEvent) => {
7. // ...
8. })
9. .onDragMove((event: DragEvent) => {
10. hilog.info(0x0000, TAG, `The x-coordinate of the display is ${event.getDisplayX()}.`);
11. hilog.info(0x0000, TAG, `The y-coordinate of the display is ${event.getDisplayY()}.`);
12. hilog.info(0x0000, TAG, `The x-coordinate of the window is ${event.getWindowX()}.`);
13. hilog.info(0x0000, TAG, `The y-coordinate of the window is ${event.getWindowY()}.`);
14. })
```

[Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L157-L209)

说明

只有监听了[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)事件，拖拽在组件范围内移动时，才会触发[onDragMove()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove)事件。

### 释放拖拽

[默认支持拖入能力的组件](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)，如[Search](../harmonyos-references/ts-basic-components-search.md)组件等，将目标拖入组件区域内会使用默认拖入响应。如果想自定义组件的拖入响应，需要将组件的[allowDrop()](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)属性设置为允许拖入的数据类型，并在其[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)接口获取拖入数据后，读取其中的UnifiedRecord记录的集合。对于每条记录，调用[getTypes()](../harmonyos-references/js-apis-data-unifieddatachannel.md#gettypes12)方法获取其中包含的数据类型，取出所需要的数据。以Text组件获取拖拽文字为例：

```
1. Column() {
2. Text(this.dropContent)
3. // ...
4. }
5. // ...
6. .allowDrop([uniformTypeDescriptor.UniformDataType.TEXT,
7. uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
8. .onDrop((event: DragEvent) => {
9. try {
10. let dragData = event.getData();
11. let records = dragData.getRecords();
12. for (let record of records) {
13. let types = record.getTypes();
14. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
15. const plainTextUds =
16. record.getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
17. this.dropContent = plainTextUds.textContent;
18. event.setResult(DragResult.DRAG_SUCCESSFUL);
19. }
20. }
21. }
22. // ...
23. })
```

[TextInput.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textInput/TextInput.ets#L78-L123)

可以在[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中处理接收到的数据，例如将图片识别为文字以显示在只支持文字的组件上，详情见[AI识别拖拽内容](bpta-unified-drag-and-drop.md#section4125035104613)。

## 拖拽图像增加水印

在拖拽过程中，可以自定义拖出响应，为拖拽图像增加水印，以标识图像的相关信息。下面以在图像中增加拖拽时间水印为例，介绍实现原理。

**运行效果**

**图1** 拖拽图片增加水印  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/NMye_NrIQcir7dg_t7m5pQ/zh-cn_image_0000002315615638.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=610770206054A7DB01FE4DA646FA330B18FD34C4846B487143FBBA03C05202ED "点击放大")

**实现原理**

在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中获取图像信息，调用系统绘制能力[drawing](../harmonyos-references/js-apis-graphics-drawing.md)在图像上绘制水印，通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setData()](../harmonyos-references/ts-universal-events-drag-drop.md#setdata10)接口将水印图像设置为拖拽数据。

**开发步骤**

1. 将拖出方Image组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性设置为true。

   ```
   1. Image($rawfile('river.png'))
   2. // ...
   3. .draggable(true)
   ```

   [Watermark.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/watermark/Watermark.ets#L145-L158)
2. 在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中，获取图像信息并将其转换成[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

   ```
   1. Image($rawfile('river.png'))
   2. // ...
   3. .onDragStart((event: DragEvent) => {
   4. const resourceMgr: resourceManager.ResourceManager = this.context!.resourceManager;
   5. let rawFileDescriptor = resourceMgr.getRawFdSync('river.png');
   6. const imageSourceApi: image.ImageSource = image.createImageSource(rawFileDescriptor);
   7. let pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync();
   8. // ...
   9. })
   ```

   [Watermark.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/watermark/Watermark.ets#L146-L199)
3. 将图片绘制到[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布上，并获取拖拽时间作为水印绘制到画布上的指定位置，得到添加水印的图像。

   ```
   1. Image($rawfile('river.png'))
   2. // ...
   3. .onDragStart((event: DragEvent) => {
   4. // ...
   5. this.time = this.getTimeWatermark(systemDateTime.getTime(false));
   6. let markPixelMap: image.PixelMap = this.addWaterMark(this.time, pixelMap);
   7. // ...
   8. })
   ```

   [Watermark.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/watermark/Watermark.ets#L147-L200)

   ```
   1. addWaterMark(watermark: string, pixelMap: image.PixelMap) {
   2. try {
   3. if (!canIUse('SystemCapability.Graphics.Drawing')) {
   4. hilog.error(0x0000, TAG, `%{public}s`, `watermark is not supported`);
   5. return pixelMap;
   6. }
   7. watermark = this.context!.resourceManager.getStringSync($r('app.string.drag_time').id) + watermark;
   8. const imageInfo: image.Size = pixelMap.getImageInfoSync().size;
   9. const imageWidth: number = imageInfo.width;
   10. const imageHeight: number = imageInfo.height;
   11. const imageScale: number = imageWidth / display.getDefaultDisplaySync().width;
   12. const canvas: drawing.Canvas = new drawing.Canvas(pixelMap);
   13. const pen: drawing.Pen = new drawing.Pen();
   14. const brush: drawing.Brush = new drawing.Brush();
   15. pen.setColor({
   16. alpha: 102,
   17. red: 255,
   18. green: 255,
   19. blue: 255
   20. });
   21. brush.setColor({
   22. alpha: 102,
   23. red: 255,
   24. green: 255,
   25. blue: 255
   26. });
   27. const font: drawing.Font = new drawing.Font();
   28. font.setSize(48 * imageScale);
   29. let textWidth: number = font.measureText(watermark, drawing.TextEncoding.TEXT_ENCODING_UTF8);
   30. const textBlob: drawing.TextBlob =
   31. drawing.TextBlob.makeFromString(watermark, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
   32. canvas.attachBrush(brush);
   33. canvas.attachPen(pen);
   34. canvas.drawTextBlob(textBlob, imageWidth - 24 * imageScale - textWidth, imageHeight - 32 * imageScale);
   35. canvas.detachBrush();
   36. canvas.detachPen();
   37. } catch (error) {
   38. hilog.error(0x0000, TAG, '%{public}s', 'addWaterMark failed:', (error as BusinessError).message);
   39. }
   40. return pixelMap;
   41. }
   ```

   [Watermark.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/watermark/Watermark.ets#L95-L136)
4. 将图像打包保存在文件中，调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setData()](../harmonyos-references/ts-universal-events-drag-drop.md#setdata10)接口将水印图像设置为拖拽数据。

   ```
   1. Image($rawfile('river.png'))
   2. // ...
   3. .onDragStart((event: DragEvent) => {
   4. // ...
   5. let packOpts: image.PackingOption = { format: 'image/png', quality: 20 };
   6. let file: fs.File =
   7. fs.openSync(`${this.context!.filesDir}/watermark.png`, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
   8. const imagePackerApi: image.ImagePacker = image.createImagePacker();
   9. imagePackerApi.packToFile(markPixelMap, file.fd, packOpts);
   10. imagePackerApi?.release();
   11. let imgData: uniformDataStruct.FileUri = {
   12. uniformDataType: 'general.file-uri',
   13. oriUri: fileUri.getUriFromPath(`${this.context!.filesDir}/watermark.png`),
   14. fileType: 'general.image'
   15. }
   16. let unifiedRecord =
   17. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, imgData);
   18. let unifiedData = new unifiedDataChannel.UnifiedData(unifiedRecord);
   19. event.setData(unifiedData);
   20. fs.closeSync(file.fd);
   21. // ...
   22. })
   ```

   [Watermark.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/watermark/Watermark.ets#L148-L201)

## 自定义拖拽背板图

[拖拽背板图](../harmonyos-guides/arkts-common-events-drag-event.md#拖拽背板图)用于在拖拽过程中展示用户拖动的数据，可以自定义拖拽背板图。

**运行效果**

**图2** 自定义拖拽背板  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/7Egk3hUhRdSjhpjpk39_3g/zh-cn_image_0000002349574333.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=3799CC15F9482814398BAB649C20F2603F19541F0177211B74FF9C7F133DFF53 "点击放大")

**实现原理**

在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中，自定义[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)作为拖拽过程中的背板图。

**开发步骤**

1. 创建自定义组件。

   ```
   1. @Builder
   2. pixelMapBuilder() {
   3. Column() {
   4. Text($r('app.string.background_content'))
   5. .fontSize('16fp')
   6. .margin({
   7. left: '16vp',
   8. right: '16vp',
   9. top: '8vp',
   10. bottom: '8vp'
   11. })
   12. }
   13. .backgroundColor($r('sys.color.comp_background_primary'))
   14. .borderRadius(16)
   15. }
   ```

   [Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L45-L60)
2. 将自定义组件转换成PixelMap，作为拖拽过程中显示的图片。

   ```
   1. private getComponentSnapshot(): void {
   2. this.getUIContext().getComponentSnapshot().createFromBuilder(() => {
   3. this.pixelMapBuilder()
   4. }, (error: Error, pixmap: image.PixelMap) => {
   5. if (error) {
   6. hilog.error(0x0000, TAG, `%{public}s`, error.message);
   7. return;
   8. }
   9. this.pixelMap = pixmap;
   10. })
   11. }
   ```

   [Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L64-L75)

   说明

   由于[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)需要离线渲染之后才能使用，存在一定的性能开销和时延，因此推荐开发者优先使用[DragItemInfo](../harmonyos-references/ts-universal-events-drag-drop.md#dragiteminfo)中的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)方式返回背板图。
3. 在拖出对象的[onPreDrag()](../harmonyos-references/ts-universal-events-drag-drop.md#onpredrag12)接口中，预先创建背板图。

   ```
   1. Image($r('app.media.mount'))
   2. // ...
   3. .onPreDrag((status: PreDragStatus) => {
   4. this.PreDragChange(status);
   5. })
   6. // ...
   ```

   [Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L98-L140)

   ```
   1. private PreDragChange(preDragStatus: PreDragStatus): void {
   2. if (preDragStatus == PreDragStatus.ACTION_DETECTING_STATUS) {
   3. this.getComponentSnapshot();
   4. }
   5. }
   ```

   [Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L79-L84)
4. 在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中，将回调的PixelMap作为拖拽过程中的背板图。

   ```
   1. Image($r('app.media.mount'))
   2. // ...
   3. .onDragStart(() => {
   4. let dragItemInfo: DragItemInfo = {
   5. pixelMap: this.pixelMap,
   6. builder: () => {
   7. this.pixelMapBuilder()
   8. },
   9. };
   10. return dragItemInfo;
   11. })
   12. // ...
   ```

   [Background.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/background/Background.ets#L97-L141)

## AI识别拖拽内容

在拖拽过程中，可以自定义拖入响应，以识别拖拽内容并将其输出在释放区内。本章节以通过AI识别拖拽图像中的文字为例，介绍实现原理。

**运行效果**

**图3** AI识别拖拽内容  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/LhPsxYUZQC-VsLosjQI4ow/zh-cn_image_0000002349614541.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=7C6708364F1EFA988CF03CF32BEF679006002C84C8C91167207CA64A87F7C958 "点击放大")

**实现原理**

在拖入对象的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中，通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)接口获取拖拽数据后，调用系统能力[textRecognition（文字识别）](../harmonyos-references/core-vision-text-recognition-api.md)得到图像中的文字信息。

**开发步骤**

1. 在拖拽释放区域的[allowDrop()](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)接口中设置允许拖入的数据类型为[uniformTypeDescriptor.UniformDataType.IMAGE](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformdatatype)。

   ```
   1. Column() {
   2. Text(this.textContent)
   3. // ...
   4. }
   5. // ...
   6. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
   7. // ...
   ```

   [AIRecognition.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/aiRecognition/AIRecognition.ets#L80-L184)
2. 在拖入对象的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中，调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)接口获取拖拽数据。

   ```
   1. Column() {
   2. Text(this.textContent)
   3. // ...
   4. }
   5. // ...
   6. .onDrop(async (event?: DragEvent) => {
   7. try {
   8. let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
   9. if (dragData === undefined) {
   10. hilog.info(0x0000, TAG, `%{public}s`, `ondrop undefined data`);
   11. return;
   12. }
   13. let records: unifiedDataChannel.UnifiedRecord[] = dragData.getRecords();
   14. // ...
   15. } catch (error) {
   16. const err = error as BusinessError;
   17. hilog.error(0x0000, TAG, `onDrop error, error code: ${err.code}, errorMessage: ${err.message}`);
   18. }
   19. })
   ```

   [AIRecognition.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/aiRecognition/AIRecognition.ets#L81-L185)
3. 将拖拽数据转换成颜色数据格式为BGRA\_8888的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)类型的视觉信息。

   ```
   1. Column() {
   2. Text(this.textContent)
   3. // ...
   4. }
   5. // ...
   6. .onDrop(async (event?: DragEvent) => {
   7. try {
   8. // ...
   9. for (let i = 0; i < records.length; i++) {
   10. let types = records[i].getTypes();
   11. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
   12. const fileUriUds =
   13. records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
   14. let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
   15. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
   16. const resourceReg = new RegExp('resource');
   17. if (resourceReg.test(fileUriUds.oriUri)) {
   18. const numberReg = new RegExp('[0-9]+');
   19. let idArray = fileUriUds.oriUri.match(numberReg);
   20. if (idArray !== null) {
   21. let id = idArray[0];
   22. let drawableDescriptor =
   23. this.context.getHostContext()!.resourceManager.getDrawableDescriptor(Number(id), 0, 1);
   24. let pixelMapInit = drawableDescriptor.getPixelMap() as image.PixelMap;
   25. let imageHeight = pixelMapInit.getImageInfoSync().size.height;
   26. let imageWidth = pixelMapInit.getImageInfoSync().size.width;
   27. const readBuffer: ArrayBuffer = new ArrayBuffer(imageHeight * imageWidth * 4);
   28. pixelMapInit.readPixelsToBufferSync(readBuffer);
   29. let opts: image.InitializationOptions = {
   30. editable: true,
   31. size: { height: imageHeight, width: imageWidth },
   32. srcPixelFormat: pixelMapInit.getImageInfoSync().pixelFormat,
   33. pixelFormat: 3,
   34. alphaType: pixelMapInit.getImageInfoSync().alphaType,
   35. scaleMode: 0
   36. };
   37. let pixelMap: image.PixelMap = image.createPixelMapSync(readBuffer, opts);
   38. // ...
   39. }
   40. }
   41. }
   42. }
   43. }
   44. } catch (error) {
   45. const err = error as BusinessError;
   46. hilog.error(0x0000, TAG, `onDrop error, error code: ${err.code}, errorMessage: ${err.message}`);
   47. }
   48. })
   ```

   [AIRecognition.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/aiRecognition/AIRecognition.ets#L82-L183)
4. 调用系统文字识别能力textRecognition获取拖拽数据中的文字信息。

   ```
   1. Column() {
   2. Text(this.textContent)
   3. // ...
   4. }
   5. // ...
   6. .onDrop(async (event?: DragEvent) => {
   7. try {
   8. // ...
   9. for (let i = 0; i < records.length; i++) {
   10. let types = records[i].getTypes();
   11. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
   12. // ...
   13. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
   14. // ...
   15. if (resourceReg.test(fileUriUds.oriUri)) {
   16. // ...
   17. if (idArray !== null) {
   18. // ...
   19. let visionInfo: textRecognition.VisionInfo = { pixelMap: pixelMap };
   20. let data = await textRecognition.recognizeText(visionInfo);
   21. let recognitionString = data.value;
   22. this.textContent = recognitionString;
   23. }
   24. }
   25. }
   26. }
   27. }
   28. } catch (error) {
   29. const err = error as BusinessError;
   30. hilog.error(0x0000, TAG, `onDrop error, error code: ${err.code}, errorMessage: ${err.message}`);
   31. }
   32. })
   ```

   [AIRecognition.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/aiRecognition/AIRecognition.ets#L83-L181)

## 文件拖拽

文件拖拽操作可分为在线文件拖拽和本地文件拖拽。

在线文件拖拽时，拖出方需提供文件的下载地址，下载操作由落入方处理。若业务需求要求在拖出方完成下载，则需将下载与拖拽操作分开处理，确保文件在拖出前已完成下载，以避免拖出失败。

对于本地文件的拖拽，建议构造FileUri类型的数据进行拖拽。在文件落入时，应通过调用[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取数据，如需将文件保存在本地，可设置[datasyncoptions](../harmonyos-references/ts-universal-events-drag-drop.md#datasyncoptions15)参数的destUri值，将文件保存至本地沙箱路径中。

## 在线文件拖拽保存

以在线图片为例，拖出放Image组件绑定了在线的图片资源。通过拖拽将图片移至目标区域展示，目标区域可选择是否将图片资源下载到本地。

**运行效果**

**图4** 在线图片拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/gsP-GRmIQniTk7Pam6O81Q/zh-cn_image_0000002315775454.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=95A4EAA38732888E58B105DAE3A0569EB3879B7A521B9CD737144448D970B3FB "点击放大")

**使用说明**

加载在线图片资源需在工程module.json5文件中添加网络权限。

**实现原理**

在落入方[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调中获取拖拽数据，得到访问图片的链接，同时根据业务需要选择是否将图片下载到本地。本示例模拟了需要下载的场景。

**开发步骤：**

1. 开启网络权限。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.INTERNET",
   4. "reason": "$string:internet_reason",
   5. "usedScene": {
   6. "abilities": [
   7. "EntryAbility"
   8. ],
   9. "when": "inuse"
   10. }
   11. }
   12. ],
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/module.json5#L63-L74)
2. 设置拖出方Image组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性为true。

   ```
   1. Image('https://www-file.huawei.com/-/media/corp2020/home/banner/12/pura-x-1.jpg')
   2. // ...
   3. .draggable(true)
   4. // ...
   ```

   [OnlineImage.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/onlineimage/OnlineImage.ets#L53-L69)
3. 在落入方Image组件的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调中获取图片的uri，绑定到落入方组件上，触发UI刷新。

   ```
   1. Column() {
   2. Image(this.targetImage)
   3. // ...
   4. }
   5. // ...
   6. .onDrop((event?: DragEvent) => {
   7. try {
   8. let dragData = event?.getData() as unifiedDataChannel.UnifiedData;
   9. if (dragData) {
   10. let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
   11. for (let i = 0; i < records.length; i++) {
   12. let types = records[i].getTypes();
   13. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
   14. const fileUriUds =
   15. records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
   16. let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
   17. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
   18. this.targetImage = fileUriUds.oriUri;
   19. // ...
   20. }
   21. }
   22. }
   23. }
   24. }
   25. // ...
   26. });
   ```

   [OnlineImage.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/onlineimage/OnlineImage.ets#L84-L148)
4. 在落入方Image组件的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里调用[request](../harmonyos-references/js-apis-request.md#导入模块)的[downloadFile()](../harmonyos-references/js-apis-request.md#requestdownloadfile9)方法下载图片资源。

   ```
   1. Column() {
   2. Image(this.targetImage)
   3. // ...
   4. }
   5. // ...
   6. .onDrop((event?: DragEvent) => {
   7. try {
   8. let dragData = event?.getData() as unifiedDataChannel.UnifiedData;
   9. if (dragData) {
   10. let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
   11. for (let i = 0; i < records.length; i++) {
   12. let types = records[i].getTypes();
   13. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
   14. // ...
   15. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
   16. // ...
   17. request.downloadFile(this.context, {
   18. url: fileUriUds.oriUri,
   19. filePath: this.filesDir + '/test.png'
   20. }).then(() => {
   21. const file = fileIo.openSync(this.filesDir + '/test.png', fileIo.OpenMode.READ_WRITE);
   22. const arrayBuffer = new ArrayBuffer(1024);
   23. const readLen = fileIo.readSync(file.fd, arrayBuffer);
   24. buffer.from(arrayBuffer, 0, readLen);
   25. fileIo.closeSync(file);
   26. }).catch((error: BusinessError) => {
   27. hilog.error(0x0000, TAG, `%{public}s`, error.code, error.message);
   28. })
   29. }
   30. }
   31. }
   32. }
   33. }
   34. // ...
   35. });
   ```

   [OnlineImage.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/onlineimage/OnlineImage.ets#L85-L149)

## 本地文件拖拽保存

本示例展示拖拽本地的文件，以$rawfile目录下的视频文件为例。

**运行效果**

**图5** 本地视频拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/5ncRH5DgRV6wpnDf1-Z0MA/zh-cn_image_0000002315615654.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=7C380DB84C1C023B134F717A66A3F2A09B6105218C64E575643D53FA724EC6D9 "点击放大")

**实现原理**

为了实现文件的拖拽，通常会构建一个[uniformDataStruct.FileUri](../harmonyos-references/js-apis-data-uniformdatastruct.md#fileuri15)类型的数据对象，传入文件的uri，并通过设置fileType属性来区分不同的文件类型。在接收方的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调函数中获取uri，进而访问该文件。建议使用UDMF的[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取文件，并展示获取进度。如果接收方需要将文件拷贝到本地，可以通过向参数[datasyncoptions](../harmonyos-references/ts-universal-events-drag-drop.md#datasyncoptions15)传入destUri来指定目标路径，UDMF将会把文件拷贝至该路径。

**实现步骤：**

1. 设置拖出方Video组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性为true。

   ```
   1. Video({
   2. src: $rawfile('video.mp4'),
   3. controller: new VideoController()
   4. })
   5. // ...
   6. .draggable(true)
   7. // ...
   ```

   [LocalVideo.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/localvideo/LocalVideo.ets#L50-L94)
2. 在拖出视频的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调中，将视频文件复制到沙箱目录。构造[uniformDataStruct.FileUri](../harmonyos-references/js-apis-data-uniformdatastruct.md#fileuri15)类型的数据，将oriUri设置为沙箱路径下视频文件的uri。

   ```
   1. Video({
   2. src: $rawfile('video.mp4'),
   3. controller: new VideoController()
   4. })
   5. // ...
   6. .onDragStart((event: DragEvent) => {
   7. try {
   8. let data = this.context!.resourceManager.getRawFdSync('video.mp4');
   9. let filePath = this.context?.filesDir + '/video.mp4';
   10. let dest = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
   11. let bufferSize = data.length as number;
   12. let buf = new ArrayBuffer(bufferSize);
   13. fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
   14. fileIo.writeSync(dest.fd, buf, { offset: 0, length: bufferSize });
   15. fileIo.close(dest.fd);
   16. this.context!.resourceManager.closeRawFd('video.mp4');
   17. this.originalVideoUri = fileUri.getUriFromPath(filePath);
   18. let unifiedData = new unifiedDataChannel.UnifiedData();
   19. let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
   20. let video: uniformDataStruct.FileUri = {
   21. uniformDataType: 'general.file-uri',
   22. oriUri: this.originalVideoUri,
   23. fileType: 'general.video'
   24. }
   25. unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.VIDEO, video);
   26. unifiedData.addRecord(unifiedRecord);
   27. event.setData(unifiedData);
   28. } catch (error) {
   29. const err = error as BusinessError;
   30. hilog.error(0x0000, TAG, `%{public}s`, err.code, err.message);
   31. }
   32. })
   ```

   [LocalVideo.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/localvideo/LocalVideo.ets#L51-L92)
3. 在拖入方Video组件的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里调用[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取拖拽的数据，提取uri并绑定到落入方Video组件上。同时由于设置了[datasyncoptions](../harmonyos-references/ts-universal-events-drag-drop.md#datasyncoptions15)中的destUri参数，UDMF会将视频保存到本地的沙箱路径中。

   ```
   1. Column() {
   2. Video({ src: this.targetVideoUri, controller: new VideoController() })
   3. // ...
   4. }
   5. // ...
   6. .onDrop((event?: DragEvent) => {
   7. try {
   8. let progressListener: unifiedDataChannel.DataProgressListener =
   9. (_progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
   10. if (dragData) {
   11. let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
   12. for (let i = 0; i < records.length; i++) {
   13. let types = records[i].getTypes();
   14. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
   15. const fileUriUds =
   16. records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
   17. let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
   18. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.VIDEO)) {
   19. this.targetVideoUri = fileUriUds.oriUri;
   20. }
   21. }
   22. }
   23. } else {
   24. hilog.info(0x0000, TAG, 'dragData is undefined');
   25. }
   26. };
   27. const destUri = fileUri.getUriFromPath(this.context!.distributedFilesDir);
   28. let options: DataSyncOptions = {
   29. destUri: destUri,
   30. fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
   31. progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
   32. dataProgressListener: progressListener,
   33. };
   34. (event as DragEvent).startDataLoading(options);
   35. } catch (error) {
   36. const err = error as BusinessError;
   37. hilog.error(0x0000, TAG, `startDataLoading errorCode: ${err.code}, errorMessage: ${err.message}`);
   38. }
   39. }, { disableDataPrefetch: true })
   ```

   [LocalVideo.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/localvideo/LocalVideo.ets#L110-L160)

## 图文混排拖拽

此场景涉及拖拽图片与文字混合的内容。对于轻量级的图文混排内容，可以通过向[Text](../harmonyos-references/ts-basic-components-text.md#接口)组件中添加[Span](../harmonyos-references/ts-basic-components-span.md#接口)和[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md#接口)子组件来实现。此外，使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md#接口)组件也可构建图文混排内容。如何选择适合的图文混排组件，请参考[如何选择图文混排方案](../harmonyos-faqs/faqs-arkui-23.md)。

在某些情况下，不同的接收方对同一内容支持的格式各不相同。此时，开发者可以自定义图文混排的拖拽内容，设置UDMF多Entry形式的拖拽数据，以适应不同的接收方。

### 基于Text组件的图文混排拖拽

**运行效果如下所示**

**图6** Text组件图文混排拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/davBtnSjShGw1jdBVsCWVg/zh-cn_image_0000002349574337.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=EC7E944D8E371B9BC2EC74CC620EF506E7B09914BF3F50CFFBB770E40B86FAF1 "点击放大")

**实现原理**

[Text](../harmonyos-references/ts-basic-components-text.md#接口)组件默认具有拖出能力，在拖入区域中分别接收文本和图片对应的UnifiedRecord数据，绑定至拖入Text组件的[Span](../harmonyos-references/ts-basic-components-span.md#接口)和[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md#接口)子组件上，实现较为简单，但是不支持交互式编辑，且拖入方组件需要预先和拖出方组件保持一致的样式，灵活性较差。

```
1. Column() {
2. Text() {
3. // ...
4. }
5. // ...
6. }
7. // ...
8. .onDrop(async (event?: DragEvent) => {
9. try {
10. let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
11. if (dragData !== undefined) {
12. let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
13. if (records.length > 0) {
14. for (let i = 0; i < records.length; i++) {
15. let types = records[i].getTypes();
16. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
17. const fileUriUds =
18. records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
19. let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
20. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
21. this.targetImage = fileUriUds.oriUri;
22. }
23. continue;
24. }
25. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
26. const plainTextUds =
27. records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
28. this.targetTextContent = plainTextUds.textContent;
29. continue;
30. }
31. if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP)) {
32. const pixelMapUds =
33. records[i].getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) as uniformDataStruct.PixelMap;
34. this.targetImage = pixelMapUds.pixelMap;
35. continue;
36. }
37. }
38. }
39. // ...
40. }
41. // ...
42. event?.setResult(0);
43. }
44. // ...
45. })
```

[Text.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/Text.ets#L90-L172)

### 基于RichEditor组件的图文混排拖拽

**运行效果展示**

**图7** RichEditor组件图文混排拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/wJsK6zBEQp-T1AwAKggXTA/zh-cn_image_0000002349614553.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=F014C8DA81286BEBED0CD97733840BFF923993EDF018025E2DBB2E8FB8B4F584 "点击放大")

**实现原理**

RichEditor组件默认具备拖出的能力，并且支持交互式编辑，在拖出方不需要手动构造拖拽的数据，在拖入方通过[addImageSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)方法和[addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)方法动态地将图片和文字的内容添加到拖入方RichEditor组件上。通过这种方式，在拖入方声明RichEditor组件即可，接收到的图文内容可以动态地添加，使用起来更加方便灵活，代码开发较为简单，核心代码如下：

```
1. RichEditor({ controller: this.targetController })
2. // ...
3. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE,
4. uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, uniformTypeDescriptor.UniformDataType.TEXT,
5. uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
6. .onDrop((event: DragEvent) => {
7. try {
8. event.setResult(0);
9. this.receiveDragData(event);
10. } catch (error) {
11. const err = error as BusinessError;
12. hilog.error(0x0000, TAG, `on drop error, errorCode: ${err.code}, errorMessage: ${err.message}`);
13. }
14. })
```

[RichEditor.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/RichEditor.ets#L161-L178)

```
1. async receiveDragData(event: DragEvent) {
2. try {
3. let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
4. if (dragData !== undefined) {
5. let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
6. if (records.length > 0) {
7. for (let i = 0; i < records.length; i++) {
8. let types = records[i].getTypes();
9. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
10. const fileUriUds =
11. records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
12. let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
13. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
14. this.targetController.addImageSpan(fileUriUds.oriUri,
15. {
16. imageStyle: this.imageStyle,
17. offset: this.targetController.getCaretOffset()
18. })
19. }
20. continue;
21. }
22. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
23. const plainTextUds =
24. records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
25. this.targetController.addTextSpan(plainTextUds.textContent,
26. {
27. style: this.textStyle,
28. offset: this.targetController.getCaretOffset(),
29. })
30. continue;
31. }
32. if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP)) {
33. const pixelMapUds =
34. records[i].getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) as uniformDataStruct.PixelMap;
35. this.targetController.addImageSpan(pixelMapUds.pixelMap,
36. {
37. imageStyle: this.imageStyle,
38. offset: this.targetController.getCaretOffset()
39. })
40. continue;
41. }
42. }
43. }
44. // ...
45. }
46. // ...
47. }
48. // ...
49. }
```

[RichEditor.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/RichEditor.ets#L55-L117)

说明

使用RichEditor组件时，需要在[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里手动调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setResult()](../harmonyos-references/ts-universal-events-drag-drop.md#setdata10)接口设置拖拽结果，否则会执行系统默认的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口导致文字落入两次。参见[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口。

### 基于UDMF多Entry的图文混排拖拽

**运行效果如下所示**

**图8** 多Entry图文混排拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/VrKJkVyzRIqAtJEy7PvWEg/zh-cn_image_0000002315775466.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=E218AC7771B91842F134B11550F1B4C6BAD2D5CE6673BCFDF599AFD4AB304335 "点击放大")

**实现原理**

在拖出方手动构造多Entry数据进行拖拽，这种方式灵活性较高，但是由于需要用户手动去构造拖拽数据，因此代码开发更加复杂。

**开发步骤**

1. 在拖出方RichEditor组件的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调中，根据选中的内容构造拖拽数据。

   ```
   1. RichEditor({ controller: this.sourceController })
   2. // ...
   3. .onSelectionChange((value: RichEditorRange) => {
   4. this.selectedStartIndex = value.start as number;
   5. this.selectedEndIndex = value.end as number;
   6. })
   7. // ...
   8. .onDragStart((event) => {
   9. try {
   10. const selection = this.sourceController.getSelection();
   11. // construct drag data
   12. this.buildUnifiedRecords(selection);
   13. event.setData(this.unifiedData);
   14. } catch (error) {
   15. const err = error as BusinessError;
   16. hilog.error(0x0000, TAG, `%{public}s`, err.code, err.message);
   17. }
   18. })
   19. // ...
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L274-L317)
2. 封装buildUnifiedRecords()函数，构造图片和文字内容的拖拽数据。

   ```
   1. buildUnifiedRecords(selection: RichEditorSelection) {
   2. try {
   3. selection.spans.forEach(async (item) => {
   4. if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
   5. let originImageUri = this.getOriginImageUri();
   6. const imageData: uniformDataStruct.FileUri = {
   7. uniformDataType: 'general.file-uri',
   8. oriUri: originImageUri,
   9. fileType: 'general.image'
   10. }
   11. const unifiedRecord =
   12. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, imageData);
   13. let createdPixelMap = this.getOriginPixelMap();
   14. if (createdPixelMap) {
   15. let pixelMap: uniformDataStruct.PixelMap = {
   16. uniformDataType: 'openharmony.pixel-map',
   17. pixelMap: createdPixelMap,
   18. }
   19. unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
   20. this.unifiedData.addRecord(unifiedRecord);
   21. }
   22. // ...
   23. } else {
   24. if (typeof (item as RichEditorTextSpanResult)['value'] != 'undefined') {
   25. const selectedText = this.getSelectedText(item as RichEditorTextSpanResult);
   26. const textData: uniformDataStruct.PlainText = {
   27. uniformDataType: 'general.plain-text',
   28. textContent: selectedText
   29. }
   30. const unifiedRecord =
   31. new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, textData);
   32. this.unifiedData.addRecord(unifiedRecord);
   33. }
   34. }
   35. })
   36. }
   37. // ...
   38. }
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L66-L113)
3. 封装getOriginImageUri()函数，getOriginPixelMap()函数，和getSelectedText()函数。

   ```
   1. getOriginImageUri(): string {
   2. let filePath = this.context.filesDir + '/river.png';
   3. try {
   4. let data = this.context.resourceManager.getRawFdSync('river.png');
   5. let dest = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
   6. let bufferSize = data.length as number;
   7. let buf = new ArrayBuffer(bufferSize);
   8. fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
   9. fileIo.writeSync(dest.fd, buf, { offset: 0, length: bufferSize });
   10. fileIo.close(dest.fd).catch((err: BusinessError) => {
   11. hilog.error(0x0000, TAG, `getOriginImageUri failed. code=${err.code}, message=${err.message}`);
   12. });
   13. this.context.resourceManager.closeRawFd('river.png');
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. hilog.error(0x0000, TAG, `getOriginImageUri failed. code=${err.code}, message=${err.message}`);
   17. }
   18. const originImageUri = fileUri.getUriFromPath(filePath);
   19. return originImageUri;
   20. }
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L117-L137)

   ```
   1. getOriginPixelMap(): PixelMap | undefined {
   2. try {
   3. let data = this.context.resourceManager.getRawFileContentSync('river.png');
   4. let arrayBuffer = data.buffer.slice(0);
   5. let imageSource: image.ImageSource = image.createImageSource(arrayBuffer);
   6. let value = imageSource.getImageInfoSync();
   7. let opts: image.DecodingOptions = {
   8. editable: true,
   9. desiredSize: {
   10. height: value.size.height,
   11. width: value.size.width
   12. }
   13. };
   14. let pixelMap = imageSource.createPixelMapSync(opts);
   15. return pixelMap;
   16. }
   17. // ...
   18. }
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L141-L165)

   ```
   1. getSelectedText(item: RichEditorTextSpanResult): string {
   2. const textStart: number = item.spanPosition.spanRange[0];
   3. const textEnd: number = item.spanPosition.spanRange[1];
   4. let textSelected: string = '';
   5. if (textStart >= this.selectedStartIndex) {
   6. const begin = 0;
   7. const end = Math.min(textEnd, this.selectedEndIndex) - textStart;
   8. textSelected = item.value.substring(begin, end);
   9. } else {
   10. const begin = this.selectedStartIndex - textStart;
   11. const end = Math.min(this.selectedEndIndex, textEnd) - textStart;
   12. textSelected = item.value.substring(begin, end);
   13. }
   14. return textSelected;
   15. }
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L169-L184)
4. 在落入方[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里获取拖拽数据，调用[getEntry()](../harmonyos-references/js-apis-data-unifieddatachannel.md#getentry15)接口读取所需要格式的数据。

   ```
   1. RichEditor({ controller: this.targetController1 })
   2. // ...
   3. .allowDrop([uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP,
   4. uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, uniformTypeDescriptor.UniformDataType.TEXT])
   5. .onDrop((event: DragEvent) => {
   6. event.setResult(0);
   7. this.receiveDragData(event, DROP_AREA.PIXELMAP_AREA);
   8. })
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L330-L341)

   ```
   1. RichEditor({ controller: this.targetController2 })
   2. // ...
   3. .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, uniformTypeDescriptor.UniformDataType.TEXT,
   4. uniformTypeDescriptor.UniformDataType.IMAGE])
   5. .onDrop((event: DragEvent) => {
   6. try {
   7. event.setResult(0);
   8. this.receiveDragData(event, DROP_AREA.URI_AREA);
   9. } catch (error) {
   10. const err = error as BusinessError;
   11. hilog.error(0x0000, TAG, `startDataLoading errorCode: ${err.code}, errorMessage: ${err.message}`);
   12. }
   13. })
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L354-L370)

   ```
   1. receiveDragData(event: DragEvent, area: DROP_AREA) {
   2. try {
   3. let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
   4. if (dragData !== undefined) {
   5. let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
   6. if (records.length > 0) {
   7. for (let i = 0; i < records.length; i++) {
   8. let types = records[i].getTypes();
   9. if (area === DROP_AREA.URI_AREA) {
   10. if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
   11. const fileUriUds =
   12. records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
   13. let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
   14. if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
   15. let targetImage = fileUriUds.oriUri;
   16. this.targetController2.addImageSpan(targetImage,
   17. {
   18. imageStyle: this.imageStyle,
   19. offset: this.targetController2.getCaretOffset()
   20. })
   21. }
   22. continue;
   23. }
   24. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
   25. const plainTextUds =
   26. records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
   27. this.targetController2.addTextSpan(plainTextUds.textContent,
   28. {
   29. style: this.textStyle,
   30. offset: this.targetController2.getCaretOffset()
   31. })
   32. continue;
   33. }
   34. } else {
   35. if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP)) {
   36. const pixelMapUds =
   37. records[i].getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) as uniformDataStruct.PixelMap;
   38. let targetImage = pixelMapUds.pixelMap;
   39. this.targetController1.addImageSpan(targetImage,
   40. {
   41. imageStyle: this.imageStyle,
   42. offset: this.targetController1.getCaretOffset()
   43. })
   44. continue;
   45. }
   46. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
   47. const plainTextUds =
   48. records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
   49. this.targetController1.addTextSpan(plainTextUds.textContent,
   50. {
   51. style: this.textStyle,
   52. offset: this.targetController1.getCaretOffset()
   53. })
   54. continue;
   55. }
   56. }
   57. }
   58. }
   59. // ...
   60. }
   61. // ...
   62. event.setResult(DragResult.DRAG_SUCCESSFUL);
   63. }
   64. // ...
   65. }
   ```

   [MultiEntry.ets](https://gitcode.com/HarmonyOS_Samples/DragFramework/blob/master/entry/src/main/ets/pages/textandimage/MultiEntry.ets#L188-L266)

## 分屏拖拽

将拖拽框架与系统的分屏能力结合，可以将数据从一个分屏页面拖拽到另一个分屏页面，实现跨应用拖拽或同应用跨页面拖拽。

**使用说明**

需要应用[声明支持分屏](../harmonyos-guides/multi-window-support.md#section2205081316)，并根据需求自定义拖拽响应。

**运行效果如下图所示**

**图9** 分屏拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/27DhmxyQRs-pyz4Ox5P7fw/zh-cn_image_0000002315615670.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=C07AF37C9D62406066D8FE6A06D5F51C2E359F2BCBAC5E17C25EBFC5DCC36D63 "点击放大")

## 跨设备拖拽

将拖拽框架与系统的键鼠穿越能力结合，可以接入跨设备拖拽，实现在平板或2in1类型的任意两台设备之间拖拽数据。

**使用说明**

需要满足跨设备拖拽开发指导中的[使用限制条件](../harmonyos-guides/distributed-drag-guide.md#section17575828642)，并根据需求自定义拖拽响应。

**结果展示**

**图10** 跨设备拖拽效果展示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/77Tldp5bQs2WNG1NHddt0w/zh-cn_image_0000002349574349.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=33D6BA5C0921B0E77B6A91A5C1801C30C24470E7F97C3EF561FA4F501C7BC11C "点击放大")

## 拖入小艺和中转站

将数据拖入系统的中转站，可以实现跨应用数据拖拽和跨设备数据流转。将数据拖入小艺，可以利用系统的AI能力处理拖拽数据。小艺和中转站支持落入[标准化数据通路](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifiedrecord)中定义的数据类型，开发者需要在起拖时构造相应的数据。

**使用限制**

应用本身预置的[资源文件](../harmonyos-guides/resource-categories-and-access.md#资源组目录)（即应用在安装前的HAP包中已经存在的资源文件）不支持拖入小艺和中转站。

**运行效果如下图所示**

**图11** 将数据拖入小艺  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/lPNNnwdFQKixoZCY_LgisA/zh-cn_image_0000002349614565.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=DC681260A4CD9A4B59D0063C863999C4EA5BE973BA100A391F06B8B9C2B3E649 "点击放大")

**图12** 将数据拖入中转站  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/aUPV5lF1TLSfMVdM9neTcg/zh-cn_image_0000002315775482.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=A1AE9E7DCD913A0E5BB7BBCEDC5D2351F1AE10E9ED5EA45FF19320C07104E17E "点击放大")

## 常见问题

### 模拟器无法识别AI拖拽内容

模拟器不支持[textRecognition](../harmonyos-guides/core-vision-text-recognition.md)接口的调用，建议使用真机进行调试，详细请参见[通用文字识别约束与限制](../harmonyos-guides/core-vision-text-recognition.md#section2020122517405)。

### 拖拽的触发手势长按浮起与长按手势之间存在冲突

若组件既需要处理长按手势，又需要支持可拖拽能力（拖拽的触发为长按500ms并移动10vp)，则可通过 parallelGesture 实现多个手势事件的处理，而不产生冲突。详细请参见[绑定手势方法](../harmonyos-references/ts-gesture-settings.md)。

### 拖出的PixelMap落入时与拖出端存在色差

拖出PixelMap时，需要设置当前PixelMap的编码格式，否则落入方不能确定该PixelMap的编码方式，按照默认行为处理可能出现存在色差的情况。PixelMap的默认编码格式是BGRA\_8888，若拖出方未指定PixelMap的编码格式，则落入方按照RGBA格式解码即可。若拖出方有指定了PixelMap的编码格式，则落入方可以通过systemDefinedPixelMap.details，details['pixel-format'] 获取拖出方的编码格式，再以该格式解码即可。

### 图文混排数据拖拽落位后与原拖出方排版格式有差异

当前拖拽数据中图文混排数据可通过HTML实现，但拖拽落入方组件可能并非HTML格式，如RichEditor、RichText等。当前系统能力对各类富文本数据的格式转换能力较弱，不能保证排版样式一致。图文混排拖拽建议使用多Entry适配方案，参见[基于UDMF多Entry的图文混排拖拽](bpta-unified-drag-and-drop.md#section5352104013812)。

### 文字无法长按选中后再起拖

文字若要长按选中后再起拖，需要设置copyOptions属性，否则无法触发长按选中逻辑。

### 拖拽到文字某些"输入框"后不响应拖拽

因ArkUI默认支持落入的组件包括Search、TextInput、TextArea、Video，若应用实现时输入框使用的是Text组件实现，则默认不可响应拖拽事件。若要实现对拖拽事件的响应，则应主动设置allowDrop属性、调用onDrop接口实现落入。

### 拖拽到小艺后显示不支持处理此类数据

该问题通常是由于拖拽数据源设置不当导致的问题，如拖拽文件时文件的uri为非法参数，则在落位获取数据时，UDMF不能正常读取数据，导致落位失败。在拖拽发起时候应正确设置拖拽数据，避免拖拽数据为空或拖拽数据非法，如无效uri等情况。

### 拖入区域显示绿色角标仍落位失败

显示绿色角标是因为落入方组件在allowDrop列表中刚设置了当前拖拽数据类型，标识支持该类数据的落入。但是具体是否能够成功落位取决于落入组件在onDrop逻辑中是否正确处理了拖拽数据，如未对数据做处理并刷新UI、读取数据失败等情况都有可能导致落位失败。落入方应用需明确在onDrop回调中是否对当前拖拽数据做处理并刷新UI，排查当前拖拽数据是否非法，如无效uri、无效在线地址等情况。

## 示例代码

* [实现组件的自定义拖拽功能](https://gitcode.com/harmonyos_samples/DragFramework)
