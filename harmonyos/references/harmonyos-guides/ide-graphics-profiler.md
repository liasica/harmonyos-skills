---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-graphics-profiler
title: GPU帧捕获工具：Graphics Profiler抓帧入口
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > GPU帧捕获工具：Graphics Profiler抓帧入口
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bd6a80690e58317726c186f52078b7d61b6eaabe2bbc41d8e57782872797bab8
---

Graphics Profiler（图形性能调优）是专为GPU分析和优化提供的一种调试分析解决方案，可帮助OpenGL ES游戏或Vulkan游戏提升性能，分析绘制和计算问题。从DevEco Studio 6.0.0 Beta1版本开始，提供Graphics Profiler工具的抓帧入口，该工具用于对HarmonyOS手机设备进行调试，需使用调试证书。

## 约束与限制

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 操作步骤

1. 将需要分析的使用OpenGL ES或Vulkan API接口开发的应用推送到设备，并确认应用完成安装。
2. 在DevEco Studio顶部菜单栏中点击View > Tool Windows > Graphics Profiler进入帧捕获页面。
3. 在帧捕获页面，可配置Ref All Resources和Verify Buffer Access两个参数，配置完成后点击Launch APP拉起应用。
   * Ref All Resources：默认关闭，在打开此选项后，抓帧时捕获所有活动资源，无论抓取的这一帧是否使用活动资源，都保存在Trace中。
   * Verify Buffer Access：默认关闭，设置校验Buffer是否可以访问。

   此处为可选配置，配置与否均可直接点击Launch APP拉起应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/dVYbqBLBT-yll5rhY1zALg/zh-cn_image_0000002808767081.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A46C14E5D8369E9C5E71647F2A48A21A2804B7CCDE88CE5B598718250AF35204)
4. 在帧捕获界面拉起应用，成功建立连接后，Capture按钮点亮。设置抓帧数量，点击Capture按钮，等待帧捕获完成。
   * Scope：不可修改，默认为Frame。
   * Count：抓帧数量设置，范围为1-10帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Sf4HLKP8RyWnQlqlPj7BZA/zh-cn_image_0000002779407526.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA718C6AD210FE4ABC55D36933B8A815F9B76AECFF1FE897E997F83E856AB067)
5. 抓帧完成后，在下方显示界面中选择一条捕获帧，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/naHjOklySL6HfBTaWBmmLg/zh-cn_image_0000002779567504.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=110B3C4173B354CF016A08EAB88CE85AD9DE1DC9F85C5FCC8E56B2574BD49E13)按钮，可自动打开Graphics Profiler工具解析捕获帧信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/J6FlNDUvRaSrY6Un9yKLTg/zh-cn_image_0000002808887167.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=229CEB26506FFFB03363EDAFBA571DB2BD6D2C5811D5934ED6C9CB819CFF6807 "点击放大")

   **说明** 

   * 抓帧文件名格式为：[应用包名] \_ [抓帧时间] \_frame [帧号].rdc。
   * Graphics Profiler工具一次只能解析一个rdc文件。
6. 若首次使用，需根据界面提示下载Graphics Profiler执行工具，并在菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Tools > Graphics Profiler**中配置工具路径。默认路径为：工具安装路径/frame\_profiler/FrameProfiler.exe（macOS中为工具安装路径/Contents/MacOS/FrameProfiler）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ZNhLVSEoQciczxnWyt72nw/zh-cn_image_0000002779567502.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFB36F252B9A6991635CD7C68C6815752E5308E2BE097B473F1DDF7CA9554A68)
