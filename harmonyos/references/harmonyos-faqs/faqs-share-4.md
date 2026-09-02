---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-4
title: 如何解决分享pdf文件到微信问题
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 如何解决分享pdf文件到微信问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3219b311f322b431e25e288e7d68c560670bd3fea3c96f12b0debf9525d2a36e
---

## 问题现象

开发者需要将pdf文件分享到微信。

## 背景知识

[Share Kit](../harmonyos-guides/share-introduction.md)（分享服务）为应用提供文本、图片、视频等内容跨应用、跨端分享能力。

应用把需要分享的内容和预览样式配置给Share Kit，Share Kit将根据不同的场景进行使用：

* 针对应用间分享的场景，根据分享的数据类型、数量等信息构建分享面板，为用户提供内容预览、推荐分享联系人、关联应用及操作界面，便于用户快速选择分享应用或操作，将内容分发到目标应用。
* 针对跨端分享的场景，根据分享的数据类型、数量等信息构建预览界面，用于跨端分享。

  如果应用需要显示在分享面板，则需要构建数据处理能力并按照配置要求在应用配置文件中声明，社交类应用可以通过意图框架接口捐献联系人信息，可以让用户一步分享到应用内的指定用户。

## 解决方案

可以使用Share kit（分享服务）将pdf文件分享到微信，需要先在resource资源目录下resfile目录里放入pdf文件。

```ts
import { systemShare } from '@kit.ShareKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import fs from '@ohos.file.fs';
@Entry
@Component
struct SharePage {
  context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    let fileExtention = '.pdf';
    let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(fileExtention);
    uniformTypeDescriptor.getTypeDescriptor(typeId);
  }

  sharePDF(){
    // 获取文件沙箱路径
    let filePath = this.context.filesDir + '/test.pdf';
    // 将沙箱路径转换为uri
    let uri = fileUri.getUriFromPath(filePath);
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: 'com.adobe.pdf',
      uri: uri,
      title: '标题', // 不传title字段时,显示图片文件名
      description: '描述', // 不传description字段时,显示图片大小
    });
    // 进行分享面板显示
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    controller.show(this.context, {
      selectionMode: systemShare.SelectionMode.BATCH, // 选择模式默认为SINGLE,BATCH模式为批量分享
      previewMode: systemShare.SharePreviewMode.DETAIL,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
    });
  }

  copyPDF(){
    let file = fs.openSync(this.context.resourceDir+'/test.pdf', fs.OpenMode.READ_ONLY);
    let file2 = fs.openSync(this.context.filesDir+'/test.pdf', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    fs.copyFileSync(file.fd, file2.fd);
    fs.closeSync(file);
    fs.closeSync(file2);
  }

  build() {
    Column() {
      Button('点击分享pdf')
        .width(150).margin({ top: 20 })
        .onClick(()=>{
          this.copyPDF();
          this.sharePDF();
        })
    }.padding(20)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
