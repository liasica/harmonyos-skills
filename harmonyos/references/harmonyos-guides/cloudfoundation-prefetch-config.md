---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-config
title: 配置预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 配置预加载
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c7bb891430f34dd1fc6489571dcdc51a02f30d473141e09913573f103fc77fb5
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/O2FjR5-pQ6ilZLwk_Sbrfg/zh-cn_image_0000002558605710.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=9876DF9CD0F8E854D27735039A3D6443E175090127F0E7D48028E93AC84D6681)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“云函数”，然后点击“函数名称”后的“修改”。

   说明

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/3HqECC-URfCn_Hrar3mwGA/zh-cn_image_0000002589325237.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=AEFEEB482A8A056D1E5E365D0BE66A0CAA376F75000BBF0A66AFF7630D930F84)
5. 以“周期性预加载”为例，在“函数名称”下拉框选择实现周期性预加载的函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/wmkerUilTfqKoFXDotQEMA/zh-cn_image_0000002589245173.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=9808DCDAF21C9F10D78A6413E409455AA5C223FA82E952BC8F5C16BB2D67B448)
6. 点击“保存”完成周期性预加载配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/HEroyUTBRi6wPmgXfrILSg/zh-cn_image_0000002558765368.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=C60DD61B1036A2A1E6BFD27DBC29B92015F973233572157F4D1DC492E0C96BA8)
7. 若配置“安装预加载”或“跳链安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改绑定的云函数，只需点击“函数名称”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/T7ij_32JThChBgo22FL1rw/zh-cn_image_0000002558605712.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=3EE7B6837000239DF9E454142A22DCDB25DD3B7C8782449198095F6543A3DD18)

## 数据来源为开发者服务器

### 前提条件

已[开通预加载服务](cloudfoundation-enable-prefetch.md)。

### 配置服务器地址

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击您的项目，在项目下的应用列表中选择需要配置预加载的HarmonyOS应用/元服务。
3. 在左侧导航栏选择“云开发（Serverless）> 预加载”，进入预加载页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/tNewy6BDTXihq5VgtFBhaA/zh-cn_image_0000002589325239.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=00A5FF8739B08F8A922E459C00370B21F0C4F7EB3D3E47D1F3C9BAED20CA5344)
4. 根据实际需要，在“周期性预加载”、“安装预加载”或者“跳链安装预加载”区域，“数据来源”选择“开发者服务器”。

   说明

   * 跳链安装预加载仅支持在HarmonyOS应用中调用。
   * 由于跳链安装预加载功能需要使用App Linking Kit提供的延迟链接能力，因此在配置跳链安装预加载之前，请务必先完成延迟链接的开发。具体请参见[通过延迟链接跳转至应用详情页](applinking-deferredlink.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/LVsf65cxQ5qj4vLUZGcQmA/zh-cn_image_0000002589245175.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=2848BB41BA71CA793C2B7E05EA8A86A35B7EC22398A3AADA042EF0D3234645D0)
5. 点击“下载地址”后的“修改”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/5W7vZJM2TBaijoPAhJ_RrA/zh-cn_image_0000002558765370.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=903D46437B1A6F12BF1E695D0106AA5DB11CE1170E7F02F31C1D38D8AD814FA8)
6. 以“周期性预加载”为例，“下载地址”以“https://”开头，输入框中输入服务器地址，配置完成后点击“保存”。

   需要注意以下几点：

   * 仅支持填写一个服务器地址，需包含预加载资源接口路径，如图中示例：prefetchData。
   * 域名：须填写完整的域名。例如www.example.com，不可写为example.com。
   * IP地址：须填写准确的IP地址，确保没有输入错误。
   * 端口号：如果要指定端口号，可在服务器地址后面以冒号分隔，例如https://www.example.com:443。HTTPS协议的默认端口号（443）可以省略。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/LjEXrRtXSPWP1JGypFuSrQ/zh-cn_image_0000002558605714.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=4FA7939D87309558A2C41CB390447819E1A0FD4D223A3FF24A9654CC551E4FAA)

   后续AGC会周期性地向该处配置的开发者服务器（即下载地址）发起一个HTTP GET请求，其中包含的query参数请参考[开发者服务器接口规范](cloudfoundation-prefetch-cloud-interdev.md#开发者服务器接口规范)，获取到数据后会将整个HTTP body缓存在本地。

   说明

   * 开发者服务器接口返回的数据内容需仅包含文本、图片、视频、音频等供页面展示的静态资源，不支持包含代码、脚本等动态数据。
   * 开发者服务器接口返回的数据类型为其自定义格式的JSON或字符串数据，大小需限定在3MB以内。
7. 若配置“安装预加载”，重复步骤4-6即可。
8. （可选）若后续需要修改下载地址，只需点击“下载地址”后的“修改”进行更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SUapleU6SeiCq2qLUQ_wjA/zh-cn_image_0000002589325241.png?HW-CC-KV=V1&HW-CC-Date=20260429T053750Z&HW-CC-Expire=86400&HW-CC-Sign=E04202DC579E1A8205AB23D51FB56220257CDDDD8E3A764606F852ACA23EED96)
