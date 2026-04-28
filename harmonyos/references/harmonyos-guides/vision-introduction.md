---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-introduction
title: Vision Kit简介
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > Vision Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:474169c8cd06a298a60d1889ac3545c43be7b414b7234dbee6047c8825588e66
---

Vision Kit（场景化视觉服务）集成了视觉类AI能力，包括人脸活体检测（interactiveLiveness）能力、卡证识别（CardRecognition）能力、文档扫描（DocumentScanner）能力、AI识图控件（visionImageAnalyzer）能力。人脸活体检测能力便于用户与设备进行互动，验证用户是否为真实活体；卡证识别能力可提供身份证、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务；文档扫描控件可提供拍摄文档并转换为高清扫描件的服务；AI识图控件可提供场景化的文本识别、主体分割、识图搜索功能。其中动作活体检测能力、卡证识别能力实施试用期免费的计费政策，试用期至2026年12月31日。开始正式收费前，华为将会提前通过正式途径发布计费调整通告。

## 场景介绍

Vision Kit提供了人脸活体检测能力、卡证识别能力、文档扫描能力和AI识图能力，具体如下：

* [人脸活体检测](vision-interactiveliveness.md)：通过动作活体检测，验证用户是否为真实活体。
* [卡证识别](vision-cardrecognition.md)：多证件的结构化识别服务。
* [文档扫描](vision-documentscanner.md)：提供拍摄文档并转换为高清扫描件的服务。
* [AI识图](vision-imageanalyzer.md)：提供场景化的文本识别、主体分割、识图搜索功能。

## 约束与限制

### 支持的设备

| 能力 | 支持的设备 |
| --- | --- |
| 人脸活体检测 | Phone、Tablet。 |
| 卡证识别 | Phone、Tablet。 |
| 文档扫描 | Phone、Tablet。 |
| AI识图 | Phone、Tablet、PC/2in1。 |

### 支持的国家/地区

仅适用于中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 能力限制

| AI能力 | 约束 |
| --- | --- |
| 人脸活体检测 | - 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。  - 支持的播报语种类型：简体中文、英文。  - 人脸活体检测服务暂不支持横屏、分屏进行检测。 |
| 卡证识别 | - 支持的语种类型：简体中文、英文。  - 卡证识别暂时只支持中国二代身份证、中国国内银行卡、中国护照、中国驾驶证、中国行驶证（暂不支持中国港澳台地区及海外证件）。  - 卡证需要保持与真实证件一致的长宽比、没有形变、正向拍摄角度小于30度。  - 卡证图像清晰、完整。无摩尔纹、无遮挡、无反光、无卡套。  - 不允许被其他组件或窗口遮挡。 |
| 文档扫描 | - 支持的语种类型：简体中文、英文。  - 文档扫描暂时只支持phone、tablet设备。  - 不允许被其他组件或窗口遮挡。 |
| AI识图 | - 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。  - 支持图片最小规格100\*100分辨率。  - 分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)进行分析，目前仅支持[RGBA\_8888](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)类型。  - 支持翻译的图片宽高最小比例为1:3（高度小于宽度的3倍），支持文本识别的图片宽高最小比例为1:7（高度小于宽度的7倍）。  - 支持的设备情况请参见[约束与限制](vision-imageanalyzer.md#约束与限制)。 |

## 模拟器支持情况

本kit暂不支持模拟器。
