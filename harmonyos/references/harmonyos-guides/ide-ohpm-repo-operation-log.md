---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-operation-log
title: 操作日志
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 操作日志
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:cbdcd2b8d2ae88a4cd931b85d2e3c4f34dba3826a285f791df3d9dc3388c3430
---

操作日志界面显示用户通过ohpm-repo管理界面进行的所有操作，以及通过ohpm命令行工具执行publish，unpublish和dist-tags等相关命令所记录的日志。操作日志界面分为两个部分：第一部分为筛选条件，第二部分是展示符合筛选条件的数据。

注意

操作日志的数据每隔一天会定时清除，默认保留100天内的操作日志数据，数据保留时间可通过config.yaml中配置项[operation\_log\_retention](ide-ohpm-repo-configuration.md#li38847353322)设定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/6YP-e4RvT5WkpBzG57YCzw/zh-cn_image_0000002561831177.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=75B601532CD7F45DEDD90F38F41AC4660190C0BB0763B89C49D8337D8D54B5A4 "点击放大")

数据筛选：操作日志的数据筛选类别有五类，分别为：用户类型，事件类型，操作类型，操作时间区间和操作对象的用户名。

* 用户类型：分为系统管理员用户和普通用户，当选中普通用户时，只会显示普通用户的操作日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/KEh60tmTT7ugBX8-TTmRng/zh-cn_image_0000002561751211.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=F8E9CB331D24BCCD64F8735F6EA6DF4CF05716B3B06386512C432EE3E3337613)
* 事件类型：包括六种事件类型，包括用户管理，仓库管理，包权限管理，认证管理，组织管理和系统设置，通过选择事件类型进行日志的筛选。
  + 例如当事件类型选择用户管理中的新增用户时，操作日志界面仅显示事件类型为新增用户的日志信息。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/IsiBXysZS7iSDI58cCwArQ/zh-cn_image_0000002530751268.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=481C6748C0FCE4F79D1D0F558C263EAACA08AD189F4446BE2E7585CAD19632E1 "点击放大")
  + 事件类型具体内容见下表：当选择一级事件类型时，将自动包含所有二级事件类型和三级事件类型；当选择二级事件类型时，自动包含所有三级事件类型。

    | 一级事件类型 | 二级事件类型 | 三级事件类型 |
    | --- | --- | --- |
    | 用户管理 | 新增用户 | - |
    | 删除用户 | - |
    | 修改用户角色 | - |
    | 重置用户密码 | - |
    | 仓库管理 | 管理仓库 | 新增仓库 |
    | 删除仓库 |
    | 更新代码仓 |
    | 上架资源包 |
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

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Yzxp4sUYQMaB9nN2_3DD8Q/zh-cn_image_0000002530911256.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=932875F2867A61BD97BEE3A6B2A09BE10947C1A5F53FD3C63B05A513F1CDEF55 "点击放大")
  + 操作时间区间：选中操作时间的区间进行筛选。如区间时间选择在2025.8.4到2025.8.11，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/J25hzgB8SVaQu4nzEq27SQ/zh-cn_image_0000002561751213.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=73C7219E33559A8BA3DFA45D29CAADC3C65ABCF9A8C7B7C1000B7EFCA374A695 "点击放大")
  + 操作对象用户名：输入操作对象用户名进行筛选。如输入用户名为user，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/b7SKJk_qSDmXuEZqJ9ba8A/zh-cn_image_0000002530751266.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=966C0D2F4CB3876ACFAB8FD23D72B49690D06AE875D0FF7AD4C1313C7CFAE78E "点击放大")
