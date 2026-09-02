---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-157
title: 如何处理自定义文件类型
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何处理自定义文件类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:11badf502960550dfd0a2c381e9aaf0867acc3a75c127746acf08bb24b309a1b
---

## 问题现象

如果应用根据自身业务定义了一些特殊格式的文件类型（非标准化数据类型），如何使应用能够处理这些特殊格式的文件呢？

## 背景知识

* [拉起文件处理类应用](../harmonyos-guides/file-processing-apps-startup.md#目标方接入步骤)：声明文件打开能力。
* [UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)：标准化数据类型（Uniform Type Descriptor，简称UTD）用于解决系统中的类型模糊问题，即针对同一种数据类型，存在不同的类型描述方式：MIME Type、文件扩展名等。列表当中展示当前HarmonyOS默认支持的文件类型，包括基础类型、系统关联类型、应用定义类型。
* [应用自定义数据类型](../harmonyos-guides/uniform-data-type-descriptors.md#应用自定义数据类型)：由于预置标准数据类型无法穷举所有数据类型，在业务跨应用、跨设备交互过程中，会涉及到一些应用独有的数据类型，因此支持应用声明自定义数据类型。

## 解决方案

首先从HarmonyOS官网UTD配置列表当中确认当前格式文件是否为HarmonyOS默认支持的文件类型，如果不是，则参看以下步骤自定义文件类型。实现方案如下：

1. 在当前应用entry\src\main\resources\rawfile\arkdata\utd\目录下新增utd.json5文件。其中的**TypeId属性由应用bundleName和具体类型名组成**，例如com.example.myapplication.kml，其中com.example.myapplication为应用bundleName。其余字段详情介绍可参考[约束限制](../harmonyos-guides/uniform-data-type-descriptors.md#约束限制)。代码示例参考如下：

   ```json
   {
     "UniformDataTypeDeclarations": [
       {
         "TypeId": "com.example.myapplication.suffix1",
         "BelongingToTypes": ["general.file"],
         "FilenameExtensions": [".suffix1"],
         "MIMETypes": ["application/suffix1"],
         "Description": "自定义类型文件suffix1",
         "ReferenceURL": ""
       },
       {
         "TypeId": "com.example.myapplication.suffix2",
         "BelongingToTypes": ["general.file"],
         "FilenameExtensions": [".suffix2"],
         "MIMETypes": ["application/suffix2"],
         "Description": "自定义类型文件suffix2",
         "ReferenceURL": ""
       }
     ]
   }
   ```

2. 修改应用的module.json5文件，声明相关文件的打开能力，代码示例参考如下：

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           // ...
           "skills": [
             // ...
             {
               "actions": [
                 "ohos.want.action.viewData"
               ],
               "uris": [
                 {
                   "scheme": "file",
                   "type": "com.example.myapplication.suffix1",
                   "linkFeature": "FileOpen"
                 },
                 {
                   "scheme": "file",
                   "type": "com.example.myapplication.suffix2",
                   "linkFeature": "FileOpen"
                 }
               ]
             }
           ]
         }
       ],
       // ...
     }
   }
   ```
3. 修改EntryAbility（UIAbility），在onNewWant生命周期回调当中，接收文件，处理逻辑，代码示例参考如下：

   ```ts
   import { UIAbility, Want } from '@kit.AbilityKit';
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { buffer } from '@kit.ArkTS';

   export default class EntryAbility extends UIAbility {
     // ...
     onNewWant(want: Want): void {
       let uri = want.uri;
       if (!uri) {
         return;
       }
       try {
         // 根据待打开文件的URI进行相应操作。例如同步读写的方式打开URI获取file对象
         let file = fs.openSync(uri, fs.OpenMode.READ_WRITE);
         console.info(`Succeed to open file.${file.fd}`);
         let buf = new ArrayBuffer(4096);
         fs.readSync(file.fd, buf);
         // 案例以文本文件为例
         console.info(`文件内容：${buffer.from(buf)}`);
       } catch (err) {
         let error: BusinessError = err as BusinessError;
         console.error(`Failed to open file openSync, code: ${error.code}, message: ${error.message}`);
       }
     }
   }
   ```
