---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-child-process
title: 调试Native子进程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 调试Native子进程
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:03+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1ee93231b389c10265e7d1e61c84e32d92619998d8baace95e08015a56d3a024
---

从26.0.0版本开始，DevEco Studio支持调试Native子进程，包括[扩展进程（C/C++）](capi-nativechildprocess-development-guideline.md)和[应用程序包集成bin文件开发的子进程](../doccenter-getting-started/hap-bin.md)。

## 使用约束

* 对扩展进程（C/C++）进行调试时，支持API 26.0.0及以上版本的2in1设备；对应用程序包集成bin文件开发的子进程进行调试时，支持API 26.0.1及以上版本的2in1设备。
* 通过OH\_Ability\_StartNativeChildProcess接口创建Native子进程时，不支持调试[隔离模式](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationmode)（NCP\_ISOLATION\_MODE\_ISOLATED = 1）的Native子进程。
* 通过OH\_Ability\_CreateNativeChildProcess接口创建Native子进程时，不支持调试[独立uid](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationuid)的Native子进程。

## 调试配置

调试器会自动从模块编译输出目录查找符号文件。

```screen
<module>/build/<product>/intermediates/libs/<target>/<abi>/
```

<product>和<target>默认均为default，<abi>由设备架构决定（如arm64-v8a、x86\_64）。

本地编译的so/bin通常无需额外配置。以下两种情况需要手动配置。

### 添加符号路径

**场景**：调试bin文件，或调试非本地编译的so文件。

打开运行/调试配置面板，点击**Debugger >** **LLDB Startup Commands** **> +**添加命令，支持添加多个路径。

```screen
settings append target.exec-search-paths "<符号文件所在文件夹路径>"
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/OjXldLSPSkeXnE7BGquT-Q/zh-cn_image_0000002808766233.png "点击放大")

### 添加源码映射

**场景**：so/bin文件非本地编译时，编译路径与本地源码路径不一致，会导致断点无法命中，需要添加源码映射。

打开运行/调试配置面板，点击**Debugger >** **LLDB Startup Commands** **> +**添加命令。

```screen
settings set target.source-map "<编译时路径>" "<本地源码路径>"
```

* 编译时路径：符号文件中记录的源码路径，可通过dwarfdump或LLDB image dump symfile查看。
* 本地源码路径：本地对应源码文件的实际路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/i6b5J90pRv6KwPCJMVhfQA/zh-cn_image_0000002808766239.png "点击放大")

调试过程中如果找不到源码文件，DevEco Studio也会在反汇编窗口顶部弹出通知，点击后可直接选择本地文件完成映射。

## 调试方式

通过attach方式对Native子进程进行调试，在attach窗口中直接选择子进程进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/ECsa_uaWSpuW512R1yAbVA/zh-cn_image_0000002808886317.png)

或者先attach调试主进程，再点击调试面板的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/pdZcP7QjTPqhpC75iIj6ig/zh-cn_image_0000002808886313.png)，打开attach窗口选择子进程进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/qZVChRlISlqvrsQxtOmqcw/zh-cn_image_0000002779406670.png)

## 常见问题

| 问题 | 解决措施 |
| --- | --- |
| 断点空心圆、不命中 | 编译路径与本地不一致，添加源码映射。 |
| 调用栈只有地址、没有函数名 | 符号文件未加载，检查符号路径配置。 |
| 提示"找不到符号文件" | 模块未编译或编译输出为空，重新构建项目。 |
