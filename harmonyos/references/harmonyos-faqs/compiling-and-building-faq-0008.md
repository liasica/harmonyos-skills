---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0008
title: Hvigor版本更新依赖报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > Hvigor版本更新依赖报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:4b6e075298467dc513810302c031538e4af9abe9eccaabc609e5906bf6b5d3f0
---

**Q：更新hvigor版本时，配置了依赖却在build init时报未找到此依赖？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/spN_WnI1S7ixzaXjm-e5jw/zh-cn_image_0000002794527263.png "点击放大")

A：出现该问题的原因是工程中使用了3.3.0及后续版本的Hvigor，但Hvigor-wrapper.js版本较旧，两者不兼容。不兼容的场景包括：

* 场景一：使用4.0 Canary2之前的DevEco Studio时，同步只会下载Hvigor，不会下载dependencies下的内容（即hvigor-ohos-plugin）。如果需要更新Hvigor版本且不更新DevEco Studio，只能下载Hvigor，无法下载hvigor-ohos-plugin。建议更新至DevEco Studio NEXT Developer Preview1及以上版本。
* 场景二：对于4.0 Beta1之前的DevEco Studio创建的工程，需要更新Hvigor版本。使用DevEco Studio NEXT Developer Preview1及以上版本的DevEco Studio打开历史工程，修改hvigor-config.json5中的Hvigor和plugin版本号，然后Sync。同步时会提示更新，点击按钮后将自动完成Hvigor和plugin的下载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/d5TWzjzlSBeFkSlmv9AKpQ/zh-cn_image_0000002765168682.png)
