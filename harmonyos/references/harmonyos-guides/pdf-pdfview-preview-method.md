---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-preview-method
title: 设置PDF文档预览效果
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 设置PDF文档预览效果
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:16+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4b68f92d5e8ed97f464c5d13cda048107f479a4e56b2c4d07d251527695fde42
---

pdfViewManager为PDF文档提供了丰富的预览特性。

* 单双页布局，是否连续滚动和页面适配方式。
* 页面跳转，如上一页，下一页，跳转到指定页。
* 页面放大、缩小。

**图1**：提供了双页预览布局，页面宽度适配和连续滚动的预览方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/SI-L7zI0QvuzpQjjjBFXQQ/zh-cn_image_0000002742124279.png)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [setPageLayout](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagelayout)(columnCount: pdfService.PageLayout): void | 设置页面布局模式。其中“columnCount”取值如下：  1：单页面。  2：双页面。 |
| [setPageContinuous](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagecontinuous)(isContinuous: boolean): void | 设置页面滚动是否连续排列。 |
| [setPageFit](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagefit)(pageFit: pdfService.PageFit): void | 设置页面的适配模式。 |
| [goToPage](../harmonyos-references/pdf-arkts-pdfviewmanage.md#gotopage)(pageIndex: number): void | 跳转到指定页。 |
| [setPageZoom](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setpagezoom)(zoom: number): void | 设置视图的缩放比例。 |

## 示例代码

1. 先加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在按钮【setPreviewMode】里，调用setPageLayout、setPageContinuous等方法，设置文档预览效果。
4. 在按钮【goTopage】里，调用goToPage方法，设置页面跳转。
5. 在按钮【zoomPage2】里，调用setPageZoom方法，将页面放大2倍。

```typescript
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
// ...

@Entry
@Component
struct PdfViewPreviewMethod {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
      // 注意：这里刚加载文档，请不要在这里立即设置PDF文档的预览方法。
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
        .width('100%')
        .height('100%')
        .margin({ top: 150 })

      Column({ space: 10 }) {
        // ...
        Row({ space: 10 }) {
          // 设置预览方式
          Button('setPreviewMode')
            .onClick(() => {
              if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
                // 单页布局
                this.controller.setPageLayout(pdfService.PageLayout.LAYOUT_SINGLE);
                // 是否连续滚动预览
                this.controller.setPageContinuous(true);
                // 适配页的预览方式
                this.controller.setPageFit(pdfService.PageFit.FIT_PAGE);
              }
            })
          // 跳转到第11页
          Button('goTopage')
            .onClick(() => {
              if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
                this.controller.goToPage(10);
              }
            })
        }
        Row({ space: 10 }) {
          // 页面放大2倍
          Button('zoomPage2')
            .onClick(() => {
              if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
                this.controller.setPageZoom(2);
              }
            })
        }
      }
      .alignItems(HorizontalAlign.Start)
      .padding(10)
    }
    .width('100%').height('100%')
  }
}
```
