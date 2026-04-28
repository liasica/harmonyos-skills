---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-24
title: 打开工程时左侧目录树不显示
breadcrumb: FAQ > DevEco Studio > 工程管理 > 打开工程时左侧目录树不显示
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:00+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:b174aa95c6d61a51770137975f7cad21c47b6483815347c1854e74e0952d101c
---

**问题现象**

左侧目录树不显示，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/rxRUZsbHQOmGbkjjHc7Myg/zh-cn_image_0000002583384877.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=73282723910D7D2FFAE48A460E22BA1FA17F20714887754782677B55F15A748C)

**问题原因**

**情况1：**

在 macOS上，系统对隐私权限的管理非常严格。如果没有获得访问特定目录（如“下载”或“桌面”）的权限，就会出现项目虽然打开了，但左侧目录树一片空白的情况。

**情况2：**

当用户删除工程目录下的.idea/modules文件夹或者.idea/modules文件夹不存在时，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/htpUljIXTCKqWyO8DXqWBA/zh-cn_image_0000002552745208.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=2C0C44F59ADD895D90BDED7921634C66496E992EDF41AE1C49741F77136889F4)

由于modules文件夹下的iml文件定义了详细的工程模块结构信息，modules.xml定义了工程模块结构文件的位置。删除modules文件夹后根据modules.xml无法找到对应的iml文件。

**解决措施**

**情况1：**

如果缺少访问权限，设置项目文件夹访问权限就可以解决问题：系统设置->隐私与安全->文件和文件夹->允许访问（找到DevEco Studio，点击展开），重启IDE，工程目录树才可以恢复

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Nbj_iuhqQyGD4Y8jYO1PNA/zh-cn_image_0000002583305609.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=79E98356C8F922A3723973087935C51F29803EBF9292696A90DA5B6EB13EA7C3)

**情况2：**

需要关闭工程，在文件管理器中删除工程的modules.xml，重新启动IDE打开工程，工程目录树才可以恢复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/fIoZw-F2T8Wq2uDCRd0LzQ/zh-cn_image_0000002583385109.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=4F7257837C9428C5AB827D252697B0F55750310B7F6EDBD17D48E34ECEBF71CE)
