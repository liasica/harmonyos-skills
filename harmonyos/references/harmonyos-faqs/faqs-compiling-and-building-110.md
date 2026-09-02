---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-110
title: 构建报错“input module releaseType is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“input module releaseType is different”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9efceab0e8f5037536cabdb94217dd598059358397049d3754199bd0a4fdb1a2
---

**问题现象**

在打包APP时，如果提示“input module releaseType is different”，请检查输入模块的发布类型是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/f8aH7X-ATbW4IpwhsKhPMw/zh-cn_image_0000002194318432.png)

**解决措施**

根据报错日志中的Warning信息提示的模块名称，检查模块间的apiReleaseType字段是否一致。

apiReleaseType字段由编译构建工具自动生成并保存在HAP/HSP包的module.json文件中。请确认各模块间该字段是否一致。如果存在不一致，需使用相同版本的SDK重新打包应用的各个模块，然后重新打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/wlfxYrEPRyGKARP4fmzc5w/zh-cn_image_0000002229604205.png)
