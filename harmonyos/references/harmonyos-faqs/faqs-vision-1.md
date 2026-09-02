---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-1
title: 人脸活体检测结果获取方法
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 人脸活体检测结果获取方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:e0e05a63b6901615ebba0b0caad4fca4edf92b0cae767f666f8aa75eb7b9de54
---

## 问题现象

当前通过https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection()方法跳转到人脸活体检测页面，通过getInteractiveLivenessResult()方法可以获取人脸活体检测结果，但无法确定何时调用该方法以获取采集结果。

## 背景知识

人脸活体检测通常需要快速响应，在检测过程中需要实时获取结果并处理相关事件。目前官网文档的API提供跳转检测页面https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection的方法和主动获取检测结果[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)的功能。主动获取检测结果具体使用参考代码如下：

```typescript
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let successResult = interactiveLiveness.getInteractiveLivenessResult();
successResult.then(data => {
  hilog.info(0x0001, 'LivenessCollectionIndex', `Succeeded in detecting.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0001, 'LivenessCollectionIndex', `Failed to detect. Code：${err.code}，message：${err.message}`);
});
```

人脸活体检测相对应的页面生命周期状态可参考下图逻辑：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/8G2yttQESmGdVVi_DKC-sg/zh-cn_image_0000002628394820.png "点击放大")

**检测开始**：页面A点击开始检测按钮调用https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection()，进入检测页面B，此时页面A进入onPageHide()阶段，页面B进入onPageShow()阶段。

**检测结束**：根据routeMode设置的不同值，在检测结束后会跳转至上一页面A或者新的页面C，此时会触发页面A或者页面C的onPageShow()阶段。

## 解决方案

获取人脸活体检测结果可通过以下方案解决：根据routeMode设置的不同值，可以配置检测完成后路由跳转模式为back模式或者replace模式。

* 设置为back模式时，可以直接通过https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection()的回调函数获取检测结果。
* 设置为replace模式时，则需要利用生命周期的onPageShow()阶段回调实现，即在检测结束后进入页面C的onPageShow()阶段调用getInteractiveLivenessResult()方法获取检测结果，实现代码可参考官方[开发实例](../harmonyos-guides/vision-interactiveliveness.md#开发实例)。

## 常见FAQ

Q：注释“getInteractiveLivenessResult接口调用完会释放资源”是什么意思？

A：用户活体检测完成之后，调用[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)接口会获取到上次活体检测的结果，接口返回结果之后会清理活体检测的结果，如果再次获取会显示算法在初始化。使用https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness#startlivenessdetection的callback获取活体检测的结果，接口返回结果之后会清理活体检测的结果。
