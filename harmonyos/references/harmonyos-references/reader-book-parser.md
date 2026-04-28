---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-book-parser
title: bookParser（书籍解析能力）
breadcrumb: API参考 > 应用服务 > Reader Kit（阅读服务） > ArkTS API > bookParser（书籍解析能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:393a63966c617818f0d6b75c3eb5e522f42f5405183fda8c9e9aaed30ff5448d
---

本模块提供书籍解析的能力，支持对txt、epub、mobi、azw、azw3格式的书籍文件进行解析。通过提前导入到[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)中的书籍文件，初始化[BookParserHandler](reader-book-parser.md#bookparserhandler)。将书籍基本信息、[书脊](../harmonyos-guides/reader-introduction.md#基本概念)内容列表、目录列表和章节内容解析出来。

**起始版本：** 5.0.4(16)

## 导入模块

PhonePC/2in1Tablet

```
1. import { bookParser } from '@kit.ReaderKit';
```

## BookInfo

PhonePC/2in1Tablet

书籍基本信息。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| bookTitle | string | 否 | 否 | 书籍名称。 |
| bookCreator | string | 否 | 是 | 作者。 |
| bookPublishDate | string | 否 | 是 | 出版日期。（预留字段，暂不支持。） |
| bookLanguage | string | 否 | 是 | 书籍语言。  - zh\_HK：繁体中文，包括台湾繁体及香港繁体。  - zh\_CN：中文简体。  - zh：中文（不支持或非法语言会使用zh作为默认值）。  - en\_US：英文。 |
| bookCoverImage | string | 否 | 是 | 书封图片路径。例如：“OEBPS/images/coverpage.jpg”。 |
| bookCharset | string | 否 | 是 | 书籍内容的字符集，根据书籍编码格式决定，例如："utf-8"。具体支持格式可参考[TextEncoder](js-apis-util.md#textencoder)定义。（预留字段，暂不支持。） |
| bookType | string | 否 | 是 | 书籍格式： "txt"、"epub"、"mobi"、"azw"、"azw3"。 |
| isRtl | boolean | 否 | 是 | 书籍阅读方向。（预留字段，暂不支持。）  - true：从右到左排版  - false：从左到右排版 |
| renditionLayout | string | 否 | 是 | 书籍排版方式。（预留字段，暂不支持。）  - reflowable：流式排版  - pre-paginated：固定版式排版 |
| renditionOrientation | string | 否 | 是 | 横竖屏呈现定义。（预留字段，暂不支持。）  - landscape：横屏  - portrait：竖屏  - auto：自适应 |
| renditionSpread | string | 否 | 是 | 书脊左右页合并场景。（预留字段，暂不支持。）  - none：不合并分页  - landscape：横屏合并  - portrait：竖屏时合并  - auto：自动适配 |

## SpineItem

PhonePC/2in1Tablet

书脊（spine）内容节点，标识着可阅读的一个内容资源（例如：chapter1.xhtml)。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idRef | string | 否 | 否 | 内容节点资源标识，唯一标识一个正文内容文件。 |
| index | number | 否 | 否 | 内容资源索引，从0开始顺序取值。 |
| href | string | 否 | 否 | 内容资源在书籍内的引用路径。例如："/OEBPS/Txt/chapter01.xhtml"。 |
| properties | string | 否 | 否 | 当一屏双页展示时，内容节点的呈现方式。（预留字段，暂不支持。）  - page-spread-left：标识内容在屏幕左侧呈现。  - page-spread-right：标识内容在屏幕右侧呈现。 |

## CatalogItem

PhonePC/2in1Tablet

书籍目录节点，可用于目录列表的展示。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| catalogId | number | 否 | 否 | 目录节点Id，从0开始取值。 |
| catalogName | string | 否 | 否 | 目录节点名称。 |
| catalogLevel | number | 否 | 是 | 目录节点层级。  例如：第一章的目录层级是0，下面有子章节，那子章节的目录层级+1，为1。如果子章节下面还有子章节，则继续+1，为2。  开发者根据目录节点顺序及层级，可识别出目录之间的层级关系。 |
| playOrder | number | 否 | 是 | 目录节点阅读顺序，从0开始取值。（预留字段，暂不支持。） |
| idRef | string | 否 | 是 | 目录节点对应内容资源的标识。（预留字段，暂不支持。） |
| href | string | 否 | 是 | 目录节点带锚点的内容资源路径。 |
| resourceFile | string | 否 | 是 | 目录节点不带锚点的内容资源路径。  以EPUB书籍为例，该字段则标识着资源以/OEBPS为根目录的相对路径。 |

说明

CatalogItem与SpineItem的区别在于，CatalogItem对应一个目录节点，而SpineItem对应一个内容资源文件，两者并不总是一一对应的。例如：epub书籍一章下面有3个子章节，那就有4个CatalogItem。但是这4个CatalogItem有可能只对应一个SpineItem文件，两者通过CatalogItem.resourceFile及SpineItem.href进行对应。

## CallbackRes

PhonePC/2in1Tablet

type CallbackRes<T, V> = (data: T) => V

书籍资源请求回调接口，在排版引擎渲染界面时调用，需配合ReaderComponentController的注册接口[on('resourceRequest')](reader-read-core.md#onresourcerequest)使用。如果有自定义背景及字体资源，需要在此返回对应资源。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 资源请求接口中的参数。例如：获取自定义字体时，该字段代表需要获取字体的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 资源请求接口中的返回值类型。例如：获取自定义字体时，该返回值代表字体文件的二进制数据流。 |

**示例：**

```
1. import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
10. private selectFontPath = 'fonts/SourceHanSerifCN-VF.ttf';

12. aboutToAppear(): void {
13. this.registerListener();
14. }

16. private async registerListener(){
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. await this.readerComponentController.init(context)
19. this.readerComponentController.on('resourceRequest', this.resourceRequest);
20. }

22. private resourceRequest: bookParser.CallbackRes<string,ArrayBuffer> = (fileName: string): ArrayBuffer => {
23. if (this.isFont(fileName)) {
24. let res = $rawfile(this.selectFontPath);
25. let context = this.getUIContext().getHostContext();
26. if (res && context) {
27. // 获取资源路径下的字体数据
28. let value: Uint8Array = context.resourceManager.getRawFileContentSync(this.selectFontPath);
29. hilog.info(0x0000, 'testTag', 'resourceRequest : get success');
30. return value.buffer as ArrayBuffer;
31. }
32. }
33. return new ArrayBuffer(0);
34. }

36. private isFont(filePath: string): boolean {
37. let options = [".ttf", ".woff2", ".otf"];
38. let path = filePath.toLowerCase();
39. let result = path.indexOf(options[0]) != -1 || path.indexOf(options[1]) != -1 || path.indexOf(options[2]) != -1;
40. hilog.info(0x0000, 'testTag', 'isFont = ' + result);
41. return result;
42. }

44. build() {
45. Stack() {
46. ReadPageComponent({
47. controller: this.readerComponentController,
48. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
49. this.readerComponentController = data;
50. }
51. })
52. }.width('100%').height('100%')
53. }
54. }
```

## getDefaultHandler

PhonePC/2in1Tablet

getDefaultHandler(path: string): Promise<BookParserHandler>

获取书籍默认解析器。使用Promise异步回调。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 本地书籍文件路径（仅支持当前应用下的[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BookParserHandler](reader-book-parser.md#bookparserhandler)> | Promise对象，返回BookParserHandler类。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010003](reader-error-code.md#section1017010003) | Book file format is unexpected. |
| [1017010004](reader-error-code.md#section1017010004) | File is not exist. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.initBookParser();
10. }

12. private async initBookParser() {
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. // 业务自行根据需要调用bookParserHandler接口
18. hilog.info(0x0000, 'testTag', `getDefaultHandler succeeded`);
19. }

21. build() {
22. // 业务自行实现页面布局
23. }
24. }
```

## BookParserHandler

PhonePC/2in1Tablet

书籍解析接口类。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

### getBookInfo

PhonePC/2in1Tablet

getBookInfo(): BookInfo

获取书籍信息。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BookInfo](reader-book-parser.md#bookinfo) | 书籍基本信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getBookInfo();
10. }

12. private async getBookInfo() {
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. let bookInfo: bookParser.BookInfo = bookParserHandler.getBookInfo();
18. hilog.info(0x0000, 'testTag', `getBookInfo succeeded, bookInfo:` + JSON.stringify(bookInfo));
19. }

21. build() {
22. // 业务自行实现页面布局
23. }
24. }
```

### getCatalogList

PhonePC/2in1Tablet

getCatalogList(): CatalogItem[]

获取书籍目录列表。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CatalogItem](reader-book-parser.md#catalogitem)[] | 目录节点列表。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized |
| [1017000999](reader-error-code.md#section1017000999) | Other error |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getCatalogList();
10. }

12. private async getCatalogList(){
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. let catalogList: bookParser.CatalogItem[] = bookParserHandler.getCatalogList();
18. hilog.info(0x0000, 'testTag', `getCatalogList succeeded, catalogList:` + JSON.stringify(catalogList));
19. }

21. build() {
22. // 业务自行实现页面布局
23. }
24. }
```

### getSpineList

PhonePC/2in1Tablet

getSpineList(): SpineItem[]

获取书脊内容列表。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SpineItem](reader-book-parser.md#spineitem)[] | 内容节点列表。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getSpineList();
10. }

12. private async getSpineList(){
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
18. hilog.info(0x0000, 'testTag', `getSpineList succeeded, spineList:` + JSON.stringify(spineList));
19. }

21. build() {
22. // 业务自行实现页面布局
23. }
24. }
```

### getSpineItemContent

PhonePC/2in1Tablet

getSpineItemContent(spineIndex: number): Promise<string>

获取单个书脊资源里的内容，当排版引擎获取资源文件对应内容时会调用。如果不需要自定义排版引擎，开发者不需要关注。使用Promise异步回调。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spineIndex | number | 是 | 内容资源索引[SpineItem](reader-book-parser.md#spineitem).index。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回单个书脊内容字符串。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1.Incorrect parameter types; 2. Parameter out of range. |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010001](reader-error-code.md#section1017010001) | Invalid spine item. |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getSpineItemContent();
10. }

12. private async getSpineItemContent(){
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
18. let spineItemContent: string = await bookParserHandler.getSpineItemContent(spineList[0].index);
19. hilog.info(0x0000, 'testTag', `getSpineItemContent succeeded, spineItemContent:` + JSON.stringify(spineItemContent));
20. }

22. build() {
23. // 业务自行实现页面布局
24. }
25. }
```

### getResourceContent

PhonePC/2in1Tablet

getResourceContent(spineIndex: number, filePath: string): ArrayBuffer

获取书籍内容资源。

说明

开发者通过此接口可获取书封资源。同时排版引擎获取书籍里的图片等资源时，会优先调用该方法，如果获取不到资源会继续调用[on('resourceRequest')](reader-read-core.md#onresourcerequest)获取资源。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spineIndex | number | 是 | 内容资源索引[SpineItem](reader-book-parser.md#spineitem).index。如果传负数，如-1，代表获取书封。 |
| filePath | string | 是 | 书籍中资源文件的相对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回文件的二进制数据。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1.Incorrect parameter types; 2. Parameter out of range. |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010001](reader-error-code.md#section1017010001) | Invalid spine item. |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getResourceContent();
10. }

12. private async getResourceContent() {
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. // 需要替换成实际书籍文件中存在的图片名称
18. let imagePath = './2188093923226426261_image001.jpg'
19. let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
20. let resourceContent: ArrayBuffer = bookParserHandler.getResourceContent(spineList[0].index, imagePath);
21. hilog.info(0x0000, 'testTag', `getResourceContent succeeded, resourceContentByteLength:` + resourceContent.byteLength);
22. }

24. build() {
25. // 业务自行实现页面布局
26. }
27. }
```

### getDomPosByCatalogHref

PhonePC/2in1Tablet

getDomPosByCatalogHref(href: string): string

获取阅读起始位置domPos，可用于阅读进度标识（例如：跳转到指定阅读位置）。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| href | string | 是 | 目录节点带锚点的内容资源路径[CatalogItem](reader-book-parser.md#catalogitem).href。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 章节的domPos信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1.Incorrect parameter types; 2. Parameter out of range. |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getDomPosByCatalogHref();
10. }

12. private async getDomPosByCatalogHref(){
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. let catalogList: bookParser.CatalogItem[] = bookParserHandler.getCatalogList();
18. let href = catalogList[1]?.href || '';
19. let domPos: string = bookParserHandler.getDomPosByCatalogHref(href);
20. hilog.info(0x0000, 'testTag', `getDomPosByCatalogHref succeeded, domPos:` + domPos);
21. }

23. build() {
24. // 业务自行实现页面布局
25. }
26. }
```

### getAbsoluteResourcePath

PhonePC/2in1Tablet

getAbsoluteResourcePath(spineIndex: number): string

获取资源的完整文件路径。

说明

此方法一般为排版引擎渲染资源时调用，如果不需要自定义排版引擎，开发者不需要关注。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.BookParser

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spineIndex | number | 是 | 内容资源索引[SpineItem](reader-book-parser.md#spineitem).index。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源的完整路径 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1.Incorrect parameter types; 2. Parameter out of range. |
| [1017000001](reader-error-code.md#section1017000001) | Book parser is not initialized. |
| [1017000999](reader-error-code.md#section1017000999) | Other error. |
| [1017010002](reader-error-code.md#section1017010002) | Invalid request. |
| [1017010004](reader-error-code.md#section1017010004) | File is not exist. |

**示例：**

```
1. import { bookParser } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Reader {
8. aboutToAppear(): void {
9. this.getAbsoluteResourcePath();
10. }

12. private async getAbsoluteResourcePath(){
13. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let filePath: string = `${context.filesDir}/abc.epub`;
16. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
17. let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
18. let resourcePath: string = bookParserHandler.getAbsoluteResourcePath(spineList[0].index);
19. hilog.info(0x0000, 'testTag', `getAbsoluteResourcePath succeeded, resourcePath:` + resourcePath);
20. }

22. build() {
23. // 业务自行实现页面布局
24. }
25. }
```
