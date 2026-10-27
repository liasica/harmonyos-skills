---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-39
title: Windows电脑上启动模拟器，提示可申请内存不足
breadcrumb: FAQ > DevEco Studio > 应用运行 > Windows电脑上启动模拟器，提示可申请内存不足
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4423b04f050332d79a9712d3a4181eafc2ad05f03b63b8228768a77fc3f977a5
---

**问题现象**

启动模拟器时，如果系统提示“当前可申请的内存不足”，表示Windows电脑内存不足。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/si4EzdmyRc6_d8ToVVLW0g/zh-cn_image_0000002624638676.png)

**解决措施**

1. 打开任务管理器的详细信息页面，在列表表头右键选择列，勾选“提交大小”，然后点击“提交大小”列进行排序，关闭提交大小占用高的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Y9eiXx8wRRK4bemRzLK1rA/zh-cn_image_0000002624478768.png "点击放大")
2. 打开任务管理器的性能和内存页面，确保已提交内存的剩余量大于模拟器设置的RAM大小。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/bdWZ_TqURq21kT4bKyy_hw/zh-cn_image_0000002624638678.png)
