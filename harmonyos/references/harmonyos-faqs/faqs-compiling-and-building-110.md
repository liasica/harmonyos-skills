---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-110
title: 构建报错“input module releaseType is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“input module releaseType is different”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4576ba90b9af35264baa8a00403d1e634bcfa6e40707e770bf84040eb7ee8957
---

**问题现象**

在打包APP时，如果提示“input module releaseType is different”，请检查输入模块的发布类型是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/f8aH7X-ATbW4IpwhsKhPMw/zh-cn_image_0000002194318432.png?HW-CC-KV=V1&HW-CC-Date=20260429T062042Z&HW-CC-Expire=86400&HW-CC-Sign=A603351674EF9B18046393815BBF8BF49A66A38FF70F9D0AB3A6A792AF7B14BA)

**解决措施**

根据报错日志中的Warning信息提示的模块名称，检查模块间的apiReleaseType字段是否一致。

apiReleaseType字段由编译构建工具自动生成并保存在HAP/HSP包的module.json文件中。请确认各模块间该字段是否一致。如果存在不一致，需使用相同版本的SDK重新打包应用的各个模块，然后重新打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/wlfxYrEPRyGKARP4fmzc5w/zh-cn_image_0000002229604205.png?HW-CC-KV=V1&HW-CC-Date=20260429T062042Z&HW-CC-Expire=86400&HW-CC-Sign=DC6F75ABFB82D50FD47E2C602B90AF75E5DABDFF99DB48F23BA12E935DDE0E11)
