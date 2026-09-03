---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7918bd500b83c4da56922924fdcdd7d9179c0c88674f666dd249382839e105e0
---

当代码行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/8_b8LZxGS6SeD59kcP3afQ/zh-cn_image_0000002731382857.png)按钮或快捷键Shift + F7高亮展示可步入的函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/QKe2SSKNQbuTINowqIEzbA/zh-cn_image_0000002731382859.png)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/y2IfL__VREmfHTqK5XDdaw/zh-cn_image_0000002701663630.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/V4-XYNwRS-uvy85XNHMWoQ/zh-cn_image_0000002701663632.png)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/XUPTRrD2R6mPTJKke7bQTQ/zh-cn_image_0000002701823552.png)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/t5-trR4ZTSKRZ_kjyuuaoA/zh-cn_image_0000002731542829.png)
