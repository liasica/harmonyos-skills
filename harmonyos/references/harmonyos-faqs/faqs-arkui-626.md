---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-626
title: 沉浸式状态栏深色模式下显示不清晰
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 沉浸式状态栏深色模式下显示不清晰
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:29d627d2c016eafb7b3e7c216066ca9ab97c69c995040bc260dd9608fad8c4ec
---

## 问题现象

应用使用白色主题背景图，在深色模式下，状态栏看不清。

如下图所示（左边是正常模式，右边是深色模式）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ufQCF-ZLRUKWf2YoauNh5Q/zh-cn_image_0000002628554170.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/EwpRJ6DfSgahYZK68g5DQA/zh-cn_image_0000002628394270.png "点击放大")

## 背景知识

1. [沉浸式页面实现](../best-practices/bpta-multi-device-window-immersive.md)：沉浸式页面开发常通过将应用页面延伸到状态栏和导航栏的方式，来为用户提供更好的视觉体验。
2. [深色模式适配](../best-practices/bpta-dark-mode-adaptation.md)：深色模式，是与日常应用使用过程中的浅色模式相对应的一种UI主题。相较浅色模式更加柔和，能减少亮度对用户眼睛造成的刺激和疲劳，此外深色模式能在一定程度上降低应用功耗，提升续航表现。

## 问题定位

1. 在应用启动以及切换到该页面的日志里检索关键字“SetLayoutFullScreen”：

   ```shell
   34359-34359   C04209/com.xx...xx/WMSImms  com.xx...xx  I     [] SetLayoutFullScreen(2088): winId:1044 xx0 status:1
   ```

   或者在代码中排查“setWindowLayoutFullScreen”接口：

   ```ts
   windowClass?.setWindowLayoutFullScreen(true).then(() => {
     hilog.info(0x0000, 'testTag', 'Succeeded in setting full-screen mode.');
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'testTag', `Failed to set full-screen mode. Code: ${err.code}, message: ${err.message}`);
   });
   ```

   表明应用开启了全屏沉浸式，需要屏蔽应用内深色模式，或者对深色模式进行适配。
2. 开启深色模式时，检索日志“UpdateDefaultStatusBarColor”：

   ```shell
   50731-50731   C04209/com.xx...xx/WMSImms  com.xx...xx  I     [] UpdateDefaultStatusBarColor(711): winId: 1045, type: 1, colorMode: dark
   ```

   表明状态栏进入了深色模式，图标和字体颜色会由默认的黑色变成白色，在应用白色背景下，显示不清晰。

## 分析结论

由于应用启用了全屏沉浸式并且页面使用了白色背景，在没有对深色模式适配的情况下，状态栏图标和字体在深色模式会变成白色，导致该问题。

## 修改建议

应用需要屏蔽深色模式，或者适配深色模式。

* 屏蔽深色模式：在应用启动时或者在页面内，固定应用窗口为浅色模式。以启动时为例，在onCreate生命周期回调适配：参考[应用主动设置深浅色模式](../harmonyos-guides/ui-dark-light-color-adaptation.md#应用主动设置深浅色模式)。
* 适配深色模式，在深色模式下，替换背景图为深色背景，或者设置状态栏为其他对比明显的颜色。参考[状态栏适配](../best-practices/bpta-dark-mode-adaptation.md#section1618831013284)。
