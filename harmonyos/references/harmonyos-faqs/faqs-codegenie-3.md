---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-3
title: CodeGenie偶现报错：The reasoning_content in the thinking mode must be passed back to the API.
breadcrumb: FAQ > DevEco Studio > AI辅助编程 > CodeGenie偶现报错：The reasoning_content in the thinking mode must be passed back to the API.
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:581eb713e799882d4cf17cc24614d5d92040543476efbe5a73e5e663318c70fd
---

**问题现象**

DevEco Studio 6.1.0 Release（6.1.0.850）及以上版本，在CodeGenie中通过URL方式配置deepseek-v4模型后，过程中界面提示“The reasoning\_content in the thinking mode must be passed back to the API.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/uVUDTN2wQvGdmJkGjTEneg/zh-cn_image_0000002624478830.png?HW-CC-KV=V1&HW-CC-Date=20261112T233205Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6F98E38B86FBE08BB20D3C080CA0232734BAFEB302F465049BA774C7F570D45 "点击放大")

**解决措施**

使用Service Provider（服务提供商）方式配置模型，并在使用过程中打开深度思考。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Y6HldpvjR5-m1afD2iISqw/zh-cn_image_0000002654798195.png?HW-CC-KV=V1&HW-CC-Date=20261112T233205Z&HW-CC-Expire=31536000000&HW-CC-Sign=35F4CD66CCD3C64D4970D575A0FB4434BCFED1E493B5A63EC542D92A99E0C552 "点击放大")
