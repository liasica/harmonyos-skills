---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-38
title: 如何显示图片验证码
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何显示图片验证码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f9b5c2698de4a5880578c4b3ca59d73ef140a5b529cf904802c6ecf2a0422056
---

## 问题现象

登录页面需通过接口获取图片验证码并展示，HarmonyOS未提供其他平台的Bitmap类型，无法直接解析接口返回的二进制图片数据并渲染到UI。这导致验证码功能阻塞，影响登录流程的核心安全校验。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Vq_skhLbTruJq_Wb_ZTuFQ/zh-cn_image_0000002658853165.gif "点击放大")

## 背景知识

* 图像处理机制差异：HarmonyOS使用[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)作为图像处理的核心类型（而非其他平台的Bitmap），需通过@kit.ImageKit模块的[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)将二进制数据或文件描述符转换为可渲染对象。
* Image组件数据源要求：[Image组件](../harmonyos-references/ts-basic-components-image.md)支持三种数据源：本地资源路径（string）、网络地址（需安全策略）或PixelMap对象。接口返回的二进制流需转换为上述任一格式才能显示。

## 解决方案

通过分阶段处理实现验证码加载：

1. 下载图片到本地：首先需要获取[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)权限，然后使用@kit.BasicServicesKit的[request.downloadFile()](../harmonyos-references/js-apis-request.md#requestdownloadfile9)将接口返回的图片保存至应用沙箱路径，注意生成唯一文件名（如时间戳）避免缓存冲突。
2. 转换为可渲染资源。

* 方案一：直接使用本地URI（推荐静态图）

  通过[fileUri.getUriFromPath()](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)获取文件URI，赋值给Image组件的src属性。
* 方案二：生成PixelMap（需动态调整图片属性）

  适用于需缩放/裁剪验证码的场景。

完整示例参考如下：

```ts
import { BusinessError, request } from '@kit.BasicServicesKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct DownLoadFileDemo {
  @State imageUrl: PixelMap | string | undefined = undefined;
  @State imageUrl1: PixelMap | string | undefined = undefined;

  build() {
    Column({ space: 20 }) {
      Button('获取网络图片').onClick(() => {
        this.downloadFile();
      })
      Image(this.imageUrl).height(200).width(200).objectFit(ImageFit.Contain)
      Image(this.imageUrl1).height(200).width(200).objectFit(ImageFit.Contain)
    }.justifyContent(FlexAlign.Center).width('100%').height('100%')
  }

  downloadFile() {
    let tempPath = this.getUIContext().getHostContext()!.filesDir + '/' + new Date().getTime() + '.gif';
    try {
      request.downloadFile(this.getUIContext().getHostContext(), {
        // 通过request.downloadFile方法下载到本地之后展示，需要将url替换成网络图片地址
        url: '',
        header: { 'deviceid': '' },
        filePath: tempPath
      }).then((downloadTask: request.DownloadTask) => {
        downloadTask.on('complete', async () => {
          console.info('Download complete!');
          // 方式一：直接使用本地uri展示，也可以展示gif动态效果
          this.imageUrl = fileUri.getUriFromPath(tempPath);
          // 方式二：本地文件转为pixelMap展示
          let file = fileIo.openSync(tempPath, fileIo.OpenMode.READ_ONLY);
          let imageSource: image.ImageSource = image.createImageSource(file.fd);
          let opts: image.InitializationOptions = {
            editable: false,
            pixelFormat: image.PixelMapFormat.RGBA_8888,
            alphaType: 0,
            size: { height: 100, width: 100 }
          };
          this.imageUrl1 = await imageSource.createPixelMap(opts);
        });
      }).catch((err: BusinessError) => {
        console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (error) {
      const errorMessage: string = JSON.stringify(error);
      console.error(`Invoke downloadFile failed, error is ${errorMessage}`);
    }
  }
}
```
