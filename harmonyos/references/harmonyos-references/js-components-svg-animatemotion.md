---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion
title: animateMotion
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > animateMotion
category: harmonyos-references
scraped_at: 2026-04-28T08:03:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:edce814effa2ba137433f0178324cabbe07eed47d07de316f0485359633a587e
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

路径动效。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

支持animate属性（values不生效）和以下表格中的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| keyPoints | string | - | 是 | 一组关键帧的点位置，每帧的值为对象沿路径的距离比例。功能与animate属性中的values相同。 |
| path | string | - | 是 | 定义运动的路径，使用与path组件d属性相同的语法。 |
| rotate | [auto | auto-reverse | <number>] | auto | 否 | 设置动画对象的旋转方向。 |
