---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:367c708ffe3eabbfbfcb4b1f864e9c045043aa659bfef2b46db00cb92eb7fd38
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/KI6ouNydRiyXaHUoQ_TgfA/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FE2D5FD0CB87CB3C41176C0CC857F3195E6BE416C430ED3F71FEE0360919409)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qVVubsjzR3WFlk65qRqyYA/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBDDCE4CC3E949F7304B652EF320FAFC7CFF4B9A5B7F91F2C9A197FDEE4B8DC1)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/2ZjdsNuYSEqeF73PVy__LA/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=08A6316E3BE59008EFE0D4F542C1A26DCFC30CA1BEDEDABAF5641DA1E8CB4D57)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/0j8HL-sTROODbDJWkQnJVA/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBB5A64BCDAC4DFBBE5ADC6772F29B38F86B6554F7ED1E43719759766A7D610F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ze4k5QegRHSwsm-DHKz6FA/zh-cn_image_0000002817507791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6A7D9470B606E558BEEF2162F54BC4D4E3866907E2DD692EEF79A6B5970133F)
5. 配置Wallet Kit服务参数：服务类型选择卡，服务子类型选择会员卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/jsS0d23-QXOzXEhjrX03JQ/zh-cn_image_0000002788308360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BE265E3E87A1D027F095FBDD84960468388FCA6896D2E290D17FA235B910B5A)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“卡”。 |
   | 服务子类型 | 固定选择“会员卡”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：按需选择卡片激活设备限制，默认选择开通NFC能力，开通NFC能力，同时需要配置应用ID和文件参数，按需选择二维码配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Gk7FERx8TGaHoqsk1mJf_w/zh-cn_image_0000002788308368.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAB282023EBE09C452AC484AEC1244BB62A78073036BCC08D7ADA2B175C4F27E)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 固定选择“是”。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 用于控制是否展示二维码。如果配置展示二维码需要配置二维码配置。 |
   | 二维码类型 | 用于控制二维码类型。 |
   | 是否可反馈交易结果 | 用于控制扫码后是否支持跳转到成功页面，只有动态二维码才支持，静态二维码默认配置否。如果配置是，需要提供相应API接口以便钱包实时请求扫码结果。 |
   | 刷卡页是否默认展码 | 用于控制刷卡页是否默认展码。 |
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ffbxgLhcTgqObbfjebd5xA/zh-cn_image_0000002817427731.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EF82643DC6B9529E440709622646197BCF2C1133F4ADB3F385B78D277BED9AE)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/O8GnIq-1R1uyBhhiSBLFYA/zh-cn_image_0000002788468312.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC088544EC786B32476C6BB0457CA65616DCDF9E084B8F8F08AC1B8D041BB14D)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/22WGWiC1R62VKnFIA4fxBQ/zh-cn_image_0000002817507801.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=9742BC1E6AA576A3C984766EC94A65A023C18A563F554DB5BFDCF352BB84DD99)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/RNSSc0RBQuOgr76BQq0G2A/zh-cn_image_0000002788308370.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EFC47AA16A63D9F3D4E79112B5148ACFAE37EA36F50D35FC0967CF3A47F64D8)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Ac4sG7axRGmbCWKYhCprcA/zh-cn_image_0000002817427733.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=052D8EA523073488AC970B615620396830DFCC894EF218F074E3661C9C8720D4)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成会员卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/uVc9IobbSuSQG9HjENdfJA/zh-cn_image_0000002817507795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=628C101561994B8BFABE30D813901766A545195A2BB85BACEA197801A372E8DA)
