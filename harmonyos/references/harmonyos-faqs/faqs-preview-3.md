---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-3
title: Reader Kit如何进行小说章节跳转
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > Reader Kit如何进行小说章节跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:27+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f492ef36d582015e1ee2c2b7dd96556eb53a2a521fc537cdc91b0c54372c513b
---

## 问题现象

使用Reader Kit如何实现通过目录列表进行小说章节跳转？

## 背景知识

[Reader Kit（阅读服务）](../harmonyos-guides/reader-introduction.md)为开发者提供多种格式电子书的解析、排版、阅读交互能力，开发者可以借助Reader Kit的能力和组件快速构建书籍阅读能力。

* 提供多种格式书籍的解析能力：提供对txt、epub、mobi、azw、azw3格式书籍进行解析的能力，可获取书籍中的书名、作者、书封、目录、以及目录对应的正文内容。
* 提供txt、富文本内容排版能力：支持对标准的txt、富文本内容（html+css）按仿真和横滑方式进行分页排版，并提供排版快照和排版信息。
* [阅读页组件（ReadPageComponent）](../harmonyos-references/reader-api-readpagecomponent.md)：支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。

## 解决方案

通过[getDomPosByCatalogHref](../harmonyos-references/reader-book-parser.md#getdomposbycataloghref)获取domPos信息，通过[getSpineList](../harmonyos-references/reader-book-parser.md#getspinelist)得到Spine的列表再对比获得对应章节的spineIndex。最后使用[startPlay](../harmonyos-references/reader-read-core.md#startplay)完成跳转。

```ts
import { display } from '@kit.ArkUI';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ReadPageComponent, readerCore, bookParser } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';

const TAG: string = 'ReaderKitJumpCatalogItem';

@Entry
@Component
struct Index {
  private defaultHandler: bookParser.BookParserHandler | null = null;
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();
  /**
   * Display dialog box
   */
  @State showModalBanner: boolean = false;
  /**
   * Menu bar type index, 0 : catalog list, 1 : setting, 1 : close dialog
   */
  @State currentIndex: number = -1;
  @State catalogItemList: bookParser.CatalogItem[] = [];
  @State bookTitle: string = '';

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
      fileIo.close(file.fd).catch(() => {
        hilog.error(0x0000, TAG, `file close failed`);
      });
    } catch (err) {
      let e = err as BusinessError;
      hilog.error(0x0000, TAG,`copy book rawfile to sanbox failed: code = ${e.code}, message = ${e.message}`);
    }

    return bookSandBoxPath;
  }

  aboutToAppear(): void {
    // 代码正常运行需要在entry\src\main\resources\rawfile目录下新增名称为test.txt的小说文本文件
    let filePath = this.copyRawfileToSanBox(this.getUIContext().getHostContext() as common.UIAbilityContext, 'test.txt');
    let resourceIndex = 0;
    let domPos = '';
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
      this.readerComponentController.startPlay(resourceIndex || 0, domPos).catch(() => {
        hilog.error(0x0000, TAG, `startPlay failed`);
      });
    } catch (err) {
      hilog.error(0x0000, TAG, `startPlay: err: + ${JSON.stringify(err)}`);
    }
  }

  private async getBookInfo() {
    try {
      let bookInfo: bookParser.BookInfo | undefined = this.defaultHandler?.getBookInfo();
      if (bookInfo) {
        this.bookTitle = bookInfo.bookTitle || '';
      }
      hilog.info(0x0000, TAG, 'getBookInfo bookInfo is: ' + JSON.stringify(bookInfo));
    } catch (error) {
      hilog.error(0x0000, TAG, `getBookInfo failed, Code: ${error.code}, message: ${error.message}`);
    }
  }

  private showModal() {
    this.showModalBanner = true;
  }

  private closeModal() {
    this.showModalBanner = false;
    this.currentIndex = -1;
  }

  private jumpToCatalogList() {
    this.currentIndex = 0;
    try {
      this.catalogItemList = this.defaultHandler?.getCatalogList() || [];
    } catch (error) {
      hilog.error(0x0000, TAG, `getCatalogList failed, Code: ${error.code}, message: ${error.message}`);
    }
    this.getBookInfo();
    hilog.info(0x0000, TAG, 'catalog list length: ' + this.catalogItemList.length);
  }

  // 跳转目录函数
  private async jumpToCatalogItem(catalogItem: bookParser.CatalogItem) {
    const domPos = await this.getDomPos(catalogItem);
    const resourceIndex = this.getResourceItemByCatalog(catalogItem).index;
    this.readerComponentController.startPlay(resourceIndex, domPos).catch(() => {
      hilog.error(0x0000, TAG, `startPlay failed`);
    });
    this.closeModal();
  }

  // 获取dompos
  private async getDomPos(catalogItem: bookParser.CatalogItem): Promise<string> {
    try {
      const domPos: string = this.defaultHandler?.getDomPosByCatalogHref(catalogItem.href || '') || '';
      return domPos;
    } catch (error) {
      hilog.error(0x0000, TAG, `getDomPos failed, Code: ${error.code}, message: ${error.message}`);
    }
    return Promise.reject();
  }

  // 获取spineIndex
  private getResourceItemByCatalog(catalogItem: bookParser.CatalogItem): bookParser.SpineItem {
    let resourceFile = catalogItem.resourceFile || '';
    try {
      let spineList: bookParser.SpineItem[] = this.defaultHandler?.getSpineList() || [];
      let resourceItemArr = spineList.filter(item => item.href === resourceFile);
      if (resourceItemArr.length > 0) {
        hilog.info(0x0000, TAG, 'getResourceItemByCatalog get resource ', resourceItemArr[0]);
        let resourceItem = resourceItemArr[0];
        return resourceItem;
      } else if (spineList.length > 0) {
        hilog.info(0x0000, TAG, 'getResourceItemByCatalog get resource in resourceList', spineList[0]);
        return spineList[0];
      }
    } catch (error) {
      hilog.error(0x0000, TAG, `getSpineList failed, Code: ${error.code}, message: ${error.message}`);
    }
    hilog.info(0x0000, TAG, 'getResourceItemByCatalog get resource in escape');
    return {
      idRef: '',
      index: 0,
      href: '',
      properties: ''
    };
  }

  aboutToDisappear(): void {
    try {
      display.off('change', this.screenDensityCallBack);
    } catch (error) {
      hilog.error(0x0000, TAG, `display.off change failed, Code: ${error.code}, message: ${error.message}`);
    }
    this.readerComponentController.off('pageShow');
    this.readerComponentController.releaseBook();
  }

  // 目录列表
  @Builder
  private buildCatalogItemList() {
    Column() {
      Row() {
        Text(this.bookTitle)
          .maxLines(1)
          .margin({ right: 12, left: 12 })
          .fontWeight(FontWeight.Bold)
          .flexShrink(1)
          .height(40)
          .visibility(this.bookTitle ? Visibility.Visible : Visibility.None)
      }
      .padding({
        left: 16,
        right: 16
      })
      .width('100%')
      .margin({ bottom: 20 })
      .alignSelf(ItemAlign.Start)

      List() {
        ForEach(this.catalogItemList, (item: bookParser.CatalogItem) => {
          ListItem() {
            Column() {
              Row() {
                Row() {
                  Text(' · ')
                    .fontSize(14)
                  Text(item.catalogName)
                    .fontSize(14)
                    .textOverflow({ overflow: TextOverflow.Ellipsis })
                    .padding({ top: 8, bottom: 8 })
                    .maxLines(2)
                    .layoutWeight(1)
                }
              }
              .width('100%')
              .height(48)
              .justifyContent(FlexAlign.Center)
              .alignItems(VerticalAlign.Center)

              Divider()
            }
            .padding({
              left: item.catalogLevel ? item.catalogLevel * 26 : 16,
              right: 16,
              top: 6,
              bottom: 6
            })
            .onClick(async () => {
              this.jumpToCatalogItem(item);
            })
          }
        })
      }
      .scrollBar(BarState.Off)
      .width('100%')
      .height('100%')
    }
    .borderRadius({ topRight: 32, topLeft: 32 })
    .visibility(this.currentIndex === 0 ? Visibility.Visible : Visibility.None)
    .backgroundColor(Color.White)
    .zIndex(3)
  }

  build() {
    Stack() {
      Column(){
        Text('注：本文由AI生成无任何版权纠纷！')
          .fontSize(14)
          .zIndex(2)
          .position({x:30, y:90})
          .fontColor('rgba(0, 0, 0, 0.5)')

        ReadPageComponent({
          controller: this.readerComponentController,
          readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
            this.readerComponentController = data;
            hilog.error(0x0000, TAG, `ReadPageComponent: err: + ${JSON.stringify(err)}`);
          }
        })
          .position({y:20})
          .zIndex(1)
        Column() {
          Column() {
            Column() {
              // 目录列表显示
              this.buildCatalogItemList();
            }
            .padding({ bottom: 100 })
            .backgroundColor(Color.White)
          }
          .visibility(this.currentIndex < 0 ? Visibility.None : Visibility.Visible)
          .width('100%')
          .height(this.currentIndex === 0 ? 'calc(100%  - 80vp - 56vp)' : '60%')
          .justifyContent(FlexAlign.End)
          .onClick(() => {
            this.showModalBanner = true;
          })

          Row() {
            Text('目录')
              .width('100%')
              .height('100%')
              .onClick(() => {
                this.jumpToCatalogList();
              })
              .textAlign(TextAlign.Center)
          }
          .width('100%')
          .height(80)
          .backgroundColor(Color.White)
        }
        .width('100%')
        .height('100%')
        .backgroundColor(this.currentIndex === 0 ? '#0d626262' : Color.Transparent)
        .zIndex(this.showModalBanner ? 3 : 0)
        .justifyContent(FlexAlign.End)
        .onClick(() => {
          this.closeModal();
        })
      }
      .height('100%')
      .width('100%')
      .zIndex(3)
    }.width('100%').height('100%').onClick(() => {
      this.showModal();
    })
  }
}
```

**说明** 

代码正常运行需要在“entry\src\main\resources\rawfile”目录下新增名称为test.txt的小说文本文件。

## 总结

[bookParser（书籍解析能力）](../harmonyos-references/reader-book-parser.md)提供了小说目录信息解析功能。[readerCore（阅读核心能力）](../harmonyos-references/reader-read-core.md)提供了目录跳转功能。两者共同完成阅读器章节显示和跳转功能，方便使用者能够选择自己想看的章节。
