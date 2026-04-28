---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-switch-call-devices
title: 使用通话设备切换组件
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 分布式媒体会话 > 使用通话设备切换组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d7f0bda4cee0c992f7b62ec8c229b8ca00824a0cabf1694fe88247879d121f0f
---

## 切换通话输出设备

本文主要介绍AVCastPicker组件接入，实现通话设备切换功能。相关参数可参考[@ohos.multimedia.avCastPicker(投播组件)](../harmonyos-references/ohos-multimedia-avcastpicker.md)和[@ohos.multimedia.avCastPickerParam（投播组件参数）](../harmonyos-references/js-apis-avcastpickerparam.md)。如果希望实现音频输出设备路由切换的效果，请参考[实现音频输出设备路由切换](audio-output-device-switcher.md)。

当前系统支持两种组件样式的显示方式：默认样式显示和自定义样式显示。

* 如果应用选择显示默认样式，当设备切换时，系统将根据当前选择的设备显示系统默认的组件样式。
* 如果应用选择显示自定义样式，那么需要应用根据设备的变化刷新自己定义的样式。

### 默认样式实现

1. 创建voice\_call类型的AVSession，AVSession在构造方法中支持不同的类型参数，由AVSessionType定义，voice\_call表示通话类型，如果不创建，将显示空列表。

   ```
   1. import { AVCastPicker, AVCastPickerState, AVInputCastPicker, avSession } from '@kit.AVSessionKit';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = '模拟通话';
   7. @State session: avSession.AVSession | undefined = undefined;
   8. @State context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   9. // ...

   11. async init() {
   12. try {
   13. let context = this.getUIContext().getHostContext() as Context;
   14. // 通话开始时创建voice_call类型的avsession。
   15. this.session = await avSession.createAVSession(context, 'voiptest', 'voice_call');
   16. } catch (err) {
   17. console.error(`AVSession create :  Error: Code: ${err.code}, message: ${err.message}`);
   18. }
   19. // ...
   20. }
   21. // ...
   22. }
   ```
2. 在需要切换设备的通话界面创建AVCastPicker组件。

   ```
   1. import { AVCastPicker } from '@kit.AVSessionKit';

   3. @Entry
   4. @Component
   5. struct OutputCastPicker {
   6. @State normalColor:Color = Color.White;
   7. @State activeColor:Color = Color.Blue;
   8. @State pickerImage: ResourceStr = $r('app.media.sound'); // 自定义资源。
   9. // ...
   10. // 创建组件，并设置大小。
   11. build() {
   12. Row() {
   13. Column() {
   14. AVCastPicker({
   15. normalColor: this.normalColor,
   16. activeColor: this.activeColor,
   17. customPicker: this.ImageBuilder.bind(this), // 新增自定义参数。
   18. })
   19. .size({ width: '50%', height: '20%' })
   20. .id('AVCastPicker')
   21. // ...
   22. }
   23. .width('100%')
   24. .alignItems(HorizontalAlign.Center)
   25. }
   26. .alignItems(VerticalAlign.Center)
   27. .width('100%')
   28. .height('100%')
   29. }

   31. // 自定义内容。
   32. @Builder
   33. ImageBuilder() {
   34. Text($r('app.string.switch_OutputDevice'))
   35. Image(this.pickerImage)
   36. .size({ width: '100%', height: '100%' })
   37. .backgroundColor('#00000000')
   38. .fillColor(Color.Black)
   39. }
   40. }
   ```

   或者创建AVCastPickerHelper组件。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { avSession } from '@kit.AVSessionKit';

   5. class MyPage {
   6. private avCastPicker: avSession.AVCastPickerHelper;

   8. constructor(context: common.UIAbilityContext) {
   9. this.avCastPicker = new avSession.AVCastPickerHelper(context);
   10. }

   12. async selectCastDevice() {
   13. const avCastPickerOptions: avSession.AVCastPickerOptions = {
   14. sessionType: 'video',
   15. };

   17. this.avCastPicker.select(avCastPickerOptions).then(() => {
   18. console.info('select successfully');
   19. }).catch((err: BusinessError) => {
   20. console.error('AVCastPicker.select failed with err: ${err.code}, ${err.message}');
   21. });
   22. }
   23. }
   ```
3. 创建VOICE\_COMMUNICATION类型的AudioRenderer，并开始播放。具体通话音频播放等实现，请参考[开发音频通话功能](audio-call-development.md)。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { resourceManager } from '@kit.LocalizationKit';
   5. import { fileIo } from '@kit.CoreFileKit';

   7. class Options {
   8. public offset: number = 0;
   9. public length: number = 0;
   10. }
   11. export default class AudioRenderer {
   12. private audioRenderer: audio.AudioRenderer | undefined = undefined;
   13. private audioStreamInfo: audio.AudioStreamInfo = {
   14. // 请按照实际场景设置，当前参数仅参考。
   15. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
   16. channels: audio.AudioChannel.CHANNEL_2, // 通道。
   17. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
   18. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
   19. }
   20. public appContext?: common.UIAbilityContext | undefined = undefined;
   21. private audioSource = 'test1.wav';
   22. private fileDescriptor?: resourceManager.RawFileDescriptor | undefined = undefined;
   23. // ...
   24. async getStageFileDescriptor(fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
   25. let fileDescriptor: resourceManager.RawFileDescriptor | undefined = undefined;
   26. if (this.appContext) {
   27. let mgr = this.appContext.resourceManager;
   28. this.fileDescriptor = mgr.getRawFdSync(fileName);
   29. await mgr.getRawFd(fileName).then(value => {
   30. fileDescriptor = value;
   31. console.info('case getRawFileDescriptor success fileName: ' + fileName);
   32. }).catch((error: BusinessError) => {
   33. console.error('case getRawFileDescriptor err: ' + error);
   34. });
   35. }
   36. return fileDescriptor;
   37. }

   39. async startRenderer(): Promise<void> {
   40. if (this.audioRenderer !== undefined) {
   41. return;
   42. }
   43. this.getStageFileDescriptor(this.audioSource).then((res) => {
   44. this.fileDescriptor = res;
   45. });
   46. if (!this.fileDescriptor) {
   47. return;
   48. }
   49. let file: resourceManager.RawFileDescriptor = this.fileDescriptor;
   50. try {
   51. this.audioRenderer = await audio.createAudioRenderer(this.audioRendererOption);
   52. } catch (error) {
   53. console.error(`audioRenderer create : Error: ${JSON.stringify(error)}`);
   54. return;
   55. }
   56. let bufferSize: number = this.fileDescriptor.offset;
   57. let writeDataCallback = (buffer: ArrayBuffer) => {
   58. let options: Options = {
   59. offset: bufferSize,
   60. length: buffer.byteLength
   61. }
   62. fileIo.readSync(file.fd, buffer, options);
   63. bufferSize += buffer.byteLength;
   64. };
   65. this.audioRenderer.on('writeData', writeDataCallback);
   66. await this.audioRenderer.start();
   67. }

   69. async stopRenderer(): Promise<void> {
   70. if (this.audioRenderer) {
   71. await this.audioRenderer.release();
   72. this.audioRenderer = undefined;
   73. }
   74. if (this.fileDescriptor) {
   75. this.closeResource(this.audioSource);
   76. this.fileDescriptor = undefined;
   77. }
   78. }

   80. async closeResource(fileName: string): Promise<void> {
   81. if (this.appContext) {
   82. let mgr = this.appContext.resourceManager;
   83. await mgr.closeRawFd(fileName).then(() => {
   84. console.info('case closeRawFd success fileName: ' + fileName);
   85. }).catch((error: BusinessError) => {
   86. console.error('case closeRawFd err: ' + error);
   87. });
   88. }
   89. }
   90. }
   ```
4. （可选）如果应用想知道设备切换情况，可以监听当前发声设备切换回调。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. // ...
   3. export default class AudioRenderer {
   4. // ...
   5. private audioManager: audio.AudioManager | undefined = undefined;
   6. private audioRoutingManager: audio.AudioRoutingManager | undefined = undefined;
   7. private audioRendererInfo: audio.AudioRendererInfo = {
   8. // 需使用通话场景相应的参数。
   9. usage: audio.StreamUsage.STREAM_USAGE_VIDEO_COMMUNICATION, // 音频流使用类型：VOIP视频通话，默认为扬声器。
   10. rendererFlags: 0 // 音频渲染器标志：默认为0即可。
   11. }
   12. private  audioRendererOption: audio.AudioRendererOptions = {
   13. streamInfo: this.audioStreamInfo,
   14. rendererInfo: this.audioRendererInfo
   15. };

   17. async observerDevices() {
   18. this.audioManager = audio.getAudioManager(); // 先创建audiomanager。
   19. if (!this.audioManager) {
   20. console.error('get audioManager failed');
   21. return;
   22. }
   23. // 再调用AudioManager的方法创建AudioRoutingManager实例。
   24. this.audioRoutingManager = this.audioManager.getRoutingManager();
   25. if(!this.audioRoutingManager) {
   26. return;
   27. }
   28. // 可选监听当前发声设备切换回调。
   29. this.audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo, (desc: audio.AudioDeviceDescriptors) => {
   30. console.info(`device change to: ${desc[0].deviceType}`); // 设备类型。
   31. });
   32. }
   33. // ...
   34. }
   ```
5. 通话结束后，销毁会话。

   ```
   1. // 通话结束销毁第一步创建的session。
   2. this.session?.destroy((err) => {
   3. if (err) {
   4. console.error(`Failed to destroy session. Code: ${err.code}, message: ${err.message}`);
   5. } else {
   6. console.info(`Destroy : SUCCESS `);
   7. }
   8. });
   ```

### 自定义样式实现

自定义样式通过设置[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)类型的参数[customPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)实现。

实现自定义样式的步骤与实现默认样式基本相同，开发者可参考[默认样式实现](using-switch-call-devices.md#默认样式实现)，完成创建AVSession、实现音频播放等步骤。

存在差异的步骤如下所示。

1. 创建自定义AVCastPicker，需要新增自定义参数（对应默认样式实现步骤2）。

   ```
   1. import { AVCastPicker } from '@kit.AVSessionKit';
   2. // ...

   4. @Entry
   5. @Component
   6. struct SelfCastPicker {
   7. @State pickerImage: ResourceStr = $r('app.media.earpiece'); // 自定义资源。
   8. // ...
   9. build() {
   10. Row() {
   11. Column() {
   12. AVCastPicker(
   13. {
   14. customPicker: (): void => this.ImageBuilder() // 新增自定义参数。
   15. }
   16. ).size({ height: 45, width: 45 })
   17. }
   18. }
   19. }

   21. // 自定义内容。
   22. @Builder
   23. ImageBuilder() {
   24. Image(this.pickerImage)
   25. .size({ width: '100%', height: '100%' })
   26. .backgroundColor('#00000000')
   27. .fillColor(Color.Black)
   28. }
   29. }
   ```
2. 如果应用要根据出声设备变化而改变自定义样式，必须监听设备切换，然后实时刷新自定义样式（对应默认样式实现步骤4）。

   ```
   1. import { audio } from '@kit.AudioKit';

   3. @Entry
   4. @Component
   5. struct SelfCastPicker {
   6. // ...
   7. async selfObserverDevices() {
   8. let audioManager = audio.getAudioManager();
   9. let audioRoutingManager = audioManager.getRoutingManager();

   11. // 初次拉起AVCastPicker时需获取当前设备,刷新显示。
   12. this.changePickerShow(audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo));

   14. // 监听当前发声设备切换，及时根据不同设备类型显示不同的样式。
   15. audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo, (desc: audio.AudioDeviceDescriptors) => {
   16. this.changePickerShow(audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo));
   17. });
   18. }

   20. // 设备更新后刷新自定义资源pickerImage。
   21. private changePickerShow(desc: audio.AudioDeviceDescriptors) {
   22. if(!desc || !desc.length || !desc[0]) {
   23. return;
   24. }
   25. if (desc[0].deviceType === 2) {
   26. this.pickerImage = $r('app.media.sound');
   27. } else if (desc[0].deviceType === 7) {
   28. this.pickerImage = $r('app.media.bluetooth');
   29. } else {
   30. this.pickerImage = $r('app.media.earpiece');
   31. }
   32. }
   33. // ...
   34. }
   ```

## 切换通话输入设备（仅在PC/2in1设备可用）

系统不再提供音频输入设备切换的API，如果需要在应用内切换音频输入设备，并实现AVInputCastPicker组件，相关参数可参考[@ohos.multimedia.avInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md) 和 [@ohos.multimedia.avCastPickerParam](../harmonyos-references/js-apis-avcastpickerparam.md)。

本文将主要介绍AVInputCastPicker组件接入，实现通话输入设备切换功能。

当前系统支持两种组件样式的显示方式：默认样式显示和自定义样式显示。

* 如果应用选择显示默认样式，当设备切换时，系统将根据当前选择的设备显示系统默认的组件样式。
* 如果应用选择显示自定义样式，那么需要应用根据设备的变化刷新自己定义的样式。

### 默认实现方式

1. 在需要切换设备的通话界面创建AVInputCastPicker组件。

   ```
   1. import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

   3. // ...
   4. // 设备列表显示状态变化回调（可选）。
   5. private onStateChange(state: AVCastPickerState) {
   6. if (state === AVCastPickerState.STATE_APPEARING) {
   7. console.info('The picker starts showing.');
   8. } else if (state === AVCastPickerState.STATE_DISAPPEARING) {
   9. console.info('The picker finishes presenting.');
   10. }
   11. }

   13. // 创建组件，并设置大小。
   14. build() {
   15. Row() {
   16. Column() {
   17. AVInputCastPicker(
   18. {
   19. onStateChange: this.onStateChange
   20. }
   21. ).size({ height: 45, width: 45 })
   22. }
   23. }
   24. }
   ```
2. 实现通话功能，请参考[开发音频通话功能](audio-call-development.md)。

### 自定义实现方式

自定义样式通过设置[AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md#avinputcastpicker)中的参数customPicker实现。

1. 创建自定义AVInputCastPicker，需要新增自定义参数。

   ```
   1. import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

   3. @Entry
   4. @Component
   5. struct InputCastPicker {
   6. @State pickerImage: ResourceStr = $r('app.media.sound'); // 自定义资源。
   7. // ...

   9. // 设备列表显示状态变化回调（可选）。
   10. private onStateChange(state: AVCastPickerState) {
   11. if (state === AVCastPickerState.STATE_APPEARING) {
   12. console.info('The picker starts showing.');
   13. } else if (state === AVCastPickerState.STATE_DISAPPEARING) {
   14. console.info('The picker finishes presenting.');
   15. }
   16. }

   18. build() {
   19. Row() {
   20. Column() {
   21. AVInputCastPicker(
   22. {
   23. customPicker: this.ImageBuilder.bind(this), // 新增自定义参数。
   24. onStateChange: this.onStateChange
   25. }
   26. )
   27. .size({ width: '50%', height: '20%' })
   28. .id('AVInputCastPicker')
   29. // ...
   30. }
   31. .width('100%')
   32. .alignItems(HorizontalAlign.Center)
   33. }
   34. .alignItems(VerticalAlign.Center)
   35. .width('100%')
   36. .height('100%')
   37. }

   39. // 自定义内容。
   40. @Builder
   41. ImageBuilder() {
   42. Text($r('app.string.switch_InputDevice'))
   43. Image(this.pickerImage)
   44. .size({ width: '100%', height: '100%' })
   45. .backgroundColor('#00000000')
   46. .fillColor(Color.Black)
   47. }
   48. }
   ```
2. 实现通话功能，请参考[开发音频通话功能](audio-call-development.md)。
