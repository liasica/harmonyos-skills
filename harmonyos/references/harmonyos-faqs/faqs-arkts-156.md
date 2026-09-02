---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-156
title: 音视频文件转换Base64字符串
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 音视频文件转换Base64字符串
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9763248d446b8b1974bab5f9dadf46b307680f2882d3f1816aad9fb66266fd27
---

## 问题现象

业务场景需要在H5页面使用Base64字符串播放音视频，如何将录制的视频、录音的音频文件转换为Base64字符串？

## 背景知识

Base64编码常用于存储二进制数据，如图片、视频、音频文件等，因为它将数据转换为可打印字符，避免了二进制数据在存储过程中可能出现的问题。HarmonyOS提供了工具类[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)进行Base64编解码。

## 解决方案

1. 读取音视频文件调用[encodeSync](../harmonyos-references/js-apis-util.md#encodesync9)函数得到Base64字符串。示例代码如下：

   ```ts
   videoToBase64() {
     // 读取rawfile目录下的sample.mp4视频
     let rawfileContent = this.getUIContext().getHostContext()?.resourceManager.getRawFileContentSync('sample.mp4');
     let base64Helper = new util.Base64Helper();
     let base64Result = base64Helper.encodeSync(rawfileContent);
     let base64ResultArrayBuffer:ArrayBuffer = base64Result.buffer.slice(0);
     console.info('the videoBase64 is: ' + base64Result);
     // 保存到沙箱目录下
     let path = this.getUIContext().getHostContext()?.filesDir + '/Vbase64.txt';
     let sandBoxFile = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
     fs.write(sandBoxFile.fd, base64ResultArrayBuffer).then((writeLen:number) => {
       console.info('write data size: ' + writeLen);
     }).catch((err:BusinessError) => {
       console.info('write sandboxFile data failed: ' + err.message + 'error code: ' + err.code);
     }).finally(() => {
       fs.closeSync(sandBoxFile);
     });
     this.base64 = this.uint8ArrayToString(base64Result);
     console.info('base64 String is: ' + this.base64);
   }
   ```
2. 从Base64转回原视频，读取Base64数据到ArrayBuffer使用[decode](../harmonyos-references/js-apis-util.md#decode9)解码Base64并写入到沙箱中：

   ```ts
   base64ToVideo() {
     let path = this.getUIContext().getHostContext()?.filesDir + '/Vbase64.txt';
     let sandBoxFile = fs.openSync(path, fs.OpenMode.READ_ONLY);
     let fileStat = fs.statSync(path);
     let arrayBuffer:ArrayBuffer = new ArrayBuffer(fileStat.size);
     fs.read(sandBoxFile.fd, arrayBuffer, (err:BusinessError) => {
       if (err) {
         console.error('read failed with error message: ' + err.message + ', error code: ' + err.code);
       } else {
         console.info('read file data succeed');
         let base64Helper = new util.Base64Helper();
         let videoPath = this.getUIContext().getHostContext()?.filesDir + '/Vbase64.mp4';
         let videoFile = fs.openSync(videoPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
         let uint8Array:Uint8Array = new Uint8Array(arrayBuffer);
         base64Helper.decode(uint8Array, util.Type.MIME).then((res) => {
           console.info('decode base64:' + res.toString());
           let oringData:ArrayBuffer = res.buffer.slice(0);
           fs.write(videoFile.fd, oringData).then((writeLen:number) => {
             console.info('write data size: ' + writeLen);
           }).catch((err:BusinessError) => {
             console.info('write videoFile data failed: ' + err.message + 'error code: ' + err.code);
           }).finally( () => {
             fs.closeSync(videoFile);
           });
         });
       }
       fs.closeSync(sandBoxFile);
     });
   }
   ```

完整示例代码如下：

```ts
import fs from '@ohos.file.fs';
import util from '@ohos.util';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State base64:string = '';

  uint8ArrayToString(array: Uint8Array) {
    let textDecoderOptions: util.TextDecoderOptions = {
      fatal: false,
      ignoreBOM: true
    };
    let decodeToStringOptions: util.DecodeToStringOptions = {
      stream: false
    };
    let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
    let retStr = textDecoder.decodeToString(array, decodeToStringOptions);
    console.info('Byte flow into understandable strings：' + retStr);
    return retStr;
  }

  videoToBase64() {
    // 读取rawfile目录下的sample.mp4视频
    let rawfileContent = this.getUIContext().getHostContext()?.resourceManager.getRawFileContentSync('sample.mp4');
    let base64Helper = new util.Base64Helper();
    let base64Result = base64Helper.encodeSync(rawfileContent);
    let base64ResultArrayBuffer:ArrayBuffer = base64Result.buffer.slice(0);
    console.info('the videoBase64 is: ' + base64Result);
    // 保存到沙箱目录下
    let path = this.getUIContext().getHostContext()?.filesDir + '/Vbase64.txt';
    let sandBoxFile = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    fs.write(sandBoxFile.fd, base64ResultArrayBuffer).then((writeLen:number) => {
      console.info('write data size: ' + writeLen);
    }).catch((err:BusinessError) => {
      console.info('write sandboxFile data failed: ' + err.message + 'error code: ' + err.code);
    }).finally(() => {
      fs.closeSync(sandBoxFile);
    });
    this.base64 = this.uint8ArrayToString(base64Result);
    console.info('base64 String is: ' + this.base64);
  }

  base64ToVideo() {
    let path = this.getUIContext().getHostContext()?.filesDir + '/Vbase64.txt';
    let sandBoxFile = fs.openSync(path, fs.OpenMode.READ_ONLY);
    let fileStat = fs.statSync(path);
    let arrayBuffer:ArrayBuffer = new ArrayBuffer(fileStat.size);
    fs.read(sandBoxFile.fd, arrayBuffer, (err:BusinessError) => {
      if (err) {
        console.error('read failed with error message: ' + err.message + ', error code: ' + err.code);
      } else {
        console.info('read file data succeed');
        let base64Helper = new util.Base64Helper();
        let videoPath = this.getUIContext().getHostContext()?.filesDir + '/Vbase64.mp4';
        let videoFile = fs.openSync(videoPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
        let uint8Array:Uint8Array = new Uint8Array(arrayBuffer);
        base64Helper.decode(uint8Array, util.Type.MIME).then((res) => {
          console.info('decode base64:' + res.toString());
          let oringData:ArrayBuffer = res.buffer.slice(0);
          fs.write(videoFile.fd, oringData).then((writeLen:number) => {
            console.info('write data size: ' + writeLen);
          }).catch((err:BusinessError) => {
            console.info('write videoFile data failed: ' + err.message + 'error code: ' + err.code);
          }).finally( () => {
            fs.closeSync(videoFile);
          });
        });
      }
      fs.closeSync(sandBoxFile);
    });
  }
  build() {
    Column() {
      Button('videoToBase64txt')
      // 保存编码后的base64到沙箱中
        .onClick( () => {
          this.videoToBase64();
        })
      Button('base64txtToVideo')
      // 从沙箱加载base64解码成原视频到沙箱中
        .onClick(()=> {
          this.base64ToVideo();
        })
    }
  }
}
```

## 常见FAQ

Q：转换后的Base64字符串添加到页面中用Video组件加载是可以正常显示的，但是打印出的log日志通过在线Base64转视频工具转换后无法正常显示。

A：日志有长度限制，输出的日志只是Base64字符串一部分。建议使用TextArea组件获取视频转换后完整的Base64字符串，或者将输出的Base64字符串保存进应用沙箱路径的文件中。
