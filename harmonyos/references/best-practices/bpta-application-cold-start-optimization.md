---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-cold-start-optimization
title: 应用冷启动时延优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 应用启动与响应优化 > 应用冷启动时延优化
category: best-practices
scraped_at: 2026-04-28T08:22:32+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:12659382fbf803da42e80ac6051e415642543c85e799e0d35038bb2e09c05db9
---

## 概述

应用启动时延是影响用户体验的关键要素，是指从用户点击桌面应用图标、通知或其他入口启动应用，到应用界面内容成功加载并显示在屏幕上的时间间隔。如果这段时间超过3秒，将显著影响用户体验。

应用启动可以分为冷启动和热启动。当应用启动时，后台没有该应用的进程，系统会重新创建应用的进程，这种启动方式就叫做**冷启动**。而**热启动**是当应用程序已经在后台运行，用户再次打开应用程序时，应用程序仍然在内存中，可以直接从内存中加载并继续之前的状态，而不需要重新初始化和加载资源。

当应用冷启动时延大于1100ms时，可以认为是应用启动缓慢，体验标准可以参考[应用流畅体验设计](bpta-smooth-application-design.md)。

本文将介绍以下内容，帮助开发者提升应用的冷启动速度，避免启动过程中的延迟。

* [应用冷启动流程](bpta-application-cold-start-optimization.md#section196451814101216)
* [应用冷启动时延检测](bpta-application-cold-start-optimization.md#section860412154015)
* [应用冷启动时延问题分析](bpta-application-cold-start-optimization.md#section167931444111612)
* [识别启动缓慢问题](bpta-application-cold-start-optimization.md#section8516174361218)
* [提升应用冷启动速度](bpta-application-cold-start-optimization.md#section1770316268136)

## 应用冷启动流程

优化应用冷启动体验前，了解应用冷启动的流程和重要生命周期。应用冷启动分为5个阶段：应用进程创建&初始化、Application&Ability初始化、Ability/AbilityStage生命周期、加载绘制首页、网络数据二次刷新。

**图1** 应用冷启动流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/mfBLvD56Roeh0OD6R-Xe1g/zh-cn_image_0000002512014501.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=2E61FB39D14D4FB5545B2C7FB1E45AE65272B19D671F76E854782744934EA170 "点击放大")

1. 应用进程创建和初始化阶段：此阶段系统完成应用进程的创建和初始化，包括启动页图标（startWindowIcon）的解码。
2. Application和Ability初始化：该阶段包括资源加载、虚拟机创建、Application&Ability 对象的创建与初始化、依赖模块加载等。
3. Ability/AbilityStage 生命周期：此阶段主要涉及 AbilityStage/Ability 的启动，执行相应的生命周期回调。
4. 加载首页内容，测量布局，刷新组件并绘制。
5. 网络数据二次刷新：此阶段应用根据业务需求对网络数据进行请求、处理和刷新。

若要提升应用冷启动速度，需缩短上述阶段的耗时。

## 应用冷启动时延检测

在应用开发中，网络请求时机、图片下载、页面资源加载、依赖模块的加载等，都会导致应用冷启动时延受到影响，合理处理代码逻辑可以提升应用冷启动速度。开发者可以通过[AppAnalyzer](bpta-performance-detection.md#section135451444171)对应用冷启动进行检测，针对诊断出的应用冷启动不达标问题进行分析和优化。

应用冷启动时延检测步骤如下：

1. 选择entry模块，暂时关闭模块build-profile中的混淆开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/_WSSQjCzTlWq1pwwqP1hxA/zh-cn_image_0000002510840649.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=8A9D73FE56806586174910355EE4FEA14B0E750220C04E1A3FC3075CC6F3E389 "点击放大")
2. 检查一下build模式，改为release。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/TDTWF9N5RkW2bwnDhl1hgA/zh-cn_image_0000002478640720.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=3972FB9EAFB755707F1D100B43AFF15F3B98110436ED9EF0BA0AD07E13D7C31D)
3. 点击菜单 -> tool -> AppAnalyzer，打开体检工具。
4. 选择“场景化体检”，点击“手动性能冷启动体检”。

   工具开始准备，会自动编译、安装、运行当前工程，此时需要“保持手机解锁状态”，当准备完成后，会提示点击开始按钮，开始体检。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/3TFbiKMlT2iAqOFp5GqpNg/zh-cn_image_0000002478800706.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=22407044994A294F30923EAA4565E178F9CF313311CD43EA7A3B221B6CBDB454 "点击放大")
5. 根据提示在设备上进行手动操作：
   1. 首先，在最近任务列表关闭应用。
   2. 进入手机设置 ，在顶部搜索栏中输入应用名并，点击进入应用设置界面，如果该应用还有进程存活，在应用设置界面可以点击强行停止按钮。
   3. 在桌面点击应用图标重新启动应用。
   4. 点击“结束”按钮停止体检任务，体检工具会将刚才的操作数据进行解析。

说明

冷启动体检需要强行停止应用：

1. 进入手机设置。
2. 在顶部搜索栏中输入应用名并点击进入应用设置界面。
3. 在应用设置界面点击强行停止。
4. 在桌面启动待检测的应用。

## 应用冷启动时延问题分析

AppAnalyzer详情报告中会显示动态检测可能导致冷启动完成时延不达标的故障原因，并提供相应的优化建议，此处列举以下冷启动时延不达标问题原因进行说明：

### **高耗时非UI操作**

高耗时函数可能会造成应用卡顿，对于执行次数较多的函数，应尽量减少调用次数，单次执行但总耗时较高的函数，可以考虑通过异步方式进行优化。

在检测结果中，开发者可以通过点击报告表格中的对应方法名，快速跳转至对应代码片段，同时体检工具也会给出相应的优化建议，如将耗时函数放到子线程或进行缓存、使用多线程能力等，详细流程及示例可参考文档：[主线程耗时操作优化--其他主线程优化思路](bpta-time-optimization-of-the-main-thread.md#section4365993361)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/VEmzqTLuQt6Dv7cTdmh-sQ/zh-cn_image_0000002510841011.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=7B229AAD8390B7E2C4FFC442513E0D4E1F985935B81C055FC2968FAEB4D665C3 "点击放大")

### **import加载耗时**

体检工具可以检测出应用冷启动过程中累计加载的文件数量、未使用的文件数量和加载总耗时，开发者可参考以下优化思路和流程，对此类冷启动问题进行优化。

**import加载耗时问题优化思路**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/1QksrQqdSZuegB96O6U6VA/zh-cn_image_0000002510761277.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=012FE46E0072575D4576699E526D0827B7BB97A95DAA0B78706B1411286D4264 "点击放大")

1. 分析模块使用情况：查看总结信息和未使用文件import列表信息，包括加载文件总耗时，和未使用文件数量和总耗时，了解未使用文件import情况。
2. 查找依赖关系优化导入：点击第一个“下载”按钮下载全量依赖关系文件，使用调用链搜索框查找未使用文件依赖关系，结合代码逻辑对未使用文件进行延迟加载。
3. 标记优化状态：点击第二个“下载”按钮下载全量import清单文件，统计已优化和未优化的未使用文件，分析全量文件的依赖关系。
4. 再次进行冷启动检测：优化耗时最多的几个文件之后，再次进行冷启动检测，验证整改收益。在逐步优化未使用文件导入的过程中，收益会逐步降低，开发者需根据实际情况是否需要继续“lazy import”的整改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/MIJbVDlZQbC2tkfXkwmhDA/zh-cn_image_0000002478801360.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=6166DD4515D18A207903C3A027446504FE6C24A9ACFB6B780CC8C444162EA3A1 "点击放大")

**import加载耗时问题优化流程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/QOCSeotnSGCy6i2X_Ya4Yw/zh-cn_image_0000002478641376.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=2C55DF33ECC56B9FAAA3A412050108B13EECE9894386C0177204FBBBA2FA317A "点击放大")

1. 查找耗时最高的未使用import文件。

   在本地浏览器中打开下载的依赖关系的文件full\_dependency.html，视图中左侧列表表示已加载未使用的文件，并且按照耗时从高到低排序；右侧表示已使用文件，开发者需要关注未使用文件中耗时较多的几个文件导入，例如DetailView文件的导入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/q4Nw0Gy3Q5yzz2pxP7rmOg/zh-cn_image_0000002510841309.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=E59FE11D01F67BAC7939614DCE28CDBA1080EB1E70344B27AF55C022B8300C7A "点击放大")
2. 根据文件名检索文件调用关系链。

   在搜索框中通过文件名DetailView进行检索，该文件的依赖关系则会在下方节点视图中展示，并且默认会展示其子节点的使用情况，未使用的文件会被标红显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/H_o_Ber7SY6oedjEJtFVTQ/zh-cn_image_0000002510761285.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=4C017C9D55E498338E3B33CC0133224E88066B90525FB01296FDC1BBA1ADAC45 "点击放大")
3. 查看检索文件的上层和下层文件节点信息。

   查找上层文件节点信息，即目标文件被导入的位置；查找下层文件节点信息，目标文件的耗时是否由其子节点导致，如果下层文件耗时较长，则需要考虑优化子节点的导入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/KnOlOthsTo2rLryZS4lCpw/zh-cn_image_0000002478801366.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=FDE99F2DE40D76D4DB7B388ABAAA85418FDF4266CFA999BB52A35F92EFFFE393 "点击放大")
4. 判断上层文件是否为为其他module的Index.ets文件导出。
   * 如果上层文件不为其他module的统一对外暴露接口文件（例如Index.ets），则可以在上层文件中使用对该模块使用lazy import进行优化。

     ```
     1. import lazy { DetailView } from '../view/DetailView';

     3. @Entry
     4. @Component
     5. struct Index {
     6. build() {
     7. // ...
     8. }
     9. }
     ```
   * 如果上层文件为其他module的统一对外暴露接口文件（例如Index.ets），则需要通过import路径展开性能优化。

     例如CustomLayout1上层模块为library模块的Index.ets，其中有多个文件导出。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/5RChflRUToCDASZPH06QYg/zh-cn_image_0000002478641380.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=AA3E07580E81C024238B81AC7523DCB2CF68357F07F63E0960837D53FAEF4235 "点击放大")

     在Entry的首页通过依赖对应模块引入，会导致冷启动阶段将CustomLayout2和CustomLayout3等冷启动阶段无用的文件导入。

     ```
     1. // entry/src/main/ets/pages/Index.ets
     2. import { CustomLayout1 } from 'library';
     ```

     具体优化方案，则是通过在import时，对路径展开进而优化性能。

     ```
     1. // entry/src/main/ets/pages/Index.ets
     2. import { CustomLayout1 } from 'library/src/main/ets/pages/CustomLayout1';
     ```
5. 在导出文件中标记已修改的文件。

   在下载全量import文件清单表格中，标记已优化的未使用文件，便于优化备忘，特别是当需要优化的文件比较多的时候。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/mHJ2KkGvRFu40HlhyWfasQ/zh-cn_image_0000002510841315.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=EC2FD00F263E3B5C75FCBAF74ECC3C85DF62580798DA332EEDE8B244E5A216AE "点击放大")
6. 重新进行冷启动场景化检测。

   当优化完成后，重新进行冷启动场景化检测，查看优化收益是否达到预期，如未达到预期，则需要重新进行分析优化。

### **网络请求耗时**

应用首页内容需要通过网络请求获取数据并显示时，网络请求耗时和网络请求发起的时机，对应用冷启动时长会产生一定影响。使用AppAnalyzer能够检测出应用中请求URL的请求耗时和点击离手到请求发起间隔。

* 网络请求本身耗时长

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bp1O3XVrQvOWMijeS_90QA/zh-cn_image_0000002478801796.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=250592BCD41A17860194C7BC6E950469BD1D5C0DE18958D091769B00A182A74B "点击放大")

  网络请求本身是否耗时可通过检测结果中的请求耗时时长来进行判断，时间越长，则网络请求本身耗时越久。详细分析请参考：[网络诊断：Network分析](../harmonyos-guides/ide-profiler-network.md)。

  网络请求本身耗时长，可对该URL请求进行预连接和预解析来优化网络传输速度，提前完成DNS查询和TCP/TLS握手，即在应用启动或空闲时提前建立并维护一个持久的连接池；还可以使用CDN来优化网络传输速度，即将静态资源部署到CDN上。
* 网络请求发起太晚

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/L4QXSlMDTeqW7TEdmOTmYg/zh-cn_image_0000002478641822.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=4A77936D1A06D8C6D394D02E85FB19A92FF2BB40DBAE3BA55286304E11F604AE "点击放大")

  点击离手到请求发起间隔则表示用户进行点击操作后，到真正向服务器发起网络请求的那一刻止，这中间所经过的时间。可通过检测结果中的点击离手到请求发起间隔时长来进行判断，时间越长，则表示网络请求发起的越晚。可通过提前发起网络请求，来进行优化。可参考：[网络请求提前发送](bpta-application-cold-start-optimization.md#section199911250658)。

如果开发者既无法优化网络请求本身耗时，也无法将网络请求提前发起，可以考虑提前将网络请求数据缓存，下次冷启动时候直接加载缓存数据，再通过发送网络请求二刷刷新数据。

### **首页组件复杂度高导致构建耗时**

首页组件复杂度较高会影响首页加载绘制耗时，AppAnalyzer工具能检测出页面中组件自身创建是否耗时过长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/uzIv_H-bRHSFRtbMCejRbg/zh-cn_image_0000002478641864.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=A0CC11CEA6DE6E71642152DD94A8B05AC449597546E7423FBF28300DDEC06458 "点击放大")

在静态检测可能故障原因表格中，可点击源文件定位到创建耗时的UI组件，根据提供的可能故障原因，去对UI组件进行相应优化修改，即可减少该UI组件自身创建耗时。

开发者可采用以下方式，控制UI的渲染范围，防止页面卡顿或掉帧：

* **合理控制元素显示与隐藏**

  在应用开发中，控制页面元素的显示与隐藏是一种常见的场景，通过Visibility.None、if条件判断等都能够实现该效果。visibility属性可以控制元素在布局阶段是否参与布局渲染，if条件判断控制的是组件的创建、布局阶段。
* **懒加载**

  懒加载LazyForEach是一种延迟加载的技术，通常应用于长列表优化、瀑布流优化等数据量较大、子组件可重复使用的场景，当用户滚动页面到相应位置时，才会触发资源的加载，以减少组件的加载时间，提高应用性能，提升用户体验。

### **异步线程阻塞主线程**

当主线程长时间等待子线程或异步函数返回，会造成主线程长时间被阻塞，可能导致时延不达标的情况。体检工具会对主线程长时间被阻塞进行检测，可以根据检测结果中主线程空闲时间判断主线程是否长时间被阻塞，空闲时间越长，则阻塞时间越久，详细请参考：[主线程长时间被阻塞](bpta-click-to-complete-delay-analysis.md#section73671398291)。

## 识别启动缓慢问题

开发者需要分析启动过程的耗时瓶颈，优化应用或服务的冷启动速度时，可使用Profiler的Launch场景分析功能，录制启动过程中的关键数据，识别启动缓慢的原因。Profiler Launch可拆解应用冷启动过程，抓取各阶段的耗时数据，帮助开发者快速分析冷启动过程的耗时瓶颈。Launch的具体使用方法参见[冷启动分析：Launch分析](../harmonyos-guides/ide-launch-overview.md)。

已录制一段Launch任务，具体操作步骤请参考[性能问题定位：深度录制](../harmonyos-guides/deep-recording.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/U11v0doYT1SQYlm2j2rdqQ/zh-cn_image_0000002193851180.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=C36B3E093433724F94635EECAE6700DE56E93AE840DA9C107988B3377AFB3DF6 "点击放大")

上图显示，Launch将应用的冷启动过程分为以下几个阶段：

1. Create Process：应用进程创建阶段，对应的trace打点为AppMgrServiceInner::StartProcess。
2. Application Launching：应用启动阶段，对应的trace打点为AppMgrServiceInner::AttachApplication##{bundleName}。
3. UIAbility Launching：UIAbility启动阶段，对应的trace打点为MainThread::HandleLaunchAbility##{bundleName}。
4. UI Ability OnForeground：应用进入前台阶段，对应的 trace 打点为 AbilityThread::HandleAbilityTransaction。
5. First Frame - App Phase：App首帧渲染提交阶段，对应的trace打点为H:ReceiveVsync，H:MarshRSTransactionData。
6. First Frame - Render Phase：RS首帧渲染提交阶段，对应的trace打点为H:ReceiveVsync和H:RSMainThread::ProcessCommandUni。
7. EntryAbility：应用启动之后的阶段，渲染完成，首页显示。

说明

阶段1对应图1中的第1阶段，阶段2对应图1中的第2阶段，阶段3和4对应图1中的第3阶段，阶段5和6对应图1中的第4阶段，阶段7对应图1中的第5阶段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/E7CUhE8RQiiVFRm_P4Bfag/zh-cn_image_0000002194010752.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=4D5918C0EA1DABD301ADC6886948DA85F4E6900FFED1D80A07E3954113FFA3D2 "点击放大")

**冷启动缓慢示例分析**

运行以下示例代码，开发者可以明显感知到应用启动速度较慢。接下来，开发者可以通过此示例，结合 Launch 分析应用冷启动缓慢的问题。

```
1. const LARGE_NUMBER: number = 200000000;

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. aboutToAppear(): void {
9. console.log('aboutToAppear');
10. this.computeTask();
11. }

13. computeTask(): void {
14. let count: number = 0;
15. while (count < LARGE_NUMBER) {
16. count++;
17. }
18. }

20. build() {
21. Row() {
22. Column() {
23. Text(this.message)
24. .fontSize(50)
25. .fontWeight(FontWeight.Bold)
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

[ColdStartSlow.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ColdStartSlow.ets#L17-L47)

首先创建Launch分析录制，可以观察到整个启动时间较长。UI Ability OnForeground阶段在应用冷启动过程中耗时最多，达到了3.3秒。因此，需要重点分析该阶段的耗时。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/NxKet-oDR86k56KipyeEFA/zh-cn_image_0000002375918437.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=6934C6D33EF349F15AE5B0CFEF1B105C5ACF2A1BBC0EBE354CCD933E06BB2C6B "点击放大")

针对应用冷启动问题的性能分析，可以选择分析主线程的Trace数据或采样得到的函数热点。

**分析主线程的Trace数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/1DVqUke9SvWpQ2uqNC5C0w/zh-cn_image_0000002341876318.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=5473C8745D8DEA9405BF4B3826158847F2497E22D24F58D1AD5FFF8B070CE40F "点击放大")

1. 单击“Launch”泳道上的UI Ability OnForeground阶段，在下方“Details”面板中可查看所选阶段的耗时统计。
2. 展开UI Ability OnForeground统计信息折叠表，可查看各函数的具体耗时信息。
3. 根据Duration找到耗时最长的函数aboutToAppear。
4. 单击图标按钮，可直接跳转至主线程的打点任务，查看相关Trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/DlCxgoM9TVOX2CwnBXYpzQ/zh-cn_image_0000002375834697.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=470491510183FDF1A65B2A76F2FD1D345810AAD9DD610BA82A05A9CBA4AB5788 "点击放大")

在UI Ability OnForeground阶段的耗时主要由aboutToAppear引起。通过分析aboutToAppear中的代码逻辑，可以确定计算任务computeTask是导致耗时的原因。

**分析采样得到的函数热点**

开发者也可以分析采样得到的函数热点直观的显示应用冷启动过程中具体函数的耗时，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/EA6R3HQzTXqzUsFWy_DKAw/zh-cn_image_0000002375915041.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=E0CD6B52E016DDD70F8B7BB0CBB3D428086A0CD227E48A471501B387ECA5CE8A "点击放大")

1. 单击“Launch”泳道的UI Ability OnForeground阶段。
2. 选择“ArkTS Callstack”泳道，它会基于时间轴展示CPU使用率和状态变化，以及当前调用栈名称和类型。
3. 在“Details”详情面板中，可以查看这段时间内的函数热点，以Top-Down形式的树状列表展示。computeTask函数在aboutToAppear函数中耗时最多，占整个阶段的97.9%。双击该函数可跳转到源码。
4. 此外，点击底部Flame Chart按钮打开火焰图可以更直观的看出热点函数的耗时情况，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/jEOvsgTjQLignfdsg48hEg/zh-cn_image_0000002342038042.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=ACB232703BD9733767427F004026D20A0A8EDBE1DA48B5D10DF11FD54B20BA12 "点击放大")

**冷启动速度优化**

通过前面的分析，冷启动缓慢的原因是在aboutToAppear方法中执行了耗时计算任务。可以将computeTask以异步延时的方式处理，优化后的代码如下：

```
1. const LARGE_NUMBER: number = 100000000;
2. const DELAYED_TIME: number = 1000;

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. aboutToAppear(): void {
10. console.log('aboutToAppear');
11. this.computeTaskAsync();
12. }

14. // ...

16. computeTask(): void {
17. let count: number = 0;
18. while (count < LARGE_NUMBER) {
19. count++;
20. }
21. }

23. // Asynchronous processing of operation tasks
24. private computeTaskAsync(): void {
25. setTimeout(() => { // SetTimeout is used here to realize asynchronous delayed operation.
26. this.computeTask();
27. }, DELAYED_TIME);
28. }
29. }
```

[ColdStartSpeedOptimization.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ColdStartSpeedOptimization.ets#L17-L57)

重新编译并运行程序，录制Launch过程。优化后，UI Ability OnForeground阶段的耗时显著缩短，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/a8dyabzMTWyhFkjhtsQbaA/zh-cn_image_0000002229450977.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=9BF2C8F6C059DE1D222800805C733A12CFC8BD1ABCB177C08519A6137D715834 "点击放大")

**查看首帧卡顿**

为了识别首帧是否卡顿，可以先查看Launch的Frame泳道。应用的首帧渲染提交在First Frame - App Phase阶段，APP侧的这一帧表示应用渲染的首帧。如下图所示，此处首帧为36号帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/nPpy6H4uSwWK7ZvPgRZjOQ/zh-cn_image_0000002229336561.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=09F1F158DAFA2381DDF966B07DA05533AA64053A362AAD85F39E452C457B8ADC "点击放大")

如上所示36号帧被标记为了红色，表示首帧出现了卡顿。鼠标左键36号帧，可以看到它的期望提交渲染时间为左边白色竖线区域所示，这里出现了比较严重的延时。发现问题后，开发者可以参考前面讲到的示例进行问题定位和优化。

## 提升应用冷启动速度

本文将通过公共类优化的方法，包括[非冷启动必需的服务或模块延迟加载](bpta-application-cold-start-optimization.md#section1351981113010)、[减少主线程非UI耗时操作](bpta-application-cold-start-optimization.md#section17543719239)和[网络请求提前发送](bpta-application-cold-start-optimization.md#section199911250658)，以及结合应用启动的几个阶段分别介绍提升应用冷启动速度的相关方法。

### 非冷启动必需的服务或模块延迟加载

应用在启动前加载过多不必要启动项，同时这些启动项在主线程串行执行，该阶段耗时为450ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/lUx2Yo7ESUKdfiljOjJCBw/zh-cn_image_0000002229451033.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=AC4FEDA0D5D01E706354F0592A14EDB0AC14C55DF0062ED9B99561AFD3563B22 "点击放大")

应用冷启动过程中，加载不必要的启动项会增加冷启动时间。建议延后加载或并行处理，具体可以参考[延迟加载Lazy-Import使用指导](bpta-arkts-high-performance.md#section12861143418213)。

### 减少主线程非UI耗时操作

在应用启动流程中，主要聚焦在执行UI相关操作中，为了更快的显示首页内容，不建议在主线程中执行非UI相关的耗时操作，建议通过异步任务进行异步处理或放到其他子线程中执行，线程并发方案详细请参见[TaskPool和Worker的对比实践](bpta-comparative_practice_of_taskpool_and_worker.md)。

在冷启动过程中如果存在图片下载、网络请求前置数据、数据反序列化等非UI操作，开发者可以根据实际情况移至子线程中进行，详细请参见[应用并发设计](bpta-app-concurrency-design.md)。

### 网络请求提前发送

当前大多数应用的首页内容需从网络获取，发送网络请求的时机显得尤为重要。应用发送网络请求后等待网络数据的返回，网络请求的这段时间应用可以继续执行启动流程，直到网络数据返回后进行解析，反序列化之后就可以加载首页数据，因此网络请求的发起时机越早，整个冷启动的完成时延阶段越短。

将网络请求及初始化流程放置在AbilityStage/UIAbility的onCreate()生命周期中。仅执行网络相关预处理。等待网络请求发送后继续执行首页数据准备和UI操作。在服务端处理相同的情况下，应用可以更早获取网络数据并行展示。

**图2** 应用首页框架加载时进行网络数据请求

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/QWw7H_gxTxOMPEZrpBm5BQ/zh-cn_image_0000002420612214.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=0E8F78922312DCEB8A19206C4BA3E380363BD437F98A49FB964DA9FEEEBD0D2A "点击放大")

将网络请求提前至AbilityStage/UIAbility的onCreate()生命周期回调函数中。这可以将首刷或二刷时间提前，减少用户等待时间。为了体现性能收益，将网络请求放到了更早的AbilityStage的onCreate()生命周期回调中。

**图3** 网络请求提前至AbilityStage的onCreate()生命周期回调中

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ZrG0ATTRSsWwqmhzlwiGow/zh-cn_image_0000002420772730.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=C3A3AE6138FA9D33A66572EBA7267C6AA9985E747E156CBFAC7B6B92C9CD38F5 "点击放大")

【优化前】：在首页根组件的onAppear()回调中发起网络请求。

```
1. // entry/src/main/ets/pages/Index.ets
2. import { httpRequest } from '../utils/NetRequest';

4. import { number } from '../utils/Calculator';

6. AppStorage.link('netData');
7. PersistentStorage.persistProp('netData', undefined);

9. @Entry
10. @Component
11. struct Index {
12. // In order to reflect the performance benefits, refer to the execution result number of the time-consuming function.
13. @State message: string = 'Hello World' + number;
14. @StorageLink('netData') netData: PixelMap | undefined = undefined;

16. build() {
17. Column() {
18. Text(this.message)
19. .fontSize(32)
20. Image(this.netData)
21. .objectFit(ImageFit.Contain)
22. .width('50%')
23. .height('50%')
24. }
25. .width('100%')
26. .height('100%')
27. .justifyContent(FlexAlign.Center)
28. .onAppear(() => {
29. // Send a network request
30. httpRequest();
31. })
32. }
33. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/Index.ets#L17-L49)

```
1. // NetRequest.ets
2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
3. import { http } from '@kit.NetworkKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { image } from '@kit.ImageKit';
6. // Download picture resources from the Internet through the http request method
7. export function httpRequest(): void {
8. hiTraceMeter.startTrace('Http Request', 1);
9. http.createHttp()
10. // The actual development needs to "https://www.example1.com/POST?e=f&g=h"replaced with the real website address to visit
11. .request('https://www.example1.com/POST?e=f&g=h',
12. (error: BusinessError, data: http.HttpResponse) => {
13. if (error) {
14. // The follow-up logic is not executed when the download fails.
15. return;
16. }
17. // Processing the data returned by network requests
18. transcodePixelMap(data);
19. }
20. )
21. }

23. // Use createPixelMap to replace pictures of ArrayBuffer types with PixelMap types.
24. function transcodePixelMap(data: http.HttpResponse): void {
25. if (http.ResponseCode.OK === data.responseCode) {
26. const imageData: ArrayBuffer = data.result as ArrayBuffer;
27. // Create a picture source instance through ArrayBuffer
28. const imageSource: image.ImageSource = image.createImageSource(imageData);
29. const options: image.InitializationOptions = {
30. 'alphaType': 0, // Transparency
31. 'editable': false, // Is it editable?
32. 'pixelFormat': 3, // Pixel format
33. 'scaleMode': 1, // Abbreviation
34. 'size': { height: 100, width: 100 }
35. }; // Create the size of the picture
36. // Create PixelMap through properties
37. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
38. AppStorage.set('netData', pixelMap);
39. hiTraceMeter.finishTrace('Http Request', 1);
40. });
41. }
42. }
```

[NetRequest.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/utils/NetRequest.ets#L2-L45)

```
1. // Calculator.ets
2. const LARGE_NUMBER: number = 100000000;

4. function computeTask(): number {
5. let count: number = 0;
6. while (count < LARGE_NUMBER) {
7. count++;
8. }
9. return count;
10. }

12. export let number = computeTask();
```

[Calculator.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/utils/Calculator.ets#L2-L13)

【优化后】

1. 在NetRequest.ets中进行网络请求以及数据处理。

   ```
   1. // NetRequest.ets
   2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
   3. import { http } from '@kit.NetworkKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { image } from '@kit.ImageKit';
   6. // Download picture resources from the Internet through the http request method
   7. export function httpRequest(): void {
   8. hiTraceMeter.startTrace('Http Request', 1);
   9. http.createHttp()
   10. // The actual development needs to "https://www.example1.com/POST?e=f&g=h"replaced with the real website address to visit
   11. .request('https://www.example1.com/POST?e=f&g=h',
   12. (error: BusinessError, data: http.HttpResponse) => {
   13. if (error) {
   14. // The follow-up logic is not executed when the download fails.
   15. return;
   16. }
   17. // Processing the data returned by network requests
   18. transcodePixelMap(data);
   19. }
   20. )
   21. }

   23. // Use createPixelMap to replace pictures of ArrayBuffer types with PixelMap types.
   24. function transcodePixelMap(data: http.HttpResponse): void {
   25. if (http.ResponseCode.OK === data.responseCode) {
   26. const imageData: ArrayBuffer = data.result as ArrayBuffer;
   27. // Create a picture source instance through ArrayBuffer
   28. const imageSource: image.ImageSource = image.createImageSource(imageData);
   29. const options: image.InitializationOptions = {
   30. 'alphaType': 0, // Transparency
   31. 'editable': false, // Is it editable?
   32. 'pixelFormat': 3, // Pixel format
   33. 'scaleMode': 1, // Abbreviation
   34. 'size': { height: 100, width: 100 }
   35. }; // Create the size of the picture
   36. // Create PixelMap through properties
   37. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
   38. AppStorage.set('netData', pixelMap);
   39. hiTraceMeter.finishTrace('Http Request', 1);
   40. });
   41. }
   42. }
   ```

   [NetRequest.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/utils/NetRequest.ets#L3-L44)
2. 在AbilityStage的onCreate()生命周期回调中发起网络请求。

   ```
   1. // MyAbilityStage.ets
   2. import { AbilityStage, Want } from '@kit.AbilityKit';
   3. import { httpRequest } from '../utils/NetRequest';
   4. export default class MyAbilityStage extends AbilityStage {
   5. onCreate(): void {
   6. // Send a network request
   7. httpRequest();
   8. }

   10. onAcceptWant(want: Want): string {
   11. // Triggered in specified mode only.
   12. return 'MyAbilityStage';
   13. }
   14. }
   ```

   [MyAbilityStage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/entryability/MyAbilityStage.ets#L17-L30)
3. 在首页 Index.ets 中展示请求获取的图片。

   ```
   1. // Index.ets
   2. import { number } from '../utils/Calculator';

   4. AppStorage.link('netData');
   5. PersistentStorage.persistProp('netData', undefined);

   7. @Entry
   8. @Component
   9. struct Index {
   10. @State message: string = 'Hello World' + number; // In order to reflect the performance benefits, refer to the execution result number of the time-consuming function.
   11. @StorageLink('netData') netData: PixelMap | undefined = undefined;
   12. build() {
   13. Row() {
   14. Image(this.netData)
   15. .objectFit(ImageFit.Contain)
   16. .width('50%')
   17. .height('50%')
   18. }
   19. .onDisAppear(() => {
   20. AppStorage.set('netData', undefined);
   21. })
   22. .height('100%')
   23. .width('100%')
   24. }
   25. }
   ```

   [NewIndex.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/NewIndex.ets#L17-L41)

使用Launch分析工具，对比优化前后启动性能。分析阶段从启动Ability（即H:void OHOS::AppExecFwk::MainThread::HandleLaunchAbility的开始点）到应用接收到网络数据返回后的首帧刷新（即H:ReceiveVsync dataCount:24Bytes now:timestamp expectedEnd:timestamp vsyncId:int的开始点）。

**图4** 优化网络请求时机前   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/AMByA1q8RNm7-jYR7FjaaA/zh-cn_image_0000002194010676.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=2F225AE7851869BD980B3FB8E9359D4DA0F513D6D8D67BCF217DC3B8629B44D4 "点击放大")

**图5** 优化网络请求时机后   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/mb-xvSWFTH2DXToFG9u0Kg/zh-cn_image_0000002229450941.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=3805B267FF1AA866F74861AB7107FED9BA80ACA97849E09752407B98C24B171E "点击放大")

对比数据如下：

| 方案 | 阶段时长(毫秒) |
| --- | --- |
| 优化网络请求时机前 | 1700 |
| 优化网络请求时机后 | 885.3 |

因此，可以通过提前网络请求的方式减少应用冷启动耗时。

### 缩短应用进程创建和初始化阶段耗时

应用进程创建和初始化阶段包括系统完成应用进程的创建及初始化，以及启动页图标（startWindowIcon）的解码。建议使用不超过256×256分辨率的图标，以减少图片解码时延，提升体验。

说明

建议开发者优先使用[Code Linter扫描工具](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/start-window-icon-check](../harmonyos-guides/ide-start-window-icon-check.md)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

**设置合适分辨率的startWindowIcon**

如果启动页图标分辨率过大，解码耗时会影响应用的启动速度。建议启动页图标分辨率不超过256像素×256像素，如下所示。

```
1. {
2. // ...
3. "abilities": [
4. {
5. "name": "EntryAbility",
6. "srcEntry": "./ets/entryability/EntryAbility.ets",
7. "description": "$string:EntryAbility_desc",
8. "icon": "$media:layered_image",
9. "label": "$string:EntryAbility_label",
10. "startWindowIcon": "$media:startIcon",
11. "startWindowBackground": "$color:start_window_background",
12. // ...
13. }
14. ]
15. }
16. }
```

[module.json5](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/module.json5#L2-L55)

下面使用Launch分析对比优化前的startWindowIcon（4096像素\\*4096像素）及优化后的startWindowIcon（144像素\\*144像素）的启动性能。分析阶段的起点为Process Creating，阶段终点为First Frame - Render Phase，优化前后的启动耗时如下图：

**图6** 优化前使用4096px-4096px启动页图标应用启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/vu4JcuuCTbyBxgTBZSrkOA/zh-cn_image_0000002229451013.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=714F1D8327D6CB31B407A6C560381660F05567DA7186FD4DB76F7CECF19C2BD0)

**图7** 优化后使用144px-144px启动页图标应用启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/PaXeLLlZTTC7odI0DHVedw/zh-cn_image_0000002229450965.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=EB52CE2C7DCB728C39A081A44B5A2CFD05147F2C9CCFB65FE297035E174C25AF)

优化后，应用启动时长缩短了37.2ms，设置合适的startWindowIcon分辨率能有效减少应用进程创建和初始化阶段的耗时。

### 缩短Application和Ability初始化阶段耗时

Application和Ability初始化包括资源加载、虚拟机创建、相关对象的创建与初始化及依赖模块的加载。

主要耗时点在资源加载阶段，分为以下几个步骤。

1. 文件加载：查找并解析所有的文件到模块中记录。
2. 依赖模块解析（实例化）：分配内存空间来存放模块所有导出的变量，此时内存中并没有分配变量的值。
3. 文件执行：运行.ets文件，将内存中之前未分配值的变量赋为真实的值。

本章节将详细说明这三个阶段的具体优化方法。

**减少import的模块**

应用程序在执行代码前，必须找到并加载所有导入的模块。每个加载的第三方框架或模块都会增加启动时间，具体耗时取决于模块的数量和大小。建议开发者优先使用系统提供的模块，并按需加载，以缩短应用程序的启动时间。

```
1. // Optimize modules that reduce import
2. /*import { ConfigurationConstant, contextConstant, wantConstant } from '@kit.AbilityKit';
3. import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
4. import { distributedAccount, osAccount } from '@kit.BasicServicesKit';
5. import { Configuration } from '@kit.ArkUI';
6. import { atomicService } from '@kit.ScenarioFusionKit';
7. import { sim } from '@kit.TelephonyKit';*/

10. import { UIAbility } from '@kit.AbilityKit';

13. export default class EntryAbility extends UIAbility {
14. // ...
15. }
```

[ReduceImport.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ReduceImport.ets#L17-L31)

下面使用Launch分析，对优化import的模块前（模块数量15个）及优化import的模块后（移除不必要的模块剩余5个）的启动性能进行对比分析。分析的trace点为H:SourceTextModule::Evaluate，优化前后的启动耗时如下图：

**图8** 优化前import 15个模块   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/WYkVJ0hOQoOtMDV5DZgi2w/zh-cn_image_0000002229336481.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=B6C5B7E3175386982ECA7C731D5DBDF44A0A256C9E079A77476D1D8EF240B8CB "点击放大")

**图9** 优化后import 5个模块   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/XBV6KVwBT-WaZK0VbiA7-g/zh-cn_image_0000002229336453.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=3A1745A2BC5A459E9D108A7CEFBCBC8CFB924A8A997101CAD16FD4E241B11BBD "点击放大")

对比数据如下：

| 方案 | 阶段时长(微秒) |
| --- | --- |
| 减少import的模块前 | 6239.5 |
| 减少import的模块后 | 119.7 |

减少不必要的模块导入可以缩短应用的冷启动时间。如果某些必要模块的导入较为耗时，建议采用动态导入方式。具体方法可参考[动态加载](../harmonyos-guides/arkts-dynamic-import.md)。

减少使用嵌套的export \*和import \*方式。

* 减少使用嵌套的export \*方式进行全量导出

  在应用冷启动过程中，`HandleLaunchAbility` 会执行冷启动相关的 `.ets` 文件。所有被主页面import的 `.ets` 文件均会被执行，包括数据结构、变量和全局函数的初始化。首页所需的变量和函数可能来自其他 `.ets` 文件，并通过export形式提供给首页使用。详细信息请参见[减少同文件大量export \*导出方式](bpta-arkts-high-performance.md#section1218510102815)。

  使用Launch分析，对比优化前（嵌套8层export \*）和优化后（直接从目标文件中import）的启动性能。分析阶段从开始加载abc文件（H:JSPandaFileExecutor::ExecuteFromAbcFile）到abc文件加载完成。

  **图10** （优化前）存在8层嵌套export \*   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/EVRyhrjASD6i6O8Aq3rpBA/zh-cn_image_0000002193851128.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=988C5B3BD0D1982366063044F24136E930A53A1DDEA2A54821A645F4987534E7 "点击放大")

  **图11** （优化后）不存在嵌套export \*，从目标文件中直接import   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ajwGWYXWR5-whUBugm6w7w/zh-cn_image_0000002194010744.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=0F2F99B6338E09657F1237260FF2E5EA337BA97BA29769AE85F0BCA290F28A42 "点击放大")

  对比数据如下：

  | 方案 | 阶段时长(微秒) |
  | --- | --- |
  | （优化前）存在8层嵌套export \* | 492.6 |
  | （优化后）不存在嵌套export \*，从目标文件中直接import | 388.7 |

  可见阶段时长已缩短。减少多层文件嵌套导出可以提升应用冷启动速度。
* 减少import \*的方式全量引用

  应用程序加载时，通常将相同类型的变量或函数放在同一个工具类文件中。使用时，通过import方式引入对应的模块。当工具类中存在较多暴露的函数或变量时，推荐按需引用具体的变量，以减少 `.ets` 文件的执行耗时和文件中所有export变量的初始化过程。详情请参见[减少同文件大量export \*导出方式](bpta-arkts-high-performance.md#section1218510102815)。

  对优化前（使用 `import \* as nm` 全量引用2000条数据）和优化后（使用import { One }按需引用）的启动性能进行对比分析。分析阶段从 `H:void OHOS::AppExecFwk::MainThread::HandleLaunchAbility(const std::shared\_ptr<AbilityLocalRecord> &)` 的开始点到结束点。

  **图12** 优化前，使用import \* as nm全量引用2000条数据   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/1K7PvojvQd-1-yvs34g0Ew/zh-cn_image_0000002229450969.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=6C09BCA279AB3ACDEF196399A72565D44BCBB416D98326D27A5373AD5FABBD57 "点击放大")

  **图13** 优化后，使用import { One }按需引用   
  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/rHsXniguS7OhZiYdWg1iWg/zh-cn_image_0000002229450953.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=31944AB28E506491360F70CBBD0684BE49848B3105EC21FB24DF4E752508DB7A "点击放大")

  优化前后的对比数据如下：

  | 方案 | 阶段时长(毫秒) |
  | --- | --- |
  | （优化前）使用import \* as nm全量引用 | 16.7 |
  | （优化后）使用import { One }按需引用 | 7.1 |

  可见阶段的时长已减少。使用按需引用的方式，可以进一步缩短应用冷启动的完成时间。

  说明

  此优化方案仅可将冷启动阶段耗时缩短，但是可能导致其他场景耗时增长，即变量初始化过程从冷启动阶段分摊至其它使用阶段，例：当二级页面使用到Numbers.ets中Two变量，此方案会使二级页面跳转过程对比优化前耗时更长。

**合理拆分导出文件，减少冗余文件执行**

应用程序加载模块后，需执行应用侧的.ets文件，进行初始化并执行全局变量和函数的初始化。文件可分类为冷启动强相关文件（如首页展示界面及组件相关文件）和非冷启动强相关文件（如跳转后二级页面）。冷启动过程中仅执行冷启动强相关文件，以缩短应用启动时间。

【场景示例】

应用包含两个页面：首页Index和二级页面SecondPage。首页展示HAR包中MainPage.ets文件的Text组件，该文件中没有耗时操作。点击首页中的Text组件时，跳转至二级页面。二级页面引用HAR包中的SubPage.ets文件，该文件包含全局函数的耗时操作，这些操作在模块加载时执行。

HAR包中的导出文件Index.ets同时导出了MainPage.ets和SubPage.ets两个文件。当首页直接使用 “import { MainPage } from 'library/Index'” 的方式进行导入时，会导致应用在冷启动过程中执行非冷启动强相关文件SubPage.ets，增加了冷启动时间。

**图14** 优化前，加载模块时执行了非冷启动相关文件 SubPage.ets。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/0y4SJ16iS0ief23_zSm5LQ/zh-cn_image_0000002454292713.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=9F2CABC5ADC7B7E48C6D7E749769704D8A6314B1B793E0D4D7900F62E261DA58 "点击放大")

以下为示例代码：

```
1. // entry/src/main/ets/pages/Index.ets
2. import { MainPage } from 'library/Index'; // Unrecommended usage: Direct import of subPage.ets files related to cold start non-strong
3. @Component
4. export struct Index{
5. @Provide pathStack: NavPathStack = new NavPathStack();
6. build() {
7. Navigation(this.pathStack) {
8. Row() {
9. // Refer to the custom components of HAR
10. MainPage()
11. }
12. }
13. }
14. }
```

[NotRecommendDemo.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/NotRecommendDemo.ets#L17-L30)

```
1. // library/src/main/ets/components/mainpage/MainPage.ets
2. @Component
3. export struct MainPage {
4. @Consume pathStack: NavPathStack;
5. @State message: string = 'HAR MainPage';

7. build() {
8. Row() {
9. Text(this.message)
10. .fontSize(32)
11. .fontWeight(FontWeight.Bold)
12. }.onClick(() => {
13. this.pathStack.pushPath({ name: 'SecondPage' });
14. })
15. }
16. }
```

[MainPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/src/main/ets/components/mainpage/MainPage.ets#L17-L32)

```
1. // entry/src/main/ets/pages/SecondPage.ets
2. import { SubPage } from 'library/Index';
3. @Builder
4. export function SecondPageBuilder() {
5. SecondPage()
6. }
7. @Entry
8. @Component
9. struct SecondPage {
10. pathStack: NavPathStack = new NavPathStack();
11. build() {
12. NavDestination() {
13. Row() {
14. // Refer to the custom components of HAR
15. SubPage()
16. }
17. .height('100%')
18. }
19. .onReady((context: NavDestinationContext) => {
20. this.pathStack = context.pathStack;
21. })
22. }
23. }
```

[SecondPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/SecondPage.ets#L17-L39)

```
1. // library/src/main/ets/components/mainpage/SubPage.ets
2. // Global time-consuming functions in SubPage
3. const LARGE_NUMBER: number = 10000000;

5. function computeTask(): number {
6. let count: number = 0;
7. while (count < LARGE_NUMBER) {
8. count++;
9. }
10. return count;
11. }

13. computeTask();
14. // ...
```

[SubPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/src/main/ets/components/mainpage/SubPage.ets#L2-L15)

```
1. export { MainPage } from './src/main/ets/components/mainpage/MainPage'; // Cold start strong related files
2. export { SubPage } from './src/main/ets/components/mainpage/SubPage'; // Non-cold start strong related files
```

[Index.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/Index.ets#L17-L18)

【优化方案一】

将HAR包的导出文件Index.ets进行拆分，IndexAppStart.ets文件仅导出首页相关文件，即MainPage.ets。IndexOthers.ets文件导出非首页相关文件，即SubPage.ets。

优点：使用此种方案优化后可以将冷启动阶段（加载首页文件）与非冷启动阶段（加载非首页文件）需要执行的.ets文件进行完全拆分，类比其他需优化的场景也可以使用本方案进行拆分。

缺点：拆分后，需确保IndexAppStart.ets中的导出文件不引用IndexOthers.ets中的导出文件。

**图15** 优化方案一，拆分HAR导出文件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/4oYZixJNTxSyqO4qkSlfrw/zh-cn_image_0000002454173657.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=633FBB163BA37D3236FE0F94072BE6BCAF246DA501AEBA578996B3DE1445281C "点击放大")

示例代码如下：

1. 将HAR包的导出文件Index.ets进行拆分，IndexAppStart.ets文件仅导出首页相关文件，IndexOthers.ets文件导出非首页相关文件。

   ```
   1. // library/IndexAppStart.ets
   2. export { MainPage } from './src/main/ets/components/mainpage/MainPage';
   ```

   [IndexAppStart.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/IndexAppStart.ets#L2-L3)

   ```
   1. // library/IndexOthers.ets
   2. export { SubPage } from './src/main/ets/components/mainpage/SubPage';
   ```

   [IndexOthers.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/library/IndexOthers.ets#L2-L3)
2. 首页Index从IndexAppStart.ets导入MainPage。

   ```
   1. // Index.ets
   2. import { MainPage } from 'library/IndexAppStart';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @Provide pathStack: NavPathStack = new NavPathStack();

   9. build() {
   10. Navigation(this.pathStack) {
   11. Row() {
   12. // Refer to the custom components of HAR
   13. MainPage()
   14. }
   15. }
   16. .height('100%')
   17. .width('100%')
   18. }
   19. }
   ```

   [ImportMainPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ImportMainPage.ets#L17-L35)
3. 跳转后的页面SecondPage从IndexOthers.ets导入SubPage。

   ```
   1. // SecondPage.ets
   2. import { SubPage } from 'library/IndexOthers';

   4. @Builder
   5. export function SecondPageBuilder() {
   6. SecondPage()
   7. }

   9. @Entry
   10. @Component
   11. struct SecondPage {
   12. pathStack: NavPathStack = new NavPathStack();

   14. build() {
   15. NavDestination() {
   16. Row() {
   17. // Refer to the custom components of HAR
   18. SubPage()
   19. }
   20. .height('100%')
   21. }
   22. .onReady((context: NavDestinationContext) => {
   23. this.pathStack = context.pathStack;
   24. })
   25. }
   26. }
   ```

   [ImportSubPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ImportSubPage.ets#L17-L42)

【优化方案二】

在首页的Index.ets文件中导入MainPage.ets时，使用全路径。

优点：无需新增文件即可汇总导出所有冷启阶段的文件。

缺点：引用时需对冷启阶段的所有文件路径进行展开，增加开发和维护成本。

**图16** 优化方案二，首页导入冷启动文件时使用全路径展开

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/sVwZnPY7T_a856eqXnSrOg/zh-cn_image_0000002420614820.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=F9EB50DDD39DC667FBD208B43B8830018598F3BAA05399ECECF363B80FF24B14 "点击放大")

示例代码如下：

```
1. // Index.ets
2. import { MainPage } from 'library/IndexAppStart';

4. @Entry
5. @Component
6. struct Index {
7. @Provide pathStack: NavPathStack = new NavPathStack();

9. build() {
10. Navigation(this.pathStack) {
11. Row() {
12. // Refer to the custom components of HAR
13. MainPage()
14. }
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

[ImportMainPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ImportMainPage.ets#L17-L35)

说明

1. 上述两种优化方案假设MainPage中不存在对SubPage的import。

2. 当MainPage中存在对SubPage的直接import时，需使用[动态import](../harmonyos-guides/arkts-dynamic-import.md)方法来进行优化。

3. 开发者可自行根据优化方案的优缺点权衡选择合适的优化方案。

使用Launch分析优化前后启动性能。阶段起点为UI Ability Launching，终点为应用首帧即First Frame - App Phase。

**图17** 优化前：加载模块时执行了非冷启动相关文件   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/VUjXoYINSy6irXrplmkH9A/zh-cn_image_0000002229336505.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=7BECAD0B8A1D7E933A209B3F3D7213FF289141CC1907A73EA8F7DB88C055AEB2 "点击放大")

**图18** 优化方案一：拆分HAR导出文件   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/TF6Lf_pHQKi2Tw5wUwGNIA/zh-cn_image_0000002193851072.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=E6F33C36A5CA9D8A0709CA9D3425D2575154D010C5E66D7E00A650E9A1B5298D "点击放大")

**图19** 优化方案二：导入冷启动文件时全路径展开   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/DqwB02NbQh-AWOqjDxIjEg/zh-cn_image_0000002194010672.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=14F4C9B2A1270C3E8BCB0CA1AB17CE62F9761C86A7E14E328C68A36EDD21C524 "点击放大")

优化前后的对比数据如下：

| 方案 | 阶段时长(毫秒) |
| --- | --- |
| 优化前 | 140.1 |
| 优化方案一（拆分HAR导出文件） | 62.9 |
| 优化方案二（导入冷启动文件时全路径展开） | 61.3 |

可见阶段的时长已减少。为减少应用冷启动时.ets文件的执行耗时，可以采取以下措施：拆分HAR包导出的Index.ets文件，或在导入冷启动文件时展开完整路径，从而提升应用冷启动速度。

**减少多个HAP/HSP对相同HAR的引用**

在应用开发的过程中，可以使用[HSP](../harmonyos-guides/in-app-hsp.md)或[HAR](../harmonyos-guides/har-package.md)的共享包方式，整合同类模块，实现多个模块或工程间共享ArkUI组件、资源等相关代码。同时，避免多个HAP/HSP引用相同HAR。详细信息请参见[多HAP/HSP引用相同HAR包的影响](bpta-modular-design.md#section9492615385)。

**优化加载HSP时间过长**

对于单窗口应用的APP工程，其仅包含一个Entry类型的HAP。如果划分的模块没有按需加载的需求，建议业务组件和公共组件采用HAR的打包方式。最终构建应用HAP包时，这些被依赖的HAR将被编译进HAP包中。HSP采用动态加载，在启动过程中会将依赖的HSP加载进来，增加额外的IO与运行耗时。在单HAP场景下，如果使用多模块的话。推荐使用多HAR，不推荐使用HSP。

以下为示例代码：

```
1. import { add } from 'hsp1';
2. import { add2 } from 'hsp2';
3. import { add3 } from 'hsp3';
4. import { add4 } from 'hsp4';
5. import { add5 } from 'hsp5';
6. import { add6 } from 'hsp6';
7. import { add7 } from 'hsp7';
8. import { add8 } from 'hsp8';
9. import { add9 } from 'hsp9';
10. import { add10 } from 'hsp10';
11. import { add11 } from 'hsp11';
12. import { add12 } from 'hsp12';
13. import { add13 } from 'hsp13';
14. import { add14 } from 'hsp14';
15. import { add15 } from 'hsp15';
16. import { add16 } from 'hsp16';
17. import { add17 } from 'hsp17';
18. import { add18 } from 'hsp18';
19. import { add19 } from 'hsp19';
20. import { add20 } from 'hsp20';
```

下面使用Launch分析，对比HAP与20个HSP混合打包以及将20个HSP包设计成HAR包的启动性能。

**图20** HAP+20个HSP混合打包   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/cXrzW6WnQlCMQe29pi5oJA/zh-cn_image_0000002229451061.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=144FA7DE2F3D3A25E6C4E30502C2F912CA86D1FEC01D732F80F27475CD7CDC06 "点击放大")

**图21** 将20个HSP包设计成HAR包   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/7xxv5V5xT26YOoIZNjBZaw/zh-cn_image_0000002229450981.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=113B145ECDAA4EFFFF21F93B91363BAA31E78FAF75543CE33C2C148B9F823CE6 "点击放大")

对比数据如下：

| 方案 | 阶段时长(微秒) |
| --- | --- |
| HAP+20个HSP混合打包 | 34643.7 |
| 将20个HSP包设计成HAR包 | 36.4 |

在单HAP场景下，如果需要使用多模块，建议使用多HAR，不建议使用HSP。

### 缩短AbilityStage生命周期阶段耗时

AbilityStage生命周期阶段执行相应的生命周期回调。

**避免在AbilityStage生命周期回调接口进行耗时操作**

在应用启动流程中，系统会执行 AbilityStage 的生命周期回调函数。不建议在这些回调函数中执行耗时操作，例如 onCreate。建议将耗时操作通过异步任务延迟处理或放到其他线程执行。关于线程并发方案，可以参考 [TaskPool和Worker的对比实践](bpta-comparative_practice_of_taskpool_and_worker.md)。在这些生命周期回调中，推荐仅执行必要的操作。关于 AbilityStage，可以参考 [AbilityStage组件管理器](../harmonyos-guides/abilitystage.md)，以下为示例代码：

```
1. const LARGE_NUMBER: number = 100000000;
2. const DELAYED_TIME: number = 1000;

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. aboutToAppear(): void {
10. console.log('aboutToAppear');
11. this.computeTaskAsync();
12. }

14. // ...

16. computeTask(): void {
17. let count: number = 0;
18. while (count < LARGE_NUMBER) {
19. count++;
20. }
21. }

23. // Asynchronous processing of operation tasks
24. private computeTaskAsync(): void {
25. setTimeout(() => { // SetTimeout is used here to realize asynchronous delayed operation.
26. this.computeTask();
27. }, DELAYED_TIME);
28. }
29. }
```

[ColdStartSpeedOptimization.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ColdStartSpeedOptimization.ets#L17-L57)

使用Launch分析，对比优化前同步执行耗时操作和优化后异步执行耗时操作的启动性能。分析范围从Process Creating到First Frame - Render Phase，优化前后的启动耗时如下图所示。

**图22** 优化前同步执行操作（computeTask），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/nYbLDZs_Q16tX3rUaqe5hg/zh-cn_image_0000002229336541.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=7FE66F73609509835D5D50D339FD386C653D7A6164DE5C2D5E51549C2B0F3353)

**图23** 优化后异步执行操作（computeTaskAsync），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/QeqVDTV1SX25n4vQPub6fA/zh-cn_image_0000002229450973.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=CA03DEE3A2A690E5945279FAC92E5A992DB0554A7BE7AF1B203826A9E68069DB)

使用异步后，应用冷启动时间从2.2秒减少到220.9毫秒，速度提升显著。

### 缩短Ability生命周期阶段耗时

Ability生命周期阶段执行相应的生命周期回调。

**避免在Ability生命周期回调接口进行耗时操作**

在应用启动流程中，系统会执行Ability的生命周期回调函数。因此，不建议在这些回调函数中执行耗时操作，建议通过异步任务延迟处理或者放到其他线程执行。线程并发方案可以参考 [TaskPool和Worker的对比实践](bpta-comparative_practice_of_taskpool_and_worker.md)。

在这些生命周期回调里，推荐开发者只做必要的操作，下面以UIAbility为例进行说明。比如在生命周期回调函数onCreate、onWindowStageCreate、onForeground等中执行耗时操作都会导致启动缓慢问题，关于UIAbility组件生命周期的详细说明，参见[UIAbility组件生命周期](../harmonyos-guides/uiability-lifecycle.md)。

**图24** UIAbility生命周期状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/fjZhLOJZTGytCavTy14CYA/zh-cn_image_0000002454294977.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=34899CADF5EADEDDF1547951522500FB7EAA628AB1A28C34D06481C8FDF48F97 "点击放大")

下面示例代码在UIAbility的回调函数onCreate()中分别执行了同步和异步操作：

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI'

4. const LARGE_NUMBER: number = 100000000;
5. const DELAYED_TIME: number = 1000;

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
10. // Time-consuming operation
11. // this.computeTask();
12. this.computeTaskAsync(); // Asynchronous tasks
13. }

15. onWindowStageCreate(windowStage: window.WindowStage): void {
16. windowStage.loadContent('pages/Index', (err, data) => {
17. if (err.code) {
18. console.error('Failed to load the content. Cause: ' + JSON.stringify(err) ?? '');
19. return;
20. }
21. console.info('Succeeded in loading the content. Data: ' + JSON.stringify(data) ?? '');
22. });

24. // Time-consuming operation
25. // this.computeTask();
26. // this.computeTaskAsync(); // Asynchronous mission
27. }

29. onForeground(): void {
30. // Time-consuming operation
31. // this.computeTask();
32. // this.computeTaskAsync(); // Asynchronous mission
33. }

35. private computeTask(): void {
36. let count: number = 0;
37. while (count < LARGE_NUMBER) {
38. count++;
39. }
40. }

42. private computeTaskAsync(): void {
43. setTimeout(() => { // SetTimeout is used here to achieve asynchronous delayed operation.
44. this.computeTask();
45. }, DELAYED_TIME);
46. }
47. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/entryability/EntryAbility.ets#L17-L63)

下面使用Launch分析，对比优化前同步执行耗时操作和优化后异步执行耗时操作的启动性能。分析从Process Creating阶段开始，到First Frame - Render Phase阶段结束。优化前后的启动耗时如下图所示。

**图25** 优化前同步执行操作（computeTask），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/PrRVXLyXTEqQeEAsApIn5g/zh-cn_image_0000002193851092.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=6FFDAF5615A9E779B55015718D7FADFEC881ECC44254F444FF2DDEF8F7075751)

**图26** 优化后异步执行操作（computeTaskAsync），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/oQDQ16UHRI6yMiNBV8CGVg/zh-cn_image_0000002194010748.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=F59C8DB10109ACBE49C0DCFC1AE9D481717180C7CF73E5A07BD1B64081BB3BD7)

使用延时异步后，应用冷启动时间显著提升，耗时从2.1秒减少到220毫秒。

### 缩短加载绘制首页阶段耗时

首页加载绘制阶段主要包含加载首页内容、测量布局、刷新组件和绘制。处理页面生命周期时，避免耗时操作，优先创建首页需要显示的组件，使用if分支语句隐藏不需要显示的组件，减少创建过程的耗时。耗时操作建议通过异步任务或放到其他线程执行，线程并发方案可参考 [TaskPool和Worker的对比实践](bpta-comparative_practice_of_taskpool_and_worker.md)。

**自定义组件生命周期回调接口里避免耗时操作**

自定义组件的生命周期变更会调用相应的回调函数，aboutToAppear()函数会在创建自定义组件实例后，页面绘制之前执行，而onPageShow则是在页面进入前台的时候显示，因此避免在这两个回调函数中执行该耗时操作，不阻塞页面绘制。关于自定义组件生命周期的详细说明，参见[页面和自定义组件生命周期](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)。

**图27** 被@Entry装饰的组件（页面）生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/bTq-V9s4RxCdZa1tfZRmhQ/zh-cn_image_0000002420776488.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=FF4FE23452EC0E3097B8D8981EDB06F89DEFEBAEED8E9D5FD80C48FE1A5E4DB1 "点击放大")

在Page的回调函数aboutToAppear()中分别执行同步和异步操作的示例代码如下：

```
1. const LARGE_NUMBER: number = 100000000;
2. const DELAYED_TIME: number = 1000;

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. aboutToAppear(): void {
10. // Time-consuming operation
11. // this.computeTask();
12. this.computeTaskAsync(); // Asynchronous tasks
13. }

15. build() {
16. Row() {
17. Column() {
18. Text(this.message)
19. .fontSize(50)
20. .fontWeight(FontWeight.Bold)
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }

27. private computeTask(): void {
28. let count: number = 0;
29. while (count < LARGE_NUMBER) {
30. count++;
31. }
32. }

34. // Asynchronous processing of computing tasks
35. private computeTaskAsync(): void {
36. setTimeout(() => { // SetTimeout is used here to achieve asynchronous delayed operation.
37. this.computeTask();
38. }, DELAYED_TIME);
39. }
40. }
```

[ComputeTaskAsync.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ComputeTaskAsync.ets#L17-L56)

下面使用Launch分析，对优化前同步执行耗时操作及优化后异步执行耗时操作的启动性能进行对比分析。分析阶段的起点Process Creating，阶段终点为First Frame - Render Phase。

如下图所示，优化前后的启动耗时对比：

**图28** 优化前同步执行操作（computeTask），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/uAYKmhqvQWiIoQ4RtPNMFw/zh-cn_image_0000002229336521.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=61EE184B74F76692D11C54166CBFBD37E189FF493883472B07C2A798A0A96717)

**图29** 优化后异步执行操作（computeTaskAsync），应用冷启动耗时   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/-IEePHtYTNyQbw45bsc6mw/zh-cn_image_0000002229336501.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=C945DA6B76C5E31088F780B950D8391BD69EB1BE6FFF78310FC5BF0359F6A221 "点击放大")

使用异步处理后，应用冷启动时间显著提升，耗时从2.4秒减少到238.3毫秒。

**使用本地存储加载首页数据**

在应用启动流程中，大部分应用的首页数据信息需要等待网络请求返回的数据解析结果，因此可以将首页数据通过应用数据持久化的方式进行本地存储，再次冷启动时优先展示已存储数据，网络请求后再次刷新首页数据。

**图30** 使用本地存储首页数据流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/XR_Jvs6WRwO2mGleFqMWlw/zh-cn_image_0000002420776904.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=66417A21C05C1E8772055A7D1DEC2DE3805FBDA2579701531A4293733BF8D157 "点击放大")

使用本地**存储**优先展示，可减少首帧展示延迟，缩短用户可见白屏时间，提升冷启动体验。

说明

应用需根据自身对于数据的时效性要求，来决定是否使用**本地存储**数据。例如时效性要求为一天时，一天前保存的数据就不适合进行展示，需从网络获取新数据进行展示，并更新本地存储数据。

【场景示例】

应用首页需展示从网站获取的图片信息。在aboutToAppear()中发起网络请求，数据返回并解析后展示在首页。图片信息存储在本地应用沙箱内。再次冷启动时，首先从沙箱获取图片信息，若存在则解析并展示。网络请求返回时，更新图片信息。

以下为关键示例代码：

```
1. // Index.ets
2. import { http } from '@kit.NetworkKit';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
6. import { fileIo, fileIo as fs } from '@kit.CoreFileKit';

8. const PERMISSIONS: Array<Permissions> = [
9. 'ohos.permission.READ_MEDIA',
10. 'ohos.permission.WRITE_MEDIA'
11. ];
12. AppStorage.link('net_picture');
13. PersistentStorage.persistProp('net_picture', '');

15. @Entry
16. @Component
17. struct Index {
18. @State image: PixelMap | undefined = undefined;
19. @State imageBuffer: ArrayBuffer | undefined = undefined; // Picture ArrayBuffer

21. /**
22. * Download picture resources from the Internet through the http request method
23. */
24. async getPicture(): Promise<void> {
25. http.createHttp()
26. .request('https://www.example1.com/POST?e=f&g=h',
27. (error: BusinessError, data: http.HttpResponse) => {
28. if (error) {
29. return;
30. }
31. // Determine whether the resources obtained by the network are of the ArrayBuffer type.
32. if (data.result instanceof ArrayBuffer) {
33. this.imageBuffer = data.result as ArrayBuffer;
34. }
35. this.transcodePixelMap(data);
36. }
37. )
38. }

40. /**
41. * Use createPixelMap to replace pictures of ArrayBuffer type with PixelMap type
42. * @param data：Resources obtained from the network
43. */
44. transcodePixelMap(data: http.HttpResponse): void {
45. if (http.ResponseCode.OK === data.responseCode) {
46. const imageData: ArrayBuffer = data.result as ArrayBuffer;
47. // Create a picture source instance through ArrayBuffer
48. const imageSource: image.ImageSource = image.createImageSource(imageData);
49. const options: image.InitializationOptions = {
50. 'alphaType': 0, // Transparency
51. 'editable': false, // Is it editable?
52. 'pixelFormat': 3, // Pixel format
53. 'scaleMode': 1, // Abbreviation
54. 'size': { height: 100, width: 100 }
55. }; // Create the size of the picture

57. // Create PixelMap through attributes
58. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
59. this.image = pixelMap;
60. setTimeout(() => {
61. if (this.imageBuffer !== undefined) {
62. this.saveImage(this.imageBuffer);
63. }
64. }, 0)
65. });
66. }
67. }

69. async saveImage(buffer: ArrayBuffer | string): Promise<void> {
70. try {
71. const context:common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
72. const filePath: string = context.cacheDir + '/test.jpg';
73. AppStorage.set('net_picture', filePath);
74. const file: fileIo.File = await fs.open(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
75. await fs.write(file.fd, buffer);
76. await fs.close(file.fd);
77. } catch (err) {
78. let error = err as BusinessError;
79. console.error(`onAddForm err, code: ${error.code}, mesage: ${error.message}`);
80. }
81. }

84. async useCachePic(): Promise<void> {
85. if (AppStorage.get('net_picture') !== '') {
86. // Get the ArrayBuffer of the picture
87. const imageSource: image.ImageSource = image.createImageSource(AppStorage.get('net_picture'));
88. const options: image.InitializationOptions = {
89. 'alphaType': 0, // transparency
90. 'editable': false, // Is it editable?
91. 'pixelFormat': 3, // pixel format
92. 'scaleMode': 1, // Abbreviated value
93. 'size': { height: 100, width: 100 }
94. };
95. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
96. this.image = pixelMap;
97. });
98. }
99. }

101. async aboutToAppear(): Promise<void> {
102. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
103. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
104. await atManager.requestPermissionsFromUser(context, PERMISSIONS);
105. this.useCachePic(); // Get data from local storage
106. this.getPicture(); // Obtain data from the network side
107. }

110. build() {
111. Column() {
112. Image(this.image)
113. .objectFit(ImageFit.Contain)
114. .width('50%')
115. .height('50%')
116. }
117. }
118. }
```

[ScenariosExample.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppColdStart/entry/src/main/ets/pages/ScenariosExample.ets#L17-L134)

下面对比优化前后的启动性能。分析阶段从启动Ability开始，到首次解析Pixelmap后的第一个vsync结束。

**图31** 优化前未使用本地存储数据   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Fpgf8HQuS9u5P9gT9fdgzQ/zh-cn_image_0000002229336461.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=2D0F0C2B7DBB3C350B1C888F42B397D31946C2CF696D880DC2D4B282C073B908 "点击放大")

**图32** 优化后使用本地存储数据   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ZV4m2lRpSJaj9Vk0Ui835g/zh-cn_image_0000002194010688.png?HW-CC-KV=V1&HW-CC-Date=20260428T002229Z&HW-CC-Expire=86400&HW-CC-Sign=0BAAEAF0FC731412320BE9BF27F881475C0E2A1187774CB3E19548B2CD92C0EF "点击放大")

对比数据如下：

| 方案 | 阶段时长(毫秒) |
| --- | --- |
| （优化前）未使用本地存储 | 641.8 |
| （优化后）使用本地存储 | 68.9 |

使用本地存储后，应用冷启动时从Ability启动到图片显示的阶段耗时明显减少。

针对应用冷启动过程中网络请求耗时久的问题，提供了一个三方库供开发者使用，优化方式是首页内容复用，先使用本地缓存的数据。三方库链接：[首页数据缓存](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fdatacache)。加速应用冷启动的使用方法可参考：[基于DataCache提升应用冷启动速度](https://gitcode.com/harmonyos_samples/DataCache)。

**优化首页显示速度**

启动过程从用户点击应用入口到首页数据显示在屏幕上，这是对用户点击事件响应的过程。开发者可以通过UI优化、并发优化、代码逻辑优化及IPC通信优化等方法来提升首页的响应速度，具体可参考：[点击响应时延分析](bpta-click-to-click-response-optimization.md)。

## 总结

本文介绍了应用冷启动的流程，如何识别和分析冷启动缓慢问题，以及针对冷启动各阶段的注意事项和优化方法。

* 非冷启动所需的服务或模块可以延迟加载。
* 将网络请求提前至AbilityStage/UIAbility的onCreate()生命周期回调函数中，提前首刷或二刷时间，减少用户等待时间。
* 建议将启动页图标startWindowIcon的分辨率设置为不超过256px\*256px。
* 在AbilityStage、UIAbility和自定义组件的生命周期回调函数中，不建议直接执行复杂的计算任务、同步文件读写等耗时任务。建议通过异步任务或在其他线程中处理。
* 按需导入模块，移除初始化阶段不必要的模块导入，动态加载耗时的模块。
* 减少使用嵌套的export \*全量导出和import \*全量引用。
* 拆分HAR包导出文件或导入冷启动相关文件时，使用全路径，减少应用冷启动的.ets文件执行耗时。
* 避免多个HAP/HSP对相同HAR的引用。
* 在单HAP场景下，建议模块使用多HAR，而不推荐使用HSP。
* 建议通过使用合理的布局结构和懒加载等UI优化方法来减少首帧绘制时间。
* 建议使用本地存储首页数据，以减少首帧展示完成的时延，并减少用户可见的白屏或白块时间。

希望通过本文的学习，开发者可以了解和识别应用启动耗时的问题，有助于开发者提升应用冷启动速度，提升用户体验。
