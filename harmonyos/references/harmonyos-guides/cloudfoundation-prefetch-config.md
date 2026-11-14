---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-config
title: 配置预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 配置预加载
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ccfd1d26d7d973b082b33b1a6fa8b980df52ed6e8362a4fa8318f905efecd13c
---

安装预加载、周期性预加载和跳链安装预加载需分别进行配置，且三者均可通过云函数和开发者服务器（即HTTPS请求）两种数据来源方式来实现。

对于不同类型的开发者，支持的数据来源方式有所不同：

* 个人开发者：数据来源默认选择云函数，且仅支持通过云函数来实现预加载。需要开通云函数服务并创建函数才可以配置。
* 非个人开发者：数据来源支持云函数和开发者服务器两种。可根据实际需要进行选择。

下文介绍如何配置两种数据来源方式的预加载实现。

## 数据来源为云函数

### 前提条件

* 已[开通预加载服务](cloudfoundation-enable-prefetch.md)。
* 已[创建函数](cloudfoundation-create-and-config-function.md)。

### 绑定云函数

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/bmv5Wa0gQc6vx2oppcVCyw/zh-cn_image_0000002788307992.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F678AA58084521F701FF05AA408A5B8544219E952142C2D25E9F7F829AE4137)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“云函数”，然后点击“函数名称”后的“修改”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Wp_fVPeITiyyOMI6NrHHYw/zh-cn_image_0000002817427355.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=7811DC67217106FC8A0A53B5C489BCBB6BD4CC1648D4AF9C1864783787273CCA)
5. 以“周期性预加载”为例，在“函数名称”下拉框选择实现周期性预加载的函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/h5_jhXsiSGmZg-8HKXfgog/zh-cn_image_0000002788467936.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=E433F7232F7808E0BCD897337175E48EE3B6ABA63810C3F7C2980D26482C2B69)
6. 点击“保存”完成周期性预加载配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/7Cszeg2cSp-3i1SBqpGegw/zh-cn_image_0000002817507425.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC4C83439924CE34172137319DC3CC0D3C8FEBF8E3F906F7CDC8CE7BDB7819BC)
7. 若配置“安装预加载”或“跳链安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改绑定的云函数，只需点击“函数名称”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/rs4U8KTiQh-6moY_PXToEg/zh-cn_image_0000002788307994.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=74B4DC02ED419C8296257F413106043F26889356C3059C2019F543A31C8F7981)

## 数据来源为开发者服务器

### 前提条件

已[开通预加载服务](cloudfoundation-enable-prefetch.md)。

### 配置服务器地址

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Uix_yNrJSMi8NnySMsmbNA/zh-cn_image_0000002817427357.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=694F12FD240FBB6238DC00DAC448595945F8DB461987F5A6A442463838C02A7F)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“开发者服务器”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/amz35LvwTbytf0qz6JDRLQ/zh-cn_image_0000002788467938.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D792557C1C65A0ADE6CC01E32C419B823B7F07CB6E85A69B3391D1E73DE748A)
5. 点击“下载地址”后的“修改”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/gemROxXFSYe6YrKXlthMFA/zh-cn_image_0000002817507427.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BA7B25CF05DE0BB6F04A1A827A70FB09E49BD4673CC785329BC5D2093DCA6EC)
6. 以“周期性预加载”为例，“下载地址”以“https://”开头，输入框中输入服务器地址，配置完成后点击“保存”。

   需要注意以下几点：

   * 仅支持填写一个服务器地址，需包含预加载资源接口路径，如图中示例：prefetchData。
   * 域名：须填写完整的域名。例如www.example.com，不可写为example.com。
   * IP地址：须填写准确的IP地址，确保没有输入错误。
   * 端口号：如果要指定端口号，可在服务器地址后面以冒号分隔，例如https://www.example.com:443。HTTPS协议的默认端口号（443）可以省略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/AiFJn8s5TIuUl-l6a1-hxQ/zh-cn_image_0000002788307996.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=88A5B4B964325CACDFEE221C71F5AB8158981A585E54EDF9DA81213CBB56C683)

   后续AGC会周期性地向该处配置的开发者服务器（即下载地址）发起一个HTTP GET请求，其中包含的query参数请参考[开发者服务器接口规范](cloudfoundation-prefetch-cloud-interdev.md#开发者服务器接口规范)，获取到数据后会将整个HTTP body缓存在本地。

   **说明** 

   * 开发者服务器接口返回的数据内容需仅包含文本、图片、视频、音频等供页面展示的静态资源，不支持包含代码、脚本等动态数据。
   * 开发者服务器接口返回的数据类型为其自定义格式的JSON或字符串数据，大小需限定在3MB以内。
7. 若配置“安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改下载地址，只需点击“下载地址”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/I1WX_jUkQDCBfMXWyuzHmg/zh-cn_image_0000002817427359.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=99B59846C19D1DD968229334F35A6FB1BEF4AD6775BF548036847FBFC7AA4A8B)
