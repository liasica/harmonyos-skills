---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-10
title: PdfView组件如何实时显示编辑后的PDF文件
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PdfView组件如何实时显示编辑后的PDF文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:6b07f493195f442a88febae2c05a9c359b0ff9fc377593d6f7fe2fef3592b5d0
---

## 问题现象

PdfView组件加载一个PDF文件，对这个文件做编辑操作，如何使编辑后的效果在PdfView组件里体现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/IqmnRyLnTBujSBBFKH8K1A/zh-cn_image_0000002658793615.gif "点击放大")

## 背景知识

* [PdfView](../harmonyos-references/pdf-arkts-pdfview-component.md)：HarmonyOS应用通过集成该组件完成PDF文件的预览功能。
* [pdfViewManager](../harmonyos-references/pdf-arkts-pdfviewmanage.md)：为应用提供统一的PDF预览能力。
* [pdfService](../harmonyos-references/pdf-arkts-pdfservice.md)：为应用提供统一的管理PDF页面的页眉页脚、水印和背景、文档的多种批注风格和书签便捷的PDF能力。
* [loadDocument](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)：加载文件并显示指定的页面。
* [saveDocument](../harmonyos-references/pdf-arkts-pdfviewmanage.md#savedocument)：保存PDF文档，由于文档不可同时读写，如果需要覆盖回原文档，需要创建临时文档作为过渡。

## 解决方案

以加载一个PDF文件，为其添加背景色为例：

```ts
import { common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { systemDateTime } from '@kit.BasicServicesKit';

@Entry
@Component
struct PdfAddBgc {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State filePath: string = '';
  @State curPage: number = 0;

  aboutToAppear(): void {
    let dir: string = this.context.filesDir;
    // 确保在工程目录src/main/resources/rawfile里存在test.pdf文档
    this.filePath = dir + '/test.pdf';
    let res = fs.accessSync(this.filePath);
    if (!res) {
      let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('rawfile/test.pdf');
      let fdSand: fs.File | null = null;
      try {
        fdSand =
          fs.openSync(this.filePath, fs.OpenMode.WRITE_ONLY | fs.OpenMode.CREATE | fs.OpenMode.TRUNC);
        fs.writeSync(fdSand.fd, content.buffer);
      } catch (e) {
        console.error('fs.openSync failed error is : ', JSON.stringify(e));
      } finally {
        if (fdSand !== null) {
          fs.closeSync(fdSand.fd);
        }
      }
    }
    (async () => {
      let loadResult: pdfService.ParseResult = await this.controller.loadDocument(this.filePath);
      console.log('loadResult is ', loadResult);
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        this.controller.setPageZoom(1);
        // 监听滑动到第几页
        this.controller.registerPageChangedListener((pageIndex: number) => {
          this.curPage = pageIndex;
        });
      }
    })();

  }

  build() {
    Column({ space: 5 }) {
      Row() {
        Button('添加背景色').onClick(() => {
          // pdfDocument.saveDocument不支持编辑加载的文件，拷贝一份用来编辑
          let tempDir = this.context.tempDir;
          let tempEditFilePath = tempDir + `/tempEdit${systemDateTime.getTime()}.pdf`;
          fs.copyFileSync(this.filePath, tempEditFilePath);
          let pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
          // 编辑PDF文件时使用临时文件过渡
          let loadResult = pdfDocument.loadDocument(tempEditFilePath);
          if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
            let pageCount = pdfDocument.getPageCount();
            let bgInfo: pdfService.BackgroundInfo = new pdfService.BackgroundInfo();
            bgInfo.backgroundColor = 20;
            bgInfo.isOnTop = true;
            bgInfo.rotation = 0;
            bgInfo.scale = 1;
            bgInfo.opacity = 0.3;
            bgInfo.verticalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_TOP;
            bgInfo.horizontalAlignment = pdfService.BackgroundAlignment.BACKGROUND_ALIGNMENT_LEFT;
            bgInfo.horizontalSpace = 1;
            bgInfo.verticalSpace = 1;
            pdfDocument.addBackground(bgInfo, 0, pageCount, true, false);
            // 将添加背景色后的内容保存到源文件
            pdfDocument.saveDocument(this.filePath);
            // 释放PdfView组件中编辑前的PDF文件
            this.controller.releaseDocument();
            // 将通过pdfService编辑好的PDF文件加载到PdfView组件中
            this.controller.loadDocument(this.filePath, '', this.curPage);
          }
        })
      }
      .height('10%')

      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_NONE,
        showScroll: false
      })
        .height('90%')
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
    .width('100%')
    .height('100%')
  }
}
```

## 常见FAQ

Q：编辑PDF文件后，重新进入页面，PdfView组件里还是展示的编辑前的效果。

A：编辑PDF文件后要及时保存，需要调用PdfView组件绑定的controller的saveDocument方法。

Q：编辑PDF文档的页面时，需要用到包括拆页、合页、旋转、缩放、创建等能力。

A：参考[pdfService与PdfView能力比较](../harmonyos-guides/pdf-introduction.md#pdfservice与pdfview能力比较)；编辑能力可参考[pdfService](../harmonyos-references/pdf-arkts-pdfservice.md)。
