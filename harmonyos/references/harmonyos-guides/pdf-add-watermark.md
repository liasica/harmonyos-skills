---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-watermark
title: 添加、删除水印
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除水印
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:16+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:716edfcea4a1786ce51794199e3167ae8351135403ddfd43c415d9d5ce1f4aca
---

对指定页面添加水印，包括文本水印或图片水印。

* 文本水印可以设置字体、大小、旋转，位置等属性。
* 图片水印可以设置缩放、旋转、透明度和位置等属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/DuYoJH5aQyCp2SFblM469A/zh-cn_image_0000002742004319.png)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [addWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#addwatermark)(info: WatermarkInfo, startIndex: number, endIndex: number, oddPages: boolean, evenPages: boolean): void | 插入水印到PDF文档。如果插入的是图片，支持的图片格式参考[ImageFormat](../harmonyos-references/pdf-arkts-pdfservice.md#imageformat)，文本字符无限制。 |
| [removeWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#removewatermark)(): boolean | 删除PDF文档水印。 |

**注意** 

[addWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#addwatermark)方法属于耗时业务，需要遍历每一页去添加水印，添加页面较多时建议放到线程里去处理。

## 示例代码

### 添加、删除文本水印

**添加文本水印**

1. 调用loadDocument方法，加载PDF文档。
2. 实例化文本水印TextWatermarkInfo类，并设置相关属性，包括字体、大小、旋转、位置等。
3. 调用addWatermark，添加文本水印。
4. 保存PDF文档到应用沙箱。

**删除文本水印**

1. 调用loadDocument方法，加载PDF文档。
2. 调用removeWatermark，删除文本水印。
3. 保存PDF文档到应用沙箱。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Font } from '@kit.ArkUI';
// ...

@Entry
@Component
struct WatermarkPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
    // ...
        Button('addTextWatermark').onClick(async () => {
          // 确保在工程目录src/main/resources/resfile里有input.pdf文档
          let filePath = this.context.resourceDir + '/input.pdf';
          let res = this.pdfDocument.loadDocument(filePath);
          if (res === pdfService.ParseResult.PARSE_SUCCESS) {
            let wminfo: pdfService.TextWatermarkInfo = new pdfService.TextWatermarkInfo();
            wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_TEXT;
            wminfo.content = 'This is Watermark';
            wminfo.textSize = 30;
            wminfo.textColor = 200;
            wminfo.fontInfo = new pdfService.FontInfo();
            // 确保字体路径存在
            let font: Font = new Font()
            wminfo.fontInfo.fontPath = font.getFontByName('HarmonyOS Sans').path;
            wminfo.opacity = 0.5;
            wminfo.isOnTop = true;
            wminfo.rotation = 45;
            wminfo.scale = 1.5;
            wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
            wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
            wminfo.horizontalSpace = 1.0;
            wminfo.verticalSpace = 1.0;
            this.pdfDocument.addWatermark(wminfo, 0, 5, true, true);
            let outPdfPath = this.context.filesDir + '/testTextWatermark.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            hilog.info(0x0000, 'WatermarkPage', 'addTextWatermark %{public}s!', result ? 'success' : 'fail');
          }
          this.pdfDocument.releaseDocument();
        })
        Button('removeTextWatermark').onClick(async () => {
          let filePath = this.context.filesDir + '/testTextWatermark.pdf';
          let res = this.pdfDocument.loadDocument(filePath);
          if (res === pdfService.ParseResult.PARSE_SUCCESS && this.pdfDocument.hasWatermark()) {
            let removeResult = this.pdfDocument.removeWatermark();
            if (removeResult) {
              let outPdfPath = this.context.filesDir + '/removeWatermark.pdf';
              let result = this.pdfDocument.saveDocument(outPdfPath);
              hilog.info(0x0000, 'WatermarkPage', 'removeWatermark %{public}s!', result ? 'success' : 'fail');
            }
          }
          this.pdfDocument.releaseDocument();
        })
        // ...
        // ...
    }
  }
}
```

### 添加、删除图片水印

**添加图片水印**

1. 调用loadDocument方法加载PDF文档。
2. 实例化图片水印ImageWatermarkInfo类，并设置相关属性，包括缩放、旋转、透明度和位置等。
3. 调用addWatermark添加图片水印。
4. 保存PDF文档到应用沙箱。

**删除图片水印**

1. 调用loadDocument方法加载PDF文档。
2. 调用removeWatermark删除图片水印。
3. 保存PDF文档到应用沙箱。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Font } from '@kit.ArkUI';
// ...

@Entry
@Component
struct WatermarkPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
    // ...
        Button('addImageWatermark').onClick(async () => {
          let doc: pdfService.PdfDocument = new pdfService.PdfDocument();
          let filePath: string = this.context.resourceDir + '/input.pdf';
          let outPdfPath = this.context.filesDir + '/testImageWatermark.pdf';

          doc.loadDocument(filePath);
          let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
          wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_IMAGE;
          wminfo.imagePath = this.context.resourceDir + '/img.jpg';
          wminfo.opacity = 1;
          wminfo.isOnTop = true;
          wminfo.rotation = 0;
          wminfo.scale = 0.1;
          wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_HCENTER;
          wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_VCENTER;
          wminfo.horizontalSpace = 1.0;
          wminfo.verticalSpace = 1.0;
          doc.addWatermark(wminfo, 0, 18, true, true);
          let result = doc.saveDocument(outPdfPath);
          hilog.info(0x0000, 'WatermarkPage', 'addImageWatermark %{public}s!', result ? 'success' : 'fail');
          doc.releaseDocument();
        })
        Button('removeImageWatermark').onClick(async () => {
          let filePath = this.context.filesDir + '/testImageWatermark.pdf';
          let res = this.pdfDocument.loadDocument(filePath);
          if (res === pdfService.ParseResult.PARSE_SUCCESS && this.pdfDocument.hasWatermark()) {
            let removeResult = this.pdfDocument.removeWatermark();
            if (removeResult) {
              let outPdfPath = this.context.filesDir + '/removeImageWatermark.pdf';
              let result = this.pdfDocument.saveDocument(outPdfPath);
              hilog.info(0x0000, 'WatermarkPage', 'removeImageWatermark %{public}s!', result ? 'success' : 'fail');
            }
          }
          this.pdfDocument.releaseDocument();
        })
        // ...
    }
  }
}
```
