---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-4
title: 下载HarmonyOS SDK时提示网络连接错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 下载HarmonyOS SDK时提示网络连接错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:64a081b39be2a770035f5bdc1ae5c948e667167170f11854e54b62f86a0b886b
---

**问题现象**

网络连接正常，但下载HarmonyOS SDK时提示网络连接错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/l60gc28TQ1W0Uyj5rv3iBw/zh-cn_image_0000002229758633.png?HW-CC-KV=V1&HW-CC-Date=20260428T002852Z&HW-CC-Expire=86400&HW-CC-Sign=C0340AFB3ED438B2D454E7DB2A107C0EEABDCAA34EF57249FCC7BE29627DAB24)

**解决措施**

由于使用的PC系统语言为英文且区域码为US，可能导致问题。请按照以下步骤将区域码修改为CN，在修改前请确保已关闭DevEco Studio。

在C:\Users\\_username\_\AppData\Roaming\Huawei\DevEcoStudio4.1\options路径下（MacOS 路径为/Users/\_username\_/Library/Application Support/Huawei/DevEcoStudio4.1/options），打开country.region.xml文件，将countryregion name修改为“CN”。

```
1. <application>
2. <component name="CountryRegionSetting">
3. <countryregion name="CN"/>
4. </component>
5. </application>
```
