---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ringtone-preparations
title: 设置铃声
breadcrumb: 指南 > 媒体 > Ringtone Kit（铃声服务） > 设置铃声
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e58f3f8a74cbeace3f82fa11e91a597415c68a0cf8e44da8aab6e068df0c50e1
---

1. 导入ringtone模块和相关公共模块。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { ringtone } from '@kit.RingtoneKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileUri, picker } from '@kit.CoreFileKit';
   ```
2. 调用[ringtone.getSupportedRingtoneTypes](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupportedringtonetypes)接口，查询支持设置的铃声类型。

   ```typescript
   import { ringtone } from '@kit.RingtoneKit'
   import { JSON } from '@kit.ArkTS';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const APP_TAG = 'Msc_Demo'
   const DOMAIN = 0x0001

   @Entry
   @Component
   struct GetSupportedRingtoneTypes {
     build() {
       Stack() {
         Column() {
           Button('查询当前系统支持自定义的铃声类型')
             .width(200)
             .height(50)
             .onClick(() => {
               let typeList: ringtone.RingtoneType[] = ringtone.getSupportedRingtoneTypes()
               hilog.info(DOMAIN, APP_TAG, `getSupportedRingtoneTypes: ${JSON.stringify(typeList)}`);
             })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.Pink)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
3. 调用[ringtone.getSupportedDataTypes](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupporteddatatypes)接口，查询支持的数据类型。当前支持格式：MP3，OGG，FLAC，AAC，MP2，M4A，MP4。

   ```typescript
   import { ringtone } from '@kit.RingtoneKit'
   import { BusinessError } from '@kit.BasicServicesKit';
   import { uniformTypeDescriptor } from '@kit.ArkData';
   import { JSON } from '@kit.ArkTS';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const APP_TAG = 'Msc_Demo'
   const DOMAIN = 0x0001

   @Entry
   @Component
   struct GetSupportedDataTypes {
     build() {
       Stack() {
         Column() {
           Button('查询支持的文件类型')
             .width(200)
             .height(50)
             .onClick(() => {
               try {
                 let typeList: uniformTypeDescriptor.UniformDataType[] =
                   ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION)
                 hilog.info(DOMAIN, APP_TAG, `getSupportedDataType: ${JSON.stringify(typeList)}`);
               } catch (error) {
                 let err: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, APP_TAG,
                   `getSupportedDataType error message: ${err.message}, error code: ${err.code}`);
               }
             })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.Pink)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
4. 调用[ringtone.startRingtoneSetting](../harmonyos-references/ringtone-ringtone.md#ringtonestartringtonesetting)接口拉起设置弹窗，用户设置铃声后返回设置的铃声类型。

   通过promise异步方式：

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { ringtone } from '@kit.RingtoneKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileUri, picker } from '@kit.CoreFileKit';

   @Entry
   @Component
   struct Index {
     @State isShowUIExtensionCom: boolean = false;
     private prefixUri: string = '';
     private buttonText: string = '';
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     aboutToAppear(): void {
       const documentViewPicker = new picker.DocumentViewPicker(this.context);
       const documentSaveOptions = new picker.DocumentSaveOptions();
       documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
       documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
         let savePath = documentSaveResult[0];
         let fileUriObject = new fileUri.FileUri(savePath);
         this.prefixUri = fileUriObject.path
         console.info('documentViewPicker.save succeed and prefixUri is:' + this.prefixUri);
       }).catch((err: BusinessError) => {
         console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
       })
     }

     build() {
       Column() {
         Column() {
           Text($r('app.string.setting_ringtone'))
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .fontColor($r('sys.color.ohos_id_color_text_primary'))
             .alignSelf(ItemAlign.Start)
             .margin({
               top: 64,
               left: 12,
               bottom: 16
             })

           TextInput({ placeholder: $r('app.string.please_enter_the_file_name') })
             .width(312)
             .height(40)
             .onChange((value: string) => {
               this.buttonText = value;
             })
         }

         Button($r('app.string.setting_ringtone'))
           .width(312)
           .height(40)
           .margin({
             bottom: 16
           })
           .onClick(async () => {
             if (this.buttonText) {
               let audioPath: string = this.prefixUri + '/' + this.buttonText;
               console.info(`audioPath:${audioPath}`);
               try {
                 let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
                 console.info(`fileName:${fileName}`);
                 ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
                   console.info(`setFlag : ${res}`);
                 });
               } catch (error) {
                 let err: BusinessError = error as BusinessError;
                 if (err.code === ringtone.RingtoneErrors.ERROR_FILE_NOT_FOUND) {
                   this.getUIContext().getPromptAction().showToast({
                     message: $r('app.string.file_exist'),
                     duration: 2000
                   });
                 }
                 console.error(`accessSync failed with error. message: ${err.message}, code: ${err.code}`);
               }
             } else {
               this.getUIContext().getPromptAction().showToast({
                 message: $r('app.string.please_enter_the_file_name'),
                 duration: 2000
               });
             }
           })
       }
       .justifyContent(FlexAlign.SpaceBetween)
       .width('100%')
       .height('100%')
     }
   }
   ```

   通过callback异步方式：

   ```typescript
   // 详细代码参考API参考
   let prefixUri: string = '';
   let audioPath: string = prefixUri + '/' + this.buttonText;
   let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
   ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, data) => {
     hilog.info(DOMAIN, APP_TAG, `返回值：${JSON.stringify(data)}`)
   });
   ```
5. 调用[ringtone.getSupportedMaxDuration](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupportedmaxduration)接口，获取当前铃声支持的最大时长。

   ```typescript
   import { ringtone } from '@kit.RingtoneKit'
   import { BusinessError } from '@kit.BasicServicesKit';
   import { uniformTypeDescriptor } from '@kit.ArkData';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const APP_TAG = 'Msc_Demo'
   const DOMAIN = 0x0001

   @Entry
   @Component
   struct GetSupportedMaxDuration {
     build() {
       Stack() {
         Column() {
           Button('查询最大时长')
             .width(200)
             .height(50)
             .onClick(() => {
               try {
                 let maxDuration: number =
                   ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE,
                     uniformTypeDescriptor.UniformDataType.MP3)
                 hilog.info(DOMAIN, APP_TAG, `getSupportedMaxDuration: ${maxDuration}`);
               } catch (error) {
                 let err: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, APP_TAG,
                   `getSupportedMaxDuration error message: ${err.message}, error code: ${err.code}`);
               }
             })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.Pink)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
6. 调用[ringtone.getSupportedMaxSize](../harmonyos-references/ringtone-ringtone.md#ringtonegetsupportedmaxsize)接口，获取当前铃声支持的文件大小。

   ```typescript
   import { ringtone } from '@kit.RingtoneKit'
   import { BusinessError } from '@kit.BasicServicesKit';
   import { uniformTypeDescriptor } from '@kit.ArkData';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const APP_TAG = 'Msc_Demo'
   const DOMAIN = 0x0001

   @Entry
   @Component
   struct GetSupportedMaxSize {
     build() {
       Stack() {
         Column() {
           Button('查询文件大小限制')
             .width(200)
             .height(50)
             .onClick(() => {
               try {
                 let maxSize: number =
                   ringtone.getSupportedMaxSize(ringtone.RingtoneType.CALL,
                     uniformTypeDescriptor.UniformDataType.MP3)
                 hilog.info(DOMAIN, APP_TAG, `getSupportedMaxSize: ${maxSize}`);
               } catch (error) {
                 let err: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, APP_TAG,
                   `getSupportedMaxSize error message: ${err.message}, error code: ${err.code}`);
               }
             })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.Pink)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
