---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-75
title: 如何实现加解密下载文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何实现加解密下载文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:258305e7842f7c9c47c2fc1ae634a3bdf4ea0b5bfeaf53055e2d04d91d0673fb
---

## 问题现象

如何实现文件下载后加密存储到公共目录，使之无法打开查看，需要再次读取公共目录保存的加密文件进行解密后再次保存，方可正常查看？

## 背景知识

* [@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)：该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。
* [加解密开发指导](../harmonyos-guides/crypto-encrypt-decrypt-dev.md)：在数据存储或传输场景中，可以使用加解密操作用于保证数据的机密性，防止敏感数据泄露。
* [DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)：适用于文件类型文件的选择与保存。DocumentViewPicker对接的选择资源来自于FilePicker，负责文件类型的资源管理，文件类型不区分后缀，比如浏览器下载的图片、文档等，都属于文件类型。通过Picker访问相关文件，将拉起对应的应用，引导用户完成界面操作，接口本身无需申请权限。

## 解决方案

由问题可知实现此功能重点是如下两步：

1. 文件读取并加密后保存至公共目录；
2. 选择公共目录下的加密文件解密后，再次保存至公共目录。

**示例代码如下**（代码中使用AES对称密钥（ECB模式）加解密，亦可选择其他加解密算法；前置步骤需要配置网络权限已省略，请参考[配置网络权限](../harmonyos-guides/graphics-accelerate-assetdownload-prepare.md#配置网络权限)）：

```ts
import { BusinessError, request } from '@kit.BasicServicesKit';
import picker from '@ohos.file.picker';
import fs from '@ohos.file.fs';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
let symKey = genSymKeyByData(keyData);

function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = aesGenerator.convertKeySync(symKeyBlob);
  return symKey;
}

// 加密消息
function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('AES128|ECB|PKCS7');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null); // ECB模式params为null。
  let cipherData = cipher.doFinalSync(plainText);
  return cipherData;
}

// 解密消息
function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('AES128|ECB|PKCS7');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null); // ECB模式params为null。
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

function getPlainText(file: fs.File) {
  let stat = fs.statSync(file.path); // 获取文件状态
  let buf = new ArrayBuffer(stat.size); // 创建一个ArrayBuffer对象
  let num = fs.readSync(file.fd, buf); // 读取文件
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buf.slice(0, num)) };
  return plainText;
}

@Entry
@Component
export struct DocumentSave {
  context = this.getUIContext().getHostContext() as Context;
  // downloadUrl替换为实际文件下载链接
  downloadUrl: string = 'https://xxx/xxx/xx.docx';

  // 下载文件并加密内容
  downloadFileAndEncrypt() {
    // 自定义文件名以及文件格式
    const fileName = `test${Date.now()}.docx`;
    request.downloadFile(this.context, {
      enableMetered: true,
      url: this.downloadUrl,
      filePath: `${this.context.filesDir}/${fileName}`, // 沙箱路径
    }).then((downloadTask: request.DownloadTask) => {
      downloadTask.on('complete', () => {
        const documentSaveOptions = new picker.DocumentSaveOptions(); // 创建文件管理器保存选项实例
        documentSaveOptions.newFileNames = [fileName]; // 保存文件名
        const documentViewPicker = new picker.DocumentViewPicker;
        documentViewPicker.save(documentSaveOptions)
          .then(async (documentSaveResult) => {
            // 获取到图片或者视频文件的URI后进行文件读取等操作
            let uri = documentSaveResult[0];
            if (uri) {
              // 沙箱路径文件
              let sanFile =
                fs.openSync(`${this.context.filesDir}/${fileName}`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
              let pubFile = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
              const plainText = getPlainText(sanFile);
              // 加密
              let encryptText = encryptMessage(symKey, plainText);
              fs.writeSync(pubFile.fd, encryptText.data.buffer);
              fs.unlink(sanFile.path);
            } else {
              // 取消保存到用户目录之后，删除沙箱目录下保存的文件
              fs.rmdirSync(`${this.context.filesDir}/${fileName}`);
            }
          }
          );
      });
    }
    ).catch((err: BusinessError) => {
      console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
    });
  }

  // 文件解密
  async decryptFile() {
    let uri: string = '';
    // 自定义文件名以及文件格式
    const fileName = `test${Date.now()}.docx`;
    let documentSelectOptions = new picker.DocumentSelectOptions();
    documentSelectOptions.fileSuffixFilters = [];
    documentSelectOptions.maxSelectNumber = 1;
    let documentViewPicker = new picker.DocumentViewPicker();
    await documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
      uri = decodeURIComponent(documentSelectResult[0]);
      let pubFile = fs.openSync(uri, fs.OpenMode.READ_ONLY);
      let file =
        fs.openSync(`${this.context.filesDir}/${fileName}`, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE); // 打开文件

      const plainText = getPlainText(pubFile);
      let decryptText = decryptMessage(symKey, plainText);
      fs.writeSync(file.fd, decryptText.data.buffer);
      const documentSaveOptions = new picker.DocumentSaveOptions(); // 创建文件管理器保存选项实例
      documentSaveOptions.newFileNames = [fileName];
      documentViewPicker.save(documentSaveOptions).then(async (documentSaveResult) => {
        let uri = documentSaveResult[0];
        if (uri) {
          let pubFile = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
          fs.copyFileSync(file.fd, pubFile.fd);
          fs.unlink(file.path);
        } else {
          fs.rmdirSync(`${this.context.filesDir}/${fileName}`);
        }
      });
    }).catch((err: Error) => {
      console.error(`Invoke documentViewPicker.select failed, code is ${err}, message is ${err.message}`);
    });
  }

  build() {
    RelativeContainer() {
      Row() {
        Button('下载加密保存')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.downloadFileAndEncrypt();
          });
        Button('解密后保存')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.decryptFile();
          });
      };
    }
    .height('100%')
    .width('100%');
  }
}
```
