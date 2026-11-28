---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator
title: 应用UI生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 应用UI生成
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0099f9196b428a23edc73fa6425ef1814b772c97751eba990c1c346b17fcfa62
---

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

## 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

## 启用插件

1. 在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/D8CqbRbGTwOMdzELIwnRcw/zh-cn_image_0000002808767119.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E407DE9A3E580618B0261DC081764F205AE577B914245585CC7992D5CACCEA9)
2. 单击OK并关闭设置窗口，插件启用成功。

## 开始使用

1. 在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2. 输入待配置项路径，点击**Next**进入下一步。

   | 待配置项 | 说明 |
   | --- | --- |
   | Installation package path | 待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。 |
   | SDK path | 等于或高于编译应用包所使用版本的SDK路径。 |
   | Git Bash path | Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/1O4BpWX4SXeIFQJ6D900bg/zh-cn_image_0000002779407564.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE93385A0A4B87680FE0BE01DA521A6644425794F051134B0D815494795E2CA2)
3. 选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/bEimknVjRxWnjz2rsU9VNw/zh-cn_image_0000002808767117.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=49CE6210652C4599DA00426F95ACE245B68BE8B114BF7E06CD1AEDF1049E1BDA)
4. 配置输出工程待配置项，点击**Finish**进行生成。

   | 待配置项 | 说明 |
   | --- | --- |
   | Destination Path | 生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改） |
   | Compatible SDK | 生成的新工程所使用的SDK版本 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ld8R1MTuSoikGmLisyQUOA/zh-cn_image_0000002779407566.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFD012234E6DCCC503B934AE6D73DD4A155D870F4722879E24387BAC22FCCCBA)
5. （可选）如果所选XML无有效根节点，需要选择根节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/xo07g9cfQIWewrLTzhRVHQ/zh-cn_image_0000002808887203.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=2726D7DFF2309E349EF97252AC9761D5487A099D0BED8F41B79263C6CB98D47A)
6. 点击**Finish**，在弹窗中点击确认，打开新工程。

   生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WgCoK9v-SrOl2OnoxhWRjA/zh-cn_image_0000002808887205.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FFE034262529894704A74DE76064D48ADAC857175CC97B2471CBDF1843C9ACD)
7. 生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/PxnCQn5KRMy2hczpvaR5Uw/zh-cn_image_0000002779567540.png?HW-CC-KV=V1&HW-CC-Date=20261128T023447Z&HW-CC-Expire=31536000000&HW-CC-Sign=22EABE817B26C10A14AE334AB823E048429F49E1390E21862D3BBE1E544D4397 "点击放大")

   更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
