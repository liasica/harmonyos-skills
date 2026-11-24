---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e93da7408f8e05eb69f830b52d31191b69cca49035154ead084869ce4daf5344
---

当代码行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/WrzBK2MpTAaMnqUnSWGlJw/zh-cn_image_0000002808887071.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A7168DD66EEFCB95824B7940F02D289DBA8EAB2DEBC84CB643F10FEAD2907D1)按钮或快捷键Shift + F7高亮展示可步入的函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/U1w4JP6VQhiQ7gfMwjndhQ/zh-cn_image_0000002808766987.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=93A665AF32008A63E199DCBA56A1BB8A2FB0714D357350A8FAF44A3E7CD67C6C)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/tuoUqchmT3uxqaOfH-pz3A/zh-cn_image_0000002808766993.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1B0D64BBEDCA4E1C1C4D002091EAD63B9D6C9F7412CADEF774A2B7261B357CD)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Cr4QfkxDS8WWinVQ5qzf7A/zh-cn_image_0000002779567408.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F585D27CE033A18E338764C3398B6C00322C9CC9352EA2A304ED531ADE8D40A)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/i-26-wjXSCqnaQSd7PuZ8g/zh-cn_image_0000002779407434.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A509E146D20CB18DBF898D7B8CD183864D39D35EBB87FD09604F5EB819D9B29)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/XmsPS4w5TfSu49aFDfNrRQ/zh-cn_image_0000002779567414.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B0AAE74306FAC61FEBAB7616763F0F82F4874BB32209136CF104514AA412BA7)
