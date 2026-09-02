---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice
title: pdfService（PDF服务）
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS API > pdfService（PDF服务）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:06+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9650dfaaa685cc0b651b7b4bb78aef9e6fc595235313858bd377a79213cdec30
---

本模块为应用提供统一的管理PDF页面的页眉页脚、水印和背景、文档的多种批注风格和书签等便捷的PDF能力。

**注：**

1. 涉及到尺寸和坐标的属性都是以点（Points）为单位，一英寸等于72Points。
2. 对PDF文件进行编辑操作后，需要调用[saveDocument](pdf-arkts-pdfservice.md#savedocument)接口将PDF文件保存，确保编辑操作生效。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { pdfService } from '@kit.PDFKit';
```

## PdfDocument

PDF文档类。

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
import { pdfService } from '@kit.PDFKit';

let pdfDocument = new pdfService.PdfDocument();
```

### loadDocument

loadDocument(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult

加载指定文件路径。由于loadDocument不支持重复调用，因此在二次调用之前，必须先通过releaseDocument释放当前已加载的文档，以确保资源正确释放并避免潜在的冲突或异常。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文档路径。 |
| password | string | 否 | 文档加密密码。默认值：空字符串 |
| onProgress | (progress: number) => number | 否 | 进度条回调函数，传此参数返回文档加载进度，不传不返回文档加载进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ParseResult](pdf-arkts-pdfservice.md#parseresult) | ParseResult枚举类型。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
```

### releaseDocument

releaseDocument(): void

释放PDF文档。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfDocument = new pdfService.PdfDocument();
// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfDocument.releaseDocument();
}
```

### saveDocument

saveDocument(path: string, onProgress?: (progress: number) => number): boolean

保存文档。

**说明** 

由于文档不可同时读写，如果需要覆盖回原文档，请创建临时文档作为过渡。具体请参见下方示例代码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文档的沙箱路径。 |
| onProgress | (progress: number) => number | 否 | 进度条回调函数，传此参数返回文档保存进度，不传不返回文档保存进度 。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否保存文档成功，true表示成功，false表示失败。 |

**示例：**

```typescript
import { fileIo } from '@kit.CoreFileKit';
import { pdfService } from '@kit.PDFKit';
import { Font } from '@kit.ArkUI';

// 将测试文件上传至应用沙箱路径
let context = this.getUIContext().getHostContext() as Context;
let dir = context.filesDir;
let tempDir = context.tempDir;
// 确保该路径下的源文档有读写的权限
let filePath = dir + `/input.pdf`;
let tempFilePath = tempDir + `/temp${Math.random()}.pdf`;
fs.copyFileSync(filePath, tempFilePath);
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
// 对文档加一些水印
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
  wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
  wminfo.content = "This is Watermark";
  wminfo.textSize = 30;
  wminfo.textColor = 200;
  wminfo.fontInfo = new pdfService.FontInfo();
  let font: Font = new Font()
  wminfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans").path;
  wminfo.opacity = 0.5;
  wminfo.isOnTop = true;
  wminfo.rotation = 45;
  wminfo.scale = 1.5;
  wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
  wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
  wminfo.horizontalSpace = 1.0;
  wminfo.verticalSpace = 1.0;
  pdfDocument.addWatermark(wminfo, 0, 1, true, true);
  // 保存文件将覆盖源文档
  let result = pdfDocument.saveDocument(filePath);
}
```

### createDocument

createDocument(width: number, height: number): boolean

创建空白文档。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 文档宽度，必须大于0，单位为Points（一英寸等于72Points）。 |
| height | number | 是 | 文档高度，必须大于0，单位为Points（一英寸等于72Points）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功创建文档，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfDocument = new pdfService.PdfDocument();
pdfDocument.createDocument(600, 900);
```

### isEncrypted

isEncrypted(path: string): boolean

文档是否加密。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 文档是否加密，true表示加密，false表示没有加密。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let isEncrypted = pdfDocument.isEncrypted(tempFilePath);
}
```

### removeSecurity

removeSecurity(): boolean

删除文档加密锁。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功删除文档加密锁，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let result = pdfDocument.removeSecurity();
}
```

### getPageCount

getPageCount(): number

获取文档页数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文档总页数，取值范围大于0。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageCount = pdfDocument.getPageCount();
}
```

### getPage

getPage(index: number): PdfPage

获取指定页的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 获取第几页对象，大于等于0，小于总页数，0为起始页。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfPage](pdf-arkts-pdfservice.md#pdfpage) | 指定页的对象 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage = pdfDocument.getPage(0);
}
```

### insertBlankPage

insertBlankPage(index: number, width: number, height: number): PdfPage

在指定位置插入PDF空白页，原位置PDF页顺序后移。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| index | number | 是 | 在第几页插入PDF页，必须大于等于0，小于总页数，0为起始页。 |
| width | number | 是 | 插入PDF页宽度，必须大于0，单位为Points（一英寸等于72Points）。 |
| height | number | 是 | 插入PDF页高度，必须大于0，单位为Points（一英寸等于72Points）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfPage](pdf-arkts-pdfservice.md#pdfpage) | 插入的PDF页 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage = pdfDocument.insertBlankPage(1, 600, 900);
}
```

### insertPageFromDocument

insertPageFromDocument(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage

将其他Document的Page添加到当前Document，Page中的批注不支持插入到当前Document。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| document | [PdfDocument](pdf-arkts-pdfservice.md#pdfdocument) | 是 | PdfDocument对象。 |
| fromIndex | number | 是 | 从其他文档第几页开始添加，大于等于0，0为起始页。 |
| pageCount | number | 是 | 添加页数量，大于0且不超过总页数。最大支持1000页，从fromIndex起插入，超出1000页部分不插入且不报错。 |
| index | number | 是 | 从当前文档第几页开始添加，大于等于0，小于总页数，0为起始页。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfPage](pdf-arkts-pdfservice.md#pdfpage) | 插入的PDF最后一页。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath1 = '/data/storage/el2/base/temp/test1.pdf';
let document: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult1 = document.loadDocument(tempFilePath1, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult1) {
  // 将测试文件上传至应用沙箱路径
  let tempFilePath2 = '/data/storage/el2/base/temp/test2.pdf';
  let pdfDocument2 = new pdfService.PdfDocument();
  // 加载临时文件
  let loadResult2 = pdfDocument2.loadDocument(tempFilePath2, '');
  if(pdfService.ParseResult.PARSE_SUCCESS === loadResult2) {
    let page = pdfDocument2.insertPageFromDocument(document, 1, 2, 3);
  }
}
```

### deletePage

deletePage(index: number, count: number): void

删除指定位置PDF页。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| index | number | 是 | 从当前文档第几页开始，索引大于等于0，小于总页数，0为起始页。 |
| count | number | 是 | 删除几个PDF页面，大于0，小于等于总页数。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfDocument.deletePage(1, 2);
}
```

### movePage

movePage(index: number, dest: number): boolean

将index索引的页面插入到dest指定的位置，原dest索引的页面顺序后移。

**说明** 

例如原页面顺序是0，1，2，3，4

movePage(2, 3)，Page[2]移动到Page[3]的位置，原Page[3]后移，顺序不变：0，1，2，3，4。

movePage(2, 4)，Page[2]移动到Page[4]的位置，原Page[4]后移，顺序变为：0，1，3，2，4。

movePage(3, 2)，Page[3]移动到Page[2]的位置，原Page[2]后移，顺序变为：0，1，3，2，4。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| index | number | 是 | 指定页面索引，大于等于0，小于总页数，0为起始页。 |
| dest | number | 是 | 目标页面索引，大于等于0，小于等于总页数，0为起始页。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功将指定页面移到索引位置，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfDocument.movePage(2, 4);
}
```

### getFontWeight

getFontWeight(): number

获取字体粗细。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 字体粗细，必须大于0，单位为Points（一英寸等于72Points）。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let weight = pdfDocument.getFontWeight();
}
```

### setFontWeight

setFontWeight(weight: number): void

设置字体粗细。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| weight | number | 是 | 字体粗细，必须大于0，单位为Points（一英寸等于72Points）。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let weight = pdfDocument.setFontWeight(10);
}
```

### getMetadata

getMetadata(): Metadata

获取PDF元数据，包括作者、创建者、创建日期等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Metadata](pdf-arkts-pdfservice.md#metadata) | PDF元数据 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  pdfDocument.getMetadata();
}
```

### convertToImage

convertToImage(path: string, format: ImageFormat, onProgress?: (progress: number) => number): boolean

转换PDF文档为图片。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |
| format | [ImageFormat](pdf-arkts-pdfservice.md#imageformat) | 是 | 图片枚举类型。 |
| onProgress | (progress: number) => number | 否 | 转换成图片进度，传此参数返回转换进度，不传不返回转换进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功转换图片，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { fileIo } from '@kit.CoreFileKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let context = this.getUIContext().getHostContext() as Context;
  let dir = context.filesDir + '/output/';
  await fileIo.mkdir(dir);
  let result = pdfDocument.convertToImage(dir, pdfService.ImageFormat.PNG);
}
```

### getRootBookmark

getRootBookmark(): Bookmark

获取PDF文档第一个根书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 第一个根书签。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let rootBookmark = pdfDocument.getRootBookmark();
}
```

### getRootBookmarks

getRootBookmarks(): Array<Bookmark>

PDF文档获取根书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Bookmark](pdf-arkts-pdfservice.md#bookmark)> | 根书签。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let rootBookmark = pdfDocument.getRootBookmarks();
}
```

### createBookmark

createBookmark(): Bookmark

创建PDF文档书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 成功创建的书签，并返回Bookmark信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let rootBookmark: pdfService.Bookmark = pdfDocument.createBookmark();
}
```

### removeBookmark

removeBookmark(bookmark: Bookmark): boolean

移除PDF文档书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bookmark | [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 是 | 要移除的书签对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功移除书签，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let bookmarks: Array<pdfService.Bookmark> = pdfDocument.getRootBookmarks();
  if (bookmarks.length && bookmarks[0].isRootBookmark()) {
    let isRemoved: boolean = pdfDocument.removeBookmark(bookmarks[0]);
  }
}
```

### insertBookmark

insertBookmark(bookmark: Bookmark, parent: Bookmark, position: number): boolean

插入PDF文档书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| bookmark | [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 是 | 书签的信息。 |
| parent | [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 是 | 父类书签信息，可以传null。 |
| position | number | 是 | 子书签位置，从1开始，找到子书签的位置，则插在该子书签的后面，如果没找到子书签的位置，则插在第一个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功插入书签，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let parentBookmark: pdfService.Bookmark = pdfDocument.createBookmark();
  let bookmark: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(bookmark, null, 1);
  pdfDocument.insertBookmark(bookmark, parentBookmark, 1);
  let bool1: boolean = parentBookmark.isRootBookmark();
  let bool2: boolean = bookmark.isRootBookmark();
}
```

### addHeaderFooter

addHeaderFooter(info: HeaderFooterInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

插入PDF文档页眉页脚。该方法属于耗时业务，需要遍历每一页去添加页眉页脚，添加页面较多时建议放到线程中去处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| info | [HeaderFooterInfo](pdf-arkts-pdfservice.md#headerfooterinfo) | 是 | 页眉页脚的信息。 |
| startIndex | number | 是 | 起始页，必须大于等于0，0为起始页。 |
| endIndex | number | 是 | 结束页，小于总页数。 |
| oddPages | boolean | 是 | 奇数页是否添加，true表示是，false表示否。 |
| evenPages | boolean | 是 | 偶数页是否添加，true表示是，false表示否。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { Font } from '@kit.ArkUI';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let document: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = document.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let hfInfo: pdfService.HeaderFooterInfo = new pdfService.HeaderFooterInfo();
  hfInfo.fontInfo = new pdfService.FontInfo();
  let font: Font = new Font()
  hfInfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans")?.path; // 确保字体存在
  hfInfo.fontInfo.fontName = '';
  hfInfo.textSize = 10;
  hfInfo.charset = pdfService.CharsetType.PDF_FONT_DEFAULT_CHARSET;
  hfInfo.underline = false;
  hfInfo.textColor = 0x00000000;
  hfInfo.leftMargin = 1.0;
  hfInfo.topMargin = 40.0;
  hfInfo.rightMargin = 1.0;
  hfInfo.bottomMargin = 40.0;
  hfInfo.headerLeftText = "left H <<dd.mm.yyyy>><<1/n>>";
  hfInfo.headerCenterText = "center H <<m/d/yyyy>><<1>>";
  hfInfo.headerRightText = "right H <<m/d>><<1/n>>";
  hfInfo.footerLeftText = "left F <<m/d>><<1>>";
  hfInfo.footerCenterText = "center F <<m/d>><<1>>";
  hfInfo.footerRightText = "right F <<dd.mm.yyyy>><<1>>";
  document.addHeaderFooter(hfInfo, 1, 5, true, true);
}
```

### getHeaderFooter

getHeaderFooter(): HeaderFooterInfo

获取PDF文档页眉页脚。没有页眉页脚的PDF文档获取的HeaderFooterInfo的属性是默认值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HeaderFooterInfo](pdf-arkts-pdfservice.md#headerfooterinfo) | 获取到的页眉页脚信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let headerFooterInfo = pdfDocument.getHeaderFooter();
}
```

### hasHeaderFooter

hasHeaderFooter(): boolean

PDF文档是否有页眉页脚。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PDF文档是否有页眉页脚，true表示有，false表示没有。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let hasHeaderFooter: boolean = pdfDocument.hasHeaderFooter();
}
```

### removeHeaderFooter

removeHeaderFooter(): boolean

删除PDF文档页眉页脚。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除PDF文档页眉页脚，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  if (pdfDocument.hasHeaderFooter()) {
    let delHeaderFooter: boolean = pdfDocument.removeHeaderFooter();
  }
}
```

### addWatermark

addWatermark(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

插入PDF文档水印。该方法属于耗时业务，需要遍历每一页去添加水印，添加页面较多时建议放到线程中去处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| info | [WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo) | 是 | 水印的信息。 |
| startIndex | number | 是 | 起始页，必须大于等于0，0为起始页。 |
| endIndex | number | 是 | 结束页，小于总页数。 |
| oddPages | boolean | 是 | 奇数页是否添加，true表示是，false表示否。 |
| evenPages | boolean | 是 | 偶数页是否添加，true表示是，false表示否。 |

**示例：**

* 添加文本水印

```typescript
import { pdfService } from '@kit.PDFKit';
import { Font } from '@kit.ArkUI';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
  wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
  wminfo.content = "This is watermark";
  wminfo.textSize = 30;
  wminfo.textColor = 200;
  wminfo.fontInfo = new pdfService.FontInfo();
  let font: Font = new Font()
  wminfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans").path;
  wminfo.opacity = 0.5;
  wminfo.isOnTop = true;
  wminfo.rotation = 45;
  wminfo.scale = 1.5;
  wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
  wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
  wminfo.horizontalSpace = 1.0;
  wminfo.verticalSpace = 1.0;
  pdfDocument.addWatermark(wminfo, 1, 18, true, true);
}
```

* 添加图片水印

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
  wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_IMAGE;
  wminfo.imagePath = "/data/storage/el2/base/haps/View/files/img.jpg";
  wminfo.opacity = 0.5;
  wminfo.isOnTop = true;
  wminfo.rotation = 45;
  wminfo.scale = 1.5;
  wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
  wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
  wminfo.horizontalSpace = 1.0;
  wminfo.verticalSpace = 1.0;
  pdfDocument.addWatermark(wminfo, 1, 18, true, true);
}
```

### getWatermark

getWatermark(): WatermarkInfo

获取PDF文档水印。没有水印的PDF文档获取的WatermarkInfo的属性是默认值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo) | 获取PDF文档水印信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let watermarkInfo: pdfService.WatermarkInfo = pdfDocument.getWatermark();
}
```

### hasWatermark

hasWatermark(): boolean

PDF文档是否有水印。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PDF文档是否有水印，true表示有，false表示没有。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let hasWatermark: boolean = pdfDocument.hasWatermark();
}
```

### removeWatermark

removeWatermark(): boolean

删除PDF文档水印。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否删除PDF文档水印成功，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let hasWatermark: boolean = pdfDocument.hasWatermark();
  if (hasWatermark) {
    let hasRemoveWatermark = pdfDocument.removeWatermark();
  }
}
```

### addBackground

addBackground(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

插入PDF文档背景。该方法属于耗时业务，需要遍历每一页去添加背景，添加页面较多时建议放到线程中去处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| info | [BackgroundInfo](pdf-arkts-pdfservice.md#backgroundinfo) | 是 | 背景的信息。 |
| startIndex | number | 是 | 起始页，必须大于等于0，0为起始页。 |
| endIndex | number | 是 | 结束页，小于总页数。 |
| oddPages | boolean | 是 | 奇数页是否添加，true表示是，false表示否。 |
| evenPages | boolean | 是 | 偶数页是否添加，true表示是，false表示否。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let bginfo: pdfService.BackgroundInfo = new pdfService.BackgroundInfo();
  bginfo.imagePath = "/data/storage/el2/base/haps/View/files/img.jpg";
  bginfo.backgroundColor = 50;
  bginfo.isOnTop = true;
  bginfo.rotation = 90;
  bginfo.scale = 0.5;
  bginfo.opacity = 0.3;
  bginfo.verticalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_TOP;
  bginfo.horizontalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_LEFT;
  bginfo.horizontalSpace = 1.0;
  bginfo.verticalSpace = 1.0;
  pdfDocument.addBackground(bginfo, 2, 18, true, true);
}
```

### getBackground

getBackground(): BackgroundInfo

获取PDF文档背景信息。没有背景的PDF文档获取的BackgroundInfo的属性是默认值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BackgroundInfo](pdf-arkts-pdfservice.md#backgroundinfo) | 获取PDF文档背景信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  if (pdfDocument.hasBackground()) {
    let backgroundInfo: pdfService.BackgroundInfo = pdfDocument.getBackground();
  }
}
```

### hasBackground

hasBackground(): boolean

PDF文档是否有背景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PDF文档是否有背景，true表示有，false表示没有。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let hasBackground: boolean = pdfDocument.hasBackground();
}
```

### removeBackground

removeBackground(): boolean

删除PDF文档背景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功删除背景，true表示成功，false表示失败。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  if (pdfDocument.hasBackground()) {
    let delBackground: boolean = pdfDocument.removeBackground();
  }
}
```

### setPdfPassword

setPdfPassword(password: string): boolean

采用AES-256加密算法,对PDF文件进行加密。

**说明** 

加密后的文件仅在支持AES-256的PDF阅读软件中正常打开。若使用不支持AES-256的软件打开，可能会因兼容性问题导致打开失败，并提示“密码错误”。请尝试使用支持AES-256的软件打开该文件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| password | string | 是 | 密码（只支持0-127以内的ASCII字符）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否添加密码成功。  - true：添加成功  - false：添加失败 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(filePath);
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
   let setPassword: boolean = pdfDocument.setPdfPassword('123456');
 }
```

### getPixelMapWithPages

getPixelMapWithPages(pageIndices: number[], matrices: PdfMatrix[], bitmapWidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap

获取多个页面合并后的pixelMap，最多支持指定16张PDF页面。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndices | number[] | 是 | 页面索引数组，0为起始页。 |
| matrices | [PdfMatrix](pdf-arkts-pdfservice.md#pdfmatrix)[] | 是 | 坐标变换矩阵数组，用于在渲染时对页面内容做缩放、平移、旋转等。与pageIndices数组一一对应。 |
| bitmapWidth | number | 是 | 渲染后图像的宽度，单位为Points（一英寸等于72Points），取值范围：大于0。 |
| bitmapHeight | number | 是 | 渲染后图像的高度，单位为Points（一英寸等于72Points），取值范围：大于0。 |
| options | [PixelOptions](pdf-arkts-pdfservice.md#pixeloptions) | 否 | PDF页面转图片参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 合并后PDF页面的image.PixelMap。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-pdf.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1011301001](errorcode-pdf.md#section1011301001-数组大小不匹配) | The arrays of pageIndices and matrices do not match. |
| [1011301002](errorcode-pdf.md#section1011301002-页码值超出范围) | Invalid page number. |
| [1011301003](errorcode-pdf.md#section1011301003-尺寸超出最大值) | The number of pixels in the bitmap exceeds the upper limit. |
| [1011301004](errorcode-pdf.md#section1011301004-创建bitmap失败) | Failed to create a bitmap. |
| [1011301005](errorcode-pdf.md#section1011301005-bitmap渲染失败) | Failed to render the bitmap. |
| [1011301006](errorcode-pdf.md#section1011301006-pdf文档未加载) | The PDF document is not loaded. |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pageIndices: number[] = [0, 1];
  let matrices: pdfService.PdfMatrix[] = [
    new pdfService.PdfMatrix(),
    new pdfService.PdfMatrix()
  ];
  matrices[0].x = 0;
  matrices[0].y = 0;
  matrices[0].width = 200;
  matrices[0].height = 200;
  matrices[0].rotate = 0;
  matrices[1].x = 250;
  matrices[1].y = 250;
  matrices[1].width = 200;
  matrices[1].height = 200;
  matrices[1].rotate = 0;
  let options: pdfService.PixelOptions = new pdfService.PixelOptions();
  options.isGray = false;
  options.drawAnnotations = true;
  options.isTransparent = false;
  let pixelMap: image.PixelMap = pdfDocument.getPixelMapWithPages(pageIndices, matrices, 500, 500, options);
}
```

### searchKey

searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise<void>

对PDF文件执行搜索关键词操作。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 要搜索的关键词（不支持跨PDF页面的字符串） |
| listener | [SearchKeyCallback](pdf-arkts-pdfservice.md#searchkeycallback) | 是 | 每页搜索完毕后执行的回调函数 |
| options | [SearchOptions](pdf-arkts-pdfservice.md#searchoptions) | 否 | 搜索设置项 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 确保在工程目录src/main/resources/resfile里有input.pdf文档
let filePath = this.context.resourceDir + '/input.pdf';
const keyword: string = 'watermelon';
const options: pdfService.SearchOptions = {
  startIndex: 0,
  endIndex: 50,
  isMatchWholeWord: true,
  isMatchCase: true,
  contextStringLength: 80
}
const listener: pdfService.SearchKeyCallback = (results: pdfService.SearchResultData[]): boolean => {
  for (let i = 0; i < results.length; i++) {
    let contextString = results[i].contextString;
    hilog.info(0x0000, 'searchKey',`Get context string: ${contextString}`);
  }
  return false;
};
let doc: pdfService.PdfDocument | undefined = undefined;
doc = new pdfService.PdfDocument();
let loadResult = doc.loadDocument(filePath);
if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
  await doc.searchKey(keyword, listener, options);
}
```

## SearchKeyCallback

type SearchKeyCallback = (results: SearchResultData[]) => boolean

搜索关键词的回调函数，每完成一页内容的搜索回调一次。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| results | [SearchResultData](pdf-arkts-pdfservice.md#searchresultdata)[] | 是 | 搜索的结果 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否终止搜索任务。  - true: 终止搜索任务  - false: 不终止搜索任务 |

## SearchOptions

搜索设置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startIndex | number | 否 | 是 | 搜索关键词的起始页码，必须大于等于0，默认值：0。 |
| endIndex | number | 否 | 是 | 搜索关键词的终止页码，必须大于等于0，endIndex需要大于等于startIndex，默认值：PDF总页数减1。 |
| isMatchWholeWord | boolean | 否 | 是 | 是否匹配全字（仅英文有效）。  true：是  false：否  默认值：false |
| isMatchCase | boolean | 否 | 是 | 是否匹配大小写（仅英文有效）。  true：是  false：否  默认值：false |
| contextStringLength | number | 否 | 是 | 搜索命中项上下文字符串长度（每个中英文字符都算作1个字符），取值范围：0~200，默认值：80。 |

## SearchResultData

搜索关键词的结果数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pageIndex | number | 否 | 否 | 搜索命中项所在的页码值。 |
| rects | [PdfRect](pdf-arkts-pdfservice.md#pdfrect)[] | 否 | 否 | 搜索命中项的矩形信息。 |
| contextString | string | 否 | 否 | 当字符串长度不超过contextStringLength时，按原字符串进行输出；当字符串长度超过contextStringLength时，截取至contextStringLength长度。 |

## Metadata

PDF元数据类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 获取标题。 |
| author | string | 否 | 否 | 获取作者。 |
| subject | string | 否 | 否 | 获取主题。 |
| keywords | string | 否 | 否 | 获取关键字。 |
| creator | string | 否 | 否 | 获取创建者，如果文件是从另一种格式转换到PDF 格式的，创建的原始文件的程序的名字。 |
| producer | string | 否 | 否 | 获取转化者，如果文件是从另一种格式转换到PDF 格式的，转化到PDF 格式的应用程序。 |
| creationDate | Date | 否 | 否 | 获取创建日期。 |
| modifiedDate | Date | 否 | 否 | 获取修改日期。 |

## PdfAnnotation

PDF页面的批注类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AnnotationType](pdf-arkts-pdfservice.md#annotationtype) | 否 | 否 | 批注类型。 |
| uniqueId | string | 否 | 否 | 批注ID。 |

### getPdfPage

getPdfPage(): PdfPage

获取PDF页面。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfPage](pdf-arkts-pdfservice.md#pdfpage) | PDF页面数据。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的批注
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
}
```

### getAnnotationIndex

getAnnotationIndex(): number

获取PDF页面批注的索引。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | PDF页面批注的索引。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的批注
  let annoIndex: number = annot.getAnnotationIndex(); // 返回当前页的批注索引
}
```

### getAnnotationInfo

getAnnotationInfo(): PdfAnnotationInfo

获取PDF页面的当前批注的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo) | PDF页面批注。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的一个批注
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
  let annoIndex: number = annot.getAnnotationIndex(); // 返回当前页的批注索引
  let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
  let annot1: pdfService.PdfAnnotation = annotations[1];
  let annot2: pdfService.PdfAnnotation = annotations[2];
  // 如果页面的第二个批注有页内跳转链接
  let gotoAction = annot1.getAnnotationInfo().action as pdfService.PdfActionGoTo;
  // 如果页面的第三个批注有超链接
  let hyperlinkAction = annot2.getAnnotationInfo().action as pdfService.PdfActionHyperlink;
}
```

### moveTo

moveTo(x: number, y: number): void

增量移动PDF页面批注x，y的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 增量移动PDF页面x的距离，单位为Points（一英寸等于72Points）。 |
| y | number | 是 | 增量移动PDF页面y的距离，单位为Points（一英寸等于72Points）。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的批注
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
  let annoIndex: number = annot.getAnnotationIndex(); // 返回当前批注页的索引
  let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
  annot.moveTo(50, 50); // 当前页批注移动到 x为50， y为50的位置
  let isMarkupAnno: boolean = annot.isMarkup();
}
```

### isMarkup

isMarkup(): boolean

当前批注是否为标记类型批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前批注是否为标记类型批注，true表示是，false表示否。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
  let annot: pdfService.PdfAnnotation = annotations[0]; // 获取 当前页的批注
  let pdfPage: pdfService.PdfPage = annot.getPdfPage();
  let annoIndex: number = annot.getAnnotationIndex(); // 返回当前批注页的索引
  let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
  annot.moveTo(50, 50); // 当前页批注移动到 x为50， y为50的位置
  let isMarkupAnno: boolean =  annot.isMarkup();
}
```

## PdfAnnotationInfo

PDF页面的批注信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AnnotationType](pdf-arkts-pdfservice.md#annotationtype) | 否 | 否 | 批注类型。 |
| uniqueId | string | 否 | 否 | 批注ID。 |
| content | string | 否 | 是 | 批注内容。 |
| modifiedTime | Date | 否 | 是 | 批注修改时间。 |
| border | [PdfBorder](pdf-arkts-pdfservice.md#pdfborder) | 否 | 是 | 线框类型。 |
| flag | [AnnotationFlag](pdf-arkts-pdfservice.md#annotationflag) | 否 | 是 | 批注显示类型。 |
| title | string | 否 | 是 | 批注标题。 |
| opacity | number | 否 | 是 | 透明度，取值 0~1。0表示透明，1表示不透明。 |
| subject | string | 否 | 是 | 注释的主题。 |
| creationDate | Date | 否 | 是 | 注释创建日期，例如：2024-01-01。 |
| action | [PdfAction](pdf-arkts-pdfservice.md#pdfaction) | 否 | 是 | 页面链接跳转，PDF文档内跳转到相应页面和超链接跳转（如：网页地址），目前只支持获取链接，暂不支持添加或编辑链接。  **起始版本：** 5.1.0(18) |

## TextAnnotationInfo

PDF页面的文本批注类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconName | string | 否 | 否 | 文本类型标注的图标名称。 |
| state | [TextAnnotationState](pdf-arkts-pdfservice.md#textannotationstate) | 否 | 否 | 文本批注状态类型枚举。 |
| x | number | 否 | 否 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| y | number | 否 | 否 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| color | number | 否 | 是 | 批注文本颜色，BGR格式，取值范围：0x000000~0xFFFFFF，默认值：0x000000。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## LinkAnnotationInfo

PDF页面的链接类型注释的信息，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| highlightMode | [HighlightMode](pdf-arkts-pdfservice.md#highlightmode) | 否 | 是 | 高亮模式类型，用于设置链接注释被激活时的高亮效果。 |
| color | number | 否 | 是 | 颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## FreeTextAnnotationInfo

PDF页面的自由文本类型注释的信息，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| y | number | 否 | 否 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| width | number | 否 | 是 | 宽，必须大于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| fillColor | number | 否 | 是 | 填充颜色，BGR格式，取值范围：0x000000~0xFFFFFF，默认值：0x000000。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| textStyle | [TextStyle](pdf-arkts-pdfservice.md#textstyle) | 否 | 是 | 文本类型。  说明：传值取值会有差异，有些传入的是布尔值，如果是true，则取值是1，如果是false，取值是0。传入的字体参数，因字体文件名称有多个，返回字体名称会有偏差。 |
| textAlignment | [AlignmentType](pdf-arkts-pdfservice.md#alignmenttype) | 否 | 是 | 对齐类型，默认值：LEFT。 |

## SquareAnnotationInfo

PDF页面的方块类型标注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| lineColor | number | 否 | 是 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| fillColor | number | 否 | 是 | 填充颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## OvalAnnotationInfo

PDF页面的椭圆型标注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| lineColor | number | 否 | 是 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| fillColor | number | 否 | 是 | 填充颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## PolygonAnnotationInfo

PDF页面的多边形批注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vertexes | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 按顺序描述多边形的PdfPoint类型的数组。 |
| lineColor | number | 否 | 是 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| fillColor | number | 否 | 是 | 填充颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## LineAnnotationInfo

PDF页面的线型标注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startX | number | 否 | 否 | 起点的x坐标（到左边缘的距离），单位为Points（一英寸等于72Points）。  说明：传参和取值会有偏差，底层对数据做了处理。 |
| startY | number | 否 | 否 | 起点的y坐标（到下边缘的距离），单位为Points（一英寸等于72Points）。  说明：传参和取值会有偏差，底层对数据做了处理。 |
| endX | number | 否 | 否 | 终点的x坐标（到左边缘的距离），单位为Points（一英寸等于72Points）。  说明：传参和取值会有偏差，底层对数据做了处理。 |
| endY | number | 否 | 否 | 终点的y坐标（到下边缘的距离），单位为Points（一英寸等于72Points）。  说明：传参和取值会有偏差，底层对数据做了处理。 |
| startPointStyle | [LineEndStyle](pdf-arkts-pdfservice.md#lineendstyle) | 否 | 否 | 线条开始端点的线条样式。 |
| endPointStyle | [LineEndStyle](pdf-arkts-pdfservice.md#lineendstyle) | 否 | 否 | 线条结束端点的线条样式。 |
| lineColor | number | 否 | 是 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF。例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## PolylineAnnotationInfo

PDF页面的折线类型标注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vertexes | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 按顺序描述折线的PdfPoint类型的数组。 |
| lineColor | number | 否 | 是 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## HighlightAnnotationInfo

PDF页面的高亮类型标注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quadPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 高亮区域的PdfPoint数组。  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。  说明：传参和取值会有差异，底层对数据做了处理。 |
| color | number | 否 | 是 | 突出显示的BGR颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## UnderlineAnnotationInfo

PDF页面的下划线类型标注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quadPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 下划线区域的PdfPoint数组。  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。  说明：传参和取值会有差异，底层对数据做了处理。 |

## StrikethroughAnnotationInfo

PDF页面的删除线类型批注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quadPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 删除线区域的PdfPoint数组。  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。  说明：传参和取值会有差异，底层对数据做了处理。 |

## InkAnnotationInfo

PDF页面的墨水类型注释信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inkPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | PdfPoint数组按顺序描述墨迹批注  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。 |
| lineColor | number | 否 | 是 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF，默认值：0x000000。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## StampAnnotationInfo

PDF页面的图章类型注释的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string | 否 | 否 | 标记为的图像的文件路径。 |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |

## PdfPoint

PDF页面的点位置类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标，距离页面左边缘的距离，单位为Points（一英寸等于72Points）。 |
| y | number | 否 | 否 | y坐标，距离页面底边缘的距离，单位为Points（一英寸等于72Points）。 |

### constructor

constructor()

用于创建点位置类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfPoint = new pdfService.PdfPoint();
```

## PdfBorder

PDF页面的边框类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| borderStyle | [BorderStyle](pdf-arkts-pdfservice.md#borderstyle) | 否 | 否 | 线框类型。 |
| borderWidth | number | 否 | 否 | 线框宽度，必须大于0，单位为Points（一英寸等于72Points）。 |
| borderColor | number | 否 | 否 | 线框颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

### constructor

constructor()

用于创建边框类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfBorder = new pdfService.PdfBorder();
```

## PdfRect

PDF页面的矩形类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左边距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 上边距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右边距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 下边距，必须大于等于0，单位为Points（一英寸等于72Points）。 |

### constructor

constructor()

用于创建矩形类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfRect = new pdfService.PdfRect();
```

## PdfMatrix

PDF页面的坐标变换矩阵。包含 x, y, width, height,rotate。x, y指定图像左上角相对于页面的偏移；width, height指定图像的宽度和高度，单位为Points；rotate指定旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。用于指定目标页左上角在 PDF 页面中的水平偏移。 |
| y | number | 否 | 否 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。用于指定目标页左上角在 PDF 页面中的垂直偏移。 |
| width | number | 否 | 否 | 宽，必须大于0，单位为Points（一英寸等于72Points）。 |
| height | number | 否 | 否 | 高，必须大于0，单位为Points（一英寸等于72Points）。 |
| rotate | number | 否 | 否 | 旋转角度，1个单位为90度，不能使用Infinity和-Infinity。  取值1，2，3，4，代表90，180，270，360度。 |

### constructor

constructor()

用于创建矩形区域的PDF矩阵类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfMatrix = new pdfService.PdfMatrix();
```

## PdfPage

PDF页面类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### getDocument

getDocument(): PdfDocument

获取PDFDocument对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfDocument](pdf-arkts-pdfservice.md#pdfdocument) | PdfDocument对象。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let document:pdfService.PdfDocument = page.getDocument();
}
```

### getAnnotations

getAnnotations(): Array<PdfAnnotation>

获取文档批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation)> | 文档批注数组。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let page: pdfService.PdfPage = pdfDocument.getPage(0);
  let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
}
```

### addAnnotation

addAnnotation(annotationInfo: PdfAnnotationInfo): PdfAnnotation

在当前页添加批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotationInfo | [PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo) | 是 | 文档批注类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation) | 文档批注。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let aInfo = new pdfService.TextAnnotationInfo();
  aInfo.iconName = "test iconName";
  aInfo.x = 200;
  aInfo.y = 200;
  aInfo.state = pdfService.TextAnnotationState.MARKED;
  aInfo.flag = pdfService.AnnotationFlag.PRINTED;
  let doc = pdfPage.addAnnotation(aInfo);
}
```

### setAnnotation

setAnnotation(annotation: PdfAnnotation, annotationInfo: PdfAnnotationInfo): void

在当前页设置批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotation | [PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation) | 是 | 文档批注。 |
| annotationInfo | [PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo) | 是 | 文档批注类。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let aInfo = new pdfService.TextAnnotationInfo();
  // Text param
  aInfo.iconName = "test iconName";
  aInfo.state = pdfService.TextAnnotationState.UNMARKED;
  aInfo.x = 200;
  aInfo.y = 200;
  aInfo.state = pdfService.TextAnnotationState.MARKED;
  aInfo.flag = pdfService.AnnotationFlag.PRINTED;
  let annotation = pdfPage.addAnnotation(aInfo);
  let bInfo = new pdfService.TextAnnotationInfo();
  bInfo.iconName = "yet another test iconName";
  bInfo.state = pdfService.TextAnnotationState.MARKED;
  bInfo.x = 200;
  bInfo.y = 200;
  bInfo.subject = "this is a subject";
  bInfo.content = "this is a content";
  pdfPage.setAnnotation(annotation, bInfo);
}
```

### removeAnnotation

removeAnnotation(annotation: PdfAnnotation): void

删除当前页批注。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotation | [PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation) | 是 | 文档批注。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let aInfo = new pdfService.TextAnnotationInfo();
  // Text param
  aInfo.iconName = "test iconName";
  aInfo.x = 200;
  aInfo.y = 200;
  aInfo.state = pdfService.TextAnnotationState.MARKED;
  aInfo.flag = pdfService.AnnotationFlag.PRINTED;
  let annotation = pdfPage.addAnnotation(aInfo);
  pdfPage.removeAnnotation(annotation);
}
```

### getIndex

getIndex(): number

获取当前页的索引。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 索引，取值范围大于等于0，小于总页数。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let index = pdfPage.getIndex();
}
```

### getWidth

getWidth(): number

获取当前页的宽。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 宽度值，单位为Points（一英寸等于72Points）。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let width = pdfPage.getWidth();
}
```

### getHeight

getHeight(): number

获取当前页的高。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 高度值，单位为Points（一英寸等于72Points）。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let height = pdfPage.getHeight();
}
```

### setBox

setBox(boxtype: BoxType, rect: PdfRect): void

设置页边界。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| boxtype | [BoxType](pdf-arkts-pdfservice.md#boxtype) | 是 | 页边界。 |
| rect | [PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 是 | 矩形。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfRect = new pdfService.PdfRect();
  pdfRect.left = 100;
  pdfRect.top = 100;
  pdfRect.right = 100;
  pdfRect.bottom = 100;
  pdfPage.setBox(pdfService.BoxType.BOX_MEDIA , pdfRect);
}
```

### getBox

getBox(boxtype: BoxType): PdfRect

获取页边界。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| boxtype | [BoxType](pdf-arkts-pdfservice.md#boxtype) | 是 | 页边界。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 返回页边界矩形。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let box: pdfService.PdfRect = pdfPage.getBox(pdfService.BoxType.BOX_MEDIA);
}
```

### setRotation

setRotation(rotation: RotationAngle): void

设置指定页面的显示旋转角度。旋转角度为顺时针方向的固定值，可选值包括 0、90、180、270 度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | [RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 是 | 旋转角度枚举值。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  pdfPage.setRotation(pdfService.RotationAngle.ANGLE_90);
}
```

### getRotation

getRotation(): RotationAngle

获取页面的旋转角度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 旋转角度。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let rotation = pdfPage.getRotation();
}
```

### getPagePixelMap

getPagePixelMap(): image.PixelMap

获取当前页的图片。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 当前页的image.PixelMap类型。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let img = pdfPage.getPagePixelMap();
}
```

### getCustomPagePixelMap

getCustomPagePixelMap(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap

获取指定PdfPage区间的图片内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [PdfMatrix](pdf-arkts-pdfservice.md#pdfmatrix) | 是 | 坐标变换矩阵，用于在渲染时对页面内容做缩放、平移、旋转等。 |
| isGray | boolean | 是 | 是否只获取黑白色，true：黑白色，false：彩色。 |
| drawAnnotations | boolean | 是 | 是否在图像中绘制注释，true：是，false：否。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 当前页PixelMap。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
  let pixelMap: image.PixelMap = pdfPage.getCustomPagePixelMap(pdfMatrix, true, true);
}
```

### getAreaPixelMap

getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap

将指定 PDF 页面渲染为像素图（PixelMap）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [PdfMatrix](pdf-arkts-pdfservice.md#pdfmatrix) | 是 | 坐标变换矩阵，用于在渲染时对页面内容做 缩放、平移、旋转等。 |
| bitmapwidth | number | 是 | 渲染后图像的宽度，取值范围：大于0。 |
| bitmapHeight | number | 是 | 渲染后图像的高度，取值范围：大于0。 |
| isGray | boolean | 是 | 是否获取灰度图，true：灰度图，false：彩色图。 |
| drawAnnotations | boolean | 是 | 是否渲染页面注释，true：是，false：否。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 当前页PixelMap。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
  let pixelMap: image.PixelMap = pdfPage.getAreaPixelMap(pdfMatrix, 200, 300, true, true);
}
```

### addTextObject

addTextObject(text: string, x: number, y: number, style: TextStyle): void

添加文本内容，只可按行添加。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**说明** 

系统版本请使用5.0.0.126(SP8)及其以上的版本，低于此版本该API不可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |
| x | number | 是 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| y | number | 是 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| style | [TextStyle](pdf-arkts-pdfservice.md#textstyle) | 是 | 文本Style。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let textStyle = new pdfService.TextStyle();
  let fontInfo = new pdfService.FontInfo();
  fontInfo.fontPath = "/system/fonts/HarmonyOS_Sans_SC_Black.ttf"
  textStyle.fontInfo = fontInfo;
  textStyle.textSize = 11;
  textStyle.textColor = 234;
  textStyle.isBold = true;
  textStyle.isItalic = false;
  textStyle.isUnderline = true;
  pdfPage.addTextObject('a', 20, 20, textStyle);
}
```

### addImageObject

addImageObject(path: string, x: number, y: number, width: number, height: number): void

在PDF文档的页面中添加图片。当前仅支持添加像素格式为RGB\_888、RGBA\_8888、BGR\_888、BGRA\_8888、ARGB\_8888、ABGR\_8888、Y8的图片。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |
| x | number | 是 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| y | number | 是 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| width | number | 是 | 宽，必须大于0，单位为Points（一英寸等于72Points）。 |
| height | number | 是 | 高，必须大于0，单位为Points（一英寸等于72Points）。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let context = this.getUIContext().getHostContext() as Context;
  let dir = context.filesDir;
  let imgPath = dir + "/img.jpg";
  pdfPage.addImageObject(imgPath, 0, 0, 200, 200);
  pdfDocument.saveDocument("/data/storage/el2/base/haps/entry/files/testAddImageToDocument.pdf");
}
```

### getGraphicsObjects

getGraphicsObjects(): Array<GraphicsObject>

获取所有图形对象。按位置顺序返回，如从左向右、从上向下。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)> | 所有图形对象数组。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let allImgObj = pdfPage.getGraphicsObjects();
}
```

### deleteGraphicsObject

deleteGraphicsObject(object: GraphicsObject): void

删除指定的[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)类型对象。需要配合getGraphicsObjects使用，且调用之后会实际删除PDF页面中的GraphicsObject对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | [GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject) | 是 | 图形对象。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let graphs: Array<pdfService.GraphicsObject> = pdfPage.getGraphicsObjects();
  if (graphs.length > 0) {
    pdfPage.deleteGraphicsObject(graphs[0]);
  }
}
pdfDocument.releaseDocument();
```

### release

release(): void

释放已加载的PDF页面。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  pdfPage.release();
}
```

### getAreaPixelMapWithOptions

getAreaPixelMapWithOptions(matrix: PdfMatrix,bitmapwidth: number,bitmapHeight: number,options?: PixelOptions): image.PixelMap

获取当前PDF页面pixelMap类型的图片。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [PdfMatrix](pdf-arkts-pdfservice.md#pdfmatrix) | 是 | 坐标变换矩阵，用于在渲染时对页面内容做缩放、平移、旋转等。 |
| bitmapwidth | number | 是 | 图片宽度，单位为Points（一英寸等于72Points），取值范围：大于0。 |
| bitmapHeight | number | 是 | 图片高度，单位为Points（一英寸等于72Points），取值范围：大于0。 |
| options | [PixelOptions](pdf-arkts-pdfservice.md#pixeloptions) | 否 | PDF页面转图片参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 当前页PixelMap。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
  let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
  pdfMatrix.x = 0;
  pdfMatrix.y = 0;
  pdfMatrix.width = pdfPage.getWidth();
  pdfMatrix.height = pdfPage.getHeight();
  pdfMatrix.rotate = 0;
  let options: pdfService.PixelOptions = new pdfService.PixelOptions();
  options.isGray = false;
  options.drawAnnotations = true;
  options.isTransparent = false;
  let pixelMap: image.PixelMap = pdfPage.getAreaPixelMapWithOptions(pdfMatrix, 200, 300, options);
}
```

### getTextContent

getTextContent(): string

获取指定页面文本信息。

**说明** 

该接口用于从文本类型的页面中提取原始文本数据，返回值为包含转义字符（如\r\n等）的String类型字符串。

页面中的图片、水印等元素不支持文本提取，返回空字符串。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 页面文本内容。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

// 将测试文件上传至应用沙箱路径
let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();

// 加载临时文件
let loadResult = pdfDocument.loadDocument(tempFilePath, '');

if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
  let pdfPage = pdfDocument.getPage(0);
  let pageText = pdfPage.getTextContent(); // 获取索引为0页文本数据信息
}
```

## GraphicsObject

图形对象的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [GraphicsObjectType](pdf-arkts-pdfservice.md#graphicsobjecttype) | 否 | 否 | 获取当前图形对象的类型。 |
| x | number | 否 | 否 | 获取当前图形左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| y | number | 否 | 否 | 获取当前图形到底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| clipRect | [PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 否 | 否 | 获取Clip Rect信息。 |
| strokeColor | number | 否 | 否 | 获取笔画颜色(RGB)，取值0x000000 ~ 0xFFFFFF。 |
| strokeOpacity | number | 否 | 否 | 获取笔画透明度，取值 0 ~ 1。0表示完全透明，1表示完全不透明。 |
| fillColor | number | 否 | 否 | 获取填充颜色(RGB)，取值0x000000 ~ 0xFFFFFF。 |
| fillOpacity | number | 否 | 否 | 获取填充透明度，取值0 ~ 1。0表示完全透明，1表示完全不透明。 |
| rotate | number | 否 | 否 | 获取当前图形旋转角度。 |

## TextObject

文本对象的类型，继承[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 获取文本。 |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 否 | 字体信息 |
| textSize | number | 否 | 否 | 字体大小，必须大于0，单位为Points（一英寸等于72Points）。 |
| charspace | number | 否 | 否 | 获取字符间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| wordspace | number | 否 | 否 | 获取单词间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| charRects | Array<[PdfRect](pdf-arkts-pdfservice.md#pdfrect)> | 否 | 否 | 获取字符的区域列表，每个区域用矩形的left、right、top、bottom描述位置。 |
| charUnicodes | Array<number> | 否 | 否 | 获取字符的Unicode。 |

## ImageObject

图片对象的类型，继承[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 使用一种特殊的语法来表示直接在内容流内的小图像数据。 |
| width | number | 否 | 否 | 图像宽度，必须大于0，单位为Points（一英寸等于72Points）。 |
| height | number | 否 | 否 | 图像高度，必须大于0，单位为Points（一英寸等于72Points）。 |

## Bookmark

书签对象的相关方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### isRootBookmark

isRootBookmark(): boolean

是否是根书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否是根书签，true表示是，false表示否。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let isRootBookmark = mark1.isRootBookmark();
}
```

### getParent

getParent(): Bookmark

获取书签父类相关的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 父书签。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let parentBookmark = mark2.getParent();
}
```

### hasChild

hasChild(): boolean

是否有子书签。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否有子书签，true表示是，false表示否。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let hasChildBookmark = mark1.hasChild();
}
```

### getChildren

getChildren(): Array<Bookmark>

获取子书签列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Bookmark](pdf-arkts-pdfservice.md#bookmark)> | 子书签列表。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let childBookmark = mark1.getChildren();
}
```

### getDestInfo

getDestInfo(): DestInfo

获取书签的跳转信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DestInfo](pdf-arkts-pdfservice.md#destinfo) | 书签的跳转信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}
```

### setDestInfo

setDestInfo(info: DestInfo): void

设置书签的跳转信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [DestInfo](pdf-arkts-pdfservice.md#destinfo) | 是 | 书签的跳转信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}
```

### getBookmarkInfo

getBookmarkInfo(): BookmarkInfo

获取书签信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BookmarkInfo](pdf-arkts-pdfservice.md#bookmarkinfo) | 书签信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}
```

### setBookmarkInfo

setBookmarkInfo(info: BookmarkInfo): void

设置书签信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [BookmarkInfo](pdf-arkts-pdfservice.md#bookmarkinfo) | 是 | 书签信息。 |

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
let pdfDocument = new pdfService.PdfDocument();
let loadResult = pdfDocument.loadDocument(tempFilePath, '');
if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
  let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
  let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
  pdfDocument.insertBookmark(mark1, null, 1);
  pdfDocument.insertBookmark(mark2, mark1, 1);
  let destInfo: pdfService.DestInfo = mark1.getDestInfo();
  destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
  destInfo.pageIndex = 1;
  destInfo.left = 20;
  destInfo.top = 30;
  destInfo.zoom = 1.5;
  mark1.setDestInfo(destInfo);
  let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
  bookInfo.title = "hh";
  bookInfo.titleColor = 12;
  bookInfo.isBold = true;
  bookInfo.isItalic = true;
  mark1.setBookmarkInfo(bookInfo);
}
```

## BookmarkInfo

书签类的相关属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 书签的标题文本，用于标识书签指向的PDF内容。 |
| titleColor | number | 否 | 是 | 标题颜色，BGR格式，取值范围：0x000000~0xFFFFFF，默认值：0x000000。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| isBold | boolean | 否 | 是 | 标题是否粗体，true表示是，false表示否  ，默认值：false。 |
| isItalic | boolean | 否 | 是 | 标题是否斜体，true表示是，false表示否，默认值：false。 |

### constructor

constructor()

用于创建书签类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let bookmarkInfo = new pdfService.BookmarkInfo();
```

## HeaderFooterInfo

页眉页脚类的相关属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 否 | 字体的信息。默认值为fontName:""，空字体名（无自定义字体）。 |
| textSize | number | 否 | 否 | 页眉页脚文本大小，必须大于0，单位为Points（一英寸等于72Points）。默认值：0，0Points（无指定）。 |
| charset | [CharsetType](pdf-arkts-pdfservice.md#charsettype) | 否 | 否 | 文本字符集。默认值：0，PDF\_FONT\_ANSI\_CHARSET （ANSI字符集）。 |
| underline | boolean | 否 | 否 | 下划线是否添加，true表示是，false表示否。默认值：false，无下划线。 |
| textColor | number | 否 | 否 | 文字颜色，BGR格式，取值范围：0x000000~0xFFFFFF。默认值：0，表示黑色。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| leftMargin | number | 否 | 否 | 页眉页脚左间距，必须大于等于0，单位为Points（一英寸等于72Points）。默认值：0，表示无左边距。 |
| topMargin | number | 否 | 否 | 页眉页脚顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。默认值：0，表示无顶部边距。 |
| rightMargin | number | 否 | 否 | 页眉页脚右间距，必须大于等于0，单位为Points（一英寸等于72Points）。默认值：0，表示无右边距。 |
| bottomMargin | number | 否 | 否 | 页眉页脚底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。默认值：0，表示无底部边距。 |
| headerLeftText | string | 否 | 否 | 页眉左边文字。默认值：""，表示无文本。 |
| headerCenterText | string | 否 | 否 | 页眉中间文字。默认值：""，表示无文本。 |
| headerRightText | string | 否 | 否 | 页眉右边文字。默认值：""，表示无文本。 |
| footerLeftText | string | 否 | 否 | 页脚左边文字。默认值：""，表示无文本。 |
| footerCenterText | string | 否 | 否 | 页脚中间文字。默认值：""，表示无文本。 |
| footerRightText | string | 否 | 否 | 页脚右边文字。默认值：""，表示无文本。 |

### constructor

constructor()

用于创建页眉页脚类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let headerFooterInfo = new pdfService.HeaderFooterInfo();
```

## WatermarkInfo

水印类的相关属性，自己属于父类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| watermarkType | [WatermarkType](pdf-arkts-pdfservice.md#watermarktype) | 否 | 否 | 水印类型。默认值：0，表示无水印。 |
| isOnTop | boolean | 否 | 否 | 是否置顶，true表示是，false表示否。默认值：false。 |
| scale | number | 否 | 否 | 缩放，必须大于0，小于等于5。默认值：0，表示无缩放。 |
| rotation | number | 否 | 否 | 旋转。默认值：0，表示无旋转。 |
| opacity | number | 否 | 否 | 透明度，取值范围 0~1。默认值：0，表示完全透明。 |
| horizontalAlignment | [WatermarkAlignment](pdf-arkts-pdfservice.md#watermarkalignment) | 否 | 否 | 水平对齐。默认值：0，表示垂直置顶。 |
| horizontalSpace | number | 否 | 否 | 表示水印与页面边缘的水平距离，必须大于等于0，单位为Points（一英寸等于72Points）。默认值：0，表示无水平间距。 |
| verticalAlignment | [WatermarkAlignment](pdf-arkts-pdfservice.md#watermarkalignment) | 否 | 否 | 垂直对齐。默认值：0，表示垂直置顶。 |
| verticalSpace | number | 否 | 否 | 表示水印与页面边缘的垂直距离，必须大于等于0，单位为Points（一英寸等于72Points）。默认值：0，表示无垂直间距。 |

### constructor

constructor()

用于创建水印类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

```typescript
import { pdfService } from '@kit.PDFKit';

let watermarkInfo = new pdfService.WatermarkInfo();
```

## TextWatermarkInfo

文本水印类的相关属性，继承[WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | 否 | 否 | 文本水印内容。 |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 否 | 字体的信息。 |
| textSize | number | 否 | 否 | 文本大小，必须大于0。 |
| textColor | number | 否 | 否 | 文本颜色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |

## ImageWatermarkInfo

图片水印类的相关属性，继承[WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string | 否 | 否 | 图片路径。 |

## BackgroundInfo

背景类的相关属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string | 否 | 否 | 图片路径（图片路径不填则背景色必填）。默认值：""，空字符串（无背景图片）。 |
| backgroundColor | number | 否 | 否 | 背景颜色（背景色不填则图片路径必填）默认值：0，表示无色，BGR格式，取值范围：0x000000~0xFFFFFF。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| isOnTop | boolean | 否 | 否 | 是否置顶，true表示是，false表示否。默认值：false。 |
| scale | number | 否 | 否 | 缩放，必须大于0，小于等于5。默认值：0，表示无缩放。 |
| rotation | number | 否 | 否 | 旋转。默认值：0，表示无旋转（0度）。 |
| opacity | number | 否 | 否 | 透明度，取值范围0~1。默认值：0，表示完全透明。 |
| horizontalAlignment | [BackgroundAlignment](pdf-arkts-pdfservice.md#backgroundalignment) | 否 | 否 | 水平对齐。默认值：0，表示垂直置顶。 |
| horizontalSpace | number | 否 | 否 | 水平间距，必须大于等于0，单位为英寸（一英寸等于72Points）。默认值：0，表示无水平间距。 |
| verticalAlignment | [BackgroundAlignment](pdf-arkts-pdfservice.md#backgroundalignment) | 否 | 否 | 垂直对齐。默认值：0，表示垂直置顶。 |
| verticalSpace | number | 否 | 否 | 垂直间距，必须大于等于0，单位为英寸（一英寸等于72Points）。默认值：0，表示无垂直间距。 |

### constructor

constructor()

用于创建背景类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let backgroundInfo = new pdfService.BackgroundInfo();
```

## PdfAction

批注链接跳转，属于父类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PdfActionType](pdf-arkts-pdfservice.md#pdfactiontype) | 否 | 否 | 批注链接跳转类型。 |

### constructor

constructor()

用于创建批注链接类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let pdfAction = new pdfService.PdfAction();
```

## PdfActionGoTo

页面内的跳转，继承[PdfAction](pdf-arkts-pdfservice.md#pdfaction)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| destInfo | [DestInfo](pdf-arkts-pdfservice.md#destinfo) | 否 | 否 | 跳转信息。 |

## PdfActionHyperlink

超链接跳转，继承[PdfAction](pdf-arkts-pdfservice.md#pdfaction)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hyperlink | string | 否 | 否 | 超链接地址。 |

## PixelOptions

PDF页面转图片相关参数选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isGray | boolean | 否 | 是 | 是否获取仅灰度的图像，true: 是，false: 否。  默认值：true。 |
| drawAnnotations | boolean | 否 | 是 | 是否在图像中注释，true: 是，false: 否。  默认值：true。 |
| isTransparent | boolean | 否 | 是 | 是否获取透明图像，true: 是，false: 否。  默认值：false。 |

### constructor

constructor()

用于创建图片类参数选项的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

```typescript
import { pdfService } from '@kit.PDFKit';

let pixelOptions = new pdfService.PixelOptions();
```

## FontInfo

字体类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontPath | string | 否 | 是 | 字体的路径。 |
| fontName | string | 否 | 是 | 字体的名称。 |

### constructor

constructor()

用于创建字体类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let fontInfo = new pdfService.FontInfo();
```

## DestInfo

书签跳转信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fitMode | [FitMode](pdf-arkts-pdfservice.md#fitmode) | 否 | 否 | 跳转到目标时的页面适合模式。 |
| pageIndex | number | 否 | 否 | 页面索引，大于等于0，小于总页数，0为起始页。 |
| left | number | 否 | 是 | 视图矩形左边界距页面左边的距离，必须大于等于0，单位为Points（一英寸等于72Points），默认值：0。仅在FitMode为FIT\_MODE\_XYZ时生效。 |
| top | number | 否 | 是 | 视图矩形上边界距页面上边的距离，必须大于等于0，单位为Points（一英寸等于72Points），默认值：0。仅在FitMode为FIT\_MODE\_XYZ或FIT\_MODE\_VERTICAL时生效。 |
| right | number | 否 | 是 | 视图矩形右边界距页面右边的距离，必须大于等于0，单位为Points（一英寸等于72Points），默认值：0。仅在FitMode为FIT\_MODE\_RECT时生效。 |
| bottom | number | 否 | 是 | 视图矩形下边界距页面底边的距离，必须大于等于0，单位为Points（一英寸等于72Points），默认值：0。仅在FitMode为FIT\_MODE\_RECT时生效。 |
| zoom | number | 否 | 是 | 缩放比例，1表示100%，必须大于0，小于等于5，默认值：1。仅在FitMode为FIT\_MODE\_XYZ时生效。 |

### constructor

constructor()

用于创建书签跳转类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService } from '@kit.PDFKit';

let destInfo = new pdfService.DestInfo();
```

## TextStyle

文本样式的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 是 | 字体信息，默认字体：HarmonyOS\_Sans。 |
| textSize | number | 否 | 是 | 字体大小，必须大于0，默认值：20。单位为Points（一英寸等于72Points）。 |
| textColor | number | 否 | 是 | 字体颜色，BGR格式，取值范围：0x000000~0xFFFFFF，默认值：0x000000。  例如：0xFF0000代表蓝色，0x0000FF代表红色。 |
| isBold | boolean | 否 | 是 | 是否粗体，true表示是，false表示否，默认值：false。 |
| isItalic | boolean | 否 | 是 | 是否斜体，true表示是，false表示否，默认值：false。 |
| isUnderline | boolean | 否 | 是 | 是否有下划线，true表示是，false表示否，默认值：false。 |
| isStrikethrough | boolean | 否 | 是 | 是否有删除线，true表示是，false表示否，默认值：false。 |

## BorderStyle

线框枚举类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无边框。 |
| SOLID | 1 | 实线边框。 |
| BEVELED | 2 | 斜边边框。 |
| INSET | 3 | 插入边框。 |
| UNDERLINE | 4 | 下划线边框。 |
| DASH | 5 | 虚线边框。 |

## AnnotationFlag

批注标识举类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVISIBLE | 1 | 不可见。 |
| HIDDEN | 2 | 隐藏。 |
| PRINTED | 4 | 注释。 |

## TextAnnotationState

文本批注状态类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNMARKED | 0 | 由用户评论和标记。 |
| MARKED | 1 | 默认情况下，用户不用再标记注释。 |

## HighlightMode

文本高亮模式类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGHLIGHT\_INVERT | 1 | 反转注释区域内的颜色。 |
| HIGHLIGHT\_OUTLINE | 2 | 显示注释的边框轮廓。 |
| HIGHLIGHT\_PUSH | 3 | 将注释外观覆盖在页面内容上。 |
| HIGHLIGHT\_TOGGLE | 4 | 切换显示状态，仅用于表单控件。 |

## AlignmentType

文本对齐方式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 到页面左边缘的距离。 |
| MIDDLE | 1 | 到页面中心线的距离。 |
| RIGHT | 2 | 到页面右边缘的距离。 |

## LineEndStyle

线条端点的线条样式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE\_NONE | 0 | 默认样式。 |
| STYLE\_SQUARE | 1 | 方形样式。 |
| STYLE\_CIRCLE | 2 | 圆形样式。 |
| STYLE\_DIAMOND | 3 | 钻石样式。 |
| STYLE\_OPEN\_ARROW | 4 | 开放箭头样式。 |
| STYLE\_CLOSED\_ARROW | 5 | 闭合箭头样式。 |
| STYLE\_BUTT | 6 | 平角接合样式。 |
| STYLE\_R\_OPEN\_ARROW | 7 | 右开放箭头样式。 |
| STYLE\_R\_CLOSED\_ARROW | 8 | 右闭合箭头样式 |
| STYLE\_SLASH | 9 | 斜线样式 |

## ParseResult

打开文档返回值枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARSE\_SUCCESS | 0 | 成功解析。 |
| PARSE\_ERROR\_FILE | 1 | 文件错误。 |
| PARSE\_ERROR\_FORMAT | 2 | 格式错误。 |
| PARSE\_ERROR\_PASSWORD | 3 | 密码错误。 |
| PARSE\_ERROR\_HANDLER | 4 | 处理程序错误。 |
| PARSE\_ERROR\_CERT | 5 | 证书错误。 |

## PageLayout

页面布局显示方式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYOUT\_SINGLE | 1 | 单页面。 |
| LAYOUT\_DOUBLE | 2 | 双页面。 |

## PageFit

页面适配方式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIT\_NONE | 0 | 实际大小。 |
| FIT\_PAGE | 1 | 按页缩放。 |
| FIT\_WIDTH | 2 | 按宽度。 |
| FIT\_HEIGHT | 3 | 按高度。 |

## RotationAngle

旋转角度枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ANGLE\_0 | 0 | 0度。 |
| ANGLE\_90 | 90 | 90度。 |
| ANGLE\_180 | 180 | 180度。 |
| ANGLE\_270 | 270 | 270度。 |

## ImageFormat

图片类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PNG | 0 | png类型。 |
| BMP | 1 | bmp类型。 |
| JPEG | 2 | jpeg类型。 |

## AnnotationType

批注类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知文本。 |
| TEXT | 1 | 严格文本。 |
| LINK | 2 | 链接。 |
| FREETEXT | 3 | 自由文本。 |
| LINE | 4 | 线。 |
| SQUARE | 5 | 正方形，包括长方形。 |
| OVAL | 6 | 椭圆，包括圆。 |
| POLYGON | 7 | 多边形。 |
| POLYLINE | 8 | 折线。 |
| HIGHLIGHT | 9 | 高亮。 |
| UNDERLINE | 10 | 下划线。 |
| STRIKETHROUGH | 12 | 删除线。 |
| STAMP | 13 | 印章。 |
| INK | 15 | 水墨。 |
| POPUP | 16 | 弹窗。 |

## BoxType

页边界枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOX\_MEDIA | 0 | 定义页面显示或打印的物理介质的边界。 |
| BOX\_CROP | 1 | 定义默认用户空间的可见区域。 |
| BOX\_BLEED | 2 | 印刷出血区域，超出裁切线的部分，防止裁切后出现白边。 |
| BOX\_TRIM | 3 | 修剪后完成页面的预期尺寸。 |
| BOX\_ART | 4 | 页面核心内容区域，排除页眉、页脚等辅助信息。 |

## GraphicsObjectType

图形对象类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OBJECT\_TEXT | 1 | 文本对象。 |
| OBJECT\_PATH | 2 | 路径对象，包含线条和形状。 |
| OBJECT\_IMAGE | 3 | 图像对象。 |
| OBJECT\_SHADING | 4 | 着色对象，包含渐变等填充效果。 |
| OBJECT\_FORM | 5 | 表单对象，可复用的内容组。 |

## CharsetType

字符集对象类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PDF\_FONT\_CID\_FONT\_CHARSET | 0x100000 | CID字符集，用于中日韩等多字节字符。 |
| PDF\_FONT\_ANSI\_CHARSET | 0 | ANSI字符集，西欧字符。 |
| PDF\_FONT\_DEFAULT\_CHARSET | 1 | 默认字符集。 |
| PDF\_FONT\_SYMBOL\_CHARSET | 2 | 符号字符集。 |
| PDF\_FONT\_SHIFT\_JIS\_CHARSET | 128 | Shift JIS字符集，日文。 |
| PDF\_FONT\_HANGUL\_CHARSET | 129 | 韩文字符集。 |
| PDF\_FONT\_GB2312\_CHARSET | 134 | GB2312字符集，简体中文。 |
| PDF\_FONT\_CHINESE\_BIG5\_CHARSET | 136 | 繁体中文BIG5字符集。 |
| PDF\_FONT\_THAI\_CHARSET | 222 | 泰文字符集。 |
| PDF\_FONT\_EAST\_EUROPE\_CHARSET | 238 | 东欧字符集。 |
| PDF\_FONT\_RUSSIAN\_CHARSET | 204 | 俄文字符集，西里尔字母。 |
| PDF\_FONT\_GREEK\_CHARSET | 161 | 希腊字符集。 |
| PDF\_FONT\_TURKISH\_CHARSET | 162 | 土耳其字符集。 |
| PDF\_FONT\_VIETNAMESE\_CHARSET | 163 | 越南文字符集。 |
| PDF\_FONT\_HEBREW\_CHARSET | 177 | 希伯来文字符集。 |
| PDF\_FONT\_ARABIC\_CHARSET | 178 | 阿拉伯文字符集。 |
| PDF\_FONT\_BALTIC\_CHARSET | 186 | 波罗的海字符集。 |

## FitMode

页面适合模式枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIT\_MODE\_XYZ | 1 | 按页面左上角的点缩放页面，页面内容按缩放比例放大。 |
| FIT\_MODE\_HORIZONTAL | 2 | 使页面适应窗口内的整个页面宽度。 |
| FIT\_MODE\_VERTICAL | 3 | 使页面适应窗口内的整个页面高度。 |
| FIT\_MODE\_RECT | 4 | 使页面适合窗口内的页面矩形。 |

## WatermarkType

页面水印类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WATERMARK\_TEXT | 1 | 文本水印。 |
| WATERMARK\_IMAGE | 2 | 图片水印。 |

## WatermarkAlignment

文档水印位置类型枚举

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WATERMARK\_ALIGNMENT\_TOP | 0 | 垂直置顶。 |
| WATERMARK\_ALIGNMENT\_VCENTER | 1 | 垂直居中。 |
| WATERMARK\_ALIGNMENT\_BOTTOM | 2 | 垂直置底。 |
| WATERMARK\_ALIGNMENT\_LEFT | 3 | 水平居左。 |
| WATERMARK\_ALIGNMENT\_HCENTER | 4 | 水平居中。 |
| WATERMARK\_ALIGNMENT\_RIGHT | 5 | 水平居右。 |

## BackgroundAlignment

文档背景位置类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND\_ALIGNMENT\_TOP | 0 | 垂直置顶。 |
| BACKGROUND\_ALIGNMENT\_VCENTER | 1 | 垂直居中。 |
| BACKGROUND\_ALIGNMENT\_BOTTOM | 2 | 垂直置底。 |
| BACKGROUND\_ALIGNMENT\_LEFT | 3 | 水平居左。 |
| BACKGROUND\_ALIGNMENT\_HCENTER | 4 | 水平居中。 |
| BACKGROUND\_ALIGNMENT\_RIGHT | 5 | 水平居右。 |

## PdfActionType

链接跳转类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知类型 |
| GOTO | 1 | 文档内链接类型 |
| HYPERLINK | 2 | 超链接类型 |
