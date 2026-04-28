---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-config
title: 配置预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 配置预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:46+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d131aea682b64e3f89c77f40e281e3342e6830f72b66923b1ecebd1bb488f281
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/HbtPgHrHSEaXXR1UtMuIww/zh-cn_image_0000002583478867.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=B17D221A700689955649A94BC040EEDCE4A6780557FB58A935B6018C66D5B3C4)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“云函数”，然后点击“函数名称”后的“修改”。

   说明

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/jGTdHAgwQ6i1QyXlMWUyuw/zh-cn_image_0000002552799218.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=2734691C25CDD27E5D978F19FC0A2F081F22B568BF5730B54A50318B87EE5C62)
5. 以“周期性预加载”为例，在“函数名称”下拉框选择实现周期性预加载的函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/vN8AYh1XTvKa7wzZClIdBw/zh-cn_image_0000002583438913.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=60FE8133874225BEC67424DCDD2DCA3C9D654E954D93823D3193FC16FD98F94B)
6. 点击“保存”完成周期性预加载配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/jMPJPStzTgWECGcnb1R_lQ/zh-cn_image_0000002552958868.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=1FF7E1AFC966BA9F312FF10A53CE990C42059E09750E5D90C3D9007E2B162A3D)
7. 若配置“安装预加载”或“跳链安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改绑定的云函数，只需点击“函数名称”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/UTxWcHpsSROd9IZR7E3ieQ/zh-cn_image_0000002583478869.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=90C0944E40964867E88B44E30CB19F9D33D6803C818B638B8CBDF3613282ACBD)

## 数据来源为开发者服务器

### 前提条件

已[开通预加载服务](cloudfoundation-enable-prefetch.md)。

### 配置服务器地址

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/EeXjV11hQ9GXWBfBoA0zAg/zh-cn_image_0000002552799220.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=3B8D87BB589F5E7CA8291DD9C3757BB999CAD85B6D7C92E4956F767B40160929)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“开发者服务器”。

   说明

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/dQHjZmVwTGefJ9FmGxkuvg/zh-cn_image_0000002583438915.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=CAC886DAEF3D9C727AE0243FC298706C4B58CDE85585A8F71C9A4BA7D3D9185D)
5. 点击“下载地址”后的“修改”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Q-FscgqoTkikHunZtUp2KA/zh-cn_image_0000002552958870.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=EE4C33B3FEA2943D643EA9BAE956229CA6DC3D174A1B1DBA2D8DCBD70FE1F85F)
6. 以“周期性预加载”为例，“下载地址”以“https://”开头，输入框中输入服务器地址，配置完成后点击“保存”。

   需要注意以下几点：

   * 仅支持填写一个服务器地址，需包含预加载资源接口路径，如图中示例：prefetchData。
   * 域名：须填写完整的域名。例如www.example.com，不可写为example.com。
   * IP地址：须填写准确的IP地址，确保没有输入错误。
   * 端口号：如果要指定端口号，可在服务器地址后面以冒号分隔，例如https://www.example.com:443。HTTPS协议的默认端口号（443）可以省略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/w8IHcKurRN-K3_jKnVkU5w/zh-cn_image_0000002583478871.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=325939BBB1E961EC2C045643BFF2AAC50B6494331A715EA30C445D6A6C88454F)

   后续AGC会周期性地向该处配置的开发者服务器（即下载地址）发起一个HTTP GET请求，其中包含的query参数请参考[开发者服务器接口规范](cloudfoundation-prefetch-cloud-interdev.md#开发者服务器接口规范)，获取到数据后会将整个HTTP body缓存在本地。

   说明

   * 开发者服务器接口返回的数据内容需仅包含文本、图片、视频、音频等供页面展示的静态资源，不支持包含代码、脚本等动态数据。
   * 开发者服务器接口返回的数据类型为其自定义格式的JSON或字符串数据，大小需限定在3MB以内。
7. 若配置“安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改下载地址，只需点击“下载地址”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/0LgUzJ4jQW21fm9xP33oAA/zh-cn_image_0000002552799222.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=C23F63BAFC99C571C205994AF40D00F830097775BD69C870BDABF6B32ED14068)
