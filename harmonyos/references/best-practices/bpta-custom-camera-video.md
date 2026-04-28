---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-camera-video
title: 自定义相机录像
breadcrumb: 最佳实践 > 媒体 > 相机 > 自定义相机录像
category: best-practices
scraped_at: 2026-04-28T08:20:23+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:251b44de98f470916f515ccdfffcaf51a9bcfc7b8b412e5c336d3a7252718b4c
---

## 概述

本文面向于相机应用开发场景，在相机应用中实现了基础视频录制功能。内容涵盖相机设备的创建与调用、录像的启动与停止、以及输出处理的完整流程，有效满足第三方应用在不同硬件平台上对录像功能的开发需求。

## 基础录像

### 场景描述

录像功能是自定义相机应用的核心功能，提供实时预览和构图调整能力。通过点击界面上的录像按钮，用户即可开始视频录制。在录制过程中，相机应用会持续采集画面数据并将其保存为视频文件，用户可根据需要随时暂停或结束录制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/7-C2Gup5SDy-MkiYj00ZEw/zh-cn_image_0000002401601769.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002022Z&HW-CC-Expire=86400&HW-CC-Sign=39E71FDBEB0D660A7400949B5D14D378A17D4DE28C0741C2916D42A384607E6A "点击放大")

### 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/RuolIUzBSQeCMuGWVOAB-w/zh-cn_image_0000002367922004.png?HW-CC-KV=V1&HW-CC-Date=20260428T002022Z&HW-CC-Expire=86400&HW-CC-Sign=F8BEF18B356B1BF6FC92612E36A0E5B5960B31CCF508D22793BF20E6D9ACEF3D "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/jgZLgnPHS-Wo3tk9uaGnfg/zh-cn_image_0000002383780282.png?HW-CC-KV=V1&HW-CC-Date=20260428T002022Z&HW-CC-Expire=86400&HW-CC-Sign=70E83A9D481E77471323E5E445F7A66AA7E328AE2A68C12B1C29390B4A93EE7A "点击放大")

详细的API说明请参考[Camera API参考](../harmonyos-references/js-apis-camera.md)。

1. 申请相关权限

   在开发相机应用时，需要先参考[申请相机开发的权限](../harmonyos-guides/camera-preparation.md)。
2. 配置视频录制参数
   * 通过相册管理模块 PhotoAccessHelper 创建一个视频资源，以便后续写入录像文件。

     ```
     1. let options: photoAccessHelper.CreateOptions = {
     2. title: Date.now().toString()
     3. };
     4. let videoAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
     5. try {
     6. this.videoUri = await videoAccessHelper.createAsset(photoAccessHelper.PhotoType.VIDEO, 'mp4', options);
     7. this.file = fileIo.openSync(this.videoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     8. } catch (exception) {
     9. Logger.error(TAG_LOG, `createAsset failed, code is ${exception.code}, message is ${exception.message}`);
     10. }
     ```

     [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L258-L267)
   * 动态生成视频录制的配置profile。

     ```
     1. this.avProfile = {
     2. audioBitrate: 48000, // Audio bitrate (unit: bps), which affects audio quality
     3. audioChannels: 2, // Stereo two-channel recording
     4. audioCodec: media.CodecMimeType.AUDIO_AAC, // The audio encoding format is AAC
     5. audioSampleRate: 48000, // Audio sampling rate (unit: Hz), CD-quality sound
     6. fileFormat: media.ContainerFormatType.CFT_MPEG_4, // Container Format Configuration
     7. videoBitrate: 32000000, // Video bitrate (unit: bps) determines video clarity
     8. // Dynamic Selection of Video Encoding Format
     9. videoCodec: (this.qualityLevel === QualityLevel.HIGHER &&
     10. this.cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK) ?
     11. media.CodecMimeType.VIDEO_HEVC : media.CodecMimeType.VIDEO_AVC,
     12. videoFrameWidth: this.videoProfile?.size.width, // Obtain width from video configuration
     13. videoFrameHeight: this.videoProfile?.size.height, // Obtain height from video configuration
     14. videoFrameRate: this.cameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
     15. 60 : 30, // Obtain rate from video configuration
     16. };
     ```

     [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L276-L291)
   * 音视频录制参数设置，包括采集源类型、编码方式、画质配置、保存路径等，为录制的启动和后续操作提供基础配置。

     ```
     1. this.avConfig = {
     2. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_CAMCORDER,
     3. videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
     4. profile: this.avProfile,
     5. url: `fd://${this.file.fd}`,
     6. metadata: {
     7. videoOrientation: this.getCameraImageRotation().toString()
     8. }
     9. };
     ```

     [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L295-L303)

3. 获取Surface

   系统提供的media接口可以创建一个录像AVRecorder实例，通过该实例的[getInputSurface()](../harmonyos-references/arkts-apis-media-avrecorder.md#getinputsurface9-1)方法获取SurfaceId，用于后续录像输出流的关联，处理录像输出流的数据。

   ```
   1. let videoSurfaceId = await this.avRecorder.getInputSurface();
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L210-L210)

4. 创建录像输出流

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)模块中的videoProfiles属性，可获取当前设备支持的录像输出流配置，根据设备能力和目标配置，选择合适的视频配置。在当前示例中，演示了根据不同相机位置、图片质量去设置不同的分辨率和帧率，最后通过[createVideoOutput()](../harmonyos-references/arkts-apis-camera-cameramanager.md#createvideooutput)方法创建录像输出流。

   ```
   1. async createVideoOutput(cameraManager: camera.CameraManager | undefined): Promise<void> {
   2. if (!this.avRecorder || this.avRecorder.state !== AVRecorderState.PREPARED) {
   3. return;
   4. }
   5. try {
   6. let videoSurfaceId = await this.avRecorder.getInputSurface();
   7. this.output = cameraManager?.createVideoOutput(this.videoProfile, videoSurfaceId);
   8. } catch (error) {
   9. Logger.error(TAG_LOG,
   10. `Failed to create the output instance. error code: ${error.code}`);
   11. }
   12. }

   14. setVideoProfile(cameraManager: camera.CameraManager | undefined, targetProfile: camera.Profile,
   15. device: camera.CameraDevice): void {
   16. this.cameraPosition = device.cameraPosition;
   17. let cameraOutputCap: camera.CameraOutputCapability | undefined =
   18. cameraManager?.getSupportedOutputCapability(device,
   19. camera.SceneMode.NORMAL_VIDEO);
   20. let videoProfilesArray: camera.VideoProfile[] | undefined = cameraOutputCap?.videoProfiles;
   21. if (videoProfilesArray?.length) {
   22. try {
   23. const displayRatio = targetProfile.size.width / targetProfile.size.height;
   24. const profileWidth = targetProfile.size.width;
   25. const videoProfile = videoProfilesArray
   26. .sort((a, b) => Math.abs(a.size.width - profileWidth) - Math.abs(b.size.width - profileWidth))
   27. .find(pf => {
   28. const pfDisplayRatio = pf.size.width / pf.size.height;
   29. return Math.abs(pfDisplayRatio - displayRatio) <= CameraConstant.PROFILE_DIFFERENCE &&
   30. pf.format === camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP;
   31. });
   32. if (!videoProfile) {
   33. Logger.error(TAG_LOG, 'Failed to get video profile');
   34. return;
   35. }
   36. this.videoProfile = videoProfile;
   37. } catch (error) {
   38. Logger.error(TAG_LOG, `Failed to createPhotoOutput. error: ${JSON.stringify(error)}`);
   39. }
   40. }
   41. }
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L204-L247)

5. 启动录像

   先通过videoOutput的[start()](../harmonyos-references/arkts-apis-camera-videooutput.md#start-1)方法启动录像输出流，再通过avRecorder的[start()](../harmonyos-references/arkts-apis-media-avrecorder.md#start9)方法开始录像。如需实现前置摄像头录像功能，先通过[isMirrorSupported()](../harmonyos-references/arkts-apis-camera-videooutput.md#ismirrorsupported15)方法判断设备是否支持镜像功能；如果支持且当前为前置摄像头，则调用[enableMirror()](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15)方法开启镜像效果。

   ```
   1. async start(isFront: boolean): Promise<void> {
   2. try {
   3. if (this.avRecorder?.state === AVRecorderState.PREPARED) {
   4. if (this.isSupportMirror() && isFront) {
   5. this.output?.enableMirror(true);
   6. }
   7. // ...
   8. await this.output?.start();
   9. await this.avRecorder?.start();
   10. }
   11. } catch (error) {
   12. Logger.info(TAG_LOG, `Failed to start and catch error is  ${error.message}`);
   13. }
   14. }
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L112-L128)

6. 暂停录像

   先通过avRecorder的[pause()](../harmonyos-references/arkts-apis-media-avrecorder.md#pause9-1)方法暂停录像，再通过videoOutput的[stop()](../harmonyos-references/arkts-apis-camera-videooutput.md#stop-1)方法停止录像输出流。

   ```
   1. async pause(): Promise<void> {
   2. try {
   3. if (this.avRecorder?.state === AVRecorderState.STARTED) {
   4. await this.avRecorder.pause();
   5. await this.output?.stop();
   6. }
   7. } catch (error) {
   8. Logger.error(TAG_LOG, `Failed to pause and catch error is  ${error.message}`);
   9. }
   10. }
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L151-L161)
7. 恢复录像

   先通过videoOutput的[start()](../harmonyos-references/arkts-apis-camera-videooutput.md#start-1)方法启动录像输出流，再通过avRecorder的[resume()](../harmonyos-references/arkts-apis-media-avrecorder.md#resume9-1)方法恢复录像。

   ```
   1. async resume(): Promise<void> {
   2. try {
   3. if (this.avRecorder?.state === AVRecorderState.PAUSED) {
   4. await this.output?.start();
   5. await this.avRecorder.resume();
   6. }
   7. } catch (error) {
   8. Logger.error(TAG_LOG, `Failed to resume and catch error is  ${error.message}`);
   9. }
   10. }
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L165-L175)
8. 停止录像

   先通过avRecorder的[stop()](../harmonyos-references/arkts-apis-media-avrecorder.md#stop9-1)方法停止录像，再通过videoOutput的[stop()](../harmonyos-references/arkts-apis-camera-videooutput.md#stop-1)方法停止录像输出流。

   ```
   1. async stop(): Promise<void> {
   2. try {
   3. if (this.avRecorder?.state === AVRecorderState.STARTED ||
   4. this.avRecorder?.state === AVRecorderState.PAUSED) {
   5. await this.avRecorder.stop();
   6. await this.output?.stop();
   7. const thumbnail = await this.getVideoThumbnail();
   8. if (thumbnail) {
   9. this.callback(thumbnail, this.videoUri);
   10. }
   11. }
   12. } catch (error) {
   13. Logger.error(TAG_LOG, `Failed to stop and catch error is  ${error.message}`);
   14. }
   15. }
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L132-L147)
9. 释放资源

   先通过avRecorder的[release()](../harmonyos-references/arkts-apis-media-avrecorder.md#release9-1)方法释放录像资源，再通过videoOutput的[release()](../harmonyos-references/arkts-apis-camera-cameraoutput.md#release-1)方法释放输出流。

   ```
   1. async release(): Promise<void> {
   2. try {
   3. await this.avRecorder?.release();
   4. await this.output?.release();
   5. this.file && await fileIo.close(this.file.fd);
   6. } catch (exception) {
   7. Logger.error(TAG_LOG, `release failed, code is ${exception.code}, message is ${exception.message}`);
   8. }
   9. this.avRecorder?.off('stateChange');
   10. this.avRecorder = undefined;
   11. this.output = undefined;
   12. this.file = undefined;
   13. }
   ```

   [VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L179-L192)

## 视频防抖

通过session中[setVideoStabilizationMode()](../harmonyos-references/arkts-apis-camera-stabilization.md#setvideostabilizationmode11)方法可以设置视频防抖模式，详细请参见[Stabilization](../harmonyos-references/arkts-apis-camera-stabilization.md#setvideostabilizationmode11)。

```
1. setVideoStabilizationMode(session: camera.VideoSession): boolean {
2. let mode: camera.VideoStabilizationMode = camera.VideoStabilizationMode.AUTO;
3. // Check whether video stabilization is supported
4. try {
5. let isSupported: boolean = session.isVideoStabilizationModeSupported(mode);
6. if (!isSupported) {
7. Logger.info(TAG_LOG, `videoStabilizationMode: ${mode} is not support`);
8. return false;
9. }
10. Logger.info(TAG_LOG, `setVideoStabilizationMode: ${mode}`);
11. // Set video stabilization
12. session.setVideoStabilizationMode(mode);
13. let activeVideoStabilizationMode = session.getActiveVideoStabilizationMode();
14. Logger.info(TAG_LOG, `activeVideoStabilizationMode: ${activeVideoStabilizationMode}`);
15. return isSupported;
16. } catch (exception) {
17. Logger.error(TAG_LOG,
18. `setVideoStabilizationMode failed, code is ${exception.code}, message is ${exception.message}`);
19. return false;
20. }
21. }
```

[VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L412-L433)

## 设置录像旋转角度

录像的旋转角度与重力方向（即设备旋转角度）相关。调用[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)类中的[getVideoRotation()](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)可以获取到录像的旋转角度。详细请参见[适配相机旋转角度(ArkTS)](../harmonyos-guides/camera-rotation-angle-adaptation.md#录像) 。

deviceDegree：设备旋转角度。获取方式请见[计算设备旋转角度](../harmonyos-guides/camera-rotation-angle-adaptation.md#计算设备旋转角度)。

```
1. getVideoRotation(deviceDegree: number): camera.ImageRotation {
2. let videoRotation: camera.ImageRotation = this.getCameraImageRotation();
3. try {
4. if (this.output) {
5. videoRotation = this.output.getVideoRotation(deviceDegree);
6. }
7. Logger.info(TAG_LOG, `Video rotation is: ${videoRotation}`);
8. } catch (error) {
9. Logger.error(TAG_LOG, `Failed to getVideoRotation and catch error is: ${error.message}`);
10. }
11. return videoRotation;
12. }
```

[VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L364-L376)

## HDR Vivid相机录像

HDR Vivid是UWA认证的动态HDR视频标准，能够拍摄出层次更丰富、光影细节更鲜明的画面，显著提升画面质感。应用仅需接入媒体领域提供的API，即可集成HarmonyOS的HDR Vivid视频采集、转码和解码显示功能。与普通录像相比，HDR录像需要开启视频防抖，随后查询设备支持的色彩空间列表，最终通过调用[setColorSpace()](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)方法完成色彩空间设置。普通录像无需执行这些步骤。详细请参见[HDR Vivid相机录像(ArkTS)](../harmonyos-guides/camera-hdr-recording.md)。

```
1. getSupportedColorSpaces(session: camera.VideoSession): colorSpaceManager.ColorSpace[] {
2. let colorSpaces: colorSpaceManager.ColorSpace[] = [];
3. try {
4. colorSpaces = session.getSupportedColorSpaces();
5. } catch (error) {
6. Logger.error(TAG_LOG, `The getSupportedColorSpaces call failed. error code: ${error.message}`);
7. }
8. return colorSpaces;
9. }

11. setColorSpaceAfterCommitConfig(session: camera.VideoSession, isHdr: boolean): void {
12. let colorSpace: colorSpaceManager.ColorSpace =
13. isHdr ? colorSpaceManager.ColorSpace.BT2020_HLG_LIMIT : colorSpaceManager.ColorSpace.BT709_LIMIT;
14. let colorSpaces: colorSpaceManager.ColorSpace[] = this.getSupportedColorSpaces(session);
15. if (!colorSpaces.includes(colorSpace)) {
16. Logger.info(TAG_LOG, `colorSpace: ${colorSpace} is not support`);
17. return;
18. }
19. try {
20. Logger.info(TAG_LOG, `setColorSpace: ${colorSpace}`);
21. session.setColorSpace(colorSpace);
22. } catch (exception) {
23. Logger.error(TAG_LOG, `setColorSpace failed, code is ${exception.code}, message is ${exception.message}`);
24. }
25. try {
26. let activeColorSpace: colorSpaceManager.ColorSpace = session.getActiveColorSpace();
27. Logger.info(TAG_LOG, `activeColorSpace: ${activeColorSpace}`);
28. } catch (error) {
29. Logger.error(TAG_LOG, `getActiveColorSpace Faild: ${error.message}`);
30. }
31. }
```

[VideoManager.ets](https://gitcode.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets#L437-L468)

## 示例代码

* [实现自定义相机功能](https://gitcode.com/harmonyos_samples/CustomCamera)
