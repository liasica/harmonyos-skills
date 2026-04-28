---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-package-permission-management
title: 包权限管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 包权限管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:acbba57f9427ce21b1bbe0d58c43b15029cf902ab687d3b63fc617c755ce029d
---

ohpm-repo从5.3.0版本开始支持配置包级别的权限管理。系统支持对单个三方包配置精细化的权限控制，包含包的所有者、包的维护者和包的查看者。

系统管理员在仓库管理页的[包的可见性配置](ide-ohpm-depot-management.md#li183931814142614)，能够把包设置为授权可读，并通过[白名单配置](ide-ohpm-depot-management.md#li174331117117)，添加包的查看者。当用户在执行下载、上传、下架和编辑Tag标签时，需要同时具有[仓库的对应权限](ide-ohpm-depot-management.md#zh-cn_topic_0000001792256181_管理仓库)和包的对应权限，缺一不可。

| 包权限角色 | 操作权限 | 适用场景 |
| --- | --- | --- |
| 所有者 | * 下载包 * 上传新包 * 下架现有包 * 编辑包标签（Tag） | 包的管理员，需要所有控制权限 |
| 维护者 | * 下载 * 上传 * 编辑包标签（Tag） | 核心开发者，允许更新但不允许删除包（下架包） |
| 查看者 | * 下载包 | 仅需访问权限的成员或外部协作者 |

在包权限管理页，支持对所拥有的包执行如下操作：管理所有者、管理维护者、转移所有者；对所维护的包执行如下操作：查看所有者、查看维护者。

## 所拥有的包

在所拥有的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 管理所有者。
4. 管理维护者。
5. 转移所有者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/TMZ8ATOzQRyC_mchx8Oo5A/zh-cn_image_0000002561831237.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=E1965489196B2BE9214147DF3C62D02BAC2EAAC335875A7AC501CFE171C5EAD8 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有group3，仓库名为ohpma的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UEvbqsUBRPCN4ZJbVv2YnA/zh-cn_image_0000002530911296.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=47430D4953B4DF1BF67453F1A11FC17B8577C45BAB6837B93E44B6DDBF36F70D "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/0jBukdKeRaa-lj3eWH2lmA/zh-cn_image_0000002530911302.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=0006FD869D6A5C5A3668D5AB94F8407BB7C010EA3BE160B4496F2F5D8B94B38A "点击放大")
* 区域3：管理所有者，包的所有者具有包的下载，上传，下架和编辑包Tag权限，支持对包所有者进行新增和删除。

  当包仅剩唯一一个所有者用户时，禁止删除。当一个用户已经是包的维护者时，禁止被添加为包的所有者。禁止删除当前用户的所有者权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/H0XT84_cSGubzGpGlgw2bg/zh-cn_image_0000002561831249.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=28F64ED6B7ED7EDD7CCCF78DDB73CB197111C5B0C63939A26D2AE6E2DC63E607 "点击放大")
* 区域4：管理维护者，包的维护者具有包的下载，上传和编辑Tag权限，支持对包维护者进行新增和删除。当一个用户已经是包的所有者时，禁止被添加为包的维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/BM8k-pgmRR-og4tQGmuFNw/zh-cn_image_0000002530911304.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=97666897C3F7AE2AEBD24C73B0B1755512B22E47C4A54DCE98CA95D7DFD35C0B "点击放大")
* 区域5：转移所有者，支持当前用户将包的所有者转移给其他非包所有者或维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/vCg4hKxgQt6F77naIfm-Bw/zh-cn_image_0000002561831223.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=84B9DCA810C2393E91322BAB7E91496383AE8910D34A4D0DC420042196FC3A4B "点击放大")

## 所维护的包

在所维护的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 查看包的所有者用户列表。
4. 查看包的维护者用户列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/hRoKpJzqQVG8-C198lZPcg/zh-cn_image_0000002561751245.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=8A4F62F07EAAF728869CE9B3F6E95466F9C1F06EB2127EE1FD794076D898C705 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有a1，仓库名为ohpm的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/cxaoPmpvR8mm9Bpeq9kOgg/zh-cn_image_0000002530751326.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=36EA50B941087682D1423099BA219347BB932519D40979BBE4D81B0DC448D830 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。
* 区域3：查看包的所有者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/6ZKVf2NtSmKTceyyoJpMvA/zh-cn_image_0000002561751253.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=1782D39E6C6D4D59BB48939C7E92A9078F6ED57B56883373F95EC73C434E6CB8 "点击放大")
* 区域4：查看包的维护者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/2_W5CdyMRMOLOM4juyxeIw/zh-cn_image_0000002561751241.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=6168C185333370B027D8878D4F9D41939E8D77B19EDA502D074017BBD0A66A6A "点击放大")
