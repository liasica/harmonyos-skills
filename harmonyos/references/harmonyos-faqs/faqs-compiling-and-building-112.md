---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-112
title: 构建报错“proxy data is duplicated”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“proxy data is duplicated”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9391eec10786d057ae4eaa2ea8d656ca1eff085b45f724fde9302a89e063e280
---

**问题现象**

打包APP时，出现“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”的提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/LYs7NnDoQLWGVl50zESDSA/zh-cn_image_0000002624478596.png)

**解决措施**

proxyData 标识模块提供的数据代理列表，仅允许 entry 和 feature 配置，不同 proxyData 中配置的 URI 不得重复。遇到此问题，检查模块间是否配置了相同的 URI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KAnR_t4ESK6d9AWgN77Iag/zh-cn_image_0000002654797955.png)
