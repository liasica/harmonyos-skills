---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-39
title: Windows电脑上启动模拟器，提示可申请内存不足
breadcrumb: FAQ > DevEco Studio > 应用运行 > Windows电脑上启动模拟器，提示可申请内存不足
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d5e44e4b5763ccf13481279d8f0f62590f8039515921cc29f29ab7977201f385
---

**问题现象**

启动模拟器时，如果系统提示“当前可申请的内存不足”，表示Windows电脑内存不足。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/QtPs78WnQ1Cb7a55Qe9ItA/zh-cn_image_0000002229604313.png?HW-CC-KV=V1&HW-CC-Date=20260429T062119Z&HW-CC-Expire=86400&HW-CC-Sign=3837358462BA3DEFC62FA68DB98D8A58ECB82AFF42E49CBA01CB87DA29FCB6A6)

**解决措施**

1. 打开任务管理器的详细信息页面，在列表表头右键选择列，勾选“提交大小”，然后点击“提交大小”列进行排序，关闭提交大小占用高的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/ls0CcoD5R5WV-8Wib1Yt_A/zh-cn_image_0000002229758817.png?HW-CC-KV=V1&HW-CC-Date=20260429T062119Z&HW-CC-Expire=86400&HW-CC-Sign=7C845B7EB09C293A88078EEA5A1827AF581BB7678E2329B7A30DCB687AB67F61 "点击放大")
2. 打开任务管理器的性能和内存页面，确保已提交内存的剩余量大于模拟器设置的RAM大小。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/HneqbFoNRbq3xCZUkRnNRg/zh-cn_image_0000002194158932.png?HW-CC-KV=V1&HW-CC-Date=20260429T062119Z&HW-CC-Expire=86400&HW-CC-Sign=3B94143654DC9B3042E98D1CB6E285EB9F14972033E26FC9439C6B28D905D825)
