---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-operation-log
title: 操作日志
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 操作日志
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:47+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:1f4bcdfa1711e0e7a0f5b05ad645865df246337ec96ca996e0f041dfa9089f45
---

操作日志界面显示用户通过ohpm-repo管理界面进行的所有操作，以及通过ohpm命令行工具执行publish，unpublish和dist-tags等相关命令所记录的日志。操作日志界面分为两个部分：第一部分为筛选条件，第二部分是展示符合筛选条件的数据。

操作日志的数据每隔一天会定时清除，默认保留100天内的操作日志数据，数据保留时间可通过config.yaml中配置项[operation\_log\_retention](ide-ohpm-repo-configuration.md#li38847353322)设定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/nEx4lwa2Tvmc5E74T_KS-A/zh-cn_image_0000002808764727.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=386868352B83744B03BB3D1BE866CAC067825781A30F84EB5FB30DA197736A7A "点击放大")

数据筛选：操作日志的数据筛选类别有五类，分别为：用户类型，事件类型，操作类型，操作时间区间和操作对象的用户名。

* 用户类型：分为系统管理员用户和普通用户，当选中普通用户时，只会显示普通用户的操作日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/d0dxdKsYSTiUd7fhM8dqGw/zh-cn_image_0000002779405216.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EBC2CB4047CA7BED7BB3C142C9406D3973BF36DA2B0ED787E65B9E923F5A0BF "点击放大")
* 事件类型：六种事件类型包括用户管理、仓库管理、包权限管理、认证管理、组织管理、系统设置。通过选择事件类型进行日志的筛选。
  + 例如当事件类型选择用户管理中的新增用户时，操作日志界面仅显示事件类型为新增用户的日志信息。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/kDPYI_aeS3qKAKMFYTFLng/zh-cn_image_0000002779405196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=C066D30C568D969664C4DE04429222CB25EE63A3986344B8CFF51DA7D8CA61D4 "点击放大")
  + 事件类型具体内容见下表：当选择一级事件类型时，将自动包含所有二级事件类型和三级事件类型；当选择二级事件类型时，自动包含所有三级事件类型。

    | 一级事件类型 | 二级事件类型 | 三级事件类型 |
    | --- | --- | --- |
    | 用户管理 | 新增用户 | - |
    | 编辑用户 |  |
    | 删除用户 | - |
    | 修改用户角色 | - |
    | 重置用户密码 | - |
    | 仓库管理 | 管理仓库 | 新增仓库 |
    | 删除仓库 |
    | 更新代码仓 |
    | 上架资源包 |
    | 批量上架资源包 |
    | 下架资源包 |
    | 批量下架资源包 |
    | uplink | 更新Uplink代理 |
    | 添加Uplink |
    | 修改Uplink |
    | 删除Uplink |
    | tag | 增加Tag |
    | 更新Tag |
    | 删除Tag |
    | 权限管理 | 编辑包可见性 |
    | 新增包白名单用户 |
    | 删除包白名单用户 |
    | 包权限管理 | 新增包所有者 | - |
    | 删除包所有者 | - |
    | 转移包所有者 | - |
    | 新增包维护者 | - |
    | 删除包维护者 | - |
    | 认证管理 | 证书认证 | 添加发布公钥 |
    | 删除发布公钥 |
    | Access Token | 生成Access Token |
    | 删除Access Token |
    | 组织管理 | 组织 | 添加分组 |
    | 修改分组 |
    | 删除分组 |
    | 组织成员 | 添加组成员 |
    | 删除组成员 |
    | 组织管理员 | 添加组管理员 |
    | 删除组管理员 |
    | 系统设置 | 更新oh-package.json5检查规则 | - |
    | 重置系统密钥 | - |
    | 更新系统安全配置 | - |
  + 操作结果：选择成功/失败进行筛选。如操作结果选择失败，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/0kGoyHgKT7aRlhMMsd8VQg/zh-cn_image_0000002779405178.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=67FE97250E024282FDFA4A1D25FC3E791FD54431786D8616E161EACBEF3A71C0 "点击放大")
  + 操作时间区间：选中操作时间的区间进行筛选。如区间时间选择在2026.6.27到2026.7.4，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/2IefFzFmQrm0iXS-uRvf9Q/zh-cn_image_0000002808884863.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=23DB26A96189B915E3032BB1BE96A358C06BEEB0BD304C168637C7A95D0FB9CD "点击放大")
  + 操作对象用户名：输入操作对象用户名进行筛选。如输入用户名为user，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/zi14qQtkQZC70m3Uk4sBkg/zh-cn_image_0000002779565178.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BC78387041DA9108B17275A95F4F62D31F2F4CE90C288162AEE47F68E600D65 "点击放大")
