---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-110
title: 构建报错“input module releaseType is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“input module releaseType is different”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:6f601ce254211afd3c5b787ca29f553ad5d11c43919947cd4f94759a76156582
---

**问题现象**

在打包APP时，如果提示“input module releaseType is different”，请检查输入模块的发布类型是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/xS6Om8R_RPuBiUUGLQWVWw/zh-cn_image_0000002654837859.png)

**解决措施**

根据报错日志中的Warning信息提示的模块名称，检查模块间的apiReleaseType字段是否一致。

apiReleaseType字段由编译构建工具自动生成并保存在HAP/HSP包的module.json文件中。请确认各模块间该字段是否一致。如果存在不一致，需使用相同版本的SDK重新打包应用的各个模块，然后重新打包APP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/YykKEf2gS3qaZnnNmYCqtw/zh-cn_image_0000002624478548.png)
