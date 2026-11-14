---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clangd
title: 代码索引（clangd）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码索引（clangd）
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0e110479fd967abb2e51b3241c9311ca8f4d1dd91767fd3efb927969f2e3ee48
---

在打开C/C++大工程时，代码索引耗时较长，且持续占用CPU和内存，开发者通常需要等待一段时间才能进入编码状态，影响开发效率。

从26.0.0版本开始，DevEco Studio支持切换C/C++代码索引模式，满足不同工程规模和开发需求。代码索引模式包括无索引（No index）、轻量化索引（Lightweight index）、全量索引（Full index），默认为全量索引。

* 无索引：无需依赖clangd后台索引，资源占用最小化，加载速度相对最快。该索引模式会影响代码跳转、代码引用查找、代码重命名和Safe Delete等功能。
* 轻量化索引：聚焦核心符号，构建精简索引，减少索引时长，索引效率较高。该索引模式会影响template<>相关场景下的代码跳转、代码引用查找、代码重命名和Safe Delete等功能。
* 全量索引：构建全局符号索引，索引时长较长和资源开销较高，实现精准高效的语言服务。

**说明** 

该配置对当前工程持续生效。

点击菜单栏**File** **>** **Settings（macOS为DevEco Studio > Preferences/Settings）****>** **Advanced Settings** **>** **Clangd**，进行索引模式切换。切换索引模式后，需要重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/SxnCnMN5TSGbDWsSOziZmg/zh-cn_image_0000002808766443.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=6011E9169FD60EA23C0994EAEAEA37BDC234DAE300EC291588E18234284B7602)

打开C/C++大工程时，DevEco Studio右下角会弹出提示，建议切换索引模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/qwzfIBrwR_Go57OwGdxbxw/zh-cn_image_0000002779406884.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=55F0E89DA89D939B75F28D8C58BE8C457D587388B74D6C294292985807892EE5)
