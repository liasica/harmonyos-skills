---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-troubleshooting-0002
title: HarmonyOS 开发者中心软件包上传报错996问题排查与解决
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 故障排查 > HarmonyOS 开发者中心软件包上传报错996问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:44+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:e50f2233c8fd2daba3de2af361a5ea23bee5b060479df64d6196583266430579
---

## 问题现象

开发者使用的是打包工具通过命名的方式生成App包，然后对App包进行签名。生成签名后的App包上传到HarmonyOS 开发者中心进行上架，但是上传软件包后一直报[错误码996。](../app/agc-help-package-errorcode-0000002312513009.md#section451313022017)多次重传后仍无法解决。

## 定位过程

1. 首先获取上传的软件包，检查软件包格式是否是.app，如果是.hap说明文件错误，需要重新生成.app包。
2. 确认是.app格式包后，使用解压工具解压.app包，查看是否含有pack.info文件，如果没有，确认下是否强行通过.hap压缩成.zip后修改后缀名为.app。这种方式会破坏软件包的完整性，是无法上架的。
3. 检查pack.info里面的packages里面的name和.hap包的文件名是否一致。如果.hap包的名字与pack.info中name值不同，需要更改HAP包的名字与name相同。否则软件包也无法上传至HarmonyOS 开发者中心。
4. 解压软件包发现HAP包名称为：entry-default-unsigned.hap，而pack.info里面name和.hap包的文件名为：entry-default，对比两个文件名发现多了一个unsigned，说明问题出在打包指令执行错误。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/jHt1wm_LS5C7aVV5jF5caA/zh-cn_image_0000002760273848.png "点击放大")

## 分析结论

1. 一般生成的构建产物如果未签名时文件名为xxx-unsigned.hap，用于显性区分文件是否签名，如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/AGAOs5OPRaa2Nvf_q-c7lQ/zh-cn_image_0000002760273852.png)
2. 问题原因是：通过App打包指令生成App包时未修改输入参数.hap包名称。

## 修改建议

1. 使用App打包指令时，修改.hap的名字，去掉-unsigned，如改成entry-default.hap，然后再执行命令，生成未签名的.app包。成功生成后可以解压.app包验证.hap名称是否为entry-default.hap。
2. 再通过DevEco Studio自带的签名工具，对App包进行签名，生成已签名的.app包。成功生成后可以再次解压.app包验证.hap名称是否为entry-default.hap。确认无误再将.app包上传HarmonyOS 开发者中心。正确的软件包样式：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/pETXls62TUKppR9PfRq8kg/zh-cn_image_0000002760113942.png "点击放大")
3. 若使用流水线或CI构建，需确保流水线脚本中在打包后追加了签名步骤，使用正确的发布证书和发布Profile对App包进行签名，再上传HarmonyOS 开发者中心。
