---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-19
title: 如何使用DevEco Studio上的Git工具进行多远程仓管理
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何使用DevEco Studio上的Git工具进行多远程仓管理
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f8b453e63b4fb6f6c54415b9ea9ef38640ae63becb4d522b6f7d3a3ebe5b9f41
---

添加新的远程仓库：

1. 右击Remote以调出菜单。
2. 点击Manage Remotes，打开Git Remotes窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JW44x5b1T5mmsTt0nFFBUw/zh-cn_image_0000002194318352.png)
3. 点击添加按钮。
4. 输入远程仓名称和URL，远程仓名称可自由命名。
5. 点击Define Remote窗口的OK按钮，在新弹出的窗口中输入域账号和密码。
6. 点击Git Remotes窗口的确定按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/n81WFTKaQPCgbFHkSdGgMQ/zh-cn_image_0000002229604125.png "点击放大")
7. 点击拉取远程记录，新添加的远程仓库将在Remote子菜单中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/t339yd8_SE-TFQLfm8kjZw/zh-cn_image_0000002229758613.png)

Push提交：

Push提交和Push提交到远程仓库的过程相似。如需切换远程仓库，可单击下图中标记1的分支名；标记3表示以PR方式提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/3sNnui86QH6VbFP4cBRmjg/zh-cn_image_0000002194158744.png "点击放大")

切换默认关联的远程仓库：

可以使用以下命令进行切换。

```
1. git branch hmos_dev_20230907 --set-upstream-to=codehub_origin/hmos_dev_20230907
```
