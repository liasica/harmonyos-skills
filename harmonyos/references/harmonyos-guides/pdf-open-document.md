---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-open-document
title: 打开和保存PDF文档
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 打开和保存PDF文档
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3521f52ee704f740d5aafaa3b2976ba7758fd60fa97bfedb1ba28f2bcc541857
---

对PDF文档[添加内容](pdf-add-txt-img-annot.md)、[页眉页脚](pdf-add-headerfooter.md)、[水印](pdf-add-watermark.md)、[背景图片](pdf-add-background.md)或[书签](pdf-add-bookmark.md)等操作前，需要打开文档，并且在文档操作完成后，保存PDF文档。

pdfService和PdfView都可实现打开和保存文档，使用场景上有如下区别：

* 需要对PDF文档做相关的编辑和操作，建议使用pdfService的能力打开和保存文档。
* 需要预览、搜索关键字、监听PDF文档回调和批注等操作，推荐使用PdfView打开。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadDocument](../harmonyos-references/pdf-arkts-pdfservice.md#loaddocument)(path: string, password?: string, onProgress?: (progress: number) => number): ParseResult | 加载指定文档路径。 |
| [saveDocument](../harmonyos-references/pdf-arkts-pdfservice.md#savedocument)(path: string, onProgress?: (progress: number) => number): boolean | 保存文档。 |

## 示例代码

1. 调用loadDocument方法，加载PDF文档。
2. 在【Save As】和【Save】两个按钮中调用saveDocument方法，分别实现了另存为PDF文档和保存覆盖源PDF文档的两种方式。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct OpenDocument {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;
  private filePath = '';
  @State saveEnable: boolean = false;

  aboutToAppear(): void {
    this.filePath = this.context.filesDir + '/input.pdf';
    try {
      let res = fileIo.accessSync(this.filePath);
      if(!res) {
        // 确保在工程目录src/main/resources/resfile里有input.pdf文档
        let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('resfile/input.pdf');
        let fdSand =
          fileIo.openSync(this.filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
      this.pdfDocument.loadDocument(this.filePath);
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'OpenDocument', `Failed to loadDocument. Code: ${error.code}, message: ${error.message} `);
    }
  }

  build() {
    Column() {
      Row() {
      // ...
        Button('Save As').onClick(() => {
          let outPdfPath = this.context.filesDir + '/testSaveAsPdf.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          this.saveEnable = true;
          hilog.info(0x0000, 'OpenSavePage', 'saveAsPdf %{public}s!', result ? 'success' : 'fail');
        })
        Button('Save').enabled(this.saveEnable).onClick(() => {
          // 这里可以对PDF文档添加内容、页眉页脚、水印、背景等一些内容，然后保存文档
          let tempDir = this.context.tempDir;
          let tempFilePath = tempDir + `/temp${Math.random()}.pdf`;
          try {
            fileIo.copyFileSync(this.filePath, tempFilePath);
          } catch (e) {
            let error: BusinessError = e as BusinessError;
            hilog.error(0x0000, 'OpenSavePage', `Failed to copyFileSync. Code: ${error.code}, message: ${error.message} `);
          }
          let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
          // 加载临时文档
          let loadResult = pdfDocument.loadDocument(tempFilePath, '');
          if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            let result = pdfDocument.saveDocument(this.filePath);
            hilog.info(0x0000, 'OpenSavePage', 'savePdf %{public}s!', result ? 'success' : 'fail');
          }
        })
      }
    }
  }
}
```
