---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-page2img
title: PDF缩略图转换为图片
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > PDF缩略图转换为图片
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1e00ead475d695da873eb21c1e51b4d62fc953a8c326aab96cab140cd72ae2d2
---

## 场景介绍

调用[getPagePixelMap](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getpagepixelmap)方法，将指定PDF缩略图转化为图片。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [getPagePixelMap](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getpagepixelmap)(pageIndex: number, isSync?: boolean): Promise<image.PixelMap> | 获取对应PDF页面的缩略图，使用Promise异步回调。 |

## 示例代码

1. 调用loadDocument方法，加载PDF文档。
2. 调用getPagePixelMap方法，获取image.PixelMap对象。
3. 将image.PixelMap转化为二进制图片文件并保存。

```typescript
import { pdfService, pdfViewManager } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
@Entry
@Component
struct PdfViewPageImage {
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

  // 将 pixelMap 转成图片格式
  pixelMap2Buffer(pixelMap: image.PixelMap): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {
      /**
       设置打包参数
       format：图片打包格式
       quality：JPEG 编码输出图片质量
       */
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 }
      // 创建ImagePacker实例
      const imagePackerApi = image.createImagePacker()
      imagePackerApi.packToData(pixelMap, packOpts).then((buffer: ArrayBuffer) => {
        resolve(buffer)
      }).catch((err: BusinessError) => {
        reject()
      })
    })
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
       // ...
        // 转换为图片并保存到应用沙箱
        Button('getPagePixelMap')
          .position({ x: 10, y: 60 })
          .onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              let pixmap: image.PixelMap = await this.controller.getPagePixelMap(0, true);
              if (!pixmap) {
                return
              }
              const imgBuffer = await this.pixelMap2Buffer(pixmap)
              try {
                const file =
                    fileIo.openSync(this.context.filesDir + `/${Date.now()}.png`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                await fileIo.write(file.fd, imgBuffer);
                // 关闭文件
                await fileIo.close(file.fd)
              } catch (e) {
                let error: BusinessError = e as BusinessError;
                hilog.error(0x0000, 'getPagePixelMap-', `Code: ${error.code}, message: ${error.message} `);
              }
            }
          })
      }
    }
    .width('100%').height('100%')
  }
}
```
