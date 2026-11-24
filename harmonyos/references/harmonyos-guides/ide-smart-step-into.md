---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smart-step-into
title: 智能步入
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6088cfdedda834076b60daf02e33ab1c515166d87633b2fe027ffcce31acc4f1
---

进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/-vkKVxkJS-qhkB-WdMvLDw/zh-cn_image_0000002779406508.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5F1E1EACAA959738989210839E8CD9DFFCD54952DC7D4DCE39BFFC5C1090345)直接Step Into到其中某一个函数的实现中。

## 操作步骤

通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/zasqABHXRhaHGyXuPuB7kA/zh-cn_image_0000002779406510.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B3C8C94714E2E7E19C82C6B926511AF99348A127CBC43FC10A5F5A4A4E34213)（或使用快捷键**Shift+F7**）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ggYDoVNFRqOLvjyirKHrAg/zh-cn_image_0000002779566486.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1910089D5CFFE9AF26D5434B074D008BBB1794045897741058CFEBA0B9022C67 "点击放大")

开发者点击需要跳转的函数，程序会运行到目标函数的实现内。

**说明** 

已经执行完毕的函数不会高亮显示。
