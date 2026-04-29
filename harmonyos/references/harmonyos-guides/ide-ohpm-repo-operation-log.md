---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-operation-log
title: 操作日志
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 操作日志
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:48+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9d70175448922d323f6bf5782668064fc9d59f4862ae76293095fbf02e13e8fa
---

操作日志界面显示用户通过ohpm-repo管理界面进行的所有操作，以及通过ohpm命令行工具执行publish，unpublish和dist-tags等相关命令所记录的日志。操作日志界面分为两个部分：第一部分为筛选条件，第二部分是展示符合筛选条件的数据。

注意

操作日志的数据每隔一天会定时清除，默认保留100天内的操作日志数据，数据保留时间可通过config.yaml中配置项[operation\_log\_retention](ide-ohpm-repo-configuration.md#li38847353322)设定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/mwvfZ7_bQ12nWrgaAuJvCA/zh-cn_image_0000002561831177.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=3A567A5652EA4FBDBEB6C9E510A800078AB0E4EBDC52F40C54DB1C6849A332E4 "点击放大")

数据筛选：操作日志的数据筛选类别有五类，分别为：用户类型，事件类型，操作类型，操作时间区间和操作对象的用户名。

* 用户类型：分为系统管理员用户和普通用户，当选中普通用户时，只会显示普通用户的操作日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/rtJ0dNNEQ2Oy9UxMqnU8VQ/zh-cn_image_0000002561751211.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=5A39FEA77D8D608B6D1CFAD9BA110EB51E849FEE3DB57DBC06F2E25539B98D69)
* 事件类型：包括六种事件类型，包括用户管理，仓库管理，包权限管理，认证管理，组织管理和系统设置，通过选择事件类型进行日志的筛选。
  + 例如当事件类型选择用户管理中的新增用户时，操作日志界面仅显示事件类型为新增用户的日志信息。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/BVE3-_WkS86iKYCJGaoUKA/zh-cn_image_0000002530751268.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=2CB55F1A5EA9788A9EBF1B6490876AA2DAE80D65FFE03079853FB7D0BC64B004 "点击放大")
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

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/jXaGocdvTRiuSynN5NCPfw/zh-cn_image_0000002530911256.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=703C7679237BAA53BD39F4955D589F57B81FA210A356C8857B15C5A36D2822A7 "点击放大")
  + 操作时间区间：选中操作时间的区间进行筛选。如区间时间选择在2025.8.4到2025.8.11，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/oESOVq1KTIyRYrpU8hbQrg/zh-cn_image_0000002561751213.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=617AB90B01A652535BDFD3D7370EA15EC55FBB62D956468733A98CC7AF8FDAC7 "点击放大")
  + 操作对象用户名：输入操作对象用户名进行筛选。如输入用户名为user，操作日志页面结果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ZZRycdiHRLGS5CSDR2BT6g/zh-cn_image_0000002530751266.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=98864F38321ADBD933D35323D9B091EFAA51FC6A4AB5A88224134AB67ED53928 "点击放大")
