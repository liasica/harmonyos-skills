---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-111
title: 构建报错“debug is different”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错“debug is different”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:05305b9c48c50ba20c89c09722e2cc7e2ac22ade05c6bd41ff6d90db7e77c339
---

**问题现象**

打包应用时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Dwf2EfkgRruISZ-sdoNwzw/zh-cn_image_0000002654797907.png)

**解决措施**

根据报错日志的Warning信息提示的模块名称，检查模块间的debug字段是否一致，重点关注本地模块与外部引用模块。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/2LbETFjMTmOA64r1uEzFlA/zh-cn_image_0000002624638456.png)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/FCgr3-SEQVeHfM-GC94wuw/zh-cn_image_0000002654837897.png)
