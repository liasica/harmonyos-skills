---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-4
title: 下载HarmonyOS SDK时提示网络连接错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 下载HarmonyOS SDK时提示网络连接错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:76e05c2238a53ebf4205197c65e1cceefc2ac213f8de8be530c1d9d3ba017059
---

**问题现象**

网络连接正常，但下载HarmonyOS SDK时提示网络连接错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/inNTn09oRD-h5hJw6ZgTEw/zh-cn_image_0000002654797765.png)

**解决措施**

由于使用的PC系统语言为英文且区域码为US，可能导致问题。请按照以下步骤将区域码修改为CN，在修改前请确保已关闭DevEco Studio。

在C:\Users\\_username\_\AppData\Roaming\Huawei\DevEcoStudio4.1\options路径下（MacOS 路径为/Users/\_username\_/Library/Application Support/Huawei/DevEcoStudio4.1/options），打开country.region.xml文件，将countryregion name修改为“CN”。

```xml
<application>
    <component name="CountryRegionSetting">
        <countryregion name="CN"/>
    </component>
</application>
```
