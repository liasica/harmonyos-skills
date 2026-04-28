---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording
title: 录像(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 录像(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:57+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:e9da89bb8700cc1d305e55f86b9ce8f380894dedbfbdc0727ed415735cbf2484
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

相机应用可通过调用和控制相机设备，完成预览、拍照和录像等基础操作。

录像也是相机应用的最重要功能之一，录像是循环帧的捕获。对于录像的自定义配置，开发者可以参考[拍照](camera-shooting.md)中的步骤4，设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入media模块。

   创建录像输出流的SurfaceId以及录像输出的数据，都需要用到系统提供的media接口[@ohos.multimedia.media (媒体服务)](../harmonyos-references/arkts-apis-media.md)能力，导入media接口的方法如下。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { camera } from '@kit.CameraKit';
   3. import { media } from '@kit.MediaKit';
   ```
2. 创建Surface。

   系统提供的media接口可以创建一个录像[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)实例，通过该实例的[getInputSurface](../harmonyos-references/arkts-apis-media-avrecorder.md#getinputsurface9)方法获取SurfaceId，与录像输出流做关联，处理录像输出流输出的数据。

   ```
   1. async function getVideoSurfaceId(aVRecorderConfig: media.AVRecorderConfig): Promise<string | undefined> {  // aVRecorderConfig可参考步骤3.创建录像输出流。
   2. let avRecorder: media.AVRecorder | undefined = undefined;
   3. let videoSurfaceId: string | undefined = undefined;
   4. try {
   5. avRecorder = await media.createAVRecorder();
   6. if (avRecorder === undefined) {
   7. return videoSurfaceId;
   8. }
   9. await avRecorder.prepare(aVRecorderConfig);
   10. videoSurfaceId = await avRecorder.getInputSurface();
   11. } catch (error) {
   12. let err = error as BusinessError;
   13. console.error(`createAVRecorder call failed. error code: ${err.code}`);
   14. }
   15. return videoSurfaceId;
   16. }
   ```
3. 创建录像输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的videoProfiles属性，可获取当前设备支持的录像输出流。然后，定义创建录像的参数，通过[createVideoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createvideooutput)方法创建录像输出流。

   说明

   1.预览流与录像输出流的分辨率的宽高比要保持一致，如示例代码中宽高比为640:480 = 4:3，则需要预览流中的分辨率的宽高比也为4:3，如分辨率选择640:480，或960:720，或1440:1080，以此类推。

   2.在设置预览输出流的分辨率宽高前，需要先通过[AVRecorderProfile](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)查询视频帧支持可配置的宽高范围。

   3.获取录像旋转角度的方法：通过[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)中的[getVideoRotation](../harmonyos-references/arkts-apis-camera-videooutput.md#getvideorotation12)方法获取rotation实际的值。

   4.录像输出流帧率通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的videoProfiles属性，选择[VideoProfile](../harmonyos-references/arkts-apis-camera-i.md#videoprofile)中[frameRateRange](../harmonyos-references/arkts-apis-camera-i.md#frameraterange)满足实际业务需求的录像输出流videoProfile。

   ```
   1. async function getVideoOutput(cameraManager: camera.CameraManager, videoSurfaceId: string, cameraOutputCapability: camera.CameraOutputCapability): Promise<camera.VideoOutput | undefined> {
   2. if (!cameraManager || !videoSurfaceId || !cameraOutputCapability || !cameraOutputCapability.videoProfiles) {
   3. return;
   4. }
   5. let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCapability.videoProfiles;
   6. if (!videoProfilesArray || videoProfilesArray.length === 0) {
   7. console.error("videoProfilesArray is null or []");
   8. return undefined;
   9. }
   10. // AVRecorderProfile。
   11. let aVRecorderProfile: media.AVRecorderProfile = {
   12. fileFormat : media.ContainerFormatType.CFT_MPEG_4, // 视频文件封装格式，只支持MP4。
   13. videoBitrate : 100000, // 视频比特率。
   14. videoCodec : media.CodecMimeType.VIDEO_AVC, // 视频文件编码格式，支持avc格式。
   15. videoFrameWidth : 640,  // 视频分辨率的宽。
   16. videoFrameHeight : 480, // 视频分辨率的高。
   17. videoFrameRate : 30 // 视频帧率。
   18. };
   19. // 创建视频录制的参数，预览流与录像输出流的分辨率的宽(videoFrameWidth)高(videoFrameHeight)比要保持一致。
   20. let avMetadata: media.AVMetadata = {
   21. videoOrientation: '90' // rotation的值90，是通过getVideoRotation接口获取到的值，具体请参考说明中获取录像旋转角度的方法。
   22. }

   24. let aVRecorderConfig: media.AVRecorderConfig = {
   25. videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
   26. profile: aVRecorderProfile,
   27. url: 'fd://35', // 此处为样例示范，需要根据开发需求填写实际的路径。
   28. metadata: avMetadata
   29. };
   30. // 创建avRecorder，设置视频录制的参数。
   31. let avRecorder: media.AVRecorder | undefined = undefined;
   32. try {
   33. avRecorder = await media.createAVRecorder();
   34. if (avRecorder === undefined) {
   35. return undefined;
   36. }
   37. await avRecorder.prepare(aVRecorderConfig);
   38. } catch (error) {
   39. let err = error as BusinessError;
   40. console.error(`createAVRecorder call failed. error code: ${err.code}`);
   41. await avRecorder?.release();
   42. return;
   43. }

   45. // 创建VideoOutput对象。
   46. let videoOutput: camera.VideoOutput | undefined = undefined;
   47. // createVideoOutput传入的videoProfile对象的宽高需要和aVRecorderProfile保持一致。
   48. let videoProfile: undefined | camera.VideoProfile = videoProfilesArray.find((profile: camera.VideoProfile) => {
   49. return profile.size.width === aVRecorderProfile.videoFrameWidth && profile.size.height === aVRecorderProfile.videoFrameHeight;
   50. });
   51. if (!videoProfile) {
   52. console.error('videoProfile is not found');
   53. await avRecorder.release();
   54. return undefined;
   55. }
   56. try {
   57. videoOutput = cameraManager.createVideoOutput(videoProfile, videoSurfaceId);
   58. } catch (error) {
   59. let err = error as BusinessError;
   60. console.error('Failed to create the videoOutput instance. errorCode = ' + err.code);
   61. await avRecorder.release();
   62. }
   63. return videoOutput;
   64. }
   ```
4. 开始录像。

   说明

   * 在设置预览流帧率时，需要先通过[getActiveFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#getactiveframerate12)查询当前录像流的帧率。
   * 当录像流已设置过范围帧率时，预览流帧率必须设置与其相同的范围帧率。
   * 当录像流已设置过固定帧率时，预览流帧率要设置成录像帧率的约数，且必须也为固定帧率。

   先通过videoOutput的[start](../harmonyos-references/arkts-apis-camera-videooutput.md#start-1)方法启动录像输出流，再通过avRecorder的[start](../harmonyos-references/arkts-apis-media-avrecorder.md#start9)方法开始录像。

   ```
   1. async function startVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
   2. try {
   3. await videoOutput.start();
   4. } catch (error) {
   5. let err = error as BusinessError;
   6. console.error(`start videoOutput failed, error: ${err.code}`);
   7. }
   8. avRecorder.start(async (err: BusinessError) => {
   9. if (err) {
   10. console.error(`Failed to start the video output ${err.message}`);
   11. return;
   12. }
   13. console.info('Callback invoked to indicate the video output start success.');
   14. });
   15. }
   ```
5. 停止录像。

   先通过avRecorder的[stop](../harmonyos-references/arkts-apis-media-avrecorder.md#stop9-1)方法停止录像，再通过videoOutput的[stop](../harmonyos-references/arkts-apis-camera-videooutput.md#stop-1)方法停止录像输出流。

   ```
   1. async function stopVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
   2. avRecorder.stop((err: BusinessError) => {
   3. if (err) {
   4. console.error(`Failed to stop the video output ${err.message}`);
   5. return;
   6. }
   7. console.info('Callback invoked to indicate the video output stop success.');
   8. });
   9. await videoOutput.stop();
   10. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听录像输出流状态，包括录像开始、录像结束、录像流输出的错误。

* 通过注册固定的frameStart回调函数获取监听录像开始结果，videoOutput创建成功时即可监听，录像第一次曝光时触发，有该事件返回结果则认为录像开始。

  ```
  1. function onVideoOutputFrameStart(videoOutput: camera.VideoOutput): void {
  2. videoOutput.on('frameStart', (err: BusinessError) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info('Video frame started');
  7. });
  8. }
  ```
* 通过注册固定的frameEnd回调函数获取监听录像结束结果，videoOutput创建成功时即可监听，录像完成最后一帧时触发，有该事件返回结果则认为录像流已结束。

  ```
  1. function onVideoOutputFrameEnd(videoOutput: camera.VideoOutput): void {
  2. videoOutput.on('frameEnd', (err: BusinessError) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info('Video frame ended');
  7. });
  8. }
  ```
* 通过注册固定的error回调函数获取监听录像输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```
  1. function onVideoOutputError(videoOutput: camera.VideoOutput): void {
  2. videoOutput.on('error', (error: BusinessError) => {
  3. console.error(`Video output error code: ${error.code}`);
  4. });
  5. }
  ```

## 示例代码

* [基于CameraKit通过AVRecorder录像](https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder)
