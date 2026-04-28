---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-111
title: 构建报错“debug is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“debug is different”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6aeedb6860d345c20675604c31413cbc34fba1e3ff4ae6eaf9215d1b9e1db588
---

**问题现象**

打包应用时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/EYkUziPXSwiQjeQ3BYFGJA/zh-cn_image_0000002229758605.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=8EB2815489AD799044756ADA4E9CCE5CF2D5362142A3BB30E05B0F55CD0002BD)

**解决措施**

根据报错日志的Warning信息提示的模块名称，检查模块间的debug字段是否一致，重点关注本地模块与外部引用模块。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/wMddO0fcSVSG4ybBa74FBQ/zh-cn_image_0000002229604117.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=E60BCC3F1F6D8694AE45B4F754134A4C44F6D3594A66E606E9A800243B03942C)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/q7Xj_-trSeeGuAw5ssDfNQ/zh-cn_image_0000002194318344.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=80527DF086FFCB1C32B965490D04AB1FC98BA899BB1347A760CDD2A4053BD495)
