---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-21
title: 如何跟随系统深/浅色模式获取对应的资源文件
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何跟随系统深/浅色模式获取对应的资源文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4972c751296feaa7d5551ac8e9ce7db960fb23f7da9c409a757abe265b9c07fc
---

## 问题现象

深色模式下获取dark目录下的资源，浅色模式下获取base目录下的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/D20CDGIOSNmJDD2jYqQnGg/zh-cn_image_0000002628823000.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/jEaM8_RUT1OKOmeEveab9g/zh-cn_image_0000002628663114.png "点击放大")

## 背景知识

[resourceManager.getResourceManager](../harmonyos-references/js-apis-resource-manager.md#resourcemanagergetresourcemanager)获取的资源的配置（语言、深浅色、分辨率、横竖屏等）是由系统决定的，而通过[getOverrideResourceManager](../harmonyos-references/js-apis-resource-manager.md#getoverrideresourcemanager12)接口返回的对象，应用可以获取符合指定配置的资源，即差异化资源，比如在浅色模式时可以获取深色资源。

## 解决方案

* 方式一：获取与系统配置相同的资源管理器。通过getOverrideResourceManager获取对应当前系统配置对应的资源管理对象，然后调用资源接口获取对应资源即可，例如：let overrideResMgr = context.resourceManager.getOverrideResourceManager();。
* 方式二：获取指定配置的资源管理器。
  1. 通过getOverrideConfiguration获取配置：let config = context.resourceManager.getOverrideConfiguration()。
  2. 修改对应参数：config.colorMode = resourceManager.ColorMode.DARK。
  3. 将配置传入getOverrideResourceManager，获取指定配置下的资源管理器：let overrideResMgr = context.resourceManager.getOverrideResourceManager(config)。

根据系统配置获取对应图片并绘制到界面，示例代码如下：

```screen
import { ConfigurationConstant, Context } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

export class Point {
  x: number = 0;
  y: number = 0;

  set(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

@Entry
@Component
struct GetResource {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  hostContext = this.getUIContext().getHostContext()?.getApplicationContext();
  isDarkMode: boolean = false;
  mCircleBg: image.PixelMap | undefined = undefined;
  centerPoint = new Point();

  // 获取资源并转化为PixelMap
  image2PixelMap(context: Context, resource: Resource) {
    // 获取对应系统颜色模式配置下的资源管理器
    let overrideResMgr = context.resourceManager.getOverrideResourceManager();
    let data = overrideResMgr.getMediaContentSync(resource.id);

    let arrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
    let imageSource: image.ImageSource = image.createImageSource(arrayBuffer);
    let value = imageSource.getImageInfoSync();
    let opts: image.DecodingOptions = {
      editable: true,
      desiredSize: {
        height: value.size.height,
        width: value.size.width
      }
    };
    return imageSource.createPixelMapSync(opts);
  }

  // 清除并绘制图片
  draw() {
    this.mCircleBg = this.image2PixelMap(this.hostContext as Context, $r('app.media.theme_joystick_big_circle_bg'));
    this.context.clearRect(-this.centerPoint.x, -this.centerPoint.y, this.centerPoint.x * 2, this.centerPoint.y * 2);
    let innerR = 150;
    this.context.drawImage(this.mCircleBg, -innerR, -innerR, innerR * 2, innerR * 2);
  }

  build() {
    Column() {
      Text('适配颜色(点我切换)')
        .fontColor($r('app.color.text_primary'))
        .fontSize(24)
        .margin({ top: 100 })
        .onClick(() => {
          if (this.isDarkMode) {
            this.hostContext?.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
            this.isDarkMode = false;
            this.draw();
          } else {
            this.hostContext?.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
            this.isDarkMode = true;
            this.draw();
          }
        })
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            let measuredWidth = this.context.width;
            let measuredHeight = this.context.height;
            this.centerPoint.set(measuredWidth / 2, measuredHeight / 2);
            this.context.clearRect(-this.centerPoint.x, -this.centerPoint.y, this.centerPoint.x * 2,
              this.centerPoint.y * 2);
            this.context.translate(this.centerPoint.x, this.centerPoint.y);
            this.draw();
          })
      }
      .width('100%')
      .height('auto')
    }
    .height('100%')
    .padding({ left: 16, right: 16 })
    .width('100%')
    .backgroundColor($r('app.color.bg_primary'))
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
  }
}
```

## 常见FAQ

Q：为什么context.resourceManager只能获取LIGHT模式下的资源？

A：当前接口获取系统资源管理ResourceManager对象中的Configuration为默认值，颜色模式默认是LIGHT。
