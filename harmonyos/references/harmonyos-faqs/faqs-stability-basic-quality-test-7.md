---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-stability-basic-quality-test-7
title: 稳定性测试常见咨询FAQ
breadcrumb: FAQ > DevEco Testing > 专项测试 > 稳定性基础质量测试 > 稳定性测试常见咨询FAQ
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-30
content_hash: sha256:bcb986fe0940086c2e782ed935dea2b100f2077737cbdb5a814b0744f273d689
---

## 问题现象

* 问题一：DevEco Testing工具稳定性测试如何遍历所有tab页？是否存在不支持的场景？
* 问题二：DevEco Testing进行稳定性测试时具体有哪些初始化内容？
* 问题三：使用DevEco Testing跑稳定性测试有crash会通过吗？
* 问题四：使用DevEco Testing跑稳定性测试如何查看用户的操作，比如用户的点击，滑动操作？
* 问题五：使用DevEco Testing跑稳定性测试出现部分Web页面白屏，如何解决？

## 解决方案

* 问题一解决方案：

  DevEco Testing稳定性测试为HarmonyOS NEXT应用开发者提供面向应用的智能遍历测试手段，及稳定性测试模型管理能力。实现上采用Testing遍历引擎，尽力而为优先覆盖前三层页面，用户可以自定义遍历时长进行探索测试和场景压测：打开DevEco Testing客户端->探索测试->应用探索测试，选择模式类型为探索测试或场景压测，具体操作请参考[应用探索测试](../harmonyos-guides/other-test.md#section3638191433115)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/u0TX-Rk2Qemouf-nb-m3hQ/zh-cn_image_0000002628563434.png "点击放大")

  遍历规格请参见[是否支持对使用Flutter等三方框架开发的应用进行测试](faqs-deveco-testing-faq-5.md)。

* 问题二解决方案：

  DevEco Testing稳定性测试的环境初始化会先进行解析应用信息，然后检查设备状态，最后进行环境初始化操作：测试应用的安装状态（支持已安装的应用和安装新的应用），初始化后将遍历任务推入设备执行遍历任务。可打开DevEco Testing的测试任务，选择稳定性基础质量测试的任务，查看执行日志：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/P5bkuLS9Q3KR7zsfEF2NDg/zh-cn_image_0000002658922741.png "点击放大")
* 问题三解决方案：

  如果出现crash，测试结果会不通过。
* 问题四解决方案：

  DevEco Testing日志会记录用户的操作，日志路径：resources\data\XXX\resources\kingkong\_log，一共五类，点击操作：[INFO] touch 、滑动操作：[INFO] swipe 、返回操作：back event、指关节：knuckle single finger、捏合：pinch double fingers。日志路径如图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/sNv_YDJtQxep_qfDSXdNvw/zh-cn_image_0000002628403534.png "点击放大")
* 问题五解决方案：

  建议用户排查下是否在高级配置里开启了MemDebug模式开关，如果打开此开关，工具会开启asan\_wrapper检测内存，可能会出现应用概率启动时自动退出、JS对象的方法概率丢失等问题，请用户关闭MemDebug模式开关即可。
