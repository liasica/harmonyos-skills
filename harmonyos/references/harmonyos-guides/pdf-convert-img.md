---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-convert-img
title: 转换整个PDF文档为图片
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 转换PDF文档为图片 > 转换整个PDF文档为图片
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:31d10147428182ca7ae31a1772f6290555cedb881ba92868f7eca01ba4a9d78a
---

## 场景介绍

将整个PDF文档的页面转换为图片，每页为一张图片，并且所有图片存放在指定的同一个文件夹下。

当前支持的图片格式请参考[ImageFormat](../harmonyos-references/pdf-arkts-pdfservice.md#imageformat)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [convertToImage](../harmonyos-references/pdf-arkts-pdfservice.md#converttoimage)(path: string, format: ImageFormat, onProgress?: (progress: number) => number): boolean | 转换PDF文档为图片。 |

## 示例代码

1. 调用loadDocument方法，加载PDF文档。
2. 设置要输出图片的文件夹，调用convertToImage方法转化PDF文档所有页面为图片。

```typescript
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { pdfService } from '@kit.PDFKit';
// ...
@Entry
@Component
struct ConvertImagePage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    this.loadResult = this.pdfDocument.loadDocument(filePath);
  }

  build() {
    Column() {
    // ...
        // 获取为图片并保存到应用沙箱
        Button('convertToImage').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            let outputPath = this.getUIContext().getHostContext()?.filesDir + '/output/';
            fileIo.mkdir(outputPath);
            // 将所有的页面转化为png图片，并存储在output文件夹里，确保output文件夹目录存在
            let res = this.pdfDocument.convertToImage(outputPath, pdfService.ImageFormat.PNG);
            hilog.info(0x0000, 'ConvertImagePage', 'convertToImage %{public}s!', res ? 'success' : 'fail');
          }
        })
        // ...
    }
  }
}
```
