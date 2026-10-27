---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/form-kit-faq-0001
title: 元服务卡片多张图片刷新展示常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 常见问题 > 元服务卡片多张图片刷新展示常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:50+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:ba90c122fd90fa0041863efcdbc02d0c2a0db2e6a7eadc5a22dff1b3b6476c26
---

**Q：卡片加载时，有多张图片需要显示在卡片页面里，如何一次性添加到卡片页面上？**

**A**：以将沙箱filesDir目录下图片添加到卡片页面为例：

1. 在卡片生命周期[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)中获取沙箱filesDir目录下的图片，构造传递给卡片页面的数据。

   ```ts
   import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';
   import { fileIo as fs, ListFileOptions } from '@kit.CoreFileKit';

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       let formId = "";
       let parameters = want.parameters;
       if (parameters) {
         formId = parameters["ohos.extra.param.key.form_identity"] as string;
         console.info("onAddForm formId ", formId);
       }
       // 遍历出沙箱路径下的图片（保证对应沙箱路径下有相应格式图片）
       let dir: string = this.context.filesDir;
       let listFileOption: ListFileOptions = {
         recursion: false,
         listNum: 0,
         filter: {
           suffix: [".png", ".jpg", ".jpeg"]
         }
       };
       let filenames = fs.listFileSync(dir, listFileOption);
       console.info("filenames: ", JSON.stringify(filenames));
       let imgMap: Record<string, number> = {};
       for (let i = 0; i < filenames.length; i++) {
         // 打开本地图片并获取其打开后的fd
         let file = fs.openSync(dir + '/' + filenames[i]);
         imgMap[filenames[i]] = file.fd;
       }

       class FormDataClass {
         formId: string = formId;
         // 卡片需要显示图片场景, 必须和formImages中的key对应
         imgNames: string[] = filenames;
         // 卡片需要显示图片场景, 必填字段(formImages不可缺省或改名)
         formImages: Record<string, number> = imgMap;
       }

       let formData = new FormDataClass();
       return formBindingData.createFormBindingData(formData);
     }
   }
   ```
2. 卡片页面接收数据并展示图片。

   ```ts
   let storageWidgetImageUpdate = new LocalStorage();

   @Entry(storageWidgetImageUpdate)
   @Component
   export struct WidgetCard {
     @LocalStorageProp('formId') formId: string = "";
     @LocalStorageProp('imgNames') imgNames: string[] = [];

     build() {
       List({ space: 10 }) {
         ForEach(this.imgNames, (item: string) => {
           ListItem() {
             Row() {
               Text(item + ": ")
                 .layoutWeight(1)
                 .height(20)
                 .fontSize(12)
                 .textAlign(TextAlign.Start)
               Image('memory://' + item)
                 .height(20)
                 .width(20)
                 .objectFit(ImageFit.Contain)
             }
             .justifyContent(FlexAlign.Start)
           }
           .id(item)
           .width('100%')
         })
       }
       .listDirection(Axis.Vertical)
       .width('100%')
       .height('100%')
       .padding(10)
     }
   }
   ```

   效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/KXIZEsFtTx-NbCusgpAX8g/zh-cn_image_0000002766078502.png "点击放大")

**Q：服务卡片中是否可以加载GIF图？**

**A**：服务卡片可使用Image组件直接加载GIF图。为避免卡片频繁渲染刷新带来的功耗问题，GIF图只能播放一次，因此[不建议通过服务卡片实现高频的动态变换界面效果](../doccenter-atomic-service/atomic-widget-development.md)。
