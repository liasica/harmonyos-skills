---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-39
title: 应用上架检测反馈存在RS前台空跑现象
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用上架检测反馈存在RS前台空跑现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e48f63d84580a8617c23a9217dd72328d66d21400adccfee3e17445cf311e8c0
---

## 问题现象

应用上架检测驳回，反馈问题：应用在前台存在不合理使用不可见动画的问题，应用在前台不允许有RS绘制空跑。

## 背景知识

上架检测RS空跑拦截标准：skip/(duration/1000) > 10，每秒10次（帧）以上不可见刷新，认为是存在不可见动效。

## 问题定位

**一、环境准备**：

1. 打开手机相关日志和Trace开关。
   * 打开USB调试开关：设置-系统-开发者选项-USB调试。
   * 打开图形debug日志：

     ```shell
     hdc shell hilog -b D -D 0xD001400
     hdc shell hilog -b D -D 0xD001406
     ```
   * 设置屏幕休眠时长10分钟，防止测试过程中快速休眠：设置-显示和亮度-休眠。
2. 升级最新的ROM版本。
   * 使用DevEco Studio 6.0.0.274及以后的版本，插入设备。
   * 下滑entry入口，打开Enable DebugLine开关。
   * 编译debug版本应用安装到设备。

**分析流程**：

1. 复现空跑异常操作路径：打开DevEco->Log，过滤DisplayNode skip关键字；按照上架检测测试步骤操作，发现有频繁打印（每秒5次以上）则判断当前界面有空跑异常。
2. 按照复现路径抓取详细信息：
   * 抓取Trace信息：点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，抓取15s左右信息。观察Energy Anomaly泳道，标注红色异常则为识别到了空跑异常。
   * 分析Trace信息：
     + 点击Energy Anomaly泳道红色区域会展示Details信息。
     + 点击Details的Anomaly Count会展示More信息，More信息展示的是每一帧空跑VSyncId和持续时间。
     + 右边有个跳转箭头，点击会跳转到当前空跑帧的详细信息。
     + 在空跑帧界面，点击Details模块下的Open Layout打开布局展示。
     + 在Component Tree展开布局组件，左边有感叹号图标的则为当前空跑帧的组件。

## 分析结论

前台RS空跑可能是应用侧使用的动画效果在离开页面后没有及时停止，可能是系统动画、lottie动画等，具体原因需要应用侧进行排查。

## 修改建议

当前系统为了便利开发者，对一些常用的动图内置了可见性接口，防止其空跑。例如，lottie库版本在2.0.14及以上、apng库版本在1.1.2及以上。如果开发者未对此类三方动画库的播放控制进行封装或修改，可直接通过更新库来避免不可见时的空跑问题。如果已进行封装或修改，则建议按照以下两种方法进行修改。

方法1-监听法：通过监听组件是否可见，管理刷新动画的不可见现象。

方法2-可见法：通过监听组件移出屏幕的事件，修改动画播放状态，从而控制空跑。

## 总结

RS空跑常见于加载动画、刷新动画未及时停止等场景，建议引导开发者对应用中的动画进行排查。
