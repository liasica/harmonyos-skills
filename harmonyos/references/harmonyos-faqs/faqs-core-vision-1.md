---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-1
title: 人脸检测FaceRectangle坐标值偏差问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础视觉（Core Vision） > 人脸检测FaceRectangle坐标值偏差问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:847078c1600329928cffa4caa5bda3e901e86dec507537668d2ef7b14df8a2f9
---

## 问题现象

参考[人脸检测指南](../harmonyos-guides/core-vision-face-detector.md)检测照片并获取了人脸数据，但返回的数据中，[FaceRectangle](../harmonyos-references/core-vision-face-detector-api.md#facerectangle)数据看起来较大，并且看起来不对应于设备屏幕中的实际位置。

## 背景知识

* [人脸检测](../harmonyos-references/core-vision-face-detector-api.md)：支持2D人脸检测框的检测能力。检测给定图片中的人脸数量、人脸位置、特征点（左右眼中心、鼻子、左右嘴角）和姿态（pitch、roll、yaw）信息。人脸检测框按照大小排序。
* [适用场景](../harmonyos-guides/core-vision-face-detector.md#适用场景)：检测图片中的人脸，返回高精度人脸矩形框坐标、人脸五官位置、人脸朝向、人脸置信度。可通过对人脸的定位，实现对人脸特定位置的美化修饰。广泛应用于各类人脸识别场景，如人脸聚类、美颜等场景中。

## 问题定位

1. 排查是否是[像素单位](../harmonyos-references/ts-pixel-units.md)问题：接口返回的数据值看起来比较大，是否是像素单位不一致导致的。使用对应像素单位进行转换后发现还是数值较大。
2. 排查[faceDetector.detect](../harmonyos-references/core-vision-face-detector-api.md#facedetectordetect)接口返回的数据[FaceRectangle](../harmonyos-references/core-vision-face-detector-api.md#facerectangle)是相对宽高（数据值没有问题），还是绝对宽高。

## 分析结论

不是像素单位的问题，FaceRectangle是表示人脸的矩形框，宽高是相对图片尺寸的宽高，不是在设备屏幕中位置。

## 修改建议

人脸检测使用方法可参考[官网示例demo](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_Next-CoreVisionKit)。人脸检测通过[faceDetector.detect](../harmonyos-references/core-vision-face-detector-api.md#facedetectordetect)返回的结果中包含人脸数据的相关信息，数据中[FaceRectangle](../harmonyos-references/core-vision-face-detector-api.md#facerectangle)表示的是人脸在检测图片中的位置，其宽高是相对于图片的尺寸宽高，并不是相对于屏幕的位置，不存在坐标值偏差问题。

## 常见FAQ

Q：人脸识别是否支持纹理？

A：目前暂不支持。
