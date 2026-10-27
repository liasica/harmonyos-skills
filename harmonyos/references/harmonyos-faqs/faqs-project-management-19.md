---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-19
title: 如何使用DevEco Studio上的Git工具进行多远程仓管理
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何使用DevEco Studio上的Git工具进行多远程仓管理
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:49+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:91018df90b380ef6906eec74c53d5f12ad08cd5a410d6f6ff870ed848f9ab729
---

添加新的远程仓库：

1. 右击Remote以调出菜单。
2. 点击Manage Remotes，打开Git Remotes窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/jnc7k9L_TrmGVuMm88Qh2A/zh-cn_image_0000002624478434.png)
3. 点击添加按钮。
4. 输入远程仓名称和URL，远程仓名称可自由命名。
5. 点击Define Remote窗口的OK按钮，在新弹出的窗口中输入域账号和密码。
6. 点击Git Remotes窗口的确定按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/3sbkwSE4SMOLxZnUFdmFbA/zh-cn_image_0000002654797801.png "点击放大")
7. 点击拉取远程记录，新添加的远程仓库将在Remote子菜单中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/bnUZGL9BTI-D4o5KGUNVGA/zh-cn_image_0000002624638342.png)

Push提交：

Push提交和Push提交到远程仓库的过程相似。如需切换远程仓库，可单击下图中标记1的分支名；标记3表示以PR方式提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/cnfgdRicRAOTNk_T8pqRIQ/zh-cn_image_0000002654837747.png "点击放大")

切换默认关联的远程仓库：

可以使用以下命令进行切换。

```screen
git branch hmos_dev_20230907 --set-upstream-to=codehub_origin/hmos_dev_20230907
```
