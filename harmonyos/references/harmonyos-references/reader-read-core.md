---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core
title: readerCore（阅读核心能力）
breadcrumb: API参考 > 应用服务 > Reader Kit（阅读服务） > ArkTS API > readerCore（阅读核心能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a19ef19084957e741b27a13a33b422ca99caa7024fe87b70da66852d5dc5c7d
---

本模块为Reader Kit核心能力。提供阅读页面数据基础类、页面状态、内容分页信息、页面排版属性、组件控制器等能力。

**起始版本：** 5.0.4(16)

## 导入模块

PhonePC/2in1Tablet

```
1. import { readerCore } from '@kit.ReaderKit';
```

## PageDatabaseBean

PhonePC/2in1Tablet

页面数据基础类。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nodeType | string | 否 | 否 | 节点类型，固定值为“ReaderCoreIdentity”，表示阅读器节点。 |
| dataId | string | 否 | 否 | 节点标识，根据资源索引、页面偏移量自动生成。 |

### constructor

PhonePC/2in1Tablet

constructor(nodeType: string, nodeDataId: string)

页面数据构造函数。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nodeType | string | 是 | 节点类型，固定值为“ReaderCoreIdentity”，表示阅读器节点。 |
| nodeDataId | string | 是 | 节点标识，根据子类[PageDataInfo](reader-read-core.md#pagedatainfo).resourceIndex、[PageDataInfo](reader-read-core.md#pagedatainfo).pageOffset字段自动生成。 |

## PageState

PhonePC/2in1Tablet

页面状态。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAGE\_WAITING | 1 | 等待加载。 |
| PAGE\_LOADING | 2 | 加载中。 |
| PAGE\_ON\_SHOW | 3 | 加载成功。 |
| OPEN\_BOOK\_FAIL | 4 | 加载失败。 |

## PageDataInfo

PhonePC/2in1Tablet

内容分页信息，继承[PageDatabaseBean](reader-read-core.md#pagedatabasebean)。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nodeType | string | 否 | 否 | 节点类型，固定值为"ReaderCoreIdentity"，表示阅读器节点。 |
| dataId | string | 否 | 否 | 节点标识，根据“resourceIndex”、“pageOffset”字段自动生成。 |
| pageHeaderContent | string | 否 | 否 | 页眉文本。（预留字段，暂不支持。） |
| pageFooterContent | string | 否 | 否 | 页脚文本。（预留字段，暂不支持。） |
| startDomPos | string | 否 | 否 | 当前页的起始位置信息。 |
| endDomPos | string | 否 | 否 | 当前页的结束位置信息。 |
| state | [PageState](reader-read-core.md#pagestate) | 否 | 否 | 页面状态。 |
| resourceIndex | number | 否 | 否 | 书脊内容节点索引[SpineItem](reader-book-parser.md#spineitem).index。 |
| pageOffset | number | 否 | 否 | 页数偏移值，从0开始取值。  例如：一个内容资源文件有50页，这个值的取值范围则为0-49。 |

### constructor

PhonePC/2in1Tablet

constructor(nodeType: string, nodeId: string)

内容分页信息构造函数。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nodeType | string | 是 | 节点类型，固定值为“ReaderCoreIdentity”。 |
| nodeId | string | 是 | 节点标识，根据子类[PageDataInfo](reader-read-core.md#pagedatainfo).resourceIndex、[PageDataInfo](reader-read-core.md#pagedatainfo).pageOffset字段自动生成。 |

## ReaderSetting

PhonePC/2in1Tablet

页面排版属性。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| fontName | string | 否 | 否 | 字体名称。 |
| fontSize | number | 否 | 否 | 字号大小，单位：px。 |
| fontWeight | number | 否 | 否 | 文本的字体粗细，依赖所引用的字体文件是否支持设置文本的粗细。（预留字段，暂不支持。） |
| fontColor | string | 否 | 否 | 字体颜色。例如'#ffffff'、'rgba(248, 249, 250, 1)'。  字体颜色值的限制如下：  - 对于16进制颜色值，只支持6位颜色值，不支持透明度。  - 对于rgba颜色值，透明度的值只支持1。 |
| fontPath | string | 否 | 否 | 字体文件本地路径。  支持两种存放路径：  - 工程目录resources/rawfile文件夹。适合预置字体场景。  - [应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。适合在线下载字体场景。 |
| lineHeight | number | 否 | 否 | 行高系数。一行文本实际显示高度为fontSize \* lineHeight。 |
| nightMode | boolean | 否 | 否 | 是否深色模式，需要开发者在监听到深、浅模式变化时手动设置。  用于仿真翻页时背面主题色的绘制。  - true：深色模式。  - false：浅色模式，默认是false。 |
| themeColor | string | 否 | 否 | 主题背景色。示例：'#ffffff'、'rgba(248, 249, 250, 1)'。  如果有设置背景图片的情况下，通常用于仿真翻页时背面主题色的绘制。  如果没有设置背景图片，还会用于渲染阅读页的背景色。  背景色的值限制如下：  - 对于16进制颜色值，只支持6位颜色值，不支持透明度。  - 对于rgba颜色值，透明度的值只支持1。 |
| themeBgImg | string | 否 | 否 | 主题背景图路径，用于阅读页背景的绘制。  支持两种存放路径：  - 工程目录resources/rawfile文件夹。适合预置背景图场景。  - [应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。适合在线下载背景图场景。 |
| flipMode | string | 否 | 否 | 翻页方式。  - '0'：仿真。  - '1'：横滑。  默认值为0。 |
| scaledDensity | number | 否 | 否 | 系统显示文本的缩放因子，该值通过[display.getDefaultDisplaySync().scaledDensity](js-apis-display.md#displaygetdefaultdisplaysync9)字段获取。  在智慧多窗等场景，文本缩放因子发生变化时，开发者需要调用ReaderComponentController组件控制器的[setPageConfig](reader-read-core.md#setpageconfig)接口更新该属性。 |
| viewPortWidth | number | 否 | 否 | 排版视口宽度，单位：px。 |
| viewPortHeight | number | 否 | 否 | 排版视口高度，单位：px。 |

## ReaderComponentController

PhonePC/2in1Tablet

[ReadPageComponent](reader-api-readpagecomponent.md#readpagecomponent)组件控制器，需要配合ReadPageComponent组件一起使用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

### init

PhonePC/2in1Tablet

init(context: common.UIAbilityContext): Promise<void>

初始化ReaderComponentController，使用Promise异步回调。

说明

在集成ReaderComponentController时，初始化接口一定要优先于controller的其他接口之前执行。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 当前应用上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1016910004](reader-error-code.md#section1016910004) | Invalid caller. |

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.init();
13. }

15. private async init(){
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. await this.readerComponentController.init(context);
18. hilog.info(0x0000, 'testTag', `init succeeded`);
19. }

21. build() {
22. Stack() {
23. ReadPageComponent({
24. controller: this.readerComponentController,
25. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
26. this.readerComponentController = data;
27. }
28. })
29. }.width('100%').height('100%')
30. }
31. }
```

### registerBookParser

PhonePC/2in1Tablet

registerBookParser(bookParserHandler: bookParser.BookParserHandler): void

注册书籍解析器。

说明

registerBookParser接口需要在[startPlay](reader-read-core.md#startplay)接口之前调用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bookParserHandler | bookParser.[BookParserHandler](reader-book-parser.md#bookparserhandler) | 是 | 书籍解析器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1016900002](reader-error-code.md#section1016900002) | Read Page Component is not initialized. |
| [1016900003](reader-error-code.md#section1016900003) | Invalid request. |
| [1016900999](reader-error-code.md#section1016900999) | Other error. |

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

11. aboutToAppear(): void {
12. this.registerBookParser();
13. }

15. private async registerBookParser(){
16. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. let filePath: string = `${context.filesDir}/abc.epub`;
19. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
20. await this.readerComponentController.init(context);
21. this.readerComponentController.registerBookParser(bookParserHandler);
22. hilog.info(0x0000, 'testTag', `registerBookParser succeeded`);
23. }

25. build() {
26. Stack() {
27. ReadPageComponent({
28. controller: this.readerComponentController,
29. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
30. this.readerComponentController = data;
31. }
32. })
33. }.width('100%').height('100%')
34. }
35. }
```

### setPageConfig

PhonePC/2in1Tablet

setPageConfig(pageConfig: ReaderSetting): void

设置或者修改页面排版属性。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageConfig | [ReaderSetting](reader-read-core.md#readersetting) | 是 | 页面排版属性。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1016900002](reader-error-code.md#section1016900002) | Read Page Component is not initialized. |
| [1016900003](reader-error-code.md#section1016900003) | Invalid request. |
| [1016900999](reader-error-code.md#section1016900999) | Other error. |

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { display } from '@kit.ArkUI';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. @Entry
8. @Component
9. struct Reader {
10. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

12. aboutToAppear(): void {
13. this.setPageConfig();
14. }

16. private async setPageConfig(){
17. let readerSetting: readerCore.ReaderSetting = {
18. fontName: '系统字体',
19. fontPath: '',
20. fontSize: 18,
21. fontColor: '#000000',
22. fontWeight: 400,
23. lineHeight: 1.9,
24. nightMode: false,
25. themeColor: 'rgba(248, 249, 250, 1)',
26. themeBgImg: '',
27. flipMode: '0',
28. scaledDensity: display.getDefaultDisplaySync().scaledDensity > 0 ? display.getDefaultDisplaySync().scaledDensity :
29. 1,
30. viewPortWidth: 1260, // 视口宽度，需要根据设备实际情况获取，否则会导致阅读界面异常
31. viewPortHeight: 2720, // 视口高度，需要根据设备实际情况获取，否则会导致阅读界面异常
32. };

34. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
35. await this.readerComponentController.init(context);
36. this.readerComponentController.setPageConfig(readerSetting);
37. hilog.info(0x0000, 'testTag', `setPageConfig succeeded`);
38. }

40. build() {
41. Stack() {
42. ReadPageComponent({
43. controller: this.readerComponentController,
44. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
45. this.readerComponentController = data;
46. }
47. })
48. }.width('100%').height('100%')
49. }
50. }
```

### startPlay

PhonePC/2in1Tablet

startPlay(spineIndex: number, domPos: string): Promise<void>

以指定阅读进度打开书籍，使用Promise异步回调。

说明

startPlay接口需在[registerBookParser](reader-read-core.md#registerbookparser)事件成功触发后，才能调用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spineIndex | number | 是 | 内容资源索引[SpineItem](reader-book-parser.md#spineitem).index。 |
| domPos | string | 是 | 用户上次阅读进度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1016900002](reader-error-code.md#section1016900002) | Read Page Component is not initialized. |
| [1016900003](reader-error-code.md#section1016900003) | Invalid request. |
| [1016900999](reader-error-code.md#section1016900999) | Other error. |
| [1016910001](reader-error-code.md#section1016910001) | Invalid spine item. |
| [1016910002](reader-error-code.md#section1016910002) | Unexpected spine item resource data. |
| [1016910003](reader-error-code.md#section1016910003) | Spine item resource data out of range. |

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

11. aboutToAppear(): void {
12. this.startPlay();
13. }

15. private async startPlay() {
16. // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. let filePath: string = `${context.filesDir}/abc.epub`;
19. let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
20. let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
21. let spineIndex: number = spineList[0].index;
22. let domPos: string = '';

24. await this.readerComponentController.init(context);
25. this.readerComponentController.registerBookParser(bookParserHandler);
26. // 调用startPlay接口初始化书籍内容显示
27. this.readerComponentController.startPlay(spineIndex || 0, domPos);
28. hilog.info(0x0000, 'testTag', `startPlay succeeded`);
29. }

31. build() {
32. Stack() {
33. ReadPageComponent({
34. controller: this.readerComponentController,
35. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
36. this.readerComponentController = data;
37. }
38. })
39. }.width('100%').height('100%')
40. }
41. }
```

### flipPage

PhonePC/2in1Tablet

flipPage(isNext: boolean): void

触发[ReadPageComponent](reader-api-readpagecomponent.md#readpagecomponent)组件进行翻页。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNext | boolean | 是 | 是否翻到下一页。  - true：往下一页翻页。  - false：往上一页翻页。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1016900002](reader-error-code.md#section1016900002) | Read Page Component is not initialized. |
| [1016900003](reader-error-code.md#section1016900003) | Invalid request. |
| [1016900999](reader-error-code.md#section1016900999) | Other error. |

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.flipPage();
13. }

15. private async flipPage(){
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. await this.readerComponentController.init(context);
18. // 翻下一页
19. this.readerComponentController.flipPage(true);
20. hilog.info(0x0000, 'testTag', `flipPage succeeded`);
21. }

23. build() {
24. Stack() {
25. ReadPageComponent({
26. controller: this.readerComponentController,
27. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
28. this.readerComponentController = data;
29. }
30. })
31. }.width('100%').height('100%')
32. }
33. }
```

### releaseBook

PhonePC/2in1Tablet

releaseBook(): void

释放书籍资源，在退出阅读器等释放资源场景时使用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.releaseBook();
13. }

15. private async releaseBook(){
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. await this.readerComponentController.init(context);
18. // 释放加载书籍时的资源
19. this.readerComponentController.releaseBook();
20. hilog.info(0x0000, 'testTag', `releaseBook succeeded`);
21. }

23. build() {
24. Stack() {
25. ReadPageComponent({
26. controller: this.readerComponentController,
27. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
28. this.readerComponentController = data;
29. }
30. })
31. }.width('100%').height('100%')
32. }
33. }
```

### on('pageShow')

PhonePC/2in1Tablet

on(type: 'pageShow', callback: Callback<PageDataInfo>): void

注册页面展示的通知服务，该通知在页面排版成功展示后触发。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为“pageShow”。 |
| callback | Callback<[PageDataInfo](reader-read-core.md#pagedatainfo)> | 是 | 回调函数，返回内容分页排版信息。 |

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.registerListener();
13. }

15. private async registerListener(){
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. await this.readerComponentController.init(context)
18. // 此处只演示方法调用，实际触发回调，需要配合startPlay接口使用
19. this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
20. // 开发者可在此保存内容分布排版数据，利用data.resourceIndex及data.startDomPos数据调用startPlay接口继续阅读
21. hilog.info(0x0000, 'testTag', 'pageshow: data is: ' + JSON.stringify(data));
22. });
23. }

25. build() {
26. Stack() {
27. ReadPageComponent({
28. controller: this.readerComponentController,
29. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
30. this.readerComponentController = data;
31. }
32. })
33. }.width('100%').height('100%')
34. }
35. }
```

### off('pageShow')

PhonePC/2in1Tablet

off(type: 'pageShow', callback?: Callback<PageDataInfo>): void

注销章节内容分页展示结果回调，可在页面销毁时调用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为“pageShow”。 |
| callback | Callback<[PageDataInfo](reader-read-core.md#pagedatainfo)> | 否 | 回调函数，需要传[on('pageShow')](reader-read-core.md#onpageshow)注册时的回调函数，若不传则注销所有的回调函数。 |

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.unregisterListener();
13. }

15. private async unregisterListener(){
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. let readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
18. await readerComponentController.init(context);
19. readerComponentController.off('pageShow');
20. hilog.info(0x0000, 'testTag', `offPageShow succeeded`);
21. }

23. build() {
24. Stack() {
25. ReadPageComponent({
26. controller: this.readerComponentController,
27. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
28. this.readerComponentController = data;
29. }
30. })
31. }.width('100%').height('100%')
32. }
33. }
```

### on('resourceRequest')

PhonePC/2in1Tablet

on(type: 'resourceRequest', callback: bookParser.CallbackRes<string, ArrayBuffer>): void

注册资源请求回调，如果设置了自定义背景，字体时，排版引擎会通过此接口获取对应的资源ArrayBuffer。

说明

注册多个资源请求回调时，只会生效最后一个。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为“resourceRequest”。 |
| callback | bookParser.[CallbackRes](reader-book-parser.md#callbackres)<string, ArrayBuffer> | 是 | 回调函数，string：请求资源路径。ArrayBuffer：请求资源对应的二进制数据。 |

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
10. // 字体文件以实际文件名及路径为准
11. private selectFontPath = 'fonts/SourceHanSerifCN-VF.ttf';

13. aboutToAppear(): void {
14. this.registerListener();
15. }

17. private async registerListener(){
18. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
19. await this.readerComponentController.init(context);
20. // 此处只演示方法调用，实际触发回调，需要配合startPlay接口使用
21. this.readerComponentController.on('resourceRequest', this.resourceRequest);
22. }

24. private resourceRequest: bookParser.CallbackRes<string,ArrayBuffer> = (fileName: string): ArrayBuffer => {
25. if (this.isFont(fileName)) {
26. let res = $rawfile(this.selectFontPath);
27. let context = this.getUIContext().getHostContext();
28. if (res && context) {
29. // 获取资源路径下的字体数据
30. let value: Uint8Array = context.resourceManager.getRawFileContentSync(this.selectFontPath);
31. hilog.info(0x0000, 'testTag', 'resourceRequest : get success');
32. return value.buffer as ArrayBuffer;
33. }
34. }
35. return new ArrayBuffer(0);
36. }

38. private isFont(filePath: string): boolean {
39. let options = [".ttf", ".woff2", ".otf"];
40. let path = filePath.toLowerCase();
41. let result = path.indexOf(options[0]) != -1 || path.indexOf(options[1]) != -1 || path.indexOf(options[2]) != -1;
42. hilog.info(0x0000, 'testTag', 'isFont = ' + result);
43. return result;
44. }

46. build() {
47. Stack() {
48. ReadPageComponent({
49. controller: this.readerComponentController,
50. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
51. this.readerComponentController = data;
52. }
53. })
54. }.width('100%').height('100%')
55. }
56. }
```

### off('resourceRequest')

PhonePC/2in1Tablet

off(type: 'resourceRequest', callback?: bookParser.CallbackRes<string, ArrayBuffer>): void

注销资源请求回调接口，可在页面销毁时调用。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为“resourceRequest”。 |
| callback | bookParser.[CallbackRes](reader-book-parser.md#callbackres)<string, ArrayBuffer> | 否 | 回调函数，需要传[on('resourceRequest')](reader-read-core.md#onresourcerequest)注册时的回调函数，若不传则注销所有的回调函数。 |

**示例：**

```
1. import { readerCore, ReadPageComponent } from '@kit.ReaderKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Reader {
9. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

11. aboutToAppear(): void {
12. this.unregisterListener();
13. }

15. private async unregisterListener(){
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. await this.readerComponentController.init(context);
18. this.readerComponentController.off('resourceRequest');
19. hilog.info(0x0000, 'testTag', `offResourceRequest succeeded`);
20. }

22. build() {
23. Stack() {
24. ReadPageComponent({
25. controller: this.readerComponentController,
26. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
27. this.readerComponentController = data;
28. }
29. })
30. }.width('100%').height('100%')
31. }
32. }
```
