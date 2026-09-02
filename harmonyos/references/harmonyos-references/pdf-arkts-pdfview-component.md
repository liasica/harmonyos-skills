---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfview-component
title: PdfView（PDF预览组件）
breadcrumb: API参考 > 应用服务 > PDF Kit（PDF服务） > ArkTS组件 > PdfView（PDF预览组件）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ef95e5cfc4b05879089cc0d6078c7c2f49ab3866457086eafad32f01d5c7f07b
---

本模块提供PdfView组件，HarmonyOS应用通过集成该组件完成PDF文件的预览功能。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
```

## PdfView

该类是用来展示PDF文档预览的UI组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**装饰器类型：** @Component

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| controller | pdfViewManager.[PdfController](pdf-arkts-pdfviewmanage.md#pdfcontroller) | PdfView组件控制器。 |
| pageLayout | pdfService.[PageLayout](pdf-arkts-pdfservice.md#pagelayout) | 页面布局显示模式，默认值：LAYOUT\_SINGLE。 |
| isContinuous | boolean | 是否连续预览，true：是，false：否。默认值：false。 |
| showScroll | boolean | 是否显示滚动条，true：显示，false：隐藏。默认值：false。 |
| pageFit | pdfService.[PageFit](pdf-arkts-pdfservice.md#pagefit) | 页面适配模式，默认值：FIT\_NONE。 |

### build

build(): void

用于构建[PdfView](pdf-arkts-pdfview-component.md#pdfview)对象的生命周期方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.OfficeService.PDFService.Core

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit'
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as Context;
    let dir: string = context.filesDir
    // 确保在工程目录src/main/resources/rawfile里存在input.pdf文档
    let filePath: string = dir + '/input.pdf';
    let res = fileIo.accessSync(filePath);
    if (!res) {
      let content: Uint8Array = context.resourceManager.getRawFileContentSync('rawfile/input.pdf');
      let fdSand =
        fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
      fileIo.writeSync(fdSand.fd, content.buffer);
      fileIo.closeSync(fdSand.fd);
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
    Row() {
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
    .width('100%')
    .height('100%')
  }
}
```
