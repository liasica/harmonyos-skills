---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:c898aff869b122e7408a23fa485b920142fd94f369d75aa330f783018a1b0bf6
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/TPKXAMW3Tru9dr-DfgkBMw/zh-cn_image_0000002786520542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=1697CA0BF0B112E5158A5AF50FB4E84E1316D3517E0F571483D8F8D3DB5230FF)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/KJUXXRKGRX271qAcxKo_Lg/zh-cn_image_0000002786360614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6481584A3664869B3F09B4FA50ED5CF45CF7986F50EB407E7DDBD46E06753BF)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/q8ec6QkMSbuuOpuctl49Fw/zh-cn_image_0000002786360616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B36C777DA1780674D2DA173AB0CACA9355516E0E419976FE7458C64B11EF735)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/_MszAKz-RxmtJv-d5g8QxA/zh-cn_image_0000002815560037.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=42C391C8665CAC5859C713D8C91D87681EE1A8840142EBE7D756EBE2863624B5)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/yxo2X7x5S42TUG5m-oGyKg/zh-cn_image_0000002786360626.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=91374B90899E46D592BB15D33CC27914099E6AF8DEE273073CB7A966E6537BAE)
5. 配置Wallet Kit服务参数：服务类型选择卡，服务子类型选择会员卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/pgwnXxm9TUKbmkmM0fsgUg/zh-cn_image_0000002815560047.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A0B3B3F186A9E7AB2180D2FCD4E3389313CAB2653C2A58A0B72BB9DC120D26D)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Y5YpwaC-Rd2bazyQof64gg/zh-cn_image_0000002815560055.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=97D32AC2141B8BDA4FA0D51DE901A71F82DD2DCC250E794725B56B2502123173)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-Aw8ODllTNKR6yQuAhZDgw/zh-cn_image_0000002815400139.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=E040B71CABBCA75C18A8A69DCD48C30D6EE13E41695724D767CF6F557782E825)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/sju8kPQwSeSl1QkT96MJ0g/zh-cn_image_0000002786520564.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD8FADB182E8E6C270CAA315BDC42C0901FEBD53DBBA90CEF4E5C72F9CCC0399)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/f2ZjBg6PRP6CQyoC9xFSiQ/zh-cn_image_0000002786360636.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DA2BCFF94BC3C494449BA7C2DA762DC534D0CF7BCC865C2AC3E217741ECB0FF)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/C9K4toDrT4iWz-A939f71g/zh-cn_image_0000002815560057.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=53C06542F86CFEED22FF0CAB711F969263084B743C1D3F7AB491E63E53ABD145)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/fHS-_y_9TYmaPVgEVK15Xg/zh-cn_image_0000002815400141.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA4E751E945B96C205242A33FA56011BBB2FFFB366F08E0F8B0B65F35EB4425A)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成会员卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Omkv3YYgSFmEvApx98BPjQ/zh-cn_image_0000002786360630.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1D588E10138396EC610D8048018512F52FAA9B120D375B1945D2BB412802636)
