---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-use
title: 使用多设备预览器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 使用多设备预览器
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d435e174150e708194507697d50123562fa5164f85741f208c5bc6fe446154d4
---

## 前提条件

* 在2in1设备上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 > *具体的设备名称***中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
* 在多设备预览器上运行应用/元服务需要根据[配置调试签名](ide-hmos-signing.md)章节，提前对应用/元服务进行签名。

## 快速启动

1. 点击鸿蒙电脑DevEco Studio顶部的设备选择框，选择**多设备预览器**中的设备类型，支持单选或者多选，点击运行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wNwaPuE5TVmOCNjDU5VurA/zh-cn_image_0000002781470992.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C85887D2DAFF48E4D0A8F50848C6A77A25E646FEE67B064E9DC9490B0643A44)或调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/0F48e9SvREC87dTv77JXgw/zh-cn_image_0000002810750659.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBA9F393F82D59AA984C77475E87E5F028E9C3B43735734DC156374C2AA27858)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/tE2CBA1NQbmhl25qx3cKFQ/zh-cn_image_0000002781311064.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F75E605275FDDC8319A7BB19C051A0561DD54D6DA546E977455E36DA390E837)
2. 等待项目编译安装完成后，拉起多设备预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/srO034KvSmmKVLcIKrzaQw/zh-cn_image_0000002781471000.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=3811F50EB9F25FAB998AECCDB115CDB4C94768232600CD3BABA10F56CF80F41F)
3. 点击设备栏中的设备图标可以切换设备，滚动鼠标滚轮或使用左右箭头可以在设备过多时进行翻页。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/H7NjOsjwRhCgpTahQF3eTA/zh-cn_image_0000002810630553.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=699E04C039670A57530CB9694E3221AE107AAB354B217858E4A92690BD4A2D8B)按钮可以查看所有设备详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/--n6lYz4S4WbDyh64AyH1w/zh-cn_image_0000002781311060.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EC9CECF8C52F2F8A3F42F2B3910D899325C1E949CF91BF615888A43E049B46A)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/XNVwIJ6mTHq66dLJJ80AIw/zh-cn_image_0000002781470988.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=1130CDEE70BA16B27C6BC88E8C930BC5C997F0D6734C554E663DDF7B7451FAD1)

## 移动和缩放多设备预览器

* 移动多设备预览器

  开发者可以使用鼠标拖动多设备预览器到屏幕的指定位置。
* 缩放多设备预览器

  如需改变多设备预览器大小，将鼠标悬停到预览器四角的任意一处，当鼠标变成![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/M4UUb6OrQrebfJ8tRcTyWw/zh-cn_image_0000002781470994.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=51EDACAA3EC5CE35AEC3C514E2197AA6CA3446F104EA7A1D439C66B48ACD0E6D)，按住鼠标左键并移动即可缩放多设备预览器。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/PZRMS7hJREOr1vq7BvIzxA/zh-cn_image_0000002781311058.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=963B69D014A1F733F23EA868900D7A300353918C9C84FA24EE0387AAD6C4418E "点击放大")

## 自定义设备

除了使用多设备预览器预置的设备之外，也支持自定义设备，具体操作步骤如下。

1. 点击设备选择框，选择**添加自定义预览器**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/HedXDntgQUOmJsl9Ioug2w/zh-cn_image_0000002781470990.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=02673E75E1E2CD7AE0AFB0C01DB8A0C662D0C1568E949D7A4D060D3790AA9A1E)
2. 设置设备名称，选择设备类型。如果是Phone类型，还支持选择设备子类型。

   | **设备子类型** | **说明** |
   | --- | --- |
   | Phone | 直板机 |
   | Foldable | 双折叠 |
   | WideFold | 阔折叠 |
   | TripleFold | 三折叠 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/FipdNUsXQMSkLu3FCK3AXg/zh-cn_image_0000002781311062.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=9652586955A5EE4E247BD3BB476E7355669E80A9307A5D8C807DF5927B7C3C1F "点击放大")
3. 设置屏幕尺寸。如果选择预置的机型配置，会自动填充各块屏幕的分辨率和DPI。也可选择**Custom**手动输入各块屏幕的分辨率和DPI，点击**确认**完成创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/NXJwxESoSR6ybq1qcxTU2w/zh-cn_image_0000002810750663.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=3553DC6ED394A726F289B1B627619FA73E23F6C70E44FB163193FEDC39F123CE)
4. 新创建的预览器会显示在设备列表中。如需删除，可点击删除按钮，即可删除该自定义设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Rc3Z5X4eTnaWXyJCkPhyZw/zh-cn_image_0000002810750661.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=1237D96BC0356694AA3F47152D57A15DE9BBB21215949660BB260EE1AD53ADCF)
