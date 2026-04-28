---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-19
title: 如何使用DevEco Studio上的Git工具进行多远程仓管理
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何使用DevEco Studio上的Git工具进行多远程仓管理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bf93c338c3cd14cd31a05d8177c63a171e60b8076871406badb6c5cab3fb3b1f
---

添加新的远程仓库：

1. 右击Remote以调出菜单。
2. 点击Manage Remotes，打开Git Remotes窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JW44x5b1T5mmsTt0nFFBUw/zh-cn_image_0000002194318352.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=1137243DFDCA87E40C1A56FF418DB8D81F308472D59BD08B2894A2079113C7EB)
3. 点击添加按钮。
4. 输入远程仓名称和URL，远程仓名称可自由命名。
5. 点击Define Remote窗口的OK按钮，在新弹出的窗口中输入域账号和密码。
6. 点击Git Remotes窗口的确定按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/n81WFTKaQPCgbFHkSdGgMQ/zh-cn_image_0000002229604125.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=35D134F143A26FCFCF9AD49099EA8D188572268AF0E3000EB794F10FC7D1ED6F "点击放大")
7. 点击拉取远程记录，新添加的远程仓库将在Remote子菜单中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/t339yd8_SE-TFQLfm8kjZw/zh-cn_image_0000002229758613.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=EB563EA348218D3B42C8357AFDB4DE2DD7D5E3CAC5660BBB0F36133D55DDC9CE)

Push提交：

Push提交和Push提交到远程仓库的过程相似。如需切换远程仓库，可单击下图中标记1的分支名；标记3表示以PR方式提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/3sNnui86QH6VbFP4cBRmjg/zh-cn_image_0000002194158744.png?HW-CC-KV=V1&HW-CC-Date=20260428T002859Z&HW-CC-Expire=86400&HW-CC-Sign=20FE4522212CD0DB7214B839B1423EA7FFA1D7FF6CE198FE9460A090FC7D0B85 "点击放大")

切换默认关联的远程仓库：

可以使用以下命令进行切换。

```
1. git branch hmos_dev_20230907 --set-upstream-to=codehub_origin/hmos_dev_20230907
```
