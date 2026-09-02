---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-74
title: 如何读写常见办公类文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何读写常见办公类文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:a5448be68a3a65ebd27385614b615ef29055dcc73365aa8533de6edcbc0dda4f
---

## 问题现象

如何新建或修改一些常见的办公文件？比如：Excel、Word、PDF。

## 背景知识

* [fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)：打开或者创建文件。
* [fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)：将数据写入文件。
* [fs.closeSync](../harmonyos-references/js-apis-file-fs.md#fileioclosesync)：关闭文件或目录，释放不再需要操作的文件资源。
* [save](../harmonyos-references/js-apis-file-picker.md#save)：通过保存模式拉起documentPicker界面，用户可以保存一个或多个文件。
* [PDF Kit](../harmonyos-guides/pdf-introduction.md)：包含[pdfService](../harmonyos-guides/pdf-pdfservice-implements.md)和[PdfView预览组件](../harmonyos-guides/pdf-pdfview-implements.md)。pdfService提供了加载和保存PDF文档、在PDF页面中添加文本内容、图片、批注、页眉页脚、水印、背景图片、书签、判断PDF文档是否加密及删除文档加密等相关的功能，对PDF文档的操作有更多的应用场景。PdfView组件提供了文档预览功能，如：PDF文档预览、高亮显示、搜索关键字，批注等场景。

## 解决方案

|  | 创建文件接口 | 写入接口 | 可写入的数据格式 |
| --- | --- | --- | --- |
| Excel | [fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync) | [fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync) | CSV格式的字符串。比如：  名称\t价格\t数量\n"电脑"\t5000\t5\n"手机"\t3000\t3 |
| Word | [fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync) | [fs.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync) | 字符串。比如："我是Word文档的内容。" |
| PDF | [createDocument](../harmonyos-references/pdf-arkts-pdfservice.md#createdocument) | [addTextObject](../harmonyos-references/pdf-arkts-pdfservice.md#addtextobject) | 字符串。比如："我是PDF文档内容。" |

* 创建Excel文件，并写入内容。
  1. 构造Excel表格对应的CSV文件数据。

     ```ts
     convertToCSV(data: Product[]): string {
       let headers = ['名称', '价格', '数量'];
       let fields = ['name', 'price', 'quantity'];
       let csvContent = headers.join('\t') + '\n';
       data.forEach((product) => {
         let rowData = fields.map(field => {
           let value: string = Object(product)[field].toString() || ''; // 获取字段值
           // 移除换行符
           value = value.toString().replace(/[\n\r]/g, ' ');
           // 如果值中包含逗号、引号，则用双引号包裹，并且转义双引号
           if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
             let temp = value.replace(/"/g, '""');
             value = `"${temp}"`;
           }
           return value;
         });
         csvContent += rowData.join('\t') + '\n';
       });
       return csvContent;
     }
     ```
  2. 使用DocumentViewPicker获取保存文件的路径，然后使用fs.write将数据写入Excel文件。

     ```ts
     Button('创建一个Excel文件')
       .margin({ bottom: 20 })
       .onClick(() => {
         // 定义文件路径，这里假设要保存到应用的内部存储某个目录下，可根据实际需求调整。
         try {
           let uris: Array<string> = [];
           // 创建文件管理器选项实例
           const documentSaveOptions = new picker.DocumentSaveOptions();
           documentSaveOptions.newFileNames = ['Excel.xlsx'];
           documentSaveOptions.fileSuffixChoices = ['文档|.xlsx', '.xlsx'];
           const documentViewPicker = new picker.DocumentViewPicker(this.context);
           // 用户选择目标文件夹，用户选择与文件类型相对应的文件夹，即可完成文件保存操作。保存成功后，返回保存文档的URI。
           documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
             uris = documentSaveResult;
             let file = fs.openSync(uris[0], fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
             // 构建CSV数据
             let csvData = this.convertToCSV(products);
             fs.write(file.fd, csvData).then((writeLen: number) => {
               console.info('write data to file succeed and size is:', writeLen);
             }).catch((err: BusinessError) => {
               console.error('write data to file failed with error message: ', err.message, ', error code: ',
                 err.code);
             }).finally(() => {
               fs.closeSync(file);
             });
             console.info('documentViewPicker.save to file succeed and uris are:', uris);
           }).catch((err: BusinessError) => {
             console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
           });
         } catch (e) {
           console.error('documentViewPicker.save error: ', JSON.stringify(e));
         }
       });
     ```
* 创建Word文件，并写入内容。

  ```ts
  Button('创建一个Word文件，并写入内容')
    .margin({ bottom: 20 })
    .onClick(() => {
      try {
        const documentSaveOptions = new picker.DocumentSaveOptions();
        documentSaveOptions.newFileNames = ['Word.docx'];
        documentSaveOptions.fileSuffixChoices = ['文档|.docx', '.docx'];
        const documentViewPicker = new picker.DocumentViewPicker(this.context);
        // 用户选择目标文件夹，用户选择与文件类型相对应的文件夹，即可完成文件保存操作。保存成功后，返回保存文档的URI。
        documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
          const uris = documentSaveResult;
          // 创建文件并写入字符串
          const file = fs.openSync(uris[0], fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
          const content = '这是要写入DOC文件的文本内容';
          fs.writeSync(file.fd, content);
          fs.closeSync(file.fd);
          console.info('文件写入成功');
        });
      } catch (error) {
        console.error('文件操作失败:', error);
      }
    });
  ```
* 创建PDF文件，并写入内容。

  使用[PDF Kit](../harmonyos-guides/pdf-introduction.md)新建PDF文件，并支持在PDF页面中添加文本内容、图片、批注、页眉页脚、水印、背景图片、书签、判断PDF文档是否加密及删除文档加密等相关的功能。在PDF文件中写入文本、图片示例代码：[添加文本和图片](../harmonyos-guides/pdf-add-txt-img-annot.md#添加文本和图片)。

完整示例参考如下：

```ts
import fs from '@ohos.file.fs';
import { picker } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

interface Product {
  name: string;
  price: number;
  quantity: number;
}

let products: Product[] = [
  { name: 'Prod,uct1', price: 10.0, quantity: 5 },
  { name: 'Pr"oduc"t2', price: 15.0, quantity: 3 }
];

@Entry
@Component
struct WorkDocumentPage {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  convertToCSV(data: Product[]): string {
    let headers = ['名称', '价格', '数量'];
    let fields = ['name', 'price', 'quantity'];
    let csvContent = headers.join('\t') + '\n';
    data.forEach((product) => {
      let rowData = fields.map(field => {
        let value: string = Object(product)[field].toString() || ''; // 获取字段值
        // 移除换行符
        value = value.toString().replace(/[\n\r]/g, ' ');
        // 如果值中包含逗号、引号，则用双引号包裹，并且转义双引号
        if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
          let temp = value.replace(/"/g, '""');
          value = `"${temp}"`;
        }
        return value;
      });
      csvContent += rowData.join('\t') + '\n';
    });
    return csvContent;
  }

  build() {
    Column() {
      Button('创建一个Excel文件')
        .margin({ bottom: 20 })
        .onClick(() => {
          // 定义文件路径，这里假设要保存到应用的内部存储某个目录下，可根据实际需求调整。
          try {
            let uris: Array<string> = [];
            // 创建文件管理器选项实例
            const documentSaveOptions = new picker.DocumentSaveOptions();
            documentSaveOptions.newFileNames = ['Excel.xlsx'];
            documentSaveOptions.fileSuffixChoices = ['文档|.xlsx', '.xlsx'];
            const documentViewPicker = new picker.DocumentViewPicker(this.context);
            // 用户选择目标文件夹，用户选择与文件类型相对应的文件夹，即可完成文件保存操作。保存成功后，返回保存文档的URI。
            documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
              uris = documentSaveResult;
              let file = fs.openSync(uris[0], fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
              // 构建CSV数据
              let csvData = this.convertToCSV(products);
              fs.write(file.fd, csvData).then((writeLen: number) => {
                console.info('write data to file succeed and size is:', writeLen);
              }).catch((err: BusinessError) => {
                console.error('write data to file failed with error message: ', err.message, ', error code: ',
                  err.code);
              }).finally(() => {
                fs.closeSync(file);
              });
              console.info('documentViewPicker.save to file succeed and uris are:', uris);
            }).catch((err: BusinessError) => {
              console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
            });
          } catch (e) {
            console.error('documentViewPicker.save error: ', JSON.stringify(e));
          }
        });

      Button('创建一个Word文件，并写入内容')
        .margin({ bottom: 20 })
        .onClick(() => {
          try {
            const documentSaveOptions = new picker.DocumentSaveOptions();
            documentSaveOptions.newFileNames = ['Word.docx'];
            documentSaveOptions.fileSuffixChoices = ['文档|.docx', '.docx'];
            const documentViewPicker = new picker.DocumentViewPicker(this.context);
            // 用户选择目标文件夹，用户选择与文件类型相对应的文件夹，即可完成文件保存操作。保存成功后，返回保存文档的URI。
            documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
              const uris = documentSaveResult;
              // 创建文件并写入字符串
              const file = fs.openSync(uris[0], fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
              const content = '这是要写入DOC文件的文本内容';
              fs.writeSync(file.fd, content);
              fs.closeSync(file.fd);
              console.info('文件写入成功');
            });
          } catch (error) {
            console.error('文件操作失败:', error);
          }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
