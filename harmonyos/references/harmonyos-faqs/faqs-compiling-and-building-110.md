---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-110
title: 构建报错“input module releaseType is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“input module releaseType is different”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:58efde1ed0b18a82b8cd46ac7bff5b7b91a4720f70279da2d1244890364b6369
---

**问题现象**

在打包APP时，如果提示“input module releaseType is different”，请检查输入模块的发布类型是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/f8aH7X-ATbW4IpwhsKhPMw/zh-cn_image_0000002194318432.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=99075F53B0B65AAF7FA3A53FD9067B600151A54AA855E6304AC9446CA93FBB5E)

**解决措施**

根据报错日志中的Warning信息提示的模块名称，检查模块间的apiReleaseType字段是否一致。

apiReleaseType字段由编译构建工具自动生成并保存在HAP/HSP包的module.json文件中。请确认各模块间该字段是否一致。如果存在不一致，需使用相同版本的SDK重新打包应用的各个模块，然后重新打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/wlfxYrEPRyGKARP4fmzc5w/zh-cn_image_0000002229604205.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=3A9A60D172B79689BB8224E1B02874EF85CA6808A08ABDA11830EC3B595B9FBC)
