---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/audio-kit-faq-0002
title: 音频播放功能实现常见问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 常见问题 > 音频播放功能实现常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:39+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:9bdffdf812d5f329b330e83b430eacd62e8fb93da17939dba8fe7b42dc63da1e
---

**Q：如何后台播放音乐？**

**A**：AVSession管控媒体播放。当第三方应用从前台切换到后台或进入锁屏状态时，媒体播放会强制暂停，且应用不会感知。若需开发后台播放功能，应在后台任务管理中启动长时任务播放音乐，并接入AVSession能力，允许控制中心的播控面板控制第三方应用的播放功能。

参考链接：[backgroundTaskManager.startBackgroundRunning](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12)、[媒体会话提供方](../harmonyos-guides/using-avsession-developer.md)。

**Q：从服务端获取的生成式语音字符串，如何正常播放？**

**A**：处理方式如下：

1. 使用[HttpRequest](../harmonyos-references/js-apis-http.md#httprequest)的[request方法](../harmonyos-references/js-apis-http.md#request)，传入请求的url地址和可选的参数，发起HTTP数据请求，并在回调中根据实际的业务需求，解析服务端响应的内容（需根据不同的服务端返回内容格式，重写解析方法）。

   ```ts
   private async postHttp() {
       let httpRequest = http.createHttp();
       httpRequest.on('headersReceive', (header) => {
         hilog.info(0x0000, 'testTag', '---httpRequestSucess%{public}s', header);
       });
       let avPlayer: media.AVPlayer = await media.createAVPlayer();
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
           this.musics = '';
           for (let i = 0; i < lines.length; i++) {
             if (lines[i] && lines[i] !== '' && lines[i].startsWith('data:')) {
               let linei = lines[i].slice(5);
               let dataEntry: DataEntry = JSON.parse(linei) as DataEntry;
               let resultData: ResultData = dataEntry.data;
               let music = resultData.audio;
               if (music && music !== '') {
                 this.musics += music;
               }
             }
           }
           let fileName = this.save(this.musics);
           this.avPlayerDataSrcNoSeekDemo(avPlayer, fileName);
           httpRequest.destroy();
         } else {
           httpRequest.off('headersReceive');
           httpRequest.destroy();
         }
       }
       );
     }
   ```
2. 将服务端响应的字符串格式的数据转换成mp3格式的数据，并存储在本地应用沙箱目录下。

   ```ts
   save(music: string) {
       const arraybuffer = this.hexStringToArrayBuffer(music);
       let fileName = `temp_audio_${Date.now()}.mp3`;
       const filePath = `${this.context?.filesDir}/${fileName}`;
       const file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
       try {
         fs.writeSync(file.fd, arraybuffer);
       } finally {
         fs.closeSync(file);
       }
       return fileName;
     }

     hexStringToArrayBuffer(hex: string): ArrayBuffer {
       const len = hex.length / 2;
       const buffer = new ArrayBuffer(len);
       const uint8Array = new Uint8Array(buffer);
       for (let i = 0; i < len; i++) {
         uint8Array[i] = parseInt(hex.substr(i * 2, 2), 16);
       }
       return buffer;
     }
   ```
3. 使用AVPlayer播放存储在本地应用沙箱目录下的mp3音频文件。

   ```ts
   async avPlayerDataSrcNoSeekDemo(avPlayer: media.AVPlayer, fileName: string) {
       this.setAVPlayerCallback(avPlayer);
       let src: media.AVDataSrcDescriptor = {
         fileSize: -1,
         callback: (buf: ArrayBuffer, length: number) => {
           let num = 0;
           if (buf === undefined || length === undefined) {
             return -1;
           }
           num = fs.readSync(this.fd, buf);
           if (num > 0) {
             return num;
           }
           return -1;
         }
       };
       if (this.context !== undefined) {
         let pathDir = this.context.filesDir;
         let path = pathDir + `/${fileName}`;
         let file = fs.openSync(path);
         this.fd = file.fd;
         avPlayer.dataSrc = src;
       }
     }
   ```
4. 完整的demo如下：

   ```ts
   import { http } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { audio } from '@kit.AudioKit';
   import { media } from '@kit.MediaKit';

   @Entry
   @Component
   export struct Player {
     // 在线链接，返回音频的16进制数据流
     private url: string = 'www.example.com';
     private context: Context | undefined = this.getUIContext().getHostContext();
     @State musics: string = '';
     fd: number = 0;

     build() {
       Column() {
         Button(`下载播放`).onClick(() => {
           this.postHttp();
         });
       }.width('100%');

     }
     private async postHttp() {
       let httpRequest = http.createHttp();
       httpRequest.on('headersReceive', (header) => {
         hilog.info(0x0000, 'testTag', '---httpRequestSucess%{public}s', header);
       });
       let avPlayer: media.AVPlayer = await media.createAVPlayer();
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
           this.musics = '';
           for (let i = 0; i < lines.length; i++) {
             if (lines[i] && lines[i] !== '' && lines[i].startsWith('data:')) {
               let linei = lines[i].slice(5);
               let dataEntry: DataEntry = JSON.parse(linei) as DataEntry;
               let resultData: ResultData = dataEntry.data;
               let music = resultData.audio;
               if (music && music !== '') {
                 this.musics += music;
               }
             }
           }
           let fileName = this.save(this.musics);
           this.avPlayerDataSrcNoSeekDemo(avPlayer, fileName);
           httpRequest.destroy();
         } else {
           httpRequest.off('headersReceive');
           httpRequest.destroy();
         }
       }
       );
     }
     save(music: string) {
       const arraybuffer = this.hexStringToArrayBuffer(music);
       let fileName = `temp_audio_${Date.now()}.mp3`;
       const filePath = `${this.context?.filesDir}/${fileName}`;
       const file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
       try {
         fs.writeSync(file.fd, arraybuffer);
       } finally {
         fs.closeSync(file);
       }
       return fileName;
     }

     hexStringToArrayBuffer(hex: string): ArrayBuffer {
       const len = hex.length / 2;
       const buffer = new ArrayBuffer(len);
       const uint8Array = new Uint8Array(buffer);
       for (let i = 0; i < len; i++) {
         uint8Array[i] = parseInt(hex.substr(i * 2, 2), 16);
       }
       return buffer;
     }
     async avPlayerDataSrcNoSeekDemo(avPlayer: media.AVPlayer, fileName: string) {
       this.setAVPlayerCallback(avPlayer);
       let src: media.AVDataSrcDescriptor = {
         fileSize: -1,
         callback: (buf: ArrayBuffer, length: number) => {
           let num = 0;
           if (buf === undefined || length === undefined) {
             return -1;
           }
           num = fs.readSync(this.fd, buf);
           if (num > 0) {
             return num;
           }
           return -1;
         }
       };
       if (this.context !== undefined) {
         let pathDir = this.context.filesDir;
         let path = pathDir + `/${fileName}`;
         let file = fs.openSync(path);
         this.fd = file.fd;
         avPlayer.dataSrc = src;
       }
     }
     setAVPlayerCallback(avPlayer: media.AVPlayer) {
       avPlayer.on('seekDone', (seekDoneTime: number) => {
         console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
       });
       avPlayer.on('error', (err: BusinessError) => {
         console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
         avPlayer.reset();
       });
       avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
         console.info(`${JSON.stringify(reason)}`);
         switch (state) {
           case 'idle':
             console.info('AVPlayer state idle called.');
             break;
           case 'initialized':
             console.info('AVPlayer state initialized called.');
             avPlayer.audioRendererInfo = {
               usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
               rendererFlags: 0
             };
             avPlayer.prepare();
             break;
           case 'prepared':
             console.info('AVPlayer state prepared called.');
             avPlayer.play();
             break;
           case 'completed':
             console.info('AVPlayer state completed called.');
             avPlayer.stop();
             break;
           case 'stopped':
             console.info('AVPlayer state stopped called.');
             avPlayer.reset();
             break;
           case 'released':
             console.info('AVPlayer state released called.');
             break;
           default:
             console.info('AVPlayer state unknown called.');
             break;
         }
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
