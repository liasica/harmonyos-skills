---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-screen-diff
title: 多设备适配屏幕差异
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备功能开发 > 多设备适配屏幕差异
category: best-practices
scraped_at: 2026-04-29T14:12:38+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:09b5bbb37219c19c44758c6ef852d091f835f6b04ebcc0d4ad41cf57c3df979c
---

## 概述

多设备适配技术旨在解决跨设备界面一致性问题，如在折叠屏开合、窗口自由调整等场景中保障布局完整性。其核心策略在于通过动态布局调整和响应式设计，消除屏幕尺寸差异导致的截断与留白问题，并确保交互状态切换时的视觉连续性。

本文主要面向中高级开发者。开始之前，建议先了解[一次开发，多端部署](bpta-multi-device-overview.md)、[断点](bpta-multi-device-responsive-layout.md#section1532120147301)等知识点。

本文主要内容如下：

* [适配多设备屏幕差异](bpta-multi-device-screen-diff.md#section82114465127)：根据多设备屏幕的差异，建议页面适配不同尺寸的屏幕，具体可参考[页面适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section103508214132)；在短视频等场景下，建议考虑视频在多设备下的沉浸式体验和尺寸适配，具体可参考[视频适配不同尺寸屏幕](bpta-multi-device-screen-diff.md#section1452572513130)。
* [适配折叠设备屏幕](bpta-multi-device-screen-diff.md#section2079763671319)：开发者在适配折叠设备屏幕时，除了页面需要适配不同尺寸屏幕外，建议适配：[开合连续](bpta-multi-device-screen-diff.md#section16541144511135)和[悬停态](bpta-multi-device-screen-diff.md#section32851531135)。

## 适配多设备屏幕差异

### 页面适配不同尺寸屏幕

页面适配不同尺寸屏幕的本质，是适配不同尺寸的窗口——无论是手机、折叠屏、平板还是电脑，其屏幕差异最终都体现为应用显示窗口宽高、比例的差异。因此，适配的核心应基于窗口属性抽象出响应式能力，通过“[断点](bpta-multi-device-responsive-layout.md#section1532120147301)适配”实现界面随窗口尺寸动态调整，确保在任意窗口规格下均能稳定显示，详情可参考[通过断点刷新UI](bpta-multi-device-responsive-layout.md#section175001836203617)。通过一次性基于断点的布局适配，即可支持分屏、悬浮窗、自由窗口等多种窗口模式，确保界面在不同形态间平滑、连续地响应变化。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DsgnQ91CTNu1vquGiScEYA/zh-cn_image_0000002506596732.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=849131F0ABACE510417C03231A190E8DEF6A5DF215B72D2E67824898A9AB35AC "点击放大")

开发多设备界面时，不同屏幕类型常用的响应式布局可参考[屏幕类型布局场景](bpta-multi-device-screen-layout.md)，包含[直板机竖屏](bpta-multi-device-screen-layout.md#section1919517165814)、[大屏横屏](bpta-multi-device-screen-layout.md#section6493354468)等常见窗口形态和[小方形屏](bpta-multi-device-screen-layout.md#section1395830175918)等特殊窗口形态的适配。

### 视频适配不同尺寸屏幕

视频适配不同尺寸屏幕，旨在确保各类宽高比的视频在多种设备屏幕上均能呈现良好效果，避免拉伸变形或关键内容被过度裁切。为提升视频观看体验，可通过全屏展示、弱化界面干扰，使用户更加专注于视频内容。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/dBN4RLF4T4e5KVlx1LL90w/zh-cn_image_0000002506436906.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=36CD3A5250ADD07E35A078FB3A068EC9D0748746D23715B437FC987F79B136B3 "点击放大")

为了实现这一效果，需考虑不同尺寸视频在不同尺寸窗口上的适配规则。从视频的宽高比出发，可分为9:16和非9:16两种类型。

说明

本章节的适配规则适用于宽度大于320vp的窗口。

**适配宽高比非9:16的视频**

宽高比非9:16的视频包括竖向视频（高>宽）或横向视频（宽>高），红色区域为推荐的视频显示区域，适配建议如下图所示，其中横向坐标为窗口宽高比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/c02l4ZSVSnqo4c6m8T1qCw/zh-cn_image_0000002538396643.png?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=14A93167BE5856E1418703BEAE9F4AB9DF8E23BD810500ADAC20A6E593542BDC "点击放大")

**适配宽高比为9:16的视频**

当视频宽高比为9:16时，其在断点区间的适配效果图如下图所示，红色区域为推荐的视频显示区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zkkYVi7TTR22dODaVgKxCQ/zh-cn_image_0000002538316627.png?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=F92EB114C92B688EC74C4567E6ECD5959028E25ABE4492B3404FF50C34717817 "点击放大")

当横向断点为sm、纵向断点为lg时，由于设备尺寸的差异，存在不同的适配建议。具体如下图所示，其中横坐标为窗口宽高比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/n81olrlJSfmRICLQFASaoA/zh-cn_image_0000002506596740.png?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=5519DBE34175F8CAC31675B7622D970C2FBE8647B6A4358C022D9A7A3AC1F8C0 "点击放大")对于不满足横向断点为sm、纵向断点为lg的其他窗口尺寸，建议顶部状态栏和底部Tab栏均采用沉浸式设计，内容区高度=窗口高度，内容区宽度=内容区高度×视频宽高比。

**获取窗口信息**

如前述章节所述，在视频适配不同窗口尺寸时，需获取窗口尺寸信息、避让区信息等参数用于计算。以下列举的方法将在适配过程中使用：

* 使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法，返回的对象中windowRect.width和windowRect.height分别表示窗口的宽度和高度；
* 使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)方法，返回的[AvoidArea](../harmonyos-references/arkts-apis-window-i.md#avoidarea7)对象可获得当前设备的避让区域信息；
* 屏幕窗口尺寸可能会发生变化，比如在自由窗口模式下可任意调整窗口大小，需使用[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)监听窗口尺寸的变化。当窗口尺寸变化时，应依据适配规则重新计算内容区域的尺寸，确保视频展示效果良好；
* 系统避让区可能会发生变化，例如窗口从全屏模式切换至悬浮窗模式，需要使用[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听系统避让区的尺寸变化，避让区尺寸变化时，应依据适配规则重新计算内容区域的尺寸；

以上适配建议的实现示例代码可参考[基于adaptive\_video的短视频适配](bpta-short-video-base-adaptivevideo.md)。

## 适配折叠设备屏幕

折叠设备通常具有支持独立显示的两块或多块屏幕，例如Mate X5、Mate XT和MateBook Fold等。开发者在适配折叠设备屏幕时，除了页面适配不同尺寸屏幕外，还需关注两个特殊点：[开合连续](bpta-multi-device-screen-diff.md#section16541144511135)和[悬停态](bpta-multi-device-screen-diff.md#section32851531135)。

### 开合连续

[开合连续](bpta-foldable-guide.md#section186893019118)指应用在各种屏幕和窗口状态间切换时页面内容连续，切换之前的任务和相关状态能保存、延续，或能够快速恢复，给用户提供连续的体验。具体可参考[适配应用界面开合连续](bpta-foldable-guide.md#section186893019118)。

### 悬停态

折叠屏在悬停态下可平稳放置于桌面，实现免手持体验，适用于视频通话、播放视频、拍照及听歌等无需频繁交互的场景。设计规范可参照[悬停态](../design-guides/foldable-0000002352875141.md#section183378919119)。设备在悬停态时，应用需避开中间折痕区域，并对上下两个界面进行悬停适配，重新布局。悬停状态的实现方案可参考[折叠屏悬停态](bpta-folded-hover.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Obk0hf2nSlu8qa7Mf4GbBg/zh-cn_image_0000002506436912.png?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=80D950ACC67BE300EA09A7810FC43F60EE7A4E887250341247D6AD20792D985A "点击放大")
