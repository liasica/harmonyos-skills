---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-21
title: 编译报错“Failed to generate test project build system”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to generate test project build system”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4a442bf8c22e4cd437cf0b2257f624ea7359a8967612fec70da8641a5395ee28
---

**问题现象**

执行多模块Native模块构建时，出现“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/NOexis7LTl-GgwfG-8ttzw/zh-cn_image_0000002624638396.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DF689AE62B317FC98B91DF9EC01FB8AA3AE2478BE550A15D8AC367181CABE81)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行Make Module {moduleName}完成单独构建。注意：此方案需避免多模块并行构建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/BvOqyucfRCSc8xDR12eEpA/zh-cn_image_0000002654837805.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=046CC220418FB296F121FD9F051B2452237A4893E0644D3A5EC55934FED78CF1)
