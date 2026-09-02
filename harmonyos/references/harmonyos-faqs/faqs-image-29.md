---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-29
title: 如何将图片转换为Base64格式
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将图片转换为Base64格式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:bd9bf981e6d06094bbe5868ac8c98848adf3fcaa02a899ff2f4a785b095cb201
---

## 问题现象

HarmonyOS如何将图片转成base64格式。

## 背景知识

base64编码是基于64个可打印字符来表示任意二进制数据的方法，它通常用于在文本协议和文件格式中传输或存储二进制数据。使用base64编码的优缺点如下所示：

**优点**：

* 减少HTTP请求：将图像嵌入到文档中（如HTML文件、CSS文件、JS文件等文本文件），减少了对图像的独立HTTP请求，提高了页面加载性能。
* 无需额外存储：不需要单独存储图像文件，将图像数据包含在文档中，对于一部分小型图像的临时需求更加方便。
* 用于CSS和HTML属性：base64图片可以用作CSS的背景图片background-image，也可以应用于HTML元素的src属性中。

**缺点**：

* 增加文档大小：base64编码后的图像数据会增加文档的大小约33%，如果文档中包含大量图像或大型图像，可能会导致文档过大，加载时间长。
* 编解码开销：base64编码和解码需要一定的计算开销，对于一些大型图像进行处理时，可能会导致性能下降。

## 解决方案

HarmonyOS提供[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)工具函数[encodeToStringSync](../harmonyos-references/js-apis-util.md#encodetostringsync9)方法将Uint8Array转换为base64编码，使用方法如下：

```ts
// 入参为Uint8Array
function uint8Array2Base64(uint8Array: Uint8Array): string {
  let base64Helper = new util.Base64Helper();
  return base64Helper.encodeToStringSync(uint8Array);
}

// 入参为ArrayBuffer，可转换为Uint8Array后再转base64
function arrayBuffer2Base64(arrayBuffer: ArrayBuffer): string {
  return uint8Array2Base64(new Uint8Array(arrayBuffer));
}
```

下面列举常用的图片转换ArrayBuffer或Uint8Array的场景和方法：

* **场景一**：应用resources资源文件通过[resourceManager.getMediaContentSync](../harmonyos-references/js-apis-resource-manager.md#getmediacontentsync10)获取Uint8Array：

  ```ts
  // 开发者根据自身需求传入resource目录下的文件
  function readResource2Uint8Array(resource: Resource): Uint8Array {
    let resourceManager = uContext.getHostContext()?.resourceManager;
    return resourceManager!.getMediaContentSync(resource.id);
  }
  ```
* **场景二**：应用沙箱文件通过[fs.readSync](../harmonyos-references/js-apis-file-fs.md#fileioreadsync)获取ArrayBuffer：

  ```ts
  // 传入应用沙箱路径，需要保证路径存在，路径不存在会使应用崩溃
  function readSandFile2ArrayBuffer(sandFilePath: string): ArrayBuffer {
    let sandFile: fs.File | null = null;
    try {
      console.info('sandFilePath:', sandFilePath);
      let stat = fs.statSync(sandFilePath);
      let sandFile = fs.openSync(sandFilePath, fs.OpenMode.READ_ONLY);
      let arrayBuffer = new ArrayBuffer(stat.size);
      fs.readSync(sandFile.fd, arrayBuffer);
      return arrayBuffer;
    } catch (err) {
      console.error(`readSandFile2ArrayBuffer failed: ${err.code}, message: ${err.message}`);
      return new ArrayBuffer(0);
    } finally {
      if (sandFile) {
        fs.closeSync(sandFile);
      }
    }
  }
  ```
* **场景三**：使用[PhotoPicker](../harmonyos-guides/component-guidelines-photoviewpicker.md)组件访问图片，用户相册文件通过fs.readSync获取ArrayBuffer：

  ```ts
  // 调用相册管理模块选择指定图片
  async function readUserPhoto2ArrayBuffer(): Promise<ArrayBuffer> {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult = await photoPicker.select(photoSelectOptions);
    let file: fs.File | null = null;
    try {
      let file = fs.openSync(photoSelectResult.photoUris[0], fs.OpenMode.READ_ONLY);
      let stat = fs.statSync(file.fd);
      let arrayBuffer = new ArrayBuffer(stat.size);
      fs.readSync(file.fd, arrayBuffer);
      return arrayBuffer;
    } catch (err) {
      console.error(`readUserPhoto2ArrayBuffer failed: ${err.code}, message: ${err.message}`);
      return new ArrayBuffer(0);
    } finally {
      if (file) {
        fs.closeSync(file);
      }
    }
  }
  ```
* **场景四**：网络文件通过http模块[request](../harmonyos-references/js-apis-http.md#request)请求获取文件ArrayBuffer：

  ```ts
  // 使用网络图片需要确保module.json5中申请了网络权限ohos.permission.INTERNET，网络图片地址url需要实际可用
  async function readHttpFile2ArrayBuffer(url: string): Promise<ArrayBuffer> {
    try {
      let httpResponse: http.HttpResponse = await http.createHttp().request(url);
      if (http.ResponseCode.OK === httpResponse.responseCode) {
        console.info('httpResponse success');
        return httpResponse.result as ArrayBuffer;
      }
    } catch (e) {
      console.error(`http request failed with. Code: ${e.code}, message: ${e.message}`);
    }
    return new ArrayBuffer(0);
  }
  ```
* **场景五**：[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)通过ImagePacker组件[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)获取ArrayBuffer：

  ```ts
  // 使用packToData获取PixelMap的ArrayBuffer
  async function readPixelMap2ArrayBuffer(pixelMap: image.PixelMap,
    packOpts: image.PackingOption): Promise<ArrayBuffer> {
    try {
      let imagePackerApi: image.ImagePacker = image.createImagePacker();
      return await imagePackerApi.packToData(pixelMap, packOpts);
    } catch (e) {
      console.error(`Failed to pack the image.code ${e.code},message is ${e.message}`);
    }
    return new ArrayBuffer(0);
  }
  ```

对于大尺寸图片，为避免内存溢出，可根据业务需要设置PackingOption压缩参数quality，详情可参考[quality参数与图片原始大小、压缩后大小的关系](faqs-image-4.md)。

完整示例参考如下：

```ts
import { util } from '@kit.ArkTS';
import fs from '@ohos.file.fs';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { UIContext } from '@kit.ArkUI';

let uContext: UIContext;

// 入参为Uint8Array
function uint8Array2Base64(uint8Array: Uint8Array): string {
  let base64Helper = new util.Base64Helper();
  return base64Helper.encodeToStringSync(uint8Array);
}

// 入参为ArrayBuffer，可转换为Uint8Array后再转base64
function arrayBuffer2Base64(arrayBuffer: ArrayBuffer): string {
  return uint8Array2Base64(new Uint8Array(arrayBuffer));
}

// 开发者根据自身需求传入resource目录下的文件
function readResource2Uint8Array(resource: Resource): Uint8Array {
  let resourceManager = uContext.getHostContext()?.resourceManager;
  return resourceManager!.getMediaContentSync(resource.id);
}

// 传入应用沙箱路径，需要保证路径存在，路径不存在会使应用崩溃
function readSandFile2ArrayBuffer(sandFilePath: string): ArrayBuffer {
  let sandFile: fs.File | null = null;
  try {
    console.info('sandFilePath:', sandFilePath);
    let stat = fs.statSync(sandFilePath);
    let sandFile = fs.openSync(sandFilePath, fs.OpenMode.READ_ONLY);
    let arrayBuffer = new ArrayBuffer(stat.size);
    fs.readSync(sandFile.fd, arrayBuffer);
    return arrayBuffer;
  } catch (err) {
    console.error(`readSandFile2ArrayBuffer failed: ${err.code}, message: ${err.message}`);
    return new ArrayBuffer(0);
  } finally {
    if (sandFile) {
      fs.closeSync(sandFile);
    }
  }
}

// 调用相册管理模块选择指定图片
async function readUserPhoto2ArrayBuffer(): Promise<ArrayBuffer> {
  let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  photoSelectOptions.maxSelectNumber = 1;
  let photoPicker = new photoAccessHelper.PhotoViewPicker();
  let photoSelectResult = await photoPicker.select(photoSelectOptions);
  let file: fs.File | null = null;
  try {
    let file = fs.openSync(photoSelectResult.photoUris[0], fs.OpenMode.READ_ONLY);
    let stat = fs.statSync(file.fd);
    let arrayBuffer = new ArrayBuffer(stat.size);
    fs.readSync(file.fd, arrayBuffer);
    return arrayBuffer;
  } catch (err) {
    console.error(`readUserPhoto2ArrayBuffer failed: ${err.code}, message: ${err.message}`);
    return new ArrayBuffer(0);
  } finally {
    if (file) {
      fs.closeSync(file);
    }
  }
}

// 使用网络图片需要确保module.json5中申请了网络权限ohos.permission.INTERNET，网络图片地址url需要实际可用
async function readHttpFile2ArrayBuffer(url: string): Promise<ArrayBuffer> {
  try {
    let httpResponse: http.HttpResponse = await http.createHttp().request(url);
    if (http.ResponseCode.OK === httpResponse.responseCode) {
      console.info('httpResponse success');
      return httpResponse.result as ArrayBuffer;
    }
  } catch (e) {
    console.error(`http request failed with. Code: ${e.code}, message: ${e.message}`);
  }
  return new ArrayBuffer(0);
}

// 使用packToData获取PixelMap的ArrayBuffer
async function readPixelMap2ArrayBuffer(pixelMap: image.PixelMap,
  packOpts: image.PackingOption): Promise<ArrayBuffer> {
  try {
    let imagePackerApi: image.ImagePacker = image.createImagePacker();
    return await imagePackerApi.packToData(pixelMap, packOpts);
  } catch (e) {
    console.error(`Failed to pack the image.code ${e.code},message is ${e.message}`);
  }
  return new ArrayBuffer(0);
}

@Entry
@Component
struct Base64 {
  @State base64Pixel: image.PixelMap | undefined = undefined;
  @State base64String: string = '';
  private url: string = '';

  aboutToAppear() {
    uContext = this.getUIContext();
  }

  build() {
    Column() {
      Image('data:image/jpeg;base64,' + this.base64String)
        .objectFit(ImageFit.Contain)
        .height('20%');
      Text(this.base64String)
        .width('100%')
        .height('50%');
      Button('本地图片转base64')
        .onClick(() => {
          let uint8Array = readResource2Uint8Array($r('app.media.startIcon'));
          this.base64String = uint8Array2Base64(uint8Array);
        });
      Button('沙箱图片转base64')
        .onClick(() => {
          const resourceManager = uContext.getHostContext()?.resourceManager;
          const imageBuffer = resourceManager!.getMediaContentSync($r('app.media.sandbox').id);
          const pathDir = uContext.getHostContext()?.filesDir;
          let filePath = pathDir + '/img.png';
          let file: fs.File | null = null;
          try {
            let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            let writeLen = fs.writeSync(file.fd, imageBuffer.buffer);
            let sandArrayBuffer = readSandFile2ArrayBuffer(filePath);
            this.base64String = arrayBuffer2Base64(sandArrayBuffer);
            console.info(`${writeLen}`);
          } catch (err) {
            console.error(`change to base64 failed: ${err.code}, message: ${err.message}`);
          } finally {
            if (file) {
              fs.closeSync(file);
            }
          }
        })
        .margin(5);
      Button('相册图片转base64')
        .onClick(async () => {
          readUserPhoto2ArrayBuffer().then((photoArrayBuffer) => {
            this.base64String = arrayBuffer2Base64(photoArrayBuffer);
            console.info('', this.base64String);
          });
        })
        .margin(5);
      Button('网络图片转base64')
        .onClick(async () => {
          readHttpFile2ArrayBuffer(this.url).then((httpArrayBuffer) => {
            this.base64String = arrayBuffer2Base64(httpArrayBuffer);
          });
        })
        .margin(5);
      Button('PixelMap转base64')
        .onClick(async () => {
          let resourceManager = uContext.getHostContext()?.resourceManager;
          resourceManager?.getMediaContent($r('app.media.pixelmap').id).then((value) => {
            let pixelBuffer = value.buffer as Object as ArrayBuffer;
            let imageSource = image.createImageSource(pixelBuffer);
            let opts: image.DecodingOptions = { editable: true };
            this.base64Pixel = imageSource.createPixelMapSync(opts);
            let packingOpts: image.PackingOption = {
              quality: 100,
              format: 'image/png'
            };
            readPixelMap2ArrayBuffer(this.base64Pixel, packingOpts).then((pixelBuffer) => {
              this.base64String = arrayBuffer2Base64(pixelBuffer);
            });
          });
        })
        .margin(5);
    };
  }
}
```

## 常见FAQ

Q：PixelMap通过ImagePacker转换base64后，为什么图片文件会膨胀超过33%甚至几倍？

A：原始图片文件在最初编码时设置的quality参数仅为80甚至更低，使用ImagePacker编码时将quality设为100，就会导致图片文件体积明显增大，详情可参考[PixelMap和base64的相互转换](faqs-image-15.md)。

Q：对于不同路径获取到的ArrayBuffer数据，如何判断是否为空？

A：可以将文件存入沙箱中，将文件拖进notepad中，查看其二进制数据，除去头尾之外，如果大部分均为0数据，说明该ArrayBuffer为一个空Buffer。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/SH-7IHwKTIy4mTx_j6sdYQ/zh-cn_image_0000002628552488.png "点击放大")
