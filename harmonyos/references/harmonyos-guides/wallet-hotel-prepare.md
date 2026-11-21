---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:1c900339cc28d06e00cb8b535695c8a187703f171b537b17cd6f54ca3bd59d8a
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/W6BGiIGgStKqfA3CaeA9AQ/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=D30C8B65D4AB022B1948A16C75CC50C77EA110FDB5ED9F41CB30BC36EB63DF64)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Jtf2XussT6C7r_qfhn2fzw/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=703EACA6C016B16DC4E9C87E691B79E8003103D7383EB2AAC90AC0D5AA308F00)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/4oBDnMgnSjKHlB56qSmYFg/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F749A52FD1D65BC65EEF3D1D013E2979278AE62744FED5D7347E5C9F4E22B37)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/fh633a4kSielrD_2QPXFYQ/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=6164370501FF97F0D116C6B32186920E669E14267A5487116ABA4FE16DE50FE6)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/dHFZ-ktxQBargTzGIZTERg/zh-cn_image_0000002821838249.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9C20F514B3303BBD6E723E8E41E1D79842BD9AE498CF114B145CE8D6CBB4CDA)
5. 配置Wallet Kit服务参数：服务类型选择钥匙，服务子类型选择酒店卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/3dJmGLeTTVqGrOAYJ-Ba8Q/zh-cn_image_0000002821758251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=12465F40E18DD8B3AE3DE76137948847241EF89ED46437EBEC14B0F4B35B34C0)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“钥匙”。 |
   | 服务子类型 | 固定选择“酒店卡”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ESPDbXU-TOysbky4TrQDfA/zh-cn_image_0000002792878358.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFA300F2A1F8B718A7838E25F65818B20500002FAD35F9DF0079695D3588B95B)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 固定选择“是”。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 固定选择“否”。 |
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/kcMU2xRRRXmRIZWYs9H9kg/zh-cn_image_0000002821838265.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AE91E0B21FA3D30FA08A6AF19D57B8EB172E513CF88ED7D4CF2E63E48B095A8)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/DiKNJZbJSIamp5bmkJeHVw/zh-cn_image_0000002821758267.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DE95921A2E4D516C356E71E965DF8000F521F42761DBD4123C12AB30C3A0128)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：按需配置详情页功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/UsGyN7oqTgugFekOkM8tLg/zh-cn_image_0000002793038330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5051CBA6CB67229D6CBF8802736475693067FA7939727B3CFB83BF0C7B58C1F)

   | **参数** | **说明** |
   | --- | --- |
   | 刷卡 | 支持刷酒店门禁及梯控能力。 |
   | 查房间号 | 查询当前预定房间的房间号。 |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 支持钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/mM6wHiH2T7W64MN9X5Z8Mw/zh-cn_image_0000002792878360.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFCDF36983FC0320631979BEEC85E27046877ADEF0A428315E14399D7D3758A1)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/uJYLSzQBSsiESJSEpYLmxw/zh-cn_image_0000002821838267.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=E093CA957E5EC3CF43AA80E45AE7D0277CB64EDEA511B301FE5679D04DA28CBA)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成酒店房卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/1rBARqzgRjWnGnXE7QaV3g/zh-cn_image_0000002821838253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3BEDCD5F431A9ECB10C3BCB0F4D075B71C29002EEBF0C75672B97B82AAE131B)
