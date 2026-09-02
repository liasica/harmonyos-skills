---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-132
title: 拍摄完照片后，点击预览，直接跳转至图库
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 拍摄完照片后，点击预览，直接跳转至图库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:3a048d204c29cdde912841657cd2239867cc65f0c0e2ab0e2e892bd148ba3372
---

## 问题现象

自定义相机照片拍摄后，点击左下角拍摄的图片不是直接打开，而是跳转到图库。

```ts
Image(this.finalPixelMap)
  .height(50)
  .width(50)
  .borderRadius(50)
  .onClick(() => {
    skipToAlbum(this.photoUri)
  })

async skipToAlbum(uriPath: string) {
  try {
    // 推荐替代方案（API 18+）
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    let bundleInfo: bundleManager.BundleInfo =
      await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    let wantInfo: Want = {
      bundleName: 'com.huawei.hmos.photos',
      abilityName: 'com.huawei.hmos.photos.MainAbility',
      uri: 'application_info_entry',
      parameters: {
        pushParams: bundleInfo.name // app的bundleName也就是包名
      }
    };
    context.startAbility(wantInfo).then(() => {
      // 成功
    }).catch(() => {
      // 失败
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('失败了', err.message);
  }
}
```

## 背景知识

* [on('photoAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)：注册监听全质量图上报。
* [image.createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource)：通过缓冲区创建ImageSource实例。
* [createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)：通过默认参数创建PixelMap对象。

## 问题定位

根据问题描述，排查点击按钮的事件，查看点击Image组件时，是否调用context.startAbility(wantInfo)接口，且里面的业务逻辑是否合理。

## 分析结论

点击Image组件时，调用context.startAbility(wantInfo)接口，里面的业务逻辑不合理，导致自定义相机照片拍摄后，点击左下角拍摄的图片不是直接打开，而是跳转到图库。

## 修改建议

建议在自定义相机拍照触发photoAvailable的回调中，将拍照的buffer保存为图片，然后使用Image组件全屏展示给用户。详细可参考[自定义相机拍照](../harmonyos-guides/camera-shooting.md)。
