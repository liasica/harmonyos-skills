---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-36
title: HarmonyOS是否可以限制拍摄的视频时长
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > HarmonyOS是否可以限制拍摄的视频时长
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:663a70102b48eaab610c4a6dac78ee2e5e88f32766423059cbb1d79eedc918b1
---

## 问题现象

业务场景：朋友圈发送视频，一般限制大小是15s。所以是否可以通过参数来控制拍摄视频的最大时长，比如30秒或者60秒等？

## 背景知识

* 系统相机开发可参考[通过系统相机拍照和录像](../harmonyos-guides/camera-picker.md)，开发者调用picker方法会直接跳转到系统相机页面，功能完备齐全。
* 自定义相机开发需要开发者自行开发相机[拍照](../harmonyos-guides/camera-shooting-case.md)与[录像](../harmonyos-guides/camera-recording-case.md)功能。

## 解决方案

* 使用[系统相机](../harmonyos-references/js-apis-camerapicker.md)时，可以通过相机配置选项[PickerProfiles](../harmonyos-references/js-apis-camerapicker.md#pickerprofile)中的videoDuration设置录制的最大时长，默认单位是秒。

  ```ts
  let pickerProfile: picker.PickerProfile = {
    cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK,
    // 录制的最大时长（单位：秒）
    videoDuration: 5
  };
  let pickerResult: picker.PickerResult = await picker.pick(context,
    [picker.PickerMediaType.PHOTO, picker.PickerMediaType.VIDEO], pickerProfile);
  ```
* 使用自定义相机[录制](../harmonyos-guides/camera-recording-case.md)视频，可以通过配置音视频参数[AVRecorderConfig](../harmonyos-references/arkts-apis-media-i.md#avrecorderconfig9)中的maxDuration设置录制的最大时长，单位为秒。

  ```ts
  let aVRecorderConfig: media.AVRecorderConfig = {
    audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
    videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
    profile: aVRecorderProfile,
    url: `fd://${file.fd.toString()}`, // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数，eg.fd://45--file:///data/media/01.mp4
    metadata: avMetadata,
    maxDuration: 5
  };
  ```
