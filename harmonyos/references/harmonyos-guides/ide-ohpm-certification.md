---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-certification
title: 认证管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 认证管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7603cd30e84f76f6f613cfb90a611955ecac27c4f2db53d63b7692bb1915807f
---

当前ohpm-repo的认证方式有证书认证和AccessToken两种方式：

证书认证：在使用ohpm客户端执行publish，unpublish或dist-tags相关命令时，通过嵌入加密ssh证书进行身份验证。

AccessToken认证：将ohpm-repo生成的AccessToken配置到ohpm客户端配置文件中，实现publish、unpublish、dist-tags、info和install等操作的免密认证。

## 证书认证

使用ohpm发布包时，需要先在配置文件.ohpmrc文件中配置publish\_id和key\_path。publish\_id对应发布码，key\_path对应私钥的地址，其详细发布流程见[使用命令行工具发布](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_使用命令行工具发布)。认证管理主要是管理私钥对应的公钥信息，在用户使用ohpm发布包时进行校验。认证管理页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/1ji0E2WuT8evSp6tTRlnjA/zh-cn_image_0000002530751476.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=D9F273C77AF75FC5C1FE7BA9808BE5474E48835AEA3157D171FFF615BEFFE2D6 "点击放大")

1. 点击新增，弹出添加公钥面板，可以添加公钥信息。一个用户最多可以添加十条公钥信息，因此可以通过配置不同的公钥信息实现多人共享该用户使用ohpm进行发布包操作。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Qyv_GV9aSNmYvYNw2BC7lA/zh-cn_image_0000002561751425.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=8221DC051F334593A9A8951F33963218B01FE61D1E69377554B36B1EAFD44E49 "点击放大")
2. 点击如何生成公钥，可查看公钥生成的说明，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/esamir6NRH6CsVbaN-J7DQ/zh-cn_image_0000002530911462.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=E52A0866C3B78DF06AB5469FB93E19B1364E59A230B6543B8F794A427683DAB8 "点击放大")
3. 点击删除，可以删除已经存在的公钥信息，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/e5xcLzDHQzat1KcC609jhw/zh-cn_image_0000002561831399.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=4769F8AA1A9941BD9D001FD04814AFC504F4A64FBFFCF00492BCF5DBBD6A68E4 "点击放大")

## AccessToken

AccessToken是ohpm-repo 2.1.0版本新引入的认证机制（需配套使用1.6.0及以上版本的ohpm命令行工具），用户通过ohpm-repo界面生成Token，并将其配置至ohpm客户端配置文件中。在与ohpm-repo交互时，客户端会自动附带Token进行身份验证。

该Token分两种权限等级：只读Token允许执行info和install操作；读写Token除了包含只读权限外，还支持publish，unpublish和dist-tags相关操作。每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。AccessToken页面效果如下:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Nss4q_tzQJ6QlJIB7mZbnw/zh-cn_image_0000002530751488.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=53C989F2CC41281C7CF4590497CA846456C6F9988FA9AB00FC7932AD8CDFCB24 "点击放大")

1. 点击生成只读Token，ohpm-repo将自动生成一个专用于ohpm客户端进行包信息查询（info）和安装包（install）操作的认证Token，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/WOXvkiiQSzOq1-p3PY1iRA/zh-cn_image_0000002530751466.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=F0C5B140FFA985608F5C66491A61AC14B2422BD3FD6CEEBBA769520C5D8B80FF "点击放大")
2. 点击生成读写Token，ohpm-repo将自动生成一个专用于ohpm客户端进行包信息查询（info）、安装包（install）、发布包（publish）、下架包（unpublish）和版本标记（dist-tags）操作的认证Token。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/g1PmIUeuSA2DvdDF20beWA/zh-cn_image_0000002530911472.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=196AE7DD9222DB081AF0C5CBE1E02C7E4FE88231ECAC2D16E5693FF33D80C6C5 "点击放大")
3. 点击AccessToken指南，即刻显示使用教程，指导如何有效使用和配置AccessToken。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/k-YV28-VQWqxBvdLsJYmvQ/zh-cn_image_0000002561751415.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=3DB7C4E5A191B7DE71906D514A19B147F8E3709BF8D23208F7B228AA5B89963A "点击放大")
4. 点击删除，删除对应的Token。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/FWsyJAagRw6dRwQuW-VFPQ/zh-cn_image_0000002561831389.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=B10DBAA1C4DCD58C21CCF0B92B4E84671C398F6F3B8BE4473D14F2D5606775B3 "点击放大")
5. AccessToken的使用：
   1. 通过ohpm-repo页面生成Token。
   2. 将Token配置在ohpm客户端的.ohpmrc配置文件中，配置示例如下所示:

      ```
      1. //127.0.0.1:8088/repos/ohpm/:_auth=readWriteToken
      2. //127.0.0.1:8088/repos/ohpm/:_read_auth=readOnlyToken
      ```

      其中//127.0.0.1:8088/repos/ohpm/是您ohpm-repo的registry地址去除协议名的部分，:\_auth和:\_read\_auth分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。
