---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-20
title: 应用横屏打开会自动切换成竖屏
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 应用横屏打开会自动切换成竖屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3af5c943d132e195d9efb1c677c7d4ec4be29e76cdacebe913a456ff682ad379
---

## 问题现象

应用横屏打开会自动切换为竖屏。

横屏状态图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/rJC-5OYGTU2UAp3V4rVpMw/zh-cn_image_0000002658911553.png "点击放大")

打开后切换为竖屏状态图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/qDal2qklQVuqpATlos15JQ/zh-cn_image_0000002628392332.png "点击放大")

## 背景知识

* 横竖屏一般是为了适应多种场景。参考[屏幕类型布局场景](../best-practices/bpta-multi-device-screen-layout.md)：竖屏适合单手操作、信息流浏览（如社交/购物APP），便于用户聚焦内容流并进行滚动、点击等基础操作。横屏提供更宽阔的视野，优化视频播放、文档编辑、游戏等场景的沉浸感和操作效率。
* 在HarmonyOS中窗口的横竖屏切换可以通过window的[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)和[getPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#getpreferredorientation12)接口配合实现。而在一多场景中，通常会在module.json5文件中配置[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)中的orientation字段来指定应用的横竖屏打开方式。

## 问题定位

1. 考虑是否是应用设置了默认打开方式为竖屏导致。检查module.json5文件中是否配置了orientation字段，该字段的值指定了应用打开方式为横屏、竖屏或其他状态。

   指定竖屏打开状态如图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/0Dpwj5obRcurAKyCwO-ADA/zh-cn_image_0000002658791619.png "点击放大")

   指定横屏打开状态如图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/K7ss4Z1zTNGyFi4wnKWZbA/zh-cn_image_0000002628552234.png "点击放大")
2. 对比发现问题中的横竖屏自动切换不是上图所示的横竖屏状态，考虑实际上发生横竖屏切换的是窗口而不是应用。检查EntryAbility.ets中onWindowStageCreate加载窗口时或者在应用打开时是否有以下变更窗口状态的类似操作：

   ```ts
   windowStage.getMainWindow((err: BusinessError, data) => {
     if (err) {
       // To do sth.
     }
     windowClass = data;
     let orientation = windowClass.getPreferredOrientation(); // 获取主窗口横竖屏状态
     if (orientation !== window.Orientation.PORTRAIT) {
       windowClass.setPreferredOrientation(window.Orientation.PORTRAIT) // 如果不是竖屏状态将主窗口设置为竖屏状态
     }
   })
   ```

## 分析结论

在窗口加载时主动变更了窗口状态导致。

## 修改建议

1. 强制变更窗口状态会给用户比较差的使用体验，不必要的情况下建议不要在窗口加载时主动变更窗口状态。
2. 如果应用只适配了竖屏，可以在module.json5中设置orientation为"portrait"，指定应用打开方式为竖屏即可。参考[配置module.json5的orientation字段](../best-practices/bpta-landscape-and-portrait-development.md#section1188593118171)。相反，如果应用只适配横屏则设置为横屏。
