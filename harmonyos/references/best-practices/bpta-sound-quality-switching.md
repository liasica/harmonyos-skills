---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-sound-quality-switching
title: 音质切换开发实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音质切换开发实践
category: best-practices
scraped_at: 2026-04-29T14:11:42+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:d273c56331285e5a5f4cc680a37b6202bc7d9c168633bd2da80e673cd188716d
---

## 概述

在音乐播放应用中，同一首歌曲在不同音质间的切换是一种常见功能，而音频文件的压缩方式是影响音质的关键因素之一。下表展示了不同压缩方式对应的音质对比：

| 类型 | 代表格式 | 播放能力支持 | 特点 |
| --- | --- | --- | --- |
| 未压缩 | PCM/WAV | PCM：AudioRenderer  WAV：AVPlayer | 高保真、体积大 |
| 无损压缩 | FLAC/APE | AVPlayer | 可还原原始数据 |
| 有损压缩 | MP3/AAC | AVPlayer | 体积小、音质损失 |

音质可以在未压缩、无损压缩和有损压缩之间切换，根据上述播放能力支持范围可以看出，音质切换的本质为[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)与[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)的播放切换，以及AVPlayer与AVPlayer的播放切换（即使用AVPlayer在不同音频格式间的播放切换）。

本文将介绍以下两种音质切换场景的实现：

* [AudioRenderer与AVPlayer播放切换](bpta-sound-quality-switching.md#section1718774317213)
* [AVPlayer与AVPlayer播放切换](bpta-sound-quality-switching.md#section198441182235)

## AudioRenderer与AVPlayer播放切换

### 场景描述

本场景以同一音频文件的PCM格式与MP3格式之间进行切换播放为例，切换后保持音频播放进度一致，即无缝衔接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/FY-E68G3Q8SC7l18PdBYvA/zh-cn_image_0000002490682592.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061138Z&HW-CC-Expire=86400&HW-CC-Sign=1D50692ABE229A51E7FFDF2A36911D97C06038B005A476F10B6C8659C8ECA4AE "点击放大")

### 实现原理

1. 使用AudioRenderer播放PCM文件，即MP3音质（标清）切换到无损未压缩的PCM音质时，通过跳转的时间戳计算出新的offset偏移位置，待下次读取音频数据时，从该offset偏移位置开始读取，AudioRenderer即可实现跳转至指定位置播放。
2. 使用AVPlayer播放MP3文件，即无损未压缩的PCM音质切换到MP3音质（标清）时，通过AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)接口可直接跳转到对应时间戳位置播放。

### 开发步骤

1. 在MediaTools类中，定义如下方法：
   * msToCountdownTime()：根据当前毫秒数转换为分钟格式。
   * getMsFromByteLength()：根据字节长度转化为播放时间长度。
   * getOffsetFromTime()：根据播放时间长度转化为字节长度。

   ```
   1. export class MediaTools {
   2. // ...

   4. static msToCountdownTime(ms: number): string {
   5. if (!ms) {
   6. return '00:00';
   7. }
   8. const days = Math.floor(ms / (1000 * 60 * 60 * 24));
   9. const hours = Math.floor((ms % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
   10. const minutes = Math.floor((ms % (1000 * 60 * 60)) / (1000 * 60));
   11. const seconds = Math.floor((ms % (1000 * 60)) / 1000);
   12. return `${(days ? MediaTools.fill(days) + ':' : '')}${(hours ? MediaTools.fill(hours) + ':' : '')}
   13. ${MediaTools.fill(minutes)}:${MediaTools.fill(seconds)} `.trim();
   14. }

   16. static getMsFromByteLength(byteLength: number): number {
   17. return 1000 * (byteLength / SECOND_BUFFER_WALK);
   18. }

   20. static getOffsetFromTime(curMs: number) {
   21. return (curMs / 1000) * SECOND_BUFFER_WALK;
   22. }
   23. }
   ```

   [MediaTools.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/utils/MediaTools.ets#L25-L68)
2. 在AVPlayerController类中，定义如下方法：
   * reset()：在其中调用AVPlayer实例的[reset()](../harmonyos-references/arkts-apis-media-avplayer.md#reset9)方法，重置播放。
   * pause()：在其中调用AVPlayer实例的[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9-1)方法，暂停播放。
   * seek()：在其中调用AVPlayer实例的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)，跳转播放。

   ```
   1. export class AVPlayerController {
   2. // ...

   4. reset(fd: number, offset: number, length: number): void {
   5. this.currentTime = AppStorage.get('progress') as number;
   6. this.isReset = true;
   7. this.avPlayer?.reset(() => {
   8. if (this.avPlayer != undefined) {
   9. this.avPlayer.fdSrc = { fd: fd, offset: offset, length: length };
   10. }
   11. })
   12. }
   13. // ...

   15. // Pause playback
   16. pause(): void {
   17. this.avPlayer?.pause().catch(() => {
   18. Logger.error('AVPlayerController pause error!');
   19. })
   20. }

   22. // Jump to playback
   23. seek(currentTime: number): void {
   24. this.avPlayer?.seek(currentTime, media.SeekMode.SEEK_NEXT_SYNC);
   25. }
   26. // ...
   27. }
   ```

   [AVPlayerController.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/player/AVPlayerController.ets#L22-L144)
3. 在AudioRendererController类中，定义如下方法：
   * initAudioRenderer()：初始化，获取AudioRenderer实例。
   * setWriteDataCallback()：写入音频数据。
   * start()：在其中调用AudioRenderer的[start()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法，启动音频渲染器。
   * pause()：在其中调用AudioRenderer的[pause()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#pause8)方法，暂停音频渲染。
   * seek()：自定义seek()方法保存当前播放进度、时间的转换和字节长度，用于AudioRenderer跳转播放。

   ```
   1. export class AudioRendererController {
   2. // ...
   3. // Initialization AudioRenderer
   4. public async initAudioRenderer(fd: number, offset: number, length: number): Promise<void> {
   5. this.fd = fd; // File descriptor
   6. this.offset = offset; // Start offset
   7. this.currentOffset = offset; // Current offset
   8. this.length = length; // File length
   9. // Audio stream information
   10. let audioStreamInfo: audio.AudioStreamInfo = {
   11. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Audio file sampling rate
   12. channels: audio.AudioChannel.CHANNEL_2, // Number of audio file channels
   13. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Audio sampling format
   14. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Audio encoding format
   15. };
   16. // AudioRenderer information
   17. let audioRendererInfo: audio.AudioRendererInfo = {
   18. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // Audio stream usage type
   19. rendererFlags: 0 // Audio renderer flag
   20. };
   21. // AudioRenderer options information
   22. let audioRendererOptions: audio.AudioRendererOptions = {
   23. streamInfo: audioStreamInfo,
   24. rendererInfo: audioRendererInfo
   25. };
   26. // Get audio renderer
   27. await audio.createAudioRenderer(audioRendererOptions).then((data) => {
   28. this.audioRenderer = data;
   29. if (this.audioRenderer !== undefined) {
   30. try {
   31. // Set the focus model to independent focus mode
   32. this.audioRenderer.setInterruptMode(audio.InterruptMode.INDEPENDENT_MODE);
   33. this.setWriteDataCallback(); // Write audio data
   34. } catch (error) {
   35. Logger.error('createAudioRenderer is calling.');
   36. }
   37. }
   38. });
   39. // Convert the file length to the corresponding number of milliseconds and store it in AppStorage.
   40. AppStorage.setOrCreate('progressMax', MediaTools.getMsFromByteLength(this.length));
   41. // Convert the file length to the corresponding number of milliseconds, then convert it to a timestamp and store it in AppStorage.
   42. AppStorage.setOrCreate('totalTime', MediaTools.msToCountdownTime(MediaTools.getMsFromByteLength(this.length)));
   43. }

   45. // Write audio data
   46. private setWriteDataCallback(): void {
   47. try {
   48. // Listening for audio data writing
   49. this.audioRenderer?.on('writeData', (buffer) => {
   50. if (this.currentOffset - this.offset >= this.length) {
   51. this.currentOffset = this.offset;
   52. this.seek(0);
   53. }
   54. let options: ReadOptions = {
   55. offset: this.currentOffset,
   56. length: buffer.byteLength
   57. };
   58. let bufferLength = fileIo.readSync(this.fd, buffer, options);
   59. this.currentOffset += buffer.byteLength;
   60. let processOffset = this.currentOffset - this.offset;

   62. if (this.offset + this.length <= this.currentOffset) {
   63. let view = new DataView(buffer);
   64. Logger.info('currentOffset ：' + this.currentOffset + '  endOffset:' + (this.offset + this.length) +
   65. ' bufferLength:' + bufferLength);
   66. for (let i = bufferLength - 1; i > processOffset - this.length; i--) {
   67. view.setUint8(i, 0);
   68. }
   69. }

   71. let curMs = MediaTools.getMsFromByteLength(processOffset);
   72. AppStorage.setOrCreate('progress', curMs);
   73. AppStorage.setOrCreate('currentTime', MediaTools.msToCountdownTime(curMs));
   74. })
   75. } catch (error) {
   76. Logger.error('setWriteDataCallback is failed. ' + error);
   77. }
   78. }

   81. public async start(): Promise<void> {
   82. if (this.audioRenderer !== undefined) {
   83. // Audio state
   84. let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
   85. if (stateGroup.indexOf(this.audioRenderer.state.valueOf()) === -1) {
   86. return;
   87. }
   88. // Starting the AudioRenderer
   89. this.audioRenderer.start((err: BusinessError) => {
   90. // ...
   91. });
   92. }
   93. }

   95. public pause(): void {
   96. if (this.audioRenderer !== undefined) {
   97. if (this.audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING) {
   98. return;
   99. }
   100. // Pause Audio rendering
   101. this.audioRenderer.pause((err: BusinessError) => {
   102. // ...
   103. });
   104. }
   105. }
   106. // Jump to playback
   107. public seek(ms: number): void {
   108. this.curMs = ms;
   109. AppStorage.setOrCreate('progress', this.curMs);
   110. AppStorage.setOrCreate('currentTime', MediaTools.msToCountdownTime(this.curMs));
   111. this.currentOffset = this.offset + MediaTools.getOffsetFromTime(this.curMs);
   112. }
   113. // ...
   114. }
   ```

   [AudioRendererController.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/player/AudioRendererController.ets#L22-L192)
4. 在PlayerController类中，定义如下方法：
   * changeType()：传入[RawFileDescriptor](../harmonyos-references/js-apis-resource-manager.md#rawfiledescriptor9)音频资源描述符，并通过audioType的值，判断使用AudioRenderer或AVPlayer播放音频。
   * seek()：通过判断isAVPlayer()返回值，调用AVPlayerController或AudioRendererController对应的seek()方法，用于跳转指定位置播放音频资源。
   * isAVPlayer()：用于判断是否使用AVPlayer播放音频资源。

   ```
   1. export class PlayerController {
   2. // ...
   3. // Modifying the audio format
   4. changeType(rawFileDescriptor: resourceManager.RawFileDescriptor, audioType: AudioType) {
   5. try {
   6. this.rawFileDescriptor = rawFileDescriptor;
   7. if (audioType === 1 || audioType === 2) {
   8. this.audioRendererController?.pause(); // Pause AudioRenderer playback
   9. // Reset AVPlayer playback
   10. this.avPlayerController?.reset(this.rawFileDescriptor.fd, this.rawFileDescriptor.offset,
   11. this.rawFileDescriptor.length);
   12. } else {
   13. this.avPlayerController?.pause(); // Pause AVPlayer playback
   14. if (this.audioRendererController === undefined) {
   15. this.audioRendererController = new AudioRendererController();
   16. }
   17. // Create an AudioRenderer instance and listen for audio data writing
   18. this.audioRendererController.initAudioRenderer(this.rawFileDescriptor.fd, this.rawFileDescriptor.offset,
   19. this.rawFileDescriptor.length).then(() => {
   20. this.audioRendererController?.start(); // Start AudioRenderer audio render
   21. });
   22. }
   23. this.currentType = audioType;
   24. } catch (error) {
   25. Logger.error('changeType error!');
   26. }
   27. }
   28. // ...
   29. // Determine the return value of isAVPlayer() and call the corresponding seek() method
   30. seek(currentTime: number): void {
   31. if (this.isAVPlayer()) {
   32. this.avPlayerController?.seek(currentTime);
   33. } else {
   34. this.audioRendererController?.seek(currentTime);
   35. }
   36. }
   37. // ...
   38. // Determine whether to use AVPlayer for playback
   39. isAVPlayer(): boolean {
   40. return this.currentType === 1 || this.currentType === 2;
   41. }
   42. }
   ```

   [PlayerController.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/player/PlayerController.ets#L22-L120)
5. 在页面中自定义changeType()事件，通过[getRawfd()](../harmonyos-references/js-apis-resource-manager.md#getrawfd9-1)获取resources/rawfile目录下的音频资源，将获取到的数据传入PlayerController的changeType()方法，调用playerController的seek()方法传入当前Slider进度的值，用于跳转播放。

   ```
   1. private changeType(songSrc: string, audioType: AudioType): void {
   2. let current: number = this.value;
   3. this.getUIContext().getHostContext()?.resourceManager.getRawFd(songSrc).then((rawFileDescriptor) => {
   4. this.playerController.changeType(rawFileDescriptor, audioType);
   5. this.playerController.seek(current);
   6. }).catch((error: BusinessError) => {
   7. Logger.error(`resourceManager error code ${error.code} message ${error.message}`);
   8. });
   9. }
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/components/ControlAreaComponent.ets#L220-L228)

   通过给对应MenuItem子组件添加对应点击事件，在其中调用changeType()方法传入音频资源文件路径和对应音频格式audioType，实现音频资源PCM格式与MP3格式的切换播放，即AudioRenderer与AVPlayer切换播放。

   ```
   1. Menu() {
   2. MenuItem({
   3. content: $r('app.string.standard_quality'),
   4. }).onClick(() => {
   5. if (this.index === 0) {
   6. return;
   7. }
   8. this.text = $r('app.string.standard_quality');
   9. this.index = 0;
   10. this.changeType(this.songData.src + AudioName.MP3, AudioType.MP3);
   11. this.isPlay = true;
   12. })
   13. // ...
   14. MenuItem({
   15. content: $r('app.string.pcm_high_quality'),
   16. })
   17. .onClick(() => {
   18. if (this.index === 2) {
   19. return;
   20. }
   21. this.text = $r('app.string.pcm_high_quality');
   22. this.index = 2;
   23. this.changeType(this.songData.src + AudioName.PCM, AudioType.PCM);
   24. this.isPlay = true;
   25. })
   26. }
   27. // ...
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/components/ControlAreaComponent.ets#L160-L216)

## AVPlayer与AVPlayer播放切换

### 场景描述

本场景以同一音频文件的FLAC格式与MP3格式之间进行切换播放为例，切换后保持音频播放进度一致，即无缝衔接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/i5aCz9QdT3CNMoWzDSY76w/zh-cn_image_0000002522762335.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061138Z&HW-CC-Expire=86400&HW-CC-Sign=B5B324D1521DA62B50565DB3377DBB13DA5B72E236C3954B32E073CCF9F97625 "点击放大")

### 实现原理

使用同一个AVPlayer实例播放FLAC文件和MP3文件，每次切换后对AVPlayer进行重置，重新设置音频资源url，然后通过AVPlayer的seek()接口直接跳转到对应时间戳位置播放。

### 开发步骤

1. 在MenuItem组件的点击事件中调用自定义changeType()方法，传入音频资源文件路径和对应音频格式audioType。

   ```
   1. Menu() {
   2. MenuItem({
   3. content: $r('app.string.standard_quality'),
   4. }).onClick(() => {
   5. if (this.index === 0) {
   6. return;
   7. }
   8. this.text = $r('app.string.standard_quality');
   9. this.index = 0;
   10. this.changeType(this.songData.src + AudioName.MP3, AudioType.MP3);
   11. this.isPlay = true;
   12. })
   13. MenuItem({
   14. content: $r('app.string.flac_high_quality'),
   15. })
   16. .onClick(() => {
   17. if (this.index === 1) {
   18. return;
   19. }
   20. this.text = $r('app.string.flac_high_quality');
   21. this.index = 1;
   22. this.changeType(this.songData.src + AudioName.FLAC, AudioType.FLAC);
   23. this.isPlay = true;
   24. })
   25. // ...
   26. }
   27. // ...
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/components/ControlAreaComponent.ets#L161-L215)
2. 同样的，在页面自定义changeType()事件中，通过getRawfd()获取音频资源，将获取到的数据传入PlayerController的changeType()方法，调用playerController的seek()方法传入当前Slider进度值，用于跳转播放。

   ```
   1. private changeType(songSrc: string, audioType: AudioType): void {
   2. let current: number = this.value;
   3. this.getUIContext().getHostContext()?.resourceManager.getRawFd(songSrc).then((rawFileDescriptor) => {
   4. this.playerController.changeType(rawFileDescriptor, audioType);
   5. this.playerController.seek(current);
   6. }).catch((error: BusinessError) => {
   7. Logger.error(`resourceManager error code ${error.code} message ${error.message}`);
   8. });
   9. }
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/components/ControlAreaComponent.ets#L220-L228)
3. 在PlayerController的changeType()方法中：
   1. 通过传入的audioType的值，判断音频是否为MP3或FLAC格式。
   2. 调用audioRendererController的pause()方法，暂停AudioRenderer音频渲染。
   3. 通过avPlayerController的reset()方法重置音频资源的描述符、偏移量和文件长度，实现音频资源FLAC格式与MP3格式的切换播放，即AVPlayer与AVPlayer切换播放。

   ```
   1. export class PlayerController {
   2. // ...
   3. // Modifying the audio format
   4. changeType(rawFileDescriptor: resourceManager.RawFileDescriptor, audioType: AudioType) {
   5. try {
   6. this.rawFileDescriptor = rawFileDescriptor;
   7. if (audioType === 1 || audioType === 2) {
   8. this.audioRendererController?.pause(); // Pause AudioRenderer playback
   9. // Reset AVPlayer playback
   10. this.avPlayerController?.reset(this.rawFileDescriptor.fd, this.rawFileDescriptor.offset,
   11. this.rawFileDescriptor.length);
   12. } else {
   13. // ...
   14. }
   15. this.currentType = audioType;
   16. } catch (error) {
   17. Logger.error('changeType error!');
   18. }
   19. }
   20. // ...
   21. // Determine the return value of isAVPlayer() and call the corresponding seek() method
   22. seek(currentTime: number): void {
   23. if (this.isAVPlayer()) {
   24. this.avPlayerController?.seek(currentTime);
   25. } else {
   26. // ...
   27. }
   28. }
   29. // ...
   30. }
   ```

   [PlayerController.ets](https://gitcode.com/harmonyos_samples/audio-format-switch/blob/master/entry/src/main/ets/player/PlayerController.ets#L23-L119)

## 示例代码

* [实现音质切换](https://gitcode.com/harmonyos_samples/audio-format-switch)
