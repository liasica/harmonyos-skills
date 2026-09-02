---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-17
title: 如何通过AddFormMenuItem组件将沙箱图片刷新至卡片
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何通过AddFormMenuItem组件将沙箱图片刷新至卡片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ff9a868968b8ebd5639854c0687e0e639cb21daf6364e32af64265aaf26524e5
---

## 问题现象

在主应用中使用FormMenu组件，实现卡片添加至桌面操作。如何在添加卡片时，将沙箱图片刷新至卡片进行展示？

## 背景知识

* [FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)组件封装了一个“添加至桌面”菜单，用于实现应用内长按组件生成“添加至桌面”菜单，点击该菜单，触发卡片添加至桌面操作。通过桌面访问该应用快捷卡片，可以直接访问该组件功能。在应用使用过程中，该组件作为留存和复访入口，可吸引用户将功能快捷添加到桌面。
* 在卡片上通常需要展示本地图片或从网络上下载的图片，获取本地图片和网络图片需要通过FormExtensionAbility来实现，[示例代码](../harmonyos-guides/arkts-ui-widget-image-update.md)介绍了如何在卡片上显示本地图片和网络图片。

## 解决方案

1. 在主应用中将resource目录中图片保存至沙箱，并根据沙箱中图片路径读取，获取文件的fd。构造传递给卡片的数据，需注意传递对象的key要与卡片页面一致。

   ```ts
   //Index.ets
   import { common } from '@kit.AbilityKit';
   import { fileIo, fileUri } from '@kit.CoreFileKit';
   import { AddFormMenuItem } from '@kit.ArkUI';
   import { formBindingData } from '@kit.FormKit';
   import { JSON } from '@kit.ArkTS';

   @ObservedV2
   export class CardModel {
     // 需注意，采用状态变量监控后，实际属性key会发生变化
     @Trace cardID: string = '';
     @Trace cardTitle: string = '';
     imageBackgroundPath_Square: string = '';
     // 卡片需要显示图片场景, 必须和下列字段formImages 中的key fileName 相同。
     imgName: string = 'fileName';
     // 卡片需要显示图片场景, 必填字段(formImages 不可缺省或改名), fileName 对应 fd
     formImages: Record<string, number> = {};
   }

   @Entry
   @ComponentV2
   struct Index {
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     @Local newCard: CardModel = new CardModel();
     @Local imageLoaded: boolean = false;

     async saveResourceToSandbox() {
       try {
         const sandboxPath = this.context.filesDir + '/test.png';
         const resourceManager = this.context.resourceManager;
         // 加载media目录下的test图片
         const fileContent = resourceManager.getMediaContentSync($r('app.media.test').id);

         let file = fileIo.openSync(sandboxPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         fileIo.writeSync(file.fd, fileContent.buffer);
         fileIo.closeSync(file);
         console.info('文件已存入沙箱路径：', sandboxPath);
         this.newCard.imageBackgroundPath_Square = sandboxPath;
         this.imageLoaded = true;
         console.info('图片已保存到沙箱路径：', this.newCard.imageBackgroundPath_Square);
       } catch (err) {
         console.error('保存失败，错误码：', (err as Error).message);
       }
     }

     async getImageFd(imagePath: string): Promise<number> {
       try {
         let file = fileIo.openSync(imagePath, fileIo.OpenMode.READ_ONLY);
         return file.fd;
       } catch (err) {
         console.error(`打开文件失败: ${err.message}`);
         return -1;
       }
     }

     async aboutToAppear() {
       // 保存图片
       await this.saveResourceToSandbox();
       this.newCard.cardID = '1';
       this.newCard.cardTitle = '测试';

       // 图片
       let fileName = 'file' + Date.now();
       let imgMap: Record<string, number> = {};
       this.newCard.imgName = fileName;
       this.newCard.formImages = imgMap;
       // 获取图片fd
       imgMap[fileName] = await this.getImageFd(this.newCard.imageBackgroundPath_Square);
       console.info('构造卡片初始化数据', JSON.stringify(this.newCard));
     }

     @Builder
     MyMenu() {
       Menu() {
         AddFormMenuItem(
           {
             // 应用包名 需要更换自己的
             bundleName: 'com.zwl.myapplication',
             abilityName: 'EntryFormAbility',
             parameters: {
               'ohos.extra.param.key.form_dimension': 2,
               'ohos.extra.param.key.form_name': 'widget',
               'ohos.extra.param.key.module_name': 'entry',
             },
           },
           this.newCard.cardID,
           {
             formBindingData: formBindingData.createFormBindingData(this.newCard),
             callback: (error, formId) => {
               console.info('AddCardMenu', `callback info：error = ${JSON.stringify(error)}, formId = ${formId}`);
               // 更新桌面卡片后 关闭文件
               fileIo.closeSync(this.newCard.formImages[this.newCard.imgName]);
               if (error?.code === 0) {
                 console.info('AddCardMenu', "添加至桌面成功");
               } else {
                 console.info('AddCardMenu', "添加至桌面失败，请尝试其它添加方式");
               }
             },
           }
         );
       };
     }

     build() {
       Row() {
         Column() {
           if (this.imageLoaded) {
             Image(fileUri.getUriFromPath(this.newCard.imageBackgroundPath_Square))   // 自定义图片
               .id(this.newCard.cardID)
               .width(200)
               .height(200)
               .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
                 placement: Placement.TopLeft
               });
           }
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
2. 在卡片接收来自主应用传递的数据，并渲染展示。

   ```ts
   let local = new LocalStorage();
   @Entry(local)
   @Component
   export struct WidgetCard {
     @LocalStorageProp('imgName') imgName: string = '';
     @LocalStorageProp('imageBackgroundPath_Square') imageBackgroundPath_Square: string = '';

     build() {
       Stack() {
         Image(`memory://${this.imgName}`)
           .width('100%')
           .aspectRatio(1)
           .borderRadius(20);
         Text(this.imageBackgroundPath_Square);
       }
       .width(175)
       .aspectRatio(1);
     }
   }
   ```
