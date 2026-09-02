---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-11
title: PDFService.searchKey如何获取关键字数量和所属页码
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PDFService.searchKey如何获取关键字数量和所属页码
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:24+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:22873d7999c1d63fd4698f37e385208b0b1702a1c807fbe92a693aa6b0c40336
---

## 问题现象

使用PDFService.searchKey方法搜索关键字，如何获取关键字数量和所属页码？

## 背景知识

pdfViewManager（PDF预览），本模块为应用提供统一的PDF预览能力。

* [searchKey](../harmonyos-references/pdf-arkts-pdfviewmanage.md#searchkey)搜索文本并返回匹配的总数。
* [setSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setsearchindex)设置搜索匹配结果的索引，页面会跳转到索引对应搜索结果处。
* [getPageIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getpageindex)获取PDF当前页的索引。

## 解决方案

1. 拷贝rawfile目录PDF文件到沙箱中。
2. 根据关键字搜索文本并返回匹配的总数。

   ```ts
   this.controller.searchKey('XXX', (total: number) => {// 执行关键字搜索
     hilog.info(0x0000, 'PdfSearch', '匹配总数：%{public}d', total);
     for (let i = 0; i < total; i++) {// 遍历所有搜索结果获取页码
       this.controller.setSearchIndex(i);
       const currentPage = this.controller.getPageIndex();
       hilog.info(0x0000, 'PdfSearch',
         '第%{public}d个匹配项位于第%{public}d页', i + 1, currentPage + 1);
     }
   });
   ```
3. 跳转索引对应搜索结果处页面并返回页面索引。

   ```ts
   for (let i = 0; i < total; i++) {// 遍历所有搜索结果获取页码
     this.controller.setSearchIndex(i);
     const currentPage = this.controller.getPageIndex();
     hilog.info(0x0000, 'PdfSearch',
       '第%{public}d个匹配项位于第%{public}d页', i + 1, currentPage + 1);
   }
   ```

完整示例代码如下：

```ts
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { promptAction } from '@kit.ArkUI';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PdfSearchExample {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  async aboutToAppear(): Promise<void> {
    try {
      //确保rawfile目录下有pdf文件
      await this.copyRawFileToSdcard(this.context, 'test.pdf');
      promptAction.openToast({ message: '全部拷贝完成' });
      const filePath = `${this.context.filesDir}/test.pdf`;
      this.controller.loadDocument(filePath).then((result) => {
        this.loadResult = result;
      });
    } catch (error) {
      promptAction.openToast({ message: '文件拷贝失败' });
    }
  }

  build() {
    Column() {
      Button('搜索关键字')
        .onClick(() => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            this.controller.searchKey('XXX', (total: number) => {// 执行关键字搜索
              hilog.info(0x0000, 'PdfSearch', '匹配总数：%{public}d', total);
              for (let i = 0; i < total; i++) {// 遍历所有搜索结果获取页码
                this.controller.setSearchIndex(i);
                const currentPage = this.controller.getPageIndex();
                hilog.info(0x0000, 'PdfSearch',
                  '第%{public}d个匹配项位于第%{public}d页', i + 1, currentPage + 1);
              }
            });
          }
        })

      PdfView({ controller: this.controller })
        .width('100%')
        .height('80%')
    }
  }

  // 拷贝pdf文件到应用沙箱目录
  private copyRawFileToSdcard(context: common.Context, pdfName: string): Promise<void> {
    return new Promise((resolve) => {
      let destRoot = context.filesDir;
      // rawfile下的文件名
      let srcFileName = pdfName;
      let destFilePath = `${destRoot}/${srcFileName}`;
      context.resourceManager.getRawFileContent(srcFileName, (error: BusinessError, data: Uint8Array) => {
        if (error) {
          promptAction.openToast({ message: '拷贝失败' });
          hilog.error(0x0000, 'PdfCopy', `Copy failed: ${error.code}`);
          return;
        }
        const fileStream = fs.createStreamSync(destFilePath, 'w+');
        fileStream.writeSync(data.buffer);
        fileStream.close();
        promptAction.openToast({ message: '拷贝成功' });
        resolve();
      });
    });
  }
}
```

**说明** 

确保工程项目rawfile目录下有PDF文件。
