---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-component
title: 预览PDF文档
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 预览PDF文档
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f99c58b3106018ee66598b597b8ade3e39f41a33f9794d90b5304c3b4b833ea0
---

PDF Kit提供了丰富的PDF文档预览能力，比如：

* 页面跳转
* 页面缩放
* 单双页显示
* 页面适配
* 滚动视图方式预览

详细说明及使用请参考：[PdfView](../harmonyos-references/pdf-arkts-pdfview-component.md#pdfview)组件。

## 示例代码

1. 导入相关模块。
2. 以下示例代码中以预览“input.pdf”文件名为例，此时需要确保在工程目录“src/main/resources/rawfile”里存在input.pdf文档，并且拷贝input.pdf文档到沙箱目录。
3. 调用loadDocument方法，加载PDF文档。
4. 调用PdfView预览组件，渲染显示。

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct PreviewPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    let dir: string = this.context.resourceDir
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath: string = dir + '/input.pdf';
    try {
      let res = fileIo.accessSync(filePath);
      if (!res) {
        let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('resfile/input.pdf');
        let fdSand = fileIo.openSync(
            filePath,
            fileIo.OpenMode.WRITE_ONLY |
            fileIo.OpenMode.CREATE |
            fileIo.OpenMode.TRUNC
        );
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'PreviewPage', `Code: ${error.code}, message: ${error.message} `);
    }
    (async () => {
      // 该监听方法只能在文档加载前调用一次
      this.controller.registerPageCountChangedListener((pageCount: number) => {
        hilog.info(0x0000, 'registerPageCountChanged-', pageCount.toString());
      });
      let loadResult1: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      // 注意：这里刚加载文档，请不要在这里立即设置PDF文档的预览方式
    })()
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')

         // ...
    }
    .width('100%').height('100%')
  }
}
```
