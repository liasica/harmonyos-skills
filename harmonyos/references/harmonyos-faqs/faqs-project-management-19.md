---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-19
title: 如何使用DevEco Studio上的Git工具进行多远程仓管理
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何使用DevEco Studio上的Git工具进行多远程仓管理
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2a6c5b0fc24c822f54bf9b47510d01072ba1cc5bec32b098c69a135e0bd4a249
---

添加新的远程仓库：

1. 右击Remote以调出菜单。
2. 点击Manage Remotes，打开Git Remotes窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JW44x5b1T5mmsTt0nFFBUw/zh-cn_image_0000002194318352.png?HW-CC-KV=V1&HW-CC-Date=20260429T062010Z&HW-CC-Expire=86400&HW-CC-Sign=6DB8485CB3DD46920ECC00B42B8D148BBD333D14F6E3FD558805A35B5E07DC58)
3. 点击添加按钮。
4. 输入远程仓名称和URL，远程仓名称可自由命名。
5. 点击Define Remote窗口的OK按钮，在新弹出的窗口中输入域账号和密码。
6. 点击Git Remotes窗口的确定按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/n81WFTKaQPCgbFHkSdGgMQ/zh-cn_image_0000002229604125.png?HW-CC-KV=V1&HW-CC-Date=20260429T062010Z&HW-CC-Expire=86400&HW-CC-Sign=80991E776372E0EBFF2EB6ED08BDBC16D1E6F0CBC04AC65715EA982470A602DA "点击放大")
7. 点击拉取远程记录，新添加的远程仓库将在Remote子菜单中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/t339yd8_SE-TFQLfm8kjZw/zh-cn_image_0000002229758613.png?HW-CC-KV=V1&HW-CC-Date=20260429T062010Z&HW-CC-Expire=86400&HW-CC-Sign=A133127F411F064FE2AC4CCC5D04A24B49A4D06546045CBA381BC04756343F60)

Push提交：

Push提交和Push提交到远程仓库的过程相似。如需切换远程仓库，可单击下图中标记1的分支名；标记3表示以PR方式提交。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/3sNnui86QH6VbFP4cBRmjg/zh-cn_image_0000002194158744.png?HW-CC-KV=V1&HW-CC-Date=20260429T062010Z&HW-CC-Expire=86400&HW-CC-Sign=963FC02827A4DA23573474757A4566D33D31A8A7D9C7798F1D2DE8A1D7E28CFF "点击放大")

切换默认关联的远程仓库：

可以使用以下命令进行切换。

```
1. git branch hmos_dev_20230907 --set-upstream-to=codehub_origin/hmos_dev_20230907
```
