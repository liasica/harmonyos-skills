---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i
title: Interfaces (其他)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c8ab28d5aed8ce5e806c82c77094bd992e1f007a3c5505f6ec86d741cf691a0e
---

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## AudioStreamInfo8+

音频流信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| samplingRate | [AudioSamplingRate](arkts-apis-audio-e.md#audiosamplingrate8) | number | 否 | 否 | 音频文件的采样率，单位为赫兹（Hz）。支持传入[AudioSamplingRate](arkts-apis-audio-e.md#audiosamplingrate8)。  从API版本26.0.0开始：  - 参数samplingRate支持number类型。  - 音频渲染扩展支持8000Hz到384000Hz范围内以10Hz为步长的采样率值。具体设备支持的采样率规格会存在差异。 |
| channels | [AudioChannel](arkts-apis-audio-e.md#audiochannel8) | 否 | 否 | 音频文件的通道数。 |
| sampleFormat | [AudioSampleFormat](arkts-apis-audio-e.md#audiosampleformat8) | 否 | 否 | 音频采样格式。 |
| encodingType | [AudioEncodingType](arkts-apis-audio-e.md#audioencodingtype8) | 否 | 否 | 音频编码格式。 |
| channelLayout11+ | [AudioChannelLayout](arkts-apis-audio-e.md#audiochannellayout11) | 否 | 是 | 音频声道布局，默认值为0x0。 |

## AudioRendererInfo8+

音频渲染器信息。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content(deprecated) | [ContentType](arkts-apis-audio-e.md#contenttypedeprecated) | 否 | 是 | 音频内容类型。  **系统能力：** SystemCapability.Multimedia.Audio.Core  API version 8、9为必填参数，从API version 10开始为可选参数，默认值为CONTENT\_TYPE\_UNKNOWN。  从API version 8开始支持，从API version 10开始废弃，建议使用usage替代。 |
| usage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 否 | 否 | 音频流使用类型。  **系统能力：** SystemCapability.Multimedia.Audio.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| rendererFlags | number | 否 | 否 | 播放流行为标志。  设置为0即可。  **系统能力：** SystemCapability.Multimedia.Audio.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| volumeMode19+ | [AudioVolumeMode](arkts-apis-audio-e.md#audiovolumemode19) | 否 | 是 | 音频的音量模式。默认值为SYSTEM\_GLOBAL。  **系统能力：** SystemCapability.Multimedia.Audio.Volume |

## AudioRendererOptions8+

音频渲染器选项信息。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8) | 否 | 否 | 音频流信息。  **系统能力：** SystemCapability.Multimedia.Audio.Renderer |
| rendererInfo | [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 否 | 否 | 音频渲染器信息。  **系统能力：** SystemCapability.Multimedia.Audio.Renderer |
| privacyType10+ | [AudioPrivacyType](arkts-apis-audio-e.md#audioprivacytype10) | 否 | 是 | 表示音频流是否可以被其他应用录制，默认值为0。  **系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture |

## InterruptEvent9+

音频中断时，应用接收的中断事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventType | [InterruptType](arkts-apis-audio-e.md#interrupttype) | 否 | 否 | 音频中断事件类型，开始或是结束。 |
| forceType | [InterruptForceType](arkts-apis-audio-e.md#interruptforcetype9) | 否 | 否 | 操作是由系统强制执行或是由应用程序执行。 |
| hintType | [InterruptHint](arkts-apis-audio-e.md#interrupthint) | 否 | 否 | 中断提示，用于提供中断事件的相关信息。 |

## DeviceBlockStatusInfo13+

描述音频设备被堵塞状态和设备信息。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| blockStatus | [DeviceBlockStatus](arkts-apis-audio-e.md#deviceblockstatus13) | 否 | 否 | 音频设备堵塞状态。 |
| devices | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 否 | 设备信息。 |

## AudioSessionStrategy12+

音频会话策略。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| concurrencyMode | [AudioConcurrencyMode](arkts-apis-audio-e.md#audioconcurrencymode12) | 否 | 否 | 音频并发模式。 |

## AudioSessionDeactivatedEvent12+

音频会话停用事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reason | [AudioSessionDeactivatedReason](arkts-apis-audio-e.md#audiosessiondeactivatedreason12) | 否 | 否 | 音频会话停用原因。 |

## AudioSessionStateChangedEvent20+

音频会话状态变更事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stateChangeHint | [AudioSessionStateChangeHint](arkts-apis-audio-e.md#audiosessionstatechangehint20) | 否 | 否 | 音频会话状态变更提示。 |

## AudioRendererChangeInfo9+

描述音频渲染器更改信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamId | number | 是 | 否 | 音频流唯一ID。 |
| rendererInfo | [AudioRendererInfo](arkts-apis-audio-i.md#audiorendererinfo8) | 是 | 否 | 音频渲染器信息。 |
| deviceDescriptors | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 是 | 否 | 音频设备描述。 |

## AudioCapturerChangeInfo9+

描述音频采集器更改信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamId | number | 是 | 否 | 音频流唯一ID。 |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 是 | 否 | 音频采集器信息。 |
| deviceDescriptors | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 是 | 否 | 音频设备信息。 |
| muted11+ | boolean | 是 | 是 | 音频采集器是否处于静音状态。true表示静音，false表示非静音。 |

## AudioDeviceDescriptor

描述音频设备。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceRole | [DeviceRole](arkts-apis-audio-e.md#devicerole) | 是 | 否 | 设备角色。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| deviceType | [DeviceType](arkts-apis-audio-e.md#devicetype) | 是 | 否 | 设备类型。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| id9+ | number | 是 | 否 | 唯一的设备ID。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| name9+ | string | 是 | 否 | 设备名称。  如果是蓝牙设备，需要申请权限ohos.permission.USE\_BLUETOOTH。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| address9+ | string | 是 | 否 | 设备静态MAC地址。  如果是蓝牙设备，需要申请权限ohos.permission.USE\_BLUETOOTH。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sampleRates9+ | Array<number> | 是 | 否 | 支持的采样率。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| channelCounts9+ | Array<number> | 是 | 否 | 支持的通道数。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| channelMasks9+ | Array<number> | 是 | 否 | 支持的通道掩码。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| displayName10+ | string | 是 | 否 | 设备显示名。  **系统能力：** SystemCapability.Multimedia.Audio.Device  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| encodingTypes11+ | Array<[AudioEncodingType](arkts-apis-audio-e.md#audioencodingtype8)> | 是 | 是 | 支持的编码类型。  **系统能力：** SystemCapability.Multimedia.Audio.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| spatializationSupported18+ | boolean | 是 | 是 | 设备是否支持空间音频。true表示支持空间音频，false表示不支持空间音频。  **系统能力：** SystemCapability.Multimedia.Audio.Spatialization |
| model22+ | string | 是 | 是 | 设备的具体型号类别。  **系统能力：** SystemCapability.Multimedia.Audio.Device |
| capabilities22+ | Array<[AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8)> | 是 | 是 | 设备支持的音频流能力。  **系统能力：** SystemCapability.Multimedia.Audio.Device |

## AudioDevicePair

描述返听使用的音频设备对，包含输入设备和输出设备。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](arkts-apis-audio-i.md#audiodevicedescriptor) | 否 | 否 | 输入音频设备描述。 |
| outputDevice | [AudioDeviceDescriptor](arkts-apis-audio-i.md#audiodevicedescriptor) | 否 | 否 | 输出音频设备描述。 |

## VolumeEvent9+

音量改变时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-apis-audio-e.md#audiovolumetype) | 否 | 否 | 音频音量类型。 |
| volume | number | 否 | 否 | 音量等级，可设置范围通过调用getMinVolume和getMaxVolume方法获取。 |
| updateUi | boolean | 否 | 否 | 标识是否会显示系统本身的音量条，true表示会显示系统音量条，false表示不会显示系统音量条。  若应用内含自定义音量条，建议根据此参数动态控制其显示：当updateUi为true时不显示自定义音量条，为false时显示自定义音量条，从而避免出现系统本身音量条与应用自定义音量条同时显示或不显示的问题。 |
| volumeMode19+ | [AudioVolumeMode](arkts-apis-audio-e.md#audiovolumemode19) | 否 | 是 | 音频的音量模式。默认值为SYSTEM\_GLOBAL。 |

## MicStateChangeEvent9+

麦克风状态变化时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mute | boolean | 否 | 否 | 系统麦克风是否为静音状态。true表示静音，false表示非静音。 |

## StreamVolumeEvent20+

音频流音量变化时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 否 | 否 | 音量发生变化的音频流。 |
| volume | number | 否 | 否 | 音量值。 |
| updateUi | boolean | 否 | 否 | 标识是否会显示系统本身的音量条，true表示会显示系统音量条，false表示不会显示系统音量条。  若应用内含自定义音量条，建议根据此参数动态控制其显示：当updateUi为true时不显示自定义音量条，为false时显示自定义音量条，从而避免出现系统本身音量条与应用自定义音量条同时显示或不显示的问题。 |
| previousVolume23+ | number | 否 | 是 | 变化前的音量值。 |

## DeviceChangeAction

描述设备连接状态变化和设备信息。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [DeviceChangeType](arkts-apis-audio-e.md#devicechangetype) | 否 | 否 | 设备连接状态变化。 |
| deviceDescriptors | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 否 | 设备信息。 |

## AudioStreamDeviceChangeInfo11+

流设备变更时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| devices | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 否 | 设备信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| changeReason | [AudioStreamDeviceChangeReason](arkts-apis-audio-e.md#audiostreamdevicechangereason11) | 否 | 否 | 流设备变更原因。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| preDevices | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 是 | 应用流设备变更前的设备信息。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## CurrentOutputDeviceChangedEvent20+

应用接收到输出设备的变更事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| devices | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 否 | 设备信息。 |
| changeReason | [AudioStreamDeviceChangeReason](arkts-apis-audio-e.md#audiostreamdevicechangereason11) | 否 | 否 | 设备变更原因。 |
| recommendedAction | [OutputDeviceChangeRecommendedAction](arkts-apis-audio-e.md#outputdevicechangerecommendedaction20) | 否 | 否 | 设备变更后推荐的操作。 |
| preDevices | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 是 | 应用输出设备变更前的设备信息。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |

## CurrentInputDeviceChangedEvent21+

应用接收到输入设备的变更事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| devices | [AudioDeviceDescriptors](arkts-apis-audio-t.md#audiodevicedescriptors) | 否 | 否 | 设备信息。 |
| changeReason | [AudioStreamDeviceChangeReason](arkts-apis-audio-e.md#audiostreamdevicechangereason11) | 否 | 否 | 设备变更原因。 |

## AudioTimestampInfo19+

音频流时间戳和当前数据帧位置信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| framePos | number | 是 | 否 | 当前播放或者录制的数据帧位置。 |
| timestamp | number | 是 | 否 | 播放或者录制到当前数据帧位置时对应的时间戳，单位为纳秒。 |

## AudioCapturerInfo8+

描述音频采集器信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| source | [SourceType](arkts-apis-audio-e.md#sourcetype8) | 否 | 否 | 音源类型。 |
| capturerFlags | number | 否 | 否 | 录制流行为标志。  设置为0即可。 |

## AudioCapturerOptions8+

音频采集器选项信息。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamInfo | [AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8) | 否 | 否 | 音频流信息。  **系统能力：** SystemCapability.Multimedia.Audio.Capturer |
| capturerInfo | [AudioCapturerInfo](arkts-apis-audio-i.md#audiocapturerinfo8) | 否 | 否 | 音频采集器信息。  **系统能力：** SystemCapability.Multimedia.Audio.Capturer |
| playbackCaptureConfig(deprecated) | [AudioPlaybackCaptureConfig](arkts-apis-audio-i.md#audioplaybackcaptureconfigdeprecated) | 否 | 是 | 音频内录的配置信息。  **系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture  从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](capi-avscreencapture.md)替代。 |
| playbackCaptureMode | [AudioPlaybackCaptureMode](arkts-apis-audio-e.md#audioplaybackcapturemode) | 否 | 是 | 内录模式。可设置为AudioPlaybackCaptureMode中的枚举值或其按位或组合，当前仅支持MODE\_DEFAULT（0x0）、MODE\_MEDIA（0x1）、MODE\_EXCLUDING\_SELF（0x8000），以及MODE\_MEDIA和MODE\_EXCLUDING\_SELF的按位或组合（0x8001）。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture |

## AudioInterrupt(deprecated)

音频监听事件传入的参数。

**说明** 

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-apis-audio-e.md#streamusage) | 否 | 否 | 音频流使用类型。 |
| contentType | [ContentType](arkts-apis-audio-e.md#contenttypedeprecated) | 否 | 否 | 音频打断媒体类型。 |
| pauseWhenDucked | boolean | 否 | 否 | 音频打断时是否可以暂停音频播放。true表示音频播放可以在音频打断期间暂停，false表示音频播放不可以在音频打断期间暂停。 |

## CaptureFilterOptions(deprecated)

待录制的播放音频流的筛选信息。

**说明** 

从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](capi-avscreencapture.md)替代。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| usages | Array<[StreamUsage](arkts-apis-audio-e.md#streamusage)> | 否 | 否 | 指定需要录制的音频播放流的StreamUsage类型。可同时指定0个或多个StreamUsage。Array为空时，默认录制StreamUsage为STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_MOVIE、STREAM\_USAGE\_GAME和STREAM\_USAGE\_AUDIOBOOK的音频播放流。  在API version 10时，CaptureFilterOptions支持使用StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION，使用时需要申请权限ohos.permission.CAPTURE\_VOICE\_DOWNLINK\_AUDIO，该权限仅系统应用可申请。  从API version 11开始，CaptureFilterOptions不再支持使用StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION，所以当前接口不再涉及此权限。 |

## AudioPlaybackCaptureConfig(deprecated)

音频内录的配置信息。

**说明** 

从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](capi-avscreencapture.md)替代。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterOptions | [CaptureFilterOptions](arkts-apis-audio-i.md#capturefilteroptionsdeprecated) | 否 | 否 | 需要录制的播放音频流的筛选信息。 |

## InterruptAction(deprecated)

音频打断/获取焦点事件的回调方法。

**说明** 

从API version 7开始支持，从API version 9开始废弃，建议使用[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actionType | [InterruptActionType](arkts-apis-audio-e.md#interruptactiontypedeprecated) | 否 | 否 | 事件返回类型。TYPE\_ACTIVATED为焦点触发事件，TYPE\_INTERRUPT为音频打断事件。 |
| type | [InterruptType](arkts-apis-audio-e.md#interrupttype) | 否 | 是 | 打断事件类型。 |
| hint | [InterruptHint](arkts-apis-audio-e.md#interrupthint) | 否 | 是 | 打断事件提示。 |
| activated | boolean | 否 | 是 | 焦点获取/释放是否成功。true表示焦点获取/释放成功，false表示焦点获取/释放失败。 |

## SystemRecordControllerConfig

系统录音控制面板的配置信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sourceType | [SourceType](arkts-apis-audio-e.md#sourcetype8) | 否 | 否 | 应用期望使用的音频源类型。系统会根据该参数确定应用的录音场景，并为用户提供匹配的降噪模式选择能力。支持的音频源类型包括SOURCE\_TYPE\_MIC、SOURCE\_TYPE\_CAMCORDER和SOURCE\_TYPE\_LIVE。 |
