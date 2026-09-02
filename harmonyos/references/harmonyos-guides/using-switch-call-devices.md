---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-switch-call-devices
title: 使用组件切换通话设备
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 分布式媒体会话 > 使用组件切换通话设备
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:574d6c724d0f82c99e3da08ed72a9f11758564ae5db01137d1fd1b845e1cbe80
---

## 切换通话输出设备

本文主要介绍AVCastPicker组件接入，实现通话设备切换功能。相关参数可参考[@ohos.multimedia.avCastPicker (投播组件)](../harmonyos-references/ohos-multimedia-avcastpicker.md)和[@ohos.multimedia.avCastPickerParam (投播组件参数)](../harmonyos-references/js-apis-avcastpickerparam.md)。如果希望实现音频输出设备路由切换的效果，请参考[实现音频输出设备路由切换](audio-output-device-switcher.md)。

当前系统支持两种组件样式的显示方式：默认样式显示和自定义样式显示。

* 如果应用选择显示默认样式，当设备切换时，系统将根据当前选择的设备显示系统默认的组件样式。
* 如果应用选择显示自定义样式，那么需要应用根据设备的变化刷新自己定义的样式。

### 默认样式实现

1. 创建voice\_call类型的AVSession。AVSession在创建方法中支持不同的类型参数，由AVSessionType定义。voice\_call表示通话类型，如果不创建，将显示空列表。

   ```typescript
   import { AVCastPicker, AVCastPickerState, AVInputCastPicker, avSession } from '@kit.AVSessionKit';

   @Entry
   @Component
   struct Index {
     @State message: string = '模拟通话';
     @State session: avSession.AVSession | undefined = undefined;
     @State context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     // ...

     async init() {
       try {
         let context = this.getUIContext().getHostContext() as Context;
         // 通话开始时创建voice_call类型的avsession。
         this.session = await avSession.createAVSession(context, 'SESSION_NAME', 'voice_call');
       } catch (err) {
         console.error(`AVSession create :  Error: Code: ${err.code}, message: ${err.message}`);
       }
       // ...
     }
     // ...
   }
   ```
2. 在需要切换设备的通话界面创建AVCastPicker组件。

   ```typescript
   import { AVCastPicker } from '@kit.AVSessionKit';

   @Entry
   @Component
   struct OutputCastPicker {
     @State normalColor:Color = Color.White;
     @State activeColor:Color = Color.Blue;
     @State pickerImage: ResourceStr = $r('app.media.sound'); // 自定义资源。
     // ...
     // 创建组件，并设置大小。
     build() {
       Row() {
         Column() {
           AVCastPicker({
             normalColor: this.normalColor,
             activeColor: this.activeColor,
           })
             .size({ width: '50%', height: '20%' })
             .id('AVCastPicker')
           // ...
         }
         .width('100%')
         .alignItems(HorizontalAlign.Center)
       }
       .alignItems(VerticalAlign.Center)
       .width('100%')
       .height('100%')
     }
   }
   ```

   或者创建AVCastPickerHelper组件。

   ```typescript
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { avSession } from '@kit.AVSessionKit';

   class MyPage {
     private avCastPicker: avSession.AVCastPickerHelper;

     constructor(context: common.UIAbilityContext) {
       this.avCastPicker = new avSession.AVCastPickerHelper(context);
     }

     async selectCastDevice() {
       const avCastPickerOptions: avSession.AVCastPickerOptions = {
         sessionType: 'video',
       };

       this.avCastPicker.select(avCastPickerOptions).then(() => {
         console.info('select successfully');
       }).catch((err: BusinessError) => {
         console.error('AVCastPicker.select failed with err: ${err.code}, ${err.message}');
       });
     }
   }
   ```
3. 创建VOICE\_COMMUNICATION类型的AudioRenderer，并开始播放。具体通话音频播放等实现，请参考[开发音频通话功能](audio-call-development.md)。

   ```typescript
   import { audio } from '@kit.AudioKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { resourceManager } from '@kit.LocalizationKit';
   import { fileIo } from '@kit.CoreFileKit';

   class Options {
     public offset: number = 0;
     public length: number = 0;
   }
   export default class AudioRenderer {
     private audioRenderer: audio.AudioRenderer | undefined = undefined;
     private audioStreamInfo: audio.AudioStreamInfo = {
       // 请按照实际场景设置，当前参数仅参考。
       samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
       channels: audio.AudioChannel.CHANNEL_2, // 通道。
       sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
       encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
     }
     public appContext?: common.UIAbilityContext | undefined = undefined;
     private audioSource = 'test1.wav';
     private fileDescriptor?: resourceManager.RawFileDescriptor | undefined = undefined;
     // ...
     async getStageFileDescriptor(fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
       let fileDescriptor: resourceManager.RawFileDescriptor | undefined = undefined;
       if (this.appContext) {
         let mgr = this.appContext.resourceManager;
         this.fileDescriptor = mgr.getRawFdSync(fileName);
         await mgr.getRawFd(fileName).then(value => {
           fileDescriptor = value;
           console.info('case getRawFileDescriptor success fileName: ' + fileName);
         }).catch((error: BusinessError) => {
           console.error('case getRawFileDescriptor err: ' + error);
         });
       }
       return fileDescriptor;
     }

     async startRenderer(): Promise<void> {
       if (this.audioRenderer !== undefined) {
         return;
       }
       await this.getStageFileDescriptor(this.audioSource).then((res) => {
         this.fileDescriptor = res;
       });
       if (!this.fileDescriptor) {
         return;
       }
       let file: resourceManager.RawFileDescriptor = this.fileDescriptor;
       try {
         this.audioRenderer = await audio.createAudioRenderer(this.audioRendererOption);
       } catch (error) {
         console.error(`audioRenderer create : Error: ${JSON.stringify(error)}`);
         return;
       }
       let bufferSize: number = this.fileDescriptor.offset;
       let writeDataCallback = (buffer: ArrayBuffer) => {
         let options: Options = {
           offset: bufferSize,
           length: buffer.byteLength
         }
         fileIo.readSync(file.fd, buffer, options);
         bufferSize += buffer.byteLength;
       };
       this.audioRenderer.on('writeData', writeDataCallback);
       await this.audioRenderer.start();
     }

     async stopRenderer(): Promise<void> {
       if (this.audioRenderer) {
         await this.audioRenderer.release();
         this.audioRenderer = undefined;
       }
       if (this.fileDescriptor) {
         this.closeResource(this.audioSource);
         this.fileDescriptor = undefined;
       }
     }

     async closeResource(fileName: string): Promise<void> {
       if (this.appContext) {
         let mgr = this.appContext.resourceManager;
         await mgr.closeRawFd(fileName).then(() => {
           console.info('case closeRawFd success fileName: ' + fileName);
         }).catch((error: BusinessError) => {
           console.error('case closeRawFd err: ' + error);
         });
       }
     }
   }
   ```
4. （可选）如果应用想知道设备切换情况，可以监听当前发声设备切换回调。

   ```typescript
   import { audio } from '@kit.AudioKit';
   // ...
   export default class AudioRenderer {
     // ...
     private audioManager: audio.AudioManager | undefined = undefined;
     private audioRoutingManager: audio.AudioRoutingManager | undefined = undefined;
     private audioRendererInfo: audio.AudioRendererInfo = {
       // 需使用通话场景相应的参数。
       usage: audio.StreamUsage.STREAM_USAGE_VIDEO_COMMUNICATION, // 音频流使用类型：VOIP视频通话，默认为扬声器。
       rendererFlags: 0 // 音频渲染器标志：默认为0即可。
     }
     private  audioRendererOption: audio.AudioRendererOptions = {
       streamInfo: this.audioStreamInfo,
       rendererInfo: this.audioRendererInfo
     };

     async observerDevices() {
       this.audioManager = audio.getAudioManager(); // 先创建audiomanager。
       if (!this.audioManager) {
         console.error('get audioManager failed');
         return;
       }
       // 再调用AudioManager的方法创建AudioRoutingManager实例。
       this.audioRoutingManager = this.audioManager.getRoutingManager();
       if(!this.audioRoutingManager) {
         return;
       }
       // 可选监听当前发声设备切换回调。
       this.audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo, (desc: audio.AudioDeviceDescriptors) => {
         console.info(`device change to: ${desc[0].deviceType}`); // 设备类型。
       });
     }
     // ...
   }
   ```
5. 通话结束后，销毁会话。

   ```typescript
   // 通话结束销毁第一步创建的session。
   this.session?.destroy((err) => {
     if (err) {
       console.error(`Failed to destroy session. Code: ${err.code}, message: ${err.message}`);
     } else {
       console.info(`Destroy : SUCCESS `);
     }
   });
   ```

### 自定义样式实现

自定义样式通过设置[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)类型的参数[customPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)实现。

实现自定义样式的步骤与实现默认样式基本相同，开发者可参考[默认样式实现](using-switch-call-devices.md#默认样式实现)，完成创建AVSession、实现音频播放等步骤。

存在差异的步骤如下所示。

1. 创建自定义AVCastPicker，需要新增自定义参数（对应默认样式实现步骤2）。

   ```typescript
   import { AVCastPicker } from '@kit.AVSessionKit';
   // ...

   @Entry
   @Component
   struct SelfCastPicker {
     @State pickerImage: ResourceStr = $r('app.media.earpiece'); // 自定义资源。
     // ...
     build() {
       Row() {
         Column() {
           AVCastPicker(
             {
               customPicker: (): void => this.ImageBuilder() // 新增自定义参数。
             }
           ).size({ height: 45, width: 45 })
         }
       }
     }

     // 自定义内容。
     @Builder
     ImageBuilder() {
       Image(this.pickerImage)
         .size({ width: '100%', height: '100%' })
         .backgroundColor('#00000000')
         .fillColor(Color.Black)
     }
   }
   ```
2. 如果应用要根据发声设备变化而改变自定义样式，必须监听设备切换，然后实时刷新自定义样式（对应默认样式实现步骤4）。

   ```typescript
   import { audio } from '@kit.AudioKit';

   @Entry
   @Component
   struct SelfCastPicker {
     // ...
     async selfObserverDevices() {
       let audioManager = audio.getAudioManager();
       let audioRoutingManager = audioManager.getRoutingManager();

       // 初次拉起AVCastPicker时需获取当前设备,刷新显示。
       this.changePickerShow(audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo));

       // 监听当前发声设备切换，及时根据不同设备类型显示不同的样式。
       audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo, (desc: audio.AudioDeviceDescriptors) => {
         this.changePickerShow(audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo));
       });
     }

     // 设备更新后刷新自定义资源pickerImage。
     private changePickerShow(desc: audio.AudioDeviceDescriptors) {
       if(!desc || !desc.length || !desc[0]) {
         return;
       }
       if (desc[0].deviceType === 2) {
         this.pickerImage = $r('app.media.sound');
       } else if (desc[0].deviceType === 7) {
         this.pickerImage = $r('app.media.bluetooth');
       } else {
         this.pickerImage = $r('app.media.earpiece');
       }
     }
     // ...
   }
   ```

## 切换通话输入设备

系统不再提供音频输入设备切换的API，如果需要在应用内切换音频输入设备，可通过接入AVInputCastPicker组件来完成。相关参数可参考[@ohos.multimedia.avInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md)和[@ohos.multimedia.avCastPickerParam](../harmonyos-references/js-apis-avcastpickerparam.md)。

本文将主要介绍AVInputCastPicker组件接入，实现通话输入设备切换功能。

当前系统支持两种组件样式的显示方式：默认样式显示和自定义样式显示。

* 如果应用选择显示默认样式，当设备切换时，系统将根据当前选择的设备显示系统默认的组件样式。
* 如果应用选择显示自定义样式，那么需要应用根据设备的变化刷新自己定义的样式。

### 默认样式实现

1. 在需要切换设备的通话界面创建AVInputCastPicker组件。

   ```typescript
   import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

   // ...
     // 设备列表显示状态变化回调（可选）。
     private onStateChange(state: AVCastPickerState) {
       if (state === AVCastPickerState.STATE_APPEARING) {
         console.info('The picker starts showing.');
       } else if (state === AVCastPickerState.STATE_DISAPPEARING) {
         console.info('The picker finishes presenting.');
       }
     }

     // 创建组件，并设置大小。
     build() {
       Row() {
         Column() {
           AVInputCastPicker(
             {
               onStateChange: this.onStateChange
             }
           ).size({ height: 45, width: 45 })
         }
       }
     }
   ```
2. 实现通话功能，请参考[开发音频通话功能](audio-call-development.md)。

### 自定义样式实现

自定义样式通过设置[AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md#avinputcastpicker)中的参数customPicker实现。

1. 创建自定义AVInputCastPicker，需要新增自定义参数。

   ```typescript
   import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

   @Entry
   @Component
   struct InputCastPicker {
     @State pickerImage: ResourceStr = $r('app.media.sound'); // 自定义资源。
     // ...

     // 设备列表显示状态变化回调（可选）。
     private onStateChange(state: AVCastPickerState) {
       if (state === AVCastPickerState.STATE_APPEARING) {
         console.info('The picker starts showing.');
       } else if (state === AVCastPickerState.STATE_DISAPPEARING) {
         console.info('The picker finishes presenting.');
       }
     }

     build() {
       Row() {
         Column() {
           AVInputCastPicker(
             {
               customPicker: (): void => this.ImageBuilder(), // 新增自定义参数。
               onStateChange: this.onStateChange
             }
           )
             .size({ width: '50%', height: '20%' })
             .id('AVInputCastPicker')
           // ...
         }
         .width('100%')
         .alignItems(HorizontalAlign.Center)
       }
       .alignItems(VerticalAlign.Center)
       .width('100%')
       .height('100%')
     }

     // 自定义内容。
     @Builder
     ImageBuilder() {
       Text($r('app.string.switch_InputDevice'))
       Image(this.pickerImage)
         .size({ width: '100%', height: '100%' })
         .backgroundColor('#00000000')
         .fillColor(Color.Black)
     }
   }
   ```
2. 实现通话功能，请参考[开发音频通话功能](audio-call-development.md)。
