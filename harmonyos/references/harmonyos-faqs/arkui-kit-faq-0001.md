---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0001
title: Image组件图片加载与缓存常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > Image组件图片加载与缓存常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:52+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:5669f8c29f688e15455338cfaf82f9bb279724489eacc08e53ec249950ad10b1
---

**Q：如何使用Image组件加载本地图片？**

**A**：Image组件加载本地图片有以下几种方案：

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
* 方案三、通过base64字符串加载。(注意：需要将this.base64ImageData替换成对应的图片资源)。实现方式：

  ```ts
  Image('data:image/jpg;base64,' + this.base64ImageData)
  ```

  + 特点：
    - 适合加载小型图片或需要动态生成的图片。
    - 需注意字符串长度对性能的影响。

**Q：Image组件如何加载apng图片？**

**A**：可以通过[ohos\_apng](https://gitee.com/openharmony-sig/ohos_apng)库来实现。

**Q：在开发过程中会遇到很多加载网络图片的场景，例如使用Web组件加载网络图片，使用Image组件加载网络图片。如何使用这两个组件加载网络图片以及两个组件的区别和适用场景是什么？**

**A**：方案一：使用Web组件进行图片加载。

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

  + ArkTS侧：

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
  + H5侧：

    ```html
    <!-- main/resources/resfile/index.html -->
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
    <!--    网络图片链接url-->
        <img src="" width="250" height="auto">
    </div>
    </body>

    </html>
    ```

**Q：使用Web组件进行图片加载和使用Image组件进行图片加载有什么区别？**

**A**：使用Web组件和Image组件都支持加载本地图片和网络图片，但对于PixelMap类型图片Image组件可以直接加载，Web组件需要将PixelMap转化为base64字符串，或将其保存为本地图片并获取本地图片路径后用于加载。

**Q：需要加载的图片文件名或路径中含有空格、特殊字符或者用户在填写表单时输入了一个带有空格的图片链接，或者某个API返回的图片地址中包含了未经编码的特殊字符，如何使用Image组件进行加载？**

**A**：可以使用encodeURI编码对包含空格或特殊字符的图片地址进行编码，将这些字符替换为对应的编码形式，然后使用Image组件加载。代码示例如下：

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

**A**：检查网络连接和网络权限配置，并在Image组件下添加监听代码，监听图片加载失败原因代码示例如下：

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

**A**：使用Global.getContext中的filesDir方法获取应用沙箱路径，将图片下载至沙箱路径下，再用Image加载图片。

**Q：使用Web组件如何加载HTTPS链接中的HTTP图片？**

**A**：将Web组件的[mixedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#mixedmode)属性设置为MixedMode.All来允许加载HTTP和HTTPS混合内容。

**Q：Image组件加载网络图片，PixelMap与直接访问url有什么区别？**

**A**：两者都支持加载网络图片。使用PixelMap方式时，可以对图片进行更多效果设置，功能更强大。

参考链接：[Image](../harmonyos-references/ts-basic-components-image.md)、[Interface (PixelMap)](../harmonyos-references/arkts-apis-image-pixelmap.md)。

**Q：Image组件是否有缓存机制？**

**A**：

1. Image的缓存策略：Image模块提供了三级Cache机制，解码后内存图片缓存、解码前数据缓存、物理磁盘缓存。在加载图片时会逐级查找，如果在Cache中找到之前加载过的图片则提前返回对应的结果。
2. Image组件如何配置打开和关闭缓存：

* 内存图片缓存：通过[setImageCacheCount](../harmonyos-references/js-apis-system-app.md#setimagecachecount7)接口打开缓存，如果希望每次联网都获取最新资源，可以不设置（默认为0），不进行缓存。
* 磁盘缓存：磁盘缓存是默认开启的，默认值为100M，可以将[setImageFileCacheSize](../harmonyos-references/js-apis-system-app.md#setimagefilecachesize7)的值设置为0关闭磁盘缓存。
* 解码前数据缓存：通过[setImageRawDataCacheSize](../harmonyos-references/js-apis-system-app.md#setimagerawdatacachesize7)设置内存中缓存解码前图片数据的大小上限，单位为字节，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。

setImageCacheCount、setImageRawDataCacheSize和setImageFileCacheSize这三个图片缓存接口灵活性不足，后续不再演进，对于复杂情况，建议使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)。
