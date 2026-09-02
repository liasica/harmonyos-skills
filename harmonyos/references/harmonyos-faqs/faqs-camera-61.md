---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-61
title: 帧率的选择和动态调整
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 帧率的选择和动态调整
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9ce7f8d3d4a368987eff1332580145feacec707b0fd2ceca2ccf118a55b12d8b
---

## 问题现象

在视频开发过程中，对于系统提供的帧率的规格参数应该如何理解？在实际业务场景又应该如何选择？

## 背景知识

* [FrameRateRange](../harmonyos-references/arkts-apis-camera-i.md#frameraterange)：帧率范围。
* 帧率调整相关接口见下表：

  | 接口 | 说明 | 适用范围 |
  | --- | --- | --- |
  | [VideoOutput.getSupportedFrameRates](../harmonyos-references/arkts-apis-camera-videooutput.md#getsupportedframerates12) | 查询录像流支持的帧率范围。 | 录像流 |
  | [VideoOutput.setFrameRate](../harmonyos-references/arkts-apis-camera-videooutput.md#setframerate12) | 设置录像流帧率范围，设置的范围必须在支持的帧率范围内。  设置前，可通过getSupportedFrameRates查询支持的帧率范围。 | 录像流 |
  | [VideoOutput.getActiveFrameRate](../harmonyos-references/arkts-apis-camera-videooutput.md#getactiveframerate12) | 获取已设置的录像流帧率范围。  使用setFrameRate对录像流设置过帧率后可查询。 | 录像流 |
  | [PreviewOutput.getSupportedFrameRates](../harmonyos-references/arkts-apis-camera-previewoutput.md#getsupportedframerates12) | 查询预览流支持的帧率范围。 | 预览流 |
  | [PreviewOutput.setFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#setframerate12) | 设置预览流帧率范围，设置的范围必须在支持的帧率范围内。  进行设置前，可通过getSupportedFrameRates接口查询支持的帧率范围。 | 预览流 |
  | [PreviewOutput.getActiveFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#getactiveframerate12) | 获取已设置的预览流帧率范围。  使用setFrameRate接口对预览流设置过帧率后可查询。 | 预览流 |

## 解决方案

1. 帧率规格的基础认识
   * 帧率规格的分类。

     帧率大致分为两类，即非固定帧率和固定帧率。所谓非固定帧率是指规格中最低帧率低于最高帧率，比如[1,30]；而固定帧率指的是规格中最低帧率等于最高帧率，比如[60,60]。
   * 帧率规格如何影响实际视频帧率？

     通常情况下，硬件会以应用指定的帧率来出帧。以固定帧率为例，代码里设定帧率为[60,60]之后，系统会以60的帧率出帧。而在选择非固定帧率如[1,30]时，系统将会倾向于以1-30之间的某个帧率作为实际帧率出帧，不会出现“拍摄的短片帧率一直在1-30之间随意变化”的情况。

     需要注意的是，在指定帧率规格之后，个别场景下帧率依然可能会有波动甚至跌破指定帧率下限，比如设备极端发热场景导致实际帧率下降等。
2. 如何选择合适的帧率

   首先开发者在选择帧率时不能跳出系统的规格范围，其次需要结合业务需求挑选合适的帧率规格，不同业务场景下的帧率设置可参考下表：

   | 应用场景 | 推荐帧率 | 核心原因 | 适用场景举例 |
   | --- | --- | --- | --- |
   | 流畅/交互类 | 60fps | 人眼感知最顺滑，消除动态模糊。 | 直播、短视频拍摄、AR特效等。 |
   | 通用/平衡类 | 30fps | **最推荐**。画质与体积平衡，符合人眼习惯。 | 日常视频记录、社交APP上传、监控回放。 |
   | 存储/带宽敏感 | 24fps | 降低码率和存储压力，动态画面会有轻微胶片感。 | 长时间录音录像、低带宽传输、非关键事件记录。 |
   | 特殊/低性能设备 | 15-24fps | 为避免设备过热或算力不足而降级。 | 老旧机型、物联网摄像头、长时间后台录制等。 |
3. 如何在开始录像后对帧率进行动态调整
   * 预览帧率的调整。

     预览帧率调整可参考[动态调整预览帧率(ArkTS)](../harmonyos-guides/camera-framerate.md)或[动态调整预览帧率(C/C++)](../harmonyos-guides/camera-setframerate-native.md)，通过[PreviewOutput.setFrameRate()](../harmonyos-references/arkts-apis-camera-previewoutput.md#setframerate12)接口设置帧率。
   * 录像帧率的调整。

     过程可参考预览帧率调整，流程相同，只需要把接口换成录像流的设置接口即可。

## 常见FAQ

Q：设备性能和视频帧率之间的影响关系是否有图表可供参考？在高性能和高帧率之间该如何做出平衡？

A：帧率与性能之间的关系受设备硬件性能影响较大，无法给出具体的、有实际参考意义的关系图。但可以肯定的一点是，长时间录制视频可能导致设备性能下降，而设备性能下降后系统出图的帧率也可能会受到影响。因此可以参考[压力管控(ArkTS)](../harmonyos-guides/camera-system-pressure.md)或[压力管控(C/C++)](../harmonyos-guides/native-camera-system-pressure.md)，监听系统压力等级，在系统压力发生变化时，及时对帧率等参数做出调整。

Q：在视频录制时，已经将AVRecorderProfile.videoFrameRate设置为60，为什么拍摄出来的视频帧率还是30帧？

A：需要在创建VideoOutput时，同时选择frameRateRange为[60,60]的profile。

Q：在使用相机服务的PreviewOutput.setFrameRate方法设置最小最大帧率为12-15时，实际帧率只有一半。但是当设置帧率大于15时，实际帧率就正常。请问是什么情况？

A：代码中同时开启了一路预览流和一路录像流，当两路流帧率不一致时系统会通过使高帧率的流丢帧来实现帧率同步，因为下发的录像流帧率为30，所以导致了录像流丢一半帧（30/12=2，因此为了实现帧率同步录像流会丢弃一半的帧）。代码中需确保下发流时保持预览流和录像流的帧率一致，如果预览流为12帧，那么下发的录像流也应该为12帧，帧率差距不能过大。

Q：屏幕的60、120刷新率是系统什么机制决定的？与相机模块的帧率是否有关？

A：系统有自己的投票机制，多组件的情况下由最后一个组件的帧率决定，比如一个组件投40hz，另一个80hz，最后就是80hz。控制帧率可以用[PreviewOutput.setFrameRate](../harmonyos-references/arkts-apis-camera-previewoutput.md#setframerate12)。

Q：动态设置帧率后实际帧率未发生变化，始终保持在设置范围内的最大值，是什么原因？

A：动态设置帧率后，在性能允许的情况下，系统会尽量按设置范围内的最大帧率出帧，以保证用户视觉体验。例如设置帧率范围为12-20，在CPU负载较低时，系统会以20帧出帧，这是符合预期的。只有在极端场景下（如设备高温导致相机功耗过高）才可能触发帧率变化，使帧率降低至范围内的较低值。
