---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-18
title: 如何解决Hypium测试用例转换为测试服务包时py_file字段获取为空的问题
breadcrumb: FAQ > DevEco Testing > 回归测试 > 如何解决Hypium测试用例转换为测试服务包时py_file字段获取为空的问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-30
content_hash: sha256:ab9d3e406d1349638b68c3b0f5c2399a95c106d8da18eed0e7de5c3a15edc54c
---

## 问题现象

[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)框架里测试套件生成测试服务包失败，提示“\*\*\*.json文件py\_file字段获取为空”，测试套件配置文件中该如何配置该字段？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/WoeAtaZ2THqoaCK_lr6CiQ/zh-cn_image_0000002661534691.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=C048342A2E46E5FC8EADB394555A62D86C057FA84BC527BCD6A3FCAEA7BDFBB5 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/UiVsv0s0TeOpHl0KVP7nlg/zh-cn_image_0000002631175564.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=12A606C0A2DAD6CFAF59BDCCC013ED003D8C848628DC9D9C7504A96CC426FB44 "点击放大")

## 背景知识

* [回归测试](../harmonyos-guides/other-test.md#section12324184817324)的测试对象为应用的核心功能，用户可将应用核心功能的测试用例构建成多个可执行测试包，每个测试包中仅包含单个测试用例，便于观察到核心功能的每个小功能点的质量。
* 测试执行前需先构建测试包，用户利用python的setuptools工具在工程根目录下构建setup-regression.py以及MANIFEST.in文件，setup-regression.py文件中声明用例，MANIFEST.in文件中声明脚本执行过程中需要用到的aw包、config文件夹下的配置文件及其他的资源文件。

## 问题定位

由于回归测试生成的可执行测试包中仅支持单用例（即单个json文件和json中指定的用例文件），根据报错信息需要检查setup-regression.py配置的单条用例xx.json文件py\_file字段是否存在或者是否为空。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/lOOJI702QrOdFqrAEvvvOw/zh-cn_image_0000002661414977.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DC6FC775776331BD3AC3D29B3DC34DF9A7C517F1E6115923EF140120B04E117 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/mnQTbGb_SMKVcsvBIH77fQ/zh-cn_image_0000002661414983.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=9350530631F89C6A1327C945CB5FAFD0B8EC1056B97C95370B5674954CE6BBB8 "点击放大")

## 分析结论

当用户在setup-regression.py文件中指定打包的json文件中未声明对应的用例py文件，会出现该提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/JYo7YCZ2SqKLulFjdqQZOg/zh-cn_image_0000002631175908.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DC3D06129409285575B4297FD9A59F26C59285D17EE8878CC66D4E3CED1D9CE "点击放大")

## 修改建议

回归测试生成的可执行测试包相关配置需要配置正确，若用例是测试套件路径配置示例如下：

* 用例xx.json文件需要包含py\_file字段；

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/f4SBz05jRXmlS6pBfMTPGw/zh-cn_image_0000002661415301.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=51971DE854BF072C585127EAEF755A498A2BE103F9A59F9C8D9DDDD2DA7B57B7 "点击放大")

* setup-regression.py文件示例；

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/rOOd9fgnRLqGU9JlRHOO9A/zh-cn_image_0000002631336454.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C301B9394E2F7A0F79AD70FA1E14BEDE984A77BB6EA1C1890E2536ACBB74B58 "点击放大")
* MANIFEST.in文件示例。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/N2JNAkHeRxmCx0qPP4G7Tg/zh-cn_image_0000002631336616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C29B2F5051147B4B24682758F096DCE23711ACFDE71D77A29D128BE2224E410 "点击放大")

## 常见FAQ

Q：生成可执行测试包时报错提示“测试套生成失败，请检查setup-regression.py文件后重试”如何解决？

A：请检测setup-regression.py文件写法，使用python setup-regression.py sdist--formats=zip进行本地自验证，验证通过后再利用插件出包。

Q：setup-regression.py文件无问题，但Hypium插件构建测试套件不成功，提示“测试套生成失败，请检查setup-regression.py文件后重试”如何解决？

A：请更新setuptools版本，可以先python -m pip install --upgrade pip更新pip，再使用命令pip install --upgrade setuptools升级setuptools。

Q：生成可执行测试包时报错提示“xxx.py文件不存在，请检查json文件是否填写正确！”如何解决？

A：当指定待打包的json文件中指定的py用例文件不存在，会出现该报错，请检查json文件中指定的py文件是否存在。
