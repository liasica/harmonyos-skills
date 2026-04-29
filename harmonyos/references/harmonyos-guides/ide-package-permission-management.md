---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-package-permission-management
title: 包权限管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 包权限管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6de69362c1788bb93abe2cbdbfd981a05741bce9c7eb6a0a8ea65a34eee0eb2f
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/LKZy9PeLQ0WkCeZxRbnv7w/zh-cn_image_0000002561831237.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=0FBE1D6B887E4A28FC47D128AE7CBC04C71F7EC9FAA10E34954579402683A07F "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有group3，仓库名为ohpma的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/yWol66g1STy7THKz3gBJDA/zh-cn_image_0000002530911296.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=8519A04C5EC2161899C7249EA6D369B3888C331DCB91C2D5E63C0CCE7DEF268A "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/JZK2SKnrRdWd0eGHZgT3gA/zh-cn_image_0000002530911302.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=C23203A1A29633D423C280616C91F8B99D3561175DDF9BFB368B63398A0275D2 "点击放大")
* 区域3：管理所有者，包的所有者具有包的下载，上传，下架和编辑包Tag权限，支持对包所有者进行新增和删除。

  当包仅剩唯一一个所有者用户时，禁止删除。当一个用户已经是包的维护者时，禁止被添加为包的所有者。禁止删除当前用户的所有者权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/mJcI50sqR9CY7tt2PvC37Q/zh-cn_image_0000002561831249.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=D19FF86C1D02B5C920E40109AA49D604C7EA7274D3B3A91FA3072660ABCFC3D1 "点击放大")
* 区域4：管理维护者，包的维护者具有包的下载，上传和编辑Tag权限，支持对包维护者进行新增和删除。当一个用户已经是包的所有者时，禁止被添加为包的维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/htgMIin3TUWtKkjdV89v3w/zh-cn_image_0000002530911304.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=1C7A797EA6E78E2697878AFAD583D426F02F95F4B4ED7C5E0A96C634701B1866 "点击放大")
* 区域5：转移所有者，支持当前用户将包的所有者转移给其他非包所有者或维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/6b6awP56Tmaj9l6eyuF0Yw/zh-cn_image_0000002561831223.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=B2A485A6379F62966AE945729B54F2C69F922FDEF2DE51647A17870E1544EBB3 "点击放大")

## 所维护的包

在所维护的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 查看包的所有者用户列表。
4. 查看包的维护者用户列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/a2xQoT19Sa6sbpXa0IzxNg/zh-cn_image_0000002561751245.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=B580FB9AEC4C36EE733BBB528AA354B52230BE64C827B3375C8B25EC96A38356 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有a1，仓库名为ohpm的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/4VYgTJwcQe2HXnVxIHDvYA/zh-cn_image_0000002530751326.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=CDB697BBA85CBE3BD346ED6AC2F0E442A983BE3C1D6D62BC4CEB3DDA8E60F8CF "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。
* 区域3：查看包的所有者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/qfUQlC_wRaWkowCKgPKINQ/zh-cn_image_0000002561751253.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=75919E28271F9C27942E958977B78DF3C8458745325DA310840F91631C7E8E77 "点击放大")
* 区域4：查看包的维护者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/9B9MsKrASl2pXAHxl8MJmA/zh-cn_image_0000002561751241.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=567C474798F701824EA60A77E2B4249CF99CC01DF9A94D92BBB2D10FBC3161C7 "点击放大")
