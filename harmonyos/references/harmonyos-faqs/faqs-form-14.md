---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-14
title: 如何在卡片上刷新展示多张图片
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何在卡片上刷新展示多张图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c1a6224e34b0574a58f0ff482c92c3a6ba01ea5af91231770d795be46d223207
---

## 问题现象

卡片加载时，有多张图片需要显示在卡片页面里，如何一次性添加到卡片页面上？

## 背景知识

* [formBindingData.createFormBindingData](../harmonyos-references/js-apis-app-form-formbindingdata.md#formbindingdatacreateformbindingdata)：创建一个FormBindingData对象。参数中图片数据以'formImages'作为标识，内容为图片标识与图片文件描述符的键值对{'formImages': {'key1': fd1, 'key2': fd2}}。
* [fs.listFileSync](../harmonyos-references/js-apis-file-fs.md#fileiolistfilesync)：默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

## 解决方案

以将沙箱filesDir目录下图片添加到卡片页面为例：

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/g-IQEp7XTIyGRs-L2zL8mA/zh-cn_image_0000002658870925.png "点击放大")

## 常见FAQ

Q：服务卡片中是否可以加载GIF图？

A：服务卡片可使用Image组件直接加载GIF图。为避免卡片频繁渲染刷新带来的功耗问题，GIF图只能播放一次，因此[不建议通过服务卡片实现高频的动态变换界面效果](../atomic-guides/atomic-widget-development.md)。对于前期突破该规则的应用，近期将进行整改。

## 总结

formBindingData.createFormBindingData(formData)构造传递给卡片页面的数据时通过formImages字段会将图片fd保存在内存中，卡片页面接收formImages里的key值即可通过key找到图片展示在图片组件。多图片场景时需要保证每张图片的key都是唯一的。
