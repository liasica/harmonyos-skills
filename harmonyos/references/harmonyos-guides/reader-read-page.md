---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-read-page
title: 构建阅读器
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 构建阅读器
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9953bce3793c56862a3a6e963e9b798dc4784f24ad7a9c2cf923ca786f143b6f
---

Reader Kit提供的阅读页组件ReadPageComponent，支持对标准的txt和富文本内容（html+css）按仿真和横滑方式进行分页排版的能力、支持翻页阅读过程中所需要的进度和行为感知能力。利用ReadPageComponent，开发者可快速实现书籍阅读的能力。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/UB9hzF7jRO2VGAR2Dx52yg/zh-cn_image_0000002706675232.png)

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

   ```typescript
   // 导入解析能力、页面组件和阅读器控制类
   import { bookParser, ReadPageComponent, readerCore } from '@kit.ReaderKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { display } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 初始化组件控制器、默认设置项，以及定义书籍解析器。

   ```typescript
   // 组件控制器，用于调用排版相关能力。
   private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
   // 默认设置项，用于初始化阅读器页面的默认属性。
   private readerSetting: readerCore.ReaderSetting = {
     fontName: '系统字体',
     fontPath: '',
     fontSize: 18,
     fontColor: '#000000',
     fontWeight: 400,
     lineHeight: 1.9,
     nightMode: false,
     themeColor: 'rgba(248, 249, 250, 1)',
     themeBgImg: '',
     flipMode: '0',
     scaledDensity: display.getDefaultDisplaySync().scaledDensity > 0 ? display.getDefaultDisplaySync().scaledDensity :
       1,
     viewPortWidth: 1260, // 视口宽度，需要根据设备实际情况获取，否则会导致阅读界面异常
     viewPortHeight: 2720 // 视口高度，需要根据设备实际情况获取，否则会导致阅读界面异常
   };
   // 书籍解析器，用于注册给组件控制器，供排版引擎调用。
   private bookParserHandler: bookParser.BookParserHandler | null = null;
   // 是否正在加载页面（需要等待页面渲染完成再隐藏，避免进入页面会先显示黑屏的问题）
   @State isLoading: boolean = true;
   ```
3. 构建ReadPageComponent组件，用于显示阅读内容。

   ```typescript
   build() {
     Stack() {
       ReadPageComponent({
         controller: this.readerComponentController,
         readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
           this.readerComponentController = data;
         }
       })

       Row() {
         Text('加载中...')
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
       .backgroundColor(Color.White)
       .visibility(this.isLoading ? Visibility.Visible : Visibility.None)
     }.width('100%').height('100%')
   }
   ```
4. 通过提前导入到[应用沙箱目录](app-sandbox-directory.md)中的书籍文件，初始化书籍解析器。调用[startPlay](../harmonyos-references/reader-read-core.md#startplay)接口，以指定进度渲染阅读器页面。

   ```typescript
   aboutToAppear(): void {
     // 初始化阅读器
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let filePath: string = `${context.filesDir}/abc.epub`;
     let spineIndex: number = 0;
     let domPos: string = '';
     this.registerListener();
     this.startPlay(filePath, spineIndex, domPos);
   }

   private registerListener(): void {
     this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
       hilog.info(0x0000, 'testTag', 'pageshow: data is: ' + JSON.stringify(data));
       if (data.state === readerCore.PageState.PAGE_ON_SHOW) {
         this.isLoading = false;
       }
     });
   }

   private async startPlay(filePath: string, spineIndex: number, domPos: string) {
     try {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       // 组件控制器初始化，用于控制ReadPageComponent调用排版引擎
       let initPromise = this.readerComponentController.init(context);
       // 初始化书籍解析器
       let bookParserHandler = bookParser.getDefaultHandler(filePath);
       let result: [bookParser.BookParserHandler, void] = await Promise.all([bookParserHandler, initPromise]);
       this.bookParserHandler = result[0];
       // 设置默认页面属性，用于排版的默认样式
       this.readerComponentController.setPageConfig(this.readerSetting);
       // 注册解析能力到控制器中，用于排版引擎的调用。
       this.readerComponentController.registerBookParser(this.bookParserHandler);
       // 调用打开书籍接口，跳章至对应进度
       this.readerComponentController.startPlay(spineIndex|| 0, domPos);
     } catch (err) {
       hilog.error(0x0000, 'testTag', 'startPlay: err: ' + JSON.stringify(err));
     }
   }

   aboutToDisappear(): void {
     this.readerComponentController.off('pageShow');
     // 退出需要释放阅读器实例
     this.readerComponentController.releaseBook();
   }
   ```
