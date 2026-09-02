---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-18
title: 如何通过Canvas绘制图形并添加到PDF上
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 如何通过Canvas绘制图形并添加到PDF上
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e34ee016f542434d9a4225d51e1942b1a50c0cd4896aa657390feadb7302a9a8
---

## 问题现象

应用需要通过在Canvas上绘制的图形、文字，添加到PDF上。

## 背景知识

* 应用有自定义场景需要使用[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)绘制图形。
* 绘制后需要将绘制的图形通过[addWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#addwatermark)添加水印到PDF页面上。

## 解决方案

1. 使用Canvas组件和onTouch方法实现手绘功能。

   ```ts
   Stack() {
     Canvas(this.context)
       .width('100%')
       .height('100%')
       .backgroundColor(Color.White)
       .onTouch((event) => {
         if (event.type === TouchType.Down) {
           this.showThickness = false;
           this.eventType = 'Down';
           this.isDrawing = true;
           this.x = event.touches[0].x;
           this.y = event.touches[0].y;
           this.context.beginPath();
           this.tempPath = new Path2D();
           this.tempPath.moveTo(this.x, this.y);
           this.context.lineCap = 'round';
         }
         if (event.type === TouchType.Up) {
           this.eventType = 'Up';
           this.isDrawing = false;
           this.context.closePath();
         }
         if (event.type === TouchType.Move) {
           if (!this.isDrawing) {
             return;
           }
           this.eventType = 'Move';
           this.isEmpty = false;
           // 绘画路径
           this.x = event.touches[0].x;
           this.y = event.touches[0].y;
           this.context.strokeStyle = '#000000';
           this.context.lineWidth = 3;
           this.tempPath.lineTo(this.x, this.y);
           this.context.stroke(this.tempPath);
         }
       });

     Column() {
       //resources/media下替换对应图片
       Image(this.isEmpty ? $r('app.media.startIcon') : $r('app.media.startIcon'))
         .width(30)
         .onClick(() => {
           this.context.clearRect(0, 0, 1080, 1922);
           this.isEmpty = true;
         });
     }
     .position({
       x: '85%',
       y: '2%'
     });
   }
   .width('100%')
   .height('70%')
   .backgroundColor('#F1F3F5')
   .margin({
     top: 36,
     bottom: 5
   })
   .visibility(this.isShow ? Visibility.Visible : Visibility.None);
   ```
2. 将绘制的Canvas内容以png的形式保存到沙箱路径。

   ```ts
   // 将rawfile中的pdf文件转存至沙箱路径供预览使用
   savePdfToCache() {
     this.UIContext.getHostContext()?.resourceManager.getRawFd('test.pdf', (err, data) => {
       let filePath = this.UIContext.getHostContext()?.tempDir + '/test.pdf';
       let dest = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
       let bufsize = 4096;
       let buf = new ArrayBuffer(bufsize);
       let off = 0, len = 0, readedLen = 0;
       // 通过buffer将rawfile文件内容copy到沙箱路径
       while ((len = fs.readSync(data.fd, buf, { offset: data.offset + off, length: bufsize })) > 0) {
         readedLen += len;
         fs.writeSync(dest.fd, buf, { offset: off, length: len });
         off = off + len;
         if ((data.length - readedLen) < bufsize) {
           bufsize = data.length - readedLen;
         }
       }
       fs.close(dest.fd);
     });
   }
   ```
3. 使用addWatermark方法将图片作为水印添加到PDF上。

   ```ts
   // 将沙箱中的canvas图片附加到pdf上
   mergeCanvasToPdf() {
     let filePath = this.UIContext.getHostContext()?.tempDir + '/test.pdf';
     let res = this.pdfDocument.loadDocument(filePath);
     if (res === pdfService.ParseResult.PARSE_SUCCESS) {
       let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
       wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_IMAGE;
       wminfo.imagePath = this.path;
       wminfo.opacity = 1;
       wminfo.isOnTop = true;
       wminfo.rotation = 0;
       wminfo.scale = 0.5;
       wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
       wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
       wminfo.horizontalSpace = 0;
       wminfo.verticalSpace = 0;
       this.pdfDocument.addWatermark(wminfo, 0, 1, true, true);
       let outPdfPath = this.UIContext.getHostContext()?.filesDir + '/testImageWatermark.pdf';
       let result = this.pdfDocument.saveDocument(outPdfPath);
       if (result) {
         this.showToast('合并成功');
       }
       hilog.info(0x0000, 'PdfPage', 'addImageWatermark %{public}s!', result ? 'success' : 'fail');
     }
     this.pdfDocument.releaseDocument();
   }
   ```

完整代码如下：

```ts
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct PaintPage {
  pathStack: NavPathStack = new NavPathStack();
  @StorageProp('topRectHeight') topRectHeight: number = 0;
  @StorageProp('bottomRectHeight') bottomRectHeight: number = 0;
  @State eventType: string = ''; //手指触碰事件类型
  @Provide isEraserMode: boolean = false; // 橡皮擦模式
  @State isDrawing: boolean = false; // 绘画笔
  @State showThickness: boolean = false;
  @State isEmpty: boolean = true;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private x: number = 0; // 触摸点x坐标
  private y: number = 0; // 触摸点y坐标
  private tempPath: Path2D = new Path2D(); // 临时绘画路径
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State UIContext: UIContext = this.getUIContext();
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  @State path: string = '';
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  @State isShow: boolean = true;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  // 将canvas图片以png形式保存至沙箱
  async saveCacheImg(pixelMap: image.PixelMap, path: string): Promise<string> {
    // 通过packing生成buffer数据写入文件 设置图片格式，并返回buffer
    const pixelMapArrayBuffer: ArrayBuffer = await image.createImagePacker().packToData(pixelMap, {
      format: 'image/png',
      quality: 98
    });
    let file = fs.openSync(path, fs.OpenMode.WRITE_ONLY | fs.OpenMode.CREATE);
    await fs.write(file.fd, pixelMapArrayBuffer);
    fs.closeSync(file);
    hilog.info(0x0000, 'PdfPage', 'Save Canvas %{public}s!', file ? 'success' : 'fail');
    this.showToast('canvas保存成功');
    return path;
  }

  // 将rawfile中的pdf文件转存至沙箱路径供预览使用
  savePdfToCache() {
    this.UIContext.getHostContext()?.resourceManager.getRawFd('test.pdf', (err, data) => {
      let filePath = this.UIContext.getHostContext()?.tempDir + '/test.pdf';
      let dest = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      let bufsize = 4096;
      let buf = new ArrayBuffer(bufsize);
      let off = 0, len = 0, readedLen = 0;
      // 通过buffer将rawfile文件内容copy到沙箱路径
      while ((len = fs.readSync(data.fd, buf, { offset: data.offset + off, length: bufsize })) > 0) {
        readedLen += len;
        fs.writeSync(dest.fd, buf, { offset: off, length: len });
        off = off + len;
        if ((data.length - readedLen) < bufsize) {
          bufsize = data.length - readedLen;
        }
      }
      fs.close(dest.fd);
    });
  }

  // 将沙箱中的canvas图片附加到pdf上
  mergeCanvasToPdf() {
    let filePath = this.UIContext.getHostContext()?.tempDir + '/test.pdf';
    let res = this.pdfDocument.loadDocument(filePath);
    if (res === pdfService.ParseResult.PARSE_SUCCESS) {
      let wminfo: pdfService.ImageWatermarkInfo = new pdfService.ImageWatermarkInfo();
      wminfo.watermarkType = pdfService.WatermarkType.WATERMARK_IMAGE;
      wminfo.imagePath = this.path;
      wminfo.opacity = 1;
      wminfo.isOnTop = true;
      wminfo.rotation = 0;
      wminfo.scale = 0.5;
      wminfo.verticalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_TOP;
      wminfo.horizontalAlignment = pdfService.WatermarkAlignment.WATERMARK_ALIGNMENT_LEFT;
      wminfo.horizontalSpace = 0;
      wminfo.verticalSpace = 0;
      this.pdfDocument.addWatermark(wminfo, 0, 1, true, true);
      let outPdfPath = this.UIContext.getHostContext()?.filesDir + '/testImageWatermark.pdf';
      let result = this.pdfDocument.saveDocument(outPdfPath);
      if (result) {
        this.showToast('合并成功');
      }
      hilog.info(0x0000, 'PdfPage', 'addImageWatermark %{public}s!', result ? 'success' : 'fail');
    }
    this.pdfDocument.releaseDocument();
  }

  // 加载pdf
  async loadPdf(path: string) {
    // 先释放再加载
    this.controller.releaseDocument();
    this.loadResult = await this.controller.loadDocument(path);
    if (this.loadResult == 0) {
      this.showToast('pdf加载成功');
    }
    hilog.info(0x0000, 'PdfPage', 'loadMergePdf %{public}s!', this.loadResult == 0 ? 'success' : 'fail');
  }

  // 提示
  showToast(str: string) {
    this.getUIContext().getPromptAction().showToast({
      message: str,
      duration: 500,
      showMode: promptAction.ToastShowMode.DEFAULT,
      bottom: 80
    });
  }

  aboutToAppear(): void {
    this.savePdfToCache();
  }

  build() {
    Column() {
      Column() {
        Stack() {
          Canvas(this.context)
            .width('100%')
            .height('100%')
            .backgroundColor(Color.White)
            .onTouch((event) => {
              if (event.type === TouchType.Down) {
                this.showThickness = false;
                this.eventType = 'Down';
                this.isDrawing = true;
                this.x = event.touches[0].x;
                this.y = event.touches[0].y;
                this.context.beginPath();
                this.tempPath = new Path2D();
                this.tempPath.moveTo(this.x, this.y);
                this.context.lineCap = 'round';
              }
              if (event.type === TouchType.Up) {
                this.eventType = 'Up';
                this.isDrawing = false;
                this.context.closePath();
              }
              if (event.type === TouchType.Move) {
                if (!this.isDrawing) {
                  return;
                }
                this.eventType = 'Move';
                this.isEmpty = false;
                // 绘画路径
                this.x = event.touches[0].x;
                this.y = event.touches[0].y;
                this.context.strokeStyle = '#000000';
                this.context.lineWidth = 3;
                this.tempPath.lineTo(this.x, this.y);
                this.context.stroke(this.tempPath);
              }
            });

          Column() {
            //resources/media下替换对应图片
            Image(this.isEmpty ? $r('app.media.startIcon') : $r('app.media.startIcon'))
              .width(30)
              .onClick(() => {
                this.context.clearRect(0, 0, 1080, 1922);
                this.isEmpty = true;
              });
          }
          .position({
            x: '85%',
            y: '2%'
          });
        }
        .width('100%')
        .height('70%')
        .backgroundColor('#F1F3F5')
        .margin({
          top: 36,
          bottom: 5
        })
        .visibility(this.isShow ? Visibility.Visible : Visibility.None);

        Column() {
          PdfView({
            controller: this.controller,
            pageFit: pdfService.PageFit.FIT_WIDTH,
            showScroll: false,
          })
            .id('pdfview_app_view')
            .layoutWeight(1);
        }
        .width('100%')
        .height('70%')
        .backgroundColor('#F1F3F5')
        .margin({
          top: 36,
          bottom: 5
        })
        .visibility(this.isShow ? Visibility.None : Visibility.Visible);

        Row() {
          Button('保存绘画')
            .width('120')
            .height('40')
            .margin({ right: 10 })
            .onClick(() => {
              this.pixelMap = this.context.getPixelMap(0, 0, 300, 300);
              this.path = this.UIContext.getHostContext()?.tempDir + '/canvas.png';
              this.saveCacheImg(this.pixelMap, this.path);
            });
          Button('合并至pdf')
            .width('120')
            .height('40')
            .onClick(() => {
              this.mergeCanvasToPdf();
            });
        }
        .margin({
          top: 10,
          bottom: 5
        })

        Row() {
          Button('加载原pdf')
            .width('120')
            .height('40')
            .margin({ right: 10 })
            .onClick(() => {
              this.loadPdf(this.UIContext.getHostContext()?.tempDir + '/test.pdf');
            });
          Button('加载新pdf')
            .width('120')
            .height('40')
            .onClick(() => {
              this.loadPdf(this.UIContext.getHostContext()?.filesDir + '/testImageWatermark.pdf');
            });
        }
        .margin({
          top: 5,
          bottom: 5
        });

        Button('切换展示')
          .width('120')
          .height('40')
          .onClick(() => {
            this.isShow = !this.isShow;
          })
          .margin({
            top: 5,
            bottom: 10
          });
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5')
      .padding({
        top: this.topRectHeight,
        left: 16,
        right: 16
      });
    };
  }
}
```
