---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-76
title: 通过打包工具构建的软件包上传AGC报错996如何解决
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 通过打包工具构建的软件包上传AGC报错996如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:670ee40c0be6b7ebed8d154eff0b1126b50fc86caa93ea59e4959686ed08f45e
---

## 问题现象

开发者使用的是打包工具通过命名的方式生成App包，然后对App包进行签名。生成签名后的App包上传到AGC进行上架，但是上传软件包后一直报[错误码996。](../app/agc-help-package-errorcode-0000002312513009.md#section451313022017)多次重传后仍无法解决。

## 背景知识

* 上架应用市场的软件包不能是.hap格式的，必须是.app格式，并且是经过签名的。
* 通过[App打包指令](../harmonyos-guides/packing-tool.md#app打包指令)可使用打包工具的jar包对应用进行打包，通过传入打包选项、HAP包文件路径等，生成所需的App包，App包用于上架应用市场。示例如下：

  ```txt
  java -jar app_packing_tool.jar --mode app --hap-path D:\entry-default.hap --out-path D:\entry-default.app
  ```
* 通过App打包指令生成的软件包是未经过签名的，还需要通过DevEco Studio自带的签名工具，可以[对APP包进行签名](faqs-signature-service-17.md)，签名后的包才能用于上架应用市场。

## 问题定位

1. 首先获取上传的软件包，检查软件包格式是否是.app，如果是.hap说明文件错误，需要重新生成.app包。
2. 确认是.app格式包后，使用解压工具解压.app包，查看是否含有pack.info文件，如果没有，确认下是否强行通过.hap压缩成.zip后修改后缀名为.app。这种方式会破坏软件包的完整性，是无法上架的。
3. 检查pack.info里面的packages里面的name和.hap包的文件名是否一致。如果.hap包的名字与pack.info中name值不同，需要更改HAP包的名字与name相同。否则软件包也无法上传至AGC。
4. 解压软件包发现HAP包名称为：entry-default-unsigned.hap，而pack.info里面name和.hap包的文件名为：entry-default，对比两个文件名发现多了一个unsigned，说明问题出在打包指令执行错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/gUx4XrnzRtmW9N3ovgdRLg/zh-cn_image_0000002628394634.png "点击放大")

## 分析结论

1. 一般生成的构建产物如果未签名时文件名为xxx-unsigned.hap，用于显性区分文件是否签名，如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/vufYz_1qS46RGaEDo8JN9A/zh-cn_image_0000002628554526.png "点击放大")
2. 问题原因是：通过App打包指令生成App包时未修改输入参数.hap包名称。

## 修改建议

1. 使用App打包指令时，修改.hap的名字，去掉-unsigned，如改成entry-default.hap，然后再执行命令，生成未签名的.app包。成功生成后可以解压.app包验证.hap名称是否为entry-default.hap。
2. 再通过DevEco Studio自带的签名工具，对App包进行签名，生成已签名的.app包。成功生成后可以再次解压.app包验证.hap名称是否为entry-default.hap。确认无误再将.app包上传AGC。正确的软件包样式：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/S3OLQumKRSGi-1fUFl4xBA/zh-cn_image_0000002658913845.png "点击放大")

## 常见FAQ

Q：如果原始构建产物有多个HAP，或者还有HSP怎么打包成.app包呢？

A：可以通过[多工程打包指令](../harmonyos-guides/packing-tool.md#多工程打包指令)通过传入已经打好的HAP、HSP和App包，将多个包打成一个最终的App包，并上架应用市场。
