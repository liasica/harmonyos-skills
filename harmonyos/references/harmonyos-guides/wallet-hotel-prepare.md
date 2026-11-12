---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:74d383872b849c04ed97aa4d508e570a27b01800b38adf07664b5fe7a217d290
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/eHEIWanyRQuKH1mqg5yusA/zh-cn_image_0000002786520542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FB1B8A5326E16A1C07C62D4506A8BAF8B3390FB403D43C4747E622DE17F5D9A)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/6zFTfKb_SbWaUF9U9t7M4g/zh-cn_image_0000002786360614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=086FF578CA414732AADD8188C346A66B4BFD7B62E5F34AB3F854A0AA99F7152D)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/P0Fnqu3vQxWCI3CCiJ6ghA/zh-cn_image_0000002786360616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=E300472E8BEFDAF88C556F9517F02AB10154DBB9AD3B5A2BF644B23AE466FCE8)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/xu5MNVupRYKush3m2VtXnA/zh-cn_image_0000002815560037.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC103F0FEFDB4F0F5AB4379251726DDE3B6AEE232060B6E0B2CC6CF6A7A35AC4)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/8kxO9rEySCOQpXHud3KG9w/zh-cn_image_0000002786360626.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=91A3E9C300C83733E0B581725C9D5D1C1E53BBBB835501CF96B1A8F3FEC1EC21)
5. 配置Wallet Kit服务参数：服务类型选择钥匙，服务子类型选择酒店卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vPEm3Z4nRkiCGH_sPQ2t0Q/zh-cn_image_0000002815560047.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1DB2AE83A18B5568968125D56B7AAE0F18F18FFB28943AD4AA70AB82D3C6F8D)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/wZVs-5yyQt2IhUwesLkc6w/zh-cn_image_0000002786520570.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=000079CEA5AD71E824284CDCEA08076CF8349CA5AE807CA9EC70910E93FCEE54)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 固定选择“是”。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 固定选择“否”。 |
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/NhDFxUpTTvKW7UrHkAW3EA/zh-cn_image_0000002786360642.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=80D46780168D42034F713BF5B2CE70F7F394C96334777A33134865B10CC8115C)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/xlGTcRXoT4a76O6Z93mqxg/zh-cn_image_0000002815560063.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=557204B0E009231391B3992EFB583F122B511169E0CE794A57770E0FF41F85DF)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：按需配置详情页功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/I0ZAEQEQR8uvCfwJWS2gCA/zh-cn_image_0000002815400147.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DEEA05119797BF9D66C8D9B1C066FAB983DF864017154C78AE7DC877B99400E)

   | **参数** | **说明** |
   | --- | --- |
   | 刷卡 | 支持刷酒店门禁及梯控能力。 |
   | 查房间号 | 查询当前预定房间的房间号。 |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 支持钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/gV4VsBBQSlKc8qaqeGrNsw/zh-cn_image_0000002786520572.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=D01329A32FB500119CA302D4228F7317976C28007680E444069498F5D7EE0056)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ylPDm_0xTGyL-KEzwNE3BQ/zh-cn_image_0000002786360644.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=D99A3B26702CADA77D852AC37442DB85F50958FEABDE3BAA70D0CCF71E4079CA)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成酒店房卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/fsPw8QXJTcyOarcNqpqyVA/zh-cn_image_0000002786360630.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CDD5CA9DEBFF908A1E0A81F0F115450B3824D676C13EA1AFAB20107EDA06B1A)
