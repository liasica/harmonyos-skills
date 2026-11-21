---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-36
title: 提交版本提示存在Beta版本API
breadcrumb: FAQ > DevEco Studio > 工程管理 > 提交版本提示存在Beta版本API
category: harmonyos-faqs
scraped_at: 2026-11-21T09:19:23+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:625b1818c9e6c8735fefa11996bf34c444909574c4a2f9c6e29076b118f27011
---

## 问题现象

DevEco Studio运行过程中SDK报错或者提交预审时提示使用Beta版本API。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/EU0AzvjfTLisjSBpXeqRrA/zh-cn_image_0000002628567978.png?HW-CC-KV=V1&HW-CC-Date=20261121T011923Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DB54111DF1F60CCC515BCBFA7B9C8DB2BD45AA6DD920184B034DCEE9AA7198C "点击放大")

## 解决方案

1. 通过界面菜单选择“Help>About HarmonyOS SDK”查询当前SDK版本，若版本超期，请更新DevEco Studio提升SDK版本。
2. HarmonyOS应用需要将工程级build-profile.json5文件里的"[runtimeOS](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)"字段配置为"HarmonyOS"。
3. 点击Help=>Check for Updates查看IDE版本检查，确定版本不是Beta版本的IDE。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/tgNoJig3RjWrxWnGvSbAOw/zh-cn_image_0000002658927299.png?HW-CC-KV=V1&HW-CC-Date=20261121T011923Z&HW-CC-Expire=31536000000&HW-CC-Sign=C68A0B5F032C00BBCE563B1E769DAA37B1648CCD2718CB7FD08D5AF137DD3096 "点击放大")
4. 在手机的设置=>关于手机中检查SDK版本，保证SDK版本和手机版本统一，可以升级手机系统或使用手机系统对应版本的IDE。
5. 请确认当前使用的开发工具为Beta版本，需使用官网发布的Release版本。
