---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-5
title: 如何解决自定义扫码只能扫描一次-无法持续扫码的问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 如何解决自定义扫码只能扫描一次-无法持续扫码的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d72fa4da52ab3f73d7a1afb6ffcd5d77b226ef2ae2cfdfde4552eed34598b3a2
---

## 问题现象

在自定义界面扫码功能中，第一次扫码成功后触发Callback回调拿到扫码结果后，继续扫码后无法再次触发Callback回调。

**问题代码如下：**

```ts
.onLoad(async () => {
  customScan.start()
    .then(async (result: Array<scanBarcode.ScanResult>) => {
       // 处理扫码结果
       this.showScanResult(result);
    });
 })
```

## 背景知识

* [customScan.start](../harmonyos-references/scan-customscan-api.md#start)：启动扫码相机流，使用Callback异步回调获取扫码结果、相机预览流（YUV-图像格式NV21基于4:2:0采样）。
* [customScan.rescan](../harmonyos-references/scan-customscan-api.md#rescan)：触发一次重新扫码。如果扫描结果不是预期结果，可以调用此接口触发下一次扫描。本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出内部错误的异常。仅对start接口的Callback异步回调有效，Promise异步回调接口无效。
* 自定义持续扫码时序图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/m87ben2DTFWX0ijWXQdTBA/zh-cn_image_0000002658911829.png "点击放大")

详情请参考：[自定义界面扫码](../harmonyos-guides/scan-customscan.md)。

## 问题定位

1. 从问题代码可以了解到使用的是自定义扫码功能，调用customScan.start()接口后通过Callback回调函数得到扫码结果，但是start接口只执行一次扫码，返回结果后扫码识别功能结束。
2. 在Callback回调函数得到扫码结果后只对结果进行了处理，没有再进行其他操作。当前通过start接口开启的扫码识别功能已经结束，导致后续再进行扫码也无法触发Callback回调。

## 分析结论

调用start接口通过Callback回调得到第一次扫码结果，后续没有调用rescan接口再次触发重新扫码。

## 修改建议

1. 使用自定义扫码功能时，需要在module.json5中配置[ohos.permission.CAMERA](../harmonyos-guides/permissions-for-all-user.md#ohospermissioncamera)权限，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 在start接口的异步回调中通过变量控制显示扫描结果和重新扫描按钮，点击重新扫描按钮即可调用rescan接口再次触发重新扫码功能。

   注意：本案例进入页面之后需要扫码才能出现重新扫码页面，重新扫码响应快速，因此点击重新扫码之前建议将摄像头远离码图。

   示例代码如下：

   ```ts
   import { scanCore, scanBarcode, customScan } from '@kit.ScanKit';
   import { display } from '@kit.ArkUI';
   import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';

   const TAG: string = '[Scan Sample]';

   @Entry
   @Component
   struct CustomScanPage {
     @State userGrant: boolean = false; // 是否已申请相机权限
     @State surfaceId: string = ''; // XComponent组件生成id
     @State scanResult: string = ''; // 扫码结果
     @State isShowResult: boolean = false; // 是否正在扫码
     @State cameraHeight: number = 640; // 设置预览流高度，默认单位：vp
     @State cameraWidth: number = 360; // 设置预览流宽度，默认单位：vp
     displayHeight: number = 0; // 屏幕高度，单位vp
     displayWidth: number = 0; // 屏幕宽度，单位vp
     private mXComponentController: XComponentController = new XComponentController();
     // 返回自定义扫描结果的回调
     private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
       async (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
         if (error) {
           hilog.error(0x0001, TAG,
             `Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
           return;
         }
         this.isShowResult = true;
         this.scanResult = JSON.stringify(result);
         hilog.info(0x0001, 'TAG',
           `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
       };

     async onPageShow() {
       // 自定义启动第一步：用户申请权限
       await this.requestCameraPermission();
       this.isShowResult = false;
       // 多码扫码识别时enableMultiMode设置为true，单码扫码识别时enableMultiMode设置为false
       let options: scanBarcode.ScanOptions = {
         scanTypes: [scanCore.ScanType.ALL],
         enableMultiMode: true,
         enableAlbum: true
       };
       // 自定义启动第二步：设置预览流布局尺寸
       this.setDisplay();
       try {
         // 自定义启动第三步：初始化接口
         customScan.init(options);
       } catch (error) {
         hilog.error(0x0001, TAG, `Failed to init customScan. Code: ${error.code}, message: ${error.message}`);
       }
     }

     async onPageHide() {
       // 页面消失或隐藏时停止并释放相机流
       this.userGrant = false;
       this.customScanStop();
       try {
         customScan.release().catch((error: BusinessError) => {
           hilog.error(0x0001, TAG,
             `Failed to release customScan by promise. Code: ${error.code}, message: ${error.message}`);
         });
       } catch (error) {
         hilog.error(0x0001, TAG, `Failed to release customScan. Code: ${error.code}, message: ${error.message}`);
       }
     }

     // 用户申请权限
     async reqPermissionsFromUser(): Promise<number[]> {
       hilog.info(0x0001, TAG, 'reqPermissionsFromUser start');
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let atManager = abilityAccessCtrl.createAtManager();
       try {
         const grantStatus: PermissionRequestResult =
           await atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);
         return grantStatus.authResults;
       } catch (error) {
         hilog.error(0x0001, TAG, `Failed to requestPermissionsFromUser. Code: ${error.code}, message: ${error.message}`);
         return [];
       }
     }

     // 用户申请相机权限
     async requestCameraPermission() {
       let grantStatus = await this.reqPermissionsFromUser();
       for (let i = 0; i < grantStatus.length; i++) {
         if (grantStatus[i] === 0) {
           hilog.info(0x0001, TAG, `Succeeded in getting permissions.`);
           this.userGrant = true;
           break;
         }
       }
     }

     // 竖屏时获取屏幕尺寸，设置预览流全屏示例
     async setDisplay() {
       try {
         // 默认竖屏
         let displayClass = display.getDefaultDisplaySync();
         this.displayHeight = this.getUIContext().px2vp(displayClass.height);
         this.displayWidth = this.getUIContext().px2vp(displayClass.width);
         let maxLen: number = Math.max(this.displayWidth, this.displayHeight);
         const RATIO: number = 16 / 9;
         this.cameraHeight = maxLen;
         this.cameraWidth = maxLen / RATIO;
       } catch (error) {
         hilog.error(0x0001, TAG, `Failed to getDefaultDisplaySync. Code: ${error.code}, message: ${error.message}`);
       }
     }

     async customScanStop() {
       try {
         customScan.stop().catch((error: BusinessError) => {
           hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${error.code}, message: ${error.message}`);
         });
       } catch (error) {
         hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${error.code}, message: ${error.message}`);
       }
     }

     build() {
       Stack() {
         Column() {
           Button('重新扫码')
             .margin({ top: 50 })
             .onClick(() => {
               try {
                 // 重新触发扫码
                 customScan.rescan();
                 this.isShowResult = false;
                 this.scanResult = '';
               } catch (error) {
                 hilog.error(0x0001, '[Scan Sample]',
                   `Failed to rescan customScan. Code: ${error.code}, message: ${error.message}`);
               }
             });
           Text(this.scanResult)
             .width(250)
             .margin({ top: 20 });
         }
         .width('100%')
         .height('100%')
         .visibility(this.isShowResult ? Visibility.Visible : Visibility.None);

         if (this.userGrant) {
           Column() {
             XComponent({
               id: 'componentId',
               type: XComponentType.SURFACE,
               controller: this.mXComponentController
             })
               .onLoad(async () => {
                 hilog.info(0x0001, TAG, `Succeeded in loading, onLoad is called.`);
                 // 获取XComponent组件的surfaceId
                 this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
                 let viewControl: customScan.ViewControl = {
                   width: this.cameraWidth,
                   height: this.cameraHeight,
                   surfaceId: this.surfaceId
                 };
                 try {
                   // 自定义启动第四步：请求扫码接口，通过Promise方式回调
                   customScan.start(viewControl, this.callback);
                 } catch (error) {
                   hilog.error(0x0001, TAG, `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
                 }
               })
               .width(this.cameraWidth)
               .height(this.cameraHeight)
               .position({ x: 0, y: 0 });
           }
           .height('100%')
           .width('100%')
           .visibility(this.isShowResult ? Visibility.None : Visibility.Visible);
         }
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 总结

在自定义扫码功能中如需不重启相机并重新触发一次扫码，可以在适当时机调用rescan接口。
