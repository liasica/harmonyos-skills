---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-27
title: 应用如何上架分发到多端（手机、PC、平板）
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用如何上架分发到多端（手机、PC、平板）
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:1c3fc9f74955b3bb79890cf61bb95425a3ac6136be459843525f7c94c17afd84
---

## 问题现象

同一个应用如何上架分发到手机、PC、平板多端设备，工程代码和AppGallery Connect侧如何配置？

## 背景知识

一个应用需要在多个设备上提供同样的内容，则需要适配不同的屏幕尺寸和硬件，开发成本较高。HarmonyOS系统面向多终端提供了"[一次开发，多端部署](../best-practices/bpta-multi-device-overview.md)"（简称为"一多"）的能力，让开发者可以基于一套设计，高效构建多端可运行的应用。

## 解决方案

应用上架时，需根据软件包中声明的设备（即module.json5配置文件中"[deviceTypes](../harmonyos-guides/module-configuration-file.md#devicetypes标签)"标签的枚举值）勾选对应的支持设备，确保软件包中声明的设备范围大于等于AppGallery Connect上勾选的支持设备范围。提交审核时会进行校验，如果AppGallery Connect上勾选的支持设备范围大于软件包内声明时，会提示上传的软件包与声明支持设备不一致，将无法提交审核。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/97_JcPHOQHKvBmBqYX4EWg/zh-cn_image_0000002658391408.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/EIz8zh6dTrS5k4VKNpKX0g/zh-cn_image_0000002688550963.png "点击放大")

## 常见FAQ

Q：AppGallery Connect应用信息中的支持设备勾选分发的规则有哪些需要注意？

A：

1. 当设备类型包含手机时，即便包里未声明平板，应用也会默认以兼容的方式分发到HarmonyOS NEXT平板。
2. 当设备类型未勾选PC/2in1时，但手机和平板应用经过测试后会默认发布到PC/2in1。

更多详情参考[配置支持设备](../app/agc-help-release-app-devicetype-0000002271592112.md)。

Q：应用在手机端已上架，PC端和平板与手机端功能有所不同，如何只针对PC端和平板上架？

A：需要重新创建项目单独上架PC端和平板，包名和手机端区分开。

Q：已上架应用仅支持手机/平板，想新增支持PC，除修改module.json5中的deviceTypes配置项外还需做哪些改动？

A：仅修改deviceTypes只是声明该HAP可在PC（2in1）上安装/运行，并不代表已完成PC适配。配置可写为：

```json
"deviceTypes": ["phone", "tablet", "2in1"]
```

还建议逐项检查以下内容：

1. 所有会随应用交付的Entry/Feature HAP都要确认module.deviceTypes包含2in1。
2. 做系统能力与API兼容性检查。PC有独立的系统能力集合，手机/平板可用的API、权限或硬件能力不一定都可用，需要为不支持项提供判断、降级或替代实现。
3. 完成大屏和自由窗口适配：窗口拉伸、最大化/最小化、横屏、不同宽高与缩放比例下不应出现固定尺寸、遮挡或留白问题。
4. 补齐PC输入方式：鼠标悬停/右键/滚轮、触控板、键盘焦点与Tab顺序、快捷键、拖拽等。
5. 检查多窗口及窗口尺寸变化时的状态保存、页面恢复和生命周期逻辑。
6. 使用PC模拟器和真机完整回归；发布侧提交新版本，并确认分发设备类型、PC截图/素材和审核信息已补齐。

如果现有工程本身已经采用响应式布局，所用能力也都支持PC，业务代码未必必须改；但deviceTypes只是最小配置改动，仍需通过上述适配和测试后再新增PC分发。
