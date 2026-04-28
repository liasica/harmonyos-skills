---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-4
title: 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”
breadcrumb: FAQ > DevEco Studio > 工程管理 > 打开历史工程，报错提示“Install failed FetchPackageInfo: hypium failed”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4d05fe7dca76806c01e28b74bc449243c4ec198ee2cb2a33d77ccbc9a0190f52
---

**问题现象**

在DevEco Studio打开历史工程，依赖安装不成功，报错信息为“Install failed FetchPackageInfo: hypium failed”。

**解决措施**

导致该问题的原因是包名使用错误。在工程级**oh-package.json5**中，将**devDependencies**字段下"hypium"修改为"@ohos/hypium"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WLUAF9O3SEmoCHRAzPiddA/zh-cn_image_0000002194158560.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=74C85175384B562586B9922850F189D88A0EFBFB61FF2EEF1B8C8D4C52A90A4A)

@ohos/hypium版本号可通过ohpm命令获取，在DevEco Studio中打开Terminal，输入**ohpm info @ohos/hypium**命令，输出结果中dist-tags下方即为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/JUXovj1CSqa1Z818ez9YkQ/zh-cn_image_0000002402257997.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=0100F5652468B5513C9FDF77F230AFBF869DFF361C6F30604D239259358D2E2E)
