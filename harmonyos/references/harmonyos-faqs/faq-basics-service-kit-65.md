---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-65
title: 使用request.downloadFile下载图片到沙箱，图片无法打开
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 使用request.downloadFile下载图片到沙箱，图片无法打开
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c60443766673f6ffbf0362cf7160ab3bf0cd0431e9da47dd222b7c766e70a1f7
---

## 问题现象

使用request.downloadFile方法下载网络图片到沙箱，图片不能直接打开查看：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/sjnxaz-aSGOjkCJ2Qs9EZw/zh-cn_image_0000002628613956.png "点击放大")

关键代码如下：

```ts
request.downloadFile(context, {
  url: 'http://www.example/fdb17952b79f46b3a20b9fc1d239177b_20250724145715AecsMOQ031.png', // 示例网址
  // url:'https://copyright.bdstatic.com/vcg/creative/cc9c744cf9f7c864889c563cbdeddce6.jpg',
  filePath: (this.getUIContext().getHostContext())?.filesDir + '/test.png'
})
```

问题原因是什么，该如何解决？

## 背景知识

* [request.downloadFile](../harmonyos-references/js-apis-request.md#requestdownloadfile9)：创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。
* [http.createHttp](../harmonyos-references/js-apis-http.md#httpcreatehttp)：创建一个HTTP请求，里面包括发起请求、中断请求、订阅/取消订阅HTTP Response Header事件。
* [request](../harmonyos-references/js-apis-http.md#request)：根据url地址，发起HTTP网络请求，使用callback方式作为异步方法。

## 问题定位

1. 直接打开问题图片的链接是可以看到图片的；

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jw-811-yTna-aErgIHglNA/zh-cn_image_0000002658973159.png "点击放大")

   使用request.downloadFile方法下载该图片到沙箱，然后导出到PC，再拖拽到浏览器，图片也不能查看了；

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/9NQn35w-TmC59ddnom9-RQ/zh-cn_image_0000002658853205.png)
2. 查看图片的二进制码，发现第二张图片和第一张图片的文件头有差异，多了以下高亮区域里的数据：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/aRyfjlmdT9CDbx0fAjVZKQ/zh-cn_image_0000002628773846.png "点击放大")
3. 读取前几个字节为1F 8B 08，其中1F 8B表明为gzip压缩，而08表示为deflate压缩。下载的是未解码的文件，所以图片无法显示。

## 分析结论

1. request.downloadFile方法下载的是未解码的文件，所以图片无法显示。
2. 尝试使用http.createHttp().request(url: string, callback: AsyncCallback<HttpResponse>)方法请求图片资源，发现Image组件能够显示，所以考虑使用这种方式获取图片数据。

## 修改建议

使用http.createHttp().request(url: string, callback: AsyncCallback)方法请求图片数据，然后把接收的数据写入沙箱，示例代码如下：

```ts
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import fs from '@ohos.file.fs';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('下载图片')
          .onClick(async () => {
            await this.getPicture();
          });
      }
      .width('100%');
    }
    .height('100%');
  }

  /**
   * 通过http的request方法从网络下载图片资源
   */
  async getPicture() {
    // 此处地址实际使用过程中替换为真实地址
    http.createHttp().request('xx.xx.xx', (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        // 下载失败时弹窗提示检查网络，不执行后续逻辑
        this.getUIContext().getPromptAction().showToast({
          message: '请求失败',
          duration: 2000
        });
        console.error(`error.code: ${error.code}, error.message: ${error.message}`);
        return;
      }

      let context = this.getUIContext().getHostContext();
      // 获取沙箱路径（如：filesDir）
      if (context) {
        let filePath = context.filesDir + '/test.png';
        // 创建文件并写入数据
        let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
        try {
          fs.writeSync(file.fd, data.result as ArrayBuffer);
        } finally {
          fs.closeSync(file);
        }
      }
    });
  }
}
```
