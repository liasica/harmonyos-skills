---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-read-page
title: 构建阅读器
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 构建阅读器
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:37a60973a0a407a1dccfcbe13b00b8bd10751d31344629249afdbe01c99e8284
---

Reader Kit提供的阅读页组件ReadPageComponent，支持对标准的txt和富文本内容（html+css）按仿真和横滑方式进行分页排版的能力、支持翻页阅读过程中所需要的进度和行为感知能力。利用ReadPageComponent，开发者可快速实现书籍阅读的能力。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/3698PzsrTEWjhuYg6Fn0VQ/zh-cn_image_0000002552799494.png?HW-CC-KV=V1&HW-CC-Date=20260427T235038Z&HW-CC-Expire=86400&HW-CC-Sign=31A8A671BA3C3B635BAF90B73AB268C973567F58EDF0061A158D3D7B50D63D60)

## 接口说明

构建书籍阅读能力共涉及5个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [getDefaultHandler](../harmonyos-references/reader-book-parser.md#getdefaulthandler)(path: string): Promise<BookParserHandler> | 获取书籍默认解析器。 |
| [init](../harmonyos-references/reader-read-core.md#init)(context: common.UIAbilityContext): Promise<void> | 初始化ReadPageComponent控制器。  初始化接口需要优先于ReaderComponentController的其他接口之前执行。 |
| [setPageConfig](../harmonyos-references/reader-read-core.md#setpageconfig)(pageConfig: ReaderSetting): void | 设置或者修改页面排版属性。 |
| [registerBookParser](../harmonyos-references/reader-read-core.md#registerbookparser)(bookParserHandler: bookParser.BookParserHandler): void | 注册书籍解析器。  需要在startPlay接口调用之前执行。 |
| [startPlay](../harmonyos-references/reader-read-core.md#startplay)(spineIndex: number, domPos: string): Promise<void> | 以指定阅读进度打开书籍，使用Promise异步回调。  需要在registerBookParser接口调用之后执行。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. // 导入解析能力、页面组件和阅读器控制类
   2. import { bookParser, ReadPageComponent, readerCore } from '@kit.ReaderKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { display } from '@kit.ArkUI';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   6. import { common } from '@kit.AbilityKit';
   ```
2. 初始化组件控制器、默认设置项，以及定义书籍解析器。

   ```
   1. // 组件控制器，用于调用排版相关能力。
   2. private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
   3. // 默认设置项，用于初始化阅读器页面的默认属性。
   4. private readerSetting: readerCore.ReaderSetting = {
   5. fontName: '系统字体',
   6. fontPath: '',
   7. fontSize: 18,
   8. fontColor: '#000000',
   9. fontWeight: 400,
   10. lineHeight: 1.9,
   11. nightMode: false,
   12. themeColor: 'rgba(248, 249, 250, 1)',
   13. themeBgImg: '',
   14. flipMode: '0',
   15. scaledDensity: display.getDefaultDisplaySync().scaledDensity > 0 ? display.getDefaultDisplaySync().scaledDensity :
   16. 1,
   17. viewPortWidth: 1260, // 视口宽度，需要根据设备实际情况获取，否则会导致阅读界面异常
   18. viewPortHeight: 2720, // 视口高度，需要根据设备实际情况获取，否则会导致阅读界面异常
   19. };
   20. // 书籍解析器，用于注册给组件控制器，供排版引擎调用。
   21. private bookParserHandler: bookParser.BookParserHandler | null = null;
   22. // 是否正在加载页面（需要等待页面渲染完成再隐藏，避免进入页面会先显示黑屏的问题）
   23. @State isLoading: boolean = true;
   ```
3. 构建ReadPageComponent组件，用于显示阅读内容。

   ```
   1. build() {
   2. Stack() {
   3. ReadPageComponent({
   4. controller: this.readerComponentController,
   5. readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
   6. this.readerComponentController = data;
   7. }
   8. })

   10. Row() {
   11. Text('加载中...')
   12. }
   13. .width('100%')
   14. .height('100%')
   15. .justifyContent(FlexAlign.Center)
   16. .backgroundColor(Color.White)
   17. .visibility(this.isLoading ? Visibility.Visible : Visibility.None)
   18. }.width('100%').height('100%')
   19. }
   ```
4. 通过提前导入到[应用沙箱目录](app-sandbox-directory.md)中的书籍文件，初始化书籍解析器。调用[startPlay](../harmonyos-references/reader-read-core.md#startplay)接口，以指定进度渲染阅读器页面。

   ```
   1. aboutToAppear(): void {
   2. // 初始化阅读器
   3. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   4. let filePath: string = `${context.filesDir}/abc.epub`;
   5. let spineIndex: number = 0;
   6. let domPos: string = '';
   7. this.registerListener();
   8. this.startPlay(filePath, spineIndex, domPos);
   9. }

   11. private registerListener(): void {
   12. this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
   13. hilog.info(0x0000, 'testTag', 'pageshow: data is: ' + JSON.stringify(data));
   14. if (data.state === readerCore.PageState.PAGE_ON_SHOW) {
   15. this.isLoading = false;
   16. }
   17. });
   18. }

   20. private async startPlay(filePath: string, spineIndex: number, domPos: string) {
   21. try {
   22. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   23. // 组件控制器初始化，用于控制ReadPageComponent调用排版引擎
   24. let initPromise = this.readerComponentController.init(context);
   25. // 初始化书籍解析器
   26. let bookParserHandler = bookParser.getDefaultHandler(filePath);
   27. let result: [bookParser.BookParserHandler, void] = await Promise.all([bookParserHandler, initPromise]);
   28. this.bookParserHandler = result[0];
   29. // 设置默认页面属性，用于排版的默认样式
   30. this.readerComponentController.setPageConfig(this.readerSetting);
   31. // 注册解析能力到控制器中，用于排版引擎的调用。
   32. this.readerComponentController.registerBookParser(this.bookParserHandler);
   33. // 调用打开书籍接口，跳章至对应进度
   34. this.readerComponentController.startPlay(spineIndex|| 0, domPos);
   35. } catch (err) {
   36. hilog.error(0x0000, 'testTag', 'startPlay: err: ' + JSON.stringify(err));
   37. }
   38. }

   40. aboutToDisappear(): void {
   41. this.readerComponentController.off('pageShow');
   42. // 退出需要释放阅读器实例
   43. this.readerComponentController.releaseBook();
   44. }
   ```
