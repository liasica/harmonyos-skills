---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-3
title: 图片文字识别方法及识别准确度优化
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础视觉（Core Vision） > 图片文字识别方法及识别准确度优化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c773d9587173e7ed4766a2240e4dfd9637aeddf26dc892963bd9de03321ffea8
---

## 问题现象

能通过API调用，来主动触发图片的识别功能吗？当识别不准确时，该怎么提高准确度？

## 背景知识

目前通用文字识别，可以对文档翻拍、街景翻拍等图片进行文字检测和识别，也可以集成于其他应用中，提供文字检测、识别的功能，并根据识别结果提供翻译、搜索等相关服务；可以处理来自相机、图库等多种来源的图像数据，提供一个自动检测文本、识别图像中文本位置以及文本内容功能的开放能力；支持特定角度范围内的文本倾斜、拍摄角度倾斜、复杂光照条件以及复杂文本背景等场景的文字识别。

## 解决方案

HarmonyOS提供了通用文字识别API，可以通过[textRecognition.recognizeText()](../harmonyos-references/core-vision-text-recognition-api.md#textrecognitionrecognizetext)方法的回调获取识别的对象。为保证较理想的识别结果，提高文字识别的准确度，使用通用文字识别时，建议：

* 输入图像具有合适的成像质量（建议720p以上）和高宽比例（建议2:1以下，接近手机屏幕高宽比例为宜）。
* 文本与拍摄角度夹角在正负30度范围内。
* 使用高动态范围模式（如[DynamicRangeMode.HIGH](../harmonyos-references/ts-basic-components-image.md#dynamicrangemode12)）提升图像细节，减少过曝或欠曝导致的文字模糊。
* 在Image组件中设置[enableAnalyzer(true)](../harmonyos-references/ts-media-components-video.md#enableanalyzer12)属性，激活系统自带的智能文本分析与图像处理能力。
* 通过优化像素格式，提升图像解析清晰度。
* 对识别结果中的数字部分进行正则匹配，自动纠正小数点位置。

具体可以参考文字识别[开发实例](../harmonyos-guides/core-vision-text-recognition.md#开发实例)。

## 常见FAQ

Q：文字识别和文件扫描功能是否封装成云市场里的接口给其他平台使用？

A：目前都是发展HarmonyOS生态，这个需要伙伴自行寻求第三方的解决方案。

Q：是否有HarmonyOS的拍照识别和图片识别功能？

A：可以参考[文字识别](../harmonyos-references/core-vision-text-recognition-api.md)官方文档。

Q：textRecognition可以支持中英日韩繁的文字识别，还有可以支持更多语种的OCR能力吗？或者是否有支持HarmonyOS的第三方库？

A：textRecognition目前不支持其他语种，可使用其他平台文字识别SDK或Tesseract OCR等第三方能力。
