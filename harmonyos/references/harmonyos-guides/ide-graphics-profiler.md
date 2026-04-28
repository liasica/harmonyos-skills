---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-graphics-profiler
title: GPU帧捕获工具：Graphics Profiler抓帧入口
breadcrumb: 指南 > 优化应用性能 > 附录 > GPU帧捕获工具：Graphics Profiler抓帧入口
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:37+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0b48a64041ab85a06938916256906dbaa09f64a58de3774587d411fccb68e4f3
---

Graphics Profiler（图形性能调优）是专为GPU分析和优化提供的一种调试分析解决方案，可帮助OpenGL ES游戏或Vulkan游戏提升性能，分析绘制和计算问题。从DevEco Studio 6.0.0 Beta1版本开始，提供Graphics Profiler工具的抓帧入口，该工具用于对HarmonyOS手机设备进行调试，需使用调试证书。

## 操作步骤

1. 将需要分析的使用OpenGL ES或Vulkan API接口开发的应用推送到设备，并确认应用完成安装。
2. 在DevEco Studio顶部菜单栏中点击View > Tool Windows > Graphics Profiler进入帧捕获页面。
3. 在帧捕获页面，可配置Ref All Resources和Verify Buffer Access两个参数，配置完成后点击Launch APP拉起应用。
   * Ref All Resources：默认关闭，在打开此选项后，抓帧时捕获所有活动资源，无论抓取的这一帧是否使用活动资源，都保存在Trace中。
   * Verify Buffer Access：默认关闭，设置校验Buffer是否可以访问。

   此处为可选配置，不配置也可直接点击Launch APP拉起应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/waq32uJyRky1AzRslwJkIQ/zh-cn_image_0000002561753539.png?HW-CC-KV=V1&HW-CC-Date=20260427T235736Z&HW-CC-Expire=86400&HW-CC-Sign=EA77FD3AD682A14E5939EF77F36E9370DE49D8118DBB9F0A4DEAC80A17BD6A9C)
4. 在帧捕获界面拉起应用，成功建立连接后，Capture按钮点亮。设置抓帧数量，点击Capture按钮，等待帧捕获完成。
   * Scope：不可修改，默认为Frame。
   * Count：抓帧数量设置，范围为1-10帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ZxKMoAIIRaSZOLzR0Gu0Nw/zh-cn_image_0000002530913596.png?HW-CC-KV=V1&HW-CC-Date=20260427T235736Z&HW-CC-Expire=86400&HW-CC-Sign=ABDE212055306BDD7E3325C04629EB454009AA48EE4B2835D2795CCB1DE25958)
5. 当抓帧完成，在下方显示界面中选择一条捕获帧，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/AK1ewbOXQq-okzo4EHpTKA/zh-cn_image_0000002530753608.png?HW-CC-KV=V1&HW-CC-Date=20260427T235736Z&HW-CC-Expire=86400&HW-CC-Sign=4F4A4B7D5C5744FCCEE22B443CA47FDF730A57813642192E0B81FEBF466430F6)按钮，可自动打开Graphics Profiler工具解析捕获帧信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/CuOtnehpT8CAmmOS72y9JQ/zh-cn_image_0000002530913598.png?HW-CC-KV=V1&HW-CC-Date=20260427T235736Z&HW-CC-Expire=86400&HW-CC-Sign=03A739C23F2EB13E9F7F7B2D297D597EA667C8F6478919037FC174853A8B179D "点击放大")

   说明

   * 抓帧文件名格式为：[应用包名] \_ [抓帧时间] \_frame [帧号].rdc。
   * Graphics Profiler工具一次只能解析一个rdc文件。
6. 若首次使用，需根据界面提示下载Graphics Profiler执行工具，并在菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Tools > Graphics Profiler**中配置工具路径。默认路径为：工具安装路径/frame\_profiler/FrameProfiler.exe（macOS中为工具安装路径/Contents/macOS/FrameProfiler）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Umj94mrNRhSxvsmSqtedrg/zh-cn_image_0000002561753537.png?HW-CC-KV=V1&HW-CC-Date=20260427T235736Z&HW-CC-Expire=86400&HW-CC-Sign=B661BBF8D61F3C8ABE5904B41C10992AF2E9BB013EE08E0EC89518096DAB7EB9)
