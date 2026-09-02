---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-14
title: 扫描表格，未生成EXCEL格式文档
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 扫描表格，未生成EXCEL格式文档
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6be3bd735ce9756669b5b53db46e714c072c9f98e5cab14eb5c202c3623bc096
---

## 问题现象

参考官方文档Vision Kit（场景化视觉服务）的[开发实例](../harmonyos-guides/vision-documentscanner.md#开发实例)，支持识别的文件类型配置了表格类型，生成的文件格式设置为JPEG格式，手机扫描表格后未生成EXCEL格式文档，如何解决？

## 背景知识

文档扫描[DocumentScanner](../harmonyos-references/vision-document-scanner.md#documentscanner)控件提供拍摄文档并转换为高清扫描件的服务，支持将文档表格扫描后生成图片。

## 解决方案

用手机对准表格扫描，预览界面左下角会出现“表格提取”按钮，需要点击“表格提取”按钮后才能进入表格提取页面，生成EXCEL格式文档。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/XTlGGL-9QoK8En8gQpWDMA/zh-cn_image_0000002658914043.png "点击放大")

## 常见FAQ

Q：HarmonyOS应用中调用文档扫描控件DocumentScanner不能弹出按钮转换，将表格照片转换为EXCEL表格，如何解决？

A：设置[DocumentScannerConfig](../harmonyos-references/vision-document-scanner.md#documentscannerconfig)的[DocType](../harmonyos-references/vision-document-scanner.md#doctype)属性仅为[DocType.SHEET]，然后识别时会作为表格去识别，回调返回的uri会是xlsx类型。设为[DocType.DOC,DocType.SHEET]，默认识别DOC，如果检测到有SHEET会在左下角显示表格提取，点击会跳转成表格提取预览流界面。

Q：调用textRecognition.recognizeText进行文本识别，这个接口的服务配额是多少？

A：配额是10000次/月。
