---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage
title: pdfViewManager（PDF预览）
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS API > pdfViewManager（PDF预览）
category: harmonyos-references
scraped_at: 2026-04-29T14:09:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f34fdf2bea0726733ff021fad808cb6e0c630b06dcdb53225dadae60bb2c6108
---

本模块为应用提供统一的PDF预览能力。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { pdfViewManager } from '@kit.PDFKit';
```

## PdfController

PhonePC/2in1Tablet

PDF文件控制器类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### constructor

PhonePC/2in1Tablet

constructor()

构造函数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
```

### setViewOffset

PhonePC/2in1Tablet

setViewOffset(offsetX: number, offsetY: number, refreshView: boolean): void

设置可视区域X和Y坐标的偏移。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offsetX | number | 是 | X坐标偏移，范围0 ~ 1，含义是0% ~ 100%的偏移如果总宽度是1000px，要偏移X轴500px，值是0.5。 |
| offsetY | number | 是 | Y坐标偏移，范围0 ~ 1，含义是0% ~ 100%的偏移，如果总高度是1000px，要偏移Y轴500px，值是0.5。 |
| refreshView | boolean | 是 | 是否刷新可视区域，true：是（页面滚动时，页面清晰），false：否（页面滚动时，页面模糊）。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setViewOffset(0.5, 0.5, true);
10. }
```

### getPagePixelMap

PhonePC/2in1Tablet

getPagePixelMap(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>

获取对应PDF页面的缩略图，使用Promise异步回调。

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

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let image = await pdfController.getPagePixelMap(0, true);
10. }
```

### registerScrollListener

PhonePC/2in1Tablet

registerScrollListener(listener: Callback<ScrollParam>): void

注册滚动监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[ScrollParam](pdf-arkts-pdfviewmanage.md#scrollparam)> | 是 | 页面滚动回调函数监听，返回ScrollParam类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerScrollListener((scrollParam: pdfViewManager.ScrollParam) => { });
```

### enablePageDrag

PhonePC/2in1Tablet

enablePageDrag(verticalEnabled: boolean, horizontalEnabled: boolean): void

设置页面是否支持拖拽。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verticalEnabled | boolean | 是 | 是否Y轴垂直拖动，true: 是，false: 否。 |
| horizontalEnabled | boolean | 是 | 是否X轴水平拖动，true: 是，false: 否。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.enablePageDrag(true, true);
10. }
```

### loadDocument

PhonePC/2in1Tablet

loadDocument(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult>

加载文件并显示指定的页面，使用Promise异步回调。由于loadDocument不支持重复调用，因此在二次调用之前，必须先通过releaseDocument释放当前已加载的文档，以确保资源正确释放并避免潜在的冲突或异常。

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

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. let context = this.getUIContext().getHostContext() as Context;
5. let dir = context.filesDir;
6. let tempFilePath = dir + '/test.pdf';
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(tempFilePath);
```

### releaseDocument

PhonePC/2in1Tablet

releaseDocument(): void

释放已加载的文件

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. let context = this.getUIContext().getHostContext() as Context;
5. let dir = context.filesDir;
6. let tempFilePath = dir + '/test.pdf';
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(tempFilePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.releaseDocument();
10. }
```

### setHighlightRects

PhonePC/2in1Tablet

setHighlightRects(rectArray: Array<PageRects>, color?: number): void

在UI层，以PDF页面左下角(0,0)为原点，以PDF点为单位，向上延展，高亮显示对应的矩形区域内容。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rectArray | Array<[PageRects](pdf-arkts-pdfviewmanage.md#pagerects)> | 是 | 高亮块在页面的矩形区域。rect的left、right最小值为0，最大值为PDF的宽度，top、bottom最小值为0，最大值为PDF的高度。 |
| color | number | 否 | 高亮颜色(ARGB)，取值范围0x00000000 ~ 0xFFFFFFFF，默认值：0x00000000。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit'

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. const highlightArray = new Array<pdfViewManager.PageRects>();
10. const rectArray = new Array<pdfService.PdfRect>();
11. const rect1: pdfService.PdfRect = { left: 20, top: 0, right: 120, bottom: 300 };
12. rectArray.push(rect1);
13. highlightArray.push(new pdfViewManager.PageRects(0, rectArray));
14. pdfController.setHighlightRects(highlightArray, 0xAA666666);
15. }
```

### setHighlightText

PhonePC/2in1Tablet

setHighlightText(pageIndex: number, textArray: string[], color: number): void

高亮选中文本，执行中的[searchKey](pdf-arkts-pdfviewmanage.md#searchkey)会中断。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引，0为起始页。 |
| textArray | string[] | 是 | 选中的文本。 |
| color | number | 是 | 高亮颜色(ARGB)，取值范围0x00000000 ~ 0xFFFFFFFF。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setHighlightText(1, ['1111', 'aaaa'], 0x66666666);
10. }
```

### setPageZoom

PhonePC/2in1Tablet

setPageZoom(zoom: number): void

设置视图的缩放比例。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoom | number | 是 | 缩放比例 [0.1 ~ 10]。(大于10的时候取10，小于0.1的时候取0.1) |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setPageZoom(2);
10. }
```

### getPageZoom

PhonePC/2in1Tablet

getPageZoom(): number

获取视图的缩放比例。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取视图的缩放比例 [0.1 ~ 10]。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageZoom = pdfController.getPageZoom();
10. }
```

### setMaxZoom

PhonePC/2in1Tablet

setMaxZoom(maxZoom: number): boolean;

设置视图的最大缩放比例。

说明

页面适配(PageFit)的优先级高于缩放比例(Zoom)，当同时执行了缩放比例设置与页面适配设置时，优先遵循设置的页面适配方式。

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

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';
2. import { common } from '@kit.AbilityKit';
3. @Entry
4. @Component
5. struct PdfPage {
6. private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
7. async aboutToAppear() {
8. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. let dir = context.filesDir;
10. let filePath = dir + `/input.pdf`;
11. let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
12. if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
13. this.pdfController.setMaxZoom(10);
14. }
15. }
16. build() {
17. Column() {
18. // 组件
19. }
20. }
21. }
```

### getMaxZoom

PhonePC/2in1Tablet

getMaxZoom(): number;

获取视图的最大缩放比例。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的视图最大缩放比例[0.1 ~ 10](精度支持到小数点后第2位)。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';
2. import { common } from '@kit.AbilityKit';
3. @Entry
4. @Component
5. struct PdfPage {
6. private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
7. async aboutToAppear() {
8. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. let dir = context.filesDir;
10. let filePath = dir + `/input.pdf`;
11. let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
12. if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
13. this.pdfController.getMaxZoom();
14. }
15. }
16. build() {
17. Column() {
18. // 组件
19. }
20. }
21. }
```

### setMinZoom

PhonePC/2in1Tablet

setMinZoom(minZoom: number): boolean;

设置视图的最小缩放比例。

说明

页面适配(PageFit)的优先级高于缩放比例(Zoom)，当同时执行了缩放比例设置与页面适配设置时，优先遵循设置的页面适配方式。

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

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';
2. import { common } from '@kit.AbilityKit';
3. @Entry
4. @Component
5. struct PdfPage {
6. private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
7. async aboutToAppear() {
8. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. let dir = context.filesDir;
10. let filePath = dir + `/input.pdf`;
11. let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
12. if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
13. this.pdfController.setMinZoom(0.1);
14. }
15. }
16. build() {
17. Column() {
18. // 组件
19. }
20. }
21. }
```

### getMinZoom

PhonePC/2in1Tablet

getMinZoom(): number;

获取视图的最小缩放比例。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取的视图最小缩放比例[0.1 ~ 10](精度支持到小数点后第2位)。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';
2. import { common } from '@kit.AbilityKit';
3. @Entry
4. @Component
5. struct PdfPage {
6. private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();
7. async aboutToAppear() {
8. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. let dir = context.filesDir;
10. let filePath = dir + `/input.pdf`;
11. let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
12. if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
13. this.pdfController.getMinZoom();
14. }
15. }
16. build() {
17. Column() {
18. // 组件
19. }
20. }
21. }
```

### setPageLayout

PhonePC/2in1Tablet

setPageLayout(columnCount: pdfService.PageLayout): void

设置页面布局模式：单页面：1，双页面：2。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| columnCount | pdfService.[PageLayout](pdf-arkts-pdfservice.md#pagelayout) | 是 | 页面布局模式：单页面：1，双页面：2。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setPageLayout(pdfService.PageLayout.LAYOUT_SINGLE);
10. }
```

### getPageLayout

PhonePC/2in1Tablet

getPageLayout(): pdfService.PageLayout

获取页面布局模式。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[PageLayout](pdf-arkts-pdfservice.md#pagelayout) | 页面布局模式：单页面：1，双页面：2。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageLayout: pdfService.PageLayout = pdfController.getPageLayout();
10. }
```

### setPageContinuous

PhonePC/2in1Tablet

setPageContinuous(isContinuous: boolean): void

设置页面滚动是否连续排列。仅支持垂直排列。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isContinuous | boolean | 是 | 滚动是否连续排列，true: 是，false: 否。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setPageContinuous(true);
10. }
```

### isPageContinuous

PhonePC/2in1Tablet

isPageContinuous(): boolean

获取页面是否连续排列。仅支持垂直排列

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否连续排列，true: 是，false: 否。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageContinuous: boolean = pdfController.isPageContinuous();
10. }
```

### setPageFit

PhonePC/2in1Tablet

setPageFit(pageFit: pdfService.PageFit): void

设置页面的适配模式。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageFit | pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit) | 是 | 页面的适配模式。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setPageFit(pdfService.PageFit.FIT_NONE);
10. }
```

### getPageFit

PhonePC/2in1Tablet

getPageFit(): pdfService.PageFit

获取页面的适配模式。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit) | 页面的适配模式。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageFitMode: pdfService.PageFit = pdfController.getPageFit();
10. }
```

### setPageSpacing

PhonePC/2in1Tablet

setPageSpacing(horizontal: number, vertical?: number): void

设置页面之间的行间距和列间距。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontal | number | 是 | 双页模式下左右页面之间的间距，大于等于0，单位为px。 |
| vertical | number | 否 | 连续滚动时上下页面的间距，大于等于0，单位为px，默认值：10。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setPageSpacing(20, 20);
10. }
```

### getPageHorizontalSpacing

PhonePC/2in1Tablet

getPageHorizontalSpacing(): number

获取双页模式下左右页面之间的间距。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 左右页面之间的间距，单位为vp。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let horSpacing = pdfController.getPageHorizontalSpacing();
10. }
```

### getPageVerticalSpacing

PhonePC/2in1Tablet

getPageVerticalSpacing(): number

获取上下页之间的间距。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 上下页之间的间距，单位为vp。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let verSpacing = pdfController.getPageVerticalSpacing();
10. }
```

### getPageCount

PhonePC/2in1Tablet

getPageCount(): number

获取PDF的总页数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 总页数，大于等于0。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageCount = pdfController.getPageCount();
10. }
```

### getPageIndex

PhonePC/2in1Tablet

getPageIndex(): number

获取PDF当前页的索引。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 页面索引。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageIndex = pdfController.getPageIndex();
10. }
```

### goToPage

PhonePC/2in1Tablet

goToPage(pageIndex: number): void

跳转到指定页。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 指定页索引，0为起始页，小于总页数。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.goToPage(1);
10. }
```

### setPageRotation

PhonePC/2in1Tablet

setPageRotation(pageIndex: number, angle: pdfService.RotationAngle): void

设置指定页面在PdfView组件中显示的旋转角度。旋转角度为逆时针方向的固定值，可选值包括 0、90、180、270 度。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 指定页索引，0为起始页，小于总页数。 |
| angle | pdfService.[RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 是 | 指定页旋转角度。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setPageRotation(1, pdfService.RotationAngle.ANGLE_90);
10. }
```

### getPageRotation

PhonePC/2in1Tablet

getPageRotation(pageIndex: number): pdfService.RotationAngle

获取指定页面的旋转度数： 0、90、180、270度。

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

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pageIndex: pdfService.RotationAngle = pdfController.getPageRotation(1);
10. }
```

### enableAnnotation

PhonePC/2in1Tablet

enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void

在常用操作之间切换并添加批注。目前支持高亮、下划线和删除线。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 是 | 支持的批注类型。 |
| color | number | 否 | 颜色(ARGB)，范围0x00000000 - 0xFFFFFFFF，默认值：0xFFFFFFFF。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAEEEEEE);
10. }
```

### addMarkupAnnotation

PhonePC/2in1Tablet

addMarkupAnnotation(annotationType: SupportedAnnotationType, selectedRects: Array<SelectedRects>, color: number): void

在PDF注释层，以PDFView视图左上角(0,0)为原点，以像素点为单位，向下延展，添加文本批注。文本批注添加成功后，通过[registerAnnotationSelectedListener](pdf-arkts-pdfviewmanage.md#registerannotationselectedlistener)回调来高亮显示文本批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 是 | 批注类型。 |
| selectedRects | Array<[SelectedRects](pdf-arkts-pdfviewmanage.md#selectedrects)> | 是 | 高亮显示的矩形区域。 |
| color | number | 是 | 颜色(ARGB)，范围0x00000000 - 0xFFFFFFFF。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let rectArray: Array<pdfService.PdfRect> = [{ left: 5, top: 5, right: 250, bottom: 250}];
10. let selectedRects: Array<pdfViewManager.SelectedRects> = [new pdfViewManager.SelectedRects(0, rectArray, 0)];
11. pdfController.addMarkupAnnotation(pdfViewManager.SupportedAnnotationType.UNDERLINE, selectedRects, 0xAA666666);
12. }
```

### disableAnnotation

PhonePC/2in1Tablet

disableAnnotation(): void

禁止添加批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.disableAnnotation();
10. }
```

### deleteSelectedAnnotation

PhonePC/2in1Tablet

deleteSelectedAnnotation(annotationIndex: number, pageIndex: number): void

删除选中的批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationIndex | number | 是 | 批注索引，从0开始。 |
| pageIndex | number | 是 | 页面索引，从0开始。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. // 确保第一页存在一个批注
10. pdfController.deleteSelectedAnnotation(0, 0);
11. }
```

### updateMarkupAnnotation

PhonePC/2in1Tablet

updateMarkupAnnotation(annotationIndex: number, pageIndex: number, color: number): void

修改批注颜色。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationIndex | number | 是 | 批注索引。 |
| pageIndex | number | 是 | 页面索引。 |
| color | number | 是 | 颜色（ARGB），范围0x00000000 - 0xFFFFFFFF。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. // 确保第一页存在一个批注
10. pdfController.updateMarkupAnnotation(0, 0, 0xAA000000);
11. }
```

### saveDocument

PhonePC/2in1Tablet

saveDocument(path: string, onProgress?: Callback<number>): Promise<number>

保存PDF文档，使用Promise异步回调。

说明

由于文档不可同时读写，如果需要覆盖回原文档，请创建临时文档作为过渡。具体请参见下方示例代码。

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

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';

4. // 将测试文件上传至应用沙箱路径
5. let context = this.getUIContext().getHostContext() as Context;
6. let dir = context.filesDir;
7. let tempDir = context.tempDir;
8. // 确保该路径下的源文档有读写的权限
9. let filePath = dir + `/input.pdf`;
10. let tempFilePath = tempDir + `/temp${Math.random()}.pdf`;
11. fs.copyFileSync(filePath, tempFilePath);
12. let pdfController = new pdfViewManager.PdfController();
13. // 加载临时文件
14. let loadResult = await pdfController.loadDocument(tempFilePath, '');
15. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
16. // 保存文件将覆盖源文档
17. let result = await pdfController.saveDocument(filePath);
18. }
19. pdfController.releaseDocument();
```

### registerSelectedRectsChangedListener

PhonePC/2in1Tablet

registerSelectedRectsChangedListener(listener: Callback<Array<SelectedRects>>): void

选中文本拖拽窗口变化，导致选中区域高亮块也要同步变化。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<Array<[SelectedRects](pdf-arkts-pdfviewmanage.md#selectedrects)>> | 是 | 选中文本拖拽窗口变化回调函数监听，返回SelectedRects类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerSelectedRectsChangedListener((pageRects: Array<pdfViewManager.SelectedRects>) => {});
```

### registerPageFitChangedListener

PhonePC/2in1Tablet

registerPageFitChangedListener(listener: Callback<pdfService.PageFit>): void

注册页面适配变化监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit)> | 是 | 页面适配变化回调函数监听，返回PageFit类型数据。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerPageFitChangedListener((pageFit: pdfService.PageFit) => {});
```

### registerPageChangedListener

PhonePC/2in1Tablet

registerPageChangedListener(listener: Callback<number>): void

注册页面索引变化监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 页面索引变化回调函数监听，返回页面索引number类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerPageChangedListener((pageIndex: number) => {});
```

### registerScaleChangedListener

PhonePC/2in1Tablet

registerScaleChangedListener(listener: Callback<number>): void

注册页面缩放变化监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 页面缩放回调函数监听，返回缩放值number类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerScaleChangedListener((scale: number) => {});
```

### registerTextSelectedListener

PhonePC/2in1Tablet

registerTextSelectedListener(listener: Callback<TextSelectedParam>): void

注册文本选中监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[TextSelectedParam](pdf-arkts-pdfviewmanage.md#textselectedparam)> | 是 | 页面文本被选中回调函数监听，返回选中文本TextSelectedParam类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerTextSelectedListener((pageText: pdfViewManager.TextSelectedParam) => {});
```

### registerAnnotationSelectedListener

PhonePC/2in1Tablet

registerAnnotationSelectedListener(listener: Callback<SelectedAnnotation>): void

注册页面批注选中监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[SelectedAnnotation](pdf-arkts-pdfviewmanage.md#selectedannotation)> | 是 | 页面批注被选中回调函数监听，返回选中批注SelectedAnnotation类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerAnnotationSelectedListener((pdfAnnotation: pdfViewManager.SelectedAnnotation) => {});
```

### registerImageSelectedListener

PhonePC/2in1Tablet

registerImageSelectedListener(listener: Callback<ImageSelectedParam>): void

注册图片选中监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[ImageSelectedParam](pdf-arkts-pdfviewmanage.md#imageselectedparam)> | 是 | 页面图片被选中回调函数监听，返回选中图片ImageSelectedParam类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerImageSelectedListener((image: pdfViewManager.ImageSelectedParam) => {});
```

### registerActionClickListener

PhonePC/2in1Tablet

registerActionClickListener(listener: Callback<RedirectInfo>): void

注册Click动作的时候监听器，例如：拿到值是链接地址可以拉取浏览器跳转到相应的网页。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[RedirectInfo](pdf-arkts-pdfviewmanage.md#redirectinfo)> | 是 | Click动作回调函数监听，返回RedirectInfo类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerActionClickListener((redirectInfo: pdfViewManager.RedirectInfo) => {});
```

### registerAnnotationChangedListener

PhonePC/2in1Tablet

registerAnnotationChangedListener(listener: Callback<AnnotationChangedParam>): void

注册批注变化监听器。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<[AnnotationChangedParam](pdf-arkts-pdfviewmanage.md#annotationchangedparam)> | 是 | 批注变化时回调函数监听，返回AnnotationChangedParam类型数据。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerAnnotationChangedListener((annotationChange: pdfViewManager.AnnotationChangedParam) => {});
```

### registerPageCountChangedListener

PhonePC/2in1Tablet

registerPageCountChangedListener(listener: Callback<number>): void

注册总页数变化的时候监听器，需要在loadDocument之前调用，否则无法捕获loadDocument期间的页数变化事件。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 总页数变化回调函数监听，返回number类型总页数。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let pdfController = new pdfViewManager.PdfController();
4. pdfController.registerPageCountChangedListener((pageCount: number) => {});
```

### searchKey

PhonePC/2in1Tablet

searchKey(text: string, listener: Callback<number>): void

搜索文本并返回匹配的总数，执行搜索会清除之前通过[setHighlightText](pdf-arkts-pdfviewmanage.md#sethighlighttext)设置的文本高亮。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 搜索的文本。 |
| listener | [Callback](js-apis-base.md#callback)<number> | 是 | 搜索文本回调函数监听，返回number类型的匹配总数。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.searchKey('a', (index: number) => {});
10. }
```

### clearSearch

PhonePC/2in1Tablet

clearSearch(): void

清除搜索文本的高亮，等价于搜索空字符串 。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.clearSearch();
10. }
```

### getSearchIndex

PhonePC/2in1Tablet

getSearchIndex(): number

获取当前命中搜索关键字匹配结果的索引，执行搜索接口后默认命中索引为0。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 匹配结果索引，大于等于0。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let res = pdfController.getSearchIndex();
10. }
```

### setSearchIndex

PhonePC/2in1Tablet

setSearchIndex(index: number): void

设置搜索匹配结果的索引，页面会跳转到索引对应搜索结果处。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 搜索结果索引，从0开始。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setSearchIndex(1);
10. }
```

### setDisplayDirection

PhonePC/2in1Tablet

setDisplayDirection(displayDirection: DisplayDirection): void

设置PDF非连续模式下文档的翻页方向。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayDirection | [DisplayDirection](pdf-arkts-pdfviewmanage.md#displaydirection) | 是 | 翻页的方向（默认竖直方向）。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';

3. let context = this.getUIContext().getHostContext() as Context;
4. let dir = context.filesDir;
5. let filePath = dir + `/input.pdf`;
6. let pdfController = new pdfViewManager.PdfController();
7. let loadResult: pdfService.ParseResult = await pdfController.loadDocument(filePath);
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfController.setDisplayDirection(pdfViewManager.DisplayDirection.VERTICAL);
10. }
```

### setNestedScroll

PhonePC/2in1Tablet

setNestedScroll(value: PdfNestedScrollOptions): void

设置嵌套滑动选项。可以设置上下左右四个方向，实现与父组件的滑动联动。

说明

若PdfNestedScrollOptions中的PdfNestedScrollMode设置为SELF\_FIRST，滑动到边缘后放手重新触发滑动才会滑动父组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PdfNestedScrollOptions](pdf-arkts-pdfviewmanage.md#pdfnestedscrolloptions) | 是 | 可滚动组件滚动时的嵌套滑动选项，包括scrollUp、scrollDown、scrollLeft、scrollRight，默认值为[PdfNestedScrollMode](pdf-arkts-pdfviewmanage.md#pdfnestedscrollmode).SELF\_ONLY。 |

**示例：**

```
1. import { pdfViewManager, pdfService } from '@kit.PDFKit';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct PdfPage {
7. private pdfController: pdfViewManager.PdfController = new pdfViewManager.PdfController();

9. async aboutToAppear() {
10. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
11. let dir = context.filesDir;
12. let filePath = dir + `/input.pdf`;

14. let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);

16. if (loadResult !== undefined && pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
17. this.pdfController.setNestedScroll({
18. scrollUp: pdfViewManager.PdfNestedScrollMode.SELF_ONLY,
19. scrollDown: pdfViewManager.PdfNestedScrollMode.SELF_ONLY,
20. scrollLeft: pdfViewManager.PdfNestedScrollMode.SELF_ONLY,
21. scrollRight: pdfViewManager.PdfNestedScrollMode.SELF_ONLY
22. });
23. }
24. }

26. build() {
27. Column() {
28. // 组件
29. }
30. }
31. }
```

## RedirectInfo

PhonePC/2in1Tablet

PDF页面重定向信息类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | 否 | 否 | 重定向信息内容。 |
| actionType | [RedirectType](pdf-arkts-pdfviewmanage.md#redirecttype) | 否 | 否 | 重定向类型。 |

### constructor

PhonePC/2in1Tablet

constructor(content: string, actionType: RedirectType)

用于创建PDF页面重定向信息类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 重定向信息内容。 |
| actionType | [RedirectType](pdf-arkts-pdfviewmanage.md#redirecttype) | 是 | 重定向类型。 |

**示例：**

```
1. import { pdfViewManager } from '@kit.PDFKit';

3. let redirectInfo = new pdfViewManager.RedirectInfo('https://www.test.com', pdfViewManager.RedirectType.URI);
```

## SelectedAnnotation

PhonePC/2in1Tablet

PDF选择的批注信息。

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

PhonePC/2in1Tablet

页面中矩形区域类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pageIndex | number | 否 | 否 | 页面索引。 |
| rectArray | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 否 | 否 | 数组PdfRect类型。 |

### constructor

PhonePC/2in1Tablet

constructor(pageIndex: number, rectArray: Array<pdfService.PdfRect>)

用于创建页面中矩形区域类的对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引。 |
| rectArray | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 是 | 数组PdfRect类型。 |

## SelectedRects

PhonePC/2in1Tablet

PDF页面中选定文本的矩形区域类，继承[PageRects](pdf-arkts-pdfviewmanage.md#pagerects)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isRotated | number | 否 | 否 | 是否支持旋转，0：否，1：是。 |

### constructor

PhonePC/2in1Tablet

constructor(pageIndex: number, rectArray: Array<pdfService.PdfRect>, isRotated: number)

用于创建PDF页面中选定文本的矩形区域类的对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 页面索引。 |
| rectArray | Array<pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 是 | 数组PdfRect类型。 |
| isRotated | number | 是 | 是否支持旋转，0：否，1：是。 |

**示例：**

```
1. import { pdfService, pdfViewManager } from '@kit.PDFKit';

3. let rectArray: Array<pdfService.PdfRect> = new Array<pdfService.PdfRect>();
4. const rect1: pdfService.PdfRect = { left: 5, top: 5, right: 250, bottom: 250};
5. rectArray.push(rect1);
6. let selectedRects: pdfViewManager.SelectedRects = new pdfViewManager.SelectedRects(0, rectArray, 0);
```

## ScrollParam

PhonePC/2in1Tablet

PDF页面[registerScrollListener](pdf-arkts-pdfviewmanage.md#registerscrolllistener)监听函数回调参数。

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

PhonePC/2in1Tablet

PDF页面 registerTextSelectedListener 监听函数回调参数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 选中的文本内容。 |
| pdfRect | Array<[SelectedRects](pdf-arkts-pdfviewmanage.md#selectedrects)> | 否 | 否 | 选中的文本在PDF页面的矩形区域。 |

## ImageSelectedParam

PhonePC/2in1Tablet

PDF页面 registerImageSelectedListener 监听函数回调参数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageType | pdfService.[ImageFormat](pdf-arkts-pdfservice.md#imageformat) | 否 | 否 | 选中的图片类型。 |
| buffer | ArrayBuffer | 否 | 是 | buffer参数是图像内容。如果缓冲区为空，则取消选择。 |
| pdfRect | pdfService.[PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 否 | 是 | 选中的图片在PDF页面的矩形区域。 |
| pageIndex | number | 否 | 是 | 页码索引。 |

## AnnotationChangedParam

PhonePC/2in1Tablet

PDF页面 registerAnnotationChangedListener 监听函数回调参数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | number | 否 | 否 | 颜色(ARGB)，范围0x00000000 ~ 0xFFFFFFFF。 |
| annotationType | [SupportedAnnotationType](pdf-arkts-pdfviewmanage.md#supportedannotationtype) | 否 | 否 | 批注类型。 |
| pageIndexArray | Array<number> | 否 | 否 | 批注在页面的的索引列表。 |
| controlType | [AnnotationEditType](pdf-arkts-pdfviewmanage.md#annotationedittype) | 否 | 否 | 批注编辑类型，0：添加，1：修改，2：删除。 |

## SupportedAnnotationType

PhonePC/2in1Tablet

PDF页面支持的批注类型。

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

PhonePC/2in1Tablet

PDF页面上支持的批注更改类型。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADD | 0 | 添加。 |
| MODIFY | 1 | 修改。 |
| DELETE | 2 | 删除。 |

## RedirectType

PhonePC/2in1Tablet

需要进行重定向的ActionType。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| URI | 6 | uri地址。 |
| LAUNCH | 4 | launch，本地文件路径。 |

## DisplayDirection

PhonePC/2in1Tablet

非连续显示时的翻页方向。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VERTICAL | 0 | 竖直方向翻页。 |
| HORIZONTAL | 1 | 水平方向翻页。 |

## PdfNestedScrollOptions

PhonePC/2in1Tablet

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

PhonePC/2in1Tablet

定义嵌套滑动组件中的嵌套模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.2(22)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELF\_ONLY | 0 | 只自身滑动，不与父组件联动。 |
| SELF\_FIRST | 1 | 自身先滑动，自身滑动到边缘以后父组件滑动。如果父组件有边缘效果，在滑动到父组件边缘后，触发父组件边缘效果，否则触发子组件的边缘效果。 |
