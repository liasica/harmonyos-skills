---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-37
title: "构建报错“ERROR: Task xxx was not found in the project xxx”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 构建报错“ERROR: Task xxx was not found in the project xxx”"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:111cdde61f6cc8009cb65523d9f32e390e7422de26e3c3aa1dfde362e188b759
---

**问题现象**

命令行手动执行构建命令时，如果构建失败并提示“ERROR: Task xxx was not found in the project xxx”，请检查以下内容：

- 确认任务名称是否正确。

- 确认项目中是否包含该任务。

- 确认项目路径是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/E2l13VViS0ijHbEMN-T0vA/zh-cn_image_0000002624478508.png)

**问题确认**

1. 执行hvigor tasks命令，查看该命令是否存在。
2. 查看对应工程中module.json5文件中“type”字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的“type”字段不是"har"类型，则会出现上述错误提示。

**解决措施**

1. 执行正确命令。
2. 查看工程中 module.json5 文件的“type”字段，执行相应命令。
