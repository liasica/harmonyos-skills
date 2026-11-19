---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:15+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:dd72e2154454ade275f6180a9e83112d5b8e2e1b227f53d55a0cb3cd48abdcdf
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/A5jls32UReS7xc3GRVZygw/zh-cn_image_0000002791566676.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=900D86FA594BE87F3DDA8D4D2E45A2F4C362035E2E7052022C7883173F41D4C5)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/9_bWOtzxR5ysXOV652bkkw/zh-cn_image_0000002820526629.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A842FCE5953F4EDB7CC04FE8847242CCB65382411BDCAF9A94C404FB1543B00)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/zUuPTBY6SzG3xkOFn26YYQ/zh-cn_image_0000002820526631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=B580D76A248E2C4E75E192A118658408ED8B028A5E0F0B103A6B42AFEB768D02)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DDaFabMXQmyI9CEKj2T2FA/zh-cn_image_0000002820406631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8AA02331F2E87C16D47778C7A64AA23C184E88E8629DDC2304A63061C565169)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/JfKyvPo3RAOgaXomKidQyQ/zh-cn_image_0000002820526641.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D7ABF884B34EFD38F510540FCCACF93F3351B79D3B9DCDB17E0C345EE95AAAC)
5. 配置Wallet Kit服务参数：服务类型选择卡，服务子类型选择会员卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/iqpRfI9OQTKzkIEFdkQq5Q/zh-cn_image_0000002820406641.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=A443B9B70CD597A7C7136ACD4DCD2B1DCAD39CAB5E0F4EF4B3F642C3243BD598)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/gOKpj7ZHTsu8tpp1kDSLCA/zh-cn_image_0000002820406649.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=01ACD7056B1E099C665A63DB5442F8AB55BBFA07380C5E7839A109359E64AE10)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/mMNmbys6Q_2YlWgDDG_Jvw/zh-cn_image_0000002791726670.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=8244F2C98C2DF2275B39E43DACD09D9FFC11CF22AB7C078B740D6033FA4CDDEA)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ebfX7eHmRlSlbX9BsjVBoA/zh-cn_image_0000002791566698.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F9CF0951EDF887B2BD4FDD079C9D12574C289CFB3C49A8A419392272878DF20)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/3acPqJ9QQj2cvIsfHtqnFA/zh-cn_image_0000002820526651.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=748D13EB72EBAD85028EA65E547B467BCFF5A1E625907E4BA9A99D606626820F)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/QMWeYKrcScWVasB4hoKsxg/zh-cn_image_0000002820406651.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8C952C82386A2506BF460EA9E6474FBBE0C99E14437B254307BADBAC64FA320)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/OMPy8_GES4mb1rbAK2zvmw/zh-cn_image_0000002791726672.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEBBC59538E75341EE69DCAE20E2371E10B7FC07246911237C40ED6F6F0E8235)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成会员卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/OgJ02h6nTza81Tq5fVu-tw/zh-cn_image_0000002820526645.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA8ADCC86B69783C19BC30657D5C2016D4A14795144D11A25251C9BA64479E5C)
