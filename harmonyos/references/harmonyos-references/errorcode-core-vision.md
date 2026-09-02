---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-core-vision
title: ArkTS API错误码
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:03:11+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:a7b1123083a40cafa081bcd4445c72ede5bfb38233d470049c3fe2061a15c951
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 200 运行超时

**错误信息**

Run timed out, please try again later.

**错误描述**

运行超时，请重试。

**可能原因**

当前存在大量的请求，无法及时处理。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

## 401 参数错误

**错误信息**

The parameter check failed.

**错误描述**

输入参数错误。

**可能原因**

输入图片的类型错误或参数值错误，入参图片不符合要求。

**处理步骤**

确保输入的图片类型正确并且参数值无误后，再次尝试。

## 1001400001 OCR运行失败

**错误信息**

Failed to run OCR, please try again.

**错误描述**

OCR运行失败，请重试。

**可能原因**

输入不符合要求，或OCR服务存在异常。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

## 1001400002 OCR服务异常

**错误信息**

The OCR service is abnormal.

**错误描述**

OCR服务异常时，系统会产生此错误码。

**可能原因**

OCR服务异常。

**处理步骤**

OCR系统异常，建议重启设备重试。

## 1008400001 人脸比对运行失败

**错误信息**

Failed to run face comparator, please try again.

**错误描述**

人脸比对运行失败，请重试。

**可能原因**

输入不符合要求，或人脸比对服务存在异常。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

## 1008400002 人脸比对服务异常

**错误信息**

The face comparator service is abnormal.

**错误描述**

人脸比对服务异常时，系统会产生此错误码。

**可能原因**

人脸比对服务异常。

**处理步骤**

人脸比对系统异常，建议重启设备重试。

## 1008800001 人脸检测运行失败

**错误信息**

Failed to run face detector, please try again.

**错误描述**

人脸检测运行失败，请重试。

**可能原因**

输入不符合要求，或人脸检测服务存在异常。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

## 1008800002 人脸检测服务异常

**错误信息**

The face detector service is abnormal.

**错误描述**

人脸检测服务异常时，系统会产生此错误码。

**可能原因**

人脸检测服务异常。

**处理步骤**

人脸检测系统异常，建议重启设备重试。

## 1011000001 运行失败

**错误信息**

Failed to run, please try again.

**错误描述**

运行失败，请重试。

**可能原因**

输入不符合要求，如传入了一张没有显著性主体的图片、损坏的无法打开的图片、非图片。

**处理步骤**

重新传入一张存在显著性主体（面积占比大于千分之五）的图片。

## 1011000002 服务异常

**错误信息**

The service is abnormal.

**错误描述**

服务异常时，系统会产生此错误码。

**可能原因**

服务异常。

**处理步骤**

系统异常，建议重启设备重试。

## 1011000003 模型运行失败

**错误信息**

Failed to run the model, please try again.

**错误描述**

模型运行失败，请重试。

**可能原因**

模型加载异常。

**处理步骤**

稍后重试。

## 1011000004 模型运行超时

**错误信息**

Running the model timed out. Try again later.

**错误描述**

模型运行超时。

**可能原因**

模型加载异常。

**处理步骤**

稍后重试。

## 1018700001 业务异常

**错误信息**

Service exception.

**错误描述**

业务运行异常时，系统会产生此错误码。

**可能原因**

1. 业务运行超时。
2. 模型推理结果失败。

**处理步骤**

业务异常，建议重启设备重试。

## 1013100001 图像不可用

**错误信息**

Invalid image path or size.

**错误描述**

图像的地址或者尺寸不满足要求时，系统会产生此错误码。

**可能原因**

1. 图像地址非本应用的沙盒地址或直接为空。
2. 图像的尺寸不满足要求。

**处理步骤**

建议使用符合要求的图像，对于图像尺寸的要求，详细内容请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。

## 1013100002 服务异常

**错误信息**

Service exception.

**错误描述**

业务运行异常时，系统会产生此错误码。

**可能原因**

1. 业务运行超时。
2. 模型推理结果失败。

**处理步骤**

业务异常，建议重启设备重试。

## 1013100003 能力已更新

**错误信息**

The capability has been updated. Please use the function clearData, and after completing it, use this function again.

**错误描述**

模型能力更新后，系统会产生此错误码。

**可能原因**

1. 当前设备里的模型已经发生更新。

**处理步骤**

使用[clearData](core-vision-text-search-image-api.md#textsearchimagecleardata)方法清空数据成功后，再重新调用此前的方法重试。
