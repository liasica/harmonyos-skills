---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-preparations
title: 创建Wallet Kit服务
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 创建Wallet Kit服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5dde83322dd2813708a019c355abbb30e5e42e711913ebf76369c3a7410c8625
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“我的项目”。
2. 点击进入对应的项目，在左侧“项目设置”页签，上侧导航选择“开放能力管理”，打开华为钱包的开关。用于钱包对车钥匙管理台向钱包服务器发起http/https请求时的权限控制。关闭状态下，开发者服务器将访问不了钱包服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/Ga-Ux62oSGaRMqOp5f5HJg/zh-cn_image_0000002558606040.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=E2D9F7EF0EE7FFE97CAC5606BD471F5141AE24952C665BD252883C42B3776F83)
3. 在“项目设置”页签，左侧导航选择“盈利 > 华为钱包”，点击“申请Wallet Kit服务”，进入申请Wallet Kit服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/SXSeAzyDQbiEYmIzyAajCg/zh-cn_image_0000002589325567.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=0B3D0249121689CB2E1B082627DB472FF933D063B10796EF4333F0ECF371D52F)
4. 点击“产品接入华为钱包服务”的“点击申请”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/M3k_PzjTSyKaBYAjNsGKRQ/zh-cn_image_0000002589245505.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=489FDF40BD0B2AD701680210679CA434A49EED96D7E3F05D46FD39809154A71D)
5. 各业务场景对应的参数有差异，具体参数请参考各业务的Wallet Kit服务基本信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/V4p7JY86R-W8KouAICpqZQ/zh-cn_image_0000002558765698.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=0A568FFC512E9431E654060B684FD729C937E787CFCE78D6B10EE171A56B92B1)

   | Wallet Kit服务参数名称 | 参数值 |
   | --- | --- |
   | 服务类型 | 分为卡、票、券、钥匙等，暂时只支持车钥匙，交通卡服务接入请参考[接入交通卡](wallet-transport-overview.md)。 |
   | 服务项目 | 服务项目依赖所选择的服务类型，不同的服务类型，有不同的服务项目。例如当服务类型选择“卡”时，对应的服务项目有：“会员卡”、“礼品卡”等。 |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。 |
   | 服务号 | 用于Wallet Kit服务器区分不同的服务且保证唯一性。 |
   | 接入方式 | 国内支持三种接入方式，App接入，云端接入，代理接入。商户可以根据自己的需求选择适合自己类型的接入方式。选择云端接入时用户需要填写“回调地址”、“用户公钥”二项资料，选择App接入则只需要上传证书请求文件生成证书即可，选择代理接入时用户需要填写“回调地址”一项资料，而用户公钥则会发送默认值到Wallet Kit服务器。 |
   | 回调地址 | 开发者提供给Wallet Kit的地址，用于Wallet Kit回调开发者，用户领卡成功或删卡时回调开发者。  注：如果不需要Wallet Kit通知开发者用户领卡或删卡的状态，可以不填该字段。 |
   | 用户公钥 | 开发者将生成的公钥复制粘贴到此处，后续该公钥将作为Wallet Kit服务器认证开发者身份的方式，参考如下公钥生成方式。 |

   **公钥生成方式：**

   （1）配置好node执行环境并使用文本编辑器新建文件，拷贝以下代码到文件中并保存命名为generateKeyPair.js。

   ```
   1. const crypto = require('crypto');
   2. // 生成密钥对
   3. const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
   4. modulusLength: 4096, // 密钥长度，不少于4096
   5. publicKeyEncoding: {
   6. type: 'spki', // 公钥编码格式
   7. format: 'der' // 公钥输出格式
   8. },
   9. privateKeyEncoding: {
   10. type: 'pkcs8', // 私钥编码格式
   11. format: 'der' // 私钥输出格式
   12. }
   13. });
   14. console.info('生成的公钥：');
   15. console.info(publicKey.toString('base64'));
   16. console.info('生成的私钥：');
   17. console.info(privateKey.toString('base64'));
   ```

   （2）打开命令行工具，执行**node generateKeyPair.js**命令。

   （3）从结果中拷贝生成的公私钥并保存。结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/aUj5UzrdSfiXyBHl-jUDGA/zh-cn_image_0000002558606042.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=84938DAFECEC2068AFAECE47AC3D900E2435E150B0A68D37B6A2FDC14EDA9E8D)
6. 点击“下一步”，进入NFC参数设置页面，各业务场景对应的参数有差异，具体参数请参考各业务的NFC参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/kxzAkDb5RcGKqd55mdeoeA/zh-cn_image_0000002589325569.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=813E5EB839FF5F2099CA8E98CBDAD11B7488D18B1EC560682D9BED8DE8FA7113)

   | NFC参数名称 | 参数值 |
   | --- | --- |
   | 是否支持跨移动设备同步 | 用户领取卡券后可通过此能力在同一账号下的多设备中共享此卡券。商户默认选择“否”即可。 |
   | 是否开通NFC能力 | 服务类型为门钥匙、一卡通、门禁卡、社会保障卡、港澳通行证、护照时，需要开通NFC能力，同时需要配置应用号和文件参数。其余的服务类型可以选择不开通NFC能力。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位），建议以“A000000048575041590100”开头。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
7. 点击“下一步”，创建完成后，返回Wallet Kit服务创建页面，可对所创建的服务进行查看、修改和删除。
