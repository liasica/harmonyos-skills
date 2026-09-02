---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-delete-page
title: 添加、删除PDF页
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除PDF页
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:60b19e92c404417487a593999c83b8e0fd8e25d0b0379b69278b9727aa5fd1b1
---

在PDF文档中添加或删除页面，包括：

* 添加单个、多个空白页到PDF文档。
* 删除PDF文档中单个、多个指定页。
* 将其他PDF文档页添加到本PDF文档。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [insertBlankPage](../harmonyos-references/pdf-arkts-pdfservice.md#insertblankpage)(index: number, width: number, height: number): PdfPage | 在指定位置插入空白PDF页。 |
| [getPage](../harmonyos-references/pdf-arkts-pdfservice.md#getpage)(index: number): PdfPage | 获取指定页的对象。 |
| [insertPageFromDocument](../harmonyos-references/pdf-arkts-pdfservice.md#insertpagefromdocument)(document: PdfDocument, fromIndex: number, pageCount: number, index: number): PdfPage | 将其他文档的页添加到当前文档。 |
| [deletePage](../harmonyos-references/pdf-arkts-pdfservice.md#deletepage)(index: number, count: number): void | 删除指定的PDF页。 |

## 示例代码

1. 调用loadDocument方法，加载PDF文档。
2. 调用getPage方法获取当前页，用于获取页面宽高。
3. 调用insertBlankPage和insertPageFromDocument方法实现如下功能。

   1. 插入单个空白页。
   2. 插入多个空白页。
   3. 将input2.pdf文档的索引1、2、3页插入到input.pdf索引0的位置，并另存文档。
4. 调用deletePage方法删除单个或多个索引页。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...

@Entry
@Component
struct PageManagementPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    this.pdfDocument.loadDocument(filePath);
  }

  build() {
    Column() {
    // ...
        Button('insertBlankPage').onClick(async () => {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let page2: pdfService.PdfPage = this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
          let outPdfPath = this.context.filesDir + '/testInsertBlankPage.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PageManagementPage', 'insertBlankPage %{public}s!', result ? 'success' : 'fail');
        })
        // 插入多个空白页
        Button('insertSomeBlankPage').onClick(async () => {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          for (let i = 0; i < 3; i++) {
            this.pdfDocument.insertBlankPage(2, page.getWidth(), page.getHeight());
          }
          let outPdfPath = this.context.filesDir + '/testInsertSomeBlankPage.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PageManagementPage', 'insertSomeBlankPage %{public}s!', result ? 'success' : 'fail');
        })
        // 将input2.pdf文档的索引1,2,3页插入到input.pdf索引0的位置，并另存文档
        Button('insertPageFromDocument').onClick(async () => {
          let pdfDoc: pdfService.PdfDocument = new pdfService.PdfDocument();
          // 确保在工程目录src/main/resources/resfile里有input2.pdf文档
          pdfDoc.loadDocument(this.context.resourceDir + '/input2.pdf');
          this.pdfDocument.insertPageFromDocument(pdfDoc, 1, 3, 0);
          let outPdfPath = this.context.filesDir + '/testInsertPageFromDocument.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PageManagementPage', 'insertPageFromDocument %{public}s!', result ? 'success' : 'fail');
        })
        // 删除单个或多个索引页
        Button('deletePage').onClick(async () => {
          this.pdfDocument.deletePage(2, 2);
          let outPdfPath = this.context.filesDir + '/testDeletePage.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PageManagementPage', 'deletePage %{public}s!', result ? 'success' : 'fail');

        })
        // ...
    }
  }
}
```
