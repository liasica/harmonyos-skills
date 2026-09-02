---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-37
title: "构建报错“ERROR: Task xxx was not found in the project xxx”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 构建报错“ERROR: Task xxx was not found in the project xxx”"
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:28+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:33b1bc98582ed9192dde7363d8019d899f09564d2dc69f546ad3295791ce588a
---

**问题现象**

命令行手动执行构建命令时，如果构建失败并提示“ERROR: Task xxx was not found in the project xxx”，请检查以下内容：

- 确认任务名称是否正确。

- 确认项目中是否包含该任务。

- 确认项目路径是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/p8yNuI9sR1Gz7PIgRMJSRA/zh-cn_image_0000002194318376.png)

**问题确认**

1. 执行hvigor tasks命令，查看该命令是否存在。
2. 查看对应工程中module.json5文件中“type”字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的“type”字段不是"har"类型，则会出现上述错误提示。

**解决措施**

1. 执行正确命令。
2. 查看工程中 module.json5 文件的“type”字段，执行相应命令。
