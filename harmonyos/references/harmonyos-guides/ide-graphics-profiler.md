---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-graphics-profiler
title: GPU帧捕获工具：Graphics Profiler抓帧入口
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > GPU帧捕获工具：Graphics Profiler抓帧入口
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9b6e07b8cafc4154881a303ec437399e2abd6884f1c5b4e3fc65e84b2d63b0f4
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/4xsjZXC1SQKTtaxP2M0tVg/zh-cn_image_0000002808767081.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=5949DED973101660B20443C9E627DCB9EEFBC56E1ACAD0C397A5509C93355232)
4. 在帧捕获界面拉起应用，成功建立连接后，Capture按钮点亮。设置抓帧数量，点击Capture按钮，等待帧捕获完成。
   * Scope：不可修改，默认为Frame。
   * Count：抓帧数量设置，范围为1-10帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/hOljO_6FTW2isDl0yYDBJA/zh-cn_image_0000002779407526.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BF081AB63DEA35AF8D5BA69AD090EEECD0A4CE4041D0DECF56E497080F5EBF6)
5. 抓帧完成后，在下方显示界面中选择一条捕获帧，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ZYDYBxthTVKVDW0CgeJzmQ/zh-cn_image_0000002779567504.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=61C69D8013C3C49CA49BDD130442CCF1D7FBEEB0B0A55F8B6FB00E4387A36540)按钮，可自动打开Graphics Profiler工具解析捕获帧信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/sdBUD_HET6CgflN0dkj7jQ/zh-cn_image_0000002808887167.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4CC160379E3CA9A6A48E0C17C20B4B49B2E608DA9A1D5CE60BBD2980A471FB2 "点击放大")

   **说明** 

   * 抓帧文件名格式为：[应用包名] \_ [抓帧时间] \_frame [帧号].rdc。
   * Graphics Profiler工具一次只能解析一个rdc文件。
6. 若首次使用，需根据界面提示下载Graphics Profiler执行工具，并在菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Tools > Graphics Profiler**中配置工具路径。默认路径为：工具安装路径/frame\_profiler/FrameProfiler.exe（macOS中为工具安装路径/Contents/MacOS/FrameProfiler）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/22aIwAIyQQWWlUg0qcP3Iw/zh-cn_image_0000002779567502.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8A4A830C7FD962B858A486DBABF30E9C7E5D7A8823EA41C4D6F0FD6D90209D1)
