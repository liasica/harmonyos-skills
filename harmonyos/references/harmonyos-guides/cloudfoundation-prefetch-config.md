---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-config
title: 配置预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 配置预加载
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:56+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:28f0ff250a23641a8f0227b9a9e4c8c7277fb2fc001acfe9f6ba9870e75efbf3
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7rO7cUXuR260n8UnlDt2Fw/zh-cn_image_0000002820406273.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF67F1BB149047F63BC5325B5A92A2F83300EFEB3D2F568942456148DB7EEB1E)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“云函数”，然后点击“函数名称”后的“修改”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/krKmJAeUTp-ws8tbm8IdoQ/zh-cn_image_0000002791726294.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=47438BE737D22A0FDEB6CA39FF24443732D5ABFC9D6C4C0247A32FEC8D8D593B)
5. 以“周期性预加载”为例，在“函数名称”下拉框选择实现周期性预加载的函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/h3XU7JCgQlC7SpCmjTyS2g/zh-cn_image_0000002791566322.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AAE93802EEE1B0BE82BC44E6EDC764DFEED99CC002280E1A5F25EB9ECCCD343)
6. 点击“保存”完成周期性预加载配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/HVEUIO7ARB6MHqKNBoKwDg/zh-cn_image_0000002820526275.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB82873D5B7D09640D0C4FEEC50DDBC9FD0881D5E386481FAE4B9F9657F25C25)
7. 若配置“安装预加载”或“跳链安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改绑定的云函数，只需点击“函数名称”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/SmZ2U90JRBGVr4jV1Pud4g/zh-cn_image_0000002820406275.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=6481CAB95620D1A8BC94F59B5454DBBA4614C0B829273ED5A49F54443E762012)

## 数据来源为开发者服务器

### 前提条件

已[开通预加载服务](cloudfoundation-enable-prefetch.md)。

### 配置服务器地址

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/9wAfEfeIQ9muOEWA2lcHTw/zh-cn_image_0000002791726296.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=C96EEF7834D434C1E75E61582A98B66A035905BC0ACE81A75BAB88935DF2532D)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“开发者服务器”。

   **说明** 

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/F_OuPkVsTyqFflkWZLxvbg/zh-cn_image_0000002791566324.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE07674B88CB7C5892F5990FBC2E6DAA5726CCA448DB7DB577471CDE3F8B1B7B)
5. 点击“下载地址”后的“修改”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/6N8FHW6dR-egeOGSpDyFFQ/zh-cn_image_0000002820526277.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=B021996C1025909E450A7AD88E99EB57FC308C31F989663DD79D90CB6D23E4B8)
6. 以“周期性预加载”为例，“下载地址”以“https://”开头，输入框中输入服务器地址，配置完成后点击“保存”。

   需要注意以下几点：

   * 仅支持填写一个服务器地址，需包含预加载资源接口路径，如图中示例：prefetchData。
   * 域名：须填写完整的域名。例如www.example.com，不可写为example.com。
   * IP地址：须填写准确的IP地址，确保没有输入错误。
   * 端口号：如果要指定端口号，可在服务器地址后面以冒号分隔，例如https://www.example.com:443。HTTPS协议的默认端口号（443）可以省略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/pOvd8aujTyKVHw6vXJDGqg/zh-cn_image_0000002820406277.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=301B727A73DB9397FAEE4F9D1C03BA871BB83EB068274498A02A01E11C6EA153)

   后续AGC会周期性地向该处配置的开发者服务器（即下载地址）发起一个HTTP GET请求，其中包含的query参数请参考[开发者服务器接口规范](cloudfoundation-prefetch-cloud-interdev.md#开发者服务器接口规范)，获取到数据后会将整个HTTP body缓存在本地。

   **说明** 

   * 开发者服务器接口返回的数据内容需仅包含文本、图片、视频、音频等供页面展示的静态资源，不支持包含代码、脚本等动态数据。
   * 开发者服务器接口返回的数据类型为其自定义格式的JSON或字符串数据，大小需限定在3MB以内。
7. 若配置“安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改下载地址，只需点击“下载地址”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/fOxQ7s4SS7SbUxE8LwuC9w/zh-cn_image_0000002791726298.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=27254DDD448FB7B7E92C44CADB7145A19A9D40246B5FF70AFC82666B244BEC41)
