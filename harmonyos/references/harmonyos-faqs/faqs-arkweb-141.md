---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-141
title: 如何使用Web播放16进制数据流格式的音频
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何使用Web播放16进制数据流格式的音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2431813d510c690018d47eec921e1bd804804fa1ad65b7397875ed2aa3d738cf
---

## 问题现象

接口返回的是mp3音频转化的16进制数据流，要如何通过Web页面嵌入的方式播放这段音频。

## 背景知识

* [Webview](../harmonyos-references/arkts-apis-webview.md)：@ohos.web.webview提供Web控制能力，Web组件提供网页显示的能力。
* [runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)：注入JavaScript脚本。

## 解决方案

通过Web注入JavaScript脚本的方式来动态把要播放的音频文件传给H5，再通过H5的audioPlayer进行音频播放。

```screen
import { webview } from '@kit.ArkWeb';
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { filePreview } from '@kit.PreviewKit';

@Entry
@Component
struct WebText {
  @State musics: Array<string> = [];
  private context: Context = this.getUIContext().getHostContext() as Context;
  // 在线链接，返回音频的16进制数据流
  private url: string = 'www.example.com';
  private sandbox: string = this.context.cacheDir + '/new.text';
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    filePreview.canPreview(this.context, this.sandbox).then((result) => {
      if (!result) {
        let file = fs.openSync(this.sandbox, fs.OpenMode.CREATE);
        fs.close(file, (err: BusinessError) => {
          if (err) {
            console.error('close file failed with error message: ' + err.message + ', error code: ' + err.code);
          } else {
            console.info('close file succeed');
          }
        });
      }
    }).catch((err: BusinessError) => {
      console.error('close file failed with error message: ' + err.message + ', error code: ' + err.code);

    });
  }

  build() {
    Column() {
      Column() {
        Web({ src: $rawfile('audio.html'), controller: this.controller })
          .domStorageAccess(true)
          .javaScriptAccess(true)
          .fileAccess(false)
          .geolocationAccess(false);
      }
      .height('20%')
      .width('100%');

      Column() {
        ForEach(this.musics, (item: string) => {
          ListItem() {
            Text('点击"' + item.toString().substring(0, 10) + '"播放该音频')
              .fontSize(16)
              .textAlign(TextAlign.Start)
              .size({ height: 10, width: '100%' })
              .onClick(() => {
                try {
                  this.controller.runJavaScript(
                    'playAudio("' + item + '")',
                    (error, result) => {
                      if (error) {
                        console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                        console.info(`result is: ${result}`);
                        return;
                      }
                    });
                } catch (error) {
                  console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                }
              });
          }.margin(10)
          .borderRadius(10)
          .backgroundColor($r('sys.color.navigation_drag_bar_item_default'));
        }, (item: string) => item);

      }.height('60%')
      .width('100%');

      Column() {
        Button('获取在线音频并存到沙箱').onClick(() => {
          this.readText();
          if (!this.musics || this.musics.length === 0) {
            this.postHttp();
          }
        });
      }.height('10%')
      .width('100%');

    }.height('100%')
    .width('100%');
  }

  private postHttp() {
    let httpRequest = http.createHttp();
    httpRequest.on('headersReceive', (header) => {
      console.info(`header:${header}`);
    });
    httpRequest.request(
      this.url,
      {
        method: http.RequestMethod.POST,
        header: {
          'contentType': 'application/json'
        },
        extraData: 'data to send',
        expectDataType: http.HttpDataType.STRING,
        usingCache: true,
        priority: 1,
        connectTimeout: 60000,
        readTimeout: 60000,
        usingProtocol: http.HttpProtocol.HTTP1_1,
        usingProxy: false
      }, async (err: BusinessError, data: http.HttpResponse) => {
      if (!err) {
        let strr = data.result as string;
        let lines = strr.split('\n');
        this.musics = [];
        for (let i = 0; i < lines.length; i++) {
          if (lines[i] && lines[i] !== '' && lines[i].startsWith('data:')) {
            let linei = lines[i].slice(5);
            let dataEntry: DataEntry = JSON.parse(linei) as DataEntry;
            let resultData: ResultData = dataEntry.data;
            let music = resultData.audio;
            if (music && music !== '') {
              this.musics.push(music);
              this.createText(music);
            }
          }
        }
        httpRequest.destroy();
      } else {
        httpRequest.off('headersReceive');
        httpRequest.destroy();
      }
    }
    );
  }

  private createText(music: string) {
    let file = fs.openSync(this.sandbox, fs.OpenMode.READ_WRITE | fs.OpenMode.APPEND);
    fs.writeSync(file.fd, music + '\n');
    fs.close(file, (err: BusinessError) => {
      if (err) {
        console.error('close file failed with error message: ' + err.message + ', error code: ' + err.code);
      } else {
        console.info('close file succeed');
      }
    });
  }

  private readText() {
    fs.readText(this.sandbox).then((str: string) => {
      let lines = str.split('\n');
      this.musics = [];
      for (let i = 0; i < lines.length; i++) {
        let music = lines[i];
        if (music && music !== '') {
          this.musics.push(music);
        }
      }
    }).catch((err: BusinessError) => {
      console.error('readText failed with error message: ' + err.message + ', error code: ' + err.code);
    });
  }
}

class DataEntry {
  data: ResultData = new ResultData;
}

class ResultData {
  audio: string = '';
}
```

html：

```screen
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>播放音频</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
        }
        button {
            margin-top: 10px;
        }
        audio {
            margin-top: 10px;
        }
    </style>
</head>
<body onload='playAudio()'>
<audio id="audioPlayer" muted="" controls></audio>
<script>
    function playAudio(hexInput) {
        // 将16进制字符串转换为二进制字节数组
        const binaryData = Uint8Array.from(hexInput.match(/.{1,2}/g), byte => parseInt(byte, 16));
        // 创建一个Blob对象
        const blob = new Blob([binaryData], { type: 'audio/mpeg' });
        // 创建一个URL对应于该Blob
        const url = URL.createObjectURL(blob);
        // 设置音频元素的src属性
        const audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.src = url;
        // 播放音频
        audioPlayer.play().catch(error => {
        });
    }
</script>
</body>
</html>
```
