---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1323
title: 重新初始化XComponent导致闪退
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 重新初始化XComponent导致闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c6e2bf5cc00a5640eaaac66b0253f2c7db037481f5f07b2796abf39b046f9e3
---

## 问题现象

添加条件判断是否渲染YUVView()，以模拟XComponent组件的初始化和资源释放场景。在“OpenGL图形绘制”和“YUV图像渲染”两个页签来回切换，触发条件渲染，第二次切换到“YUV图像渲染”页签时，应用闪退。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5W4YwYZyTWqg7_Q-mci5qg/zh-cn_image_0000002628599686.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/W2yTXRiOQt2lNy6Sva38DQ/zh-cn_image_0000002628759652.gif "点击放大")

## 背景知识

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)：提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。参数Id是组件的唯一标识，用于在应用程序中唯一的识别和操作该组件。
* [安全随机数](../harmonyos-guides/crypto-generate-random-number.md)：安全随机数生成器需要具备随机性，不可预测性，与不可重现性。

## 解决方案

由于第二次创建的XComponent的Id与首次创建时的Id重复，导致程序出现闪退现象。为避免此问题，应在生成XComponent时为其Id添加随机数后缀，确保每次创建的Id唯一。完整代码参考官方示例[NdkXComponent](https://gitee.com/harmonyos_samples/ndk-xcomponent)。

安全随机数代码如下：

```ts
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { CommonConstant as Common }  from '../common/CommonConstant';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

const TAG: string = 'YUVView';

@Component
export struct YUVView {
  @State isClick: boolean = true;
  private xComponentContext: Record<string, () => void> = {};

  doRandBySync() {
    let rand = cryptoFramework.createRandom();
    let len = 18;
    try {
      let randData = rand.generateRandomSync(len);
      if (randData !== null) {
        console.info(`[Sync]: rand result: ${randData.data}`);
      } else {
        console.error("[Sync]: get rand result fail!");
      }
      return randData.data;
    } catch (error) {
      console.error(`do rand failed：` + error);
      return null;
    }
  }

  aboutToAppear(): void {
    this.writeYUVFile();
  }

  build() {
    Column() {
      Column() {
        XComponent({
          id: Common.YUV_XCOMPONENT_ID + this.doRandBySync()?.toString(), // 给Id添加随机数(解决方案),
          type: XComponentType.TEXTURE,
          libraryname: Common.LIBRARY_NAME
        })
          .onLoad((xComponentContext?: object | Record<string, () => void>) => {
            if (xComponentContext) {
              this.xComponentContext = xComponentContext as Record<string, () => void>;
            }
          })
          .width($r('app.float.xcomponent_width'))
          .aspectRatio(1)
          .borderRadius($r('app.float.xcomponent_border_radius'))
          .backgroundColor(Color.White)
      }

      Row() {
        Button($r('app.string.load_yuv'))
          .fontSize($r('app.float.button_font_size'))
          .fontWeight(Common.FONT_WEIGHT_500)
          .onClick(() => {
            if (this.xComponentContext) {
              this.xComponentContext.loadYuv();
              this.isClick = false;
            }
          })
          .width(Common.BUTTON_WIDTH)
          .height($r('app.float.button_height'))
          .margin({
            bottom: $r('app.float.button_margin_bottom')
          })
          .backgroundColor(this.isClick ? $r('app.color.button_clickable') : $r('app.color.button_unclickable'))
          .stateEffect(this.isClick)
      }
      .width(Common.FULL_PERCENT)
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .layoutWeight(1)
    }
    .width(Common.FULL_PERCENT)
    .height(Common.FULL_PERCENT)
  }

  async writeYUVFile() {
    try {
      // Write the yuv file to the sandbox path.
      const resourceManager = this.getUIContext().getHostContext()!.resourceManager;
      const imageArray = await resourceManager.getMediaContent($r('app.media.ic_picture').id);
      let path: string = this.getUIContext().getHostContext()!.filesDir + '/image.yuv';
      let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      fileIo.write(file.fd, imageArray.buffer).then(() => {
        fileIo.closeSync(file);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, TAG, `write data to file failed with error message: ${err.message}, code: ${err.code}`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, TAG, `writeYUVFile failed. error code=${err.code}, message=${err.message}`);
    }
  }
}
```
