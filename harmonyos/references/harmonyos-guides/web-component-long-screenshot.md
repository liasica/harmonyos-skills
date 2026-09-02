---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-long-screenshot
title: Web组件长截图
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > Web组件长截图
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:23+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:57c2423d6088eed74cb7c172fbe0830479d2cc7474148402adee3943b44b1983
---

## 场景描述

Web组件的长截图功能可以对网页内容进行截图，旨在为用户提供快速便捷的数据信息分享和保存方式，确保用户能够完整地捕获和分享浏览的网页信息。

## 实现效果

点击“一键截图”按钮即可完成整个网页的长截图，并可将截图保存至相册。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/6E70y2y2TrCg2vFHgJTldw/zh-cn_image_0000002706834088.gif)

## 功能实现

Web组件可以通过滚动截图方案以及使用WebView提供的[webPageSnapshot](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#webpagesnapshot12)进行长截图。其中WebView提供的webPageSnapshot方法比较适合结构简单、静态元素的页面长截图，如果网页中有动态资源，结构相对复杂，比如有固定的标题头等，推荐使用滚动截图方案。

**使用滚动截图的方式进行网页长截图**

Web组件滚动长截图和[滚动组件长截图](../best-practices/bpta-long-snapshot-practice.md#section1398314519326)开发流程大体一样，主要是控制组件的滚动的方法不同。List组件使用的是[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)，而Web组件使用的是[webViewController](../harmonyos-references/arkts-basic-components-web-t.md#webviewcontroller9)。

在滚动截图过程中，webViewController负责控制Web组件的滚动，通过调用[webViewController.scrollBy](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#scrollby)方法来实现。为了判断是否已滚动到底部，使用this.webViewController.getPageHeight() 方法获取网页内容的总高度，详情可参考[获取网页内容高度](web-getpage-height.md)，并将当前偏移量this.curYOffset加上组件自身的高度与网页总高度进行比较。如果两者的和小于网页总高度，则表示尚未触底。

```ts
async snapAndMerge() {
  try {
    this.scrollYOffsets.push(this.curYOffset);
    const pixelMap = await this.getUIContext().getComponentSnapshot().get(WEB_ID);
    let area: image.PositionArea =
      await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.webComponentWidth,
        this.webComponentHeight);
    this.areaArray.push(area);
    if (Math.ceil(this.curYOffset + this.webComponentHeight) < this.webviewController.getPageHeight()) {
      this.webviewController.scrollBy(0, this.scrollHeight, 500);
      await CommonUtils.sleep(600)
      await this.snapAndMerge();
    } else {
      this.mergedImage =
        await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
          this.scrollYOffsets[this.scrollYOffsets.length - 1], this.webComponentHeight);
    }
  } catch (err) {
    let error = err as BusinessError;
    Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
  }
}
```

**使用webPageSnapshot()方法进行网页长截图**

Web组件使用[webPageSnapshot()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#webpagesnapshot12)方法实现长截图的步骤如下：

1. Web初始化，调用enableWholeWebPageDrawing()方法开启网页全量绘制能力。

   ```ts
   aboutToAppear(): void {
     try {
       webview.WebviewController.initializeWebEngine();
       webview.WebviewController.enableWholeWebPageDrawing();
       webview.WebviewController.prepareForPageLoad(EXAMPLE_URL, true, 2);
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `web snapshot init err, errCode: ${error.code}, error message: ${error.message}`);
     }
   }
   ```
2. 获取网页内容高度和宽度。

   ```ts
   async getWebSize() {
     const SCRIPT = '[document.documentElement.scrollWidth, document.documentElement.scrollHeight]';
     try {
       this.webviewController.runJavaScriptExt(SCRIPT).then((result) => {
         if (result.getType() === webview.JsMessageType.ARRAY) {
           this.h5Width = (result.getArray() as number[])[0];
           this.h5Height = (result.getArray() as number[])[1];
           Logger.info(TAG, `h5Width is ${this.h5Width}, h5Height is ${this.h5Height}`);
         }
       }).catch((error: BusinessError) => {
         Logger.error(TAG, `getWebSize exception, errCode: ${error.code}, error message: ${error.message}`);
       });
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(TAG, `getWebSize failed, errCode: ${err.code}, error message: ${err.message}`);
     }
   }
   ```
3. 调用webPageSnapshot()方法，进行网页截图。

   ```ts
   async webSnapshot() {
     try {
       this.webviewController.webPageSnapshot({ id: WEB_ID, size: { width: this.h5Width, height: this.h5Height } },
         async (error, result) => {
           if (result) {
             this.longPixelMap = result.imagePixelMap;
           }
         });
     } catch (error) {
       let err = error as BusinessError;
       Logger.error(TAG, `webSnapshot err, errCode: ${err.code}, error message: ${err.message}`);
     }
   }
   ```

**说明** 

加载网络html文件时，需要在entry/src/main路径下的module.json5中配置网络权限。示例代码如下所示：

```json5
{
 "module": {
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     }
   ]
 }
}
```
