---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-142
title: 如何实现长按识别H5页面的二维码图片
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何实现长按识别H5页面的二维码图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:918018a0fe4f8d545596c8e224cf946a252c9201f926010cfe6d9820ffa61326
---

## 问题现象

当前在H5页面长按二维码图片会触发拖拽动作，如何禁用图片拖拽事件并实现长按识别H5页面的二维码图片。

## 背景知识

* [应用侧调用前端页面函数](../harmonyos-guides/web-in-app-frontend-page-function-invoking.md)：应用侧可以通过runJavaScript()和runJavaScriptExt()方法调用前端页面的JavaScript相关函数。
* [onContextMenuShow](../harmonyos-references/arkts-basic-components-web-events.md#oncontextmenushow9)：长按特定元素（例如图片，链接）或鼠标右键，弹出菜单。
* [detectBarcode.decodeImage](../harmonyos-references/scan-imagedecode.md#decodeimage)：通过配置参数调用图像数据识码能力，使用Promise异步回调返回识码结果。

## 解决方案

长按识别H5页面的二维码图片实现步骤如下：

1. 通过runJavaScript禁用图片的拖拽事件。
2. 通过onContextMenuShow监听图片的长按事件并获取到图片的url。
3. 根据url获取网络图片数据并通过detectBarcode.decodeImage接口识别图片中的二维码。

样例代码如下：

Web组件绑定onContextMenuShow监听图片长按事件，获取图片的url并解码。

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { detectBarcode, scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebRecognizeQRcode {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // src需要替换为带有二维码图片的网址
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd(() => {
          // 禁用图片拖拽
          this.executeDisableDragScript();
        })
        .onContextMenuShow((event) => {
          if (event.param.getMediaType() === ContextMenuMediaType.Image) {
            // 获取图片并识别二维码
            this.scanQRFromWebImage(event.param.getSourceUrl());
            event.result.closeContextMenu();
          }
          return true;
        })
        .fileAccess(false)
        .geolocationAccess(false)
        .domStorageAccess(true);
    };
  }

  /**
   * 禁用H5中图片的拖拽事件
   */
  executeDisableDragScript() {
    const jsCode = `
          // 禁用所有图片拖拽
          const images = document.getElementsByTagName('img');
          for (let i = 0; i < images.length; i++) {
            images[i].draggable = false;
          }

          // 监听动态加载的图片
          new MutationObserver(mutations => {
            mutations.forEach(mutation => {
              mutation.addedNodes.forEach(node => {
                if (node.tagName === 'IMG') {
                  node.draggable = false;
                }
              });
            });
          }).observe(document.body, { childList: true, subtree: true });
        `;

    this.controller.runJavaScript(jsCode, (error: BusinessError) => {
      if (error) {
        hilog.error(0x0001, 'runJavaScript', `执行JavaScript失败: ${error.message}`);
      }
    });
  }

  /**
   * 根据url获取网络图片数据。
   */
  private async downloadImage(url: string): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {
      const httpRequest = http.createHttp();
      httpRequest.request(
        url,
        {
          method: http.RequestMethod.GET,
          expectDataType: http.HttpDataType.ARRAY_BUFFER
        },
        (err, data) => {
          if (err) {
            reject(new Error(`图片获取失败: ${err.message}`));
            return;
          }
          if (data && data.result) {
            resolve(data.result as ArrayBuffer);
          } else {
            reject(new Error('未获取到图片数据'));
          }
        }
      );
    });
  }

  /**
   * 识别图中二维码。
   */
  async scanQRFromWebImage(url: string) {
    this.getUIContext().getPromptAction().showToast({ message: '开始识别二维码...' });
    try {
      // 1.下载网络图片
      const imageData = await this.downloadImage(url);
      // 2.创建ImageSource
      const imageSource = image.createImageSource(imageData);
      const pixelMap = await imageSource.createPixelMap();
      // 3.二维码识别
      const result = await this.decodeImageBuffer(pixelMap);

      if (result) {
        this.getUIContext().showAlertDialog({
          message: result
        });
      } else {
        this.getUIContext().getPromptAction().showToast({ message: '识别失败' });
      }

      // 4.释放资源
      pixelMap.release();
      imageSource.release();
    } catch (error) {
      const err = error as BusinessError;
      this.getUIContext().getPromptAction().showToast({ message: err.message });
    }
  }

  async decodeImageBuffer(pixelMap: image.PixelMap) {
    pixelMap.convertPixelFormat(image.PixelMapFormat.NV12);
    let info = await pixelMap.getImageInfo();
    let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
    let buffer = new ArrayBuffer(pixelBytesNumber);
    await pixelMap.readPixelsToBuffer(buffer);
    let byteImg: detectBarcode.ByteImage = {
      byteBuffer: buffer,
      width: info.size.width,
      height: info.size.height,
      format: detectBarcode.ImageFormat.NV21
    };
    let options: scanBarcode.ScanOptions =
      { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: false };
    try {
      return detectBarcode.decodeImage(byteImg, options).then((result: detectBarcode.DetectResult) => {
        return JSON.stringify(result);
      }).catch((error: BusinessError) => {
        hilog.error(0x0001, '[ScanCode]',
          `Failed to get DetectResult by promise with options. Code: ${error.code}, message: ${error.message}`);
      });
    } catch (error) {
      hilog.error(0x0001, '[ScanCode]',
        `Failed to get DetectResult by promise with options. Code: ${error.code}, message: ${error.message}`);
    }
  }
}
```
