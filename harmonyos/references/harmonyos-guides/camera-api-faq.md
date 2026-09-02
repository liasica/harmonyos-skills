---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-api-faq
title: 相机API调用时序问题
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > Camera Kit常见问题 > 相机无法启动 > 相机API调用时序问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:17+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d6aee7e8677adc8e75b04385a2fed88fa4e58bc25b3e7ca4d1cc56c8f8e358a8
---

## 问题现象

相机无法正常启动，相关日志显示某些校验没有通过或者参数错误等问题。

## 可能原因

正常启动相机的流程包括创建相机管理器（cameraManager）、创建输入/输出流（input/output）、创建会话（session）、配置会话（session）以及启动会话（session）。这些流程间存在相互依赖，如果存在某个部分创建失败、在流程中被释放导致对象不存在、使用不匹配的配置文件等情况，则会导致相机无法正常启动。比如在创建输出流的时候，没有先创建输入流，或者在创建输出流的时候，没有使用对应输入流获取的能力值，导致输入流和输出流不匹配等。具体原因可能有如下情况：

1. 没有使用正确的profile，导致创建的输出流与输入流不匹配，会导致相机启动时黑屏。
2. 提前调用相关的相机设置接口时，对应的配置还未设定完成，导致相机启动失败。
3. 监听设置的时机不对，监听不生效，导致相机启动失败。

**问题分析步骤**

步骤一：创建相机管理器（[cameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)），并选择使用的镜头（[getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)），然后通过选定的镜头，获取输出流的配置文件（[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)），需要保证和输出流的模式对应（拍照或者录像）。

步骤二：根据配置文件创建对应的输入流，调用输入流的[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open)方法打开镜头，然后创建输出流（预览，拍照/录像）。此时建议注册photoAvailable监听，用以获取照片。输出流的分辨率保持相同，然后创建对应模式的session，注意模式和输出流对应。

步骤三：调用session的[beginConfig](../harmonyos-references/arkts-apis-camera-session.md#beginconfig11)方法，开始配置。首先调用[addInput](../harmonyos-references/arkts-apis-camera-session.md#addinput11)方法，添加输入流；再调用[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)方法，添加输出流；然后调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)方法，提交session的配置，此时session的配置完成。大部分问题都会在这个流程报错，如果有问题，则无法正常完成[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)整个流程。

步骤四：在[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)之后，大部分的session监听方法可在此时配置，并且可以做一些效果设定，例如白平衡等。

## 解决措施

1. 创建的输出流与输入流前，将两者的profile中的分辨率进行比较，保证分辨率一致。
2. 大部分的set方法建议在commitConfig之后进行调用，比如白平衡相关的set接口。
3. 大部分监听相关接口，需要在addInput之后调用，保证镜头打开并添加到session中后，数据可通过监听返回。

具体代码可参考[拍照实践(ArkTS)](camera-shooting-case.md)。
