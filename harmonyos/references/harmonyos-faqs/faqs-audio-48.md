---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-48
title: H5页面中实现扬声器听筒切换
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > H5页面中实现扬声器听筒切换
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:12350160849a70b9974d7d3326313436530df7f0151caad73aaeb3dc07bdd3a9
---

## 问题现象

如何在H5页面中播放音频，并且实现扬声器听筒切换？

## 背景知识

* [setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)：设置默认发声设备。本接口仅适用于[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为语音消息、VoIP语音通话或者VoIP视频通话的场景，支持听筒、扬声器和系统默认设备。
* [AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)：用于音频输出的API，仅支持PCM格式，需要应用持续写入音频数据进行工作。应用可以在输入前添加数据预处理，如设定音频文件的采样率、位宽、音频流信息等。
* [javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)：将javaScriptProxy中的ArkTS对象注册到Web组件中，该对象将使用JavaScriptProxy中指定的名称注册到网页的所有框架中。

**说明** 

javaScriptProxy接口需要和deleteJavaScriptRegister接口配合使用，防止内存泄漏，并且javaScriptProxy对象的所有参数不支持更新。

## 解决方案

* 使用AudioRenderer播放音频，详情可以参考AudioRenderer[开发步骤和注意事项](../harmonyos-guides/using-audiorenderer-for-playback.md#开发步骤及注意事项)以及[完整示例代码](../harmonyos-guides/using-audiorenderer-for-playback.md#完整示例)。
* 调用setDefaultOutputDevice()方法进行听筒和扬声器的切换。

  参考示例代码如下

  ```ts
  class OutputDeviceChange {
    // 扬声器播放
    async changeToSpeaker() {
      audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
        console.info('setDefaultOutputDevice to SPEAKER Success!');
      }).catch((err: BusinessError) => {
        console.error(`setDefaultOutputDevice Fail: ${err}`);
      });
    }
    // 听筒播放
    async changeToEarpiece() {
      audioRenderer.setDefaultOutputDevice(audio.DeviceType.EARPIECE).then(() => {
        console.info('setDefaultOutputDevice to EARPIECE Success!');
      }).catch((err: BusinessError) => {
        console.error(`setDefaultOutputDevice Fail: ${err}`);
      });
    }
    // AudioRenderer播放音频
    async startRenderer() {
      await audioRenderer.start();
    }
  }
  ```
* 使用javaScriptProxy()接口在前端页面调用应用侧函数，详情可以参考[如何建立应用侧与h5侧的交互通道](../harmonyos-guides/web-in-page-app-function-invoking.md#如何建立应用侧与h5侧的交互通道)。

完整示例代码参考如下：

```ts
import { audio } from '@kit.AudioKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { webview } from '@kit.ArkWeb';

// 设置AudioRenderer参数
let audioRenderer: audio.AudioRenderer;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_8000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_1, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

class OutputDeviceChange {
  // 扬声器播放
  async changeToSpeaker() {
    audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
      console.info('setDefaultOutputDevice to SPEAKER Success!');
    }).catch((err: BusinessError) => {
      console.error(`setDefaultOutputDevice Fail: ${err}`);
    });
  }
  // 听筒播放
  async changeToEarpiece() {
    audioRenderer.setDefaultOutputDevice(audio.DeviceType.EARPIECE).then(() => {
      console.info('setDefaultOutputDevice to EARPIECE Success!');
    }).catch((err: BusinessError) => {
      console.error(`setDefaultOutputDevice Fail: ${err}`);
    });
  }
  // AudioRenderer播放音频
  async startRenderer() {
    await audioRenderer.start();
  }
}

@Entry
@Component
struct PlayPcmDataDemo {
  //声明需要注册的对象
  @State testObj: OutputDeviceChange = new OutputDeviceChange();
  webviewController: webview.WebviewController = new webview.WebviewController();
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  audioData: Uint8Array = generateTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
  writeOffset = 0;

  async aboutToAppear(): Promise<void> {
    audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    await this.init(); //初始化
  }

  async aboutToDisappear(): Promise<void> {
    await audioRenderer.release();
    this.stopAndFlush();
    try {
      this.webviewController.deleteJavaScriptRegister('testObjName');
    } catch (error) {
      console.error(`ErrorCode:${(error as BusinessError).code},Message:${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      // web组件加载本地html页面
      Web({ src: $rawfile('SetOutputDevice.html'), controller: this.webviewController })
        .geolocationAccess(false)
        .fileAccess(false)
        // 将对象注入web
        .javaScriptProxy({
          object: this.testObj,
          name: 'testObjName',
          methodList: ["startRenderer", "changeToEarpiece", "changeToSpeaker"],
          controller: this.webviewController,
        })
        .javaScriptAccess(true);
    };
  }

  async init() {
    audioRenderer.on('writeData', (buffer: ArrayBuffer) => {
      if (!this.audioData) {
        return audio.AudioDataCallbackResult.INVALID;
      }
      let bufferView = new Uint8Array(buffer);
      let writeLen = Math.min(buffer.byteLength, this.audioData.byteLength - this.writeOffset);
      if (writeLen <= 0) {
        this.writeOffset = 0;
        console.info('Play Done');
        return audio.AudioDataCallbackResult.INVALID;
      }
      bufferView.set(this.audioData.slice(this.writeOffset, this.writeOffset + writeLen));
      this.writeOffset += writeLen;
      return audio.AudioDataCallbackResult.VALID;
    });
  }

  async stopAndFlush() {
    console.info('renderer status' + audioRenderer.state);
    audioRenderer.stop().then(() => {
      console.error('Renderer stop ok.');
    }).catch((err: BusinessError) => {
      console.error('Renderer stop failed. ', err);
    })
    ;
    audioRenderer.flush().then(() => {
      console.error('Renderer flush ok.');
    }).catch((err: BusinessError) => {
      console.error('renderer flush err. ' + err);
    });
    this.writeOffset = 0;
  }
}

function generateTestPCM(): Uint8Array {
  const sampleRate = 8000;
  const noteDuration = 0.5;
  const amplitude = 0.35;

  const freqMap: Record<number, number> = {
    1: 523.25, // C5
    2: 587.33, // D5
    3: 659.25, // E5
    4: 698.46, // F5
    5: 783.99, // G5
    6: 880.00  // A5
  };

  const melody = [
    1, 1, 5, 5, 6, 6, 5, 0,
    4, 4, 3, 3, 2, 2, 1, 0,
    5, 5, 4, 4, 3, 3, 2, 0
  ];

  const samplesPerNote = Math.floor(sampleRate * noteDuration); // 4000
  const totalSamples = samplesPerNote * melody.length; // 96,000
  const buffer = new ArrayBuffer(totalSamples * 2); // 192,000 bytes
  const view = new DataView(buffer);

  let idx = 0;
  for (const note of melody) {
    const freq = note ? freqMap[note] : 0;
    for (let i = 0; i < samplesPerNote; i++) {
      const t = i / sampleRate;
      const wave = freq ? amplitude * Math.sin(2 * Math.PI * freq * t) : 0;
      const sample = Math.round(wave * 32767);
      const clamped = Math.max(-32768, Math.min(32767, sample));
      view.setInt16(idx * 2, clamped, true);
      idx++;
    }
  }
  return new Uint8Array(buffer);
}
```

html页面：

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<div align="center">
<button type="button" onclick="audioPlay()" style="width: 450px; height: 120px;font-size: 50px;">Play</button>
<p id="demo"></p>
<script>
    function audioPlay() {
        let str = testObjName.startRenderer();
        document.getElementById("demo").innerHTML = str;
    }
</script>

<button type="button" onclick="changeToEarpiece()" style="width: 450px; height: 120px;font-size: 50px;">ChangeEarpiece</button>
<p id="demo1"></p>
<script>
    function changeToEarpiece() {
        let str = testObjName.changeToEarpiece();
        document.getElementById("demo1").innerHTML = str;
    }
</script>

<button type="button" onclick="changeToSpeaker()" style="width: 450px; height: 120px;font-size: 50px;">ChangeSpeaker</button>
<p id="demo2"></p>
<script>
    function changeToSpeaker() {
        let str = testObjName.changeToSpeaker();
        document.getElementById("demo2").innerHTML = str;
    }
</script>
</div>
</body>
</html>
```
