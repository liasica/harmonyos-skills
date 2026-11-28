---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-start-and-close
title: 启动和关闭模拟器
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 使用模拟器运行应用 > 管理模拟器 > 启动和关闭模拟器
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:50350a3cebddfb993bc1c4c851a8c13a3bf362acc0c5fa410dec05b01f7aa36a
---

在设备管理器页面，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/g_iAUH25S82Uwbawd8EOnw/zh-cn_image_0000002779405122.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=E800416A152BCE5406773312897383F695E73FB718746DB53CE58F79FAB6670C)即可启动模拟器。模拟器启动时会默认携带之前运行时的用户数据，包括用户上传的文件，安装的应用等。如果是新创建的模拟器，则不会携带用户数据。如果想清除之前运行时的用户数据，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/o8RehMZHRSeP6Ybc8PTngw/zh-cn_image_0000002808764673.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=D36C6CD9DCC068F7CD2A6C9F11F71866824C2392E6A393D9E58E8A9304588B81) **> Wipe User Data**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/yNnwgb-uRWyyFce-5W_lrQ/zh-cn_image_0000002779565078.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=40266CEF6743F427D304B3B6AD478EC264CE50C6A267C604D1BFEFC609C90D11 "点击放大")

从DevEco Studio 6.1.0 Beta1版本开始，如果创建模拟器时选择热启动，则启动模拟器时会加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。热启动后，多屏状态会恢复为单屏状态。

从26.0.0版本开始，如果热启动后出现异常，可点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/4qewquB5QXSJwAG5UsK-Jg/zh-cn_image_0000002779405132.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=8516B518C8825C989BC531AE348A6ADB991DAF98830843C3DBE067374657AD11) **> Cold Boot**，本次将以冷启动方式启动模拟器，并且会保留之前的用户数据，关闭模拟器时仍会保存快照。

例如推包运行后关闭模拟器，再次启动时会显示在上次运行的界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/i24HZSrKRk6w1fIsHJftGg/zh-cn_image_0000002808884783.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC97BE2C82F3CE5BD66B0A58C1C8440C0367E6B0C5282827DB81F7CE03CF9318 "点击放大")

在模拟器运行期间，可以点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/b5LUYioIQ3SrLt2gGO6fjw/zh-cn_image_0000002779565086.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=E34584990B308F7FD66E785B0E55531DCB76BA868A78A9EC9C7D965918A1B892) **> Show on Disk**显示模拟器在本地生成的用户数据。点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/4wDnt_J1SaelPFFGSh7h_w/zh-cn_image_0000002808764655.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8590D99C4FF91362700A0E9C0A4C840C8C9F5C1F03F88C80C4DFF385EF5203E) **> Generate logs**可以生成模拟器自启动到此刻的所有日志信息。想要关闭运行中的模拟器，可以在设备管理器页面点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/B-9bMwTUSNml1e6eW3FkDg/zh-cn_image_0000002779405144.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CA950C7291D462AEF118F775E7A2BCAABCE04BE06F33DC44A4AC5B562075897)，或者点击模拟器工具栏上的关闭按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/sQqSgZl4QFKl0BdcAnzpDQ/zh-cn_image_0000002779405130.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EA1935C69317038FA2E9814FAC0EEC62D51AF7CB5DA9F89D7E6C642009B9CB1)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/q98d6i6CRqmbOEVp_8LLjA/zh-cn_image_0000002808884733.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B3A5D50B1725B1895219A904A86301896C23DAEC4E4B8E7DDAD66D48AEE2B08 "点击放大")

模拟器关闭后，点击**Actions >** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/jp6aXAyvRxa3RlBz55fRcA/zh-cn_image_0000002779405126.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=08B17B6B0FB987CCA6A2E30AB8CE58E0337650CA806A6FEEDAA3511AE6FE6D7A) **> Delete**可以删除模拟器，并清除模拟器的用户数据和配置信息。
