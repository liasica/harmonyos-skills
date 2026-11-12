---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ux-basic-quality-test-1
title: 如何定位UX测试结果不通过问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > UX基础质量测试 > 如何定位UX测试结果不通过问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:72350e7b4a831e8249f992b8825d3c3412ecd1381d3160b356003c390af12961
---

## 问题现象

* 问题一：使用DevEco Testing执行UX测试结果显示“条件依赖”，报“arklayout文件存储失败”或“arklayout文件依赖调试版本应用”：

  测试结果：条件依赖。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/aScTPilARxqBXstEhPxzeQ/zh-cn_image_0000002628563632.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=26234A87EAF7C0474E459BBCCB63DB6076394C09953D8BE77347ED370E4D195C "点击放大")

  原因说明：arklayout文件存储失败。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/z8qzDIlYSyGXeQjYW19Atg/zh-cn_image_0000002658922937.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D82AEF3765EC6149C64174E4CAF1A1D0D7EC74A7FF91D8751CA74B7D141F5A50 "点击放大")

  原因说明：arklayout文件依赖调试版本应用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/IGf72pQlRsqMmjqvdl--5A/zh-cn_image_0000002658802983.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8F0487820B13E176EBE920262F94FCE06949C46229BB5E4A98DFADA768C10C2 "点击放大")
* 问题二：UX检测结果显示“条件依赖”，报“应用包不存在”是什么原因？

  原因显示说明：应用包不存在。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/jlV32cK9QzmNZsl54x23IQ/zh-cn_image_0000002628403724.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=782E29F21782581CD374CC48140901178CB4FDD4194146461CF5B55471256BDB "点击放大")
* 问题三：UX检测结果显示“元服务胶囊热区冲突”不通过，导航栏过宽该如何解决？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/XZwne1wBS1WUpn1fdofeUw/zh-cn_image_0000002628563634.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6A52D9DF174CCD7FE1E377568668F7CF914F3BDEE5BB73D22E8CC28757FC5AA "点击放大")
* 问题四：UX检测结果显示“不涉及”该如何处理？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/d55MYh-QRvWFPxia9MQqtw/zh-cn_image_0000002658922939.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=279707142940BD74789487EA8380D73913028AD05E757A51B711689A85857E5F "点击放大")
* 问题五：UX检测结果显示“不通过”，如何定位和修复？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Y5OX0mbKS2OMf5ffr8OIwg/zh-cn_image_0000002658802985.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECC409D24D580164B19528259E020F9997C17659F4D83F1C8EED5996A2FCE8C4 "点击放大")

## 解决方案

* 问题一解决方案：

  UX检测时部分规则依赖debug版本应用进行测试，请安装应用的debug签名版本重启手机后重新测试。
* 问题二解决方案：

  UX检测时部分规则依赖应用包完成，如果手机上已安装了应用，UX测试的部分结果会提示应用包不存在，请通过DevEco Testing进行应用的安装和测试。
* 问题三解决方案：

  应用UX体验建议中关于热区的标准可参考[适用范围](../harmonyos-guides/experience-suggestions-ux.md#section1541617350183)中“点击热区”，使用[AtomicServiceNavigation](../harmonyos-references/ohos-atomicservice-atomicservicenavigation.md#atomicservicenavigation-1)设置导航栏的宽度。
* 问题四解决方案：

  检测结果为不涉及代表测试用例的执行条件不满足，不会执行相关的测试场景，可以点击不涉及前面的“查看”进行详细查看。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ic2RtoD1R4KGrnZ3efkgFg/zh-cn_image_0000002628403726.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=66AAABD93D77F80A854DB50056360DA715D1915F4856518B640941C799C3B654)
* 问题五解决方案：

  举例“典型手势时长设计”测试不通过，点击对应的“不通过数”->查看定位日志和修复指南。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/mBUEOM8aScOtjTkgGhUxfQ/zh-cn_image_0000002628563636.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E7E143F095EFF162C58244A81BDD79969C06444158FA868F3472FCCE2EAA9ED "点击放大")

  定位日志查看：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/nc0cCGqMS2S7Tx480cYInA/zh-cn_image_0000002658922941.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=50D3C9CBD6331B5E6AC49984ABFB34C38B413F31A1762F37EBB1C07F83951D63 "点击放大")

  修复指南查看：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/BHN-gsihTYCyJU4WY2AerA/zh-cn_image_0000002658802987.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA1327AB6FA1661CAE8D8A6F872871AEAFA7336E60C0C3B1027A856AB728AAE8 "点击放大")
