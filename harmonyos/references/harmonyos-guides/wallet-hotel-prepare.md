---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:6b3478d34e972a2c6b706b2fcf0d276d0ecf5f43ff0742564f220c9000a0b49b
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/EyNB1_czS7OLChaZOvGJxg/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8C8812F02AA7AD4AB5FF293A3FB9E6462C9F9F336DFCA88A7C92E700C6FDB51)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/AlyNmz2MSzaN_CGy5yeklg/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CE08567ACF9ABCE260D4CEF26E735607368198B4B7786C3AD01521C00E727B1)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/dmhRLijlSIGt9bQYy0kkXw/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=32376E32FF16CB5EFAA62774CB406001A160BFAA7760255DB7B95DBDA28DDC9D)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/abUWLm_ZR5OaSgJUBv7w8g/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CEBE4CB8ADF091E6400C3D6A7DFC1F0392079357310A93E09FCFBA30F7D825E)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/2aKKuNJhQaGA3BTFOFSxMA/zh-cn_image_0000002817507791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=45839A09F0BA05E1128CDB89D4074404646A36CD934588D4E56D23984973170B)
5. 配置Wallet Kit服务参数：服务类型选择钥匙，服务子类型选择酒店卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/4ZX17-ivQWKkrp3LvpwLGg/zh-cn_image_0000002788308360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=93F723C2AD28BBBDE0E9837C28314BC67E200C4162677BCEC396B1A70D7504DD)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/rpsRE1F_SRSGDzgXamUO8g/zh-cn_image_0000002788468318.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=362E3F48CCAEC9CA646ACBAF1FBD5E964D02973DEC9CC80BB45B192B69D56224)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 固定选择“是”。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 固定选择“否”。 |
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/pcGJUggQRRCMr7HYwAJ8ug/zh-cn_image_0000002817507807.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4FCF6152D29AD8277EE2A88C4AEF9C11AD7E5951033BC0213CA300E95BFC9FB)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/nzK_3KkDReOTNR_shP5ILQ/zh-cn_image_0000002788308376.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=330D942D499BB6632A2A59F898791AAEB25FA53BC2B714E09A4985D126BD5D8A)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：按需配置详情页功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/01d7wfxDRleDdu9I0TqFDQ/zh-cn_image_0000002817427739.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD9C2AE9333028C67764226BB52F07AE1761EEF5AC36E2EB24CCA7433EBE0291)

   | **参数** | **说明** |
   | --- | --- |
   | 刷卡 | 支持刷酒店门禁及梯控能力。 |
   | 查房间号 | 查询当前预定房间的房间号。 |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 支持钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），是否提供使用记录查看链接，选择后按照提示配置即可，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/5wAh6LfcRdeemY0sRT39Fw/zh-cn_image_0000002788468320.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6606FEA77F8A80BC156DA50A96F829F2E72B9762056A81F66F2A40BB38C68A7)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/f38cvfcHTv2AiGrVJN6HuQ/zh-cn_image_0000002817507809.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=3195921D7DB1B084B3ED2EBB3230395C15A63EA189C807D5006F76918DEDE7C4)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成酒店房卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/LdAVtOBbQPKil27e0SNxaQ/zh-cn_image_0000002817507795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=405AB497565E9D4AF8A635139A62A737121DCE9FA3109186E5B79607C4EB46AD)
