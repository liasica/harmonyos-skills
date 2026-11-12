---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-config
title: 配置预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 配置预加载
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ce0a711c6c977b3e585a9c62d31026dc602ea7c86eaaf9c985cf1f3d781a8c31
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VVbuV0o-RaWGYSNsIZRRew/zh-cn_image_0000002786520188.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=24BBA8DF0EBA3A0DFF0279B1A1853D140BF5A3D64726C7535884E8E2AFD987B8)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“云函数”，然后点击“函数名称”后的“修改”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/EY5OsksUSpaxaT03z2XXuA/zh-cn_image_0000002786360260.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B62C96A12C38CBDF96C068833060D930351D7071F9407464A33D393498760BDB)
5. 以“周期性预加载”为例，在“函数名称”下拉框选择实现周期性预加载的函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/5cZjX9e7SYuXjaLYpeyqlA/zh-cn_image_0000002815559681.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CB9101EF2CCC2728B4184A816ABB6BFC4DE3AA7761885FBE9369BF36F18888B)
6. 点击“保存”完成周期性预加载配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/0UHME68RSbKxmQBf71Nofw/zh-cn_image_0000002815399765.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AF7DC0041DBCFEA30D4E0C1287E61C17896B33120FA6BEBD94E82C58FCEBEE5)
7. 若配置“安装预加载”或“跳链安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改绑定的云函数，只需点击“函数名称”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ITJkaYqxQjuJf4Y5DjihzQ/zh-cn_image_0000002786520190.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EA12AE8E705D42F2B2BBF009E9D315C0BFFC37811FA17083D7230F1B37C19BB)

## 数据来源为开发者服务器

### 前提条件

已[开通预加载服务](cloudfoundation-enable-prefetch.md)。

### 配置服务器地址

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/oYRrDYsDQgO7gXXxrMeNOw/zh-cn_image_0000002786360262.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=54A07748467F64FCD5D1F440BC85B6DB8DA4443EF0BB17F6865ED9292F1F3C3F)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“开发者服务器”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/xS_P9TgcTu6aaOLs9wDJBg/zh-cn_image_0000002815559683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A186C7D78D8897E4FBAF3854F1C445FD37E38D397F62AD070E8E1D53702A06E9)
5. 点击“下载地址”后的“修改”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/gaZdUKGYTcGivaGyZgyOfA/zh-cn_image_0000002815399767.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FCB31CAFE27411312F28F5174DA337A81B66154AEFE0258447B0EA7940A579F)
6. 以“周期性预加载”为例，“下载地址”以“https://”开头，输入框中输入服务器地址，配置完成后点击“保存”。

   需要注意以下几点：

   * 仅支持填写一个服务器地址，需包含预加载资源接口路径，如图中示例：prefetchData。
   * 域名：须填写完整的域名。例如www.example.com，不可写为example.com。
   * IP地址：须填写准确的IP地址，确保没有输入错误。
   * 端口号：如果要指定端口号，可在服务器地址后面以冒号分隔，例如https://www.example.com:443。HTTPS协议的默认端口号（443）可以省略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/YtEatenaRwyfiTeA510xfQ/zh-cn_image_0000002786520192.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=262F941042867660A8CDED82A6E4DE0069E7C4C654B5FB4597A84BD790B59AC8)

   后续AGC会周期性地向该处配置的开发者服务器（即下载地址）发起一个HTTP GET请求，其中包含的query参数请参考[开发者服务器接口规范](cloudfoundation-prefetch-cloud-interdev.md#开发者服务器接口规范)，获取到数据后会将整个HTTP body缓存在本地。

   **说明** 

   * 开发者服务器接口返回的数据内容需仅包含文本、图片、视频、音频等供页面展示的静态资源，不支持包含代码、脚本等动态数据。
   * 开发者服务器接口返回的数据类型为其自定义格式的JSON或字符串数据，大小需限定在3MB以内。
7. 若配置“安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改下载地址，只需点击“下载地址”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/9J2tgj0kTvGoqHhvkw8eJg/zh-cn_image_0000002786360264.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=8DDA9492D1AA0D06BE845592EFB7BF9386AE2C28FD7C2B7DB21165F7E77455AE)
