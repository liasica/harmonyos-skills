---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparations
title: 开发准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a601f6a03045bcae3174f7581f104a4e8da84ae9f3c483cb8a3627b04b91b868
---

## 环境准备

* 使用Ubuntu 64位运行[Tools下载](cannkit-preparations.md#tools下载)中的tools\_omg模型转换工具。
* 推荐使用[Ubuntu 22.04](https://mirrors.ustc.edu.cn/ubuntu-releases/22.04/)及以上版本、MacOS 10.14及以上版本、Windows 10及以上版本安装应用开发环境[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)。
* 准备训练好的tools\_omg模型转换工具生成的[离线模型](cannkit-overall-parameter.md)或者从[Model Zoo](cannkit-model-zoo.md)中选择合适的模型。

## Tools下载

| Tools名称 | Tools说明 | Tools下载 | SHA256校验码 |
| --- | --- | --- | --- |
| 轻量化工具  包名：tools\_dopt | 对原始模型进行轻量化，以减少模型体积及加快模型推理速度。 | [DDK-tools-6.0.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/4d/v3/ChvyTaVxR6CvAV1lVLB1-w/DDK-tools-next-6.0.1.0.zip?HW-CC-KV=V1&HW-CC-Date=20260123T095006Z&HW-CC-Expire=315360000&HW-CC-Sign=2CB6189092FA3B3FF22F538945D7DDB975C6DBCA41F753474B7B7A28E686AA6A) | 1b2822fb9e5fe7443782915c6f34b4a2ce5c028207e7782514bd93970ff8e48a |
| OMG工具  包名：tools\_omg | 模型转换工具。 | [DDK-tools-6.0.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/4d/v3/ChvyTaVxR6CvAV1lVLB1-w/DDK-tools-next-6.0.1.0.zip?HW-CC-KV=V1&HW-CC-Date=20260123T095006Z&HW-CC-Expire=315360000&HW-CC-Sign=2CB6189092FA3B3FF22F538945D7DDB975C6DBCA41F753474B7B7A28E686AA6A) | 1b2822fb9e5fe7443782915c6f34b4a2ce5c028207e7782514bd93970ff8e48a |
| AscendC工具  包名：tools\_ascendc | 为AscendC算子开发提供的算子功能、性能调测集成工具。 | [DDK-tools-6.0.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/4d/v3/ChvyTaVxR6CvAV1lVLB1-w/DDK-tools-next-6.0.1.0.zip?HW-CC-KV=V1&HW-CC-Date=20260123T095006Z&HW-CC-Expire=315360000&HW-CC-Sign=2CB6189092FA3B3FF22F538945D7DDB975C6DBCA41F753474B7B7A28E686AA6A) | 1b2822fb9e5fe7443782915c6f34b4a2ce5c028207e7782514bd93970ff8e48a |
| 平台插件包  包名：  kirin9020 | AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。 | [kirin9020-plugin-6.0.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/63/v3/RYFrodZqRG-vZ7LO5-gSuw/kirin9020-plugin-next-6.0.1.0.zip?HW-CC-KV=V1&HW-CC-Date=20251222T032701Z&HW-CC-Expire=315360000&HW-CC-Sign=D8C338777E255E82E3FE77C01F498AD8AB5390D06C6BA1580450490DB1F5D429) | b0657b18d30d59fff6d6a64eb7af93e63668a921936e66a48e692ab943eb2687 |
| 平台插件包  包名：  kirinx90 | AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。 | [kirinx90-plugin-6.0.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/bd/v3/nHZXjj-MTF6FJv_-fw8q8w/kirinx90-plugin-next-6.0.1.0.zip?HW-CC-KV=V1&HW-CC-Date=20251222T032501Z&HW-CC-Expire=315360000&HW-CC-Sign=BA1EFF3526C3E49E2C52CBBFA9EE1431E802D35B7D4AA8E58620CA1715303B66) | a3bd6872367ca370d20d392840ae5dd19c517206c48a459b531b96e0f18000a7 |
| 平台插件包  包名：  kirin9030 | AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。 | [kirin9030-plugin-6.0.1.0](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/f0/v3/m4i1iJERRn6Ni6U-zH88Kw/kirin9030-plugin-next-6.0.1.0.zip?HW-CC-KV=V1&HW-CC-Date=20251222T032403Z&HW-CC-Expire=315360000&HW-CC-Sign=FC69A5B1E9B920477B07393B604A54A8C22F3A6F7F3E27EF2EF0B2026310A867) | 3b32effc5af9804628cb9287e88cc28ed381877adb15dd85bf8d66e3be805251 |

开源软件声明：[CANN Kit 6.0.1.0 Open Source Software Notice.doc](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260114154903.91891335463699164966704263846158:50001231000000:2800:F67C8F023C664AF504C606207B4DE0330B2711275C673CD791164985E68795F6.doc?needInitFileName=true)。
