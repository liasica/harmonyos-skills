---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-39
title: 折线图等复杂图表页面操作浏览丢帧
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 折线图等复杂图表页面操作浏览丢帧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e13d65be2097a8f7a1f3ceeb3166c93e172be434a4e47a37779ba62d86e834c8
---

## 问题现象

折线图等复杂图表页面，通过手指拖动十字准星可以展示横纵坐标等具体信息，在连续拖动时发生丢帧现象。

## 背景知识

* **屏幕刷新率：**

  屏幕刷新率的意思是每秒钟屏幕会刷新的次数，即120Hz是一秒内刷新120次，平均一次耗时8.33ms。由此可得：

  | 刷新频率 | 平均单次耗时 |
  | --- | --- |
  | 120Hz | 8.33ms |
  | 90Hz | 11.11ms |
  | 60Hz | 16.67ms |
* **ui线程Trace拆解**：

  | Trace点 | 含义 |
  | --- | --- |
  | flutter::VsyncProcessCallback | 接收处理Vsync信号。 |
  | flutter::PlatformConfiguration::begin\_frame\_ | 进行flutter的“beginFrame”、“Microtasks”的任务。 |
  | flutter::PlatformConfiguration::draw\_frame\_ | 进行flutter的“drawFrame”的任务。 |
* **raster线程Trace拆解**：

  | Trace点 | 含义 |
  | --- | --- |
  | flutter::GPURasterizer::Draw | 消费pipeline的任务。 |
  | flutter::Rasterizer::DrawToSurface | 真正的“消费pipeline的任务”。 |
  | flutter::CompositorContext::ScopedFrame::Raster | 进行flutter的“绘制操作”，包括“Preroll”和“Paint”任务。 |
  | flutter::LayerTree::Preroll | 遍历所有子图层，执行具体图层的Preroll()方法，并设置绘制范围。 |
  | flutter::LayerTree::Paint | 遍历所有子图层，执行图层的绘制操作。 |
  | flutter::SurfaceFrame::Submit | 提交绘制的内容，包括“Flush”和“SwapBuffers”任务。 |
  | flutter::SkCanvas::Flush | 清空GPU的渲染缓冲区并将命令提交给GPU执行的操作。 |
  | flutter::OhosContextGL::SwapBuffers | 缓存交换操作。 |

## 问题定位

1. 通过ArkUI Inspector获取图表页面布局信息，可以看到是一个FlutterPage。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/OzC3YOIYTC-9ynmmgg_x_A/zh-cn_image_0000002628395270.png "点击放大")
2. 使用DevEco Profiler中的Frame模板抓取连续拖动准星显示坐标详情这一过程的Trace。在render\_service主泳道找到H:PreferredFrameRate子泳道，光标悬停在绿色区域可以看到当前屏幕刷新率为120Hz，根据背景知识中的换算结果可以得出单帧绘制时间超过8.3ms时就会出现掉帧现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/E_ykvOP1R3SG7ttx0BsJbA/zh-cn_image_0000002658794545.png "点击放大")
3. 由于是Flutter页面，在应用包名主泳道中找到1.ui和1.raster线程，根据ui线程中H:flutter::Animator::BeginFrame frame\_number:5931Trace点的frame\_number，在raster线程中找到对应的H:flutter::Rasterizer::DoDraw frame\_number:5931，可以看到从接收处理Vsync信号（flutter::VsyncProcessCallback）到提交GPU绘制（flutter::SurfaceFrame::Submit），单帧处理耗时26.7ms，远超当前屏幕刷新率下单帧绘制时间上限8.3ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Ys11NcN6QJqlc1IfbHps5g/zh-cn_image_0000002628555184.png "点击放大")
4. 对于单帧的ui线程耗时情况，可以看到flutter::PlatformConfiguration::draw\_frame\_Trace点耗时15.3ms占比99%，这部分是在进行flutter的“drawFrame”的任务，是应用侧业务内容。因此是页面结构、业务逻辑复杂导致单帧绘制耗时长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Tocu6dlNQyuOllzcuy0pAw/zh-cn_image_0000002658914507.png "点击放大")

   对于单帧的raster线程耗时情况，可以看到flutter::LayerTree::PaintTrace点耗时8.5ms占比75%，这部分是在遍历所有子图层，执行图层的绘制操作。结合实际页面，折线图大量数据展示的组件多层嵌套且跟随坐标变化而更新，因此Paint过程耗时也是由于页面结构、业务逻辑复杂导致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/0U21IZzSSv2uBLBJkv2gfA/zh-cn_image_0000002628395276.png "点击放大")

## 分析结论

页面结构、业务逻辑复杂导致ui和raster线程单帧处理时间过长，单位时间内送帧数减少导致丢帧。

## 修改建议

简化ui组件结构和业务逻辑，如降低Widget嵌套层级，控制重绘范围。
