---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:5c8481e12680307e5fc3ae81ffb46838bf1c1b726115fc615a288c9a92388aeb
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/5I2aLKAhS_yF5vFx6VJDmQ/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2F131B902064D212B278472A658597A8B76110C0625DF16EC19D67E90DE3758)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/T-gIf0MMS6aOhPT8Tt4G1w/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=D58AD4422F90CF387CE7CE5654AEE383F925671E27D766CC1A4B1787ED33185D)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/KEqHG3NNTT2WkeC9qKcwgw/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=18BA2E09E703BBD6D00F3D5D2D486D5A9795B346A16355E4FE195F697C235431)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/O6wdFfkuRpuqkSNs92OBVw/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE1E0976A2E0653F7A9C640DFEBD2E40BBDDB4D22083A83981CBF8ABC726F7AB)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/QqqUTA2IQWSem0JfNxeTyg/zh-cn_image_0000002821838249.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE7DF3B5F59B04D4B35344E77EC54B334D1AD7C4517FC65ECB27A338B41F2D5E)
5. 配置Wallet Kit服务参数：服务类型选择钥匙，服务子类型选择园区卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/r_UkCQevQFOuX4RbhbpOaQ/zh-cn_image_0000002821758251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=50DD2031FECA57D3ADD44EAFB4E09B04C1F85A7B2D0DF724FA4A98DF7E38F8C9)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“钥匙”。 |
   | 服务子类型 | 固定选择“园区卡”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：按需选择卡片激活设备限制，默认选择开通NFC能力，开通NFC能力，同时需要配置应用ID和文件参数，按需选择二维码配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Cvecs8GRQPWMnVZfQYBKpA/zh-cn_image_0000002793038314.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=F20D6BAC357602EDF83666485FC010A01D8827C3E05DAF91EBF262ADA09A0ABA)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 园区卡默认选择开通NFC能力。开通NFC能力，同时需要配置应用ID和文件参数。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 用于控制是否展示二维码。如果配置展示二维码需要配置二维码配置。 |
   | 二维码类型 | 用于控制二维码类型，如果是动态码需要提供相应API接口以便钱包实时请码，参考[生成展示二维码](wallet-park-scene-qr.md)章节实现。 |
   | 是否可反馈交易结果 | 用于控制扫码后是否支持跳转到成功页面，只有动态二维码才支持，静态二维码默认配置否。如果配置是，需要提供相应API接口以便钱包实时请求扫码结果。 |
   | 刷卡页是否默认展码 | 用于控制刷卡页是否默认展码。 |
7. 添加预览信息配置：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/UkBDXRieTfeUeY1dgP78Fg/zh-cn_image_0000002792878344.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=569A986376FB02C4A8699410D6DB71D0540F34DE6670D3864889988610446B17)
8. 详情页信息配置：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：按需配置是否展示前缀，文字颜色，文字位置以及字段位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/BEeK2AnGTH6-lZXLYqKlIA/zh-cn_image_0000002821838251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE23EBE60AA712BFDACDAC370E1B13205A9B84F311FACE17D9FE21BA308EA3F1)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：按需配置充值和卡片信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/u-p2EdfXTXGwgLPCPcHCJA/zh-cn_image_0000002821758253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3EAF38BE8B90BEC4CFF123B10668292232CB0114BB6D5276D3BD9584CEDA058)

   | **参数** | **说明** |
   | --- | --- |
   | 充值 | 用于控制详情页功能区的充值功能，如果需要充值功能，需要按需配置充值跳转链接，在卡详情功能区点击充值可以跳转配置的充值页面。 |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/ojqPjHqAQMKQUewQdbt6gA/zh-cn_image_0000002793038316.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A8D00D3117E721C44A79DA58CCEAAD5F8B49441A041CA64EF3E90D6C7A7460D)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/IA5s0xaWThamYHvRcKmWyw/zh-cn_image_0000002792878346.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8895CC6C4A76A800A16CE4583358E694B72AD01EB990905E924AAE8FE3C7C0B)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成园区卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/QuJnNoHASjmEwIkIVMk4cg/zh-cn_image_0000002821838253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011113Z&HW-CC-Expire=31536000000&HW-CC-Sign=B71E1AF92ACF3BE9CC6F9CB74370512B33628830165D066C940A2D55AA13301F)
