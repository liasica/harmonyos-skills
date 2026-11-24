---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-package-permission-management
title: 包权限管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 包权限管理
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:20+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1ed791c45fa56ff7ada88257666b06a9943b8d30b12cf7ca16126eb5e668c34f
---

ohpm-repo从5.3.0版本开始支持配置包级别的权限管理。系统支持对单个三方包配置精细的权限控制，包含包的所有者、包的维护者和包的查看者。

系统管理员在仓库管理页的[包的可见性配置](ide-ohpm-depot-management.md#li183931814142614)，能够把包设置为授权可读，并通过[白名单配置](ide-ohpm-depot-management.md#li174331117117)，添加包的查看者。当用户在执行下载、上传、下架和编辑Tag标签时，需要同时具有[仓库的对应权限](ide-ohpm-depot-management.md#section8501304122)和包的对应权限，缺一不可。

| 包权限角色 | 操作权限 | 适用场景 |
| --- | --- | --- |
| 所有者 | * 下载包 * 上传新包 * 下架现有包 * 编辑包标签（Tag） | 包的管理员，需要所有控制权限 |
| 维护者 | * 下载包 * 上传新包 * 编辑包标签（Tag） | 核心开发者，允许更新但不允许删除包（下架包） |
| 查看者 | * 下载包 | 仅需访问权限的成员或外部协作者 |

在包权限管理页，支持对所拥有的包执行如下操作：管理所有者、管理维护者、转移所有者；对所维护的包执行如下操作：查看所有者、查看维护者。

## 所拥有的包

在所拥有的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 管理所有者。
4. 管理维护者。
5. 转移所有者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/hIl-E4JtSfuorkewq0ew-w/zh-cn_image_0000002808764917.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=975A9B06570BBFBDAB226FF50531569FADA03491194E0370052442EDAC936C68 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有group3，仓库名为ohpma的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ugwQCevJRumVk8H6az5XqA/zh-cn_image_0000002808885029.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=746FD46D8CB166A6CAC8DBA92E99D260C6AF2BCC6B006B43475088398577F8CD "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/11VI-HxdTb6_po42G6yzAQ/zh-cn_image_0000002808885015.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AB055A50957D3F68B605057E72799BC2069BE403C7FD2089362B00DC7ABAE39 "点击放大")
* 区域3：管理所有者，包的所有者具有包的下载、上传、下架和编辑包Tag权限，支持对包所有者进行新增和删除。

  当包仅剩唯一一个所有者用户时，禁止删除。当一个用户已经是包的维护者时，禁止被添加为包的所有者。禁止删除当前用户的所有者权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/UsYdv-WzS4en4Uxq_Bp5yA/zh-cn_image_0000002779565360.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D63F79BD7E74C0784FD5894C14651D985DC13D009C387A12800A1F313DE6F65B "点击放大")
* 区域4：管理维护者，包的维护者具有包的下载，上传和编辑Tag权限，支持对包维护者进行新增和删除。当一个用户已经是包的所有者时，禁止被添加为包的维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/tLCeQMD1T0udz_e-HcpJUA/zh-cn_image_0000002779405376.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4C3315276634EB4BC4F88BDB28612C709BED7E09E6F1F0008FBBA26305A046B "点击放大")
* 区域5：转移所有者，支持当前用户将包的所有者转移给其他非包所有者或维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/D075XayXRP-hMue2jPwOFQ/zh-cn_image_0000002808885031.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=903D775B17BF48A546DE7B2A432BD0A8870F47B8D0EEE08434BEE0015590082A "点击放大")

## 所维护的包

在所维护的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 查看包的所有者用户列表。
4. 查看包的维护者用户列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Ex3QhozgTNazLKR2rtka7g/zh-cn_image_0000002779565342.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E85B85508282A0912918C6CBAB8473D92A11F33AEDCAAF3C1BC02FE3CC7D4E6 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有a1，仓库名为ohpm的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/QHyMPA_GSICmYhz7OmgBoA/zh-cn_image_0000002779565346.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=74EC10B7BA5BF0BC55E0AC1812B32F9D13720CE1F4CCBEE7AAF41E754A5FC711 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。
* 区域3：查看包的所有者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zxT_InAbR9mOOvF8Js4tuA/zh-cn_image_0000002808764935.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=F74D67D8D2895A05D18C2A662205967F43F7FD0FBADAD4E8AB1943F8B2A4777D "点击放大")
* 区域4：查看包的维护者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/8B38ANu_SZ-7QcJK0zCzzA/zh-cn_image_0000002779565334.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4574F1421016ADD8CF00A76B3F587A9CAB95AEB7263A8D0F1B2103F5792079B8 "点击放大")
