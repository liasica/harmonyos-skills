---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-15
title: 人脸活体检测结果mPixelMap的获取
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 人脸活体检测结果mPixelMap的获取
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:4bd4b6ac597feef360d80ae9fa0ff030cd6b15702957e0d8f432ce919e016e31
---

## 问题现象

在使用人脸活体检测时，配置routeMode为back模式获取结果后，callback里取到的回调result里没有mPixelMap。

```ts
interactiveLiveness.startLivenessDetection(routerOptions,
  (err: BusinessError, result: interactiveLiveness.InteractiveLivenessResult | undefined) => {
    if (err.code !== 0 && !result) {
      console.error('startLivenessDetection error')
      return;
    }
    const imagePackerApi: image.ImagePacker = image.createImagePacker();
    let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };
    console.info(`startLivenessDetection result ${JSON.stringify(result)}`);
    imagePackerApi.packing(this.result?.mPixelMap, packOpts).then((data: ArrayBuffer) => {
      let buf: buffer.Buffer = buffer.from(data);
      this.base64 = 'data:image/jpeg;base64,' + buf.toString('base64', 0, buf.length);
      let parmDic: Map<string, string> = new Map();
      parmDic['WsType'] = '2';
      parmDic['states'] = 'success';
      parmDic['FacePhoto'] = this.base64;
      console.info(`startLivenessDetection parmDic ${JSON.stringify(parmDic)}`);
    })
  })
```

打印结果如下：

```txt
09-05 14:01:22.926 21147-21147 A03D00/JSAPP com.examp..._harmony I startLivenessDetection result {"livenessType":0,"mPixelMap":{}}
```

## 背景知识

人脸活体检测API中[InteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#interactivelivenessresult)为返回人脸活体检测结果的相关参数，其中包含mPixelMap对象，该对象表示检测成功后返回最具有活体特征的图片，类型为[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

## 解决方案

[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)对象不是标准的JS对象，而是HarmonyOS提供的图像对象，所以无法使用JSON.stringify打印，可以通过[Image](../harmonyos-references/ts-basic-components-image.md)组件验证是否可以正确显示图片。

## 常见FAQ

Q：HarmonyOS提供的活体检测能力，是否会输出照片？

A：活体检测返回校验结果和一张活体照片。

Q：活体检测和人脸识别是需要通过华为服务器进行数据处理然后返回，还是通过手机本身进行处理判断的？如果是发送用户数据到华为服务器，是否能私有化到我们本地服务器，不走华为侧？

A：人脸活体检测是端侧的，不存在远程服务器，数据不保存不上传云端。

Q：HarmonyOS活体检测是否支持公安比对能力？

A：当前活体检测成功之后会返回最具有活体特征的图片，公安比对能力需开发者自行拿图片进行后续操作。

Q：活体检测返回的图片，人脸部分是蓝色的，后端无法识别，是什么原因？

A：出现偏蓝的情况可能是因为光线、相机曝光等原因导致的，可以尝试以下方法解决：

1. 调整光线：将环境光线调整到适宜的亮度，避免过暗或过亮的情况。
2. 调整相机曝光：可以尝试调整相机曝光参数，使得拍摄的图片更加清晰明亮。

Q：[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)和[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)都可以获取检测结果，一个是Promise回调一个是使用callback回调获取检测结果，有什么区别？

A：[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)的callback回调函数当前只适用于RouteRedirectionMode.BACK\_MODE跳转模式。如果是RouteRedirectionMode.REPLACE\_MODE模式需要使用[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)，参考人脸活体检测[开发实例](../harmonyos-guides/vision-interactiveliveness.md#开发实例)。

Q：调用[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)方法时，data.mPixelMap为undefined的情况有哪些？

A：活体检测失败时data.mPixelMap为undefined，常见原因包括：强光、强逆光、暗光、人脸遮挡、使用相册照片等。另外，建议判断[LivenessType](../harmonyos-references/vision-interactive-liveness.md#livenesstype)为0时再取data.mPixelMap，避免在非活体检测场景下访问该字段。
