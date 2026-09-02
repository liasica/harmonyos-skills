---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparations
title: 开发准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:21fbe2c17ca9f0cbbac7ec6d648117b10f4e7b4309baff1eb32989cdc8dd7e7f
---

## 环境准备

* 使用Ubuntu 64位运行[Tools下载](cannkit-preparations.md#tools下载)中的tools\_omg模型转换工具。
* 推荐使用[Ubuntu 22.04](https://mirrors.ustc.edu.cn/ubuntu-releases/22.04/)及以上版本、MacOS 10.14及以上版本、Windows 10及以上版本安装应用开发环境[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)。
* 准备训练好的tools\_omg模型转换工具生成的[离线模型](cannkit-overall-parameter.md)或者从[Model Zoo](cannkit-model-zoo.md)中选择合适的模型。

## Tools下载

| Tools名称 | Tools说明 | Tools下载 | SHA256校验码 |
| --- | --- | --- | --- |
| DDK工具包 | DDK工具包包含tools\_dopt、tools\_omg、tools\_ascendc和platform。  轻量化工具（tools\_dopt）：对原始模型进行轻量化，以减少模型体积及加快模型推理速度。  OMG工具（tools\_omg）：模型转换工具。  AscendC工具（tools\_ascendc）：为AscendC算子开发提供的算子功能、性能调测集成工具。  platform：将对应平台插件包安装到platform目录下。 | [DDK-tools-next-6.1.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/fa/v3/KmYm4fyVQhy8lN4CUfJAqw/DDK-tools-next-6.1.1.0.zip) | 87d7e3f186ad5c527a9385cea555559ea53c63b87dc483820523bcf7bf6f87e5 |
| 平台插件包  包名：  kirin9020 | AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。 | [kirin9020-plugin-next-6.1.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/3a/v3/7jJnQ1i5SDyX8uxR5fErEw/kirin9020-plugin-next-6.1.1.0.zip) | da4ebea4ce88889d94f96baf7bde43ff178153d68425e24d4e0db5b25089aa3f |
| 平台插件包  包名：  kirinx90 | AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。 | [kirinx90-plugin-next-6.1.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/b5/v3/NnZ7SJm2Sb6nIz2vO7EVzA/kirinx90-plugin-next-6.1.1.0.zip) | 0657efdddd2267949e83af2a382603b523d30b258d72e077a6975eb87d4f10b1 |
| 平台插件包  包名：  kirin9030 | AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。 | [kirin9030-plugin-next-6.1.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/b2/v3/r8_aLTyLSWqMdgwLd1XD3Q/kirin9030-plugin-next-6.1.1.0.zip) | 5df8110e9b494ba87216b0c195c83d7f6c1407af89613de850ed7c569e57e593 |

开源软件声明：[CANN Kit 6.1.1.0 Open Source Software Notice](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/a0/v3/F4R0Oj9eSPar3vzm34KFzg/Opensource-software-notice-6.1.1.0.zip)。
