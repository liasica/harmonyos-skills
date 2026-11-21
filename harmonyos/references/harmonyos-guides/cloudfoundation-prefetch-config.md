---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-config
title: 配置预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 配置预加载
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:75153e432dd9ef1b6dab07dabc549d96cdc095c3e28b38c8908643e2f7865303
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/cWPhxuWQQTuypzEsw-lcnA/zh-cn_image_0000002792877974.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=15744F43291DE96C497FAB3B2013A00897903CBDB14E5D31888AED3B8C215948)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“云函数”，然后点击“函数名称”后的“修改”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/keEXykU0S5--IZZunC8_Iw/zh-cn_image_0000002821837881.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=B45422AB9BC9F22AE04EFAEE8536DD9A38A065E5CA89942AC14BE8F9364111AA)
5. 以“周期性预加载”为例，在“函数名称”下拉框选择实现周期性预加载的函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/c2BILA4mTdqX2c2XSqvQcA/zh-cn_image_0000002821757883.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBB7617070E8EB3C2680BA53C7E1ADA74D829A59D6EB20B7437965AA3CBD0FD6)
6. 点击“保存”完成周期性预加载配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/cmccyIRISxim3ownHHFF7g/zh-cn_image_0000002793037946.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=E92E1FC65C8B3965C5B6FA1D0A5ED8E852DB0454B1947BC2054BDF762765B026)
7. 若配置“安装预加载”或“跳链安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改绑定的云函数，只需点击“函数名称”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/nlqDDVurTOClg4tC3zl1sQ/zh-cn_image_0000002792877976.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=360E9380C59B5A697B53770F77959F30D94EF1FDF6291259C22BC79FCB1F8D9C)

## 数据来源为开发者服务器

### 前提条件

已[开通预加载服务](cloudfoundation-enable-prefetch.md)。

### 配置服务器地址

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/nizsqAUJS-Wrz_6I2lBGuQ/zh-cn_image_0000002821837883.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=D418FCAC8E3C186621E241E3D4865CC9C2816D15E9EC0327FD7EEB54659AA508)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“开发者服务器”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/KFb1LDmLTDK9bNtGTdSzRQ/zh-cn_image_0000002821757885.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6F4162BE31FD200C6263ACD28916341539D3079E677373462496B6BC71C2E53)
5. 点击“下载地址”后的“修改”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/psSVTYzuTv-uq2Wu31uqWQ/zh-cn_image_0000002793037948.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=7488A82FAF5004855E661A2640CA3E0F8C8FADF879F8BB640EDE214A3C564E33)
6. 以“周期性预加载”为例，“下载地址”以“https://”开头，输入框中输入服务器地址，配置完成后点击“保存”。

   需要注意以下几点：

   * 仅支持填写一个服务器地址，需包含预加载资源接口路径，如图中示例：prefetchData。
   * 域名：须填写完整的域名。例如www.example.com，不可写为example.com。
   * IP地址：须填写准确的IP地址，确保没有输入错误。
   * 端口号：如果要指定端口号，可在服务器地址后面以冒号分隔，例如https://www.example.com:443。HTTPS协议的默认端口号（443）可以省略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/3PTkEiHmSFySgJJKEd5Tpw/zh-cn_image_0000002792877978.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=E66EE9164C0B7ADC9508809A4436EFDF53EF3D70C52FC3356DE0E1BE66CCB385)

   后续AGC会周期性地向该处配置的开发者服务器（即下载地址）发起一个HTTP GET请求，其中包含的query参数请参考[开发者服务器接口规范](cloudfoundation-prefetch-cloud-interdev.md#开发者服务器接口规范)，获取到数据后会将整个HTTP body缓存在本地。

   **说明** 

   * 开发者服务器接口返回的数据内容需仅包含文本、图片、视频、音频等供页面展示的静态资源，不支持包含代码、脚本等动态数据。
   * 开发者服务器接口返回的数据类型为其自定义格式的JSON或字符串数据，大小需限定在3MB以内。
7. 若配置“安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改下载地址，只需点击“下载地址”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/bB4qnu6NR8CIiHI3ckLFsg/zh-cn_image_0000002821837885.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E98C1D3FE47EC2B5BCDE3C3AAD7423E165B04B3B592B19F70EFB1BA33793B2A)
