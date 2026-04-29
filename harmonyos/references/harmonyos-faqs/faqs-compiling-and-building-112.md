---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-112
title: 构建报错“proxy data is duplicated”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“proxy data is duplicated”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b6ae744af6cdf806cde8f1f2e3b1a3e5d58e2103ae6718de38faf492321e97d2
---

**问题现象**

打包APP时，出现“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”的提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/0BxP415uTLO6H6A8lDNKzQ/zh-cn_image_0000002229758777.png?HW-CC-KV=V1&HW-CC-Date=20260429T062043Z&HW-CC-Expire=86400&HW-CC-Sign=C959394204183C5FFEF9B9E7A017FC1D5FA4AF88757D41CF8B8ABB6902CAA92F)

**解决措施**

proxyData 标识模块提供的数据代理列表，仅允许 entry 和 feature 配置，不同 proxyData 中配置的 URI 不得重复。遇到此问题，检查模块间是否配置了相同的 URI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4sh21Y2DQjaggsYMaeNjUw/zh-cn_image_0000002194158904.png?HW-CC-KV=V1&HW-CC-Date=20260429T062043Z&HW-CC-Expire=86400&HW-CC-Sign=396BCA4D2346D683098748FD3AB5F001D2303704286BD8AD4F1B14664B187FAD)
