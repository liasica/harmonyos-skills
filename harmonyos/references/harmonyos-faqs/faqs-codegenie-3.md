---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-3
title: CodeGenie偶现报错：The reasoning_content in the thinking mode must be passed back to the API.
breadcrumb: FAQ > DevEco Studio > AI辅助编程 > CodeGenie偶现报错：The reasoning_content in the thinking mode must be passed back to the API.
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:083cfdbd60603eb81273c70adbafb3184d3ea5f288565911cc648c883f1eae83
---

**问题现象**

DevEco Studio 6.1.0 Release（6.1.0.850）及以上版本，在CodeGenie中通过URL方式配置deepseek-v4模型后，过程中界面提示“The reasoning\_content in the thinking mode must be passed back to the API.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/PiTLDhxPQf6peM-APggPVA/zh-cn_image_0000002624478830.png "点击放大")

**解决措施**

使用Service Provider（服务提供商）方式配置模型，并在使用过程中打开深度思考。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/9gezK6GQSbaJDcW1QPVs9g/zh-cn_image_0000002654798195.png "点击放大")
