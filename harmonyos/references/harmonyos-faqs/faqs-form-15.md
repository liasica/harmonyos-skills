---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-15
title: 如何对服务卡片进行调试
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何对服务卡片进行调试
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:bb2d48fe607f1a92d6e7b1f51e742adb8313035670fc5d721545a61d0076c7c2
---

## 问题现象

因为卡片事件是从应用的form进程发起，正常情况下使用debug模式运行后会导致走不到断点；另外卡片交互冷启动应用的场景也无法正常使用debug模式进行断点调试。

## 背景知识

* [Form Kit（卡片开发框架）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统入口上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统入口上，以达到信息展示、服务直达的便捷体验效果。
* 开发者可以通过将某个应用设置为[“等待调试模式”](../harmonyos-guides/ide-debug-arkts-attach-to-process.md)，然后当开发者需要对应用进行调试时，拉起应用即可快速进入调试。

## 解决方案

开发者可通过[两种方式](../harmonyos-guides/ide-debug-arkts-extension.md)对EntryFormAbility生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

[方式一](../harmonyos-guides/ide-debug-arkts-extension.md#section14388152112818)：需要使用IDE的“等待调试”能力进行卡片交互调试。具体的实现步骤为：

1. 在设备选择框中选择调试的设备，并单击Run-》Attach to Process by Name。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/EShlSyuWQsW6YpCACzPZoQ/zh-cn_image_0000002628791558.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=A513625360FD61589B2639CE41CF4F20531163204BC3B27255C5AB4415C10A2F "点击放大")
2. 在选择调试的工程并将类型选为ArkTS。然后单击Attach，即可将该应用设置为“等待调试模式”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/98-c_aQwQwuHysVDVzeQbw/zh-cn_image_0000002658990865.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A20DC4608E705ED7AAC49936D05C022859D43D2A3DF964E0DDEA03A6D119DBB "点击放大")
3. 确认DevEco Studio底部出现Waiting for debugger进度条后，可以开始调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/0hha1ScHTkms9xSD7T1IFg/zh-cn_image_0000002628631654.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=75FB55D3CA4DE3A2A347055567E669821286B6F9590903FBEA47C5773687124D "点击放大")
4. 在需要调试的代码行的左侧边线设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/2izaCBqsQJyZFGhLdCytTg/zh-cn_image_0000002658870927.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=1854F22C0C2123D34CB6DE26A78622C857D9D4FA15E7227F46EEA0B48294FD02 "点击放大")
5. 操作应用，当应用运行到代码处，会在代码处停住，并高亮显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/oCOFMvEBRpGmRVvcO4jrjw/zh-cn_image_0000002628791560.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=793E40B98653651C173ABF2A247765751BEB44B515E32DE2DCC1EAFD75DCFF01 "点击放大")

[方式二](../harmonyos-guides/ide-debug-arkts-extension.md#section8660163873914)：需要修改IDE的运行配置方式。具体的实现步骤为：

1. 在运行调试窗口，运行配置项Launch Options选择Specified Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/W74T-i3zTIq33JNPhqWgfg/zh-cn_image_0000002658990869.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2FCD63B3F85399F5492D8DFD2204EFDDAEE9A238898785C3972718362C6FAC0 "点击放大")
2. 选择需要进行调试的EntryFormAbility。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/pIsB-oqeRBmMpo0gum4UEQ/zh-cn_image_0000002628631658.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=87DF24DFE58C662B965167916014F170D6F39CE5EA9CD0CB724F872328093896 "点击放大")
3. 点击OK保存配置后，点击调试按钮，启动调试即可命中生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yipXz2STRuGYCi4hLgOOrQ/zh-cn_image_0000002658870929.png?HW-CC-KV=V1&HW-CC-Date=20261112T233212Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACE0FECA50AC0783D29B795E8664025AC89B4C24AB35FA433A89E0F051C26F59 "点击放大")
