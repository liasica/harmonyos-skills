---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-12
title: 编辑功能失效，提示“ArkTS language service terminated due to memory constraints.”
breadcrumb: FAQ > DevEco Studio > 代码编辑 > 编辑功能失效，提示“ArkTS language service terminated due to memory constraints.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:854e15998b558dae7c6385e2469d14268673f317651824c7ae45c881cd2682ac
---

**问题现象**

场景1：多次执行git pull或切分支等大量修改代码的操作时，编辑器的Node进程内存峰值超过上限（默认为8GB），来不及回收内存导致OOM，编辑功能失效，弹窗提示“ArkTS language service terminated due to memory constraints.”。

场景2：编辑器启动时会扫描工程代码，当开发的工程代码量超过一定大小时，可能导致编辑器的Node进程超出内存上限（默认为8GB），从而导致编辑器启动失败，提示“Scan files to index fail”。

**解决措施**

可以调整编辑器Node进程的内存上限来解决上述问题，请根据工程代码量和开发环境内存大小配置合适的Node进程内存上限。内存上限值需要随工程的代码量和复杂程度增长，通常代码量300万行的工程建议配置大于12G，400万行建议配置大于15G，每增加100万行增加3G，可根据具体情况适当增减。

以配置内存上限为12G举例，打开DevEco Studio，通过菜单栏的Help > Edit Custom Properties...，打开idea.properties配置文件。在文件中新增一行 arkts.server.max.old.space.size=12288，然后重启DevEco Studio。编辑器Node进程的内存上限将设置为12288M（即12G）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/X8tw0dnvQX6okw4Vx3_LWA/zh-cn_image_0000002412101125.png?HW-CC-KV=V1&HW-CC-Date=20260429T062014Z&HW-CC-Expire=86400&HW-CC-Sign=BD5EDB00D718418C82A0A710FB35DF0CB4CB071064AA45B72428D1D625A06932)
