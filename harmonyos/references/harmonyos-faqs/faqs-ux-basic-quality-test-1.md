---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ux-basic-quality-test-1
title: 如何定位UX测试结果不通过问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > UX基础质量测试 > 如何定位UX测试结果不通过问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:949b966b12b25f81366cb0a7860be33c84bd954c4e6e2304530f3c4364681c62
---

## 问题现象

* 问题一：使用DevEco Testing执行UX测试结果显示“条件依赖”，报“arklayout文件存储失败”或“arklayout文件依赖调试版本应用”：

  测试结果：条件依赖。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/piqsw--uQESH8Spwud5Rew/zh-cn_image_0000002628563632.png "点击放大")

  原因说明：arklayout文件存储失败。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/i4bTzWqRQr-tHPDuj9aubw/zh-cn_image_0000002658922937.png "点击放大")

  原因说明：arklayout文件依赖调试版本应用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/3QEjao7FSq6yTJ8V9w0j1Q/zh-cn_image_0000002658802983.png "点击放大")
* 问题二：UX检测结果显示“条件依赖”，报“应用包不存在”是什么原因？

  原因显示说明：应用包不存在。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/2OIanelbQgKa0bohLaIi4w/zh-cn_image_0000002628403724.png "点击放大")
* 问题三：UX检测结果显示“元服务胶囊热区冲突”不通过，导航栏过宽该如何解决？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/41YfuJdRS427M9x5s6v4rQ/zh-cn_image_0000002628563634.png "点击放大")
* 问题四：UX检测结果显示“不涉及”该如何处理？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/J2Ws_FaaQliPl4tMzMn9Aw/zh-cn_image_0000002658922939.png "点击放大")
* 问题五：UX检测结果显示“不通过”，如何定位和修复？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/YGEb3aTTTRGzAgaG_tkbmQ/zh-cn_image_0000002658802985.png "点击放大")

## 解决方案

* 问题一解决方案：

  UX检测时部分规则依赖debug版本应用进行测试，请安装应用的debug签名版本重启手机后重新测试。
* 问题二解决方案：

  UX检测时部分规则依赖应用包完成，如果手机上已安装了应用，UX测试的部分结果会提示应用包不存在，请通过DevEco Testing进行应用的安装和测试。
* 问题三解决方案：

  应用UX体验建议中关于热区的标准可参考[适用范围](../harmonyos-guides/experience-suggestions-ux.md#section1541617350183)中“点击热区”，使用[AtomicServiceNavigation](../harmonyos-references/ohos-atomicservice-atomicservicenavigation.md#atomicservicenavigation-1)设置导航栏的宽度。
* 问题四解决方案：

  检测结果为不涉及代表测试用例的执行条件不满足，不会执行相关的测试场景，可以点击不涉及前面的“查看”进行详细查看。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ZPLtJzYYR8iisPoM7ryxvA/zh-cn_image_0000002628403726.png)
* 问题五解决方案：

  举例“典型手势时长设计”测试不通过，点击对应的“不通过数”->查看定位日志和修复指南。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/yzqhQ_iaRLyQDvKtCmppwQ/zh-cn_image_0000002628563636.png "点击放大")

  定位日志查看：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/N23R9Rs7TyaeoJputlqoNw/zh-cn_image_0000002658922941.png "点击放大")

  修复指南查看：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MqY_im-qSw2GIGs0r0L_eA/zh-cn_image_0000002658802987.png "点击放大")
