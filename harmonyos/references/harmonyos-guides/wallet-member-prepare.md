---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:e8deddf9c1ac96d033a7a5500e48ca05ca8b6301ca2befa8ab90f79e7838b384
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/4hvGTSSeRXuvRL4QCxYMHw/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDE13F7144C07D19F3673127E1AEB779BFAD2F00DE02BD642DE27FA9700F581D)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/-pDlH30CQn-8uRs3tdk18g/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA919AD60E2249C58D8982F1B5FD1A944159E777999A95A70B5DCD486DCA40AF)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/2pF-Uuw-QliverhHnTyaxg/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=579106EA71B7EEEC829CD7D7AAF8C9DE05CD597294407A67EC3FB825E615B8CA)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/nAmx9biwSCOk3GC124vZoQ/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=80CA2926ACC5834907AEACD92A040406D590F5EB5603B43890856313798F842D)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IgzxdwqvRQSRb_wwPFEOFw/zh-cn_image_0000002821838249.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=5734BA0E7B8503BAD8E9C682F8214DE5FA47EFAC11A90F366146EB329C513075)
5. 配置Wallet Kit服务参数：服务类型选择卡，服务子类型选择会员卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/9PJNqqF3SKSyjjazsJTxCA/zh-cn_image_0000002821758251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDBC71249BC1AA4F2514B4766E925095599DC3E3D6B6F5DEA42220A38C26581D)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/5NRKHAK4Q8OIrYDUdnawUg/zh-cn_image_0000002821758259.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=336FB04007D5E96C7C808996116F489C6C9D06E323A8FC4F2AE81FBEA7871223)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/vTTMw0WRTmyz5Q3zIcd30Q/zh-cn_image_0000002793038322.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=56E2C1D6D9EF68B8AC5F190F2D019C944739279E5887BD83AB04BA51BC1BBA67)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/mh0mzeMOREyjrrYcm-qZ-g/zh-cn_image_0000002792878352.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE122A819D07A5A4EBAD5699BECBB218290A465685C87676638879F9D3ADE6F5)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/dU2DUr3BTqe44mAfi95WNw/zh-cn_image_0000002821838259.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=8306A77367E4A0CC2560787F9C59121BAF9372576098D73B8DC4F987BE58FF65)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/UILs9IQpQXSkx9Eosf-l9A/zh-cn_image_0000002821758261.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E13853D217DF635DE076703D4DD3C986076DC243958B8E5A05F945655B2F643)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Fquo_wbbSCqNKt3BDHgxxg/zh-cn_image_0000002793038324.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=38E1D05A58C8E8B8B5BA56B6DEB028C00C7226F510C3EE0739972BB8571673A2)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成会员卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/dSzBc_u2RD-0DDIksAsZ_w/zh-cn_image_0000002821838253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=24C311488D89C607429CC7F428E3BFB1CA9C39CA829A5C192C0523D8D9807DBB)
