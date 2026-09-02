---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-3
title: 在预览模式下，如何一键删除所有PDF标注
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 在预览模式下，如何一键删除所有PDF标注
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3f0c4380d9a81d28aa5728c09fc1f137eb24a466fde5a4e10942ee2d86ad66fd
---

## 问题现象

HarmonyOS官方文档当前只支持指定页面和标注进行对应的删除操作，没有一键删除所有PDF标注的API可供使用。

## 背景知识

[PDF Kit（PDF服务）](../harmonyos-guides/pdf-kit-guide.md)包含[pdfService能力](../harmonyos-guides/pdf-pdfservice-implements.md)和[PdfView预览组件](../harmonyos-guides/pdf-pdfview-implements.md)。其中[PdfView预览组件](../harmonyos-guides/pdf-pdfview-implements.md)提供了文档预览功能，如：PDF文档预览、高亮显示、搜索关键字、[批注](../harmonyos-guides/pdf-pdfview-annotation.md)等场景。

| 约束与限制 | 说明 |
| --- | --- |
| 支持的国家和地区 | 当前PDF Kit仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| 模拟器支持的情况 | 当前PDF Kit支持模拟器开发，但与真机存在部分能力差异，详情请参见“[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)”。 |

## 解决方案

1. 确保在工程目录“src/main/resources/rawfile”里存在需要被批注的文档。
2. 使能删除线、高亮等批注能力。
3. 获取原始PDF批注数量，后续删除自己添加的批注，从此索引开始。
4. 注册监听批注事件，当添加批注时，对批注数进行加1操作，记录后续需要删除的批注数量。
5. 监听选中的批注信息，可以校验需要被删除批注的首索引。
6. 加载PdfView组件进行预览，在沙箱内进行批注添加删除处理。
7. 保存修改后的文档，并记录相关日志。

完整示例参考如下：

```ts
import { fileIo } from '@kit.CoreFileKit';
import { pdfViewManager, pdfService, PdfView } from '@kit.PDFKit';
import { common } from '@kit.AbilityKit';

// 循环添加删除批注
@Entry
@Component
struct delAnnotation {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  @State context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private annotationControlType: string[] = ['ADD', 'MOD', 'DEL'];
  private manualAnnNumRecord: number[] = [];
  private rawAnnotationsLen: number[] = [];

  delAllAnn() {
    for (let pageIndex = 0; pageIndex < this.manualAnnNumRecord.length; pageIndex++) {
      let pageAnnNum = this.manualAnnNumRecord[pageIndex];
      let pageAnnStartIndex = this.rawAnnotationsLen[pageIndex];
      for (let delCnt = 0; delCnt < pageAnnNum; delCnt++) {
        this.controller.deleteSelectedAnnotation(pageAnnStartIndex, pageIndex);
        console.info('delCnt is %d, pageIndex is %d, current manualAnnNumRecord is %d, pageAnnStartIndex is %d, ' +
          'pageAnnStartIndex is %d', delCnt, pageIndex, this.manualAnnNumRecord[pageIndex], pageAnnStartIndex);
        this.manualAnnNumRecord[pageIndex]--;
      }
    }
  }

  aboutToAppear(): void {
    // 获取沙箱目录
    let dir: string = this.context.filesDir;
    let filePath: string = dir + '/test.pdf'; // 需要在工程目录src/main/resources/rawfile里添加pdf文档，本例取名为test.pdf，请按实际修改
    try {
      let res = fileIo.accessSync(filePath);
      if (!res) {
        // 需要在工程目录src/main/resources/rawfile里添加pdf文档，本例取名为test.pdf，请按实际修改
        let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('test.pdf');
        let fdSand =
          fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (error) {
      console.error('pdf file access error' + error.message);
    }

    // 获取原始pdf批注数量，后续删除自己添加的批注，从此索引开始
    let loadResult = this.pdfDocument.loadDocument(filePath);
    if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
      let pageCount: number = this.pdfDocument.getPageCount();
      for (let pageIndex = 0; pageIndex < pageCount; pageIndex++) {
        // 初始化手动标注数量
        this.manualAnnNumRecord[pageIndex] = 0;
        let page: pdfService.PdfPage = this.pdfDocument.getPage(pageIndex);
        let annotations: Array<pdfService.PdfAnnotation> = page.getAnnotations();
        this.rawAnnotationsLen[pageIndex] = annotations.length;
        page.release();
        console.info('pageIndex is %d, raw_annotations_len is %d.', pageIndex, this.rawAnnotationsLen[pageIndex]);
      }
    } else {
      console.error('pdfService loadDocument failed.');
      return;
    }

    (async () => {
      // 该监听方法只能在文档加载前调用一次
      this.controller.registerPageCountChangedListener((pageCount: number) => {
        console.info('page count is %s', pageCount.toString());
      });
      let loadResult: pdfService.ParseResult = await this.controller.loadDocument(filePath);
      // 注意：这里刚加载文档，请不要在这里立即设置PDF文档的预览方式
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        // 添加删除线批注
        this.controller.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xFFFF0000);
      }
    })();
    // 注册监听批注事件
    this.controller.registerAnnotationChangedListener((annotationChange: pdfViewManager.AnnotationChangedParam) => {
      if (annotationChange.controlType === 0) {
        // ADD-0, MOD-1, DEL-2
        for (let i = 0; i < annotationChange.pageIndexArray.length; i++) {
          this.manualAnnNumRecord[annotationChange.pageIndexArray[i]]++;
          console.info('annotationChange, pageIndex is %d, manualAnnNumRecord is %d',
            annotationChange.pageIndexArray[i], this.manualAnnNumRecord[annotationChange.pageIndexArray[i]]);
        }
      }
      console.info('annotation controlType is %s', this.annotationControlType[annotationChange.controlType]);
    });
    // 监听选中的批注信息
    this.controller.registerAnnotationSelectedListener((annot: pdfViewManager.SelectedAnnotation | undefined) => {
      console.info('annotation index %d, page index %d', annot?.annotationIndex, annot?.pageIndex);
    });
  }

  build() {
    Column() {
      // 加载PdfView组件进行预览
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1)

      Button() {
        Text('删除所有标注')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }
      .padding(5)
      .margin(5)
      .onClick(() => {
        this.delAllAnn(); // 删除新增的所有批注
      })

      // 点击后调用saveDocument保存修改后的PDF，记录日志。
      Button('保存文件')
        .onClick(async () => {
          let dir: string = this.context.filesDir;
          let savePath = dir + '/test.pdf'; // 需要在工程目录src/main/resources/rawfile里添加pdf文档，本例取名为test.pdf，请按实际修改
          let result: number = await this.controller.saveDocument(savePath);
          console.info('savePdfDocument %s!', result ? 'success' : 'fail');
        })
    }
  }
}
```
