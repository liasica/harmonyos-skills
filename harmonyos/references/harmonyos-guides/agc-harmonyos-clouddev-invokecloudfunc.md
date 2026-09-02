---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudfunc
title: 在端侧调用云函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发端侧工程 > 在端侧调用云侧代码 > 在端侧调用云函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a5c5c854c810007e343692a2231655412488e255ceb8b3e9a5232395251d1661
---

## 前提条件

请确保[云函数已正确开发并部署](agc-harmonyos-clouddev-deployfunc.md)。

## 操作步骤

1. 在代码文件中引入Cloud Foundation Kit。

   ```screen
   import { cloudFunction } from '@kit.CloudFoundationKit'
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用您云侧部署的云函数。关于云函数接口的更详细信息，请参考[Cloud Foundation Kit API参考-云函数模块](../harmonyos-references/cloudfoundation-cloudfunction.md)。

   ```screen
   //填入需要调用的云函数名称
   cloudFunction.call({name: 'xxxx'})
   .then((res: cloudFunction.FunctionResult) => {  
     // 处理调用返回
   }).catch((err: BusinessError) => {
     // 调用云函数异常时的处理逻辑
   })
   ```

   例如，调用云侧函数“my-cloud-function”，以返回一个时间戳。

   ```screen
   import { cloudFunction } from '@kit.CloudFoundationKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   interface result {
     intervalTime: number
   }

   interface res {
     result: result
   }

   @Entry
   @Component
   struct CloudFunction {
     @State globalId: string = '';

     build() {
       Column() {
         Navigation()
           .title($r('app.string.cloud_function_title'))
           .height('50vp')
           .width('100%')
           .margin({ bottom: 10 })
           .titleMode(NavigationTitleMode.Mini)

         Text($r('app.string.cloud_function_description'))
           .width('90%')
           .textAlign(TextAlign.Center)
           .margin({ top: 20, bottom: 20 })
           .fontSize($r('app.float.body_font_size'))
         Button({ type: ButtonType.Normal }) {
           Text($r('app.string.cloud_function_button_text'))
             .fontColor($r('app.color.white'))
             .margin({ top: 5, bottom: 5 })
         }
         .width('90%')
         .borderRadius('8vp')
         .height('30vp')
         .margin({ top: 10 })
         .onClick(() => {
           this.callMyFunction()
         })

         Column() {
           Text(this.globalId).fontSize($r('app.float.body_font_size'))
         }
         .width('90%')
         .padding({ top: 20, bottom: 20 })
         .margin({ top: 20 })
         .backgroundColor($r('app.color.placeholder_background'))
       }.height('100%')
     }

     callMyFunction() {
       cloudFunction.call({ name: 'my-cloud-function' }).then((res: cloudFunction.FunctionResult) => {
         let callback  = res as res;
         console.info(`Succeeded in call the function, time:${callback.result.intervalTime} `);
       }).catch((err: BusinessError) => {
         console.error(`Failed to call the function, Code: ${err.code}, message: ${err.message}`);
       });
     }
   }
   ```
