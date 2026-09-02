---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-27
title: 如何解决屏幕停止录制后，无法开始第二次录制的问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何解决屏幕停止录制后，无法开始第二次录制的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9019c68b6c8ba2ddc275ba7f8aeb824ecc161ce70abb177a3b97305b0a7b4774
---

## 问题现象

为了等屏幕旋转完成后再设置视频流的宽高，在开始录制的时候进行init，但是只有首次能够初始化成功，第二次则会触发报错，最终无法改变状态。

报错内容为：

```txt
12-04 15:05:07.761   49057-49175   C02B2E/Restart...enCaptureImpl  com.a.Res...Recorder  E     #204 SetCaptureMode failed
12-04 15:05:07.761   49057-49175   P02B2E/Restart...enCaptureNapi  com.a.Res...Recorder  E     {operator()():616} ret == MSERR_OK, check failed! ret = ((void)napi->screenCapture_->Release(), GetReturnInfo(ret, "Init", ""))
12-04 15:05:07.762   49057-49057   C03919/Restart...InputTracking  com.a.Res...Recorder  I     [(100000:100000:scope)] Consumed id:19294, last id:19293
12-04 15:05:07.762   49057-49057   C04213/RestartA...InputKeyFlow  com.a.Res...Recorder  I     ConsumePointerEventInner: InputId:19294,wid:212,pointId:0,srcType:2,rect:[0,0,1216,2688],notify:1
12-04 15:05:07.762   49057-49175   C02B2E/Restart...enCaptureNapi  com.a.Res...Recorder  E     #190 failed to Init, param , errCode = 331350054
12-04 15:05:07.763   49057-49175   C02B2E/Restart...enCaptureNapi  com.a.Res...Recorder  E     #200 errCode: 5400102, errMsg: The operate Init failed due to not permit in current state.
12-04 15:05:07.763   49057-49175   C02B2E/Restart...enCaptureNapi  com.a.Res...Recorder  I     #1046 StartRecording Start
12-04 15:05:07.763   49057-49173   C02B2B/Restart...er/CommonNapi  com.a.Res...Recorder  E     #855 SignError: The operate Init failed due to not permit in current state.
12-04 15:05:07.763   49057-49175   C02B2E/Restart...enCaptureImpl  com.a.Res...Recorder  I     #125 ScreenCaptureImpl:0x29FC58 isPrivacyAuthorityEnabled:1
12-04 15:05:07.763   49057-49173   C02B2E/Restart...enCaptureNapi  com.a.Res...Recorder  I     #386 The js thread of init finishes execution and returns
12-04 15:05:07.763   49057-49057   C01320/Restart...ecorder/JsEnv  com.a.Res...Recorder  W     [source_map145]the stack without line info
12-04 15:05:07.763   49057-49057   C02B2B/Restart...er/CommonNapi  com.a.Res...Recorder  E     #915 promise napi_reject_deferred
```

问题代码如下：

```ts
 @Component
 export struct ScreenRecordWrapper {
   @State lastTime: number = 180 // 剩余时间，视频打卡默认三分钟
   @State hasStart: boolean = false
   private timer: number | null = null
   private avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined = undefined;

   aboutToAppear(): void {
     try {
       this.createAVScreenCapture();
     } catch (exception) {
       console.error(`Failed to obtain the default display object. Code: ${JSON.stringify(exception)}`);
     }
   }

   createAVScreenCapture() {
     media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
       if (captureRecorder != null) {
         this.avScreenCaptureRecorder = captureRecorder;
         // 注册监听事件
         this.avScreenCaptureRecorder.on('stateChange', (state: media.AVScreenCaptureStateCode) => {
           switch (state) {
             case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STARTED:
               this.hasStart = !this.hasStart
               this.timer = setInterval(() => {
                 if (this.lastTime > 0) {
                   this.lastTime = this.lastTime - 1
                 } else {
                   this.stopRecord()
                 }
               }, 1000)
               break;
           }
         })
       }
     })
   }

   async init() {
     if (this.avScreenCaptureRecorder !== undefined) {
       await this.avScreenCaptureRecorder.init(this.avCaptureConfig).then(() => {
         console.info('Succeeded init avScreenCaptureRecorder');
       }).catch((err: BusinessError) => {
         console.error(`Failed to init avScreenCaptureRecorder, error: ${err.message}`);
       })
     }
   }
 }
```

## 背景知识

音视频录制参考链接：

* [媒体服务](../harmonyos-guides/media-kit.md)：媒体子系统为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源，其中可调用[AVScreenCaptureRecorder](../harmonyos-guides/using-avscreencapture-arkts.md)模块完成屏幕录制，采集设备内、麦克风等的音视频源数据。
* [media.createAVScreenCaptureRecorder](../harmonyos-references/arkts-apis-media-f.md#mediacreateavscreencapturerecorder12)：创建屏幕录制实例。

## 解决方案

1. 由报错日志中的[错误码5400102](../harmonyos-references/arkts-apis-media-e.md#averrorcode9)可知，调用[stopRecording](../harmonyos-references/arkts-apis-media-avscreencapturerecorder.md#stoprecording12)后的AVScreenCaptureRecorder状态不允许或无权执行[init](../harmonyos-references/arkts-apis-media-avscreencapturerecorder.md#init12)操作，因此第二次录制需要重新创建屏幕录制实例再进行init。
2. 需将createAVScreenCapture方法改为同步操作以确保AVScreenCaptureRecorder实例为新创建的可初始化的实例。

修改方式如下：

```ts
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct ScreenRecordWrapper {
  private lastTime: number = 10; // 剩余时间，视频打卡默认10秒
  private hasStart: boolean = false;
  private timer: number | null = null;
  private avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined = undefined;
  private avCaptureConfig: media.AVScreenCaptureRecordConfig | undefined = undefined;
  private captureFile: fs.File | undefined = undefined;
  private context: Context | undefined = undefined;

  private openFile(context: Context): void {
    const path: string = context.filesDir + '/screenCapture.mp4'; // 文件沙箱路径，文件后缀名应与封装格式对应。
    try {
      this.captureFile = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    } catch (error) {
      console.error(`fs.openSync error info: ${JSON.stringify(error)}`);
    }
  }

  private closeFile(): void {
    if (!this.captureFile) {
      return;
    }
    try {
      fs.closeSync(this.captureFile);
    } catch (error) {
      console.error(`fs.closeSync error info: ${JSON.stringify(error)}`);
    }
  }

  // 初始化avScreenCaptureRecorder
  async init() {
    if (this.avScreenCaptureRecorder !== undefined) {
      await this.avScreenCaptureRecorder.init(this.avCaptureConfig).then(() => {
        console.info('Succeeded init avScreenCaptureRecorder');
      }).catch((err: BusinessError) => {
        console.error(`Failed to init avScreenCaptureRecorder, error: ${err.message}`);
      });
    }
  }

  // 创建avScreenCaptureRecorder并注册监听
  async createAVScreenCapture() {
    try {
      this.avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();
      if (!this.avScreenCaptureRecorder) {
        return;
      }
      // 注册监听事件
      this.avScreenCaptureRecorder.on('stateChange', (state: media.AVScreenCaptureStateCode) => {
        switch (state) {
          case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STARTED:
            this.hasStart = !this.hasStart;
            console.info('start avScreenCaptureRecorder success');
            // 配置10秒结束录制倒计时
            this.timer = setInterval(async () => {
              if (this.lastTime > 0) {
                this.lastTime = this.lastTime - 1;
              } else {
                await this.stopRecord();
                clearInterval(this.timer);
                this.lastTime = 10;
              }
            }, 1000);
            break;
          case media.AVScreenCaptureStateCode.SCREENCAPTURE_STATE_STOPPED_BY_USER:
            this.avScreenCaptureRecorder?.release();
            this.avScreenCaptureRecorder = undefined;
            console.info('stop avScreenCaptureRecorder success');
            break;
        };
      });
      // 注册监听事件
      this.avScreenCaptureRecorder.on('error', (err: BusinessError) => {
        console.error(`avScreenCaptureRecorder error: Code: ${err.code}, message: ${err.message}`);
      });
    } catch (error) {
      console.error(`error info: ${JSON.stringify(error)}`);
    }
  }

  // 停止录屏
  async stopRecord() {
    this.avScreenCaptureRecorder?.stopRecording().then(() => {
      console.info('Succeeded in stopping avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to stop avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
    this.avScreenCaptureRecorder?.off('stateChange');
    this.avScreenCaptureRecorder?.off('error');
    this.avScreenCaptureRecorder?.release();
    this.closeFile();
  }

  // 配置录屏参数并创建文件
  setConfig() {
    if (this.context) {
      // 创建文件。
      this.openFile(this.context);
    }
    this.avCaptureConfig = {
      // 开发者可以根据自身的需要设置宽高。
      frameWidth: 768,
      frameHeight: 1280,
      // 参考应用文件访问与管理开发示例新建并读写一个文件fd。
      fd: this.captureFile!.fd,
      // 可选参数及其默认值。
      videoBitrate: 10000000,
      audioSampleRate: 48000,
      audioChannelCount: 2,
      audioBitrate: 96000,
      displayId: 0,
      preset: media.AVScreenCaptureRecordPreset.SCREEN_RECORD_PRESET_H264_AAC_MP4
    };
  }

  aboutToAppear(): void {
    this.context = this.getUIContext().getHostContext();
  }

  aboutToDisappear(): void {
    this.stopRecord();
  }

  build() {
    Column() {
      Row({ space: 30 }) {
        Button('开始录屏')
          .fontSize(20)
          .onClick(async () => {
            try {
              await this.createAVScreenCapture();
            } catch (exception) {
              console.error(`Failed to obtain the default display object. Code: ${JSON.stringify(exception)}`);
            }
            this.setConfig();
            this.init();
            this.avScreenCaptureRecorder?.startRecording();
          })
      }
    }
  }
}
```

## 总结

AVScreenCaptureRecorder不支持停止后第二次init屏幕录制实例，需要以同步的方式重新创建屏幕录制实例再进行初始化。
