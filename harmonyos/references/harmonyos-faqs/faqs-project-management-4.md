---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-4
title: 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”
breadcrumb: FAQ > DevEco Studio > 工程管理 > 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2c6c4acb99db2ca67be1c58ddb5cee1b8b87cfac5f3a0a69a5e7d5a041e2ec0f
---

**问题现象**

在DevEco Studio打开历史工程，依赖安装不成功，报错信息为“Install failed FetchPackageInfo: hypium failed”。

**解决措施**

导致该问题的原因是包名使用错误。在工程级**oh-package.json5**中，将**devDependencies**字段下"hypium"修改为"@ohos/hypium"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WLUAF9O3SEmoCHRAzPiddA/zh-cn_image_0000002194158560.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=1CDB2671CD95D22D2E6B6C3DF7A608A7B3FA82F23FA0218E108E1C8617B3E9A3)

@ohos/hypium版本号可通过ohpm命令获取，在DevEco Studio中打开Terminal，输入**ohpm info @ohos/hypium**命令，输出结果中dist-tags下方即为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/JUXovj1CSqa1Z818ez9YkQ/zh-cn_image_0000002402257997.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=6C07D4BFF11C6260C03BC189868BD26B0AA1A7B98F44F7090DE720A491201C98)
