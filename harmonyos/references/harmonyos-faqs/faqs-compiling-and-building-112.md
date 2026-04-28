---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-112
title: 构建报错“proxy data is duplicated”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“proxy data is duplicated”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:84640e32e569e9d00a25be81ad12387fd6942642ce864cf53eea39f9cdda1d75
---

**问题现象**

打包APP时，出现“uri datashareproxy://bundleName/\*\* in proxy data is duplicated”的提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/0BxP415uTLO6H6A8lDNKzQ/zh-cn_image_0000002229758777.png?HW-CC-KV=V1&HW-CC-Date=20260428T002930Z&HW-CC-Expire=86400&HW-CC-Sign=E14ECDD56F5F30DBC76DBDC095E9FE8A7E9B8969C5BAD3391C4C3AC919F92BA0)

**解决措施**

proxyData 标识模块提供的数据代理列表，仅允许 entry 和 feature 配置，不同 proxyData 中配置的 URI 不得重复。遇到此问题，检查模块间是否配置了相同的 URI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/4sh21Y2DQjaggsYMaeNjUw/zh-cn_image_0000002194158904.png?HW-CC-KV=V1&HW-CC-Date=20260428T002930Z&HW-CC-Expire=86400&HW-CC-Sign=708397BBB075B44ED321E9DE027FC5C8B84E3324DE78F88CD071CE53738D1B71)
