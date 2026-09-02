---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-unified-drag-and-drop
title: 统一拖拽
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 统一拖拽
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-06-23
content_hash: sha256:75ca728c6ad3cfe7e4af455ad1cc729c29e46ddf9224f9144a4f8df7ad0e71ab
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

```screen
RichEditor({ controller: this.sourceController })
// ...
  .onDragStart((event) => {
    try {
      const selection = this.sourceController.getSelection();
      // construct drag data
      this.buildUnifiedRecords(selection);
      event.setData(this.unifiedData);
    } catch (error) {
      const err = error as BusinessError;
      hilog.error(0x0000, TAG, `%{public}s`, err.code, err.message);
    }
  })
  // ...
```

可以在[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中处理拖拽信息，例如为图片添加水印，详情见[拖拽图像增加水印](bpta-unified-drag-and-drop.md#section197593813453)。

### 拖拽中

通过标准手势发起拖拽后，系统会默认将组件本身的截图作为[拖拽背板图](../harmonyos-guides/arkts-common-events-drag-event.md#拖拽背板图)。如果想自定义拖拽背板图，需要在组件的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调中设置[DragItemInfo](../harmonyos-references/ts-universal-events-drag-drop.md#dragiteminfo)，传入自定义背板图。此外，可以在拖拽目标组件上注册[onDragMove()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove)监听，并在回调函数中实时获取拖拽过程中的信息，如拖拽点的坐标等。以Image组件为例，示例代码如下：

自定义拖拽背板图

```screen
Image($r('app.media.mount'))
// ...
  .onDragStart(() => {
    let dragItemInfo: DragItemInfo = {
      pixelMap: this.pixelMap,
      builder: () => {
        this.pixelMapBuilder()
      },
    };
    return dragItemInfo;
  })
  // ...
```

可以将拖拽背板图设置为自定义的图片或者文字，详情见[自定义拖拽背板图](bpta-unified-drag-and-drop.md#section350662014143)。

获取拖拽移动中的坐标等信息

```screen
Column() {
  // ...
}
// ...
.allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
.onDrop((event?: DragEvent) => {
  // ...
})
.onDragMove((event: DragEvent) => {
  hilog.info(0x0000, TAG, `The x-coordinate of the display is ${event.getDisplayX()}.`);
  hilog.info(0x0000, TAG, `The y-coordinate of the display is ${event.getDisplayY()}.`);
  hilog.info(0x0000, TAG, `The x-coordinate of the window is ${event.getWindowX()}.`);
  hilog.info(0x0000, TAG, `The y-coordinate of the window is ${event.getWindowY()}.`);
})
```

**说明** 

只有监听了[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)事件，拖拽在组件范围内移动时，才会触发[onDragMove()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragmove)事件。

### 释放拖拽

[默认支持拖入能力的组件](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)，如[Search](../harmonyos-references/ts-basic-components-search.md)组件等，将目标拖入组件区域内会使用默认拖入响应。如果想自定义组件的拖入响应，需要将组件的[allowDrop()](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)属性设置为允许拖入的数据类型，并在其[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)接口获取拖入数据后，读取其中的UnifiedRecord记录的集合。对于每条记录，调用[getTypes()](../harmonyos-references/js-apis-data-unifieddatachannel.md#gettypes12)方法获取其中包含的数据类型，取出所需要的数据。以Text组件获取拖拽文字为例：

```screen
Column() {
  Text(this.dropContent)
    // ...
}
// ...
.allowDrop([uniformTypeDescriptor.UniformDataType.TEXT,
  uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
.onDrop((event: DragEvent) => {
  try {
    let dragData = event.getData();
    let records = dragData.getRecords();
    for (let record of records) {
      let types = record.getTypes();
      if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
        const plainTextUds =
          record.getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
        this.dropContent = plainTextUds.textContent;
        event.setResult(DragResult.DRAG_SUCCESSFUL);
      }
    }
  }
  // ...
})
```

可以在[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中处理接收到的数据，例如将图片识别为文字以显示在只支持文字的组件上，详情见[AI识别拖拽内容](bpta-unified-drag-and-drop.md#section4125035104613)。

## 拖拽图像增加水印

在拖拽过程中，可以自定义拖出响应，为拖拽图像增加水印，以标识图像的相关信息。下面以在图像中增加拖拽时间水印为例，介绍实现原理。

**运行效果**

**图1** 拖拽图片增加水印  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Nq4k19BIQrOic9171zAbeA/zh-cn_image_0000002315615638.gif "点击放大")

**实现原理**

在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中获取图像信息，调用系统绘制能力[drawing](../harmonyos-references/js-apis-graphics-drawing.md)在图像上绘制水印，通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setData()](../harmonyos-references/ts-universal-events-drag-drop.md#setdata10)接口将水印图像设置为拖拽数据。

**开发步骤**

1. 将拖出方Image组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性设置为true。

   ```screen
   Image($rawfile('river.png'))
     // ...
     .draggable(true)
   ```
2. 在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中，获取图像信息并将其转换成[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

   ```screen
   Image($rawfile('river.png'))
     // ...
     .onDragStart((event: DragEvent) => {
       const resourceMgr: resourceManager.ResourceManager = this.context!.resourceManager;
       let rawFileDescriptor = resourceMgr.getRawFdSync('river.png');
       const imageSourceApi: image.ImageSource = image.createImageSource(rawFileDescriptor);
       let pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync();
       // ...
     })
   ```
3. 将图片绘制到[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布上，并获取拖拽时间作为水印绘制到画布上的指定位置，得到添加水印的图像。

   ```screen
   Image($rawfile('river.png'))
     // ...
     .onDragStart((event: DragEvent) => {
       // ...
       this.time = this.getTimeWatermark(systemDateTime.getTime(false));
       let markPixelMap: image.PixelMap = this.addWaterMark(this.time, pixelMap);
       // ...
     })
   ```

   ```screen
   addWaterMark(watermark: string, pixelMap: image.PixelMap) {
     try {
       if (!canIUse('SystemCapability.Graphics.Drawing')) {
         hilog.error(0x0000, TAG, `%{public}s`, `watermark is not supported`);
         return pixelMap;
       }
       watermark = this.context!.resourceManager.getStringSync($r('app.string.drag_time').id) + watermark;
       const imageInfo: image.Size = pixelMap.getImageInfoSync().size;
       const imageWidth: number = imageInfo.width;
       const imageHeight: number = imageInfo.height;
       const imageScale: number = imageWidth / display.getDefaultDisplaySync().width;
       const canvas: drawing.Canvas = new drawing.Canvas(pixelMap);
       const pen: drawing.Pen = new drawing.Pen();
       const brush: drawing.Brush = new drawing.Brush();
       pen.setColor({
         alpha: 102,
         red: 255,
         green: 255,
         blue: 255
       });
       brush.setColor({
         alpha: 102,
         red: 255,
         green: 255,
         blue: 255
       });
       const font: drawing.Font = new drawing.Font();
       font.setSize(48 * imageScale);
       let textWidth: number = font.measureText(watermark, drawing.TextEncoding.TEXT_ENCODING_UTF8);
       const textBlob: drawing.TextBlob =
         drawing.TextBlob.makeFromString(watermark, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
       canvas.attachBrush(brush);
       canvas.attachPen(pen);
       canvas.drawTextBlob(textBlob, imageWidth - 24 * imageScale - textWidth, imageHeight - 32 * imageScale);
       canvas.detachBrush();
       canvas.detachPen();
     } catch (error) {
       hilog.error(0x0000, TAG, '%{public}s', 'addWaterMark failed:', (error as BusinessError).message);
     }
     return pixelMap;
   }
   ```
4. 将图像打包保存在文件中，调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setData()](../harmonyos-references/ts-universal-events-drag-drop.md#setdata10)接口将水印图像设置为拖拽数据。

   ```screen
   Image($rawfile('river.png'))
     // ...
     .onDragStart((event: DragEvent) => {
       // ...
       let packOpts: image.PackingOption = { format: 'image/png', quality: 20 };
       let file: fileIo.File =
         fileIo.openSync(`${this.context!.filesDir}/watermark.png`, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
       const imagePackerApi: image.ImagePacker = image.createImagePacker();
       imagePackerApi.packToFile(markPixelMap, file.fd, packOpts);
       imagePackerApi?.release();
       let imgData: uniformDataStruct.FileUri = {
         uniformDataType: 'general.file-uri',
         oriUri: fileUri.getUriFromPath(`${this.context!.filesDir}/watermark.png`),
         fileType: 'general.image'
       }
       let unifiedRecord =
         new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, imgData);
       let unifiedData = new unifiedDataChannel.UnifiedData(unifiedRecord);
       event.setData(unifiedData);
       fileIo.closeSync(file.fd);
       // ...
     })
   ```

## 自定义拖拽背板图

[拖拽背板图](../harmonyos-guides/arkts-common-events-drag-event.md#拖拽背板图)用于在拖拽过程中展示用户拖动的数据，可以自定义拖拽背板图。

**运行效果**

**图2** 自定义拖拽背板  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/f8eN-rsgSWKGYrTkj8yhmg/zh-cn_image_0000002349574333.gif "点击放大")

**实现原理**

在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中，自定义[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)作为拖拽过程中的背板图。

**开发步骤**

1. 创建自定义组件。

   ```screen
   @Builder
   pixelMapBuilder() {
     Column() {
       Text($r('app.string.background_content'))
         .fontSize('16fp')
         .margin({
           left: '16vp',
           right: '16vp',
           top: '8vp',
           bottom: '8vp'
         })
     }
     .backgroundColor($r('sys.color.comp_background_primary'))
     .borderRadius(16)
   }
   ```
2. 将自定义组件转换成PixelMap，作为拖拽过程中显示的图片。

   ```screen
   private getComponentSnapshot(): void {
     this.getUIContext().getComponentSnapshot().createFromBuilder(() => {
       this.pixelMapBuilder()
     }, (error: Error, pixmap: image.PixelMap) => {
       if (error) {
         hilog.error(0x0000, TAG, `%{public}s`, error.message);
         return;
       }
       this.pixelMap = pixmap;
     })
   }
   ```

   **说明** 

   由于[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)需要离线渲染之后才能使用，存在一定的性能开销和时延，因此推荐开发者优先使用[DragItemInfo](../harmonyos-references/ts-universal-events-drag-drop.md#dragiteminfo)中的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)方式返回背板图。
3. 在拖出对象的[onPreDrag()](../harmonyos-references/ts-universal-events-drag-drop.md#onpredrag12)接口中，预先创建背板图。

   ```screen
   Image($r('app.media.mount'))
   // ...
     .onPreDrag((status: PreDragStatus) => {
       this.PreDragChange(status);
     })
     // ...
   ```

   ```screen
   private PreDragChange(preDragStatus: PreDragStatus): void {
     if (preDragStatus == PreDragStatus.ACTION_DETECTING_STATUS) {
       this.getComponentSnapshot();
     }
   }
   ```
4. 在拖出对象的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)接口中，将回调的PixelMap作为拖拽过程中的背板图。

   ```screen
   Image($r('app.media.mount'))
   // ...
     .onDragStart(() => {
       let dragItemInfo: DragItemInfo = {
         pixelMap: this.pixelMap,
         builder: () => {
           this.pixelMapBuilder()
         },
       };
       return dragItemInfo;
     })
     // ...
   ```

## AI识别拖拽内容

在拖拽过程中，可以自定义拖入响应，以识别拖拽内容并将其输出在释放区内。本章节以通过AI识别拖拽图像中的文字为例，介绍实现原理。

**运行效果**

**图3** AI识别拖拽内容  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/wCj36bPERN-pkOO7xDd-mA/zh-cn_image_0000002349614541.gif "点击放大")

**实现原理**

在拖入对象的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中，通过[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)接口获取拖拽数据后，调用系统能力[textRecognition（文字识别）](../harmonyos-references/core-vision-text-recognition-api.md)得到图像中的文字信息。

**开发步骤**

1. 在拖拽释放区域的[allowDrop()](../harmonyos-references/ts-universal-attributes-drag-drop.md#allowdrop)接口中设置允许拖入的数据类型为[uniformTypeDescriptor.UniformDataType.IMAGE](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformdatatype)。

   ```screen
   Column() {
     Text(this.textContent)
     // ...
   }
   // ...
   .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
   // ...
   ```
2. 在拖入对象的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口中，调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[getData()](../harmonyos-references/ts-universal-events-drag-drop.md#getdata10)接口获取拖拽数据。

   ```screen
   Column() {
     Text(this.textContent)
     // ...
   }
   // ...
   .onDrop(async (event?: DragEvent) => {
     try {
       let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
       if (dragData === undefined) {
         hilog.info(0x0000, TAG, `%{public}s`, `ondrop undefined data`);
         return;
       }
       let records: unifiedDataChannel.UnifiedRecord[] = dragData.getRecords();
       // ...
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, TAG, `onDrop error, error code: ${err.code}, errorMessage: ${err.message}`);
     }
   })
   ```
3. 将拖拽数据转换成颜色数据格式为BGRA\_8888的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)类型的视觉信息。

   ```screen
   Column() {
     Text(this.textContent)
     // ...
   }
   // ...
   .onDrop(async (event?: DragEvent) => {
     try {
       // ...
       for (let i = 0; i < records.length; i++) {
         let types = records[i].getTypes();
         if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
           const fileUriUds =
             records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
           let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
           if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
             const resourceReg = new RegExp('resource');
             if (resourceReg.test(fileUriUds.oriUri)) {
               const numberReg = new RegExp('[0-9]+');
               let idArray = fileUriUds.oriUri.match(numberReg);
               if (idArray !== null) {
                 let id = idArray[0];
                 let drawableDescriptor =
                   this.context.getHostContext()!.resourceManager.getDrawableDescriptor(Number(id), 0, 1);
                 let pixelMapInit = drawableDescriptor.getPixelMap() as image.PixelMap;
                 let imageHeight = pixelMapInit.getImageInfoSync().size.height;
                 let imageWidth = pixelMapInit.getImageInfoSync().size.width;
                 const readBuffer: ArrayBuffer = new ArrayBuffer(imageHeight * imageWidth * 4);
                 pixelMapInit.readPixelsToBufferSync(readBuffer);
                 let opts: image.InitializationOptions = {
                   editable: true,
                   size: { height: imageHeight, width: imageWidth },
                   srcPixelFormat: pixelMapInit.getImageInfoSync().pixelFormat,
                   pixelFormat: 3,
                   alphaType: pixelMapInit.getImageInfoSync().alphaType,
                   scaleMode: 0
                 };
                 let pixelMap: image.PixelMap = image.createPixelMapSync(readBuffer, opts);
                 // ...
               }
             }
           }
         }
       }
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, TAG, `onDrop error, error code: ${err.code}, errorMessage: ${err.message}`);
     }
   })
   ```
4. 调用系统文字识别能力textRecognition获取拖拽数据中的文字信息。

   ```screen
   Column() {
     Text(this.textContent)
     // ...
   }
   // ...
   .onDrop(async (event?: DragEvent) => {
     try {
       // ...
       for (let i = 0; i < records.length; i++) {
         let types = records[i].getTypes();
         if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
           // ...
           if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
             // ...
             if (resourceReg.test(fileUriUds.oriUri)) {
               // ...
               if (idArray !== null) {
                 // ...
                 let visionInfo: textRecognition.VisionInfo = { pixelMap: pixelMap };
                 let data = await textRecognition.recognizeText(visionInfo);
                 let recognitionString = data.value;
                 this.textContent = recognitionString;
               }
             }
           }
         }
       }
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, TAG, `onDrop error, error code: ${err.code}, errorMessage: ${err.message}`);
     }
   })
   ```

## 文件拖拽

文件拖拽操作可分为在线文件拖拽和本地文件拖拽。

在线文件拖拽时，拖出方需提供文件的下载地址，下载操作由落入方处理。若业务需求要求在拖出方完成下载，则需将下载与拖拽操作分开处理，确保文件在拖出前已完成下载，以避免拖出失败。

对于本地文件的拖拽，建议构造FileUri类型的数据进行拖拽。在文件落入时，应通过调用[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取数据，如需将文件保存在本地，可设置[datasyncoptions](../harmonyos-references/ts-universal-events-drag-drop.md#datasyncoptions15)参数的destUri值，将文件保存至本地沙箱路径中。

## 在线文件拖拽保存

以在线图片为例，拖出放Image组件绑定了在线的图片资源。通过拖拽将图片移至目标区域展示，目标区域可选择是否将图片资源下载到本地。

**运行效果**

**图4** 在线图片拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/_EO8t_f2QraD1f1fik12pg/zh-cn_image_0000002315775454.gif "点击放大")

**使用说明**

加载在线图片资源需在工程module.json5文件中添加网络权限。

**实现原理**

在落入方[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调中获取拖拽数据，得到访问图片的链接，同时根据业务需要选择是否将图片下载到本地。本示例模拟了需要下载的场景。

**开发步骤：**

1. 开启网络权限。

   ```screen
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET",
       "reason": "$string:internet_reason",
       "usedScene": {
         "abilities": [
           "EntryAbility"
         ],
         "when": "inuse"
       }
     }
   ],
   ```
2. 设置拖出方Image组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性为true。

   ```screen
   Image('https://www-file.huawei.com/-/media/corp2020/home/banner/12/pura-x-1.jpg')
   // ...
     .draggable(true)
     // ...
   ```
3. 在落入方Image组件的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调中获取图片的uri，绑定到落入方组件上，触发UI刷新。

   ```screen
   Column() {
     Image(this.targetImage)
     // ...
   }
   // ...
   .onDrop((event?: DragEvent) => {
     try {
       let dragData = event?.getData() as unifiedDataChannel.UnifiedData;
       if (dragData) {
         let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
         for (let i = 0; i < records.length; i++) {
           let types = records[i].getTypes();
           if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
             const fileUriUds =
               records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
             let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
             if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
               this.targetImage = fileUriUds.oriUri;
               // ...
             }
           }
         }
       }
     }
     // ...
   });
   ```
4. 在落入方Image组件的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里调用[request](../harmonyos-references/js-apis-request.md#导入模块)的[downloadFile()](../harmonyos-references/js-apis-request.md#requestdownloadfile9)方法下载图片资源。

   ```screen
   Column() {
     Image(this.targetImage)
     // ...
   }
   // ...
   .onDrop((event?: DragEvent) => {
     try {
       let dragData = event?.getData() as unifiedDataChannel.UnifiedData;
       if (dragData) {
         let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
         for (let i = 0; i < records.length; i++) {
           let types = records[i].getTypes();
           if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
             // ...
             if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
               // ...
               request.downloadFile(this.context, {
                 url: fileUriUds.oriUri,
                 filePath: this.filesDir + '/test.png'
               }).then(() => {
                 const file = fileIo.openSync(this.filesDir + '/test.png', fileIo.OpenMode.READ_WRITE);
                 const arrayBuffer = new ArrayBuffer(1024);
                 const readLen = fileIo.readSync(file.fd, arrayBuffer);
                 buffer.from(arrayBuffer, 0, readLen);
                 fileIo.closeSync(file);
               }).catch((error: BusinessError) => {
                 hilog.error(0x0000, TAG, `%{public}s`, error.code, error.message);
               })
             }
           }
         }
       }
     }
     // ...
   });
   ```

## 本地文件拖拽保存

本示例展示拖拽本地的文件，以$rawfile目录下的视频文件为例。

**运行效果**

**图5** 本地视频拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/OYv1M8tmTk2ukEW90UgNYw/zh-cn_image_0000002315615654.gif "点击放大")

**实现原理**

为了实现文件的拖拽，通常会构建一个[uniformDataStruct.FileUri](../harmonyos-references/js-apis-data-uniformdatastruct.md#fileuri15)类型的数据对象，传入文件的uri，并通过设置fileType属性来区分不同的文件类型。在接收方的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调函数中获取uri，进而访问该文件。建议使用UDMF的[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取文件，并展示获取进度。如果接收方需要将文件拷贝到本地，可以通过向参数[datasyncoptions](../harmonyos-references/ts-universal-events-drag-drop.md#datasyncoptions15)传入destUri来指定目标路径，UDMF将会把文件拷贝至该路径。

**实现步骤：**

1. 设置拖出方Video组件的[draggable()](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)属性为true。

   ```screen
   Video({
     src: $rawfile('video.mp4'),
     controller: new VideoController()
   })
     // ...
     .draggable(true)
       // ...
   ```
2. 在拖出视频的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调中，将视频文件复制到沙箱目录。构造[uniformDataStruct.FileUri](../harmonyos-references/js-apis-data-uniformdatastruct.md#fileuri15)类型的数据，将oriUri设置为沙箱路径下视频文件的uri。

   ```screen
   Video({
     src: $rawfile('video.mp4'),
     controller: new VideoController()
   })
     // ...
     .onDragStart((event: DragEvent) => {
       try {
         let data = this.context!.resourceManager.getRawFdSync('video.mp4');
         let filePath = this.context?.filesDir + '/video.mp4';
         let dest = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         let bufferSize = data.length as number;
         let buf = new ArrayBuffer(bufferSize);
         fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
         fileIo.writeSync(dest.fd, buf, { offset: 0, length: bufferSize });
         fileIo.close(dest.fd);
         this.context!.resourceManager.closeRawFd('video.mp4');
         this.originalVideoUri = fileUri.getUriFromPath(filePath);
         let unifiedData = new unifiedDataChannel.UnifiedData();
         let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
         let video: uniformDataStruct.FileUri = {
           uniformDataType: 'general.file-uri',
           oriUri: this.originalVideoUri,
           fileType: 'general.video'
         }
         unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.VIDEO, video);
         unifiedData.addRecord(unifiedRecord);
         event.setData(unifiedData);
       } catch (error) {
         const err = error as BusinessError;
         hilog.error(0x0000, TAG, `%{public}s`, err.code, err.message);
       }
     })
   ```
3. 在拖入方Video组件的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里调用[startDataLoading()](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)接口获取拖拽的数据，提取uri并绑定到落入方Video组件上。同时由于设置了[datasyncoptions](../harmonyos-references/ts-universal-events-drag-drop.md#datasyncoptions15)中的destUri参数，UDMF会将视频保存到本地的沙箱路径中。

   ```screen
   Column() {
     Video({ src: this.targetVideoUri, controller: new VideoController() })
       // ...
   }
   // ...
   .onDrop((event?: DragEvent) => {
     try {
       let progressListener: unifiedDataChannel.DataProgressListener =
         (_progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
           if (dragData) {
             let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
             for (let i = 0; i < records.length; i++) {
               let types = records[i].getTypes();
               if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
                 const fileUriUds =
                   records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
                 let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
                 if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.VIDEO)) {
                   this.targetVideoUri = fileUriUds.oriUri;
                 }
               }
             }
           } else {
             hilog.info(0x0000, TAG, 'dragData is undefined');
           }
         };
       const destUri = fileUri.getUriFromPath(this.context!.distributedFilesDir);
       let options: DataSyncOptions = {
         destUri: destUri,
         fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
         progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
         dataProgressListener: progressListener,
       };
       (event as DragEvent).startDataLoading(options);
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, TAG, `startDataLoading errorCode: ${err.code}, errorMessage: ${err.message}`);
     }
   }, { disableDataPrefetch: true })
   ```

## 图文混排拖拽

此场景涉及拖拽图片与文字混合的内容。对于轻量级的图文混排内容，可以通过向[Text](../harmonyos-references/ts-basic-components-text.md#接口)组件中添加[Span](../harmonyos-references/ts-basic-components-span.md#接口)和[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md#接口)子组件来实现。此外，使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md#接口)组件也可构建图文混排内容。如何选择适合的图文混排组件，请参考[如何选择图文混排方案](../harmonyos-faqs/faqs-arkui-23.md)。

在某些情况下，不同的接收方对同一内容支持的格式各不相同。此时，开发者可以自定义图文混排的拖拽内容，设置UDMF多Entry形式的拖拽数据，以适应不同的接收方。

### 基于Text组件的图文混排拖拽

**运行效果如下所示**

**图6** Text组件图文混排拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/assH1IPyRmmrH108M6t1tg/zh-cn_image_0000002349574337.gif "点击放大")

**实现原理**

[Text](../harmonyos-references/ts-basic-components-text.md#接口)组件默认具有拖出能力，在拖入区域中分别接收文本和图片对应的UnifiedRecord数据，绑定至拖入Text组件的[Span](../harmonyos-references/ts-basic-components-span.md#接口)和[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md#接口)子组件上，实现较为简单，但是不支持交互式编辑，且拖入方组件需要预先和拖出方组件保持一致的样式，灵活性较差。

```screen
Column() {
  Text() {
    // ...
  }
  // ...
}
// ...
.onDrop(async (event?: DragEvent) => {
  try {
    let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
    if (dragData !== undefined) {
      let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
      if (records.length > 0) {
        for (let i = 0; i < records.length; i++) {
          let types = records[i].getTypes();
          if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
            const fileUriUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
            let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
            if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
              this.targetImage = fileUriUds.oriUri;
            }
            continue;
          }
          if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
            const plainTextUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
            this.targetTextContent = plainTextUds.textContent;
            continue;
          }
          if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP)) {
            const pixelMapUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) as uniformDataStruct.PixelMap;
            this.targetImage = pixelMapUds.pixelMap;
            continue;
          }
        }
      }
      // ...
    }
    // ...
    event?.setResult(0);
  }
  // ...
})
```

### 基于RichEditor组件的图文混排拖拽

**运行效果展示**

**图7** RichEditor组件图文混排拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/xZo6oP_oQeyYlZCUH-4QyA/zh-cn_image_0000002349614553.gif "点击放大")

**实现原理**

RichEditor组件默认具备拖出的能力，并且支持交互式编辑，在拖出方不需要手动构造拖拽的数据，在拖入方通过[addImageSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addimagespan)方法和[addTextSpan()](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)方法动态地将图片和文字的内容添加到拖入方RichEditor组件上。通过这种方式，在拖入方声明RichEditor组件即可，接收到的图文内容可以动态地添加，使用起来更加方便灵活，代码开发较为简单，核心代码如下：

```screen
RichEditor({ controller: this.targetController })
// ...
  .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE,
    uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, uniformTypeDescriptor.UniformDataType.TEXT,
    uniformTypeDescriptor.UniformDataType.PLAIN_TEXT])
  .onDrop((event: DragEvent) => {
    try {
      event.setResult(0);
      this.receiveDragData(event);
    } catch (error) {
      const err = error as BusinessError;
      hilog.error(0x0000, TAG, `on drop error, errorCode: ${err.code}, errorMessage: ${err.message}`);
    }
  })
```

```screen
async receiveDragData(event: DragEvent) {
  try {
    let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
    if (dragData !== undefined) {
      let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
      if (records.length > 0) {
        for (let i = 0; i < records.length; i++) {
          let types = records[i].getTypes();
          if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
            const fileUriUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
            let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
            if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
              this.targetController.addImageSpan(fileUriUds.oriUri,
                {
                  imageStyle: this.imageStyle,
                  offset: this.targetController.getCaretOffset()
                })
            }
            continue;
          }
          if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
            const plainTextUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
            this.targetController.addTextSpan(plainTextUds.textContent,
              {
                style: this.textStyle,
                offset: this.targetController.getCaretOffset(),
              })
            continue;
          }
          if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP)) {
            const pixelMapUds =
              records[i].getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) as uniformDataStruct.PixelMap;
            this.targetController.addImageSpan(pixelMapUds.pixelMap,
              {
                imageStyle: this.imageStyle,
                offset: this.targetController.getCaretOffset()
              })
            continue;
          }
        }
      }
      // ...
    }
    // ...
  }
  // ...
}
```

**说明** 

使用RichEditor组件时，需要在[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里手动调用[DragEvent](../harmonyos-references/ts-universal-events-drag-drop.md#dragevent7)的[setResult()](../harmonyos-references/ts-universal-events-drag-drop.md#setresult10)接口设置拖拽结果，否则会执行系统默认的[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口导致文字落入两次。参见[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)接口。

### 基于UDMF多Entry的图文混排拖拽

**运行效果如下所示**

**图8** 多Entry图文混排拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/fmKjDebfSgOKxJ99mHaGhA/zh-cn_image_0000002315775466.gif "点击放大")

**实现原理**

在拖出方手动构造多Entry数据进行拖拽，这种方式灵活性较高，但是由于需要用户手动去构造拖拽数据，因此代码开发更加复杂。

**开发步骤**

1. 在拖出方RichEditor组件的[onDragStart()](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)回调中，根据选中的内容构造拖拽数据。

   ```screen
   RichEditor({ controller: this.sourceController })
   // ...
     .onSelectionChange((value: RichEditorRange) => {
       this.selectedStartIndex = value.start as number;
       this.selectedEndIndex = value.end as number;
     })
     // ...
     .onDragStart((event) => {
       try {
         const selection = this.sourceController.getSelection();
         // construct drag data
         this.buildUnifiedRecords(selection);
         event.setData(this.unifiedData);
       } catch (error) {
         const err = error as BusinessError;
         hilog.error(0x0000, TAG, `%{public}s`, err.code, err.message);
       }
     })
     // ...
   ```
2. 封装buildUnifiedRecords()函数，构造图片和文字内容的拖拽数据。

   ```screen
   buildUnifiedRecords(selection: RichEditorSelection) {
     try {
       selection.spans.forEach(async (item) => {
         if (typeof (item as RichEditorImageSpanResult)['imageStyle'] != 'undefined') {
           let originImageUri = this.getOriginImageUri();
           const imageData: uniformDataStruct.FileUri = {
             uniformDataType: 'general.file-uri',
             oriUri: originImageUri,
             fileType: 'general.image'
           }
           const unifiedRecord =
             new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, imageData);
           let createdPixelMap = this.getOriginPixelMap();
           if (createdPixelMap) {
             let pixelMap: uniformDataStruct.PixelMap = {
               uniformDataType: 'openharmony.pixel-map',
               pixelMap: createdPixelMap,
             }
             unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
             this.unifiedData.addRecord(unifiedRecord);
           }
           // ...
         } else {
           if (typeof (item as RichEditorTextSpanResult)['value'] != 'undefined') {
             const selectedText = this.getSelectedText(item as RichEditorTextSpanResult);
             const textData: uniformDataStruct.PlainText = {
               uniformDataType: 'general.plain-text',
               textContent: selectedText
             }
             const unifiedRecord =
               new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, textData);
             this.unifiedData.addRecord(unifiedRecord);
           }
         }
       })
     }
     // ...
   }
   ```
3. 封装getOriginImageUri()函数，getOriginPixelMap()函数，和getSelectedText()函数。

   ```screen
   getOriginImageUri(): string {
     let filePath = this.context.filesDir + '/river.png';
     try {
       let data = this.context.resourceManager.getRawFdSync('river.png');
       let dest = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
       let bufferSize = data.length as number;
       let buf = new ArrayBuffer(bufferSize);
       fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
       fileIo.writeSync(dest.fd, buf, { offset: 0, length: bufferSize });
       fileIo.close(dest.fd).catch((err: BusinessError) => {
         hilog.error(0x0000, TAG, `getOriginImageUri failed. code=${err.code}, message=${err.message}`);
       });
       this.context.resourceManager.closeRawFd('river.png');
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, TAG, `getOriginImageUri failed. code=${err.code}, message=${err.message}`);
     }
     const originImageUri = fileUri.getUriFromPath(filePath);
     return originImageUri;
   }
   ```

   ```screen
   getOriginPixelMap(): PixelMap | undefined {
     try {
       let data = this.context.resourceManager.getRawFileContentSync('river.png');
       let arrayBuffer = data.buffer.slice(0);
       let imageSource: image.ImageSource = image.createImageSource(arrayBuffer);
       let value = imageSource.getImageInfoSync();
       let opts: image.DecodingOptions = {
         editable: true,
         desiredSize: {
           height: value.size.height,
           width: value.size.width
         }
       };
       let pixelMap = imageSource.createPixelMapSync(opts);
       return pixelMap;
     }
     // ...
   }
   ```

   ```screen
   getSelectedText(item: RichEditorTextSpanResult): string {
     const textStart: number = item.spanPosition.spanRange[0];
     const textEnd: number = item.spanPosition.spanRange[1];
     let textSelected: string = '';
     if (textStart >= this.selectedStartIndex) {
       const begin = 0;
       const end = Math.min(textEnd, this.selectedEndIndex) - textStart;
       textSelected = item.value.substring(begin, end);
     } else {
       const begin = this.selectedStartIndex - textStart;
       const end = Math.min(this.selectedEndIndex, textEnd) - textStart;
       textSelected = item.value.substring(begin, end);
     }
     return textSelected;
   }
   ```
4. 在落入方[onDrop()](../harmonyos-references/ts-universal-events-drag-drop.md#ondrop)回调里获取拖拽数据，调用[getEntry()](../harmonyos-references/js-apis-data-unifieddatachannel.md#getentry15)接口读取所需要格式的数据。

   ```screen
   RichEditor({ controller: this.targetController1 })
   // ...
     .allowDrop([uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP,
       uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, uniformTypeDescriptor.UniformDataType.TEXT])
     .onDrop((event: DragEvent) => {
       event.setResult(0);
       this.receiveDragData(event, DROP_AREA.PIXELMAP_AREA);
     })
   ```

   ```screen
   RichEditor({ controller: this.targetController2 })
   // ...
     .allowDrop([uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, uniformTypeDescriptor.UniformDataType.TEXT,
       uniformTypeDescriptor.UniformDataType.IMAGE])
     .onDrop((event: DragEvent) => {
       try {
         event.setResult(0);
         this.receiveDragData(event, DROP_AREA.URI_AREA);
       } catch (error) {
         const err = error as BusinessError;
         hilog.error(0x0000, TAG, `startDataLoading errorCode: ${err.code}, errorMessage: ${err.message}`);
       }
     })
   ```

   ```screen
   receiveDragData(event: DragEvent, area: DROP_AREA) {
     try {
       let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
       if (dragData !== undefined) {
         let records: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
         if (records.length > 0) {
           for (let i = 0; i < records.length; i++) {
             let types = records[i].getTypes();
             if (area === DROP_AREA.URI_AREA) {
               if (types.includes(uniformTypeDescriptor.UniformDataType.FILE_URI)) {
                 const fileUriUds =
                   records[i].getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
                 let typeDescriptor = uniformTypeDescriptor.getTypeDescriptor(fileUriUds.fileType);
                 if (typeDescriptor.belongsTo(uniformTypeDescriptor.UniformDataType.IMAGE)) {
                   let targetImage = fileUriUds.oriUri;
                   this.targetController2.addImageSpan(targetImage,
                     {
                       imageStyle: this.imageStyle,
                       offset: this.targetController2.getCaretOffset()
                     })
                 }
                 continue;
               }
               if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
                 const plainTextUds =
                   records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
                 this.targetController2.addTextSpan(plainTextUds.textContent,
                   {
                     style: this.textStyle,
                     offset: this.targetController2.getCaretOffset()
                   })
                 continue;
               }
             } else {
               if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP)) {
                 const pixelMapUds =
                   records[i].getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) as uniformDataStruct.PixelMap;
                 let targetImage = pixelMapUds.pixelMap;
                 this.targetController1.addImageSpan(targetImage,
                   {
                     imageStyle: this.imageStyle,
                     offset: this.targetController1.getCaretOffset()
                   })
                 continue;
               }
               if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
                 const plainTextUds =
                   records[i].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
                 this.targetController1.addTextSpan(plainTextUds.textContent,
                   {
                     style: this.textStyle,
                     offset: this.targetController1.getCaretOffset()
                   })
                 continue;
               }
             }
           }
         }
         // ...
       }
       // ...
       event.setResult(DragResult.DRAG_SUCCESSFUL);
     }
     // ...
   }
   ```

## 分屏拖拽

将拖拽框架与系统的分屏能力结合，可以将数据从一个分屏页面拖拽到另一个分屏页面，实现跨应用拖拽或同应用跨页面拖拽。

**使用说明**

需要应用[声明支持分屏](../harmonyos-guides/multi-window-support.md#声明支持分屏)，并根据需求自定义拖拽响应。

**运行效果如下图所示**

**图9** 分屏拖拽  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/gdypck3KQtWY3kUFTvOmoA/zh-cn_image_0000002315615670.gif "点击放大")

## 跨设备拖拽

将拖拽框架与系统的键鼠穿越能力结合，可以接入跨设备拖拽，实现在平板或2in1类型的任意两台设备之间拖拽数据。

**使用说明**

需要满足跨设备拖拽开发指导中的[约束与限制](bpta-distribute-drag-cast.md#section990465462314)，并根据需求自定义拖拽响应。

**结果展示**

**图10** 跨设备拖拽效果展示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/47vhxetPRUq9CKd_0qx1hg/zh-cn_image_0000002349574349.gif "点击放大")

## 拖入小艺和中转站

将数据拖入系统的中转站，可以实现跨应用数据拖拽和跨设备数据流转。将数据拖入小艺，可以利用系统的AI能力处理拖拽数据。小艺和中转站支持落入[标准化数据通路](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifiedrecord)中定义的数据类型，开发者需要在起拖时构造相应的数据。

**使用限制**

应用本身预置的[资源文件](../harmonyos-guides/resource-categories-and-access.md#资源组目录)（即应用在安装前的HAP包中已经存在的资源文件）不支持拖入小艺和中转站。

**运行效果如下图所示**

**图11** 将数据拖入小艺  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/drH111G9T6Cki1cydNsAQg/zh-cn_image_0000002349614565.gif "点击放大")

**图12** 将数据拖入中转站  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/l_7W1ioQSWutEpqln99SiQ/zh-cn_image_0000002315775482.gif "点击放大")

## 常见问题

### 模拟器无法识别AI拖拽内容

模拟器不支持[textRecognition](../harmonyos-guides/core-vision-text-recognition.md)接口的调用，建议使用真机进行调试，详细请参见基础视觉服务[模拟器支持情况](../harmonyos-guides/core-vision-introduction.md#模拟器支持情况)。

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
