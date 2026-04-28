---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-24
title: 如何对GIF图片进行压缩
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何对GIF图片进行压缩
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1ab660aa0f7f65a66f1fd60db34b9e44fa3935526b77e4d6899115ea3247a9d5
---

* **方案一**

  可使用[packToDataFromPixelmapSequence](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodatafrompixelmapsequence18)接口保存GIF图片，然后调整PixelMap的宽高或者减少帧数对GIF图片进行压缩。

  **调整PixelMap的宽高**

  使用[createPixelMapList()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmaplist10)创建PixelMap数组，通过desiredSize参数调整PixelMap的宽高。

  **减少帧数**

  通过动图编码[PackingOptionsForSequence](../harmonyos-references/arkts-apis-image-i.md#packingoptionsforsequence18)的frameCount参数减少帧数。
* **方案二**

  通过使用FFmpeg三方库的能力降低分辨率或帧率，有以下两种方式实现GIF图片的压缩（也可将两种方式进行结合）。

  **降低分辨率**

  可以使用-s设置图片的分辨率，例如，将一个GIF图片的分辨率降低，宽高设置为90x90像素，可以使用如下命令：

  ```
  1. ffmpeg -i input.gif -s 90x90 -y output.gif （设置宽高均为90像素）
  ```

  或者使用-vf参数配合scale过滤器，设置宽为90像素，高度自动等比例缩放。

  ```
  1. ffmpeg -i input.gif -vf "scale=90:-1" -y output.gif
  ```

  以上命令的参数的意义如下：

  -s 90x90：设置图片分辨率为90x90像素。

  -y：覆盖已有文件。

  -vf "scale=90:-1"：设置图片滤镜，参数是单个滤镜或多个逗号分隔的滤镜链。

  **降低帧率**

  可以使用-r参数指定输出图片的帧率。例如，将一个GIF图片的帧率降低到16，可以使用如下命令：

  ```
  1. ffmpeg -i input.gif -r 16 output.gif
  ```

  此命令的参数的意义如下：

  -i input.gif：指定输入文件。

  -r 16：设置图片的帧率为16fps。

  output.gif：输出文件名。
