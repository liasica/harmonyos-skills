---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-reader-1
title: Reader Kit获取书籍具体页数
breadcrumb: FAQ > 应用服务开发 > 电子书阅读服务（Reader Kit） > Reader Kit获取书籍具体页数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a29e1ce0cc88b83130808d5809c7e906e68ab80503a86a03388e6a2b39e3e1f1
---

## 问题现象

用Reader kit服务的相关API能够正常展示书籍，但是如果想定位到书籍具体章节具体页数，应该如何定位？

## 背景知识

[Reader Kit（阅读服务）](../harmonyos-guides/reader-introduction.md)为开发者提供多种格式电子书的解析、排版、阅读交互能力，开发者可以借助Reader Kit的能力和组件快速构建书籍阅读能力。

* 提供多种格式书籍的解析能力：提供对txt、epub、mobi、azw、azw3格式书籍进行解析的能力，可获取书籍中的书名、作者、书封、目录、以及目录对应的正文内容。
* 提供txt、富文本内容排版能力：支持对标准的txt、富文本内容（HTML+CSS）按仿真和横滑方式进行分页排版，并提供排版快照和排版信息。
* [阅读页组件（ReadPageComponent）](../harmonyos-references/reader-api-readpagecomponent.md)：支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。

## 解决方案

使用ReaderComponentController的[on('pageShow')](../harmonyos-references/reader-read-core.md#onpageshow)事件回调，并在回调函数中进行对具体页数的处理。

```ts
import { display } from '@kit.ArkUI';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

import { ReadPageComponent, readerCore, bookParser } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';

const TAG: string = 'ReaderKitGetPageNumber';

@Entry
@Component
struct Index {
  private defaultHandler: bookParser.BookParserHandler | null = null;
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
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
    viewPortWidth: 1216,
    viewPortHeight: 2688,
  };
  private screenDensityCallBack: Callback<number> | null = null;

  copyRawfileToSanBox(context: common.UIAbilityContext, bookName: string): string {
    let bookSandBoxPath = context.filesDir + '/' + bookName;
    try {
      let data = context.resourceManager.getRawFileContentSync(bookName);
      let buffer = data.buffer;
      let file = fileIo.openSync(bookSandBoxPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
      fileIo.writeSync(file.fd, buffer);
      fileIo.close(file.fd);
    } catch (err) {
      let e = err as BusinessError;
      hilog.error(0x0000, TAG, `copy book rawfile to sanbox failed: code = ${e.code}, message = ${e.message}`);
    }

    return bookSandBoxPath;
  }

  private registerListener(): void {
    this.readerComponentController.on('pageShow', (data: readerCore.PageDataInfo): void => {
      // 开发者可在此保存内容分布排版数据，利用data.resourceIndex及data.startDomPos数据调用startPlay接口继续阅读
      hilog.info(0x0000, TAG, `当前的domPos ${data.startDomPos}`);
      hilog.info(0x0000, TAG, `pageshow: 当前页数data is: ${JSON.stringify(data)}`);
    });
  }

  aboutToAppear(): void {
    let filePath =
      this.copyRawfileToSanBox(this.getUIContext().getHostContext() as common.UIAbilityContext, 'test.txt');
    let resourceIndex = 0;
    let domPos = '';
    this.registerListener();
    this.startPlay(filePath, resourceIndex, domPos);
  }

  private async startPlay(path: string, resourceIndex: number, domPos: string) {
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let initPromise: Promise<void> = this.readerComponentController.init(context);
      let defaultHandler: Promise<bookParser.BookParserHandler> = bookParser.getDefaultHandler(path);
      let result: [bookParser.BookParserHandler, void] = await Promise.all([defaultHandler, initPromise]);
      this.defaultHandler = result[0];
      this.readerComponentController.registerBookParser(this.defaultHandler);
      this.readerComponentController.setPageConfig(this.readerSetting);
      this.readerComponentController.startPlay(resourceIndex || 0, domPos);
    } catch (err) {
      hilog.error(0x0000, TAG, `startPlay: err: + ${JSON.stringify(err)}`);
    }
  }

  aboutToDisappear(): void {
    display.off('change', this.screenDensityCallBack);
    this.readerComponentController.off('pageShow');
    this.readerComponentController.releaseBook();
  }

  build() {
    Stack() {
      Text('注：本文由AI生成无任何版权纠纷！')
        .fontSize(14)
        .zIndex(2)
        .position({ x: 30, y: 90 })
        .fontColor('rgba(0, 0, 0, 0.5)');

      Column() {
        ReadPageComponent({
          controller: this.readerComponentController,
          readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
            this.readerComponentController = data;
            hilog.error(0x0000, TAG, `ReadPageComponent: err: + ${JSON.stringify(err)}`);
          }
        })
          .position({ y: 20 });
      }
      .height('100%')
      .width('100%')
      .zIndex(1);

    }.width('100%').height('100%');
  }
}
```

## 总结

用上述方法可以将阅读进度实时保存到数据库当中，防止用户异常退出阅读器时的进度丢失。当用户下次继续阅读时，可将保存domPos及resourceIndex属性传入到startPlay接口中，用于阅读进度的恢复。
