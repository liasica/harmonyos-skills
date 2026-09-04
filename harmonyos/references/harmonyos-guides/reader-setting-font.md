---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-font
title: 自定义字体
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 修改阅读设置 > 自定义字体
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6237f4ed710270baf5055e6755e6e4c4e10d866296a548cb2da8932092d81368
---

当应用需要支持自定义字体时，开发者可通过[ReaderSetting](../harmonyos-references/reader-read-core.md#readersetting)的fontPath属性，实现对阅读内容字体的实时修改。

自定义字体文件支持两种存放路径：

* 工程目录resources/rawfile文件夹。
* [应用沙箱目录](app-sandbox-directory.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/DjYeSfUXTkuDT3FtLd66CQ/zh-cn_image_0000002742124321.png)

## 接口说明

自定义字体主要涉及3个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [setPageConfig](../harmonyos-references/reader-read-core.md#setpageconfig)(pageConfig: ReaderSetting): void | 设置或者修改页面排版属性。 |
| [on('resourceRequest')](../harmonyos-references/reader-read-core.md#onresourcerequest) | 注册资源请求回调，如果设置了自定义背景，字体时，排版引擎会通过此接口获取对应的资源ArrayBuffer。 |
| [off('resourceRequest')](../harmonyos-references/reader-read-core.md#offresourcerequest) | 注销资源请求回调接口，可在页面销毁时调用。 |

## 开发准备

* 进行自定义字体之前，请先确保已经“[构建阅读器](reader-read-page.md)”。
* 已经准备好字体资源，并放在对应的目录当中。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 定义字体文件存放路径：

   * 若资源放在项目resources/rawfile/fonts文件夹下。

     ```typescript
     let filePath: string = 'fonts/SourceHanSerifCN-VF.ttf';
     ```
   * 若资源放在[应用沙箱目录](app-sandbox-directory.md)下。

     ```typescript
     let filePath: string = this.getUIContext().getHostContext()!.filesDir + '/fonts/SourceHanSerifCN-VF.ttf'
     ```
3. 通过ReaderSetting的fontName和fontPath属性设置自定义字体的名称及所在的路径，并调用ReaderComponentController组件控制器的setPageConfig接口，重新渲染界面。

   ```typescript
   this.readerSetting.fontName = '思源宋体';
   // 路径为上述两种之一
   this.readerSetting.fontPath = filePath;
   this.readerComponentController.setPageConfig(this.readerSetting);
   ```
4. 注册排版引擎资源请求接口，并返回相应资源。

   当排版引擎检测到是自定义字体场景时，会通过接口请求字体资源。开发者需要根据返回的文件路径，判断是否为请求字体资源。如果是，则根据字体资源所在的路径，返回对应的ArrayBuffer。

   ```typescript
   aboutToAppear(): void {
     // 注册资源请求回调
     this.readerComponentController.on('resourceRequest', this.resourceRequest);
   }

   aboutToDisappear(): void {
     // 注销资源请求回调
     this.readerComponentController.off('resourceRequest');
   }

   private isFont(filePath: string): boolean {
     let options = ['.ttf', '.woff2', '.otf'];
     let path = filePath.toLowerCase();
     let result = path.indexOf(options[0]) != -1 || path.indexOf(options[1]) != -1 || path.indexOf(options[2]) != -1;
     hilog.info(0x0000, 'testTag',  'isFont = ' + result);
     return result;
   }

   /**
    * 资源请求回调
    */
   private resourceRequest: bookParser.CallbackRes<string, ArrayBuffer> = (filePath: string): ArrayBuffer => {
     hilog.info(0x0000, 'testTag', 'resourceRequest : filePath = ' + filePath);
     if (filePath.length === 0) {
       return new ArrayBuffer(0);
     }
     if (!this.isFont(filePath)) {
       return new ArrayBuffer(0);
     }
     try {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       // 获取资源路径resources/rawfile/fonts下的字体文件Uint8Array数据
       let value: Uint8Array = context.resourceManager.getRawFileContentSync(this.readerSetting.fontPath);
       hilog.info(0x0000, 'testTag', 'resourceRequest : get other resource succeeded ');
       return value.buffer as ArrayBuffer;
     } catch (error) {
       let code = (error as BusinessError).code;
       let message = (error as BusinessError).message;
       hilog.error(0x0000, 'testTag',
         `resourceRequest : get other resource failed, error code: ${code}, message: ${message}.`);
     }
     // 如果在资源路径resources/rawfile/fonts下获取字体文件数据失败，则去沙箱目录下获取字体文件数据
     return this.loadFileFromPath(this.readerSetting.fontPath);
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
