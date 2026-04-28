---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-39
title: Windows电脑上启动模拟器，提示可申请内存不足
breadcrumb: FAQ > DevEco Studio > 应用运行 > Windows电脑上启动模拟器，提示可申请内存不足
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:60372023f6231caf872f42a54b2f2994a77d333c75d5cd1388bd99b1583a2274
---

**问题现象**

启动模拟器时，如果系统提示“当前可申请的内存不足”，表示Windows电脑内存不足。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/QtPs78WnQ1Cb7a55Qe9ItA/zh-cn_image_0000002229604313.png?HW-CC-KV=V1&HW-CC-Date=20260428T003001Z&HW-CC-Expire=86400&HW-CC-Sign=5FBCB8C3E0B3640CB365E85B0900C6E7DF02831637F7E1A32B4708E36DC7749D)

**解决措施**

1. 打开任务管理器的详细信息页面，在列表表头右键选择列，勾选“提交大小”，然后点击“提交大小”列进行排序，关闭提交大小占用高的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/ls0CcoD5R5WV-8Wib1Yt_A/zh-cn_image_0000002229758817.png?HW-CC-KV=V1&HW-CC-Date=20260428T003001Z&HW-CC-Expire=86400&HW-CC-Sign=26A8C936BEA5FCCD51793232F21CE84B155C3491D6F2940DDD61DD3E5FB00B49 "点击放大")
2. 打开任务管理器的性能和内存页面，确保已提交内存的剩余量大于模拟器设置的RAM大小。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/HneqbFoNRbq3xCZUkRnNRg/zh-cn_image_0000002194158932.png?HW-CC-KV=V1&HW-CC-Date=20260428T003001Z&HW-CC-Expire=86400&HW-CC-Sign=18E23C9ADCE11604D7CEDEEEB2133DBCC26F8B1BE4B7E715E8D1853622A8B961)
