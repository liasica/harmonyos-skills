---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-38
title: 打开摄像头后使用DevEco Testing测试功耗，手机温度上升过快
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 打开摄像头后使用DevEco Testing测试功耗，手机温度上升过快
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f3d124d8cd1d1dfdb80e149d6c012d7fc1aa7d8d4502816e3ba3c072bf18f57f
---

## 问题现象

在进行自定义相机开发时，使用代码开启摄像头后手机会出现发烫问题，于是用DevEco Testing记录了摄像头打开后10分钟内手机的功耗和机壳温度，在10分钟内机壳温度上升了7-8摄氏度，并且随着时间的增加温度还会持续上升。如何优化测试工具和代码，使相同时间内的温度上升幅度控制在5摄氏度以内？

## 背景知识

* [DevEco Profiler](../harmonyos-guides/ide-profiler.md)：为了帮助开发者更高效地进行性能问题的分析，DevEco Studio提供了场景化调优工具DevEco Profiler，希望为开发者带来高效、直通代码行的调优体验。
* [动态调整预览帧率(C/C++)](../harmonyos-guides/camera-setframerate-native.md)：应用可通过动态调整预览流帧率，显性地控制流输出帧率，以适应不同帧率下的业务目标。

## 解决方案

使用DevEco Testing进行功耗测试时资源消耗较高，因此在测试时不推荐使用，推荐使用DevEco Profiler进行测试。为了排除DevEco Profiler引起的发热，测试时应断开DevEco Profiler连接，操作步骤如下：

1. 运行demo，使用DevEco Profiler工具记录此时的温度。
2. 断开手机与电脑连接的USB，让demo运行10分钟左右。
3. 再次连接电脑，使用DevEco Profiler工具记录此时的温度。

测试时可以通过以下设置关闭USB充电选项：设置->系统->开发者选项->关闭充电。

在正常情况下温度上升应小于5摄氏度，如果温度上升仍比较大，可以采取动态调整帧率的方法。如果开发者没有手动设置帧率，系统会采用默认值30FPS，此帧率会导致系统功耗升高，而手动降低帧率可在相机设备启用时降低功耗，一般可将帧率设置为25FPS左右。手动设置帧率的具体步骤可参考[动态调整预览帧率(ArkTS)](../harmonyos-guides/camera-framerate.md)和[动态调整预览帧率(C/C++)](../harmonyos-guides/camera-setframerate-native.md)。

## 常见FAQ

Q：Native相机使用ImageReceiver读取，预览帧率只有20FPS左右，属于正常范围吗？

A：目前正常帧率是在20-30FPS，20FPS是正常的。

Q：设置帧率为30FPS，但某些场景下帧率会降低到24-26FPS，这种变化是正常的吗？

A：帧率变化是正常的，一般相机在预览时会出现小幅度的帧率变化。

Q：cameraManager.getSupportedOutputCapability获取到的videoProfiles中的帧率是一个范围，比如[1,30]，那么在cameraManager.createVideoOutput(videoProfile, surfaceId)，如何设置固定的帧率？

A：videoProfiles帧率范围虽然是在[1,30]之间，但实际上录像过程中帧率会尽量保持30帧，只在性能下降时略微下滑。如果确实需要稳定的帧率，则可以检查profile的frameRateRange参数，选择min和max相等的那个profile，例如：[60,60]。
