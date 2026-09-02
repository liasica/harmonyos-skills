---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-open
title: 打开和保存PDF文档
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 打开和保存PDF文档
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5474e3af559c495b37d94f2e3348f87c12071ea517f0b84cc5e6e3f38a14601d
---

## 场景介绍

通过加载本地路径的PDF文档，实现打开PDF文档的预览功能。当PDF文档做了批注等相关的信息时，可以使用保存功能。

和pdfService的打开和保存能力相同，具体区别查看pdfService的[打开和保存PDF文档](pdf-open-document.md)的场景介绍。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadDocument](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult> | 加载PDF文档。 |
| [saveDocument](../harmonyos-references/pdf-arkts-pdfviewmanage.md#savedocument)(path: string, onProgress?: Callback<number>): Promise<number> | 保存PDF文档，使用Promise异步回调。 |

## 示例代码

1. 在aboutToAppear函数里面加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在【savePdfDocument】按钮中调用saveDocument方法另存PDF文档。

```typescript
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
 // ...

@Entry
@Component
struct PdfOpenDocument {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  build() {
   // ...
      Column() {
        Button('savePdfDocument').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            let savePath = this.context.filesDir + '/savePdfDocument.pdf';
            let result = await this.controller.saveDocument(savePath);
            hilog.info(0x0000, 'PdfPage', 'savePdfDocument %{public}s!', result ? 'success' : 'fail');
          }
        })
        PdfView({
          controller: this.controller,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1);
      }
      // ...
    .width('100%')
    .height('100%')
  }
}
```
