---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice
title: pdfService（PDF服务）
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS API > pdfService（PDF服务）
category: harmonyos-references
scraped_at: 2026-04-29T14:09:00+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3f7027185665ae63252e6bc0b5d326752e2b7c3aab4ae87fa9661b15a52d3176
---

本模块为应用提供统一的管理PDF页面的页眉页脚、水印和背景、文档的多种批注风格和书签便捷的PDF能力。

**注：** 涉及到尺寸和坐标的属性都是以点（Points）为单位，一英寸等于72点。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { pdfService } from '@kit.PDFKit';
```

## 注意事项

PhonePC/2in1Tablet

对PDF文件进行编辑操作后，需要调用[saveDocument](pdf-arkts-pdfservice.md#savedocument)接口将PDF文件保存，确保编辑操作生效。

## PdfDocument

PhonePC/2in1Tablet

PDF文件类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### constructor

PhonePC/2in1Tablet

constructor()

构造函数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfDocument = new pdfService.PdfDocument();
```

### loadDocument

PhonePC/2in1Tablet

loadDocument(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult

加载指定文件路径。由于loadDocument不支持重复调用，因此在二次调用之前，必须先通过releaseDocument释放当前已加载的文档，以确保资源正确释放并避免潜在的冲突或异常。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
```

### releaseDocument

PhonePC/2in1Tablet

releaseDocument(): void

释放PDF文档。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfDocument = new pdfService.PdfDocument();
4. // 将测试文件上传至应用沙箱路径
5. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfDocument.releaseDocument();
10. }
```

### saveDocument

PhonePC/2in1Tablet

saveDocument(path: string, onProgress?: (progress: number) => number): boolean

保存文档。

说明

由于文档不可同时读写，如果需要覆盖回原文档，请创建临时文档作为过渡。具体请参见下方示例代码。

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

```
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. import { pdfService } from '@kit.PDFKit';
3. import { Font } from '@kit.ArkUI';

5. // 将测试文件上传至应用沙箱路径
6. let context = this.getUIContext().getHostContext() as Context;
7. let dir = context.filesDir;
8. let tempDir = context.tempDir;
9. // 确保该路径下的源文档有读写的权限
10. let filePath = dir + `/input.pdf`;
11. let tempFilePath = tempDir + `/temp${Math.random()}.pdf`;
12. fs.copyFileSync(filePath, tempFilePath);
13. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
14. // 加载临时文件
15. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
16. // 对文档加一些水印
17. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
18. let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
19. wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
20. wminfo.content = "This is Watermark";
21. wminfo.textSize = 30;
22. wminfo.textColor = 200;
23. wminfo.fontInfo = new pdfService.FontInfo();
24. let font: Font = new Font()
25. wminfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans").path;
26. wminfo.opacity = 0.5;
27. wminfo.isOnTop = true;
28. wminfo.rotation = 45;
29. wminfo.scale = 1.5;
30. wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
31. wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
32. wminfo.horizontalSpace = 1.0;
33. wminfo.verticalSpace = 1.0;
34. pdfDocument.addWatermark(wminfo, 0, 1, true, true);
35. // 保存文件将覆盖源文档
36. let result = pdfDocument.saveDocument(filePath);
37. }
```

### createDocument

PhonePC/2in1Tablet

createDocument(width: number, height: number): boolean

创建空白文档。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfDocument = new pdfService.PdfDocument();
4. pdfDocument.createDocument(600, 900);
```

### isEncrypted

PhonePC/2in1Tablet

isEncrypted(path: string): boolean

文档是否加密。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
7. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let isEncrypted = pdfDocument.isEncrypted(tempFilePath);
9. }
```

### removeSecurity

PhonePC/2in1Tablet

removeSecurity(): boolean

删除文档加密锁。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功删除文档加密锁，true表示成功，false表示失败。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
7. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let result = pdfDocument.removeSecurity();
9. }
```

### getPageCount

PhonePC/2in1Tablet

getPageCount(): number

获取文档页数。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文档总页数，取值范围大于0。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
7. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let pageCount = pdfDocument.getPageCount();
9. }
```

### getPage

PhonePC/2in1Tablet

getPage(index: number): PdfPage

获取指定页的对象。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pdfPage = pdfDocument.getPage(0);
10. }
```

### insertBlankPage

PhonePC/2in1Tablet

insertBlankPage(index: number, width: number, height: number): PdfPage

在指定位置插入PDF页。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let pdfPage = pdfDocument.insertBlankPage(1, 600, 900);
10. }
```

### insertPageFromDocument

PhonePC/2in1Tablet

insertPageFromDocument(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage

将其他Document的Page添加到当前Document，Page中的批注不支持插入到当前Document。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| document | [PdfDocument](pdf-arkts-pdfservice.md#pdfdocument) | 是 | PdfDocument对象。 |
| fromIndex | number | 是 | 从其他文档第几页开始添加，大于等于0，0为起始页。 |
| pageCount | number | 是 | 添加页数量，大于0，小于等于总页数。 |
| index | number | 是 | 从当前文档第几页开始添加，大于等于0，小于总页数，0为起始页。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfPage](pdf-arkts-pdfservice.md#pdfpage) | 插入的PDF最后一页。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath1 = '/data/storage/el2/base/temp/test1.pdf';
5. let document: pdfService.PdfDocument = new pdfService.PdfDocument();
6. let loadResult1 = document.loadDocument(tempFilePath1, '');
7. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult1) {
8. // 将测试文件上传至应用沙箱路径
9. let tempFilePath2 = '/data/storage/el2/base/temp/test2.pdf';
10. let pdfDocument2 = new pdfService.PdfDocument();
11. // 加载临时文件
12. let loadResult2 = pdfDocument2.loadDocument(tempFilePath2, '');
13. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult2) {
14. let page = pdfDocument2.insertPageFromDocument(document, 1, 2, 3);
15. }
16. }
```

### deletePage

PhonePC/2in1Tablet

deletePage(index: number, count: number): void

删除指定位置PDF页。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| index | number | 是 | 从当前文档第几页开始，索引大于等于0，小于总页数，0为起始页。 |
| count | number | 是 | 删除几个PDF页面，大于0，小于等于总页数。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfDocument.deletePage(1, 2);
10. }
```

### movePage

PhonePC/2in1Tablet

movePage(index: number, dest: number): boolean

将指定页面移到索引位置。

说明

movePage(2, 3)，不会有变化，2是第3页，3是第4页，第3页只能移动到第4页后面，就是第5页，应该是movePage(2, 4)，顺序：0，1，3，2，4。

movePage(3, 2)，会有变化，顺序：0，1，3，2，4。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/CLkVZ3-CTvi1gbdH1XmN2w/zh-cn_image_0000002558767434.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T060858Z&HW-CC-Expire=86400&HW-CC-Sign=C14683E9BDBEF716E80B4963436C23EBB733AB93FD6833956651CF5043B0A824)

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfDocument.movePage(2, 4);
10. }
```

### getFontWeight

PhonePC/2in1Tablet

getFontWeight(): number

获取字体粗细。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 字体粗细，必须大于0，单位为Points（一英寸等于72Points）。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let weight = pdfDocument.getFontWeight();
10. }
```

### setFontWeight

PhonePC/2in1Tablet

setFontWeight(weight: number): void

设置字体粗细。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| weight | number | 是 | 字体粗细，必须大于0，单位为Points（一英寸等于72Points）。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let weight = pdfDocument.setFontWeight(10);
10. }
```

### getMetadata

PhonePC/2in1Tablet

getMetadata(): Metadata

获取PDF元数据，包括作者、创建者、创建日期等。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Metadata](pdf-arkts-pdfservice.md#metadata) | PDF元数据 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. pdfDocument.getMetadata();
10. }
```

### convertToImage

PhonePC/2in1Tablet

convertToImage(path: string, format: ImageFormat, onProgress?: (progress: number) => number): boolean

转换PDF文档为图片。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. // 将测试文件上传至应用沙箱路径
5. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
6. let pdfDocument = new pdfService.PdfDocument();
7. // 加载临时文件
8. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
9. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
10. let context = this.getUIContext().getHostContext() as Context;
11. let dir = context.filesDir + '/output/';
12. await fileIo.mkdir(dir);
13. let result = pdfDocument.convertToImage(dir, pdfService.ImageFormat.PNG);
14. }
```

### getRootBookmark

PhonePC/2in1Tablet

getRootBookmark(): Bookmark

获取PDF文档第一个根书签。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 第一个根书签。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let rootBookmark = pdfDocument.getRootBookmark();
10. }
```

### getRootBookmarks

PhonePC/2in1Tablet

getRootBookmarks(): Array<Bookmark>

PDF文档获取根书签。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Bookmark](pdf-arkts-pdfservice.md#bookmark)> | 根书签。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let rootBookmark = pdfDocument.getRootBookmarks();
10. }
```

### createBookmark

PhonePC/2in1Tablet

createBookmark(): Bookmark

创建PDF文档书签。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 成功创建的书签，并返回Bookmark信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let rootBookmark: pdfService.Bookmark = pdfDocument.createBookmark();
10. }
```

### removeBookmark

PhonePC/2in1Tablet

removeBookmark(bookmark: Bookmark): boolean

移除PDF文档书签。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let bookmarks: Array<pdfService.Bookmark> = pdfDocument.getRootBookmarks();
10. if (bookmarks.length && bookmarks[0].isRootBookmark()) {
11. let isRemoved: boolean = pdfDocument.removeBookmark(bookmarks[0]);
12. }
13. }
```

### insertBookmark

PhonePC/2in1Tablet

insertBookmark(bookmark: Bookmark, parent: Bookmark, position: number): boolean

插入PDF文档书签。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. // 加载临时文件
7. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
8. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
9. let parentBookmark: pdfService.Bookmark = pdfDocument.createBookmark();
10. let bookmark: pdfService.Bookmark = pdfDocument.createBookmark();
11. pdfDocument.insertBookmark(bookmark, null, 1);
12. pdfDocument.insertBookmark(bookmark, parentBookmark, 1);
13. let bool1: boolean = parentBookmark.isRootBookmark();
14. let bool2: boolean = bookmark.isRootBookmark();
15. }
```

### addHeaderFooter

PhonePC/2in1Tablet

addHeaderFooter(info: HeaderFooterInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

插入PDF文档页眉页脚。该方法属于耗时业务，需要遍历每一页去添加页眉页脚，添加页面较多时建议放到线程中去处理。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { Font } from '@kit.ArkUI';

4. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
5. let document: pdfService.PdfDocument = new pdfService.PdfDocument();
6. let loadResult = document.loadDocument(filePath);
7. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let hfInfo: pdfService.HeaderFooterInfo = new pdfService.HeaderFooterInfo();
9. hfInfo.fontInfo = new pdfService.FontInfo();
10. let font: Font = new Font()
11. hfInfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans")?.path; // 确保字体存在
12. hfInfo.fontInfo.fontName = '';
13. hfInfo.textSize = 10;
14. hfInfo.charset = pdfService.CharsetType.PDF_FONT_DEFAULT_CHARSET;
15. hfInfo.underline = false;
16. hfInfo.textColor = 0x00000000;
17. hfInfo.leftMargin = 1.0;
18. hfInfo.topMargin = 40.0;
19. hfInfo.rightMargin = 1.0;
20. hfInfo.bottomMargin = 40.0;
21. hfInfo.headerLeftText = "left H <<dd.mm.yyyy>><<1/n>>";
22. hfInfo.headerCenterText = "center H <<m/d/yyyy>><<1>>";
23. hfInfo.headerRightText = "right H <<m/d>><<1/n>>";
24. hfInfo.footerLeftText = "left F <<m/d>><<1>>";
25. hfInfo.footerCenterText = "center F <<m/d>><<1>>";
26. hfInfo.footerRightText = "right F <<dd.mm.yyyy>><<1>>";
27. document.addHeaderFooter(hfInfo, 1, 5, true, true);
28. }
```

### getHeaderFooter

PhonePC/2in1Tablet

getHeaderFooter(): HeaderFooterInfo

获取PDF文档页眉页脚。没有页眉页脚的PDF文档获取的HeaderFooterInfo的属性是默认值。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HeaderFooterInfo](pdf-arkts-pdfservice.md#headerfooterinfo) | 获取到的页眉页脚信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let headerFooterInfo = pdfDocument.getHeaderFooter();
8. }
```

### hasHeaderFooter

PhonePC/2in1Tablet

hasHeaderFooter(): boolean

PDF文档是否有页眉页脚。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PDF文档是否有页眉页脚，true表示有，false表示没有。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let hasHeaderFooter: boolean = pdfDocument.hasHeaderFooter();
8. }
```

### removeHeaderFooter

PhonePC/2in1Tablet

removeHeaderFooter(): boolean

删除PDF文档页眉页脚。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除PDF文档页眉页脚，true表示成功，false表示失败。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. if (pdfDocument.hasHeaderFooter()) {
8. let delHeaderFooter: boolean = pdfDocument.removeHeaderFooter();
9. }
10. }
```

### addWatermark

PhonePC/2in1Tablet

addWatermark(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

插入PDF文档水印。该方法属于耗时业务，需要遍历每一页去添加水印，添加页面较多时建议放到线程中去处理。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { Font } from '@kit.ArkUI';

4. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
5. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(filePath);
7. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
9. wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
10. wminfo.content = "This is watermark";
11. wminfo.textSize = 30;
12. wminfo.textColor = 200;
13. wminfo.fontInfo = new pdfService.FontInfo();
14. let font: Font = new Font()
15. wminfo.fontInfo.fontPath = font.getFontByName("HarmonyOS Sans").path;
16. wminfo.opacity = 0.5;
17. wminfo.isOnTop = true;
18. wminfo.rotation = 45;
19. wminfo.scale = 1.5;
20. wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
21. wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
22. wminfo.horizontalSpace = 1.0;
23. wminfo.verticalSpace = 1.0;
24. pdfDocument.addWatermark(wminfo, 1, 18, true, true);
25. }
```

* 添加图片水印

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
8. wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_IMAGE;
9. wminfo.imagePath = "/data/storage/el2/base/haps/View/files/img.jpg";
10. wminfo.opacity = 0.5;
11. wminfo.isOnTop = true;
12. wminfo.rotation = 45;
13. wminfo.scale = 1.5;
14. wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
15. wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
16. wminfo.horizontalSpace = 1.0;
17. wminfo.verticalSpace = 1.0;
18. pdfDocument.addWatermark(wminfo, 1, 18, true, true);
19. }
```

### getWatermark

PhonePC/2in1Tablet

getWatermark(): WatermarkInfo

获取PDF文档水印。没有水印的PDF文档获取的WatermarkInfo的属性是默认值。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo) | 获取PDF文档水印信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let watermarkInfo: pdfService.WatermarkInfo = pdfDocument.getWatermark();
8. }
```

### hasWatermark

PhonePC/2in1Tablet

hasWatermark(): boolean

PDF文档是否有水印。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PDF文档是否有水印，true表示有，false表示没有。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let hasWatermark: boolean = pdfDocument.hasWatermark();
8. }
```

### removeWatermark

PhonePC/2in1Tablet

removeWatermark(): boolean

删除PDF文档水印。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否删除PDF文档水印成功，true表示成功，false表示失败。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/input.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let hasWatermark: boolean = pdfDocument.hasWatermark();
8. if (hasWatermark) {
9. let hasRemoveWatermark = pdfDocument.removeWatermark();
10. }
11. }
```

### addBackground

PhonePC/2in1Tablet

addBackground(info: BackgroundInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void

插入PDF文档背景。该方法属于耗时业务，需要遍历每一页去添加背景，添加页面较多时建议放到线程中去处理。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let bginfo: pdfService.BackgroundInfo = new pdfService.BackgroundInfo();
8. bginfo.imagePath = "/data/storage/el2/base/haps/View/files/img.jpg";
9. bginfo.backgroundColor = 50;
10. bginfo.isOnTop = true;
11. bginfo.rotation = 90;
12. bginfo.scale = 0.5;
13. bginfo.opacity = 0.3;
14. bginfo.verticalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_TOP;
15. bginfo.horizontalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_LEFT;
16. bginfo.horizontalSpace = 1.0;
17. bginfo.verticalSpace = 1.0;
18. pdfDocument.addBackground(bginfo, 2, 18, true, true);
19. }
```

### getBackground

PhonePC/2in1Tablet

getBackground(): BackgroundInfo

获取PDF文档背景信息 。没有背景的PDF文档获取的BackgroundInfo的属性是默认值。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BackgroundInfo](pdf-arkts-pdfservice.md#backgroundinfo) | 获取PDF文档背景信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. if (pdfDocument.hasBackground()) {
8. let backgroundInfo: pdfService.BackgroundInfo = pdfDocument.getBackground();
9. }
10. }
```

### hasBackground

PhonePC/2in1Tablet

hasBackground(): boolean

PDF文档是否有背景。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | PDF文档是否有背景，true表示有，false表示没有。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let hasBackground: boolean = pdfDocument.hasBackground();
8. }
```

### removeBackground

PhonePC/2in1Tablet

removeBackground(): boolean

删除PDF文档背景。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功删除背景，true表示成功，false表示失败。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. if (pdfDocument.hasBackground()) {
8. let delBackground: boolean = pdfDocument.removeBackground();
9. }
10. }
```

### setPdfPassword

PhonePC/2in1Tablet

setPdfPassword(password: string): boolean

采用AES-256加密算法,对PDF文件进行加密。

说明

加密后的文件仅在支持AES-256的PDF阅读软件中正常打开。若使用不支持AES-256的软件打开，可能会因兼容性问题导致打开失败，并提示“密码错误”。请尝试使用支持AES-256的软件打开该文件。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. let filePath = String.raw`/data/storage/el2/base/haps/View/files/output.pdf`;
4. let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(filePath);
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let setPassword: boolean = pdfDocument.setPdfPassword('123456');
8. }
```

### searchKey

PhonePC/2in1Tablet

searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise<void>

对PDF文件执行搜索关键词操作。使用Promise异步回调。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 确保在工程目录src/main/resources/resfile里有input.pdf文档
5. let filePath = this.context.resourceDir + '/input.pdf';
6. const keyword: string = 'watermelon';
7. const options: pdfService.SearchOptions = {
8. startIndex: 0,
9. endIndex: 50,
10. isMatchWholeWord: true,
11. isMatchCase: true,
12. contextStringLength: 80
13. }
14. const listener: pdfService.SearchKeyCallback = (results: pdfService.SearchResultData[]): boolean => {
15. for (let i = 0; i < results.length; i++) {
16. let contextString = results[i].contextString;
17. hilog.info(0x0000, 'searchKey',`Get context string: ${contextString}`);
18. }
19. return false;
20. };
21. let doc: pdfService.PdfDocument | undefined = undefined;
22. doc = new pdfService.PdfDocument();
23. let loadResult = doc.loadDocument(filePath);
24. if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
25. await doc.searchKey(keyword, listener, options);
26. }
```

## SearchKeyCallback

PhonePC/2in1Tablet

type SearchKeyCallback = (results: SearchResultData[]) => boolean

搜索关键词的回调函数，每完成一页内容的搜索回调一次。

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

PhonePC/2in1Tablet

搜索设置项。

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

PhonePC/2in1Tablet

搜索关键词的结果数据。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pageIndex | number | 否 | 否 | 搜索命中项所在的页码值。 |
| rects | [PdfRect](pdf-arkts-pdfservice.md#pdfrect)[] | 否 | 否 | 搜索命中项的矩形信息。 |
| contextString | string | 否 | 否 | 当字符串长度不超过contextStringLength时，按原字符串进行输出；当字符串长度超过contextString时，截取至contextStringLength长度。 |

## Metadata

PhonePC/2in1Tablet

PDF元数据类型。

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

PhonePC/2in1Tablet

PDF页面的批注类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AnnotationType](pdf-arkts-pdfservice.md#annotationtype) | 否 | 否 | 批注类型。 |
| uniqueId | string | 否 | 否 | 批注ID。 |

### getPdfPage

PhonePC/2in1Tablet

getPdfPage(): PdfPage

获取PDF页面。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfPage](pdf-arkts-pdfservice.md#pdfpage) | PDF页面数据。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
9. let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的批注
10. let pdfPage: pdfService.PdfPage = annot.getPdfPage();
11. }
```

### getAnnotationIndex

PhonePC/2in1Tablet

getAnnotationIndex(): number

获取PDF页面批注的索引。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | PDF页面批注的索引。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
9. let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的批注
10. let annoIndex: number = annot.getAnnotationIndex(); // 返回当前页的批注索引
11. }
```

### getAnnotationInfo

PhonePC/2in1Tablet

getAnnotationInfo(): PdfAnnotationInfo

获取PDF页面的当前批注的信息。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo) | PDF页面批注。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
9. let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的一个批注
10. let pdfPage: pdfService.PdfPage = annot.getPdfPage();
11. let annoIndex: number = annot.getAnnotationIndex(); // 返回当前页的批注索引
12. let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
13. let annot1: pdfService.PdfAnnotation = annotations[1];
14. let annot2: pdfService.PdfAnnotation = annotations[2];
15. // 如果页面的第二个批注有页内跳转链接
16. let gotoAction = annot1.getAnnotationInfo().action as pdfService.PdfActionGoTo;
17. // 如果页面的第三个批注有超链接
18. let hyperlinkAction = annot2.getAnnotationInfo().action as pdfService.PdfActionHyperlink;
19. }
```

### moveTo

PhonePC/2in1Tablet

moveTo(x: number, y: number): void

增量移动PDF页面批注x，y的距离。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 增量移动PDF页面x的距离，单位为Points（一英寸等于72Points）。 |
| y | number | 是 | 增量移动PDF页面y的距离，单位为Points（一英寸等于72Points）。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
9. let annot: pdfService.PdfAnnotation = annotations[0]; // 获取当前页的批注
10. let pdfPage: pdfService.PdfPage = annot.getPdfPage();
11. let annoIndex: number = annot.getAnnotationIndex(); // 返回当前批注页的索引
12. let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
13. annot.moveTo(50, 50); // 当前页批注移动到 x为50， y为50的位置
14. let isMarkupAnno: boolean = annot.isMarkup();
15. }
```

### isMarkup

PhonePC/2in1Tablet

isMarkup(): boolean

当前批注是否为标记类型批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前批注是否为标记类型批注，true表示是，false表示否。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
9. let annot: pdfService.PdfAnnotation = annotations[0]; // 获取 当前页的批注
10. let pdfPage: pdfService.PdfPage = annot.getPdfPage();
11. let annoIndex: number = annot.getAnnotationIndex(); // 返回当前批注页的索引
12. let annotat: pdfService.TextAnnotationInfo = annot.getAnnotationInfo() as pdfService.TextAnnotationInfo;
13. annot.moveTo(50, 50); // 当前页批注移动到 x为50， y为50的位置
14. let isMarkupAnno: boolean =  annot.isMarkup();
15. }
```

## PdfAnnotationInfo

PhonePC/2in1Tablet

PDF页面的批注信息。

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

PhonePC/2in1Tablet

PDF页面的文本批注类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconName | string | 否 | 否 | 文本类型标注的图标名称。 |
| state | [TextAnnotationState](pdf-arkts-pdfservice.md#textannotationstate) | 否 | 否 | 文本批注状态类型枚举。 |
| x | number | 否 | 否 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| y | number | 否 | 否 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| color | number | 否 | 是 | 批注文本颜色，取值范围0x000000 ~ 0xFFFFFF，默认值：0x000000。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## LinkAnnotationInfo

PhonePC/2in1Tablet

PDF页面的链接类型注释的信息，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| highlightMode | [HighlightMode](pdf-arkts-pdfservice.md#highlightmode) | 否 | 是 | 高亮模式类型，用于设置链接注释被激活时的高亮效果。 |
| color | number | 否 | 是 | 颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## FreeTextAnnotationInfo

PhonePC/2in1Tablet

PDF页面的自由文本类型注释的信息，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| y | number | 否 | 否 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| width | number | 否 | 是 | 宽，必须大于0，单位为Points（一英寸等于72Points）。  说明：底层做了处理，传值和取值会有偏差。 |
| fillColor | number | 否 | 是 | 填充颜色，取值范围 0x000000 ~ 0xFFFFFF，默认值：0x000000。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| textStyle | [TextStyle](pdf-arkts-pdfservice.md#textstyle) | 否 | 是 | 文本类型。  说明：传值取值会有差异，有些传入的是布尔值，如果是true，则取值是1，如果是false，取值是0。传入的字体参数，因字体文件名称有多个，返回字体名称会有偏差。 |
| textAlignment | [AlignmentType](pdf-arkts-pdfservice.md#alignmenttype) | 否 | 是 | 对齐类型，默认值：LEFT。 |

## SquareAnnotationInfo

PhonePC/2in1Tablet

PDF页面的方块类型标注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| lineColor | number | 否 | 是 | 线框颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| fillColor | number | 否 | 是 | 填充颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## OvalAnnotationInfo

PhonePC/2in1Tablet

PDF页面的椭圆型标注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottom | number | 否 | 否 | 底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| right | number | 否 | 否 | 右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| top | number | 否 | 否 | 顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| lineColor | number | 否 | 是 | 线框颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| fillColor | number | 否 | 是 | 填充颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## PolygonAnnotationInfo

PhonePC/2in1Tablet

PDF页面的多边形批注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vertexes | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 按顺序描述多边形的PdfPoint类型的数组。 |
| lineColor | number | 否 | 是 | 线框颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| fillColor | number | 否 | 是 | 填充颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## LineAnnotationInfo

PhonePC/2in1Tablet

PDF页面的线型标注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

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
| lineColor | number | 否 | 是 | 线框颜色，取值范围0x000000 ~ 0xFFFFFF。（例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## PolylineAnnotationInfo

PhonePC/2in1Tablet

PDF页面的折线类型标注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vertexes | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 按顺序描述折线的PdfPoint类型的数组。 |
| lineColor | number | 否 | 是 | 线框颜色，取值范围0x000000~0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## HighlightAnnotationInfo

PhonePC/2in1Tablet

PDF页面的高亮类型标注信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quadPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 高亮区域的PdfPoint数组。  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。  说明：传参和取值会有差异，底层对数据做了处理。 |
| color | number | 否 | 是 | 突出显示的RGB颜色，取值范围0x000000~0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## UnderlineAnnotationInfo

PhonePC/2in1Tablet

PDF页面的下划线类型标注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quadPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 下划线区域的PdfPoint数组。  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。  说明：传参和取值会有差异，底层对数据做了处理。 |

## StrikethroughAnnotationInfo

PhonePC/2in1Tablet

PDF页面的删除线类型批注的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quadPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | 删除线区域的PdfPoint数组。  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。  说明：传参和取值会有差异，底层对数据做了处理。 |

## InkAnnotationInfo

PhonePC/2in1Tablet

PDF页面的墨水类型注释信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inkPoints | Array<[PdfPoint](pdf-arkts-pdfservice.md#pdfpoint)> | 否 | 否 | PdfPoint数组按顺序描述墨迹批注  每个链接标注有4\*n个点，每组4个点分别是：  第1个点：矩形左上角的点。  第2个点：矩形的右上点。  第3个点：矩形左下角的点。  第4个点：矩形的右下角点。 |
| lineColor | number | 否 | 是 | 线框颜色，取值范围0x000000~0xFFFFFF，默认值：0x000000。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## StampAnnotationInfo

PhonePC/2in1Tablet

PDF页面的图章类型注释的信息类，继承[PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo)。

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

PhonePC/2in1Tablet

PDF页面的点位置类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x坐标，距离页面左边缘的距离，单位为Points（一英寸等于72Points）。 |
| y | number | 否 | 否 | y坐标，距离页面底边缘的距离，单位为Points（一英寸等于72Points）。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建点位置类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfPoint = new pdfService.PdfPoint();
```

## PdfBorder

PhonePC/2in1Tablet

PDF页面的边框类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| borderStyle | [BorderStyle](pdf-arkts-pdfservice.md#borderstyle) | 否 | 否 | 线框类型。 |
| borderWidth | number | 否 | 否 | 线框宽度，必须大于0，单位为Points（一英寸等于72Points）。 |
| borderColor | number | 否 | 否 | 线框颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建边框类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfBorder = new pdfService.PdfBorder();
```

## PdfRect

PhonePC/2in1Tablet

PDF页面的矩形类。

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

PhonePC/2in1Tablet

constructor()

用于创建矩形类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfRect = new pdfService.PdfRect();
```

## PdfMatrix

PhonePC/2in1Tablet

PDF页面的坐标变换矩阵。包含 x, y, width, height,rotate。x, y指定图像左上角相对于页面的偏移；width, height指定图像的宽度和高度，单位为Points；rotate指定旋转角度。

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

PhonePC/2in1Tablet

constructor()

用于创建矩形区域的PDF矩阵类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfMatrix = new pdfService.PdfMatrix();
```

## PdfPage

PhonePC/2in1Tablet

PDF页面类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### getDocument

PhonePC/2in1Tablet

getDocument(): PdfDocument

获取PDFDocument对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PdfDocument](pdf-arkts-pdfservice.md#pdfdocument) | PdfDocument对象。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let document:pdfService.PdfDocument = page.getDocument();
9. }
```

### getAnnotations

PhonePC/2in1Tablet

getAnnotations(): Array<PdfAnnotation>

获取文档批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation)> | 文档批注数组。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let page: pdfService.PdfPage = pdfDocument.getPage(0);
8. let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
9. }
```

### addAnnotation

PhonePC/2in1Tablet

addAnnotation(annotationInfo: PdfAnnotationInfo): PdfAnnotation

在当前页添加批注。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let aInfo = new pdfService.TextAnnotationInfo();
9. aInfo.iconName = "test iconName";
10. aInfo.x = 200;
11. aInfo.y = 200;
12. aInfo.state = pdfService.TextAnnotationState.MARKED;
13. aInfo.flag = pdfService.AnnotationFlag.PRINTED;
14. let doc = pdfPage.addAnnotation(aInfo);
15. }
```

### setAnnotation

PhonePC/2in1Tablet

setAnnotation(annotation: PdfAnnotation, annotationInfo: PdfAnnotationInfo): void

在当前页设置批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotation | [PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation) | 是 | 文档批注。 |
| annotationInfo | [PdfAnnotationInfo](pdf-arkts-pdfservice.md#pdfannotationinfo) | 是 | 文档批注类。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let aInfo = new pdfService.TextAnnotationInfo();
9. // Text param
10. aInfo.iconName = "test iconName";
11. aInfo.state = pdfService.TextAnnotationState.UNMARKED;
12. aInfo.x = 200;
13. aInfo.y = 200;
14. aInfo.state = pdfService.TextAnnotationState.MARKED;
15. aInfo.flag = pdfService.AnnotationFlag.PRINTED;
16. let annotation = pdfPage.addAnnotation(aInfo);
17. let bInfo = new pdfService.TextAnnotationInfo();
18. bInfo.iconName = "yet another test iconName";
19. bInfo.state = pdfService.TextAnnotationState.MARKED;
20. bInfo.x = 200;
21. bInfo.y = 200;
22. bInfo.subject = "this is a subject";
23. bInfo.content = "this is a content";
24. pdfPage.setAnnotation(annotation, bInfo);
25. }
```

### removeAnnotation

PhonePC/2in1Tablet

removeAnnotation(annotation: PdfAnnotation): void

删除当前页批注。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| annotation | [PdfAnnotation](pdf-arkts-pdfservice.md#pdfannotation) | 是 | 文档批注。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let aInfo = new pdfService.TextAnnotationInfo();
9. // Text param
10. aInfo.iconName = "test iconName";
11. aInfo.x = 200;
12. aInfo.y = 200;
13. aInfo.state = pdfService.TextAnnotationState.MARKED;
14. aInfo.flag = pdfService.AnnotationFlag.PRINTED;
15. let annotation = pdfPage.addAnnotation(aInfo);
16. pdfPage.removeAnnotation(annotation);
17. }
```

### getIndex

PhonePC/2in1Tablet

getIndex(): number

获取当前页的索引。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 索引，取值范围大于等于0，小于总页数。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let index = pdfPage.getIndex();
9. }
```

### getWidth

PhonePC/2in1Tablet

getWidth(): number

获取当前页的宽。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 宽度值，单位为Points（一英寸等于72Points）。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let width = pdfPage.getWidth();
9. }
```

### getHeight

PhonePC/2in1Tablet

getHeight(): number

获取当前页的高。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 高度值，单位为Points（一英寸等于72Points）。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let height = pdfPage.getHeight();
9. }
```

### setBox

PhonePC/2in1Tablet

setBox(boxtype: BoxType, rect: PdfRect): void

设置页边界。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| boxtype | [BoxType](pdf-arkts-pdfservice.md#boxtype) | 是 | 页边界。 |
| rect | [PdfRect](pdf-arkts-pdfservice.md#pdfrect) | 是 | 矩形。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let pdfRect = new pdfService.PdfRect();
9. pdfRect.left = 100;
10. pdfRect.top = 100;
11. pdfRect.right = 100;
12. pdfRect.bottom = 100;
13. pdfPage.setBox(pdfService.BoxType.BOX_MEDIA , pdfRect);
14. }
```

### getBox

PhonePC/2in1Tablet

getBox(boxtype: BoxType): PdfRect

获取页边界。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let box: pdfService.PdfRect = pdfPage.getBox(pdfService.BoxType.BOX_MEDIA);
9. }
```

### setRotation

PhonePC/2in1Tablet

setRotation(rotation: RotationAngle): void

设置指定页面的显示旋转角度。旋转角度为顺时针方向的固定值，可选值包括 0、90、180、270 度。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | [RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 是 | 旋转角度枚举值。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. pdfPage.setRotation(pdfService.RotationAngle.ANGLE_90);
9. }
```

### getRotation

PhonePC/2in1Tablet

getRotation(): RotationAngle

获取页面的旋转角度。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RotationAngle](pdf-arkts-pdfservice.md#rotationangle) | 旋转角度。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let rotation = pdfPage.getRotation();
9. }
```

### getPagePixelMap

PhonePC/2in1Tablet

getPagePixelMap(): image.PixelMap

获取当前页的图片。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 当前页的image.PixelMap类型。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let img = pdfPage.getPagePixelMap();
9. }
```

### getCustomPagePixelMap

PhonePC/2in1Tablet

getCustomPagePixelMap(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap

获取指定PdfPage区间的图片内容。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { image } from '@kit.ImageKit';

4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
7. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
9. let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
10. let pixelMap: image.PixelMap = pdfPage.getCustomPagePixelMap(pdfMatrix, true, true);
11. }
```

### getAreaPixelMap

PhonePC/2in1Tablet

getAreaPixelMap(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap

将指定 PDF 页面渲染为像素图（PixelMap）。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { image } from '@kit.ImageKit';

4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
7. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
9. let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
10. let pixelMap: image.PixelMap = pdfPage.getAreaPixelMap(pdfMatrix, 200, 300, true, true);
11. }
```

### addTextObject

PhonePC/2in1Tablet

addTextObject(text: string, x: number, y: number, style: TextStyle): void

添加文本内容，只可按行添加。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

说明

系统版本请使用5.0.0.126(SP8)及其以上的版本，低于此版本该API不可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |
| x | number | 是 | x坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| y | number | 是 | y坐标，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| style | [TextStyle](pdf-arkts-pdfservice.md#textstyle) | 是 | 文本Style。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let textStyle = new pdfService.TextStyle();
9. let fontInfo = new pdfService.FontInfo();
10. fontInfo.fontPath = "/system/fonts/HarmonyOS_Sans_SC_Black.ttf"
11. textStyle.fontInfo = fontInfo;
12. textStyle.textSize = 11;
13. textStyle.textColor = 234;
14. textStyle.isBold = true;
15. textStyle.isItalic = false;
16. textStyle.isUnderline = true;
17. pdfPage.addTextObject('a', 20, 20, textStyle);
18. }
```

### addImageObject

PhonePC/2in1Tablet

addImageObject(path: string, x: number, y: number, width: number, height: number): void

在PDF文档的页面中添加图片。

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

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let context = this.getUIContext().getHostContext() as Context;
9. let dir = context.filesDir;
10. let imgPath = dir + "/img.jpg";
11. pdfPage.addImageObject(imgPath, 0, 0, 200, 200);
12. pdfDocument.saveDocument("/data/storage/el2/base/haps/entry/files/testAddImageToDocument.pdf");
13. }
```

### getGraphicsObjects

PhonePC/2in1Tablet

getGraphicsObjects(): Array<GraphicsObject>

获取所有图形对象。按位置顺序返回，如从左向右、从上向下。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)> | 所有图形对象数组。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let allImgObj = pdfPage.getGraphicsObjects();
9. }
```

### deleteGraphicsObject

PhonePC/2in1Tablet

deleteGraphicsObject(object: GraphicsObject): void

删除指定的[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)类型对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | [GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject) | 是 | 图形对象。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. let graphs: Array<pdfService.GraphicsObject> = pdfPage.getGraphicsObjects();
9. if (graphs.length > 0) {
10. pdfPage.deleteGraphicsObject(graphs[0]);
11. }
12. }
13. pdfDocument.releaseDocument();
```

### release

PhonePC/2in1Tablet

release(): void

释放已加载的PDF页面。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
8. pdfPage.release();
9. }
```

### getAreaPixelMapWithOptions

PhonePC/2in1Tablet

getAreaPixelMapWithOptions(matrix:PdfMatrix,bitmapwidth:number,bitmapHeight:number,options?:PixelOptions):image.PixelMap

获取当前PDF页面pixelMap类型的图片。

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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { image } from '@kit.ImageKit';

4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();
6. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
7. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
8. let pdfPage: pdfService.PdfPage = pdfDocument.getPage(0);
9. let pdfMatrix: pdfService.PdfMatrix = new pdfService.PdfMatrix();
10. pdfMatrix.x = 0;
11. pdfMatrix.y = 0;
12. pdfMatrix.width = pdfPage.getWidth();
13. pdfMatrix.height = pdfPage.getHeight();
14. pdfMatrix.rotate = 0;
15. let options: pdfService.PixelOptions = new pdfService.PixelOptions();
16. options.isGray = false;
17. options.drawAnnotations = true;
18. options.isTransparent = false;
19. let pixelMap: image.PixelMap = pdfPage.getAreaPixelMapWithOptions(pdfMatrix, 200, 300, options);
20. }
```

### getTextContent

PhonePC/2in1Tablet

getTextContent(): string

获取指定页面文本信息。

说明

该接口用于从文本类型的页面中提取原始文本数据，返回值为包含转义字符（如\r\n等）的String类型字符串。

页面中的图片、水印等元素不支持文本提取，返回空字符串。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 页面文本内容。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. // 将测试文件上传至应用沙箱路径
4. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
5. let pdfDocument = new pdfService.PdfDocument();

7. // 加载临时文件
8. let loadResult = pdfDocument.loadDocument(tempFilePath, '');

10. if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
11. let pdfPage = pdfDocument.getPage(0);
12. let pageText = pdfPage.getTextContent(); // 获取索引为0页文本数据信息
13. }
```

## GraphicsObject

PhonePC/2in1Tablet

图形对象的类型。

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

PhonePC/2in1Tablet

文本对象的类型，继承[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)。

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

PhonePC/2in1Tablet

图片对象的类型，继承[GraphicsObject](pdf-arkts-pdfservice.md#graphicsobject)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 使用一种特殊的语法来表示直接在内容流内的小图像数据。 |
| width | number | 否 | 否 | 图像宽度，必须大于0，单位为Points（一英寸等于72Points）。 |
| height | number | 否 | 否 | 图像高度，必须大于0，单位为Points（一英寸等于72Points）。 |

## Bookmark

PhonePC/2in1Tablet

书签对象的相关方法。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### isRootBookmark

PhonePC/2in1Tablet

isRootBookmark(): boolean

是否是根书签。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否是根书签，true表示是，false表示否。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let isRootBookmark = mark1.isRootBookmark();
12. }
```

### getParent

PhonePC/2in1Tablet

getParent(): Bookmark

获取书签父类相关的信息。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Bookmark](pdf-arkts-pdfservice.md#bookmark) | 父书签。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let parentBookmark = mark2.getParent();
12. }
```

### hasChild

PhonePC/2in1Tablet

hasChild(): boolean

是否有子书签。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否有子书签，true表示是，false表示否。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let hasChildBookmark = mark1.hasChild();
12. }
```

### getChildren

PhonePC/2in1Tablet

getChildren(): Array<Bookmark>

获取子书签列表。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Bookmark](pdf-arkts-pdfservice.md#bookmark)> | 子书签列表。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let childBookmark = mark1.getChildren();
12. }
```

### getDestInfo

PhonePC/2in1Tablet

getDestInfo(): DestInfo

获取书签的跳转信息。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DestInfo](pdf-arkts-pdfservice.md#destinfo) | 书签的跳转信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let destInfo: pdfService.DestInfo = mark1.getDestInfo();
12. destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
13. destInfo.pageIndex = 1;
14. destInfo.left = 20;
15. destInfo.top = 30;
16. destInfo.zoom = 1.5;
17. mark1.setDestInfo(destInfo);
18. let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
19. bookInfo.title = "hh";
20. bookInfo.titleColor = 12;
21. bookInfo.isBold = true;
22. bookInfo.isItalic = true;
23. mark1.setBookmarkInfo(bookInfo);
24. }
```

### setDestInfo

PhonePC/2in1Tablet

setDestInfo(info: DestInfo): void

设置书签的跳转信息。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [DestInfo](pdf-arkts-pdfservice.md#destinfo) | 是 | 书签的跳转信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let destInfo: pdfService.DestInfo = mark1.getDestInfo();
12. destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
13. destInfo.pageIndex = 1;
14. destInfo.left = 20;
15. destInfo.top = 30;
16. destInfo.zoom = 1.5;
17. mark1.setDestInfo(destInfo);
18. let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
19. bookInfo.title = "hh";
20. bookInfo.titleColor = 12;
21. bookInfo.isBold = true;
22. bookInfo.isItalic = true;
23. mark1.setBookmarkInfo(bookInfo);
24. }
```

### getBookmarkInfo

PhonePC/2in1Tablet

getBookmarkInfo(): BookmarkInfo

获取书签信息。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BookmarkInfo](pdf-arkts-pdfservice.md#bookmarkinfo) | 书签信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let destInfo: pdfService.DestInfo = mark1.getDestInfo();
12. destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
13. destInfo.pageIndex = 1;
14. destInfo.left = 20;
15. destInfo.top = 30;
16. destInfo.zoom = 1.5;
17. mark1.setDestInfo(destInfo);
18. let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
19. bookInfo.title = "hh";
20. bookInfo.titleColor = 12;
21. bookInfo.isBold = true;
22. bookInfo.isItalic = true;
23. mark1.setBookmarkInfo(bookInfo);
24. }
```

### setBookmarkInfo

PhonePC/2in1Tablet

setBookmarkInfo(info: BookmarkInfo): void

设置书签信息。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [BookmarkInfo](pdf-arkts-pdfservice.md#bookmarkinfo) | 是 | 书签信息。 |

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let tempFilePath = '/data/storage/el2/base/temp/test.pdf';
4. let pdfDocument = new pdfService.PdfDocument();
5. let loadResult = pdfDocument.loadDocument(tempFilePath, '');
6. if(pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
7. let mark1: pdfService.Bookmark = pdfDocument.createBookmark();
8. let mark2: pdfService.Bookmark = pdfDocument.createBookmark();
9. pdfDocument.insertBookmark(mark1, null, 1);
10. pdfDocument.insertBookmark(mark2, mark1, 1);
11. let destInfo: pdfService.DestInfo = mark1.getDestInfo();
12. destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
13. destInfo.pageIndex = 1;
14. destInfo.left = 20;
15. destInfo.top = 30;
16. destInfo.zoom = 1.5;
17. mark1.setDestInfo(destInfo);
18. let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
19. bookInfo.title = "hh";
20. bookInfo.titleColor = 12;
21. bookInfo.isBold = true;
22. bookInfo.isItalic = true;
23. mark1.setBookmarkInfo(bookInfo);
24. }
```

## BookmarkInfo

PhonePC/2in1Tablet

书签类的相关属性。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 书签的标题文本，用于标识书签指向的PDF内容。 |
| titleColor | number | 否 | 是 | 标题颜色，取值范围0x000000 ~ 0xFFFFFF，默认值：0x000000。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| isBold | boolean | 否 | 是 | 标题是否粗体，true表示是，false表示否  ，默认值：false。 |
| isItalic | boolean | 否 | 是 | 标题是否斜体，true表示是，false表示否，默认值：false。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建书签类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let bookmarkInfo = new pdfService.BookmarkInfo();
```

## HeaderFooterInfo

PhonePC/2in1Tablet

页眉页脚类的相关属性。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 否 | 字体的信息。 |
| textSize | number | 否 | 否 | 页眉页脚文本大小，必须大于0，单位为Points（一英寸等于72Points）。 |
| charset | [CharsetType](pdf-arkts-pdfservice.md#charsettype) | 否 | 否 | 文本字符集。 |
| underline | boolean | 否 | 否 | 下划线是否添加，true表示是，false表示否。 |
| textColor | number | 否 | 是 | 文字颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| leftMargin | number | 否 | 是 | 页眉页脚左间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| topMargin | number | 否 | 是 | 页眉页脚顶部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| rightMargin | number | 否 | 是 | 页眉页脚右间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| bottomMargin | number | 否 | 是 | 页眉页脚底部间距，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| headerLeftText | string | 否 | 是 | 页眉左边文字。 |
| headerCenterText | string | 否 | 是 | 页眉中间文字。 |
| headerRightText | string | 否 | 是 | 页眉右边文字。 |
| footerLeftText | string | 否 | 是 | 页脚左边文字。 |
| footerCenterText | string | 否 | 是 | 页脚中间文字。 |
| footerRightText | string | 否 | 是 | 页脚右边文字。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建页眉页脚类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let headerFooterInfo = new pdfService.HeaderFooterInfo();
```

## WatermarkInfo

PhonePC/2in1Tablet

水印类的相关属性，自己属于父类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| watermarkType | [WatermarkType](pdf-arkts-pdfservice.md#watermarktype) | 否 | 否 | 水印类型。 |
| isOnTop | boolean | 否 | 否 | 是否置顶，true表示是，false表示否。 |
| scale | number | 否 | 否 | 缩放，必须大于0，小于等于5。 |
| rotation | number | 否 | 否 | 旋转。 |
| opacity | number | 否 | 否 | 透明度，取值范围 0~1。 |
| horizontalAlignment | [WatermarkAlignment](pdf-arkts-pdfservice.md#watermarkalignment) | 否 | 否 | 水平对齐。 |
| horizontalSpace | number | 否 | 否 | 表示水印与页面边缘的水平距离，必须大于等于0，单位为Points（一英寸等于72Points）。 |
| verticalAlignment | [WatermarkAlignment](pdf-arkts-pdfservice.md#watermarkalignment) | 否 | 否 | 垂直对齐。 |
| verticalSpace | number | 否 | 否 | 表示水印与页面边缘的垂直距离，必须大于等于0，单位为Points（一英寸等于72Points）。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建水印类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

```
1. import { pdfService } from '@kit.PDFKit';

3. let watermarkInfo = new pdfService.WatermarkInfo();
```

## TextWatermarkInfo

PhonePC/2in1Tablet

文本水印类的相关属性，继承[WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | 否 | 否 | 文本水印内容。 |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 否 | 字体的信息。 |
| textSize | number | 否 | 否 | 文本大小，必须大于0。 |
| textColor | number | 否 | 否 | 文本颜色，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |

## ImageWatermarkInfo

PhonePC/2in1Tablet

图片水印类的相关属性，继承[WatermarkInfo](pdf-arkts-pdfservice.md#watermarkinfo)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string | 否 | 否 | 图片路径。 |

## BackgroundInfo

PhonePC/2in1Tablet

背景类的相关属性。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string | 否 | 否 | 图片路径（图片路径不填则背景色必填）。 |
| backgroundColor | number | 否 | 否 | 背景颜色（背景色不填则图片路径必填）  ，取值范围0x000000 ~ 0xFFFFFF。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| isOnTop | boolean | 否 | 否 | 是否置顶，true表示是，false表示否。 |
| scale | number | 否 | 否 | 缩放，必须大于0，小于等于5。 |
| rotation | number | 否 | 否 | 旋转。 |
| opacity | number | 否 | 否 | 透明度，取值范围0~1。 |
| horizontalAlignment | [BackgroundAlignment](pdf-arkts-pdfservice.md#backgroundalignment) | 否 | 否 | 水平对齐。 |
| horizontalSpace | number | 否 | 否 | 水平间距，必须大于等于0，单位为英寸（一英寸等于72Points）。 |
| verticalAlignment | [BackgroundAlignment](pdf-arkts-pdfservice.md#backgroundalignment) | 否 | 否 | 垂直对齐。 |
| verticalSpace | number | 否 | 否 | 垂直间距，必须大于等于0，单位为英寸（一英寸等于72Points）。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建背景类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let backgroundInfo = new pdfService.BackgroundInfo();
```

## PdfAction

PhonePC/2in1Tablet

批注链接跳转，属于父类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PdfActionType](pdf-arkts-pdfservice.md#pdfactiontype) | 否 | 否 | 批注链接跳转类型。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建批注链接类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let pdfAction = new pdfService.PdfAction();
```

## PdfActionGoTo

PhonePC/2in1Tablet

页面内的跳转，继承[PdfAction](pdf-arkts-pdfservice.md#pdfaction)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| destInfo | [DestInfo](pdf-arkts-pdfservice.md#destinfo) | 否 | 否 | 跳转信息。 |

## PdfActionHyperlink

PhonePC/2in1Tablet

超链接跳转，继承[PdfAction](pdf-arkts-pdfservice.md#pdfaction)。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hyperlink | string | 否 | 否 | 超链接地址。 |

## PixelOptions

PhonePC/2in1Tablet

PDF页面转图片相关参数选项。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isGray | boolean | 否 | 是 | 是否获取仅灰度的图像，true: 是，false: 否。  默认值：true。 |
| drawAnnotations | boolean | 否 | 是 | 是否在图像中注释，true: 是，false: 否。  默认值：true。 |
| isTransparent | boolean | 否 | 是 | 是否获取透明图像，true: 是，false: 否。  默认值：false。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建图片类参数选项的对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

```
1. import { pdfService } from '@kit.PDFKit';

3. let pixelOptions = new pdfService.PixelOptions();
```

## FontInfo

PhonePC/2in1Tablet

字体类。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontPath | string | 否 | 是 | 字体的路径。 |
| fontName | string | 否 | 是 | 字体的名称。 |

### constructor

PhonePC/2in1Tablet

constructor()

用于创建字体类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let fontInfo = new pdfService.FontInfo();
```

## DestInfo

PhonePC/2in1Tablet

书签跳转信息。

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

PhonePC/2in1Tablet

constructor()

用于创建书签跳转类对象。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { pdfService } from '@kit.PDFKit';

3. let destInfo = new pdfService.DestInfo();
```

## TextStyle

PhonePC/2in1Tablet

文本样式的类型。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontInfo | [FontInfo](pdf-arkts-pdfservice.md#fontinfo) | 否 | 是 | 字体信息，默认字体：HarmonyOS\_Sans。 |
| textSize | number | 否 | 是 | 字体大小，必须大于0，默认值：20。单位为Points（一英寸等于72Points）。 |
| textColor | number | 否 | 是 | 字体颜色，取值范围0x000000 ~ 0xFFFFFF，默认值：0x000000。  (例如：0xFF0000代表蓝色，0x0000FF代表红色) |
| isBold | boolean | 否 | 是 | 是否粗体，true表示是，false表示否，默认值：false。 |
| isItalic | boolean | 否 | 是 | 是否斜体，true表示是，false表示否，默认值：false。 |
| isUnderline | boolean | 否 | 是 | 是否有下划线，true表示是，false表示否，默认值：false。 |
| isStrikethrough | boolean | 否 | 是 | 是否有删除线，true表示是，false表示否，默认值：false。 |

## BorderStyle

PhonePC/2in1Tablet

线框枚举类型。

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

PhonePC/2in1Tablet

批注标识举类型枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVISIBLE | 1 | 不可见。 |
| HIDDEN | 2 | 隐藏。 |
| PRINTED | 4 | 注释。 |

## TextAnnotationState

PhonePC/2in1Tablet

文本批注状态类型枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNMARKED | 0 | 由用户评论和标记。 |
| MARKED | 1 | 默认情况下，用户不用再标记注释。 |

## HighlightMode

PhonePC/2in1Tablet

文本高亮模式类型枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGHLIGHT\_INVERT | 1 | 反转注释区域内的颜色。 |
| HIGHLIGHT\_OUTLINE | 2 | 显示注释的边框轮廓。 |
| HIGHLIGHT\_PUSH | 3 | 将注释外观覆盖在页面内容上。 |
| HIGHLIGHT\_TOGGLE | 4 | 切换显示状态，仅用于表单控件。 |

## AlignmentType

PhonePC/2in1Tablet

文本对齐方式枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 到页面左边缘的距离。 |
| MIDDLE | 1 | 到页面中心线的距离。 |
| RIGHT | 2 | 到页面右边缘的距离。 |

## LineEndStyle

PhonePC/2in1Tablet

线条端点的线条样式枚举。

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

PhonePC/2in1Tablet

打开文档返回值枚举。

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

PhonePC/2in1Tablet

页面布局显示方式枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYOUT\_SINGLE | 1 | 单页面。 |
| LAYOUT\_DOUBLE | 2 | 双页面。 |

## PageFit

PhonePC/2in1Tablet

页面适配方式枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIT\_NONE | 0 | 实际大小。 |
| FIT\_PAGE | 1 | 按页缩放。 |
| FIT\_WIDTH | 2 | 按宽度。 |
| FIT\_HEIGHT | 3 | 按高度。 |

## RotationAngle

PhonePC/2in1Tablet

旋转角度枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ANGLE\_0 | 0 | 0度。 |
| ANGLE\_90 | 90 | 90度。 |
| ANGLE\_180 | 180 | 180度。 |
| ANGLE\_270 | 270 | 270度。 |

## ImageFormat

PhonePC/2in1Tablet

图片类型枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PNG | 0 | png类型。 |
| BMP | 1 | bmp类型。 |
| JPEG | 2 | jpeg类型。 |

## AnnotationType

PhonePC/2in1Tablet

批注类型枚举。

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

PhonePC/2in1Tablet

页边界枚举。

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

PhonePC/2in1Tablet

图形对象类型枚举。

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

PhonePC/2in1Tablet

字符集对象类型枚举。

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

PhonePC/2in1Tablet

页面适合模式枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIT\_MODE\_XYZ | 1 | 按页面左上角的点缩放页面，页面内容按缩放比例放大。 |
| FIT\_MODE\_HORIZONTAL | 2 | 使页面适应窗口内的整个页面宽度。 |
| FIT\_MODE\_VERTICAL | 3 | 使页面适应窗口内的整个页面高度。 |
| FIT\_MODE\_RECT | 4 | 使页面适合窗口内的页面矩形。 |

## WatermarkType

PhonePC/2in1Tablet

页面水印类型枚举。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WATERMARK\_TEXT | 1 | 文本水印。 |
| WATERMARK\_IMAGE | 2 | 图片水印。 |

## WatermarkAlignment

PhonePC/2in1Tablet

文档水印位置类型枚举

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

PhonePC/2in1Tablet

文档背景位置类型枚举。

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

PhonePC/2in1Tablet

链接跳转类型。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知类型 |
| GOTO | 1 | 文档内链接类型 |
| HYPERLINK | 2 | 超链接类型 |
