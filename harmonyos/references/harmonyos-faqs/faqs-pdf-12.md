---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-12
title: PdfView如何禁用缩放
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PdfView如何禁用缩放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d570a67e2c55f32ef4567ab25456a06b315c684f67a9a427545c8cc5c43067cf
---

## 问题现象

[PdfView](../harmonyos-references/pdf-arkts-pdfview-component.md#pdfview)组件如何禁用缩放功能，不允许进行放大和缩小。

## 背景知识

PDF Kit通过[PdfView](../harmonyos-references/pdf-arkts-pdfview-component.md#pdfview)组件提供了丰富的PDF文档预览能力，其中页面缩放是通过[捏合手势](../harmonyos-guides/arkts-gesture-events-single-gesture.md#捏合手势pinchgesture)实现的。

## 解决方案

可以通过[onTouchTestDone](../harmonyos-references/ts-gesture-blocking-enhancement.md#ontouchtestdone20)接口[阻止手势参与识别](../harmonyos-guides/arkts-gesture-events-gesture-judge.md#阻止手势参与识别)，达到禁止缩放的功能。

完整示例参考如下：

```ts
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG = 'PDFView';

@Entry
@Component
struct PDFView {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      hilog.error(0x0000, TAG, 'Get context failed');
      return;
    }

    let dir: string = context.filesDir;
    // 确保rawfile里面有pdf文件
    let filePath: string = dir + '/pdf_reference.pdf';
    try {
      fileIo.accessSync(filePath);
      let content: Uint8Array = context.resourceManager.getRawFileContentSync('rawfile/pdf_reference.pdf');
      let fdSand =
        fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
      fileIo.writeSync(fdSand.fd, content.buffer);
      fileIo.closeSync(fdSand.fd);
    } catch (e) {
      let err = e as BusinessError;
      hilog.error(0x0000, TAG, `fs operation failed, error code: ${err.code}, error message: ${err.message}`);
    }

    (async () => {
      let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      if (loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
        hilog.info(0x0000, TAG, 'PDF load successfully');
      }
    })();
  }

  @Builder
  Back() {
    Button('返回')
      .width(100)
      .fontSize(20)
      .padding({ left: 30, top: 8 })
      .margin({ left: 10, top: 10 })
      .onClick(() => {
        this.getUIContext().getRouter().back({ url: 'pages/Index' });
      })
  }

  build() {
    Row() {
      Stack() {
        PdfView({
          controller: this.controller,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1)
          .overlay(this.Back(), {
            align: Alignment.TopStart
          })
      }.onTouchTestDone((event, recognizers) => {
        for (let i = 0; i < recognizers.length; i++) {
          let recognizer = recognizers[i];
          // 根据类型禁用捏合手势
          if (recognizer.getType() == GestureControl.GestureType.PINCH_GESTURE) {
            recognizer.preventBegin();
          }
        }
      })

    }
    .width('100%')
    .height('100%')
  }
}
```
