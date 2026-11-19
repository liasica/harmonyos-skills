---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:16+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:8adf7af0647c47cd4e845616cf760ea70cdc24983922218182da90a43b6330b3
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/i_GP4_b5Q8msJ7LAEc_UFQ/zh-cn_image_0000002791566676.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BD3AF2DCEC043C2042E66C6E6A02B6D4C47769E6109C1EB952747462B022D36)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/2EOT6LA4RDadfGXeWb-noA/zh-cn_image_0000002820526629.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5FB2419302CBD0337987D0B1973CBDAE5848D0BBF095F367AEAD148BF80AFA5)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/EVTG07RlRi6vSyxTzKQ5mw/zh-cn_image_0000002820526631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=07D159AFCA836E34EDA65A8313AD1FD7D7BD2BF188073E5AFB54F712B326D6A7)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/KGlJj9puTMeGqPZZgu8hSQ/zh-cn_image_0000002820406631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=51F86D9396AD3679A1A9D71D0DF9BF10B00FE44CCB89C9A2F9E2EE7E7B7CC7B0)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/enBXVp92S3WiN9TwVU8H4w/zh-cn_image_0000002820526641.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA74844E9460062EB83E65AF741C916CCF0C5E43A90761AAD21B50953C2E13AE)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择通用凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/XfPby1aSSkGX0q5yPGNg-Q/zh-cn_image_0000002820406641.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=F34CC6C8C94B012ABFC2E24F61260E7D48451DDB6953D4466742B2E7CDB9E7FA)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“票”。 |
   | 服务子类型 | 固定选择“通用凭证”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：按需选择卡片激活设备限制，可展码通行，但不涉及NFC，默认在用户华为账号登陆的所有设备可见，不支持动态二维码，推荐配置如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/kStk0H3cRGeKe7qoGCMz5A/zh-cn_image_0000002820406671.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=876A44AE1888F7042F21C92B666520CD23A96A68586E8538661CD84697A8ED8A)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/74fFqldFTkaND04toEB0NQ/zh-cn_image_0000002791726692.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B594DD3DE3BBA72CCE1E91AE5D45866462119A22D10F5458CE2A855885770F6)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际通用凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/mH2GuR6FQ3K25jAGw_g_CA/zh-cn_image_0000002791566720.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=22F1574498C756F37B2680660F8D5C474E73CB0E29265B5E42DE389D7B5EB83C)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Gyp0r7Z9Q4Cx6C3IhIQX0g/zh-cn_image_0000002820526665.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3965B8D7593B8730AEE588253C1AEAD5F43D94670B6DF0DE1A3006E284B1B0F)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/7rC2vdu-TUGQ3Kf8dVs66w/zh-cn_image_0000002820406665.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=52A5E63E3FDC3FD5844E6839372602C159662F86CA739054C76EF7A3A1C2FA0A)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/DDaARx9xQV--aIdAp_KFmQ/zh-cn_image_0000002791566714.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=693CB653EB3422F1B8B9B73A0C5BF2566F556594F6592AE7445A77CEBBEC74A1)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ArRyoQdISZGXTxiyFPySkQ/zh-cn_image_0000002820526667.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F000800F984EFED2C8253A68422DF1B16A9D8850264AF0B03C2B481BE637155)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/GHjklXSKStmYeCEJReV4kA/zh-cn_image_0000002820406667.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B74518C066A5AC1B3AD2B6560026228CB2306637D12D2B04CE00246B151A7C2)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成通用凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/vLvnM3lOQUiXS02bXni4Cw/zh-cn_image_0000002820526645.png?HW-CC-KV=V1&HW-CC-Date=20261119T014821Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D6B7D7D9A59D157478D1CAFDEB215CEFE1D0FE1F38A040468A9E92C405F9F9F)
