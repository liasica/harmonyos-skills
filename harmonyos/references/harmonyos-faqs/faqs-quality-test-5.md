---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-quality-test-5
title: 上架预检执行多个小时是否正常
breadcrumb: FAQ > DevEco Testing > 上架预检 > 上架预检执行多个小时是否正常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:598b2e63974301ab1212fcbb8271228465a1cf4658f3573df57f482892f76c33
---

## 问题现象

DevEco Testing执行上架预检，执行多个小时还没结束，是否正常？

## 解决方案

上架预检任务模式分为自定义预检和综合预检。

1. 自定义预检：可使用默认配置项，也可以自行配置时长，然后根据选择时长可以估算大概时长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/aPxpFHhlQa6zaCVV_rYuvw/zh-cn_image_0000002658922471.png "点击放大")
2. 综合预检：综合预检的测试时长是系统配置好的，会跟随应用市场的推荐策略而更新。各检测项测试时长可参考：**上架预检->应用上架预检->测试指南**（文档可能会更新，以当前版本为准）。根据测试指南中的各项检测时间估算大概时长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/pLZHkHV6Q9yQ1U2dizzlYQ/zh-cn_image_0000002658802523.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Yk7OOhksRIa7LJp10anqGg/zh-cn_image_0000002628403254.png "点击放大")

综上所述，执行多个小时属于正常情况。
