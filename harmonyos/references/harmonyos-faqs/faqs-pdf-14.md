---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-14
title: PDFView拖拽能力
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PDFView拖拽能力
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:24+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:bebea34928f89beb7bacd1bddd518e13d7ab5e340b8ec02d25b478776642e457
---

## 问题现象

PC项目中需要通过PDFView预览PDF文件时，用鼠标拖拽不生效，如何实现拖拽行为？

## 背景知识

[enablePageDrag](../harmonyos-references/pdf-arkts-pdfviewmanage.md#enablepagedrag)支持设置页面是否支持拖拽。

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verticalEnabled | boolean | 是 | 是否Y轴垂直拖动，true: 是，false: 否。 |
| horizontalEnabled | boolean | 是 | 是否X轴水平拖动，true: 是，false: 否。 |

## 解决方案

使用enablePageDrag接口，设置verticalEnabled和horizontalEnabled属性为true。

完整示例代码如下：

```ts
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { promptAction } from '@kit.ArkUI';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PdfDemo {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  async aboutToAppear(): Promise<void> {
    try {
      // 确保rawfile目录下有pdf文件
      await this.copyRawFileToSdcard(this.context, 'testDemo.pdf');
      promptAction.openToast({ message: '全部拷贝完成' });
      const filePath = `${this.context.filesDir}/testDemo.pdf`;
      this.controller.loadDocument(filePath).then((result) => {
        this.loadResult = result;
        if (pdfService.ParseResult.PARSE_SUCCESS === this.loadResult) {
        }
      });
    } catch (error) {
      promptAction.openToast({ message: '文件拷贝失败' });
    }
  }

  build() {
    Column() {
      PdfView({ controller: this.controller })
        .width('100%')
        .height('80%')
      Row() {
        Button('设置拖拽事件')
          .onClick(() => {
            this.controller.enablePageDrag(true, true);
          })
        Blank()
          .width('20%')
        Button('不设置拖拽事件')
          .onClick(() => {
            this.controller.enablePageDrag(false, false);
          })
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('20%')
    }
  }

  // 拷贝pdf文件到应用沙箱目录
  private copyRawFileToSdcard(context: common.Context, pdfName: string): Promise<void> {
    return new Promise((resolve) => {
      let destRoot = context.filesDir;
      // rawfile下的文件名
      let srcFileName = pdfName;
      let destFilePath = `${destRoot}/${srcFileName}`;
      context.resourceManager.getRawFileContent(srcFileName, (error: BusinessError, data: Uint8Array) => {
        if (error) {
          promptAction.openToast({ message: '拷贝失败' });
          hilog.error(0x0000, 'PdfCopy', `Copy failed: ${error.code}`);
          return;
        }
        const fileStream = fs.createStreamSync(destFilePath, 'w+');
        fileStream.writeSync(data.buffer);
        fileStream.close();
        promptAction.openToast({ message: '拷贝成功' });
        resolve();
      });
    });
  }
}
```

**说明** 

需要确保在工程目录“src/main/resources/rawfile”里存在testDemo.pdf文档，并且拷贝testDemo.pdf文档到沙箱目录。

## 总结

enablePageDrag接口主要场景在PC上，按住一个页面移动鼠标，可以拖动页面。

比如查看PDF时，按住空格键，再拖动鼠标可以移动页面。这个接口就是作用于这类场景的。
