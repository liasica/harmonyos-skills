---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-564
title: Image组件加载在线图片报错
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Image组件加载在线图片报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d5c5b288cebb33dd7a5393c8ef38a6182d606ef9be2df2c0c43ca4e0a388d2c2
---

## 问题现象

Image组件加载在线图片失败，可能是什么原因导致的？如何解决？

## 背景知识

在应用中经常会需要显示一些图片，例如：按钮中的icon、网络图片、本地图片等。在应用中显示图片需要使用Image组件实现，Image支持多种图片格式，包括png、jpg、bmp、svg、gif和heif，具体用法请参考[Image](../harmonyos-references/ts-basic-components-image.md)组件。

## 问题定位

1. 使用网络图片时，需要申请权限ohos.permission.INTERNET，检查module.json5是否有如下配置。

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     }
   ]
   ```
2. 确保图片能在互联网上访问，可以在浏览器中访问图片以确保图片有效。
3. 给Image组件添加onError方法，根据错误日志定位可能的原因：

   ```ts
   Image('https://example.com/example.png').width(100)
     .onError((error: ImageError) => {
       console.error('[ImageError]', `${error.message}`)
     })
   ```

## 分析结论

Image组件加载网络图片报错，可能有以下原因：

1. 没有申请ohos.permission.INTERNET权限。
2. 图片本身无法在互联网访问，比如只有在特定网络或者VPN场景才能访问。
3. 图片链接存在非法字符，比如url存在空格没有转义：

   ```txt
   [ImageError] http task of url xxx.jpg response code 0, msg from netStack: URL using bad/illegal format or missing URL
   ```
4. 图片在服务端可能加了限制，可能是SSL证书、referer、User-Agent等：

   ```txt
   [ImageError] http task of url xxx.jpg failed, response code 403
   ```

## 修改建议

* 若图片链接存在非法字符，比如空格，可以转义下url：

  ```ts
  Image('https://xxx x.png'.replace(' ', '%20')).width(100);
  ```
* 若图片链接存在非法字符又存在中文，比如空格和中文，可以对url转码：

  ```ts
  Image(encodeURI('https://xxx x中文.png')).width(100);
  ```
* 若图片存在SSL证书、referer、User-Agent等限制，可以用如下方式解决：
  1. 可以把图片下载之后再显示，参考示例如下。

     ```ts
     import { http } from '@kit.NetworkKit';
     import { image } from '@kit.ImageKit';
     import { BusinessError } from '@kit.BasicServicesKit';

     @Entry
     @Component
     struct Page {
       @State pixelMap: PixelMap | undefined = undefined;
       imgUrl: string = 'https://xxx/xxx.jpg'; // 替换在线url图片

       build() {
         Column() {
           Text('加载url显示');
           Image(this.imgUrl).width('200lpx').height('200lpx')
             .onError((error: ImageError) => {
               console.error('error:', error.message);
             });
           Button('下载图片').onClick(() => {
             // 请求头
             let header: Record<string, string | number> = {
               'userAgent': 'Mozilla/5.0'
             };
             http.createHttp().request(
               // 在线图片url
               this.imgUrl,
               // 发起请求可选参数的类型和取值范围
               {
                 expectDataType: http.HttpDataType.ARRAY_BUFFER,
                 header: header
               }
             ).then(async (res) => {
               // 将图片资源转为像素图（PixelMap）
               this.pixelMap = await image.createImageSource(res.result as ArrayBuffer).createPixelMap();
             }).catch((err: BusinessError) => {
               console.error(`Failed to request. Code is ${err.code}, message is ${err.message}`);
             });
           });
           Text('下载图片后显示');
           Image(this.pixelMap).width('200lpx');
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
  2. 配合服务端添加请求头。由于Image组件暂时不支持添加自定义的请求头，推荐使用[三方库ImageKnife](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fimageknife/v/3.2.7)的参数headerOption设置请求头：

     ```ts
     import { ImageKnifeComponent, ImageKnifeOption } from '@ohos/imageknife';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { rcp } from '@kit.RemoteCommunicationKit';

     // 自定义下载方法
     @Concurrent
     async function custom(context: Context, src: string | PixelMap | Resource): Promise<ArrayBuffer | undefined> {
       return new Promise((resolve, reject) => {
         if (typeof src === 'string') {
           const sessionConfig: rcp.SessionConfiguration = {
             headers: {
               // 添加需要的header'userAgent': 'customAgent',
             },
           };
           const session = rcp.createSession(sessionConfig);
           let req = new rcp.Request(src, 'GET');
           session.fetch(req).then((response) => {
             if (response.statusCode === 200) {
               let buffer = response.body;
               resolve(buffer);
             } else {
               reject('rcp code:' + response.statusCode);
             }
           }).catch((err: BusinessError) => {
             reject(`error rcp src:${err.message}`);
           });
         }
       });
     }

     @Entry
     @Component
     struct Index {
       @State optionErr: ImageKnifeOption = {
         loadSrc: 'https://xxx/xxx.jpg', // 替换在线url图片
         customGetImage: custom
       };

       build() {
         Column() {
           ImageKnifeComponent({ imageKnifeOption: this.optionErr }).width(300).height(300);
         };
       }
     }
     ```
