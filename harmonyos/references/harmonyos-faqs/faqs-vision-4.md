---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-4
title: 使用活体检测API报错闪退
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 使用活体检测API报错闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5e9605ae9e0b048e1811f55df3c93628aec27b4787a3326379548d0194a8ad41
---

## 问题现象

运行官网人脸活体检测API中的demo实例，出现报错闪退，报错信息为message:Cannot read property startLivenessDetection of undefined。

## 背景知识

通过IDE运行官网demo时，需确认开发环境使用的设备系统版本与IDE版本是否配套，如不配套需进行对应版本的升级处理。同时，需确定工程里build-profile.json5文件里products的内容中SDK版本是否兼容。

## 解决方案

版本升级及兼容性问题可以参考官网的[版本说明](../harmonyos-releases/overview-allversion.md)。工程里内容排查具体可以按照以下步骤处理：找到工程级build-profile.json5文件中的products，查看属性"compatibleSdkVersion"，目前API12才开始支持人脸活体检测功能，例如下列代码将最低兼容的SDK版本设为"5.0.0(12)"。

```json
"products": [
  {
    "name": "default",
    "signingConfig": "default",
    "targetSdkVersion": "6.0.0(20)",
    "compatibleSdkVersion": "5.0.0(12)",
    "runtimeOS": "HarmonyOS",
    "buildOption": {
      "strictMode": {
        "caseSensitiveCheck": true,
        "useNormalizedOHMUrl": true
      }
    }
  }
],
```

## 常见FAQ

Q：人脸活体检测手机上检测失败如何解决。

A：活体检测失败的解决办法：

1. 先确保是按提示和要求操作的（正对屏幕，靠近，只做符合提示的动作，等）；
2. 调整屏幕亮度（先往高调）；
3. 改善一下光线条件（最好是正常光，无强光直射，无强背光，光线亮一些）；
4. 换一个场景；
5. 改变角度/距离；
6. 注意：类似于正对屏幕、靠近一点这种提示，一旦出现就说明需要按照提示调整，直到提示消失。
