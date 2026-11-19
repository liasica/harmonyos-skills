---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:15+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:b25cdf71d9d2ee833e632be0bf15f70beede9ac97555365b5d3cc1efdf7f72df
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/h6MACgoNRRqF3v7LwxgK4g/zh-cn_image_0000002791566676.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=42024A201839F3F41096FB911AFC2A295DD39785FCE5FF64F82FFDA091A2CDE9)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/sn-3y4PrRbqYNHL8Wrwxfw/zh-cn_image_0000002820526629.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=45389FD3B8EA06E1E1162B558D0DCA65E48B935E870D13F59C58B536AB2B68EA)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/9cf9-9Q6SriVpJwT08_ceg/zh-cn_image_0000002820526631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=D54C0C2EE2C4D7F7D3CC5BDBB74D51BA41E95A7F81CE3DF8E142639707F24CD3)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/tz1BM9TnQdOQuFGPoaJiJg/zh-cn_image_0000002820406631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=59E31D22C2E1083DEEA593284E00BDF148BEDCEE22949D418F1D95DD9678320F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/1UUdCPaIT_GsPuaw7hXi7g/zh-cn_image_0000002820526641.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=82B1799C55FB45F1BAD4E8A171E0254B91FE0F680A127B3355ADB301432B0FF5)
5. 配置Wallet Kit服务参数：服务类型选择钥匙，服务子类型选择酒店卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/-DN4t3lPQYiVL9DCAlwQRQ/zh-cn_image_0000002820406641.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=00284F91C7F270EDE83F42C46A64D22AC79C94BB2860127875BAFE239DFD7176)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/WMkjyZh4S1mIt0goZWzjxA/zh-cn_image_0000002791566704.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7EC3149351DA5655F099F4DC0BA44692CD738C300B525A2F5DFD17DB9EA450A)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 固定选择“是”。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 固定选择“否”。 |
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/IBi4iCUjRaC8S6Euf8pqcg/zh-cn_image_0000002820526657.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=18D20385F002AC3FB880A47BF9C16B9B2358C158B393CD4747ECF5362FFA15C0)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Olt0WqIVSoaajQW3xVwebQ/zh-cn_image_0000002820406657.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A3B55ED622DAA8C054945FA1C5A9D29B3797FBD9A88CFE7016C403710C0D86C)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：按需配置详情页功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/QvzBPLUQSIuPjyBo6XNZsQ/zh-cn_image_0000002791726678.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7F2CE5E510F1EB14B0F3D25D93A666ABE89D452E543047DBC3667CC417E19B0)

   | **参数** | **说明** |
   | --- | --- |
   | 刷卡 | 支持刷酒店门禁及梯控能力。 |
   | 查房间号 | 查询当前预定房间的房间号。 |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 支持钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/UZZ8QolySyaiivvVlgFy5g/zh-cn_image_0000002791566706.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F1CA89C7B1AACD293D89E6E591AE7608C94996828AA47CAA9E6741605F8AAE1)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/q6PDeUXnTlaFO6DDULjFbg/zh-cn_image_0000002820526659.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=474EA47019379D3AD74CC50778F3BAE46CC7326DF14733A21B5FD644032BCCE7)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成酒店房卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/v0SgsTtKTFai-9DmbDuNeg/zh-cn_image_0000002820526645.png?HW-CC-KV=V1&HW-CC-Date=20261119T014915Z&HW-CC-Expire=31536000000&HW-CC-Sign=3ACAD2EE23D3AD91A7BBE2DF70DFFF572ABF28AB13FDBE48D3821A33CD289974)
