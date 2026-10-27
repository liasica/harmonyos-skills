---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-99
title: HarmonyOS 开发者中心应用状态分类和相关操作
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS 开发者中心应用状态分类和相关操作
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:47+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:80485622bbf978476a5e3e3249a21d9ddc5256970e18f0de90dccb2b39ffa927
---

## 问题现象

在HarmonyOS 开发者中心创建的应用，有哪几种状态，都可以进行什么操作？

## 解决方案

应用状态涵盖应用信息和版本信息，分为以下几种：

1. 准备提交：创建完的应用在未提交审核时状态为“准备提交”，“准备提交”状态一般也称为草稿态；草稿态的应用可以编辑，但是不能删除。如在应用信息下面修改支持的设备类型，修改应用名称和语言；在版本信息下面修改应用介绍，更换发布素材等。“准备提交”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/o3lDEjs-RJmZLX3UIFObKg/zh-cn_image_0000002709670597.png)
2. 正在审核：完成应用信息和版本信息填写后，可以提交应用审核，此时应用状态为“正在审核”，“正在审核”状态的应用的无法编辑，如果需要修改应用信息或版本信息，可以撤销审核后再编辑。“正在审核”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/vHljqyhsR9qwQwGZ2xUlJw/zh-cn_image_0000002679830918.png)
3. 待修改：应用提交审核被驳回后，应用状态为“待修改”，“待修改”状态的应用可以编辑，但是不能删除。需要根据审核意见完成修改后重新提交审核。“待修改”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/uOAv6AOkQUa4SdTz2G34jg/zh-cn_image_0000002679990784.png)
4. 待上架：如果应用提交审核时[设置了上架时间](../app/agc-help-release-app-review-time-0000002293233458.md)，审核通过时未到达上架时间，应用状态为“待上架”，“待上架”状态的应用无法编辑应用信息和版本信息，但可以编辑上架时间或者[手动发布待上架的应用](../app/agc-help-release-app-review-time-0000002293233458.md#section0726113812279)。“待修改”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/UL8jxWQCQxCIwIvtSbYxBg/zh-cn_image_0000002679990786.png)
5. 已上架：如果提交审核时上架时间选择的“审核通过立即上架”，或者“待上架”的应用已经达到了上架时间，审核通过后应用状态为“已上架”。“已上架”状态的应用的无法编辑，如果需要修改应用信息或版本信息，可以下架后再编辑。“已上架”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Z1aK0F8QQAicvh_m3Zceog/zh-cn_image_0000002709670599.png)
6. 已撤销上架：应用处于“待上架”状态时，如果不想再上架该应用，可以点击“撤销上架”，撤销上架操作不需要人工审核，撤销上架后应用状态为“已撤销上架”，“已撤销上架”状态应用可以编辑后重新上架。“已撤销上架”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/pUjx564VQQK_T-6MITNKQg/zh-cn_image_0000002709670601.png)
7. 下架处理中：处于“已上架”状态的应用可以选择申请下架，申请下架需要审核，此时应用状态为“下架处理中”，“下架处理中”的应用在等待审核过程中，还可以选择[撤销下架申请](../app/agc-help-maintain-remove-0000002274058145.md#section7906639512)。“下架处理中”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/KpGkH7wYRpGc2RjU-bKuXw/zh-cn_image_0000002679830920.png)
8. 被开发者下架：申请下架的应用审核通过后，应用状态将变为“被开发者下架”。下架的应用可以编辑信息后重新提交上架。“被开发者下架”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/arQCCUUaTWStGHy4AgN5vg/zh-cn_image_0000002709550749.png)
9. 被下架：应用上架后如果华为应用市场发现应用存在恶意违规情况，会发起应用下架操作，下架成功后应用状态为“被下架”，“被下架”的应用状态标识如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/-6F8OUFZQ42EiVrD-YgsDg/zh-cn_image_0000002679990788.png)

## 总结

已上架状态的应用无法直接删除，需先申请下架，待应用变为"被开发者下架"状态后方可执行删除操作。审核中和已上架的应用信息和版本信息无法编辑，如果需要编辑可以通过[升级版本](../app/agc-help-maintain-upgrade-0000002236494386.md)或[更新应用信息](../app/agc-help-maintain-update-0000002271413697.md)的方式更新。
