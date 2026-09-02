---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1045
title: 应用内的图片拖拽进小艺后提示没有收到图片数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 应用内的图片拖拽进小艺后提示没有收到图片数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fb4e2581490d55e6332c4d6f0c1906a2e6eb3ccd078f15d54313e7109c7b292c
---

## 问题现象

网页中的图片可以拖拽进小艺进行分析处理，开发者应用中的图片拖拽给小艺，小艺提示“该应用未能提供实际的图片给小艺，小艺无法为你处理”。

## 背景知识

* [统一拖拽](../best-practices/bpta-unified-drag-and-drop.md)：用户通过手势（如用手指、鼠标或触控笔按住并移动）在应用程序之间及其内部进行数据传输。
* [拖入小艺和中转站](../best-practices/bpta-unified-drag-and-drop.md#section1289155519508)：将数据拖入系统的中转站，可以实现跨应用数据拖拽和跨设备数据流转。将数据拖入小艺，可以利用系统的AI能力处理拖拽数据。

## 解决方案

[拖拽到小艺后显示不支持处理此类数据](../best-practices/bpta-unified-drag-and-drop.md#section1567625181513)是因为小艺不支持读取资源文件的uri，需要将资源文件的图片转换成PixelMap后，用PixelMap数据初始化图片。代码如下：

```ts
/*
 *
 *   Copyright (c) 2025 Huawei Device Co., Ltd.
 *   Licensed under the Apache License, Version 2.0 (the ""License"");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an ""AS IS"" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 *
 */
import { common } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State imageUrl: Resource | string | PixelMap = $rawfile('shineImage.png');
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  fileName: string = 'shineImage.png';

  build() {
    RelativeContainer() {
      Column() {
        Image(this.imageUrl)
          .width(`200vp`)
          .height(`300vp`)
          .margin({ bottom: 50 })
        Button('转换成PixelMap初始化图片').onClick(() => {
          this.ChangeImageFromPixelMap();
        }).borderRadius(5)
          .backgroundColor(Color.Brown)
      }
      .alignRules({
        center: { anchor: '__container__', align: VerticalAlign.Center },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })

    }
    .height('100%')
    .width('100%')
  }

  ChangeImageFromPixelMap(): void {
    try {
      this.context.resourceManager.getRawFileContent(this.fileName, (err, data) => {
        if (err) {
          console.log(`get RawFile error:${JSON.stringify(err)}`);
          return;
        }
        let ops: image.SourceOptions = {
          sourceDensity: 98,
        };
        let imageSource: image.ImageSource = image.createImageSource(data.buffer as ArrayBuffer, ops);
        imageSource.createPixelMap().then((commodityPixelMap) => {
          this.imageUrl = commodityPixelMap;
        });
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`copy directory failed with error message: ${JSON.stringify(err)}`);
    }
  }
}
```

需要将下图另存为shineImage.png。并且复制到工程的rawfile目录下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Q2mpW6ITSxa87xs2P7az6g/zh-cn_image_0000002658924757.png "点击放大")

## 总结

网络图片、沙箱图片都可以直接拖进小艺，因为rawfile目录中的资源文件会被直接打包进应用，不经过编译，也不会分配资源ID，通常rawfile/resfile目录下文件/文件夹无法直接在应用中读写。
