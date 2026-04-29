---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-certification
title: 认证管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 认证管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d2c9b0a57ea8e558b9b75242a78500cb1bec2ed2fef375ea724fe581f36ab4b9
---

当前ohpm-repo的认证方式有证书认证和AccessToken两种方式：

证书认证：在使用ohpm客户端执行publish，unpublish或dist-tags相关命令时，通过嵌入加密ssh证书进行身份验证。

AccessToken认证：将ohpm-repo生成的AccessToken配置到ohpm客户端配置文件中，实现publish、unpublish、dist-tags、info和install等操作的免密认证。

## 证书认证

使用ohpm发布包时，需要先在配置文件.ohpmrc文件中配置publish\_id和key\_path。publish\_id对应发布码，key\_path对应私钥的地址，其详细发布流程见[使用命令行工具发布](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_使用命令行工具发布)。认证管理主要是管理私钥对应的公钥信息，在用户使用ohpm发布包时进行校验。认证管理页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/asHMpBUARm-qkzzivIEImQ/zh-cn_image_0000002530751476.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=3F0DBF19C477B170FD5F383664883CA17B1D21697F33A5901A99F66C7CFB4297 "点击放大")

1. 点击新增，弹出添加公钥面板，可以添加公钥信息。一个用户最多可以添加十条公钥信息，因此可以通过配置不同的公钥信息实现多人共享该用户使用ohpm进行发布包操作。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/VS3ePIJ2SbijsxknhjJ0rQ/zh-cn_image_0000002561751425.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=C261F1355293632BA9C232254AAB634A6AC00E77F2DCE83933D32C2AAC7FD60E "点击放大")
2. 点击如何生成公钥，可查看公钥生成的说明，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/eiwEdGd7SACB0iukBbyvBA/zh-cn_image_0000002530911462.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=068AE8F640EF9290B7F0764D438E52353F3FCE2F5EFA1012C455438AAFBBD053 "点击放大")
3. 点击删除，可以删除已经存在的公钥信息，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/rfVsqLXhRsmDC72F5UT46g/zh-cn_image_0000002561831399.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=CC96BBBC3D23B23C449AD532E2AEED358D0D8FA3B1250B88D949D6B4CD3B0F73 "点击放大")

## AccessToken

AccessToken是ohpm-repo 2.1.0版本新引入的认证机制（需配套使用1.6.0及以上版本的ohpm命令行工具），用户通过ohpm-repo界面生成Token，并将其配置至ohpm客户端配置文件中。在与ohpm-repo交互时，客户端会自动附带Token进行身份验证。

该Token分两种权限等级：只读Token允许执行info和install操作；读写Token除了包含只读权限外，还支持publish，unpublish和dist-tags相关操作。每位用户每种权限类型的Token最多可生成10个，首次生成时系统自动复制到剪贴板，后续不再显示完整Token内容。AccessToken页面效果如下:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/dIw1pq8qT6y45gQ3-vUvEA/zh-cn_image_0000002530751488.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=290853473F115E5203F6DF839664A507EFE65C7A78664EF5056617C337BB335F "点击放大")

1. 点击生成只读Token，ohpm-repo将自动生成一个专用于ohpm客户端进行包信息查询（info）和安装包（install）操作的认证Token，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/XisLXvnxQoeiPc5LpJrkxA/zh-cn_image_0000002530751466.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=8DB7F992EBF573DF7B361C8B54007E18DC368B54CBD4F9C72A17FA86B8478118 "点击放大")
2. 点击生成读写Token，ohpm-repo将自动生成一个专用于ohpm客户端进行包信息查询（info）、安装包（install）、发布包（publish）、下架包（unpublish）和版本标记（dist-tags）操作的认证Token。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/u3mSEChBQQmOMrUyXUMuOw/zh-cn_image_0000002530911472.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=2C608941C97DA7D2ACAFF2591BFC761379F2CE5632E3219466ED95BA923023A0 "点击放大")
3. 点击AccessToken指南，即刻显示使用教程，指导如何有效使用和配置AccessToken。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Qph1upqoTLyRlFsEkpoHdQ/zh-cn_image_0000002561751415.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=61A7994156D16C3D0F6A45FFC324A01C9329745B6F72EF6650686F1E42391FDA "点击放大")
4. 点击删除，删除对应的Token。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/93UlkUiZRgmSxUJepZ0yVA/zh-cn_image_0000002561831389.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=F576D4B9C8CA0BCDB71A78165F6A0890717F5FE736CE81DBAD1A9C4CDD5EF55B "点击放大")
5. AccessToken的使用：
   1. 通过ohpm-repo页面生成Token。
   2. 将Token配置在ohpm客户端的.ohpmrc配置文件中，配置示例如下所示:

      ```
      1. //127.0.0.1:8088/repos/ohpm/:_auth=readWriteToken
      2. //127.0.0.1:8088/repos/ohpm/:_read_auth=readOnlyToken
      ```

      其中//127.0.0.1:8088/repos/ohpm/是您ohpm-repo的registry地址去除协议名的部分，:\_auth和:\_read\_auth分别代表配置为读写Token或只读Token，readWriteToken和readOnlyToken代表Token具体的值。ohpm客户端执行info、install操作会优先使用只读Token，如果只读Token不存在才会使用读写Token。ohpm客户端执行publish、unpublish和dist-tags操作时只会使用读写Token。每种Token最多配置三条。
