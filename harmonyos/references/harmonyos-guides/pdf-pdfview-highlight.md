---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-highlight
title: 高亮显示PDF文档
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 高亮显示PDF文档
category: harmonyos-guides
scraped_at: 2026-09-18T06:46:25+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:fe17fcd13683e04359243e9550504cbf7578e84cc2b959b349090c7a026703d4
---

PDF文档在预览时，可以对页面的矩形区域或文本设置高亮显示，高亮颜色可以自定义。

[setHighlightText](../harmonyos-references/pdf-arkts-pdfviewmanage.md#sethighlighttext)可以同时高亮多个不同的文本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-hAQg6pOQj-KSHPHKfynlQ/zh-cn_image_0000002727591930.png)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [setHighlightText](../harmonyos-references/pdf-arkts-pdfviewmanage.md#sethighlighttext)(pageIndex: number, textArray: string[], color: number): void | 高亮指定文本。 |

**注意** 

[setHighlightText](../harmonyos-references/pdf-arkts-pdfviewmanage.md#sethighlighttext)和[searchKey](../harmonyos-references/pdf-arkts-pdfviewmanage.md#searchkey)功能互斥。

## 示例代码

1. 加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在按钮【setHighlightText】里，调用setHighlightText方法，设置单个或多个要高亮的文本。

```typescript
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
// ...

@Entry
@Component
struct HighlightPage {
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
        Row() {
          // 设置文本的高亮显示风格
          Button('setHighlightText').onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              this.controller.setHighlightText(0, ['PDF'], 0xAAF9CC00);
            }
          })
        }
        // 加载PdfView组件进行预览
        PdfView({
          controller: this.controller,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1);
      }
      // ...
    .width('100%').height('100%')
  }
}
```
