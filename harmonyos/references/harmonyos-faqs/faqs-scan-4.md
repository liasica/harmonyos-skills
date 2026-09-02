---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-4
title: 扫码界面如何监听无操作返回事件
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 扫码界面如何监听无操作返回事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:1856140d56c5ba971e6c79b6b77a360efb3d34bde5f4be52e4962e44828854f2
---

## 问题现象

当使用Scan Kit扫码服务时，扫描成功或失败都能触发callback回调函数。但如果用户手动侧滑返回，不会触发任何回调，扫码相关资源不知何时被销毁导致内存泄漏。

问题代码如下：

```ts
 try
   scanBarcode.startScanForResult(this.getUIContext().getHostContext(), options).then((result: scanBarcode.ScanResult) => {
      // 处理扫描结果
   }).catch((error: BusinessError) => {
      if (error.code === 1000500001) {
         // 处理扫码结果错误事件
       } 
   });
 } catch (error) {
 }
```

默认界面扫码效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/s46dKmq8SzSL-Hc54i0VWg/zh-cn_image_0000002628552516.png "点击放大")

## 背景知识

[Scan Kit](../harmonyos-guides/scan-kit-guide.md)：扫码主要分为默认界面扫码和自定义界面扫码。

[默认界面扫码](../harmonyos-guides/scan-scanbarcode.md)：提供系统级体验一致的扫码界面，Scan Kit对系统相机权限进行了预授权，调用接口时，无需开发者再次申请相机权限。

[自定义界面扫码](../harmonyos-guides/scan-customscan.md)：提供了相机流控制接口，可根据自身需求自定义扫码界面，适用于对扫码界面有定制化需求的应用开发。同时需要开发者自己请求相机的使用权限。

## 问题定位

从问题代码看出使用了默认扫码页面，但是只对callback回调返回的结果和扫码结果出现的错误进行了处理，该操作的前提是必须要进行扫码，对于没有进行扫码操作而返回到上一个界面的情况没有处理。

## 分析结论

默认界面扫码开启扫码，却没有进行任何扫码操作而直接返回上一页面时，可以从回调中判断是否是1000500002错误码，如果是该错误码则表示用户进行了无操作返回，此时销毁资源即可。

## 修改建议

1. 默认扫码页面直接用回调的错误码1000500002判断。

   使用[scanBarcode.startScanForResult](../harmonyos-references/scan-scanbarcode-api.md#startscanforresult)函数，并在回调函数error中判断错误码是否为1000500002，如果是则处理无操作返回事件。

   ```ts
   import { scanCore, scanBarcode } from '@kit.ScanKit';
   // 导入默认界面扫码需要的日志模块和错误码模块
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct DefaultScanCode {
     build() {
       Column() {
         Row() {
           Button('默认扫码界面')
             .fontSize(20)
             .fontColor($r('sys.color.comp_background_list_card'))
             .fontWeight(FontWeight.Normal)
             .align(Alignment.Center)
             .type(ButtonType.Capsule)
             .width('90%')
             .height(40)
             .margin({ top: 5, bottom: 5 })
             .onClick(() => {
               // 定义扫码参数options
               let options: scanBarcode.ScanOptions = {
                 scanTypes: [scanCore.ScanType.ALL],
                 enableMultiMode: true,
                 enableAlbum: true
               };
               try {
                 // 可调用getHostContext接口获取当前页面关联的Context
                 scanBarcode.startScanForResult(this.getUIContext().getHostContext(), options)
                   .then((result: scanBarcode.ScanResult) => {
                     // 解析码值结果跳转应用服务页
                     hilog.info(0x0001, '[Scan CPSample]',
                       `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}`);
                   })
                   .catch((error: BusinessError) => {
                     if (error.code === 1000500001) {
                       // 处理扫码结果错误事件
                       hilog.error(0x0001, '[Scan CPSample]',
                         `Failed to get ScanResult by promise with options. Code:${error.code}, message: ${error.message}`);
                     } else if (error.code === 1000500002) {
                       // 处理无操作返回事件
                       hilog.info(0x0001, '[Scan CPSample]',
                         `没有扫描结果但是页面将要返回上一级页面`);
                     }
                   });
               } catch (error) {
                 hilog.error(0x0001, '[Scan CPSample]',
                   `Failed to get ScanResult by promise with options. Code:${error.code}, message: ${error.message}`);
               }
             });
         }
         .height('100%');
       }
       .width('100%');
     }
   }
   ```

2. 自定义界面扫码没有1000500002错误码进行判断，但是手动侧滑返回会触发[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)/[onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)方法，可以在该方法内判断是否进行了扫码操作，如果没有操作，在该方法内进行无操作返回事件处理。

* 页面被@Entry组件修饰的场景：

  若页面用@Entry组件修饰，侧滑返回会触发onBackPress页面生命周期方法，可以在该方法中判断是否进行了扫码操作，如果没有操作在该方法内处理无操作返回事件。
* 使用Navigation导航框架管理页面的场景：

  当与Navigation绑定的页面栈中存在内容时，NavDestination组件中的onBackPressed回调生效。当手动侧滑返回时触发该回调，并在该回调中处理无操作返回事件。

## 总结

1. 默认扫码页面可以使用scanBarcode.startScanForResult接口的回调函数错误码直接判断。
2. 自定义扫码页面根据项目的不同架构，主要有@Entry修饰的生命周期和NavDestination承载的生命周期，可以根据实际使用的场景进行解决方案选择。
