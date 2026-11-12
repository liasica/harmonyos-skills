---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-testing-faq-11
title: 如何使用DevEco Testing进行应用安装/卸载
breadcrumb: FAQ > DevEco Testing > 如何使用DevEco Testing进行应用安装/卸载
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:1e9f1ee96ae4ee08e43950b17b39e73ab956ccc2b380103901b811f78c0a6eac
---

## 问题现象

DevEco Testing安装应用支持哪些种类的安装包？如何进行应用安装/卸载？

## 背景知识

DevEco Testing是一款专项集成测试工具，提供了多项测试能力。DevEco Testing将测试能力以测试服务卡片的形式呈现给用户，无需复杂的配置，即可一键执行测试任务，同时提供了测试报告和分析，辅助开发者发现应用和产品问题，提升应用质量。

## 解决方案

DevEco Testing目前支持安装hap、zip类型的[调试证书](../app/agc-help-debug-cert-0000002283256797.md)签名安装包。

1. 应用安装：
   * 连接设备，DevEco Testing选择实用工具-设备投屏。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/GqZ5OgBSRO6dWZlb6zQqqQ/zh-cn_image_0000002628404180.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAF3C93AC7A74FC734B9052BE520D09251CA371D9EFEAD9EF2713648FD986574 "点击放大")
   * 点击开始投屏，然后工具栏点击安装应用。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/bXCAy5N5Q46X3_ATElm-RA/zh-cn_image_0000002628564082.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=67A0CFBFC88AC57C92123E329871B203918F08955B7E7CBA57761D60112BCBB9 "点击放大")
   * 本地文件路径点击选择，弹框可选择应用包的类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/NWAb0QE1RouhbQ2XmPMQiA/zh-cn_image_0000002658923393.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=7033C4823FEBBFB40DCA51BA6DECDA063845C14AAFD0B67935F53E521CFEDBE0 "点击放大")
   * 选择安装包，点击确定，执行日志可以看到安装成功，如果安装失败，可以看到报错信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ADDn4uCBQW--mLCvQW6DPA/zh-cn_image_0000002658803445.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2D454B1A94ACC4297FEE0FEB656818455AC175EBE4F39C85E85EACBC7E395AE "点击放大")
2. 应用卸载：
   * 连接设备，DevEco Testing选择实用工具-设备投屏，工具栏点击卸载应用。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/hHOS9C-LSOCiYNdhSAyFvQ/zh-cn_image_0000002628404182.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=0857AC95C2078A2C9B97E48B21337FCD730444875924B9B9A2142E0FD9497EDA "点击放大")
   * 下拉框选择对应的应用，点击确定。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/nDPRINfVRECkI8gYAte-fA/zh-cn_image_0000002628564084.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B639CBA0144561AFAC5E41C2D1493F2E86422AD75D8530F0C2C178C9BCE0A3E "点击放大")
   * 弹出的对话框，点击确定卸载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/XzbqfuczSoCecteLDRyKxg/zh-cn_image_0000002658923397.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCFD27919BFC53B3F1122DADCEDBD16DE733E1AFDE08CFEA8031821BA1AB2F9E "点击放大")
   * toast提示应用卸载成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/h8O_wWILRvW-X-SqZiH5dA/zh-cn_image_0000002658803447.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=A55B532A220E7E6E9B7828A70D22C51A7207267CF9C57ACA8F0215C1B3C91D53 "点击放大")

## 常见FAQ

Q：DevEco Testing是否支持安装.app类型的安装包？

A：DevEco Testing暂不支持安装.app类型的安装包。

Q：DevEco Testing如何安装多包？

A：将hap、hsp包打包成zip格式文件，安装应用时文件类型选择\*.zip，即可安装。
