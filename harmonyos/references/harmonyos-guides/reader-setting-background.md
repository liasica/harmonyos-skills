---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-background
title: 自定义页面背景
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 修改阅读设置 > 自定义页面背景
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8046c2a82f2fd52a7903075a4bb99255ff76ddcf04a1945160117d34b6d616d4
---

当应用需要支持自定义背景时，开发者可通过[ReaderSetting](../harmonyos-references/reader-read-core.md#readersetting)的themeColor及themeBgImg属性，实现对阅读内容自定义背景色及背景图片的实时修改。

更改页面背景色，可能会涉及到字体颜色和深色模式的适配。比如：设置了白色背景，但是当前是深色模式，字体颜色也是白色，这样会导致内容看不清楚。

自定义页面背景图片支持两种存放路径：

* 工程目录resources/rawfile文件夹。
* [应用沙箱目录](app-sandbox-directory.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/KxqTEQYEQkytRIzDh4MkxA/zh-cn_image_0000002712245414.png)

## 接口说明

自定义页面背景主要涉及1个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [setPageConfig](../harmonyos-references/reader-read-core.md#setpageconfig)(pageConfig: ReaderSetting): void | 设置或者修改页面排版属性。 |

## 开发准备

* 进行自定义背景之前，请先确保已经“[构建阅读器](reader-read-page.md)”。
* 已经准备好自定义背景图片资源，并放在对应的目录当中。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 单独设置背景色。如果有设置背景图片的情况下，背景色通常用于仿真翻页时背面主题色的绘制。否则，背景色还会用于渲染阅读页的背景色。

   ```typescript
   this.readerSetting.themeColor = '#000000';
   this.readerSetting.themeBgImg = '';
   // 当设置背景色为浅色时，需要将深色模式关掉
   this.readerSetting.nightMode = false;
   // 当设置背景色为浅色时，字体颜色也需要适配
   this.readerSetting.fontColor = '#FFFFFF';
   ```
3. 设置背景图片。需要同时设置与背景图片相近的主题颜色，用于仿真翻页时背面主题色的绘制。

   ```typescript
   this.readerSetting.themeBgImg = 'dark_sky_first.jpg';
   this.readerSetting.themeColor = '#000000';
   // 当设置背景图为浅色时，需要将深色模式关掉
   this.readerSetting.nightMode = false;
   // 当设置背景图为浅色时，字体颜色也需要适配
   this.readerSetting.fontColor = '#FFFFFF';
   ```
4. 调用ReaderComponentController组件控制器的setPageConfig接口，重新渲染界面。

   ```typescript
   this.readerComponentController.setPageConfig(this.readerSetting);
   ```
5. 注册排版引擎资源请求接口，并返回相应的背景图资源。

   在排版引擎检测到是自定义背景图片场景时，会通过接口请求背景图片资源。开发者需要根据返回的文件路径，判断是否为请求背景图片资源。如果是，则根据背景图片资源所在的路径，返回对应的ArrayBuffer。

   ```typescript
   aboutToAppear(): void {
     // 注册资源请求回调
     this.readerComponentController.on('resourceRequest', this.resourceRequest);
   }

   aboutToDisappear(): void {
     // 注销资源请求回调
     this.readerComponentController.off('resourceRequest');
   }

   /**
    * 资源请求回调
    */
   private resourceRequest: bookParser.CallbackRes<string, ArrayBuffer> = (filePath: string): ArrayBuffer => {
     hilog.info(0x0000, 'testTag', 'resourceRequest : filePath = ' + filePath);
     if(filePath.length === 0){
       return new ArrayBuffer(0);
     }
     try {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       // 获取资源路径resources/rawfile下的背景图片文件Uint8Array数据
       let value: Uint8Array = context.resourceManager.getRawFileContentSync(filePath);
       hilog.info(0x0000, 'testTag', 'resourceRequest : get other resource succeeded ');
       return value.buffer as ArrayBuffer;
     } catch (error) {
       let code = (error as BusinessError).code;
       let message = (error as BusinessError).message;
       hilog.error(0x0000, 'testTag',
         `resourceRequest : get other resource failed, error code: ${code}, message: ${message}.`);
     }
     // 如果在资源路径源路径resources/rawfile下获取背景图片文件数据失败，则去沙箱目录下获取背景图片数据
     return this.loadFileFromPath(filePath);
   }

   private loadFileFromPath(filePath: string): ArrayBuffer {
     try {
       let stats = fs.statSync(filePath);
       let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
       let buffer = new ArrayBuffer(stats.size);
       fs.readSync(file.fd, buffer);
       fs.closeSync(file);
       return buffer;
     } catch (err) {
       let code = (error as BusinessError).code;
       let message = (error as BusinessError).message;
       hilog.error(0x0000, 'testTag',
         `loadFileFromPath : get file failed, error code: ${code}, message: ${message}.`);
       return new ArrayBuffer(0);
     }
   }
   ```
