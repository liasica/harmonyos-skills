---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-4
title: 如何为PDF添加指定的字符串生成新的PDF文件
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 如何为PDF添加指定的字符串生成新的PDF文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f61b0a5372d68117bd3bb91f92b5464e9d659bf393b48893a4d09d86c1e8bb23
---

## 问题现象

一个字符串，如何添加到PDF文件内，生成一个新的PDF文件？

## 背景知识

* [PDF页面文本、图片和批注](../harmonyos-guides/pdf-add-txt-img-annot.md)：支持编辑PDF页面内容，包括：添加、删除文本；添加、删除图片；添加、修改、删除批注。
* [addTextObject](../harmonyos-references/pdf-arkts-pdfservice.md#addtextobject)：添加文本内容，只可按行添加。

## 解决方案

PDF Kit（PDF服务）提供的[PDF页面文本、图片和批注](../harmonyos-guides/pdf-add-txt-img-annot.md)能力支持编辑PDF页面内容，包括添加、删除文本，可调用[addTextObject](../harmonyos-references/pdf-arkts-pdfservice.md#addtextobject)接口添加字符串。

可以参考以下示例代码：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { pdfService } from '@kit.PDFKit';
import fs from '@ohos.file.fs';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let text = `测试字符`;

@Entry
@Component
struct SFAQ20250507142609641237 {
  @State imageUri: string = '';

  build() {

    Column() {
      Button('选择图片')
        .onClick(() => {
          this.selectImage();
        });
      Image(this.imageUri)
        .width('100%')
        .layoutWeight(1);

      Button('image转PDF')
        .onClick(() => {
          this.savePdf();
        });
    };
  }

  async savePdf() {
    console.info('testTag', 'enter savePath');
    let pdfDocument = new pdfService.PdfDocument();
    let isCreate = pdfDocument.createDocument(600, 900);
    if (isCreate) {
      console.info('testTag', `enter savePath getPageCount = ${pdfDocument.getPageCount()}`);
      let imagePdfPage = pdfDocument.getPage(0);
      let dir = this.getUIContext().getHostContext()?.filesDir;
      let imgPath = dir + '/test.jpg';
      console.info('testTag', `pdf imgPath = ${imgPath}`);
      imagePdfPage.addImageObject(imgPath, 20, 20, 500, 500);

      let textPdfPage = pdfDocument.insertBlankPage(1, 600, 900);
      let textStyle: pdfService.TextStyle = new pdfService.TextStyle;
      let fontInfo = new pdfService.FontInfo();
      fontInfo.fontPath = '/system/fonts/HarmonyOS_Sans.ttf';
      textStyle.fontInfo = fontInfo;
      textStyle.textSize = 32;
      textStyle.textColor = 0x0000ea;
      textStyle.isBold = true;
      textStyle.isItalic = false;
      textPdfPage.addTextObject(text, 20, 120, textStyle); // 添加示例文字

      let randomNumber = '';
      const rand = cryptoFramework.createRandom();
      const randData = rand.generateRandomSync(6);
      randData.data.forEach((val) => {
        randomNumber = randomNumber + val;
      });
      let savePath = this.getUIContext().getHostContext()?.filesDir + `/output${randomNumber}.pdf`; // 可用IDE在沙箱目录下找到
      console.info('testTag', `pdf savePath = ${savePath}`);

      let result = pdfDocument.saveDocument(savePath);
      console.info('testTag', `pdf 保存结果：${result}`);
    }
  }

  selectImage() {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions).then((photo: photoAccessHelper.PhotoSelectResult) => {
      let images = photo.photoUris;
      if (images.length > 0) {
        this.imageUri = images[0];
        let file = fs.openSync(images[0], fs.OpenMode.READ_ONLY);
        fs.copyFileSync(file.fd, this.getUIContext().getHostContext()?.filesDir + '/test.jpg');
        fs.closeSync(file);
      }
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  }
}
```

## 常见FAQ

Q：PDF预览模式使用下划线批注，如果内容过短时下划线会变成竖线。

A：这是正常现象，由于下划线跟着文字方向变化，文字内容过短是竖向排列，文字内容过长是横向排列，所以批注内容过短时下划线会变成竖线。

Q：使用PDF Kit添加文本时，如何指定字体和字号？

A：调用[addTextObject](../harmonyos-references/pdf-arkts-pdfservice.md#addtextobject)接口添加文本时，通过入参TextStyle设置文本样式，其中fontInfo用于指定字体信息，textSize用于设置字号（单位Points，默认20）。字体路径可通过以下两种方式获取：一是使用系统内置字体，通过[getFontByName](../harmonyos-references/arkts-apis-uicontext-font.md#getfontbyname)("HarmonyOS Sans").path获取路径，系统内置字体包括HarmonyOS Sans、HarmonyOS Sans Condensed等；二是使用自定义字体，将.ttf字体文件打包到应用沙箱目录，然后将其路径赋值给[fontInfo](../harmonyos-references/pdf-arkts-pdfservice.md#fontinfo).fontPath。
