---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-22
title: 通话类应用自动和手动切换音频输出设备问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 通话类应用自动和手动切换音频输出设备问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:22+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:848f47706721377960a8fa0e56d905c53c3373408914707e1e1391436a0ac639
---

## 问题现象

在语音消息、VoIP语音通话或VoIP视频通话场景的通话类应用场景下，应用需要实现音频输出设备切换功能。开发者可以选择通过调用setDefaultOutputDevice等API进行自动切换，也可以创建对应类型的AVSession并接入AVCastPicker，由用户手动选择音频输出设备。设备切换范围为本机设备（扬声器、听筒切换）和蓝牙/有线耳机等非投播外设的切换。

需注意不同方式的优先级关系和功能限制，灵活组合使用。

## 背景知识

* [StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)：音频流类型，当[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为语音消息、VoIP语音通话或者VoIP视频通话的场景时，可使用通话场景下的音频设备切换。
* [DeviceType](../harmonyos-references/arkts-apis-audio-e.md#devicetype)：表示设备类型的枚举。其中，本机音频输出设备一般指扬声器（EARPIECE）、听筒（SPEAKER）、默认设备类型（DEFAULT）。投播设备指设备类型[DeviceType](../harmonyos-references/arkts-apis-audio-e.md#devicetype)为REMOTE\_CAST的设备。耳机设备一般为非投播外设。
* [AVSession](../harmonyos-guides/avsession-overview.md)：AVSession Kit（Audio & Video Session Kit，音视频播控服务）是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。
* Class (AVCastPickerHelper)的[select](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14)接口：通过选择模式拉起AVCastPicker界面，用户可以选择投播设备。接口采用Promise异步返回形式，传入可选参数AVCastPickerOptions对象，无返回值。
* [AVCastPicker组件](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)：设备切换组件，该组件为自定义组件，开发者在使用前需要先了解[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)。
* [AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)：用于音频输出的ArkTS/JS API，仅支持PCM格式，需要应用持续写入音频数据进行工作。应用可以在输入前添加数据预处理，如设定音频文件的采样率、位宽等，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体播放应用开发。
* setDefaultOutputDevice:使用该API可以在代码逻辑中调用，从而实现不使用AVCastPicker实现音频输出设备切换。该API自API12起在[Interface(AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)中实现，自API20起在[Interface(AudioSessionManager)](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20))中也实现。仅支持在支持听筒、扬声器和系统默认设备。

## 解决方案

**一、不使用AVCastPicker切换音频输出设备**：

参考[音频设备路由管理](../harmonyos-guides/audio-device.md)，推荐使用[AVCastPicker组件](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)手动切换设备，也可使用Class (AVCastPickerHelper)的[select](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14)接口拉起AVCastPicker设备选择界面进行选择。

1. **获取所有可切换输出音频设备列表信息**：

   参考[获取输出设备信息](../harmonyos-guides/audio-output-device-management.md#获取输出设备信息)，可使用[getDevices](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9)，[getDevicesSync](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevicessync10)方法获取音频设备列表。关键参数[DeviceFlag](../harmonyos-references/arkts-apis-audio-e.md#deviceflag)是音频设备类型。

   或者使用[getAvailableDevices](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getavailabledevices12)获取音频可选设备列表，相比[getDevices](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9)和[getDevicesSync](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevicessync10)方法更细化，可以根据[DeviceUsage](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)按用途分类获取设备。
2. **使用setDefaultOutputDevice切换本机音频默认输出设备**：

   setDefaultOutputDevice接口的设备切换范围为本机设备（扬声器、听筒切换）。

   setDefaultOutputDevice是切换**本机**音频默认输出设备，是一个受限制的自动选择音频输出设备的接口，参考[实现音频输出设备路由切换](../harmonyos-guides/audio-output-device-switcher.md)以下为两者对比：

   **差异点**：

   * Interface(AudioRenderer)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)切换**本机**音频默认输出设备不受[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)影响；Interface(AudioSessionManager)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)切换本机音频默认输出设备优先级低于[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)的设备选择，后者使用后前者不再生效。
   * Interface(AudioRenderer)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)为流级别，优先级低于应用级别的Interface(AudioSessionManager)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)，后者使用后前者不再生效。
   * Interface(AudioSessionManager)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)，在AudioSessionManager创建后随时调用，系统会记录应用设置的默认本机内置发声设备，但只有激活AudioSession后才能生效，且需设置[AudioSessionScene](../harmonyos-references/arkts-apis-audio-e.md#audiosessionscene20)为VoIP场景。
   * Interface(AudioSessionManager)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)不限于使用AudioRenderer播放音频。

   **相同点**：

   * 两者均仅在启动播放的[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为语音消息、VoIP语音通话或VoIP视频通话时才生效。均仅支持听筒、扬声器和系统默认设备。
   * 应用启动播放时，若**外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声**，此时调用本接口会记录设置的本机内置发声设备，外设移除后生效。
3. **使用setCommunicationDevice通话场景下异步强制选择扬声器**：

   setCommunicationDevice是面向通话场景的自动设备强制选择的接口，优先级高，当前仅支持选择扬声器。

   **注意**，[setCommunicationDevice](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#setcommunicationdevice9)接口由于功能设计变化，将在后续版本废弃，**不建议开发者使用**。推荐使用AVSession提供的[设备切换组件](../harmonyos-guides/using-switch-call-devices.md)，实现通话设备切换。

   其设备选择类型为通信设备类型[CommunicationDeviceType](../harmonyos-references/arkts-apis-audio-e.md#communicationdevicetype9)，是系统预置的可用于通话场景的设备，当前仅支持选择扬声器，应用可以使用[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)的[isCommunicationDeviceActive](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#iscommunicationdeviceactive9)函数获取指定通信设备的激活状态，使用[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)的[setCommunicationDevice](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#setcommunicationdevice9)设置通信设备的激活状态，通过激活设备来实现通话场景音频设备的切换。

**二、使用AVCastPicker切换音频输出设备**：

AVCastPicker切换音频输出设备范围包括本机设备（扬声器、听筒切换）和蓝牙/有线耳机等非投播外设的切换。涉及外设的音频输出设备切换建议使用AVCastPicker。

与setDefaultOutputDevice不同，通话类场景使用AVCastPicker切换音频输出设备适合的音频流类型为VoIP语音通话或VoIP视频通话，语音消息暂不支持。

使用[AVCastPicker组件](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)手动切换设备，通话类应用参考[通话设备切换组件](../harmonyos-guides/using-switch-call-devices.md)，媒体类应用参考[AVCastPicker投播组件](../harmonyos-guides/distributed-playback-guide.md)。仅用于用户手动切换设备，不提供自动强制选择设备的接口。

也可使用Class (AVCastPickerHelper)的[select](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14)接口拉起AVCastPicker设备选择界面进行手动选择。

参考示例：

index.ets：

```ts
import AudioCapabilityManager from '../viewmodel/AudioCapabilityManager';
import { PickerComponent } from '../view/PickerComponent';

@Entry
@Component
struct Index {
  @State audioCapabilityManager: AudioCapabilityManager = new AudioCapabilityManager();
  @Provide('pageInfos') pathStack: NavPathStack = new NavPathStack();

  @Builder
  pagesMap(name: string) {
    if (name === 'picker') {
      PickerComponent({
        audioCapabilityManager: $audioCapabilityManager
      })
    }
  }

  build() {
    Navigation(this.pathStack) {
      Row() {
        Column({ space: 50 }) {
          Button('自动和手动切换音频输出设备')
            .onClick(() => {
              this.pathStack.pushPathByName('picker', 0);
            })
        }
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .size({
        width: $r('app.string.full_width'),
        height: $r('app.string.full_height')
      })
    }
    .hideToolBar(true)
    .hideTitleBar(true)
    .mode(NavigationMode.Stack)
    .navDestination(this.pagesMap)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
  }
}
```

AudioCapabilityManager.ets：

```ts
import { audio } from '@kit.AudioKit';
import { fileIo } from '@kit.CoreFileKit';
import { avSession } from '@kit.AVSessionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

class Options {
  public offset: number = 0;
  public length: number = 0;
}

export default class AudioCapabilityManager {
  public pixelMap: image.PixelMap | undefined = undefined;
  public preferOutputDevice: audio.AudioDeviceDescriptors | undefined = undefined;
  public deviceDesc: audio.AudioDeviceDescriptors | undefined = undefined;
  private session: avSession.AVSession | undefined = undefined;
  public audioRenderer: audio.AudioRenderer | undefined = undefined;
  public audioManager: audio.AudioManager | undefined = undefined;
  public audioRoutingManager: audio.AudioRoutingManager | undefined = undefined;
  private audioSource: string = 'output.pcm';
  private audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_VIDEO_COMMUNICATION,
    rendererFlags: 0
  };
  private audioStreamInfo: audio.AudioStreamInfo = {
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
    channels: audio.AudioChannel.CHANNEL_2,
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
  };
  private audioRendererOption: audio.AudioRendererOptions = {
    streamInfo: this.audioStreamInfo,
    rendererInfo: this.audioRendererInfo
  };
  private appContext: UIContext;
  private file: resourceManager.RawFileDescriptor;
  private bufferSize: number;
  private writeDataCallback = (buffer: ArrayBuffer) => {
    let curLength = buffer.byteLength;
    if (this.bufferSize >= this.file.length + this.file.offset) {
      this.bufferSize = this.file.offset;
    } else if (this.bufferSize + buffer.byteLength > this.file.length + this.file.offset) {
      curLength = this.file.length + this.file.offset - this.bufferSize;
    }
    let options: Options = {
      offset: this.bufferSize,
      length: curLength
    };
    fileIo.readSync(this.file.fd, buffer, options);
    this.bufferSize += buffer.byteLength;
  };

  constructor() {
    this.appContext = AppStorage.get('context') as UIContext;
    this.file = this.appContext.getHostContext()!.resourceManager.getRawFdSync(this.audioSource);
    this.bufferSize = this.file.offset;
  }

  async init() {
    try {
      if (!this.appContext) {
        this.appContext = AppStorage.get('context') as UIContext;
      }
      this.session = await avSession.createAVSession(this.appContext.getHostContext()!, 'VOIP', 'video_call');
      await this.session.activate();

      let calldata: avSession.AVCallState = {
        state: avSession.CallState.CALL_STATE_ACTIVE,
        muted: false
      };

      this.session.setAVCallState(calldata).then(() => {
        console.info('setAVCallState successfully');
      }).catch((err: BusinessError) => {
        console.error(`setAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
      });

      await this.initRenderer();
      await this.observerDevices();

    } catch (error) {
      console.error(`init catch error, code: ${error.code}, message: ${error.message}`);
      return;
    }
  }

  async observerDevices() {
    try {
      this.audioManager = audio.getAudioManager();
      if (!this.audioManager) {
        console.error('get audioManager failed');
        return;
      }
      this.audioRoutingManager = this.audioManager.getRoutingManager();

      this.audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo,
        (desc: audio.AudioDeviceDescriptors) => {
          if (!this.audioRoutingManager) {
            return;
          }
          this.preferOutputDevice = desc;
          console.info(`currentPreferOutputDevice is ${this.preferOutputDevice[0].deviceType}`);
        });

      this.audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG, () => {
        this.getDevices();
      });
    } catch (error) {
      console.error(`observerDevices catch error, code: ${error.code}, message: ${error.message}`);
    }
  }

  public getDevices() {
    console.info(`Succeeded in getting devices, AudioDeviceDescriptors, preferOutputDevice:${this.audioRoutingManager?.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo)[0].deviceType}`);

    this.audioRoutingManager?.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG,
      (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
        if (err) {
          console.error(`Failed to get devices. Code: ${err.code}, message: ${err.message}`);
        } else {
          this.deviceDesc = audioDeviceDescriptors;
          audioDeviceDescriptors.forEach(
            (item) => console.info(`Succeeded in getting devices, AudioDeviceDescriptors:${item.deviceType},${item.deviceRole}`)
          );
        }
      });
  }

  async cancelObserverDevices() {
    try {
      if (!this.audioRoutingManager) {
        this.audioRoutingManager = audio.getAudioManager().getRoutingManager();
      }
      this.audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo');
    } catch (error) {
      console.error(`cancelObserverDevices catch error, code: ${error.code}, message: ${error.message}`);
      return;
    }
  }

  async initRenderer() {
    if (this.audioRenderer !== undefined) {
      return;
    }
    audio.createAudioRenderer(this.audioRendererOption, (err, renderer) => {
      if (err) {
        console.error(`audioRenderer create : Error: ${JSON.stringify(err)}`);
        return;
      }

      this.audioRenderer = renderer;
      if (this.audioRenderer !== undefined) {
        this.audioRenderer.on('writeData', this.writeDataCallback);
      }
    });
  }

  async startRenderer() {
    if (!this.audioRenderer) {
      return;
    }
    await this.audioRenderer.start();
  }

  async stopRenderer() {
    if (!this.audioRenderer) {
      return;
    }
    await this.audioRenderer.stop();
  }

  async releaseRenderer(): Promise<void> {
    if (this.audioRenderer) {
      await this.audioRenderer.release();
      this.closeResource(this.audioSource);
      this.audioRenderer = undefined;
    }
  }

  async closeResource(fileName: string): Promise<void> {
    if (this.appContext) {
      let mgr = this.appContext.getHostContext()!.resourceManager;
      await mgr.closeRawFd(fileName).then(() => {
        console.info('case closeRawFd success fileName: ' + fileName);
      }).catch((error: BusinessError) => {
        console.error('case closeRawFd err: ' + error);
      });
    }
  }

  async destroySession() {
    try {
      if (this.session) {
        await this.session?.deactivate();
        await this.session?.destroy();
      }
    } catch (error) {
      console.error('case closeRawFd err: ' + error);
    }
  }
}
```

PickerComponent.ets：

```ts
import { AVCastPicker, AVCastPickerState, AVCastPickerStyle } from '@kit.AVSessionKit';
import AudioCapabilityManager from '../viewmodel/AudioCapabilityManager';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Component
export struct PickerComponent {
  private avCastPicker: avSession.AVCastPickerHelper | undefined = undefined;
  @State avCastPickerColor: Color = Color.White;
  @State callingEnable: boolean = true;
  @Link audioCapabilityManager: AudioCapabilityManager;
  public audioSessionManager: audio.AudioSessionManager = this.initAudioSessionManager();
  public audioManager: audio.AudioManager | undefined = undefined;
  @State currentDefaultOutputDevice: audio.DeviceType | undefined = undefined;
  @State isAudioSessionActivate: boolean = false;
  @State isAudioRenderSet: boolean = true;

  private initAudioSessionManager() {
    this.audioManager = audio.getAudioManager();
    this.audioSessionManager = this.audioManager.getSessionManager();
    this.activateAudioSession();
    this.onCurrentOutputDeviceChanged();
    return this.audioSessionManager;
  }

  private activateAudioSession() {
    let strategy: audio.AudioSessionStrategy = {
      concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
    };
    this.audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO_SESSION_SCENE_MEDIA);

    this.audioSessionManager.activateAudioSession(strategy).then(() => {
      console.info('activateAudioSession SUCCESS');
      this.isAudioSessionActivate = true;
    })
      .catch((err: BusinessError) => {
        console.error(`ERROR: ${err}`);
      });
  }

  private deactivateAudioSession() {
    this.audioSessionManager.deactivateAudioSession().then(() => {
      console.info('deactivateAudioSession SUCCESS');
      this.isAudioSessionActivate = false;
    }).catch((err: BusinessError) => {
      console.error(`ERROR: ${err}`);
    });
  }

  private onCurrentOutputDeviceChanged() {
    let currentOutputDeviceChangedCallback =
      (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
        this.currentDefaultOutputDevice = this.audioSessionManager.getDefaultOutputDevice();
        console.info(`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `);
      };
    this.audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
  }

  private translateDeviceType(type: audio.DeviceType): string {
    switch (type) {
      case audio.DeviceType.EARPIECE:
        return '听筒';
      case audio.DeviceType.SPEAKER:
        return '扬声器';
      case audio.DeviceType.WIRED_HEADSET:
        return '有线耳机带麦克风';
      case audio.DeviceType.WIRED_HEADPHONES:
        return '有线耳机无麦克风';
      case audio.DeviceType.BLUETOOTH_SCO:
        return '蓝牙设备SCO连接';
      case audio.DeviceType.BLUETOOTH_A2DP:
        return '蓝牙设备A2DP连接';
      case audio.DeviceType.USB_HEADSET:
        return 'USB耳机带麦克风';
      case audio.DeviceType.DEFAULT:
        return '默认设备类型';
      default:
        return '未知设备';
    }
  }

  async selectCastDevice() {
    let context = this.getUIContext().getHostContext();

    this.avCastPicker = new avSession.AVCastPickerHelper(context!);

    const avCastPickerOptions: avSession.AVCastPickerOptions = {
      sessionType: 'voice_call',
    };

    this.avCastPicker.select(avCastPickerOptions).then(() => {
      console.info('select successfully');
    }).catch((err: BusinessError) => {
      console.error(`AVCastPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  }

  build() {
    NavDestination() {
      Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.SpaceBetween }) {
        this.getDevices();
        this.devicesList();
        this.bottomAVCastPicker();
      }
      .width('100%')
      .height('100%')
    }
    .size({
      width: $r('app.string.full_width'),
      height: $r('app.string.full_height')
    })
    .onWillAppear(async () => {
      await this.audioCapabilityManager.init();
      this.audioCapabilityManager.getDevices();
      this.isAudioSessionActivate = this.audioSessionManager.isAudioSessionActivated();
      this.audioSessionManager.on('audioSessionDeactivated', () => {
        this.isAudioSessionActivate = false;
      });
    })
    .onWillDisappear(async () => {
      await this.audioCapabilityManager.stopRenderer();
      this.callingEnable = true;

      this.audioCapabilityManager.cancelObserverDevices();
      await this.audioCapabilityManager.destroySession();
      this.audioSessionManager.off('audioSessionDeactivated');
    })
    .backgroundColor($r('app.color.default_window_background'))
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
  }

  @Builder
  bottomAVCastPicker() {
    Row() {
      Button() {
        Image($r('app.media.phone_fill'))
          .size({
            width: $r('app.float.default_button_image_width'),
            height: $r('app.float.default_button_image_height')
          });
      }
      .backgroundColor(this.callingEnable ? $r('app.color.default_calling_color') :
        $r('app.color.default_cancel_color'))
      .size({
        width: $r('app.float.default_button_width'),
        height: $r('app.float.default_button_height')
      })
      .type(ButtonType.Circle)
      .margin({
        bottom: $r('app.float.default_button_margin_bottom'),
        left: $r('app.float.default_button_margin_space')
      })
      .enabled(this.callingEnable)
      .onClick(async () => {
        await this.audioCapabilityManager.audioRenderer?.setDefaultOutputDevice(audio.DeviceType.SPEAKER);
        await this.audioCapabilityManager.startRenderer();
        await this.audioCapabilityManager.observerDevices();
        this.callingEnable = false;
      });

      Button() {
        Image($r('app.media.xmark'))
          .size({
            width: $r('app.float.default_button_image_width'),
            height: $r('app.float.default_button_image_height')
          });
      }
      .backgroundColor(this.callingEnable ? $r('app.color.default_cancel_color') :
        $r('app.color.default_calling_color'))
      .size({
        width: $r('app.float.default_button_width'),
        height: $r('app.float.default_button_height')
      })
      .type(ButtonType.Circle)
      .margin({ bottom: $r('app.float.default_button_margin_bottom') })
      .enabled(!this.callingEnable)
      .onClick(async () => {
        await this.audioCapabilityManager.stopRenderer();
        this.callingEnable = true;
      });

      Button('Picker接口')
        .onClick(() => {
          this.selectCastDevice();
        })
        .visibility(this.callingEnable ? Visibility.Hidden : Visibility.Visible)
        .size({
          width: $r('app.float.default_button_width'),
          height: $r('app.float.default_button_height')
        })
        .type(ButtonType.Circle)
        .margin({
          bottom: $r('app.float.default_button_margin_bottom')
        })

      Button() {
        AVCastPicker({
          normalColor: this.avCastPickerColor,
          activeColor: this.avCastPickerColor,
          pickerStyle: AVCastPickerStyle.STYLE_PANEL,
          onStateChange: (state: AVCastPickerState) => {
            console.info(`change avcastpicker: ${state}`);
          }
        })
          .size({
            width: $r('app.float.default_button_AVCastPicker_width'),
            height: $r('app.float.default_button_AVCastPicker_height')
          });
      }
      .visibility(this.callingEnable ? Visibility.Hidden : Visibility.Visible)
      .size({
        width: $r('app.float.default_button_width'),
        height: $r('app.float.default_button_height')
      })
      .type(ButtonType.Circle)
      .margin({
        bottom: $r('app.float.default_button_margin_bottom'),
        right: $r('app.float.default_button_margin_space')
      })
    }
    .size({
      width: $r('app.string.full_width'),
      height: '10%'
    })
    .justifyContent(FlexAlign.SpaceBetween)
    .alignItems(VerticalAlign.Bottom)
  }

  @Builder
  devicesList() {
    Column() {

      if (this.audioCapabilityManager.preferOutputDevice) { // 获取最高优先级输出设备
        Text('preferOutputDevice' +
        this.translateDeviceType(this.audioCapabilityManager!.preferOutputDevice![0].deviceType))
      }
      Text(this.isAudioSessionActivate ? 'AudioSession已激活' : 'AudioSession已停用');
      if (!this.isAudioRenderSet) {
        Text('应用DefaultOutputDevice' +
        this.translateDeviceType(this.currentDefaultOutputDevice))
      }
      Row() {
        Button(this.isAudioRenderSet ? '使用audioRender中' : '使用audioSession中')
          .onClick(() => {
            this.isAudioRenderSet = !this.isAudioRenderSet;
          })
      }

      if (this.audioCapabilityManager?.deviceDesc &&
        this.audioCapabilityManager.deviceDesc.length > 0) {
        ForEach(this.audioCapabilityManager.deviceDesc,
          (item: audio.AudioDeviceDescriptor) => {
            Button('setDefaultOutputDevice' + this.translateDeviceType(item.deviceType))
              .onClick(() => {
                const targetDeviceManager = this.isAudioRenderSet ?
                  this.audioCapabilityManager.audioRenderer : this.audioSessionManager;

                if (item.deviceType != audio.DeviceType.EARPIECE &&
                  item.deviceType != audio.DeviceType.SPEAKER &&
                  item.deviceType != audio.DeviceType.DEFAULT) {
                  return;
                }

                targetDeviceManager?.setDefaultOutputDevice(item.deviceType)
                  .then(() => {
                    this.currentDefaultOutputDevice = this.audioSessionManager.getDefaultOutputDevice();
                    console.info(`SetDefaultOutputDevice Success! DeviceType: ${this.translateDeviceType(this.currentDefaultOutputDevice)}`);
                  })
                  .catch((err: BusinessError) => {
                    console.error(`SetDefaultOutputDevice Fail: ${err}`);
                  });
              })
              .width('90%')
              .padding(10)
              .backgroundColor(Color.Blue)
              .borderRadius(8)
              .margin({ top: 6, bottom: 6 });
          });
        Button('setDefaultOutputDevice' + this.translateDeviceType(audio.DeviceType.DEFAULT))
          .onClick(() => {
            const targetDeviceManager = this.isAudioRenderSet ?
              this.audioCapabilityManager.audioRenderer : this.audioSessionManager;
            targetDeviceManager?.setDefaultOutputDevice(audio.DeviceType.DEFAULT)
              .then(() => {
                this.currentDefaultOutputDevice = this.audioSessionManager.getDefaultOutputDevice();
                console.info(`SetDefaultOutputDevice Success! DeviceType: ${this.translateDeviceType(this.currentDefaultOutputDevice)}`);
              })
              .catch((err: BusinessError) => {
                console.error(`SetDefaultOutputDevice Fail: ${err}`);
              });
          })
          .width('90%')
          .padding(10)
          .backgroundColor(Color.Blue)
          .borderRadius(8)
          .margin({ top: 6, bottom: 6 });

      } else {
        Text('未检测到音频设备')
          .fontSize(16)
          .fontColor(Color.Gray);
      }
      Row() {
        Button(`强选扬声器`)
          .onClick(() => {
            this.audioCapabilityManager!.audioRoutingManager!
              .setCommunicationDevice(audio.CommunicationDeviceType.SPEAKER,
                true, (err: BusinessError) => {
                  if (err) {
                    console.error(`Failed to set the active status of the device. ${err}`);
                    return;
                  }
                  console.info('Callback invoked to indicate that the device is set to the active status.');
                });
          })
      }
    }
    .width('100%')
  }

  @Builder
  getDevices() {
    Column() {
      Button('获取可用音频设备')
        .onClick(async () => {
          this.audioCapabilityManager.getDevices();
        })
        .width('50%')
        .padding(8)
        .backgroundColor(Color.Blue)
        .borderRadius(8)
    }
    .alignItems(HorizontalAlign.Center) // 水平居中对齐
    .width('100%')
  }
}
```

## 常见FAQ

Q：使用AVCastPicker组件是否需要接入AVSession?

A：**建议接入AVSession**，通话类应用参考[通话设备切换组件](../harmonyos-guides/using-switch-call-devices.md)，媒体类应用参考[AVCastPicker投播组件](../harmonyos-guides/distributed-playback-guide.md)，两类场景均需创建对应类型的AVSession，并选择对应的AVSessionType，通话类应用选择'voice\_call'和'video\_call'类型，媒体类应用选择'audio'或'video'类型。

若使用Class (AVCastPickerHelper)的[select](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14)接口拉起AVCastPicker设备选择界面进行手动选择，也需创建对应类型的AVSession，且在[options](../harmonyos-references/arkts-apis-avsession-i.md#avcastpickeroptions14)参数内的sessionType与创建AVSession对应的AVSessionType相同。

若**不接入AVSession**，直接使用AVCastPicker进行设备切换，也可切换音频输出设备，但仅能切换本机音频（不区分扬声器和听筒）和非投播外设，参考[不接入AVSession使用AVCastPicker组件切换音频输出设备](../architecture-guides/avplayer_audio-0000002293630521.md)。注意，此时AVCastPicker组件需使用customPicker，否则不显示默认组件。

Q：创建'audio'或'video'类型的AVSession并接入AVCastPicker组件能不能选择听筒扬声器设备切换？

A：针对本机音频输出切换，仅[通话设备切换组件](../harmonyos-guides/using-switch-call-devices.md)，即创建'voice\_call'和'video\_call'类型的AVSession并接入AVCastPicker组件时，可以切换本机听筒、扬声器输出。创建'audio'或'video'类型的AVSession并接入AVCastPicker组件仅可选择本机音频输出，无法区分听筒、扬声器。

Q：音频文件非PCM格式，无法使用AudioRenderer播放，但又希望使用Interface(AudioRenderer)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)进行音频路由切换怎么办？

A：使用Interface(AudioSessionManager)中的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)进行音频路由切换，不受AudioRenderer播放的限制。也可以参考[音频转码转换格式](faqs-avcodec-10.md)，将原音频解码为PCM数据使用AudioRenderer播放。

**说明** 

AudioRenderer也可以播放由PCM直接封装的WAV格式文件。

## 总结

当使用AVCastPicker组件或AVCastPickerHelper的select接口进行音频输出设备切换时，会拉起设备选择列表，只可以由用户手动选择音频输出设备。

使用setDefaultOutputDevice切换本机音频默认输出设备可以允许开发者自动切换通话场景下的音频输出设备。

媒体类应用场景下无自动音频输出设备切换方法。
