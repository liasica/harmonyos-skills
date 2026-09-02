---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-2
title: 如何解决使用SafetyDetect安全检测checkSysIntegrity接口报错问题
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 如何解决使用SafetyDetect安全检测checkSysIntegrity接口报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:35e775692d1c2d6efb23165e949c50dc768eae6c510f1e5e23165cecf12cb1e6
---

## 问题现象

使用SafetyDetect安全检测checkSysIntegrity接口提示报错The network is unreachable，请问如何解决？

## 背景知识

SafetyDetect安全检测：

* 判断设备环境是否安全，比如是否被越狱、被模拟等，您可基于结果评估如何响应。
* 判断用户访问的URL是否为恶意网址，对于恶意网址，由您评估提示或拦截用户的访问风险。
* 获取本设备的系统完整性的在线检测结果：[checkSysIntegrity](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrity)。

## 问题定位

1. The network is unreachable错误信息所属错误码为[1010800002](../harmonyos-references/errorcode-devicesecurity-safetydetect.md#section1010800002-设备网络异常)，根据错误码信息排查网络情况。
2. 使用SafetyDetect安全检测功能需要在AGC上[开通Device Security服务](../harmonyos-guides/devicesecurity-deviceverify-activateservice.md)：检查是否开通相关服务。
3. 检查Profile（.p7b）文件是否使用正确，在开通服务后，需要重新申请Profile（.p7b）文件。
4. 检查调用checkSysIntegrity接口时传入的nonce值是否正确，nonce值必须为16至66字节之间，有效值为base64编码范围。

## 分析结论

调用checkSysIntegrity接口时传入的nonce值错误，包含base64编码范围之外的字符标识，最终导致调用接口报错。

## 修改建议

在调用checkSysIntegrity接口时，必须传入一个随机生成的nonce值。在检测结果中会包含这个nonce值，可以通过校验这个nonce值来确定返回结果能够对应请求，并且没有被重放攻击。nonce值必须为16至66字节之间，有效值为base64编码范围，推荐的做法是，每次请求都从服务器随机生成新的nonce值。

## 常见FAQ

Q：在调用Device Security Kit的checkSysIntegrity接口时，真机不会报错正常返回，使用模拟器测试时，报1010800001内部错误。

A：模拟器与真机存在差异性，Device Security Kit（设备安全服务）暂不支持模拟器。

详见官网：[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)。
