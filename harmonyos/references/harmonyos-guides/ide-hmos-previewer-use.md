---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-use
title: 使用多设备预览器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 使用多设备预览器
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a1b347dcf497fcf9f2650f2a471ef9ceb189c14a26a915db576a8d598597edf8
---

## 前提条件

* 在2in1设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 在多设备预览器上运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 快速启动

1. 点击鸿蒙电脑DevEco Studio顶部的设备选择框，选择**多设备预览器**中的设备类型，支持单选或者多选，点击运行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Zsm-w42lS3KULFn79og_-g/zh-cn_image_0000002778922785.png)或调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Iq6HuBbORtmrmzuWV4opbw/zh-cn_image_0000002749483576.png)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/6Kj7xwy2Qee7gsFtbSphvg/zh-cn_image_0000002749483570.png "点击放大")
2. 等待项目编译安装完成后，拉起多设备预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/bUKSZCq_SHO3nxN1XXQZXg/zh-cn_image_0000002749323698.png)
3. 点击设备栏中的设备图标可以切换设备，滚动鼠标滚轮或使用左右箭头可以在设备过多时进行翻页。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vOIRxqn7QjGJQm4f5EZYoA/zh-cn_image_0000002749483578.png)按钮可以查看所有设备详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/1KKrAbs2TPKeI4pjR2QVNA/zh-cn_image_0000002749483574.png)
4. 多设备预览器窗口下方为设备操作按键，具体如下。

   | 按键 | 功能描述 |
   | --- | --- |
   | 返回 | 将应用返回至上一页面，直至返回到首页。 |
   | 截屏 | 对拉起的应用进行截图，截屏尺寸与当前选择的设备分辨率一致。 |
   | 折叠展开 | 仅支持折叠设备，切换设备形态至折叠/展开态。 |
   | 预览模式 | 切换至预览态，用于实时[查看应用组件树](ide-hmos-previewer-arkui-inspector.md)。 |
5. 支持使用鼠标操控屏幕、使用键盘输入等，具体参考下文介绍。

## 操控屏幕

当多设备预览器运行时，支持使用鼠标来模拟手指和设备屏幕进行交互。

| 常用操作 | 描述 |
| --- | --- |
| 点击 | 将鼠标放置屏幕上方，按住鼠标左键，然后释放。 |
| 长按 | 指向屏幕上的一个项目，按下鼠标左键，保持一段时间，然后释放。 |
| 滑动 | 将鼠标放置屏幕上方，按住鼠标左键，在屏幕上轻扫，然后释放。 |
| 拖拽 | 将鼠标放置屏幕中的项目上方，按住鼠标左键，移动项目，然后释放。 |
| 物理键盘输入 | 点击输入框，使用2in1设备的物理键盘进行输入。 |

## 使用工具栏

工具栏上集成了多设备预览器的各种调试工具和控制选项，以下对各个按键功能作简要说明。

| 按键 | 功能描述 |
| --- | --- |
| 更多 | 展开更多选项，如报告、设置。 |
| 报告 | 打开Bug报告界面，保存或上传Bug日志信息。 |
| 设置 | 设置语言和截屏保存路径。 |
| 置顶 | 打开或关闭置顶功能，打开时使多设备预览器窗口始终保持在最上层，不会被其他窗口遮挡。 |

当多设备预览器运行出现错误时，可以向我们提交错误信息。打开工具栏的**Bug报告**界面：

* 界面左侧展示了Bug出现时的设备截屏。
* 右侧可以输入再现步骤和上下文信息，勾选是否包含日志或截图。
* 点击**保存**可以将Bug的相关信息保存至本地。点击**发送**可以在线提单，提交时，请在附件里上传保存的Bug信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/TBVAHByGQEO1aYC372dwFA/zh-cn_image_0000002778922781.png)

## 移动和缩放多设备预览器

* 移动多设备预览器

  开发者可以使用鼠标拖动多设备预览器到屏幕的指定位置。
* 缩放多设备预览器

  如需改变多设备预览器大小，将鼠标悬停到预览器四角的任意一处，当鼠标变成![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/jAUOonseRUGnJh61xrvFxw/zh-cn_image_0000002779082637.png)，按住鼠标左键并移动即可缩放多设备预览器。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/-Q-leQmWTLmRhfWsI-iB4Q/zh-cn_image_0000002779082635.gif "点击放大")

## 自定义设备

除了使用多设备预览器预置的设备之外，也支持自定义设备，具体操作步骤如下。

1. 点击设备选择框，选择**添加自定义预览器**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/v1J-7hMtS6u457VUdJmiKw/zh-cn_image_0000002778922779.png "点击放大")
2. 设置设备名称，选择设备类型。如果是Phone类型，还支持选择设备子类型。

   | **设备子类型** | **说明** |
   | --- | --- |
   | Phone | 直板机 |
   | Foldable | 双折叠 |
   | WideFold | 阔折叠 |
   | TripleFold | 三折叠 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/NTBXFAiUQHieiIZ02zC4YA/zh-cn_image_0000002779082639.png "点击放大")
3. 设置屏幕尺寸。如果选择预置的机型配置，会自动填充各块屏幕的分辨率和DPI。也可选择**Custom**手动输入各块屏幕的分辨率和DPI，点击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/YycSyCaDSMKDEneJEib1Fg/zh-cn_image_0000002778922791.png)
4. 新创建的预览器会显示在设备列表中。如需删除，可点击删除按钮，即可删除该自定义设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/POyXkG9pTuSIxwpsdU9R9g/zh-cn_image_0000002779082641.png "点击放大")
