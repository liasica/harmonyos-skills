---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-get-img
title: 转换指定页面或指定区域为图片
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 转换PDF文档为图片 > 转换指定页面或指定区域为图片
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1115040f994d85030361c9b63241478cd6aba5d9a57b01f88c0fe9aefa90dacb
---

## 场景介绍

PDF文档页面转换为图片，或将页面的指定区域转换为图片时使用。从26.0.0版本开始，新增支持将多张页面的指定区域转化为一张图片。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [getPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getpagepixelmap)(): image.PixelMap | 获取当前页的图片。 |
| [getCustomPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getcustompagepixelmap)(matrix: PdfMatrix, isGray: boolean, drawAnnotations: boolean): image.PixelMap | 获取指定PdfPage区域的图片内容。 |
| [getAreaPixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getareapixelmap)(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, isGray: boolean, drawAnnotations: boolean): image.PixelMap | 获取指定PdfPage区域的图片内容，并指定图片的宽和高。 |
| [getAreaPixelMapWithOptions](../harmonyos-references/pdf-arkts-pdfservice.md#getareapixelmapwithoptions)(matrix: PdfMatrix, bitmapwidth: number, bitmapHeight: number, options?: PixelOptions): image.PixelMap | 获取指定PdfPage区域的图片内容，并指定图片的宽和高等参数。 |
| [getPixelMapWithPages](../harmonyos-references/pdf-arkts-pdfservice.md#getpixelmapwithpages)(pageIndices: number[], matrices: PdfMatrix[], bitmapWidth: number, bitmapHeight: number, pixelOptions?: PixelOptions): image.PixelMap | 获取多个页面合并后的pixelMap。 |

## 示例代码

1. 调用loadDocument方法加载PDF文档。
2. 调用getPage方法获取某个页面。
3. 调用getPagePixelMap、getAreaPixelMapWithOptions、getCustomPagePixelMap或getPixelMapWithPages方法获取当前页面、页面区域或指定多个页面，返回值均为image.PixelMap图像类型。
4. 将image.PixelMap图像类型转化为二进制图片文件并保存，参考以下方法pixelMap2Buffer。

```typescript
import { pdfService } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...

@Entry
@Component
struct PdfPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    this.loadResult = this.pdfDocument.loadDocument(filePath);
  }

  // 将 pixelMap 转成图片格式
  pixelMap2Buffer(pixelMap: image.PixelMap): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {
         /**
          设置打包参数
          format：图片打包格式
          quality：JPEG 编码输出图片质量
          bufferSize：图片大小
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
    Column() {
      // ...
        // 获取为图片并保存到应用沙箱
        Button('getPagePixelMap').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            let page = this.pdfDocument.getPage(0)
            let pixmap: image.PixelMap = page.getPagePixelMap();
            if (!pixmap) {
              return
            }
            const imgBuffer = await this.pixelMap2Buffer(pixmap)
            try {
              const file =
                fileIo.openSync(this.context.filesDir + `/${Date.now()}.png`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              await fileIo.write(file.fd, imgBuffer)
              // 关闭文档
              await fileIo.close(file.fd)
            } catch (e) {
              let error: BusinessError = e as BusinessError;
              hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
            }
          }
        })
        // 获取指定PdfPage区域的图片内容
        Button('getCustomPagePixelMap').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            let page = this.pdfDocument.getPage(0);
            let matrix = new pdfService.PdfMatrix();
            matrix.x = 100;
            matrix.y = 100;
            matrix.width = 500;
            matrix.height = 500;
            matrix.rotate = 0;
            let pixmap: image.PixelMap = page.getCustomPagePixelMap(matrix, false, false);
            if (!pixmap) {
              return;
            }
            const imgBuffer = await this.pixelMap2Buffer(pixmap);
            try {
              const file =
                fileIo.openSync(this.context.filesDir + `/${Date.now()}.jpeg`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              await fileIo.write(file.fd, imgBuffer);
              await fileIo.close(file.fd);
            } catch (e) {
              let error: BusinessError = e as BusinessError;
              hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
            }
          }
        })
        // 获取指定PdfPage区域的图片内容
        Button('getAreaPixelMap').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            // 获取对应的page
            let page = this.pdfDocument.getPage(0);
            let matrix = new pdfService.PdfMatrix();
            // 设置matrix来控制需要获取的区域
            matrix.x = 100;
            matrix.y = 100;
            matrix.width = 500;
            matrix.height = 500;
            matrix.rotate = 0;
            let pixmap: image.PixelMap = page.getAreaPixelMap(matrix, 400, 400, true, false);
            if (!pixmap) {
              return
            }
            const imgBuffer = await this.pixelMap2Buffer(pixmap)
            try {
              const file =
                fileIo.openSync(this.context.filesDir + `/${Date.now()}.bmp`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              await fileIo.write(file.fd, imgBuffer)
              await fileIo.close(file.fd);
            } catch (e) {
              let error: BusinessError = e as BusinessError;
              hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
            }
          }
        })
        Button('getAreaPixelMapWithOptions').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            let page = this.pdfDocument.getPage(0);
            let matrix = new pdfService.PdfMatrix();
            matrix.x = 100;
            matrix.y = 100;
            matrix.width = 500;
            matrix.height = 500;
            matrix.rotate = 0;
            // 设置pixelmap是否黑白，背景是否透明等参数
            let options = new pdfService.PixelOptions();
            options.isGray = false;
            options.drawAnnotations = true;
            options.isTransparent = true;
            let pixmap: image.PixelMap = page.getAreaPixelMapWithOptions(matrix, 400, 400, options);
            if (!pixmap) {
              return
            }
            const imgBuffer = await this.pixelMap2Buffer(pixmap)
            try {
              const file =
                fileIo.openSync(this.context.filesDir + `/${Date.now()}.bmp`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              await fileIo.write(file.fd, imgBuffer)
              await fileIo.close(file.fd);
            } catch (e) {
              let error: BusinessError = e as BusinessError;
              hilog.error(0x0000, 'PdfPage', `Code: ${error.code}, message: ${error.message} `);
            }
          }
        })
        // ...
    }
  }
}
```
