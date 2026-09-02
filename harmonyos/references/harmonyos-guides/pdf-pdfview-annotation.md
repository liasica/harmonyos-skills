---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-annotation
title: 批注
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 批注
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6a0d6f5187bf6617292d643c496e9215535640d4091c41888639a04bb20b984f
---

进入批注模式，目前支持高亮、下划线和删除线类型批注。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [enableAnnotation](../harmonyos-references/pdf-arkts-pdfviewmanage.md#enableannotation)(annotationType: SupportedAnnotationType, color?: number): void | 在常用操作之间切换并添加批注。 |

## 示例代码

1. 先加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 调用enableAnnotation方法，进入批注模式。

```typescript
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
// ...

@Entry
@Component
struct AnnotationPage {
  private pdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        this.pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAFF0000);
      }
    })()
  }

  build() {
  // ...
      Column() {
        PdfView({
          controller: this.pdfController,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1);
      }
      // ...
  }
}
```
