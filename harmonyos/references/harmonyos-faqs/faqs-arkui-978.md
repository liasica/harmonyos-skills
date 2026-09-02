---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-978
title: 停止XComponent渲染数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 停止XComponent渲染数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3d0aae712ba9c67f233d92cb8a03ead9cdb304b99eee877fb89abcbbc3589125
---

## 问题现象

使用XComponent组件进行YUV数据渲染时，如何停止XComponent渲染数据？

## 背景知识

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)提供一个用于图形绘制和媒体数据写入的Surface，能够将其嵌入到视图中，并支持应用自定义Surface的位置和大小。
* ArkTS提供了渲染控制能力。[条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)可根据应用状态，使用if、else和else if渲染相应的UI内容。

## 解决方案

1. 获取XComponent的完整工程代码如下：[基于XComponent组件实现OpenGL图形绘制及YUV图像渲染功能](https://gitee.com/harmonyos_samples/ndk-xcomponent)。
2. YUVView页面是一个使用XComponent组件进行渲染的实例。现对该页面进行如下修改：为XComponent组件添加条件渲染逻辑，当flag值为true时渲染该组件，为false时则销毁该组件，并添加onDestroy方法以在控制面板中查看组件销毁状态。
3. 在Column组件中添加一个销毁按钮，并为其绑定点击事件。当点击按钮且flag为true时，将其值改为false，点击销毁按钮时，触发XComponent组件的onDestroy函数，表示该组件已被销毁。

```ts
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
export struct YUVViewStopPage {
  isClick: boolean = true;
  xComponentContext: Record<string, () => void> = {};
  @State flag: boolean = true;

  aboutToAppear(): void {
    this.writeYUVFile();
  }

  build() {
    Column() {
      Column() {
        if (this.flag) { // flag为true时渲染该组件，为false时销毁该组件
          XComponent({
            id: 'XComponentId',
            type: XComponentType.TEXTURE,
            libraryname: 'LIBRARY_NAME'
          })
            .onLoad((xComponentContext?: object | Record<string, () => void>) => {
              if (xComponentContext) {
                this.xComponentContext = xComponentContext as Record<string, () => void>;
              }
            })
            .width('100%')
            .aspectRatio(1)
            .borderRadius(15)
            .backgroundColor(Color.White)
            .onDestroy(() => { // 判断是否销毁
              console.info(`XComponent已销毁`);
            });
        }
      };

      Column() {
        Button('销毁')
          .fontSize(18)
          .fontWeight(20)
          .width('100%')
          .height('20%')
          .margin({
            bottom: 50
          })
          .onClick(() => {
            if (this.flag === true) {
              this.flag = !this.flag;
            }
          });
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .layoutWeight(1);
    }
    .width('100%')
    .height('100%');
  }

  async writeYUVFile() {
    try {
      const resourceManager = this.getUIContext().getHostContext()!.resourceManager;
      const imageArray = await resourceManager.getMediaContent($r('app.media.startIcon').id); // 此处仅为样例，请开发者更换为可用图片
      let path: string = this.getUIContext().getHostContext()!.filesDir + '/image.yuv';
      let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      fileIo.write(file.fd, imageArray.buffer).then(() => {
        fileIo.closeSync(file);
      }).catch(() => {
      });
    } catch (error) {
    }
  }
}
```
