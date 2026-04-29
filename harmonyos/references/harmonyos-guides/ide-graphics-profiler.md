---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-graphics-profiler
title: GPU帧捕获工具：Graphics Profiler抓帧入口
breadcrumb: 指南 > 优化应用性能 > 附录 > GPU帧捕获工具：Graphics Profiler抓帧入口
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c7251d959cc65456abb7c02511ca775a206337f1f7fc6908c8b9a500c03a22ee
---

Graphics Profiler（图形性能调优）是专为GPU分析和优化提供的一种调试分析解决方案，可帮助OpenGL ES游戏或Vulkan游戏提升性能，分析绘制和计算问题。从DevEco Studio 6.0.0 Beta1版本开始，提供Graphics Profiler工具的抓帧入口，该工具用于对HarmonyOS手机设备进行调试，需使用调试证书。

## 操作步骤

1. 将需要分析的使用OpenGL ES或Vulkan API接口开发的应用推送到设备，并确认应用完成安装。
2. 在DevEco Studio顶部菜单栏中点击View > Tool Windows > Graphics Profiler进入帧捕获页面。
3. 在帧捕获页面，可配置Ref All Resources和Verify Buffer Access两个参数，配置完成后点击Launch APP拉起应用。
   * Ref All Resources：默认关闭，在打开此选项后，抓帧时捕获所有活动资源，无论抓取的这一帧是否使用活动资源，都保存在Trace中。
   * Verify Buffer Access：默认关闭，设置校验Buffer是否可以访问。

   此处为可选配置，不配置也可直接点击Launch APP拉起应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/CE6m-9QeTZSYQiqAHN7Ytw/zh-cn_image_0000002561753539.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=C08842576D6709FE47E621D2CE33CF95979A67ADA1491A4C6BCF68F96FEA639D)
4. 在帧捕获界面拉起应用，成功建立连接后，Capture按钮点亮。设置抓帧数量，点击Capture按钮，等待帧捕获完成。
   * Scope：不可修改，默认为Frame。
   * Count：抓帧数量设置，范围为1-10帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ru236RxXSYOChvfb3oZY5Q/zh-cn_image_0000002530913596.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=910D5D48A67A258FCC50A73BF3E8F4368C113A5964E8E5D9671839683A577895)
5. 当抓帧完成，在下方显示界面中选择一条捕获帧，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/rc2a0vQqTk6S9Wr8GmEMDQ/zh-cn_image_0000002530753608.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=8504EF79BD598E741F408B4A1102174D52F35606309A4F00F2C19CC25B17C031)按钮，可自动打开Graphics Profiler工具解析捕获帧信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/1ohkvelKQBGxbbeGWpLwrg/zh-cn_image_0000002530913598.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=737332291FBEEAAF1B97ACA80701D500D5C460A0C20E22CE88EAD7E222F3B4F3 "点击放大")

   说明

   * 抓帧文件名格式为：[应用包名] \_ [抓帧时间] \_frame [帧号].rdc。
   * Graphics Profiler工具一次只能解析一个rdc文件。
6. 若首次使用，需根据界面提示下载Graphics Profiler执行工具，并在菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Tools > Graphics Profiler**中配置工具路径。默认路径为：工具安装路径/frame\_profiler/FrameProfiler.exe（macOS中为工具安装路径/Contents/macOS/FrameProfiler）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ujm9Vk4xT7qEzQQhiPL9dQ/zh-cn_image_0000002561753537.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=09570062A8C686F37F54D9A5F4880EC52BB8DF69FFAA5925CCA3A4C7BA8B0B89)
