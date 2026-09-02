---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-txt-img-annot
title: PDF页面文本、图片和批注
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > PDF页面文本、图片和批注
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e3e06fc3464a527fa067b87d7aafea7b7ac4bc9b4d009d7ad3473f4b7fceb9b7
---

支持编辑PDF页面内容，包括：

* 添加、删除文本。
* 添加、删除图片。
* 添加、修改、删除批注。

  通过索引指定PDF页面添加批注，并对批注在页面中的位置，字体、批注边框等设置，批注提供了多种风格样式，包括：文本批注[TextAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#textannotationinfo)、下划线批注[LineAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#lineannotationinfo)、高亮批注[HighlightAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#highlightannotationinfo)、删除线批注[StrikethroughAnnotationInfo](../harmonyos-references/pdf-arkts-pdfservice.md#strikethroughannotationinfo)等共13种。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/rSzV9mmiTASc0WSfWGUiTQ/zh-cn_image_0000002706675188.png)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [addTextObject](../harmonyos-references/pdf-arkts-pdfservice.md#addtextobject)(text: string, x: number, y: number, style: TextStyle): void | 添加文本内容，只可按行添加。 |
| [addImageObject](../harmonyos-references/pdf-arkts-pdfservice.md#addimageobject)(path: string, x: number, y: number, width: number, height: number): void | 在PDF文档的页面中添加图片。 |
| [deleteGraphicsObject](../harmonyos-references/pdf-arkts-pdfservice.md#deletegraphicsobject)(object: GraphicsObject): void | 删除指定的GraphicsObject。 |
| [addAnnotation](../harmonyos-references/pdf-arkts-pdfservice.md#addannotation)(annotationInfo: PdfAnnotationInfo): PdfAnnotation | 在当前页添加批注。 |

## 添加文本和图片

1. 调用loadDocument方法，加载PDF文档。
2. 在【addText】按钮中调用addTextObject的方法插入文本。
3. 在【delText】按钮中调用deleteGraphicsObject方法来删除相应的页面文本。
4. 在【addImage】按钮中调用addImageObject的方法插入图片。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Font } from '@kit.ArkUI';
// ...
@Entry
@Component
struct ContentEditPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // 确保resfile目录有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    this.pdfDocument.loadDocument(filePath);
  }

  build() {
    Column() {
      // ...
        // 添加文本
        Button('addText').onClick(async () => {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let str = 'This is add text object!';
          let fontInfo = new pdfService.FontInfo();
          // 确保字体路径存在
          let font: Font = new Font()
          fontInfo.fontPath = font.getFontByName('HarmonyOS Sans')?.path;
          fontInfo.fontName = '';
          let style: pdfService.TextStyle = { textColor: 0x000000, textSize: 30, fontInfo: fontInfo };
          page.addTextObject(str, 10, 10, style);
          let outPdfPath = this.context.filesDir + '/testAddText.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'ContentEditPage', 'addText %{public}s!', result ? 'success' : 'fail');
        })
        // 删除文本
        Button('delText').onClick(async () => {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let graphicsObjects = page.getGraphicsObjects();
          // 找到第一个要删除的文本
          let index = graphicsObjects.findIndex(item => item.type === pdfService.GraphicsObjectType.OBJECT_TEXT);
          if (index > -1) {
            // 删除第一个文本
            page.deleteGraphicsObject(graphicsObjects[index]);
          }
          let outPdfPath = this.context.filesDir + '/testDelText.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'ContentEditPage', 'delText %{public}s!', result ? 'success' : 'fail');
        })
        // 添加图片
        Button('addImage').onClick(async () => {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          // 插入图片，确保resfile目录有img.jpg图片
          let imagePath = this.context.resourceDir + '/img.jpg';
          page.addImageObject(imagePath, 100, 100, 100, 120);
          let outPdfPath = this.context.filesDir + '/testAddImage.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'ContentEditPage', 'addImage %{public}s!', result ? 'success' : 'fail');
        })
        // ...
    }
  }
}
```

## 添加文本批注

1. 调用loadDocument方法，加载PDF文档。
2. 调用getPage方法获取指定页。
3. 实例化TextAnnotationInfo文本批注，并设置相关属性。
4. 调用addAnnotation或setAnnotation方法添加或修改批注。
5. 调用removeAnnotation方法删除批注。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
      // 添加批注
      Button('addTextAnnotation').onClick(async () => {
        // 确保沙箱目录有input.pdf文档
        let filePath = this.context.filesDir + '/input.pdf';
        this.pdfDocument.loadDocument(filePath);
        let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
        let aInfo = new pdfService.TextAnnotationInfo();
        aInfo.iconName = 'Document';
        aInfo.content = 'this is a content';
        aInfo.subject = 'Annotation';
        aInfo.title = 'this is a title';
        aInfo.state = pdfService.TextAnnotationState.MARKED;
        aInfo.x = 200;
        aInfo.y = 200;
        aInfo.color = 0xf9b1b1;
        aInfo.flag = pdfService.AnnotationFlag.PRINTED;
        let annotation: pdfService.PdfAnnotation = page.addAnnotation(aInfo);
        let outPdfPath = this.context.filesDir + '/testAddTextAnnotation.pdf';
        let result = this.pdfDocument.saveDocument(outPdfPath);
        this.pdfDocument.releaseDocument();
        hilog.info(0x0000, 'PdfPage', 'addTextAnnotation %{public}s!', result ? 'success' : 'fail');
      })
      // 修改批注
      Button('setAnnotation').onClick(async () => {
        let filePath = this.context.filesDir + '/testAddTextAnnotation.pdf';
        let result = this.pdfDocument.loadDocument(filePath);
        if (result === pdfService.ParseResult.PARSE_SUCCESS) {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let annotations = page.getAnnotations();
          if (annotations.length > 0 && annotations[0].type === pdfService.AnnotationType.TEXT) {
            let newAnno = annotations[0];
            page.removeAnnotation(newAnno);
            let annotation = page.addAnnotation(newAnno);
            let newInfo = new pdfService.TextAnnotationInfo();
            newInfo.title = "new Title";
            newInfo.content = "new Info";
            newInfo.state = pdfService.TextAnnotationState.MARKED;
            newInfo.x = 100;
            newInfo.y = 100;
            page.setAnnotation(annotation, newInfo);
            let outPdfPath = this.context.filesDir + '/testSetAnnotation.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            this.pdfDocument.releaseDocument();
            hilog.info(0x0000, 'PdfPage', 'setAnnotation %{public}s!', result ? 'success' : 'fail');
          }
        }
      })
      // 删除批注
      Button('removeAnnotation').onClick(async () => {
        let filePath = this.context.filesDir + '/testAddTextAnnotation.pdf';
        let result = this.pdfDocument.loadDocument(filePath);
        if (result === pdfService.ParseResult.PARSE_SUCCESS) {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          let annotations = page.getAnnotations();
          if (annotations.length > 0 && annotations[0].type === pdfService.AnnotationType.TEXT) {
            page.removeAnnotation(annotations[0]);
            let outPdfPath = this.context.filesDir + '/testRemoveAnnotation.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            this.pdfDocument.releaseDocument();
            hilog.info(0x0000, 'PdfPage', 'removeAnnotation %{public}s!', result ? 'success' : 'fail');
          }
        }
      })
    }
  }
}
```
