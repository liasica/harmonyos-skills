---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-ripple-animation
title: 基于AudioRenderer和AudioCapturer实现音频波形动画
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于AudioRenderer和AudioCapturer实现音频波形动画
category: best-practices
scraped_at: 2026-04-28T08:20:48+08:00
doc_updated_at: 2026-04-07
content_hash: sha256:ae5b7c28283d3ab1763d762333db89c2042cdae1347096eaf2b9fcea27666e16
---

## 概述

音频波形动画是音频数据的线性波形显示，其中，水平X轴用于衡量时间，垂直Y轴用于衡量振幅，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/QCzdW9JCRyma1xf-JGC9Mw/zh-cn_image_0000002507968404.png?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=DB4C7657EBAAF09B17267657E048CA506C998C52CEA7CD6F7BF126872F12AE94 "点击放大")

由于音频波形可以清晰地显示振幅变化，因此非常适合于直观显示声音、音乐等的音量大小变化，常用于用户在录音或播放录音过程中实时展示音量大小的场景。

本文将介绍以下两种音频波形场景的实现：

* [基于AudioRenderer实现音频播放波形](bpta-audio-ripple-animation.md#section1373162254116)
* [基于AudioCapturer实现音频录制波形](bpta-audio-ripple-animation.md#section223649195014)

## 实现原理

dBFS是描述音频信号在数字系统中的幅度的单位，在波形显示中，通常使用dBFS衡量数字音频中的信号强度。其计算公式如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/QxrAqI3eR8ubaKFXMeJfxQ/zh-cn_formulaimage_0000002539808087.png?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=485721D06A98CE472274A756288C67852CA50A32164919CFB746D4B04E3C6174)

其中，A表示当前的振幅数值，即当前音频数据的位深。Amax表示振幅数值的最大值，即音频的最大位深。

在计算音频的振幅dBFS后，将振幅高度绘制到画布上，再通过动画向左移动，重复以上步骤后，即可实现音频波形动画。

## 基于AudioRenderer实现音频播放波形

### 场景描述

开发者在开发录音播放等场景时，为了体现当前播放音量的大小，需要实现音频播放波形，下面将介绍如何基于AudioRenderer实现音频播放波形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/pRC_b8yYTteLwFILpNqCHg/zh-cn_image_0000002539688123.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=ED8474A009DCB1779B849831033441B79F8121E3673659E03282EA9EA24F143D "点击放大")

### 实现原理

在基于[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)实现音频播放波形场景中，需要定时计算获取音频的dBFS。因为需要定时绘制dBFS，所以需要计算这一段时间内的平均音频位深。然后，根据平均位深计算当前的dBFS，将对应高度的线条绘制到画布上。最后，通过动画移动画布，从而实现音频播放波形。

### 开发步骤

1. 初始化AudioRenderer，在回调函数writeData()中需要计算位深的总数，便于后续计算其平均值。

   ```
   1. this.renderer.on('writeData', (buffer: ArrayBuffer) => {
   2. let lastLen: number = this.fileSize - this.readOffset;
   3. let readLen: number = lastLen >= buffer.byteLength ? buffer.byteLength : lastLen;
   4. try {
   5. fileIo.readSync(this.playFile?.fd, buffer, { offset: this.readOffset, length: readLen });
   6. } catch (error) {
   7. Logger.error(TAG, `writeData error. message:${(error as BusinessError).message}`);
   8. }

   10. this.readOffset += readLen;
   11. AppStorage.setOrCreate('RWOffset', this.readOffset);
   12. if (this.readOffset >= this.fileSize) {
   13. this.readOffset = 0;
   14. }
   15. // sum samples
   16. let samples: Int16Array = new Int16Array(buffer);
   17. for (let i = 0; i < samples.length; i++) {
   18. let val: number = samples[i] / Constants.VOLUME_MAX;
   19. this.sampleValSum += val * val;
   20. this.sampleValCnt += 1;
   21. }
   22. });
   ```

   [AudioRendererManager.ets](https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation/blob/master/entry/src/main/ets/manager/AudioRendererManager.ets#L79-L100)

   说明

   为了后续波形显示，此处在处理音频数据时，将当前获取的位深进行了平方。
2. 根据音频数据的位深计算对应的dBFS。例如，在画布移动6px后，根据这段时间的总位深sampleValSum及其采样的数量sampleValCnt计算平均位深，再根据平均位深计算这段时间的dBFS。

   ```
   1. calculateDecibel(): number {
   2. if (this.sampleValCnt === 0) {
   3. return 0;
   4. }
   5. let rms: number = this.sampleValSum / this.sampleValCnt;
   6. // calculate dBFS
   7. let dBFS: number = Math.max(Constants.MIN_DB, Math.min(0, 20 * Math.log10(rms)));
   8. this.sampleValCnt = 0;
   9. this.sampleValSum = 0;

   11. return (dBFS + Math.abs(Constants.MIN_DB)) / Math.abs(Constants.MIN_DB);
   12. }
   ```

   [AudioRendererManager.ets](https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation/blob/master/entry/src/main/ets/manager/AudioRendererManager.ets#L34-L45)
3. 将数据绘制到画布上，通过移动画布实现音频波形动效。

   ```
   1. drawOnPlay(): void {
   2. let drawCanvas = this.forwardCanvas;
   3. let xPos = this.drawXPos + this.dWidth + 2 * Constants.LINE_SPACE;
   4. if (xPos >= 2 * this.dWidth) {
   5. drawCanvas = 1 - drawCanvas;
   6. xPos = xPos % (2 * this.dWidth);
   7. }
   8. let context: CanvasRenderingContext2D = drawCanvas === 0 ? this.context0 : this.context1;
   9. let h: number = this.audioRendererMgr === undefined ? 0 :
   10. this.audioRendererMgr.calculateDecibel() * (this.dWidth / Constants.CANVAS_ASPECT_RADIO);
   11. // draw straight lines
   12. context.lineCap = 'round';
   13. context.lineWidth = 2;
   14. context.strokeStyle = 'rgba(10, 89, 247, 0.6)';
   15. context.beginPath();
   16. context.moveTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO);
   17. context.lineTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO + h);
   18. context.moveTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO);
   19. context.lineTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO - h);
   20. context.stroke();

   22. this.drawXPos += Constants.LINE_SPACE;
   23. }
   ```

   [PlayDialog.ets](https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation/blob/master/entry/src/main/ets/components/PlayDialog.ets#L144-L166)

## 基于AudioCapturer实现音频录制波形

### 场景描述

开发者在开发通讯软件的语音录制发送、音乐录制等场景时，为了体现当前录制音量的大小，需要实现音频录制波形。下面将介绍如何基于AudioCapturer实现音频录制波形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/p0CJ8SHHQi6JFudPS83Odw/zh-cn_image_0000002507968406.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002045Z&HW-CC-Expire=86400&HW-CC-Sign=5DBEBB5E574522814FA0D2BE5E7B1720FE4C6DD40F85DEA4448F67C67EB68A60 "点击放大")

### 实现原理

在基于AudioCapturer实现音频播放波形场景中，需要在readData的回调函数中获取对应的位深，再计算对应的dBFS，其他实现步骤与基于AudioRenderer实现音频播放波形类似。

### 开发步骤

1. 初始化AudioCapturer，在回调函数readData()中需要计算位深的总数，便于后续计算其平均值。

   ```
   1. this.capturer.on('readData', (buffer: ArrayBuffer) => {
   2. let options: WriteOptions = { offset: this.writeOffset, length: buffer.byteLength };
   3. fileIo.writeSync(this.recordFile?.fd, buffer, options);
   4. this.writeOffset += buffer.byteLength;
   5. AppStorage.setOrCreate('RWOffset', this.writeOffset)
   6. // sum samples
   7. let samples = new Int16Array(buffer);
   8. for (let i = 0; i < samples.length; i++) {
   9. let val = samples[i] / Constants.VOLUME_MAX;
   10. this.sampleValSum += val * val;
   11. this.sampleValCnt += 1;
   12. }
   13. });
   ```

   [AudioCapturerManager.ets](https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation/blob/master/entry/src/main/ets/manager/AudioCapturerManager.ets#L81-L93)
2. 根据音频数据的位深计算对应的dBFS。例如，在画布移动6px后，根据这段时间的总位深sampleValSum及其采样的数量sampleValCnt计算平均位深，再根据平均位深计算这段时间的dBFS。

   ```
   1. calculateDecibel(): number {
   2. if (this.sampleValCnt === 0) {
   3. return 0;
   4. }
   5. let rms: number = this.sampleValSum / this.sampleValCnt;
   6. // calculate dBFS
   7. let dBFS: number = Math.max(Constants.MIN_DB, Math.min(0, 20 * Math.log10(rms)));
   8. this.sampleValCnt = 0;
   9. this.sampleValSum = 0;

   11. return (dBFS + Math.abs(Constants.MIN_DB)) / Math.abs(Constants.MIN_DB);
   12. }
   ```

   [AudioCapturerManager.ets](https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation/blob/master/entry/src/main/ets/manager/AudioCapturerManager.ets#L39-L50)
3. 将数据绘制到画布上，通过移动画布实现音频波形动效。

   ```
   1. drawOnRecord() {
   2. let drawCanvas: number = this.forwardCanvas;
   3. let xPos: number = this.drawXPos + this.dWidth + Constants.LINE_SPACE;
   4. if (xPos >= 2 * this.dWidth) {
   5. drawCanvas = 1 - drawCanvas;
   6. xPos -= 2 * this.dWidth;
   7. }
   8. let context: CanvasRenderingContext2D = drawCanvas === 0 ? this.context0 : this.context1;
   9. let h: number = this.audioCapturerMgr.calculateDecibel() * (this.dWidth / Constants.CANVAS_ASPECT_RADIO);
   10. // draw straight lines
   11. context.lineCap = 'round';
   12. context.lineWidth = 2;
   13. context.strokeStyle = 'rgba(10, 89, 247, 0.6)';
   14. context.beginPath();
   15. context.moveTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO)
   16. context.lineTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO + h);
   17. context.moveTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO)
   18. context.lineTo(xPos, this.dWidth / Constants.CANVAS_ASPECT_RADIO - h);
   19. context.stroke();

   21. this.drawXPos += Constants.LINE_SPACE;
   22. }
   ```

   [RecordDialog.ets](https://gitcode.com/HarmonyOS_Samples/audio-ripple-animation/blob/master/entry/src/main/ets/components/RecordDialog.ets#L126-L147)

## 示例代码

* [实现音频动画](https://gitcode.com/harmonyos_samples/audio-ripple-animation)
