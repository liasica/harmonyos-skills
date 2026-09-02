---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-switch-optimize
title: 优化PDF文档切换体验
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 优化PDF文档切换体验
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:724ecb3a6fdddc4bcad1b9a47d78a7d08755fefe0705cd5ad6eb65c13652df77
---

## 场景介绍

在应用中进行多文档切换时，为了提供更加流畅和清晰的视觉体验，推荐结合状态管理来控制PdfView的渲染时机。

通过引入加载状态，可以在文档加载过程中暂时隐藏预览组件并展示加载动画，待loadDocument异步加载完成且页面布局准备就绪后，再展示清晰的文档内容。这种方式能有效优化切换过程中的视觉跳变，提升交互质感。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadDocument](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)(path: string, password?: string, initPageIndex?: number, onProgress?: Callback<number>): Promise<pdfService.ParseResult> | 加载PDF文档。 |
| [setPageFit](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagefit)(pageFit: pdfService.PageFit): void | 设置页面的适配模式。 |

## 示例代码

1. 定义@State变量isLoading，用于标记文档的加载状态，并以此控制PdfView组件的挂载与显示。
2. 将isLoading置为true，显示Loading界面；待异步加载成功后，再将isLoading置为false，展示PDF视图。
3. 通过调用loadDocument加载不同的文件路径，实现PDF文件的切换。

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@ohos.base';
// ...

const DOMAIN: number = 0x0000;
const TAG: string = 'SwitchDocumentDemo';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private filePath1: string = '';
  private filePath2: string = '';
  private switchFlag: boolean = true; // true，加载pdf1；false，加载pdf2
  @State isLoading: boolean = false;
  @State isSwitching: boolean = false;

  private makeSureFileExist(filePath: string): void {
    let fileName: string = filePath.split('/').pop() || '';
    try {
      let context = this.getUIContext().getHostContext() as Context;
      let res = fileIo.accessSync(filePath);
      if (!res) {
        let content: Uint8Array = context.resourceManager.getRawFileContentSync(`rawfile/${fileName}`);
        let fdSand =
          fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      hilog.error(DOMAIN, TAG, `Code: ${error.code}, message: ${error.message} `);
    }
  }

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.resourceDir
    hilog.error(DOMAIN, TAG, `local change: Controller load PDF failed, dir:${dir}`);
    // dir:/data/storage/el2/base/haps/entry/files
    // 确保工程目录src/main/resources/resfile内有pdf1.pdf、pdf2.pdf文档
    this.filePath1 = dir + '/pdf1.pdf';
    this.filePath2 = dir + '/pdf2.pdf';
    this.makeSureFileExist(this.filePath1);
    this.makeSureFileExist(this.filePath2);

    (async () => {
      let filePath: string = this.switchFlag ? this.filePath1 : this.filePath2;
      this.isLoading = true;
      let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      this.isLoading = false;
      if (loadResult !== pdfService.ParseResult.PARSE_SUCCESS) {
        hilog.error(DOMAIN, TAG, 'Controller load PDF failed');
        return;
      }
    })();
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      if (!this.isLoading) {
        PdfView({
          controller: this.controller,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: false
        })
          .width('100%')
          .height('100%')
      } else {
        // 此处可自定义loading界面
      }
      // ...
      Button('SwitchDocument')
        .position({ x: 10, y: 60 })
        .onClick(async () => {
          if (this.isSwitching) {
            return;
          }
          this.isSwitching = true;
          this.switchFlag = !this.switchFlag;
          let filePath: string = this.switchFlag ? this.filePath1 : this.filePath2;
          this.controller.releaseDocument();
          this.isLoading = true;
          let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
          this.isLoading = false;
          this.isSwitching = false;
          if (loadResult !== pdfService.ParseResult.PARSE_SUCCESS) {
            hilog.error(DOMAIN, TAG, 'Controller load PDF failed');
            return;
          }
          this.controller.setPageFit(pdfService.PageFit.FIT_WIDTH);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
