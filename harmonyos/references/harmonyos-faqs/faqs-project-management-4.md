---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-4
title: "打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”"
breadcrumb: "FAQ > DevEco Studio > 工程管理 > 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:49+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:113cbd4b981e7c31266348e872c6f3c3ede9e98ab1cca5587706576140077baa
---

**问题现象**

在DevEco Studio打开历史工程，依赖安装不成功，报错信息为“Install failed FetchPackageInfo: hypium failed”。

**解决措施**

导致该问题的原因是包名使用错误。在工程级**oh-package.json5**中，将**devDependencies**字段下"hypium"修改为"@ohos/hypium"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/1AKbBeEvQra69tMx7euNrQ/zh-cn_image_0000002654837735.png)

@ohos/hypium版本号可通过ohpm命令获取，在DevEco Studio中打开Terminal，输入**ohpm info @ohos/hypium**命令，输出结果中dist-tags下方即为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/R0UcvEYxT4-7Ly1--nbh7g/zh-cn_image_0000002624478424.png)
