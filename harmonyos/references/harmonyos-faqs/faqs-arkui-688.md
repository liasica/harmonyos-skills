---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-688
title: 如何让图片显示为圆形
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何让图片显示为圆形
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:a40255cff4756f3e5f1fe5173c16d49357d641af488d6780ea14332b16aa1a50
---

## 问题现象

从相册选择一张图片，当使用Image组件加载图片或通过drawImage方法将图片绘制到Canvas画布时，默认显示为矩形。如何实现加载后图片的圆形显示效果？

## 背景知识

* [borderRadius](../harmonyos-references/ts-universal-attributes-border.md#borderradius)用于设置边框的圆角。圆角大小受组件尺寸限制，最大值为组件宽或高的一半。当组件宽高一致时，设置borderRadius值为宽高的一半即可实现组件圆形展示。
* [使用PhotoPicker组件访问图片/视频](../harmonyos-guides/component-guidelines-photoviewpicker.md)：当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)是画笔，用于绘制内容到Canvas上。以下均为CanvasRenderingContext2D的方法。
  + [arc](../harmonyos-references/ts-components-canvas-common-method.md#arc)方法用于绘制弧线路径。
  + [clip](../harmonyos-references/ts-components-canvas-common-method.md#clip)方法用于设置裁剪路径。
  + [drawImage](../harmonyos-references/ts-components-canvas-common-method.md#drawimage)方法可以将一张ImageBitmap或PixelMap类型的图片绘制到Canvas上。

## 解决方案

**场景一**：给Image组件设置borderRadius属性，大小为宽高的一半。

示例代码如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State uri: string = '';

  build() {
    Column() {
      Image(this.uri)
        .width(200)
        .height(200)
        .borderRadius(100)
        .margin({ top: 100, bottom: 30 });
      Button('加载图片')
        .onClick(() => {
          // 创建图片选择配置对象
          const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
          // 设置MIME类型过滤器：仅显示图片类型（排除视频等）
          photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
          // 设置最大选择数量为1（单选模式）
          photoSelectOptions.maxSelectNumber = 1;
          // 初始化URI存储数组（用于接收选择结果）
          let uris: Array<string> = [];
          // 创建相册选择器实例
          const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
          // 调用相册选择器并处理结果
          photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            // 获取用户选择的图片URI数组
            uris = photoSelectResult.photoUris;
            this.uri = uris[0];
            console.info('photoViewPicker.select to file succeed and uris are:' + uris);
          }).catch((err: BusinessError) => {
            console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

**场景二**：使用drawImage绘制图片时将图片绘制成圆形，实现如下：

1. 通过arc方法绘制一个圆形路径。
2. 通过clip方法设置裁剪区域。
3. 通过drawImage绘制图片，并使其位置和大小匹配圆的范围。

示例代码如下：

```ts
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
export struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true); // 画布设置（启用抗锯齿）
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings); // 2D渲染上下文
  @State uri: string = '';

  async drawImage() {
    try {
      const imageSource: image.ImageSource = image.createImageSource(this.uri);
      const pixelMap: image.PixelMap = await imageSource.createPixelMap();
      // 获取图片原始尺寸
      const imageInfo = await pixelMap.getImageInfo();
      const centerX = 100; // 圆形中心X坐标
      const centerY = 100; // 圆形中心Y坐标
      const radius = 100; // 圆形半径
      // 计算绘制参数以保证圆形完整
      const cropSize = radius * 2; // 裁剪区域的边长（正方形）
      // 计算缩放比例，确保图片完全覆盖裁剪区域
      const scaleRatio = Math.max(
        cropSize / imageInfo.size.width, // 宽度方向的缩放比例
        cropSize / imageInfo.size.height // 高度方向的缩放比例
      );
      // 按比例缩放后的图片尺寸
      const scaledWidth = imageInfo.size.width * scaleRatio;
      const scaledHeight = imageInfo.size.height * scaleRatio;
      // 计算图片绘制的起始位置，使其中心与圆心重合
      const drawX = centerX - scaledWidth / 2;
      const drawY = centerY - scaledHeight / 2;
      // 执行裁剪与绘制
      this.context.save();
      this.context.beginPath();
      this.context.arc(centerX, centerY, radius, 0, Math.PI * 2); // 定义圆形裁剪区
      this.context.clip(); // 应用裁剪
      // 绘制缩放后的图片，其中心与圆形中心对齐
      this.context.drawImage(
        pixelMap,
        drawX,
        drawY,
        scaledWidth,
        scaledHeight
      );
      this.context.restore(); // 恢复画布状态
    } catch (err) {
      console.error('drawImage failed');
    }
  }

  async getFileInfo(filePathString: string) {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let resFile: fileIo.File | undefined;
    try {
      resFile = fileIo.openSync(filePathString, fileIo.OpenMode.READ_ONLY);
      // 创建临时文件目录
      let dateStr = (new Date().getTime()).toString();
      this.uri = context.cacheDir + `/${dateStr + resFile.name}`; // 生成沙箱缓存路径
      // 拷贝系统图库图片到沙箱
      fileIo.copyFileSync(resFile.fd, this.uri);
      this.drawImage(); // 触发绘制
    } catch (err) {
      console.error('Failed to copy file');
    } finally {
      if (resFile) {
        fileIo.closeSync(resFile);
      }
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Canvas(this.context)
        .width('200')
        .height('200')
        .margin({ top: 100, bottom: 30 });
      Button('加载图片')
        .onClick(() => {
          // 创建图片选择配置对象
          const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
          // 设置MIME类型过滤器：仅显示图片类型（排除视频等）
          photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
          // 设置最大选择数量为1（单选模式）
          photoSelectOptions.maxSelectNumber = 1;
          // 初始化URI存储数组（用于接收选择结果）
          let uris: Array<string> = [];
          // 创建相册选择器实例
          const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
          // 调用相册选择器并处理结果
          photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
            // 获取用户选择的图片URI数组
            uris = photoSelectResult.photoUris;
            this.getFileInfo(uris[0]);
            console.info('photoViewPicker.select to file succeed and uris are:' + uris);
          }).catch((err: BusinessError) => {
            console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
          });
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
