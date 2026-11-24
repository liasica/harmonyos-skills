---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-use
title: 使用多设备预览器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 使用多设备预览器
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eefbdf7868c781189a61bb449c9006e42223ef699cc750b54acc123f23bbf57e
---

## 前提条件

* 在2in1设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 在多设备预览器上运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 快速启动

1. 点击鸿蒙电脑DevEco Studio顶部的设备选择框，选择**多设备预览器**中的设备类型，支持单选或者多选，点击运行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/x6D7bMFoTNW-sQVHRMXv7w/zh-cn_image_0000002820721193.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=55C2DC8DC6A728146DA71B2A23BD1C3FF842C730687013A8B3B9EA3B5B3D7BE7)或调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/VbAPeUF5TKWGmSK3QNdAFw/zh-cn_image_0000002792001212.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=83950127D6627A62D2F4ABC8560E691C987FEB81DC32F48391D254BD48B7663A)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/50KoegEUReickxRo-L6OJg/zh-cn_image_0000002820681179.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3C3C9C786EA7427FA3833A5933A6FCEA9F99661902B3B73BFF81A4B0AF5D710)
2. 等待项目编译安装完成后，拉起多设备预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/i0oHOlUMSe6o6B8FiZbUdg/zh-cn_image_0000002792001220.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2A932EDF0D08C95442EBCE6DBDBC3AFEC850C06213804E71F4731962C7DBB74)
3. 点击设备栏中的设备图标可以切换设备，滚动鼠标滚轮或使用左右箭头可以在设备过多时进行翻页。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/mntRb40fQC2KOYjejAjZbw/zh-cn_image_0000002820681181.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C4A253FFF890806D8E35737783954CC17156E006B101985A2980B54332912AC)按钮可以查看所有设备详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/IigmFjcCRMCUrEM6xJew7Q/zh-cn_image_0000002820721189.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=500B1C2BDD4058C95710284E83EC039C959CB9AE7F10CD85AEC20692A9F400CD)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/70X7i8JJQ8uKxdCtiudQPw/zh-cn_image_0000002791841242.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8EF45513CBCD262FC31F4BD8A874E22FD1404D20F39263ADDB2A7D6F7696A85)

## 移动和缩放多设备预览器

* 移动多设备预览器

  开发者可以使用鼠标拖动多设备预览器到屏幕的指定位置。
* 缩放多设备预览器

  如需改变多设备预览器大小，将鼠标悬停到预览器四角的任意一处，当鼠标变成![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/FnBqATNCSji4ndoGYp9pbA/zh-cn_image_0000002820681187.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=40D76F1B38D171767773D0F8FE30D02363F5932D236D267EE2EB2EA41E3713F8)，按住鼠标左键并移动即可缩放多设备预览器。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Vp1RW2XWR2ysgNGkx0Pihw/zh-cn_image_0000002791841238.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=04C874709EF80B3F5C0CF209A681CD9B200CD911B962455E302F63FFA77668FD "点击放大")

## 自定义设备

除了使用多设备预览器预置的设备之外，也支持自定义设备，具体操作步骤如下。

1. 点击设备选择框，选择**添加自定义预览器**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/q1NMN6yTSbilTXuxeUkJJA/zh-cn_image_0000002820681183.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF6B9BE34EC146A148DD93E613B679D86C0FBA0BBE81F388F8CC81B60EBF9333)
2. 设置设备名称，选择设备类型。如果是Phone类型，还支持选择设备子类型。

   | **设备子类型** | **说明** |
   | --- | --- |
   | Phone | 直板机 |
   | Foldable | 双折叠 |
   | WideFold | 阔折叠 |
   | TripleFold | 三折叠 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/2YZsbuAhQi6CLxJ4Wyy_Qg/zh-cn_image_0000002791841244.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A745A6190307F6DA8E80F7B48E24591C13DDDE83D5B4BFAA7E0AA1090C467C0 "点击放大")
3. 设置屏幕尺寸。如果选择预置的机型配置，会自动填充各块屏幕的分辨率和DPI。也可选择**Custom**手动输入各块屏幕的分辨率和DPI，点击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/N84tn92YRp6fVjphJ1iiBg/zh-cn_image_0000002820681191.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=8161F29EDAA3865AD75B344EAC8FD1ADFE3F0D32B411E6488A2AC5B76B53FE59)
4. 新创建的预览器会显示在设备列表中。如需删除，可点击删除按钮，即可删除该自定义设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/qPzk5vYaQXCVcNDlYUzauQ/zh-cn_image_0000002792001228.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A2A7104F9C095FAD453A19B0436FBA2C86AEF6EF0FBB06C5775DF8E44F4C543)
