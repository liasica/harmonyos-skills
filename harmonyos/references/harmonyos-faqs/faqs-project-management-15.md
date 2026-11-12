---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-15
title: 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何解决Windows系统使用DevEco Studio时SDK卸载失败，报“Unable to rename the file. Cause:Unable to delete D:\xxx\default”错误
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:9bcbac2617423077f0fd2c4a45082b328a26b9edb9f83a0addd06a92d15746c5
---

**问题描述**

Windows系统使用DevEco Studio时，SDK卸载失败，提示错误信息。

Unable to rename the file. Cause: Unable to delete D:\\xxx\\default.

**解决方案**

1、启动任务管理器。

2、切换到“性能”选项卡。

3、点击下方“打开资源监视器”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/UxYDZZ1BSVaOogGQG7nHew/zh-cn_image_0000002624638340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC60478F2C9FEACAFC51DB0552AC198B04B36DB46332C6B48A215002276B32E8)

4、将路径 D:\xxx\default 粘贴到关联句柄窗口右侧的搜索栏中，按回车键搜索占用的进程，然后结束该进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VvN4o-pBTOO4X2cbS4Iceg/zh-cn_image_0000002654837745.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=444DA048060664444DE2DDF3CADF1CC31F2557E0B1DCB32F24E2FA9C9FE613F6)
