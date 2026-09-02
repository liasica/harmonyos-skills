---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-190
title: "历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\\yyy\\zzz\\D:’/ 'C:xxx\\yyy\\zzz\\C:at Object.mkdirSync (node:fs:1391:3)”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 历史问题报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\\yyy\\zzz\\D:’/ 'C:xxx\\yyy\\zzz\\C:at Object.mkdirSync (node:fs:1391:3)”"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:0157560474f26a3b963d8400e64f468050b0239ce15e660b6a54f64ba9c08070
---

**问题现象**

构建报错：“hvigor ERROR: Error: EINVAL: invalid argument, mkdir ‘D:xxx\yyy\zzz\D:’”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vkBfLvJJRJK92r0qC9D9iQ/zh-cn_image_0000002624478718.png)

**常见错误场景**

工程A通过引用外部模块的方式使用了工程B中的har模块，在工程B中执行ohpm后，在工程A中没有重新执行ohpm install直接编译（或者调试），导致编译报错。

**问题原因**

ohpm远程第三方包安装后，软连接指向的路径为非本工程路径（是由于被其他工程篡改），编译时会出现预期之外的错误。注：能以非本工程路径存在的依赖仅为本地模块，参考官网工程外模块的使用方式）

**解决措施**

1.**在问题工程中重新执行ohpm install**，或者sync。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ZauxxPz6Q52pD2nIAQBp0w/zh-cn_image_0000002654838035.png "点击放大")

2.使用build菜单先进行构建，再调试运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/l-ACCqUpT7K5LElCMkUXRg/zh-cn_image_0000002624478722.png "点击放大")
