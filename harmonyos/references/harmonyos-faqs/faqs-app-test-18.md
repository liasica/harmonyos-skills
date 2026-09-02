---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-18
title: 如何统计单元测试的覆盖率
breadcrumb: FAQ > DevEco Studio > 应用测试 > 如何统计单元测试的覆盖率
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e247ce806123658f83e6700bcf173d040f3f225f7d35336069f43b8535877b3
---

## 问题现象

如何统计整个项目的单元测试覆盖率？

## 背景知识

目前DevEco Studio针对单元测试生成的覆盖率报告都是模块级的，暂不支持自动生成项目级的覆盖率报告，但是可以使用hvigorw命令整合各个模块的覆盖率，手动生成项目级的报告。

## 解决方案

在执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/lKmJV5ylTQKGhBnJM46xdQ/zh-cn_image_0000002658808811.png)run with coverage之后，会在对应模块的“.test/default/intermediates/test”文件夹路径下生成js\_coverage.json和init\_coverage.json文件，供后续生成覆盖率报告使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/xOr57niRQ8mO-52YYMeRzw/zh-cn_image_0000002628409546.png "点击放大")

想要整合多个模块的覆盖率报告，可以使用如下命令，将各模块的json文件在命令后使用#拼接。

```txt
hvigorw collectCoverage -p projectPath={projectPath} -p reportPath={reportPath} -p coverageFile={projectPath}/{moduleName}/.test/default/intermediates/test/init_coverage.json#{projectPath}/{moduleName}/.test/default/intermediates/test/coverage_data/js_coverage.json
```

* projectPath：工程路径。
* reportPath：指定的覆盖率报告文件生成路径。

例如项目路径是“D:/HarmonyProject/CoverageTest”，要合并覆盖率的模块是harModule1和harModule2，报告生成路径是“D:/HarmonyProject/CoverageTest/coverage\_report”，则使用如下命令即可在报告生成路径下的index.html得到整合后的覆盖率报告。

```txt
hvigorw collectCoverage -p projectPath=D:/HarmonyProject/CoverageTest -p reportPath=D:/HarmonyProject/CoverageTest/coverage_report -p coverageFile=D:/HarmonyProject/CoverageTest/harModule1/.test/default/intermediates/test/init_coverage.json#D:/HarmonyProject/CoverageTest/harModule1/.test/default/intermediates/test/coverage_data/js_coverage.json#D:/HarmonyProject/CoverageTest/harModule2/.test/default/intermediates/test/init_coverage.json#D:/HarmonyProject/CoverageTest/harModule2/.test/default/intermediates/test/coverage_data/js_coverage.json
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/G0OOPzO9QjaQIW5RwijMZg/zh-cn_image_0000002628569444.png "点击放大")

## 常见FAQ

Q：多个测试产生的类似bjc\_cov\_1742528669171.json、bjc\_cov\_1742528671121.json这样的覆盖率文件，如何合并生成总的覆盖率数据？

A：可参考[黑盒覆盖率测试](../harmonyos-guides/ide-ui-test.md)，在多模块相互跳转的场景下，取各模块的init\_coverage.json文件路径，与bjc\_cov\_1742528669171.json、bjc\_cov\_1742528671121.json文件通过#拼接生成coverageFile参数。

参数拼接示例如下：

```txt
init_coverage.json#bjc_cov_1742528669171.json#bjc_cov_1742528671121.json
```

Q：Instrument Test如何执行全部测试用例来统计覆盖率？

A：右击ohosTest目录下的test文件夹，选择![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/aErPE1QZTXCNhVbD0fZCDw/zh-cn_image_0000002658928761.png)，可以统计全部测试用例的覆盖率。

Q：Local Test用例如何获取单元测试通过率？

A：Local Test单元测试通过率的获取方法如下：

1. 运行测试：首先需要运行Local Test来执行所有的测试用例，可以在DevEco Studio中通过选择测试任务并点击运行按钮来启动测试，具体操作请见[Local Test](../harmonyos-guides/ide-local-test.md)。
2. 查看测试结果：测试执行后，会在DevEco Studio的测试结果窗口中显示详细的测试报告，包括每个测试用例的通过或失败状态。
3. 计算通过率：根据测试结果，手动统计测试用例的总数，以及通过和失败的测试用例数，然后计算通过率。

Q：如何获取增量代码覆盖率？

A：目前覆盖率统计都是全量的，无法获取增量代码覆盖率。
