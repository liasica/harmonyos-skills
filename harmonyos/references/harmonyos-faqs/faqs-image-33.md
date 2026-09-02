---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-33
title: 网络图片用Image组件加载变成横屏显示如何解决
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 网络图片用Image组件加载变成横屏显示如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d5a92edd2400ae984923af4736a2c493aafc84ef2c43b35db8c7f02f53fa4468
---

## 问题现象

使用HarmonyOS系统的Image组件加载部分网络图片时，图片会变成横屏展示，问题代码和截图如下，该如何解决？

```ts
Image('图片地址')
  .objectFit(ImageFit.Contain)
  .width('100%')
  .backgroundColor(0x181818)
```

## 背景知识

1. Exif(Exchangeable image file format 可交换图像文件格式)，是一种图像文件格式，EXIF可以附加于JPEG、TIFF、RIFF、RAW等文件之中，为其增加有关数码相机拍摄信息的内容和索引图或图像处理软件的版本信息。
2. [ImageSource.getImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#getimageproperty11)：可以通过该接口获取图片中给定索引处图像的指定属性键的值，仅支持JPEG、PNG和HEIF（不同硬件设备支持情况不同）文件，且需要包含Exif信息。其中可以通过supportedFormats属性查询是否支持HEIF格式的Exif读写。

## 解决方案

该问题的根本原因是图片里的Exif信息存在旋转90°的信息，HarmonyOS的Image组件会读取图片中的信息并旋转。如果不想旋转需要应用自行进行适配，目前可尝试以下方案适配：

1. 由于Image组件无法拿到图片数据，需要先通过网络请求获取图片，设置传输数据类型expectDataType为arraybuffer，然后使用[createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9)转换成image.ImageSource对象；
2. 获取图片Exif信息，可以通过getImageProperty接口 (PropertyKey传入"Orientation"）获取旋转信息。通过判断图片是否要旋转，并将不同返回值的旋转角度返回给Image组件的[orientation](../harmonyos-references/ts-basic-components-image.md#orientation14)属性进行旋转或镜像；

   ```ts
   // 根据获取到的EXIF方向信息，转换ImageRotateOrientation，使图片显示为正确的方向。
   getOrientation(orientation: string): ImageRotateOrientation {
     if (orientation == 'Top-right') {
       return ImageRotateOrientation.UP_MIRRORED;
     } else if (orientation == 'Bottom-right') {
       return ImageRotateOrientation.DOWN;
     } else if (orientation == 'Bottom-left') {
       return ImageRotateOrientation.DOWN_MIRRORED;
     } else if (orientation == 'Left-top') {
       return ImageRotateOrientation.LEFT_MIRRORED;
     } else if (orientation == 'Right-top') {
       return ImageRotateOrientation.RIGHT;
     } else if (orientation == 'Right-bottom') {
       return ImageRotateOrientation.RIGHT_MIRRORED;
     } else if (orientation == 'Left-bottom') {
       return ImageRotateOrientation.LEFT;
     } else if (orientation == 'Top-left') {
       return ImageRotateOrientation.UP;
     } else {
       return ImageRotateOrientation.UP;
     }
   }
   ```
3. 若需要将网络图片保存至本地使用，可以下载网络图片获取图片数据后，通过imageSource.createPixelMap接口，转成PixelMap对象，最后将PixelMap对象的图片给到Image组件。

   ```ts
   requestImageUrl(url: string) {
     http.createHttp().request(url,
       {
         expectDataType: http.HttpDataType.ARRAY_BUFFER
       },
       (error: BusinessError, data: http.HttpResponse) => {
         if (error) {
           console.error(`request image failed: url: ${url}, code: ${error.code}, message: ${error.message}`);
         } else {
           let imgData: ArrayBuffer = data.result as ArrayBuffer;
           console.info(`request image success, size: ${imgData.byteLength}`);
           let imgSource: image.ImageSource = image.createImageSource(imgData);
           imgSource.createPixelMap().then((pixelMap: PixelMap) => {
             imgSource.getImageProperty(image.PropertyKey.ORIENTATION).then((data: string) => {
               console.info('image orientation data is', data);
               this.rotateOrientation = this.getOrientation(data);
             }).catch((error: BusinessError) => {
               console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
             });
             console.info('image createPixelMap success');
             this.pixelMapImg1 = pixelMap;
             imgSource.release();
           }).catch(() => {
             imgSource.release();
           });
         }
       });
   }
   ```

   也可以通过downloadFile方法将图片下载到本地后，创建新PixelMap进行展示。

   ```ts
   downloadImage() {
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let tempPath = context.filesDir + '/' + new Date().getTime() + '.png';
     try {
       request.downloadFile(this.getUIContext().getHostContext(), {
         url: this.imageUrl,
         filePath: tempPath
       }).then((downloadTask: request.DownloadTask) => {
         downloadTask.on('complete', async () => {
           let file = fileIo.openSync(tempPath, fileIo.OpenMode.READ_ONLY);
           let imgSource: image.ImageSource = image.createImageSource(file.fd);
           imgSource.createPixelMap().then((pixelMap: PixelMap) => {
             imgSource.getImageProperty(image.PropertyKey.ORIENTATION).then((data: string) => {
               this.rotateOrientation = this.getOrientation(data);
             }).catch((error: BusinessError) => {
               console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
             });
             console.info('image createPixelMap success');
             this.pixelMapImg2 = pixelMap;
             imgSource.release();
           }).catch(() => {
             imgSource.release();
           }).finally(() => {
             fileIo.close(file);
           });
         });
       });
     } catch (error) {
       console.error('download error', error);
     }
   }
   ```

   完整代码如下：

   ```ts
   import { http } from '@kit.NetworkKit';
   import { BusinessError, request } from '@kit.BasicServicesKit';
   import { image } from '@kit.ImageKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct CorrectDisplayOfImage {
     @State rotateOrientation: ImageRotateOrientation = ImageRotateOrientation.UP;
     @State pixelMapImg1: PixelMap | undefined = undefined;
     @State pixelMapImg2: PixelMap | undefined = undefined;
     imageUrl: string = ''; // 请填写一个具体的网络图片地址

     // 根据获取到的EXIF方向信息，转换ImageRotateOrientation，使图片显示为正确的方向。
     getOrientation(orientation: string): ImageRotateOrientation {
       if (orientation == 'Top-right') {
         return ImageRotateOrientation.UP_MIRRORED;
       } else if (orientation == 'Bottom-right') {
         return ImageRotateOrientation.DOWN;
       } else if (orientation == 'Bottom-left') {
         return ImageRotateOrientation.DOWN_MIRRORED;
       } else if (orientation == 'Left-top') {
         return ImageRotateOrientation.LEFT_MIRRORED;
       } else if (orientation == 'Right-top') {
         return ImageRotateOrientation.RIGHT;
       } else if (orientation == 'Right-bottom') {
         return ImageRotateOrientation.RIGHT_MIRRORED;
       } else if (orientation == 'Left-bottom') {
         return ImageRotateOrientation.LEFT;
       } else if (orientation == 'Top-left') {
         return ImageRotateOrientation.UP;
       } else {
         return ImageRotateOrientation.UP;
       }
     }

     requestImageUrl(url: string) {
       http.createHttp().request(url,
         {
           expectDataType: http.HttpDataType.ARRAY_BUFFER
         },
         (error: BusinessError, data: http.HttpResponse) => {
           if (error) {
             console.error(`request image failed: url: ${url}, code: ${error.code}, message: ${error.message}`);
           } else {
             let imgData: ArrayBuffer = data.result as ArrayBuffer;
             console.info(`request image success, size: ${imgData.byteLength}`);
             let imgSource: image.ImageSource = image.createImageSource(imgData);
             imgSource.createPixelMap().then((pixelMap: PixelMap) => {
               imgSource.getImageProperty(image.PropertyKey.ORIENTATION).then((data: string) => {
                 console.info('image orientation data is', data);
                 this.rotateOrientation = this.getOrientation(data);
               }).catch((error: BusinessError) => {
                 console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
               });
               console.info('image createPixelMap success');
               this.pixelMapImg1 = pixelMap;
               imgSource.release();
             }).catch(() => {
               imgSource.release();
             });
           }
         });
     }

     downloadImage() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let tempPath = context.filesDir + '/' + new Date().getTime() + '.png';
       try {
         request.downloadFile(this.getUIContext().getHostContext(), {
           url: this.imageUrl,
           filePath: tempPath
         }).then((downloadTask: request.DownloadTask) => {
           downloadTask.on('complete', async () => {
             let file = fileIo.openSync(tempPath, fileIo.OpenMode.READ_ONLY);
             let imgSource: image.ImageSource = image.createImageSource(file.fd);
             imgSource.createPixelMap().then((pixelMap: PixelMap) => {
               imgSource.getImageProperty(image.PropertyKey.ORIENTATION).then((data: string) => {
                 this.rotateOrientation = this.getOrientation(data);
               }).catch((error: BusinessError) => {
                 console.error(`Failed to get the value of the specified attribute key of the image, error.code ${error.code}, error.message ${error.message}`);
               });
               console.info('image createPixelMap success');
               this.pixelMapImg2 = pixelMap;
               imgSource.release();
             }).catch(() => {
               imgSource.release();
             }).finally(() => {
               fileIo.close(file);
             });
           });
         });
       } catch (error) {
         console.error('download error', error);
       }
     }

     build() {
       Column({ space: 20 }) {
         Row() {
           Text('直接加载网络图片');
           Image(this.imageUrl)
             .objectFit(ImageFit.Contain)
             .height(200);
         };

         Row() {
           Button('solution1')
             .onClick(() => {
               this.requestImageUrl(this.imageUrl); // 请填写一个具体的网络图片地址
             });
           Image(this.pixelMapImg1)
             .objectFit(ImageFit.Contain)
             .height(100)
             .orientation(this.rotateOrientation)
         };

         Row() {
           Button('solution2')
             .onClick(() => {
               this.downloadImage();
             });
           Image(this.pixelMapImg2)
             .objectFit(ImageFit.Contain)
             .height(100)
             .orientation(this.rotateOrientation)
         };
       };
     }
   }
   ```

## 总结

Image在加载图片时受图片的Exif信息的影响，可能会和预期不符，此时需要先读取并分析图片的Exif信息，然后再用正确的属性配置加载图片。
