---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-30
title: 网络图片加载的两种方式及常见问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 网络图片加载的两种方式及常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4a5e0bca5e243966e66244b19c9ce551d5432fe7be0232b7afc9a959962d5ab9
---

## 问题现象

在开发过程中会遇到很多加载网络图片的场景，例如使用Web组件加载网络图片，使用Image组件加载网络图片。本文详细介绍了如何使用这两个组件加载网络图片以及两个组件的区别和适用场景。

## 背景知识

开发过程中，加载网络图片可以使用[Web](../harmonyos-references/arkts-apis-webview.md)组件和[Image](../harmonyos-references/ts-basic-components-image.md)组件。Web组件具有网页显示的能力，进行图片加载可以直接加载在线地址；Image为图片组件，常用于在应用中显示图片。

| 组件 | 适用类型 |
| --- | --- |
| Web | 图片在线地址。 |
| Image | 支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。 |

## 解决方案

* **方案一：使用Web组件进行图片加载。**

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
* **方案二：使用Image组件加载网络图片。**

  使用Image组件加载网络图片时，默认网络超时是5分钟，在加载网络图片的过程中，建议使用[alt](../harmonyos-references/ts-basic-components-imagespan.md#alt12)配置加载时的占位图，使用[HTTP](../harmonyos-guides/http-request.md)工具包发送网络请求，然后将返回的数据解码为Image组件中的PixelMap，图片开发可参考[图片处理](../harmonyos-guides/image-overview.md)。使用Image加载网络图片时，需要申请权限ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
  + 直接使用Image组件通过网络地址加载网络图片，代码示例如下：

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
  + 使用Image加载PixelMap解码后的多媒体像素图。

    当开发者遇到需要对图片编辑或预览，或者动态生成的图片内容，或实时视频流帧捕捉与展示等情况时，可以使用PixelMap解码图片，然后使用Image进行加载。以下示例将加载的网络图片返回的数据解码成PixelMap格式，再显示在Image组件上。
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
  <!-- 网络图片链接url -->
      <img src="" width="250" height="auto">
  </div>
  </body>

  </html>
  ```

## 常见FAQ

Q：使用Web组件进行图片加载和使用Image组件进行图片加载有什么区别？

A：使用Web组件和Image组件都支持加载本地图片和网络图片，但对于PixelMap类型图片Image组件可以直接加载，Web组件需要将PixelMap转化为base64字符串，或将其保存为本地图片并获取本地图片路径后用于加载。

Q：需要加载的图片文件名或路径中含有空格、特殊字符或者用户在填写表单时输入了一个带有空格的图片链接，或者某个API返回的图片地址中包含了未经编码的特殊字符，如何使用Image组件进行加载？

A：可以使用encodeURI编码对包含空格或特殊字符的图片地址进行编码，将这些字符替换为对应的编码形式，然后使用Image组件加载。代码示例如下：

```ts
encodeURI(''); // 网络图片链接url
```

Q：使用Image组件加载图片时，图片无法加载，如何检测图片加载失败的原因。

A：检查网络连接和网络权限配置，并在Image组件下添加监听代码，监听图片加载失败原因代码示例如下：

```ts
.onError((err: ImageError) => {
  // 图片无法加载时触发
  console.error(`Failed to do sth. Code: ${err.error?.code}, message: ${err.message}`);
})
```

Q：在请求网络图片的过程中，如何进行证书校验？

A：使用Global.getContext中的filesDir方法获取应用沙箱路径，将图片下载至沙箱路径下，再用Image加载图片。

Q：使用Web组件如何加载HTTPS链接中的HTTP图片？

A：将Web组件的[mixedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#mixedmode)属性设置为MixedMode.All来允许加载HTTP和HTTPS混合内容。
