---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-release
title: 发布资源包下载任务
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 发布资源包下载任务
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c8e29ccf283beed5a17806fc36b10448003b5b59d6be4d9fe4cb78318504e44
---

在AppGallery Connect支持创建“使用华为CDN”或“使用三方CDN”的游戏资源包下载任务。

## 前提条件

* 已准备好游戏资源包并加密，且自行保证游戏资源包的可用性。资源包支持的格式请参见[上传至华为CDN的资源包文件支持哪些格式类型](graphics-accelerate-assetdownload-faq-1.md)。
* 游戏资源包支持使用三方CDN或托管至华为CDN。若使用三方CDN，请提前将资源包上传至三方CDN服务器。若托管至华为CDN，将在AppGallery Connect上传资源包，一个下载任务中的每个资源包大小不超过2GB，所有任务的资源包总大小不超过150GB。

## 进入申请页面

登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“APP与元服务 ”，在游戏列表中选择游戏后，选择“分发 > 服务 > 资源包后台下载申请”，在页面右侧点击“申请”。

说明

* 若列表中有“审核中”、“预上线”、“已发布”、“任务暂停”中的任一状态任务，将无法点击“申请”，需要终止该任务后才能申请。
* 资源包下载任务的状态说明请参见[下载任务状态说明](graphics-accelerate-assetdownload-release.md#下载任务状态说明)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/FiJT7Np5Ql-e_WaodOMYVw/zh-cn_image_0000002589325089.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=49BBC179654ABD75787C16469D0BEB240894910CFD79F10F6189B10BCDADDD21)

## 创建下载任务

### 资源包下载方式一：使用三方CDN

说明

已提前将资源包上传至三方CDN服务器。

在“资源包后台下载申请”页面填写资源包信息后，点击“提交申请”，提交资源包下载任务。若暂不提交该任务，点击“保存草稿”，允许继续编辑后再提交申请。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/hzuRfgILRAmYk3fYvkZR8g/zh-cn_image_0000002589245025.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=8F24228ADE464DD43ECB98B179D06C6CCB39F4A0ABFEE02BA1045A0DBB08C961)

| 配置项 | 填写说明 |
| --- | --- |
| 下载类型 | 请选择下载器，建议根据应用自身是否有下载器进行选择：  - 应用自身无下载器，建议选择“extension系统托管下载”。选择后，将由华为提供的系统下载器下载游戏资源包。  - 应用自身有下载器，建议选择“extension协同下载”。选择后，将由应用自身下载器下载游戏资源包。 |
| CDN | 选择“使用三方CDN”。 |
| 指定下载时间段 | 用户向三方CDN服务器请求下载游戏资源包的时间段。步骤如下：  1. 打开“指定下载时间段”开关。  2. 点击“添加时间段”，指定开始时间和结束时间，最多可支持添加20个时间段，且多个时间段不能重叠。 |
| 包体大小 | 填写已上传至三方CDN服务器的资源包大小。 |
| CDN域名白名单 | 英文逗号隔开，最多添加20个。 |

### 资源包下载方式二：使用华为CDN

说明

除了支持在AppGallery Connect“页面”方式创建“华为CDN”的资源包下载任务，还支持开发者使用“API”方式创建“华为CDN”的资源包下载任务，详情请参见[API接口](../AppGallery-connect-Guides/agcapi-res-pkg-preload-0000002362269981.md)。

在“资源包后台下载申请”页面填写资源包信息，具体步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/9J697m7zRMe9M7hVnDjd0A/zh-cn_image_0000002558765220.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=E91D23C452FCA42AD11708206ABE1527F5E55D34E62F1F1E3FDBCCF90E62F39C)

1. “下载类型”请选择“**extension系统托管下载**”。
2. “CDN”选择“**使用华为CDN**”。
3. **设置资源包下载的开始时间和结束时间**。要求如下：

   | 要求 | 举例 |
   | --- | --- |
   | 开始时间和结束时间的生效时间均为用户设备的本地时间。 | - |
   | 开始时间和结束时间只能选择到天。 | - 开始时间选择2024年4月2日，则默认开始时间为2024年4月2日0点。  - 结束时间选择2024年4月10日，则默认结束时间为2024年4月10日23点59分。 |
   | 开始时间和结束时间最长间隔为14天。 | - |
   | 资源包下载申请只有华为运营审批通过后，才能正式对外发布，因此请提前1~3天申请资源包下载任务，给华为运营预留时间进行审批。 | 申请资源包下载任务时，开始时间选择2024年4月2日，结束时间选择2024年4月10日。  若华为运营审核通过，正式对外发布的时间为2024年4月5日，则当前资源包下载任务只能从2024年4月5日开始执行。 |
   | 游戏资源包在用户客户端最长保留时间为14天，开始时间需要根据游戏首发或游戏发布更新版本的时间合理安排。 | 申请资源包下载任务时，开始时间选择2024年4月2日，结束时间选择2024年4月10日。  下载任务在2024年4月2日审核通过并对外正式发布，此后符合条件的用户设备就会将资源包下载到设备本地，直到2024年4月10日任务结束。  但您在4月25日才在华为应用市场上架游戏的最新版本，而此时用户设备的游戏资源包已经过了14天的最大保留时间，系统会自动删除设备本地的游戏资源包，从而导致用户下载游戏后无法加载下载的游戏资源包。 |
   | 开始时间设置后如果更改，则结束时间自动清除，需要重新选择。 | - |
   | 如果审核通过的时间已经晚于下载结束时间，则审核通过后任务会直接变为“任务结束”状态。 | - |
4. **填写资源包版本号**。版本号用于跟踪不同资源包的下载任务，版本号要求不超过9位的整数，且必须高于已创建任务的版本号。重新编辑“草稿”、“预上线”、“任务结束”状态的资源包下载任务时，资源包版本号也不能低于已有的版本号。
5. **上传资源包**。在“上传资源包”栏点击“选择文件”，上传提前准备好的游戏资源包。

   说明

   * 同一个开发者支持上传至华为CDN的资源包总大小不超过150GB，且历史任务的资源包文件最多保留半年。
   * 上传资源包文件的过程中，若提示华为CDN空间已满，开发者应删除历史无用的资源包文件或下载任务。

   资源包上传过程及最终状态分为如下几种：

   | 游戏资源包的文件状态 | 处理说明 |
   | --- | --- |
   | 上传中...进度x% | 等待资源包上传完成，如需停止上传，可以点击“取消上传”。 |
   | 上传失败 | 检查网络是否正常、资源包大小是否超过上限，如无异常，可点击“删除”将游戏资源包删除，并重新上传资源包。 |
   | 扫描中 | 等待游戏资源包扫描完成。 |
   | 扫描不通过，可能存在病毒 | 点击“删除”将游戏资源包删除，并检查包体中是否存在病毒，修复资源包后重新上传。 |
   | 扫描通过 | 表示游戏资源包上传成功。 |
6. （可选）填写hotversion。开发者可以通过hotversion版本号指定下一级文件的存储路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/fRdiGY_PRkCmSQUtOi2ekA/zh-cn_image_0000002558605564.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=99A278B1858D2DCA040539006015C43D7A823F0CCDAAE2B1AAAF0472DA0636CC)

   例如，资源包版本号为2.1，hotversion为2.1.0，资源包文件的存储路径如下：

   ```
   1. └──appid  10035                              // 游戏APP ID
   2. ├──v2.1/                                  // 资源包版本号
   3. │  ├──v2.1.0/                              // hotversion
   4. │  │  ├──button.png?v=20240223            // 资源包文件
   5. │  │  ├──font.ttf?v=20240210              // 资源包文件
   6. │  │  └──font.ttf?v=20240213              // 资源包文件
   7. │  └──v2.1.1/                             // hotversion
   8. │     └──font.ttf?v=20240214             // 资源包文件
   9. └──v2.0/
   ```
7. **提交资源包下载任务**。点击“提交申请”提交资源包下载任务。若暂不提交该任务，点击“保存草稿”，允许继续编辑后再提交申请。

## 提交下载任务

在[创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)时已提交申请，可跳过当前步骤。

在[创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)时保存为草稿，请继续编辑后再提交申请。具体步骤如下：

1. 在任务列表中找到“草稿”状态的任务，点击“操作”列中的“编辑”进入申请详情页。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Dg2ixscxSqS3JwVUHITtAg/zh-cn_image_0000002589325091.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=BDADCACABE4E7D9642E05B8116EE7A239259C398B282A2DE4DACD53E4ABC3606)
2. 在申请页填写资源包信息，填写要求请参见[创建下载任务](graphics-accelerate-assetdownload-release.md#创建下载任务)。完成后，点击“提交申请”提交资源包下载任务，当前任务状态变更为“预上线”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/CdMjpHoCQv-ZCibKjVdGMA/zh-cn_image_0000002589245027.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=043AC38EBD2671723B4D38686657DF08A566C19BA3021F768F71FB1EE628D42B)

## 测试下载功能

正式发布下载任务前， 请在本地测试“预上线”状态的任务是否可以成功下载资源包。

### 打开资源包自动更新开关

请在HarmonyOS 5.1.0及以上版本测试设备的“游戏中心”客户端打开“我的 > 设置 > 服务管理 > 游戏服务”，打开“允许资源包自动更新”开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/2XD2zY_lRouUKws5uaJm8g/zh-cn_image_0000002558765222.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=BB3379E8DB5495BDD4910D8A8B03914525399A0D78B407DF8D009C1F6DEC3E7B "点击放大")

### 配置设备号

1. 输入如下命令行，获取测试设备的设备号。

   ```
   1. hdc shell bm get --udid
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/5K4hsTzrQuigORGp77tmtw/zh-cn_image_0000002558605566.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=7F45358D9E36B6AF05884D08E3D9ECB409AEA8F7B5D6F9C04F5EB46A542EA118)
2. 在AppGallery Connect页面点击“测试设备”后的“编辑”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/6mHYptxMQZGPPJCWbT7yRA/zh-cn_image_0000002589325093.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=F86AE327A1E2C66F727140253AE1AC301E7C0EE32F1CA8EB47AF17E65F487828)
3. 在输入框中最多添加10台测试设备的设备号，且使用英文逗号（,）间隔开，完成后点击“保存”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/CfDflKYuST2bbkWD-nqCQw/zh-cn_image_0000002589245029.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=249ACBFBE4AA9049E3A29DEC4CD62CDD7E0079AAC1B140FF0C58BD6AC799C992)

### 验证方式

1. 如果游戏未安装，则安装游戏。

   ```
   1. // 输入命令行，安装游戏。
   2. // "entry-default-signed.hap"为示例包名，请根据您项目的实际包名替换使用。
   3. hdc install .\entry-default-signed.hap
   ```
2. 如果游戏已安装，则执行模拟设备闲时命令。

   ```
   1. // 输入命令行，模拟设备满足闲时条件。
   2. hdc shell hidumper -s 1904 -a "-s 66272 7800"
   ```
3. 验证以上两个场景是否触发系统后台下载资源包：查看测试设备的通知栏出现下载任务，则系统后台下载资源包功能验证通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/RjZf3rdtQLGCfhM4jLXAAA/zh-cn_image_0000002558765224.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=28D880E36EF9BA5D6ED58C3F7F62F4740899DFD550AE0B6BC06B95E1CA920809 "点击放大")

## 发布下载任务

1. 在任务列表找到“预上线”状态的任务，点击“操作”列中的“发布”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/TmB33qjUQyqJeL8Ttp1uEw/zh-cn_image_0000002558605568.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=AD9D01B97D3878B21609B953DD9B22C1CDF3D7993E893680E2D9D0A12601BD93)

   在弹出的提示窗中点击“确认”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/pPYcajmySX-XDlAesggBjw/zh-cn_image_0000002589325095.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=329939F38CB26EF603EDCB637CE897FB7100620A67F0B56A89EAD0276AB9E2C0)

   发布该任务后，华为运营人员将在1~3个工作日内完成审批，请耐心等待。

   任务通过审批后，游戏资源包将在指定时间内向满足条件的用户设备进行推送。
2. 若需要终止已发布的任务，可以在任务列表中主动点击“终止”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/1AWEba2UQDicpaZzwIG6QA/zh-cn_image_0000002589245031.png?HW-CC-KV=V1&HW-CC-Date=20260429T053629Z&HW-CC-Expire=86400&HW-CC-Sign=14DEB52EF47203A8571B976A72EFF0CD2D2BCD137173B534A23AEDF03907A009)

   此时，系统将不再对该资源包进行自动下载。对于用户设备上已开始下载的游戏资源包不会立刻删除，而是在下一次启动自动更新时，删除下载时间大于7\*24小时的游戏资源包。

## 下载任务状态说明

| 序号 | 状态 | 说明 |
| --- | --- | --- |
| 1 | 草稿 | 填写信息后保存为草稿后的状态，草稿状态的任务支持“编辑”和“删除”。 |
| 2 | 预上线 | 提交申请后的状态，任务可以在这个状态下进行资源包下载测试。预上线状态的任务支持“发布”和“终止”。 |
| 3 | 审核中 | “预上线”状态的任务点击“发布”后的状态。审核中的任务不支持执行任何操作。 |
| 4 | 审核不通过 | 任务点击“发布”后提交到华为运营人员审核，审核不通过的状态。审核不通过的任务支持重新“编辑”。 |
| 5 | 已发布 | 任务审核通过后任务正式发布的状态，发布中的任务仅支持“终止”。 |
| 6 | 任务结束 | 本次下载任务执行结束或者被华为运营人员终止了任务。 |
| 7 | 任务暂停 | 被华为运营人员暂停了任务。 |
