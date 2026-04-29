---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-15
title: 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:11+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:fb251e7da3955a0cb7d95bdd1e440a26d21fe486d9fae44383357ddab2ed582a
---

**问题描述**

Windows系统使用DevEco Studio时，SDK卸载失败，提示错误信息。

Unable to rename the file. Cause: Unable to delete D:\\xxx\\default.

**解决方案**

1、启动任务管理器。

2、切换到“性能”选项卡。

3、点击下方“打开资源监视器”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/sE9ulItBQV6I3A_ls6U3WA/zh-cn_image_0000002194158616.png?HW-CC-KV=V1&HW-CC-Date=20260429T062009Z&HW-CC-Expire=86400&HW-CC-Sign=EFA883583690440176E9BC62617C4A13767AC9D95E3226064FE1D3FDF8AE0A08)

4、将路径 D:\xxx\default 粘贴到关联句柄窗口右侧的搜索栏中，按回车键搜索占用的进程，然后结束该进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/YdDJajzDSXa_PJEjRfw2Dw/zh-cn_image_0000002229758493.png?HW-CC-KV=V1&HW-CC-Date=20260429T062009Z&HW-CC-Expire=86400&HW-CC-Sign=5F0451B83DAC04CF24798374C6C839F90CA4D7C58DEA399CCB87759AC6EAB48C)
