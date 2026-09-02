---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage
title: pdfViewManager（PDF预览）
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS API > pdfViewManager（PDF预览）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c0f25e9ce8a388f4aa80e58db3c79284019c50886bceb8c3972a0f16e5286505
---

本模块为应用提供统一的PDF预览能力。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { pdfViewManager } from '@kit.PDFKit';
```

## PdfController

PDF文档控制器类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### constructor

constructor()

构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
```

### setViewOffset

setViewOffset(offsetX: number, offsetY: number, refreshView: boolean): void

设置可视区域X和Y坐标的偏移。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offsetX | number | 是 | X坐标偏移，范围0 ~ 1，含义是0% ~ 100%的偏移如果总宽度是1000px，要偏移X轴500px，值是0.5。 |
| offsetY | number | 是 | Y坐标偏移，范围0 ~ 1，含义是0% ~ 100%的偏移，如果总高度是1000px，要偏移Y轴500px，值是0.5。 |
| refreshView | boolean | 是 | 是否刷新可视区域，true：是（页面滚动时，页面清晰），false：否（页面滚动时，页面模糊）。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setViewOffset(0.5, 0.5, true);
}
```

### getPagePixelMap

getPagePixelMap(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>

获取对应PDF页面的缩略图，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引，0为起始页。 |
| isSync | boolean | 否 | 是否同步获取PDF页面的缩略图，true：是，false：否，默认值：false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回image.PixelMap类型。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let image = await pdfController.getPagePixelMap(0, true);
}
```

### registerScrollListener

registerScrollListener(listener: Callback<ScrollParam>): void

注册滚动监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[ScrollParam](pdf-arkts-pdfviewmanage.md#scrollparam)> | 是 | 页面滚动回调函数监听，返回ScrollParam类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerScrollListener((scrollParam: pdfViewManager.ScrollParam) => { });
```

### enablePageDrag

enablePageDrag(verticalEnabled: boolean, horizontalEnabled: boolean): void

设置页面是否支持拖拽。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verticalEnabled | boolean | 是 | 是否Y轴垂直拖动，true: 是，false: 否。 |
| horizontalEnabled | boolean | 是 | 是否X轴水平拖动，true: 是，false: 否。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.enablePageDrag(true, true);
}
```

### loadDocument

loadDocument(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>

加载文件并显示指定的页面，使用Promise异步回调。由于loadDocument不支持重复调用，因此在二次调用之前，必须先通过releaseDocument释放当前已加载的文档，以确保资源正确释放并避免潜在的冲突或异常。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文档路径。 |
| password | string | 否 | 密码，长度不超过512字节，仅支持ASCII字符（127以内）。默认值：空字符串 |
| initPageIndex | number | 否 | 要打开的文档初始化页面索引，0为初始页。默认值：0 |
| onProgress | [Callback](js-apis-base.md#callback)<number> | 否 | 加载文档进度回调函数，返回number类型数据，传此参数返回文档加载进度，不传不返回文档加载进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<pdfService.[ParseResult](pdf-arkts-pdfservice.md#parseresult)> | Promise对象，返回ParseResult类型数据。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempFilePath = dir + '/test.pdf';
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(tempFilePath);
```

### releaseDocument

releaseDocument(): void

释放已加载的文件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempFilePath = dir + '/test.pdf';
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(tempFilePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.releaseDocument();
}
```

### setHighlightRects

setHighlightRects(rectArray: Array<PageRects>, color?: number): void

在UI层，以PDF页面左下角(0,0)为原点，以PDF点为单位，向上延展，高亮显示对应的矩形区域内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rectArray | Array<[PageRects](pdf-arkts-pdfviewmanage.md#pagerects)> | 是 | 高亮块在页面的矩形区域。rect的left、right最小值为0，最大值为PDF的宽度，top、bottom最小值为0，最大值为PDF的高度。 |
| color | number | 否 | 高亮颜色(ARGB)，取值范围0x00000000 ~ 0xFFFFFFFF，默认值：0x00000000。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit'

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  const highlightArray = new Array<pdfViewManager.PageRects>();
  const rectArray = new Array<pdfService.PdfRect>();
  const rect1: pdfService.PdfRect = { left: 20, top: 0, right: 120, bottom: 300 };
  rectArray.push(rect1);
  highlightArray.push(new pdfViewManager.PageRects(0, rectArray));
  pdfController.setHighlightRects(highlightArray, 0xAA666666);
}
```

### setHighlightText

setHighlightText(pageIndex: number, textArray: string[], color: number): void

高亮选中文本，执行中的[searchKey](pdf-arkts-pdfviewmanage.md#searchkey)会中断。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引，0为起始页。 |
| textArray | string[] | 是 | 选中的文本。 |
| color | number | 是 | 高亮颜色(ARGB)，取值范围0x00000000 ~ 0xFFFFFFFF。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setHighlightText(1, ['1111', 'aaaa'], 0x66666666);
}
```

### setPageZoom

setPageZoom(zoom: number): void

设置视图的缩放比例。使用该函数时，会将页面适配模式改为PageFit.FIT\_NONE。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoom | number | 是 | 缩放比例 [0.1 ~ 10]。(大于10的时候取10，小于0.1的时候取0.1) |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setPageZoom(2);
}
```

### getPageZoom

getPageZoom(): number

获取视图的缩放比例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取视图的缩放比例 [0.1 ~ 10]。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageZoom = pdfController.getPageZoom();
}
```

### setMaxZoom

setMaxZoom(maxZoom: number): boolean

设置视图的最大缩放比例。

**说明** 

页面适配(PageFit)的优先级高于缩放比例(Zoom)，当同时执行了缩放比例设置与页面适配设置时，优先遵循设置的页面适配方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxZoom | number | 是 | 最大缩放比例[0.1 ~ 10](精度支持到小数点后第2位)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否设置成功，true：是，false：否。  当传入的maxZoom小于当前的最小缩放比例、超出[0.1 ~ 10]的范围、输入值为空时，均会返回false。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';
@Entry
@Component
struct PdfPage {
  private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let dir = context.filesDir;
    let filePath = dir + `/input.pdf`;
    let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
    if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
      this.pdfController.setMaxZoom(10);
    }
  }
  build() {
    Column() {
      // 组件
    }
  }
}
```

### getMaxZoom

getMaxZoom(): number

获取视图的最大缩放比例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的视图最大缩放比例[0.1 ~ 10](精度支持到小数点后第2位)。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';
@Entry
@Component
struct PdfPage {
  private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let dir = context.filesDir;
    let filePath = dir + `/input.pdf`;
    let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
    if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
      this.pdfController.getMaxZoom();
    }
  }
  build() {
    Column() {
      // 组件
    }
  }
}
```

### setMinZoom

setMinZoom(minZoom: number): boolean

设置视图的最小缩放比例。

**说明** 

页面适配(PageFit)的优先级高于缩放比例(Zoom)，当同时执行了缩放比例设置与页面适配设置时，优先遵循设置的页面适配方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minZoom | number | 是 | 最小缩放比例[0.1 ~ 10]（精度支持到小数点后第2位）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否设置成功，true：是，false：否。  当传入的minZoom大于当前的最大缩放比例、超出[0.1 ~ 10]的范围、输入值为空时，均会返回false。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';
@Entry
@Component
struct PdfPage {
  private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let dir = context.filesDir;
    let filePath = dir + `/input.pdf`;
    let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
    if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
      this.pdfController.setMinZoom(0.1);
    }
  }
  build() {
    Column() {
      // 组件
    }
  }
}
```

### getMinZoom

getMinZoom(): number

获取视图的最小缩放比例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的视图最小缩放比例[0.1 ~ 10](精度支持到小数点后第2位)。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';
@Entry
@Component
struct PdfPage {
  private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let dir = context.filesDir;
    let filePath = dir + `/input.pdf`;
    let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
    if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
      this.pdfController.getMinZoom();
    }
  }
  build() {
    Column() {
      // 组件
    }
  }
}
```

### setPageLayout

setPageLayout(columnCount: pdfService.PageLayout): void

设置页面布局模式：单页面：1，双页面：2。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnCount | pdfService.[PageLayout](pdf-arkts-pdfservice.md#pagelayout) | 是 | 页面布局模式：单页面：1，双页面：2。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setPageLayout(pdfService.PageLayout.LAYOUT_SINGLE);
}
```

### getPageLayout

getPageLayout(): pdfService.PageLayout

获取页面布局模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[PageLayout](pdf-arkts-pdfservice.md#pagelayout) | 页面布局模式：单页面：1，双页面：2。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageLayout: pdfService.PageLayout = pdfController.getPageLayout();
}
```

### setPageContinuous

setPageContinuous(isContinuous: boolean): void

设置页面滚动是否连续排列。仅支持垂直排列。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isContinuous | boolean | 是 | 滚动是否连续排列，true: 是，false: 否。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setPageContinuous(true);
}
```

### isPageContinuous

isPageContinuous(): boolean

获取页面是否连续排列。仅支持垂直排列

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否连续排列，true: 是，false: 否。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageContinuous: boolean = pdfController.isPageContinuous();
}
```

### setPageFit

setPageFit(pageFit: pdfService.PageFit): void

设置页面的适配模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageFit | pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit) | 是 | 页面的适配模式。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setPageFit(pdfService.PageFit.FIT_NONE);
}
```

### getPageFit

getPageFit(): pdfService.PageFit

获取页面的适配模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit) | 页面的适配模式。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageFitMode: pdfService.PageFit = pdfController.getPageFit();
}
```

### setPageSpacing

setPageSpacing(horizontal: number, vertical?: number): void

设置页面之间的行间距和列间距。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontal | number | 是 | 双页模式下左右页面之间的间距，大于等于0，单位为px。 |
| vertical | number | 否 | 连续滚动时上下页面的间距，大于等于0，单位为px，默认值：10。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setPageSpacing(20, 20);
}
```

### getPageHorizontalSpacing

getPageHorizontalSpacing(): number

获取双页模式下左右页面之间的间距。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 左右页面之间的间距，单位为px。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let horSpacing = pdfController.getPageHorizontalSpacing();
}
```

### getPageVerticalSpacing

getPageVerticalSpacing(): number

获取上下页之间的间距。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 上下页之间的间距，单位为px。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let verSpacing = pdfController.getPageVerticalSpacing();
}
```

### getPageCount

getPageCount(): number

获取PDF的总页数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 总页数，大于等于0。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageCount = pdfController.getPageCount();
}
```

### getPageIndex

getPageIndex(): number

获取PDF当前页的索引。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 页面索引。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageIndex = pdfController.getPageIndex();
}
```

### goToPage

goToPage(pageIndex: number): void

跳转到指定页。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 指定页索引，0为起始页，小于总页数。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.goToPage(1);
}
```

### setPageRotation

setPageRotation(pageIndex: number, angle: pdfService.RotationAngle): void

设置指定页面在PdfView组件中显示的旋转角度。旋转角度为逆时针方向的固定值，可选值包括 0、90、180、270 度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 指定页索引，0为起始页，小于总页数。 |
| angle | pdfService.[RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 是 | 指定页旋转角度。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setPageRotation(1, pdfService.RotationAngle.ANGLE_90);
}
```

### getPageRotation

getPageRotation(pageIndex: number): pdfService.RotationAngle

获取指定页面的旋转度数： 0、90、180、270度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 指定页索引，0为起始页，小于总页数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 指定页面的旋转角度。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageIndex: pdfService.RotationAngle = pdfController.getPageRotation(1);
}
```

### enableAnnotation

enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void

在常用操作之间切换并添加批注。目前支持高亮、下划线和删除线。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 是 | 支持的批注类型。 |
| color | number | 否 | 颜色(ARGB)，范围0x00000000 - 0xFFFFFFFF，默认值：0xFFFFFFFF。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAEEEEEE);
}
```

### addMarkupAnnotation

addMarkupAnnotation(annotationType: SupportedAnnotationType, selectedRects: Array<SelectedRects>, color: number): void

在PDF注释层，以PDFView视图左上角(0,0)为原点，以像素点为单位，向下延展，添加文本批注。文本批注添加成功后，通过[registerAnnotationSelectedListener](pdf-arkts-pdfviewmanage.md#registerannotationselectedlistener)回调来高亮显示文本批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 是 | 批注类型。 |
| selectedRects | Array<[SelectedRects](pdf-arkts-pdfviewmanage.md#selectedrects)> | 是 | 高亮显示的矩形区域。 |
| color | number | 是 | 颜色(ARGB)，范围0x00000000 - 0xFFFFFFFF。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let rectArray: Array<pdfService.PdfRect> = [{ left: 5, top: 5, right: 250, bottom: 250}];
  let selectedRects: Array<pdfViewManager.SelectedRects> = [new pdfViewManager.SelectedRects(0, rectArray, 0)];
  pdfController.addMarkupAnnotation(pdfViewManager.SupportedAnnotationType.UNDERLINE, selectedRects, 0xAA666666);
}
```

### disableAnnotation

disableAnnotation(): void

禁止添加批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.disableAnnotation();
}
```

### deleteSelectedAnnotation

deleteSelectedAnnotation(annotationIndex: number, pageIndex: number): void

删除选中的批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationIndex | number | 是 | 批注索引，从0开始。 |
| pageIndex | number | 是 | 页面索引，从0开始。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  // 确保第一页存在一个批注
  pdfController.deleteSelectedAnnotation(0, 0);
}
```

### updateMarkupAnnotation

updateMarkupAnnotation(annotationIndex: number, pageIndex: number, color: number): void

修改批注颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationIndex | number | 是 | 批注索引。 |
| pageIndex | number | 是 | 页面索引。 |
| color | number | 是 | 颜色（ARGB），范围0x00000000 - 0xFFFFFFFF。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  // 确保第一页存在一个批注
  pdfController.updateMarkupAnnotation(0, 0, 0xAA000000);
}
```

### saveDocument

saveDocument(path: string, onProgress?: Callback<number>): Promise<number>

保存PDF文档，使用Promise异步回调。

**说明** 

由于文档不可同时读写，如果需要覆盖回原文档，请创建临时文档作为过渡。具体请参见下方示例代码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文档的沙箱路径。 |
| onProgress | [Callback](js-apis-base.md#callback)<number> | 否 | 保存文档回调函数进度，返回number类型数据，传此参数返回文档保存进度，不传不返回文档保存进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回number类型，1：成功， 0：失败。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';
import { fileIo as fs } from '@kit.CoreFileKit';

// 将测试文件上传至应用沙箱路径
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempDir = context.tempDir;
// 确保该路径下的源文档有读写的权限
let filePath = dir + `/input.pdf`;
let tempFilePath = tempDir + `/temp${Math.random()}.pdf`;
fs.copyFileSync(filePath, tempFilePath);
let pdfController = new pdfViewManager.PdfController();
// 加载临时文件
let loadResult = await pdfController.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  // 保存文件将覆盖源文档
  let result = await pdfController.saveDocument(filePath);
}
pdfController.releaseDocument();
```

### registerSelectedRectsChangedListener

registerSelectedRectsChangedListener(listener: Callback<Array<SelectedRects>>): void

注册用于监听选中区域矩形变化的监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<Array<[SelectedRects](pdf-arkts-pdfviewmanage.md#selectedrects)>> | 是 | 选中文本拖拽窗口变化回调函数监听，返回SelectedRects类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerSelectedRectsChangedListener((pageRects: Array<pdfViewManager.SelectedRects>) => {});
```

### registerPageFitChangedListener

registerPageFitChangedListener(listener: Callback<pdfService.PageFit>): void

注册页面适配变化监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit)> | 是 | 页面适配变化回调函数监听，返回PageFit类型数据。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerPageFitChangedListener((pageFit: pdfService.PageFit) => {});
```

### registerPageChangedListener

registerPageChangedListener(listener: Callback<number>): void

注册页面索引变化监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 页面索引变化回调函数监听，返回页面索引number类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerPageChangedListener((pageIndex: number) => {});
```

### registerScaleChangedListener

registerScaleChangedListener(listener: Callback<number>): void

注册页面缩放变化监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 页面缩放回调函数监听，返回缩放值number类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerScaleChangedListener((scale: number) => {});
```

### registerTextSelectedListener

registerTextSelectedListener(listener: Callback<TextSelectedParam>): void

注册文本选中监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[TextSelectedParam](pdf-arkts-pdfviewmanage.md#textselectedparam)> | 是 | 页面文本被选中回调函数监听，返回选中文本TextSelectedParam类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerTextSelectedListener((pageText: pdfViewManager.TextSelectedParam) => {});
```

### registerAnnotationSelectedListener

registerAnnotationSelectedListener(listener: Callback<SelectedAnnotation>): void

注册页面批注选中监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[SelectedAnnotation](pdf-arkts-pdfviewmanage.md#selectedannotation)> | 是 | 页面批注被选中回调函数监听，返回选中批注SelectedAnnotation类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerAnnotationSelectedListener((pdfAnnotation: pdfViewManager.SelectedAnnotation) => {});
```

### registerImageSelectedListener

registerImageSelectedListener(listener: Callback<ImageSelectedParam>): void

注册图片选中监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[ImageSelectedParam](pdf-arkts-pdfviewmanage.md#imageselectedparam)> | 是 | 页面图片被选中回调函数监听，返回选中图片ImageSelectedParam类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerImageSelectedListener((image: pdfViewManager.ImageSelectedParam) => {});
```

### registerActionClickListener

registerActionClickListener(listener: Callback<RedirectInfo>): void

注册Click动作的时候监听器，例如：拿到值是链接地址可以拉取浏览器跳转到相应的网页。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[RedirectInfo](pdf-arkts-pdfviewmanage.md#redirectinfo)> | 是 | Click动作回调函数监听，返回RedirectInfo类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerActionClickListener((redirectInfo: pdfViewManager.RedirectInfo) => {});
```

### registerAnnotationChangedListener

registerAnnotationChangedListener(listener: Callback<AnnotationChangedParam>): void

注册批注变化监听器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[AnnotationChangedParam](pdf-arkts-pdfviewmanage.md#annotationchangedparam)> | 是 | 批注变化时回调函数监听，返回AnnotationChangedParam类型数据。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerAnnotationChangedListener((annotationChange: pdfViewManager.AnnotationChangedParam) => {});
```

### registerPageCountChangedListener

registerPageCountChangedListener(listener: Callback<number>): void

注册总页数变化的时候监听器，需要在loadDocument之前调用，否则无法捕获loadDocument期间的页数变化事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 总页数变化回调函数监听，返回number类型总页数。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let pdfController = new pdfViewManager.PdfController();
pdfController.registerPageCountChangedListener((pageCount: number) => {});
```

### searchKey

searchKey(text: string, listener: Callback<number>): void

搜索文本并返回匹配的总数，执行搜索会清除之前通过[setHighlightText](pdf-arkts-pdfviewmanage.md#sethighlighttext)设置的文本高亮。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 搜索的文本。 |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 搜索文本回调函数监听，返回number类型的匹配总数。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.searchKey('a', (index: number) => {});
}
```

### clearSearch

clearSearch(): void

清除搜索文本的高亮，等价于搜索空字符串 。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.clearSearch();
}
```

### getSearchIndex

getSearchIndex(): number

获取当前命中搜索关键字匹配结果的索引，执行搜索接口后默认命中索引为0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 匹配结果索引，大于等于0。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let res = pdfController.getSearchIndex();
}
```

### setSearchIndex

setSearchIndex(index: number): void

设置搜索匹配结果的索引，页面会跳转到索引对应搜索结果处。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 搜索结果索引，从0开始。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setSearchIndex(1);
}
```

### setDisplayDirection

setDisplayDirection(displayDirection: DisplayDirection): void

设置PDF非连续模式下文档的翻页方向。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayDirection | [DisplayDirection](pdf-arkts-pdfviewmanage.md#displaydirection) | 是 | 翻页的方向（默认竖直方向）。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';

let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let filePath = dir + `/input.pdf`;
let pdfController = new pdfViewManager.PdfController();
let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfController.setDisplayDirection(pdfViewManager.DisplayDirection.VERTICAL);
}
```

### setNestedScroll

setNestedScroll(value: PdfNestedScrollOptions): void

设置嵌套滑动选项。可以设置上下左右四个方向，实现与父组件的滑动联动。

**说明** 

若PdfNestedScrollOptions中的PdfNestedScrollMode设置为SELF\_FIRST，滑动到边缘后放手重新触发滑动才会滑动父组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PdfNestedScrollOptions](pdf-arkts-pdfviewmanage.md#pdfnestedscrolloptions) | 是 | 可滚动组件滚动时的嵌套滑动选项，包括scrollUp、scrollDown、scrollLeft、scrollRight，默认值为[PdfNestedScrollMode](pdf-arkts-pdfviewmanage.md#pdfnestedscrollmode).SELF\_ONLY。 |

**示例：**

```typescript
import { pdfViewManager, pdfService } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PdfPage {
  private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let dir = context.filesDir;
    let filePath = dir + `/input.pdf`;

    let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);

    if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
      this.pdfController.setNestedScroll({
        scrollUp: pdfViewManager.PdfNestedScrollMode.SELF_ONLY,
        scrollDown: pdfViewManager.PdfNestedScrollMode.SELF_ONLY,
        scrollLeft: pdfViewManager.PdfNestedScrollMode.SELF_ONLY,
        scrollRight: pdfViewManager.PdfNestedScrollMode.SELF_ONLY
      });
    }
  }

  build() {
    Column() {
      // 组件
    }
  }
}
```

### setRenderMode

setRenderMode(renderMode: PresetRenderMode): void

自定义渲染风格。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| renderMode | [PresetRenderMode](pdf-arkts-pdfviewmanage.md#presetrendermode) | 是 | 渲染风格。默认值：DEFAULT。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011302004](errorcode-pdf.md#section1011302004-渲染忙碌) | The rendering thread is busy. |
| [1011302005](errorcode-pdf.md#section1011302005-无效渲染模式) | Unknown rendering mode. |

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.resourceDir
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath: string = dir + '/input.pdf';
    try {
      let res = fileIo.accessSync(filePath);
      if (!res) {
        let content: Uint8Array = context.resourceManager.getRawFileContentSync('resfile/input.pdf');
        let fdSand =
          fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'IndexPage', `Code: ${error.code}, message: ${error.message} `);
    }
    (async () => {
      let loadResult1: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      this.controller.setRenderMode(pdfViewManager.PresetRenderMode.DARKMODE);

    })()
  }

  build() {
    Row() {
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
    .width('100%')
    .height('100%')
  }
}
```

### loadDocumentFromMemory

loadDocumentFromMemory(data: ArrayBuffer, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>

从内存二进制数据流加载PDF文件并显示指定的页面，使用Promise异步回调。loadDocumentFromMemory和loadDocument均为文档加载接口，此类接口不支持连续调用，因此在二次调用之前，必须先通过releaseDocument释放当前已加载的文档，以确保资源正确释放并避免潜在的冲突或异常。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**说明** 

传入接口的ArrayBuffer在结束生命周期完成释放前，不推荐对内部数据流进行篡改，否则可能会导致显示异常、闪退等非预期行为。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | PDF文件的二进制数据，仅支持大小1GB以内的二进制数据。data参数建议使用private变量存储，不可使用@State或@Link等装饰器，否则将导致接口无法获取到传入的二进制数据。 |
| password | string | 否 | 密码，长度不超过512字节，仅支持ASCII字符（127以内），默认值：空字符串。 |
| initPageIndex | number | 否 | 要打开的文档初始化页面索引，0为初始页，默认值：0。 |
| onProgress | [Callback](js-apis-base.md#callback)<number> | 否 | 加载文档进度回调函数。传此参数，返回number类型数据，表示文档加载进度；不传此参数不返回文档加载进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<pdfService.[ParseResult](pdf-arkts-pdfservice.md#parseresult)> | Promise对象，返回解析二进制数据流结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011302001](errorcode-pdf.md#section1011302001-页码值错误) | Invalid page number. |
| [1011302002](errorcode-pdf.md#section1011302002-加载的文档未释放) | The loaded document has not been freed. |
| [1011302003](errorcode-pdf.md#section1011302003-加载的二进制流为空或超出范围) | The input ArrayBuffer is empty or exceeds the maximum limit. |
| [1011302006](errorcode-pdf.md#section1011302006-加载忙碌) | Another document is being loaded. |

**示例：**

```typescript
import { pdfViewManager, pdfService} from '@kit.PDFKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PdfPage {
private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
private pdfBuffer: ArrayBuffer | null | undefined = null;

    async aboutToAppear() {
        try {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let filePath = context.resourceDir;
            let tempFilePath = filePath + `/input.pdf`;
            // 可通过以下方式来构建PDF文件的ArrayBuffer
            let file = fileIo.openSync(tempFilePath, fileIo.OpenMode.READ_ONLY);
            let stat = fileIo.statSync(file.fd);
            this.pdfBuffer = new ArrayBuffer(stat.size);
            fileIo.readSync(file.fd, this.pdfBuffer);
            fileIo.closeSync(file.fd);

            let loadResult: pdfService.ParseResult = await this.pdfController.loadDocumentFromMemory(this.pdfBuffer);
        } catch (e) {
            // 错误处理
        }
    }
    aboutToDisappear(): void {
        // 释放pdfBuffer
        this.pdfBuffer = undefined;
    }
    build() {
        Column() {
            // 组件
        }
    }
}
```

### getPageIndexFromViewPoint

getPageIndexFromViewPoint(viewPoint: Point): number

将视图坐标系中的指定点转换为对应的PDF页面索引（从0开始），坐标单位：px，原点为PdfView组件左上角。同步返回页面索引。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| viewPoint | Point | 是 | 视图坐标系中的位置点，需传入单位为px的像素值。默认值：{ x: 0, y: 0 } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回对应的页面索引。大于等于0：有效的页面索引。-1：该点未落在任何有效页面上。 |

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

@Entry
@Component
struct Index {
@State message: string = 'Hello World';
private context = this.getUIContext().getHostContext() as Context;
private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
private filePath = this.context.resourceDir + '/input.pdf';

    aboutToAppear(): void {
        this.controller.loadDocument(this.filePath);
    }

    aboutToDisappear(): void {
        this.controller.releaseDocument();
    }

    build() {
        RelativeContainer() {
            Column() {
                Row() {
                    PdfView({
                        // 需将controller绑定到PdfView组件上
                        controller: this.controller,
                        pageFit: pdfService.PageFit.FIT_WIDTH,
                        showScroll: true
                    }).onTouch((event: TouchEvent) => {
                        if (event.type === TouchType.Down) {
                            try {
                                let viewPoint: pdfViewManager.Point = {
                                    x: vp2px(event.touches[0].x),
                                    y: vp2px(event.touches[0].y)
                                };
                                // 使用res
                                let res = this.controller.getPageIndexFromViewPoint(viewPoint);
                            } catch (error) {
                                console.error(`Failed to getPageIndexFromViewPoint: ${error}`);
                            };
                        }
                    })
                        .width('100%')
                        .height('100%')
                }
            .width('100%')
                    .height('100%')
            }
        }
    .width('100%')
            .height('100%')
    }
}
```

### viewRectToPDFRect

viewRectToPDFRect(pageIndex: number, viewRect: ViewRect): pdfService.PdfRect

将视图坐标系中的矩形转换为指定PDF页面坐标系的矩形，返回转换后的PDF页面坐标系矩形。视图坐标原点在PdfView组件左上角，Y轴向下，单位px。PDF坐标原点在PDF页面左下角，Y轴向上，单位Points。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 目标PDF页面的索引（从0开始）。默认值：0。 |
| viewRect | ViewRect | 是 | 视图坐标系中的矩形区域，包含left、top、right、bottom属性，单位为px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 返回转换后的PDF页面坐标系矩形。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011302001](errorcode-pdf.md#section1011302001-页码值错误) | Invalid page number. |

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

@Entry
@Component
struct Index {
private context = this.getUIContext().getHostContext() as Context;
private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
private filePath = this.context.resourceDir + '/input.pdf';

    aboutToAppear(): void {
        this.controller.loadDocument(this.filePath);
    }

    aboutToDisappear(): void {
        this.controller.releaseDocument();
    }

    build() {
        RelativeContainer() {
            Column() {
                Row() {
                    PdfView({
                        // 需将controller绑定到PdfView组件上
                        controller: this.controller,
                        pageFit: pdfService.PageFit.FIT_WIDTH,
                        showScroll: true
                    })
                        .width('100%')
                        .height('100%')

                    Button('pdfRectToViewRect').onClick(() => {
                        try {
                            let viewRect: pdfViewManager.ViewRect = {
                                left: 100,
                                top: 100,
                                right: 100,
                                bottom: 100
                            };
                            // 转换为 PDF 内部坐标
                            let res: pdfService.PdfRect = this.controller.viewRectToPDFRect(0, viewRect);
                            // 使用res
                        } catch (error) {
                            console.error(`Failed to viewRectToPDFRect: ${error}`);
                        }
                    })
                }
            .width('100%')
                    .height('100%')
            }
        }
    .width('100%')
            .height('100%')
    }
}
```

### pdfPointToViewPoint

pdfPointToViewPoint(pageIndex: number, pdfPoint: pdfService.PdfPoint): Point

将PDF页面坐标系中的点转换为视图坐标系中的点，PDF页面坐标系中的点。视图坐标原点在PdfView组件左上角，Y轴向下，单位为px。PDF页面坐标原点在PDF页面左下角，Y轴向上，单位为Points。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 源PDF页面的索引（从0开始）。默认值：0。 |
| pdfPoint | pdfService.[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint) | 是 | PDF页面坐标系中的点，单位为Points。默认值：{ x: 0, y: 0 } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Point](pdf-arkts-pdfviewmanage.md#point) | 返回转换后的视图坐标系点，包含x和y属性，单位为px。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011302001](errorcode-pdf.md#section1011302001-页码值错误) | Invalid page number. |

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as Context;
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private filePath = this.context.resourceDir + '/input.pdf';

  aboutToAppear(): void {
    this.controller.loadDocument(this.filePath);
  }

  aboutToDisappear(): void {
    this.controller.releaseDocument();
  }

  build() {
    RelativeContainer() {
      Column() {
        Row() {
          PdfView({
            // 需将controller绑定到PdfView组件上
            controller: this.controller,
            pageFit: pdfService.PageFit.FIT_WIDTH,
            showScroll: true
          })
            .width('100%')
            .height('100%')

          Button('pdfRectToViewRect').onClick(() => {
            try {
              let pdfpoint: pdfService.PdfPoint = {
                x: 100,
                y: 100
              }
              // 使用res
              let res: pdfViewManager.Point = this.controller.pdfPointToViewPoint(0, pdfpoint);
            } catch (error) {
              console.error(`Failed to pdfPointToViewPoint: ${error}`);
            }
            ;
          })
        }
        .width('100%')
        .height('100%')
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

### viewPointToPDFPoint

viewPointToPDFPoint(pageIndex: number, viewPoint: Point): pdfService.PdfPoint

将视图坐标系中的指定点转换为指定PDF页面坐标系中的点。视图坐标原点在PdfView组件左上角，Y轴向下，单位为px。PDF页面坐标原点在具体PDF页面左下角，Y轴向上，单位为Points。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 目标 PDF 页面的索引值（从 0 开始）。默认值：0。 |
| viewPoint | Point | 是 | 视图坐标系中的位置点，单位为px。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint) | 返回转换后的PDF坐标系点，包含x和y属性，单位为点（Points）。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011302001](errorcode-pdf.md#section1011302001-页码值错误) | Invalid page number. |

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private context = this.getUIContext().getHostContext() as Context;
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private filePath = this.context.resourceDir + '/input.pdf';

  aboutToAppear(): void {
    this.controller.loadDocument(this.filePath);
  }

  aboutToDisappear(): void {
    this.controller.releaseDocument();
  }

  build() {
    RelativeContainer() {
      Column() {
          Row() {
          PdfView({
            // 需将controller绑定到PdfView组件上
            controller: this.controller,
            pageFit: pdfService.PageFit.FIT_WIDTH,
            showScroll: true
          }).onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              try {
                let viewPoint :pdfViewManager.Point ={
                  x:vp2px(event.touches[0].x) ,
                  y:vp2px(event.touches[0].y)
                }
                // 使用res
                let res:pdfService.PdfPoint=  this.controller.viewPointToPDFPoint(0,viewPoint);
              } catch (error) {
                console.error(`Failed to viewPointToPDFPoint: ${error}`);
              };
            }
          })
            .width('100%')
            .height('100%')
        }
        .width('100%')
        .height('100%')
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

### pdfRectToViewRect

pdfRectToViewRect(pageIndex: number, pdfRect: pdfService.PdfRect): ViewRect

将PDF页面坐标系的矩形同步转换为视图坐标系矩形，返回转换后的视图坐标系矩形。视图坐标原点在PdfView组件左上角，Y轴向下，单位为px。PDF坐标原点在具体PDF页面左下角，Y轴向上，单位为Points。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 源PDF页面的索引值（从0开始）。默认值：0。 |
| pdfRect | pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 是 | PDF坐标系中的矩形区域，单位为Points。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ViewRect](pdf-arkts-pdfviewmanage.md#viewrect) | 返回转换后的视图坐标系矩形，单位为px。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011302001](errorcode-pdf.md#section1011302001-页码值错误) | Invalid page number. |

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as Context;
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private filePath = this.context.resourceDir + '/input.pdf';

  aboutToAppear(): void {
    this.controller.loadDocument(this.filePath);
  }

  aboutToDisappear(): void {
    this.controller.releaseDocument();
  }

  build() {
    RelativeContainer() {
      Column() {
          Row() {
          PdfView({
            // 需将controller绑定到PdfView组件上
            controller: this.controller,
            pageFit: pdfService.PageFit.FIT_WIDTH,
            showScroll: true
          })
            .width('100%')
            .height('100%')

            Button('pdfRectToViewRect').onClick(() => {
              try {
                let pdfRect: pdfService.PdfRect ={
                  left:100,
                  top: 100,
                  right:200,
                  bottom:200
                }
                // 使用res
                let res:pdfViewManager.ViewRect=  this.controller.pdfRectToViewRect(0,pdfRect);
              } catch (error) {
                console.error(`Failed to pdfRectToViewRect: ${error}`);
              };
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

## RedirectInfo

PDF页面重定向信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | 否 | 否 | 重定向信息内容。 |
| actionType | [RedirectType](pdf-arkts-pdfviewmanage.md#redirecttype) | 否 | 否 | 重定向类型。 |

### constructor

constructor(content: string, actionType: RedirectType)

用于创建PDF页面重定向信息类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 重定向信息内容。 |
| actionType | [RedirectType](pdf-arkts-pdfviewmanage.md#redirecttype) | 是 | 重定向类型。 |

**示例：**

```typescript
import { pdfViewManager } from '@kit.PDFKit';

let redirectInfo = new pdfViewManager.RedirectInfo('https://www.test.com', pdfViewManager.RedirectType.URI);
```

## SelectedAnnotation

PDF选择的批注信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| annotationIndex | number | 是 | 否 | 批注索引。 |
| pageIndex | number | 是 | 否 | 页码索引。 |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 是 | 否 | 批注类型。 |
| color | number | 是 | 否 | 批注颜色(ARGB)，范围0x00000000 ~ 0xFFFFFFFF。 |
| rect | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 是 | 是 | 批注矩形区域。 |
| points | Array<pdfService.[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 是 | 是 | 批注坐标。 |

## PageRects

页面中矩形区域类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pageIndex | number | 否 | 否 | 页面索引。 |
| rectArray | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 否 | 否 | 数组PdfRect类型。 |

### constructor

constructor(pageIndex: number, rectArray: Array<pdfService.PdfRect>)

用于创建页面中矩形区域类的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引。 |
| rectArray | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 是 | 数组PdfRect类型。 |

## SelectedRects

PDF页面中选定文本的矩形区域类，继承[PageRects](pdf-arkts-pdfviewmanage.md#pagerects)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isRotated | number | 否 | 否 | 是否支持旋转，0：否，1：是。 |

### constructor

constructor(pageIndex: number, rectArray: Array<pdfService.PdfRect>, isRotated: number)

用于创建PDF页面中选定文本的矩形区域类的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引。 |
| rectArray | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 是 | 数组PdfRect类型。 |
| isRotated | number | 是 | 是否支持旋转，0：否，1：是。 |

**示例：**

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';

let rectArray: Array<pdfService.PdfRect> = new Array<pdfService.PdfRect>();
const rect1: pdfService.PdfRect = { left: 5, top: 5, right: 250, bottom: 250};
rectArray.push(rect1);
let selectedRects: pdfViewManager.SelectedRects = new pdfViewManager.SelectedRects(0, rectArray, 0);
```

## ScrollParam

PDF页面[registerScrollListener](pdf-arkts-pdfviewmanage.md#registerscrolllistener)监听函数回调参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offsetX | number | 否 | 否 | 滚动X坐标偏移量，值：0~1，表示0%~100%。 |
| offsetY | number | 否 | 否 | 滚动Y坐标偏移值，值：0~1，表示0%~100%。 |
| pdfWidth | number | 否 | 否 | PDF页面宽度，参数为缩放后的PDF总宽度，单位为px。 |
| pdfHeight | number | 否 | 否 | PDF页面高度，参数为缩放后的PDF总高度，单位为px。 |
| viewWidth | number | 否 | 否 | 控件的宽度，单位为px。 |
| viewHeight | number | 否 | 否 | 控件的高度，单位为px。 |

## TextSelectedParam

PDF页面[registerTextSelectedListener](pdf-arkts-pdfviewmanage.md#registertextselectedlistener)监听函数回调参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 选中的文本内容。 |
| pdfRect | Array<[SelectedRects](pdf-arkts-pdfviewmanage.md#selectedrects)> | 否 | 否 | 选中的文本在PDF页面的矩形区域。 |

## ImageSelectedParam

PDF页面[registerImageSelectedListener](pdf-arkts-pdfviewmanage.md#registerimageselectedlistener)监听函数回调参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageType | pdfService.[ImageFormat](pdf-arkts-pdfservice.md#imageformat) | 否 | 否 | 选中的图片类型。 |
| buffer | ArrayBuffer | 否 | 是 | buffer参数是图像内容。如果缓冲区为空，则取消选择。 |
| pdfRect | pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 否 | 是 | 选中的图片在PDF页面的矩形区域。 |
| pageIndex | number | 否 | 是 | 页码索引。 |

## AnnotationChangedParam

PDF页面[registerAnnotationChangedListener](pdf-arkts-pdfviewmanage.md#registerannotationchangedlistener)监听函数回调参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | number | 否 | 否 | 颜色(ARGB)，范围0x00000000 ~ 0xFFFFFFFF。 |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 否 | 否 | 批注类型。 |
| pageIndexArray | Array<number> | 否 | 否 | 批注在页面的索引列表。 |
| controlType | [AnnotationEditType](pdf-arkts-pdfviewmanage.md#annotationedittype) | 否 | 否 | 批注编辑类型，0：添加，1：修改，2：删除。 |

## SupportedAnnotationType

PDF页面支持的批注类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知类型。 |
| FREE\_TEXT | 3 | 自由字体。 |
| LINE | 4 | 线。 |
| SQUARE | 5 | 方形，包括长方形。 |
| OVAL | 6 | 椭圆，包括圆。 |
| POLYGON | 7 | 多边形。 |
| HIGHLIGHT | 9 | 高亮。 |
| UNDERLINE | 10 | 下划线。 |
| STRIKETHROUGH | 12 | 删除线。 |

## AnnotationEditType

PDF页面上支持的批注更改类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADD | 0 | 添加。 |
| MODIFY | 1 | 修改。 |
| DELETE | 2 | 删除。 |

## RedirectType

需要进行重定向的ActionType。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| URI | 6 | uri地址。 |
| LAUNCH | 4 | launch，本地文件路径。 |

## DisplayDirection

非连续显示时的翻页方向。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VERTICAL | 0 | 竖直方向翻页。 |
| HORIZONTAL | 1 | 水平方向翻页。 |

## PdfNestedScrollOptions

可以设置上下左右四个方向的嵌套滑动规则。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.2(22)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scrollUp | [PdfNestedScrollMode](pdf-arkts-pdfviewmanage.md#pdfnestedscrollmode) | 否 | 是 | 可滑动组件往上滑动时的嵌套滑动选项。  默认值：PdfNestedScrollMode.SELF\_ONLY。 |
| scrollDown | [PdfNestedScrollMode](pdf-arkts-pdfviewmanage.md#pdfnestedscrollmode) | 否 | 是 | 可滑动组件往下滑动时的嵌套滑动选项。  默认值：PdfNestedScrollMode.SELF\_ONLY。 |
| scrollLeft | [PdfNestedScrollMode](pdf-arkts-pdfviewmanage.md#pdfnestedscrollmode) | 否 | 是 | 可滑动组件往左滑动时的嵌套滑动选项。  默认值：PdfNestedScrollMode.SELF\_ONLY。 |
| scrollRight | [PdfNestedScrollMode](pdf-arkts-pdfviewmanage.md#pdfnestedscrollmode) | 否 | 是 | 可滑动组件往右滑动时的嵌套滑动选项。  默认值：PdfNestedScrollMode.SELF\_ONLY。 |

## PdfNestedScrollMode

定义嵌套滑动组件中的嵌套模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.2(22)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELF\_ONLY | 0 | 只自身滑动，不与父组件联动。 |
| SELF\_FIRST | 1 | 自身先滑动，自身滑动到边缘以后父组件滑动。如果父组件有边缘效果，在滑动到父组件边缘后，触发父组件边缘效果，否则触发子组件的边缘效果。 |

## PresetRenderMode

预设渲染模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 标准渲染模式，保持原始像素，不做任何处理。适合正常光线环境。 |
| DARKMODE | 1 | 深色渲染模式，基于标准模式对像素进行反差增强，提升在暗色背景下的可见性。适合夜间或低光环境。 |

## Point

坐标系中的点位置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x坐标值，表示与Y轴的垂直距离。默认值：0。 |
| y | number | y坐标值，表示与X轴的垂直距离。默认值：0。 |

## ViewRect

视图坐标系中的矩形区域，单位为px，原点(0,0)位于PdfView组件左上角。X轴正方向向右，Y轴正方向向下。left、top、right、bottom分别表示矩形四条边到原点的垂直距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 矩形左边缘的X坐标。默认值：0。 |
| top | number | 矩形上边缘的Y坐标。默认值：0。 |
| right | number | 矩形右边缘的X坐标。默认值：0。 |
| bottom | number | 矩形下边缘的y坐标。默认值：0。 |
