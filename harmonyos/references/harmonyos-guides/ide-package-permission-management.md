---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-package-permission-management
title: 包权限管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 包权限管理
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:27+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8190f1e0a9867ac5ffaa57bc7d865605dab3aae4c1086e9b50acf224f6c7818c
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/8m4Z1mxETZ6IT8F0XgScYA/zh-cn_image_0000002808764917.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E6602DD6ACE54883CAAD1A9E373EF1530D6CB7F5553B92D6F11255EC973B45E "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有group3，仓库名为ohpma的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/MjoZ-jfhSFiO1tCaaQWTTQ/zh-cn_image_0000002808885029.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=86AEE4498DF21B710DD8A97CAE8D0DA7732F15E3C588755791D0D54A4A21B6E1 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/63ebbLV4QgyNoldy9aYX7A/zh-cn_image_0000002808885015.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8061CFD460C717CFC83C3DA1D53FA7EAA5E199F881C1CE2EA746073BFBF86EE "点击放大")
* 区域3：管理所有者，包的所有者具有包的下载、上传、下架和编辑包Tag权限，支持对包所有者进行新增和删除。

  当包仅剩唯一一个所有者用户时，禁止删除。当一个用户已经是包的维护者时，禁止被添加为包的所有者。禁止删除当前用户的所有者权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/QFRaHGd7THmw2a84p3Od-Q/zh-cn_image_0000002779565360.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=9786E60384502F2DA25A5671E77ECB0274A99DC7E359CC66EF8B64E6FBA51731 "点击放大")
* 区域4：管理维护者，包的维护者具有包的下载，上传和编辑Tag权限，支持对包维护者进行新增和删除。当一个用户已经是包的所有者时，禁止被添加为包的维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/B2azV4x8QBmBhPupVG4S_w/zh-cn_image_0000002779405376.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB865E2DA74964AF0D4407A9F672310137E1A4870AE1D2EEFCEC1BCEAB3DB5C5 "点击放大")
* 区域5：转移所有者，支持当前用户将包的所有者转移给其他非包所有者或维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/dcHZt7FpScqTiF7zYHwgJg/zh-cn_image_0000002808885031.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6B99B08EA91BF145FAFA0117D62C99055AFD05026A7A97E0E3302B948AAF988 "点击放大")

## 所维护的包

在所维护的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 查看包的所有者用户列表。
4. 查看包的维护者用户列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/xHdtBIxYT76XftkA2HJTXw/zh-cn_image_0000002779565342.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E18FF89714D252EEC8BC7E30F8593E8DF7B9BA3A36F27F4F099C6A24281CA1D "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有a1，仓库名为ohpm的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/tubEcEmXTHK3ZnGX5AJsEg/zh-cn_image_0000002779565346.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A636A54D9EA42734510D45949F8CE9927F8D8D2A88E2AB34EE707E078ACD57C "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。
* 区域3：查看包的所有者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/KA0w8pT2Sy-u8ojQHXZTfQ/zh-cn_image_0000002808764935.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=B47B48BB6B2A2011C6CE036999434BD397291B472D5B0D7B47FA9BA0981544CC "点击放大")
* 区域4：查看包的维护者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/9GXRDh24SZ2-HIzH88kybw/zh-cn_image_0000002779565334.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6AFF071B57832D8E4E47ED006FB753DE90608E4813479A27D2F4C7540CD98FF "点击放大")
