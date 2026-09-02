---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-51
title: 使用部分视频配置信息项录制视频文件损坏
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 使用部分视频配置信息项录制视频文件损坏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d44bac2c30ed9c2bb0a8a72d55aec396b9154a060dc653102f8b1bce2bee4753
---

## 问题现象

在进行自定义相机开发时，选择部分视频配置信息项[VideoProfile](../harmonyos-references/arkts-apis-camera-i.md#videoprofile)进行视频录制，录制出的文件会损坏，无法在视频列表中找到录制的视频，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/I0SKfQRUS6yyDgqpOWa_Dg/zh-cn_image_0000002658791855.png "点击放大")

## 解决方案

打印目前所选择的视频配置信息项，结果如下：

```txt
Current video format is 2002 with width 640 and height 480
```

在选择视频配置信息项时，部分[VideoProfile](../harmonyos-references/arkts-apis-camera-i.md#videoprofile)的[CameraFormat](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)为2002（CAMERA\_FORMAT\_YCRCB\_P010）类型，需要使用[HDR录像](../harmonyos-guides/camera-hdr-recording.md)的开发能力，不然会导致文件损坏。普通录像需要选择CameraFormat为1003（CAMERA\_FORMAT\_YUV\_420\_SP）的VideoProfile，重新选择VideoProfile后的录制效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/7GnuAHmPTduZr0qmWy2lUg/zh-cn_image_0000002628552476.png "点击放大")
