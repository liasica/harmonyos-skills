---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0001
title: 图片多场景加载与缓存问题排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > 图片多场景加载与缓存问题排查
category: harmonyos-faqs
scraped_at: 2026-11-27T10:50:18+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:56121916b9f94c484f37051689b5cfc953b579cddab49dbeceb02fdc848df5f6
---

**Q：如何使用Image组件加载本地图片？**

**A：**Image组件加载本地图片有以下几种方案：

* 方案一、通过Resource资源管理加载（推荐）。
  + 将图片放置在resources/base/media或resources/rawfile目录下。
  + 使用$r('app.media.图片名')。
  + 使用$rawfile('图片路径')引用资源。
  + 特点：
    - 跨模块/包访问：Resource方式支持跨模块调用。
    - 资源校验：rawfile目录下的图片会进行资源校验，不支持动态拼接文件名。
    - 性能优化：底层自动处理资源缩放和格式适配。
* 方案二、通过本地路径直接引用。
  + 将图片放在ets目录下的任意位置（如ets/images/）。新建工程或模块时，默认配置enable字段并且值为false，即默认不打包ets目录下的资源文件。需要在entry/build-profile.json5中将"copyCodeResource": {"enable": false}的false改为true。详细参考：[resOptions](../harmonyos-guides/ide-hvigor-build-profile.md#section754823013348)资源编译配置项。
  + 特点：
    - 灵活性：支持动态拼接路径（如'images/'+fileName）。
    - 限制如下：
    - 不支持跨模块调用。
    - 修改图片文件需先删除再创建同名文件，否则可能导致崩溃。
* 方案三、通过base64字符串加载。(注意：需要将this.base64ImageData替换成对应的图片资源)。

  实现方式：

  ```ts
  Image('data:image/jpg;base64,' + this.base64ImageData)
  ```

  + 特点：
    - 适合加载小型图片或需要动态生成的图片。
    - 需注意字符串长度对性能的影响。

**Q：Image组件如何加载apng图片？**

**A：**可以通过[ohos\_apng](https://gitee.com/openharmony-sig/ohos_apng)库来实现。

**Q：在开发过程中会遇到很多加载网络图片的场景，例如使用Web组件加载网络图片，使用Image组件加载网络图片。如何使用这两个组件加载网络图片以及两个组件的区别和适用场景是什么？**

**A：**方案一：使用Web组件进行图片加载。

使用Web组件加载网络图片资源时，需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。使用Web组件加载网络图片，可以直接加载图片的在线地址或者带后缀名的图片地址，其具备两个属性：[onlineImageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#onlineimageaccess)和[imageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#imageaccess)，onlineImageAccess设置是否允许从网络加载图片资源（通过HTTP和HTTPS访问的资源），默认允许访问，默认值：true；imageAccess设置是否允许自动加载图片资源，默认允许，默认值：true。代码示例如下：

```ts
Web({ src: $rawfile('index.html'), controller: this.controller })
        .height(200)
        .javaScriptAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .fileAccess(true)
        .geolocationAccess(false)
        .domStorageAccess(true);
```

方案二：使用Image组件加载网络图片。

使用Image组件加载网络图片时，默认网络超时是5分钟，在加载网络图片的过程中，建议使用[alt](../harmonyos-references/ts-basic-components-imagespan.md#alt12)配置加载时的占位图，使用[HTTP](../harmonyos-guides/http-request.md)工具包发送网络请求，然后将返回的数据解码为Image组件中的PixelMap，图片开发可参考[图片处理](../harmonyos-guides/image-overview.md)。使用Image加载网络图片时，需要申请权限ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

* 直接使用Image组件通过网络地址加载网络图片，代码示例如下：

  ```ts
  Image(this.url)
          .height(150)
          .objectFit(ImageFit.Auto)
          .onError((err: ImageError) => {
            // 图片无法加载时触发
            console.error(`Failed to do sth. Code: ${err.error?.code}, message: ${err.message}`);
          })
          .alt($r('app.media.startIcon'));
  ```
* 使用Image加载PixelMap解码后的多媒体像素图。当开发者遇到需要对图片编辑或预览，或者动态生成的图片内容，或实时视频流帧捕捉与展示等情况时，可以使用PixelMap解码图片，然后使用Image进行加载。以下示例将加载的网络图片返回的数据解码成PixelMap格式，再显示在Image组件上。
  1. 创建PixelMap状态变量。
  2. 引用网络权限与媒体库权限，并填写网络图片地址，获取图片的二进制数据，代码示例如下：

     ```ts
     // 通过http的request方法从网络下载图片资源
       async getPicture() {
         http.createHttp()
           .request(this.url, (error: BusinessError, data: http.HttpResponse) => {
             if (error) {
               // 下载失败时弹窗提示检查网络，不执行后续逻辑
               console.error(`request failed, ${JSON.stringify(error.message)}`);
               return;
             }
             this.transcodePixelMap(data);
           });
       }
     ```
  3. 将网络地址成功返回的数据，编码转码成PixelMap的图片格式，参考链接：[多媒体像素图](../harmonyos-guides/arkts-graphics-display.md#多媒体像素图)。代码示例如下：

     ```ts
     /**
        * 使用createPixelMap将ArrayBuffer类型的图片转换为PixelMap类型
        * @param data：网络获取到的资源
        */
       transcodePixelMap(data: http.HttpResponse) {
         if (http.ResponseCode.OK === data.responseCode) {
           const imageData: ArrayBuffer = data.result as ArrayBuffer;
           // 通过ArrayBuffer创建图片源实例
           const imageSource: image.ImageSource = image.createImageSource(imageData);
           let imageInfo = imageSource.getImageInfoSync(0);
           let imgWidth = imageInfo.size.width;
           let imgHeight = imageInfo.size.height;
           const options: image.DecodingOptions = {
             'editable': false,
             'desiredSize': { width: imgWidth, height: imgHeight }
           };

           // 通过属性创建PixelMap
           imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
             this.image = pixelMap;
           });
         }
       }
     ```
  4. 使用Image组件进行图片加载。代码示例如下：

     ```ts
     Image(this.image!)
             .width('100%')
             .objectFit(ImageFit.Auto);
     ```

完整代码如下：

* ArkTS侧：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { http } from '@kit.NetworkKit';
  import { image } from '@kit.ImageKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Index {
    controller: WebviewController = new webview.WebviewController();
    uiContext: UIContext = this.getUIContext();
    @State image: PixelMap | null = null;
    url: string =
      encodeURI(''); // 网络图片链接url

    aboutToAppear() {
      this.getPicture();
      webview.WebviewController.setWebDebuggingAccess(true);
    }

    // 通过http的request方法从网络下载图片资源
    async getPicture() {
      http.createHttp()
        .request(this.url, (error: BusinessError, data: http.HttpResponse) => {
          if (error) {
            // 下载失败时弹窗提示检查网络，不执行后续逻辑
            console.error(`request failed, ${JSON.stringify(error.message)}`);
            return;
          }
          this.transcodePixelMap(data);
        });
    }

    /**
     * 使用createPixelMap将ArrayBuffer类型的图片转换为PixelMap类型
     * @param data：网络获取到的资源
     */
    transcodePixelMap(data: http.HttpResponse) {
      if (http.ResponseCode.OK === data.responseCode) {
        const imageData: ArrayBuffer = data.result as ArrayBuffer;
        // 通过ArrayBuffer创建图片源实例
        const imageSource: image.ImageSource = image.createImageSource(imageData);
        let imageInfo = imageSource.getImageInfoSync(0);
        let imgWidth = imageInfo.size.width;
        let imgHeight = imageInfo.size.height;
        const options: image.DecodingOptions = {
          'editable': false,
          'desiredSize': { width: imgWidth, height: imgHeight }
        };

        // 通过属性创建PixelMap
        imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
          this.image = pixelMap;
        });
      }
    }

    build() {
      Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
        // 方案一：使用Web组件进行图片加载
        Web({ src: $rawfile('index.html'), controller: this.controller })
          .height(200)
          .javaScriptAccess(true)
          .onlineImageAccess(true)
          .imageAccess(true)
          .fileAccess(true)
          .geolocationAccess(false)
          .domStorageAccess(true);

        // 方案二：使用Image组件加载网络图片
        // 直接加载
        Image(this.url)
          .height(150)
          .objectFit(ImageFit.Auto)
          .onError((err: ImageError) => {
            // 图片无法加载时触发
            console.error(`Failed to do sth. Code: ${err.error?.code}, message: ${err.message}`);
          })
          .alt($r('app.media.startIcon'));

        // 解码后加载
        Image(this.image!)
          .width('100%')
          .objectFit(ImageFit.Auto);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* H5侧：

  ```html
  <!DOCTYPE html>
  <html lang="en">

  <head>
      <meta charset="utf-8">
      <title>Demo</title>
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no,   viewport-fit=cover">
      <script>
      </script>
  </head>

  <body>
  <div class="page">

      <img src="" width="250" height="auto">
  </div>
  </body>

  </html>
  ```

**Q：使用Web组件进行图片加载和使用Image组件进行图片加载有什么区别？**

**A：**使用Web组件和Image组件都支持加载本地图片和网络图片，但对于PixelMap类型图片Image组件可以直接加载，Web组件需要将PixelMap转化为base64字符串，或将其保存为本地图片并获取本地图片路径后用于加载。

**Q：需要加载的图片文件名或路径中含有空格、特殊字符或者用户在填写表单时输入了一个带有空格的图片链接，或者某个API返回的图片地址中包含了未经编码的特殊字符，如何使用Image组件进行加载？**

**A：**可以使用encodeURI编码对包含空格或特殊字符的图片地址进行编码，将这些字符替换为对应的编码形式，然后使用Image组件加载。代码示例如下：

```ts
import { webview } from '@kit.ArkWeb';
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();
  @State image: PixelMap | null = null;
  url: string =
    encodeURI(''); // 网络图片链接url

  aboutToAppear() {
    this.getPicture();
    webview.WebviewController.setWebDebuggingAccess(true);
  }

  // 通过http的request方法从网络下载图片资源
  async getPicture() {
    http.createHttp()
      .request(this.url, (error: BusinessError, data: http.HttpResponse) => {
        if (error) {
          // 下载失败时弹窗提示检查网络，不执行后续逻辑
          console.error(`request failed, ${JSON.stringify(error.message)}`);
          return;
        }
        this.transcodePixelMap(data);
      });
  }

  /**
   * 使用createPixelMap将ArrayBuffer类型的图片转换为PixelMap类型
   * @param data：网络获取到的资源
   */
  transcodePixelMap(data: http.HttpResponse) {
    if (http.ResponseCode.OK === data.responseCode) {
      const imageData: ArrayBuffer = data.result as ArrayBuffer;
      // 通过ArrayBuffer创建图片源实例
      const imageSource: image.ImageSource = image.createImageSource(imageData);
      let imageInfo = imageSource.getImageInfoSync(0);
      let imgWidth = imageInfo.size.width;
      let imgHeight = imageInfo.size.height;
      const options: image.DecodingOptions = {
        'editable': false,
        'desiredSize': { width: imgWidth, height: imgHeight }
      };

      // 通过属性创建PixelMap
      imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
        this.image = pixelMap;
      });
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      // 方案一：使用Web组件进行图片加载
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .height(200)
        .javaScriptAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .fileAccess(true)
        .geolocationAccess(false)
        .domStorageAccess(true);

      // 方案二：使用Image组件加载网络图片
      // 直接加载
      Image(this.url)
        .height(150)
        .objectFit(ImageFit.Auto)
        .onError((err: ImageError) => {
          // 图片无法加载时触发
          console.error(`Failed to do sth. Code: ${err.error?.code}, message: ${err.message}`);
        })
        .alt($r('app.media.startIcon'));

      // 解码后加载
      Image(this.image!)
        .width('100%')
        .objectFit(ImageFit.Auto);
    }
    .height('100%')
    .width('100%');
  }
}
```

**Q：使用Image组件加载图片时，图片无法加载，如何检测图片加载失败的原因？**

**A：**检查网络连接和网络权限配置，并在Image组件下添加监听代码，监听图片加载失败原因代码示例如下：

```ts
import { webview } from '@kit.ArkWeb';
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();
  @State image: PixelMap | null = null;
  url: string =
    encodeURI(''); // 网络图片链接url

  aboutToAppear() {
    this.getPicture();
    webview.WebviewController.setWebDebuggingAccess(true);
  }

  // 通过http的request方法从网络下载图片资源
  async getPicture() {
    http.createHttp()
      .request(this.url, (error: BusinessError, data: http.HttpResponse) => {
        if (error) {
          // 下载失败时弹窗提示检查网络，不执行后续逻辑
          console.error(`request failed, ${JSON.stringify(error.message)}`);
          return;
        }
        this.transcodePixelMap(data);
      });
  }

  /**
   * 使用createPixelMap将ArrayBuffer类型的图片转换为PixelMap类型
   * @param data：网络获取到的资源
   */
  transcodePixelMap(data: http.HttpResponse) {
    if (http.ResponseCode.OK === data.responseCode) {
      const imageData: ArrayBuffer = data.result as ArrayBuffer;
      // 通过ArrayBuffer创建图片源实例
      const imageSource: image.ImageSource = image.createImageSource(imageData);
      let imageInfo = imageSource.getImageInfoSync(0);
      let imgWidth = imageInfo.size.width;
      let imgHeight = imageInfo.size.height;
      const options: image.DecodingOptions = {
        'editable': false,
        'desiredSize': { width: imgWidth, height: imgHeight }
      };

      // 通过属性创建PixelMap
      imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
        this.image = pixelMap;
      });
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      // 方案一：使用Web组件进行图片加载
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .height(200)
        .javaScriptAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .fileAccess(true)
        .geolocationAccess(false)
        .domStorageAccess(true);

      // 方案二：使用Image组件加载网络图片
      // 直接加载
      Image(this.url)
        .height(150)
        .objectFit(ImageFit.Auto)
        .onError((err: ImageError) => {
          // 图片无法加载时触发
          console.error(`Failed to do sth. Code: ${err.error?.code}, message: ${err.message}`);
        })
        .alt($r('app.media.startIcon'));

      // 解码后加载
      Image(this.image!)
        .width('100%')
        .objectFit(ImageFit.Auto);
    }
    .height('100%')
    .width('100%');
  }
}
```

**Q：在请求网络图片的过程中，如何进行证书校验？**

**A：**使用Global.getContext中的filesDir方法获取应用沙箱路径，将图片下载至沙箱路径下，再用Image加载图片。

**Q：使用Web组件如何加载HTTPS链接中的HTTP图片？**

**A：**将Web组件的[mixedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#mixedmode)属性设置为MixedMode.All来允许加载HTTP和HTTPS混合内容。

**Q：Image组件加载网络图片，PixelMap与直接访问url有什么区别？**

**A：**两者都支持加载网络图片。使用PixelMap方式时，可以对图片进行更多效果设置，功能更强大。

参考链接：[Image](../harmonyos-references/ts-basic-components-image.md)、[Interface (PixelMap)](../harmonyos-references/arkts-apis-image-pixelmap.md)。

**Q：Image组件是否有缓存机制？**

**A：**

1. Image的缓存策略：Image模块提供了三级Cache机制，解码后内存图片缓存、解码前数据缓存、物理磁盘缓存。在加载图片时会逐级查找，如果在Cache中找到之前加载过的图片则提前返回对应的结果。
2. Image组件如何配置打开和关闭缓存：
   * 内存图片缓存：通过[setImageCacheCount](../harmonyos-references/js-apis-system-app.md#setimagecachecount7)接口打开缓存，如果希望每次联网都获取最新资源，可以不设置（默认为0），不进行缓存。
   * 磁盘缓存：磁盘缓存是默认开启的，默认值为100M，可以将[setImageFileCacheSize](../harmonyos-references/js-apis-system-app.md#setimagefilecachesize7)的值设置为0关闭磁盘缓存。
   * 解码前数据缓存：通过[setImageRawDataCacheSize](../harmonyos-references/js-apis-system-app.md#setimagerawdatacachesize7)设置内存中缓存解码前图片数据的大小上限，单位为字节，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。

setImageCacheCount、setImageRawDataCacheSize和setImageFileCacheSize这三个图片缓存接口灵活性不足，后续不再演进，对于复杂情况，建议使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)。

**Q：利用文件下载把网络图片下载到沙箱目录后，使用Image组件直接加载沙箱路径图片却无法显示，该如何解决？**

**A：**Image组件不能直接传入应用沙箱路径，需要传入应用沙箱URI。在下载完成后不要把filePath直接赋值给downloadImage，而是需要转换。

可以利用[getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法把传入的路径path生成应用自己的uri，修改如下：

```ts
import { common } from '@kit.AbilityKit';
import fs from '@ohos.file.fs';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index2 {
  @State downloadImage: string = '';

  build() {
    Column({ space: 30 }) {
      // 这里直接加载无法显示
      Image(this.downloadImage)
        .width(100);
      Button('Download Image')
        .onClick(() => {
          try {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let filesDir = context.cacheDir;
            // 将字符串/xxx.png拼接到filesDir路径末尾，表示在应用缓存文件路径下创建一个名为xxx.png的文件
            let filePath = filesDir + '/xxx.png';
            let res = fs.accessSync(filePath);
            if (res) {
              this.getUIContext().getPromptAction().showToast({
                message: '文件已存在'
              });
            } else {
              request.downloadFile(context, {
                // 此处地址实际使用过程中替换为真实地址
                url: 'XXX.XXX.png',
                filePath: filePath
              }).then((downloadTask: request.DownloadTask) => {
                downloadTask.on('complete', () => {
                  console.info(`downloadImage= ${filePath}`);
                  this.downloadImage = fileUri.getUriFromPath(filePath);
                });
              }).catch((err: BusinessError) => {
                console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
              });
            }
          } catch (error) {
            let err: BusinessError = error as BusinessError;
            console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
          }
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

**Q：如何读取沙箱目录中的GIF动画资源并使用Image组件显示？**

**A：**Image组件不能直接传入应用沙箱路径，需要先使用[getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法将沙箱文件路径转换为URI。但直接使用沙箱GIF文件的URI作为Image组件的参数不能循环播放，需要将URI转为PixelMap数组，再通过[AnimatedDrawableDescriptor](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)传入Image组件显示。示例代码如下：

```ts
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct ImageGIFDemo {
  @State delayTime: number = 1000;
  animationOpt: AnimationOptions = { duration: this.delayTime, iterations: -1 };
  @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor([], this.animationOpt);
  @State uri: string = '';

  build() {
    Column({ space: 20 }) {
      Button('加载沙箱GIF')
        .onClick(async () => {
          this.uri = this.getSandboxUri();
          let pixelMaps = await this.uriToPixelMap(this.uri);
          // 重新设置图片播放时长
          this.animationOpt = { duration: this.delayTime, iterations: -1 };
          this.animated = new AnimatedDrawableDescriptor(pixelMaps, this.animationOpt);
        });
      if (this.uri != '') {
        Image(this.animated)
          .width('300')
          .height('100');
      }
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center);
  }

  private getSandboxUri() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 沙箱files目录
    let sandboxDir = context.filesDir;
    // 目标GIF文件位置
    let targetFilePath = sandboxDir + '/testgif.gif';
    let uri = fileUri.getUriFromPath(targetFilePath);
    return uri;
  }

  async uriToPixelMap(uri: string) {
    let file: fileIo.File | null = null;
    try {
      // 1.打开文件描述符
      file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
      // 2.创建ImageSource
      let imageSource: image.ImageSource = image.createImageSource(file.fd);
      // 3.获取图像延迟时间数组
      imageSource.getDelayTimeList().then((delayTimes: Array<number>) => {
        console.info('Succeeded in getting delayTimes object.');
        for (let i = 0; i < delayTimes.length; i++) {
          console.info(`delayTimes[${i}] = ${delayTimes[i]}`);
        }
      }).catch((err: BusinessError) => {
        console.error(`Failed to get delayTimes object. code is ${err.code}, message is ${err.message}`);
      });
      // 4.获取PixelMap数组
      let pixelMapList = await imageSource.createPixelMapList({
        desiredPixelFormat: image.PixelMapFormat.RGBA_8888
      });
      return pixelMapList;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to convert URI to PixelMap. Code: ${err.code}, message: ${err.message}`);
      return [];
    } finally {
      // 5.关闭文件描述符
      if (file !== null) {
        fileIo.closeSync(file.fd);
      }
    }
  }
}
```

**Q：为什么不推荐使用'file://'进行路径拼接？**

**A：**用'file://'对路径进行拼接的时候，无法对特殊字符进行处理，导致图片显示失败，而getUriFromPath方法会对路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在URI中。

**Q：服务卡片中利用fileuri.getUriFromPath进行转换后还是无法加载出图片，该如何解决？**

**A：**可以参照[刷新本地图片和网络图片](../harmonyos-guides/arkts-ui-widget-image-update.md)进行改动，在创建卡片时读取出沙箱中图片文件的fd，然后传给卡片进行展示。

**Q：如何在Image组件加载失败时，将加载中的图片替换为失败状态的图片，并支持点击重试？**

**A：**该方案仅实现加载失败时占位图的切换，不支持点击重试，适用于API Version 22之前的版本；API Version 22及以上请使用下述增强方案。

引入状态变量控制图片的加载状态，当加载失败时切换状态为“error”，具体步骤如下：

1. 引入状态变量status，并设置初始值“loading”；
2. 通过alt设置图片加载时显示的占位图，并通过状态变量status控制图片变化；
3. 在回调函数onError中设置状态变量status为“error”，实现图片切换功能。

以下为代码实现：

```ts
@Entry
@Component
struct ImageComponentExample {
  @State status: string = 'loading';
  @State loadingImg: Resource = $r('sys.media.clone_app_badge_1');
  @State errorImg: Resource = $r('sys.media.clone_app_badge_2');

  build() {
    Column() {
      Image('')
        .width(300)
        .height(300)
        .margin(15)
        .alt(this.status === 'loading' ? this.loadingImg : this.errorImg)
        .onError(() => {
          // 通过定时器延迟3s，方便观察加载中和加载失败过程图片的切换
          setTimeout(() => {
            this.status = 'error';
          }, 3000);
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

从API Version 22开始，Image组件的[alt属性](../harmonyos-references/ts-basic-components-image.md)进行了增强，支持通过alt对象分别设置加载过程中和加载失败时的占位图；reloadKey自API Version 26起支持，可通过修改reloadKey的值触发图片重新加载。基于该增强能力，结合onError回调、onComplete回调与状态变量，可实现图片加载失败时显示错误占位图并支持点击重试，具体步骤如下：

1. 通过alt对象分别设置加载中占位图placeholder与加载失败占位图error；
2. 在onError回调中将状态变量isError置为true，在onComplete回调中将isError置为false；
3. 加载失败时显示重试按钮，在按钮的点击事件中修改reloadKey的值，触发图片重新加载。

以下为代码实现：

```ts
@Entry
@Component
struct ImageRetryPage {
  @State imageUrl: string = 'https://example.cn/'; // 网络图片地址，实际使用时可替换为需要的地址
  @State reloadKey: string = Date.now().toString(); // 重试标识，修改该值可触发图片重新加载
  @State isError: boolean = false; // 是否加载失败
  @State reloadFlag: boolean = false; // 是否正在重新加载

  build() {
    Column({ space: 20 }) {
      // 通过alt对象分别配置加载中和加载失败的占位图
      Stack() {
        Image(this.imageUrl, this.reloadKey)
          .width(300)
          .height(200)
          .alt({
            placeholder: $r('app.media.img'), // 加载中占位图
            error: $r('app.media.img_1') // 加载失败占位图
          })
          .objectFit(ImageFit.Cover)
          .onError((err: ImageError) => {
            console.info(`图片加载失败: ${err.message}`);
            this.isError = true;
            this.reloadFlag = false;
          })
          .onComplete(() => {
            this.isError = false;
            console.info('图片加载成功');
            this.reloadFlag = false;
          })
        // 点击重试按钮（加载失败时显示）
        if (this.isError) {
          Button('点击重试')
            .fontSize(16)
            .onClick(() => {
              // 通过修改reloadKey触发重新加载（API 26+）
              this.reloadKey = Date.now().toString();
              this.isError = false;
              this.reloadFlag = true;
            })
        }
        if (this.reloadFlag) {
          LoadingProgress()
            .width(300)
            .height(200)
        }
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
