---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-15
title: 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:670afdea952a1eac1b87189040bfc83ec66ff915011e29133440cfc5e3b242ad
---

**问题描述**

Windows系统使用DevEco Studio时，SDK卸载失败，提示错误信息。

Unable to rename the file. Cause: Unable to delete D:\\xxx\\default.

**解决方案**

1、启动任务管理器。

2、切换到“性能”选项卡。

3、点击下方“打开资源监视器”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/sE9ulItBQV6I3A_ls6U3WA/zh-cn_image_0000002194158616.png?HW-CC-KV=V1&HW-CC-Date=20260428T002857Z&HW-CC-Expire=86400&HW-CC-Sign=DCF3EA8937F0C9DA773B2BF71B5EF1C5C9243C3423B7D2B6BE0663038D8D2233)

4、将路径 D:\xxx\default 粘贴到关联句柄窗口右侧的搜索栏中，按回车键搜索占用的进程，然后结束该进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/YdDJajzDSXa_PJEjRfw2Dw/zh-cn_image_0000002229758493.png?HW-CC-KV=V1&HW-CC-Date=20260428T002857Z&HW-CC-Expire=86400&HW-CC-Sign=1AF289640694169BB1C0B7B884F7276BFC0B1449F9AFC4F0A5D707A6DC7759B7)
