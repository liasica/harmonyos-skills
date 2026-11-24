---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-native-memleak-detection
title: Native内存泄漏问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 资源泄漏类问题检测 > 内存泄漏类问题检测方法 > Native内存泄漏问题检测方法
category: best-practices
scraped_at: 2026-11-24T12:47:54+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:1058420aa8e9fe699f308ac25d9d9aa56b88681b6accd4a9870ad0edfaa5e360
---

## 使用Allocation检测Native内存泄漏

应用在开发过程中，可能会因为API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。

DevEco Profiler提供了基础的内存场景分析Allocation，您可以使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 请参考模块级[build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)，增加strip字段并赋值为false（false值表示附带调试和符号信息，待发布上线版本建议恢复为true）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请录制模板前按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/dY7f2kcfT8S7aHL5BUG6oQ/zh-cn_image_0000002404125133.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=94804401D3C52A924D8960A98B04FE46D579A492B3206855C9B484F2A9AA5258)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](../harmonyos-guides/deep-recording.md)，或在会话区选择Open File，导入历史数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/y5rKRdYLTJa7IWKwGwU4cw/zh-cn_image_0000002370405580.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=74820BD298F0BA026AB84EF59A632247410D254677ED28AA9230AE6C0070C331)

   **说明** 

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
   * 在任务分析窗口，可以通过“Ctrl+,”向前选中单点时间标签，通过“Ctrl+.”向后选中单点时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](../harmonyos-guides/ide-insight-session-time.md#section186881175012)。

   Allocation分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/7JIrhLAKR0qcwVf2avaPuw/zh-cn_image_0000002404045293.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CAE6ED4D572CE79C0BEFAF0FF4208BB3FCCB89E96A85C1275840FC688CF86EC)指定要录制的泳道：

   * Memory泳道：显示当前进程的物理内存使用情况，其度量方式包含：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/1T1keFulQyS5U7zEBl9y-Q/zh-cn_image_0000002370565464.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=755F15246311715E345AA51DEF62CFF7E54A40D20B9892333449F98E959765A5)PSS：进程独占内存和按比例分配共享库占用内存之和。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Wk-u7AZIRVGl6ssb66WGUQ/zh-cn_image_0000002404125137.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B7EA8C4FF4C3B5C2005D84AD2604794F8A5EEA10208EAF9D1070DD3A75A9950)RSS：进程独占内存和相关共享库占用内存之和。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/6QOa7pjeR3KV2hLBwk4v6Q/zh-cn_image_0000002370405584.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8FFE36B798162CB36F0D4DDFF0ED006FA61DA6AAE16B7D7E1B198EE40434414)USS：进程独占内存。

   默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/6F1xJar1TRaiQlyGZdoNPw/zh-cn_image_0000002404045297.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=C84F7FD07792C23EF47E8BB0EEA776974888AF92B9A3D54C8B1425318FE90CE8)展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/7YPjlL9AT9umyJv7cgBtEA/zh-cn_image_0000002370565468.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E37D72C564A967903D2EEC852C5A3DE04A2CC78E7168E8C64DA96C671312DC7)

   **说明** 

   * ArkTS Heap：ArkTS堆的内存占用。
   * Native Heap：Native层（主要是应用依赖的so库的C/C++代码）使用new/malloc分配的堆内存。
   * GL：应用纹理内存，RS：纹理+图形渲染内存。
   * Graph：该进程按去重规则统计的dma内存占用，包括直接通过接口申请的dma buffer和通过allocator\_host申请的dma buffer。
   * Guard：保护段所占内存。
   * AnonPage Other：其他所有匿名页所占内存（非heap、anon:native\_heap、anon:ArkTS heap开头的匿名页）。
   * FilePage Other：其它映射到文件页但不能被归类到.so/.db/.ttf类型的内存占用，比如ashmem内存。
   * Dev：进程加载的以/dev开头的文件所占内存。
   * Stack：栈内存。
   * .hap：进程加载的.hap文件所占内存。
   * .so：进程加载的.so动态库所占内存。
   * .ttf：进程加载的.ttf字体文件所占内存。

   * ArkTS Allocation泳道：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/iirwSdGFQca7ATEVjEbEMA/zh-cn_image_0000002404125141.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AD576EDD7C2B744E45FAC72565050CECEE427EC002B9F5B8FD193D4AB6DE328)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

   **说明** 

   由于较大的性能开销可能导致卡顿/卡死问题，当前版本仅支持分开录制ArkTS Allocation和Native Allocation两条泳道。

   * Native Allocation泳道：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

   单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/L65eS4egSw23GjOjjqKT7Q/zh-cn_image_0000002370405588.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=492394C2D6C8F5AA4B411D10731D24A01417948BE4C8239EE4E9701CAD62B901)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。默认采用统计模式，统计间隔只在统计模式下才需要设置，可设置范围为1s~3600s，默认为10s，默认最小跟踪内存为1024Bytes。FP回栈模式下需要设置JS回栈深度和Native回栈深度，DWARF回栈模式下仅需要设置回栈深度。默认Native回栈深度为10层，JS回栈深度可配置范围为0-128，默认10层。设置完成后，在录制期间小于此大小的内存分配将被忽略，最大回栈深度将达到设置的值。

   **说明** 

   * 设置的最小跟踪内存数值越小、回栈深度越大，对应用造成的影响就越大，可能会导致DevEco Profiler卡顿。请根据应用实际的调测情况进行合理设置。
   * 统计模式用于不关注单次分配、关注应用较长时间的内存变化情况的场景，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长的目的。设置的Sampling Interval为近似值，即尽可能地在接近这个时间内做统计汇总，存在一定的偏差，偏差不超过1s，这个偏差不会对内存分配的正确性产生影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/cZ6agkdZSoWmhgWvRxWPxg/zh-cn_image_0000002404045301.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=E371F52B84589E1597164EC8476CC47DA95FD98036953B213DF2DA25B785B9EF)

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/3c5CL2YiSrmMzzQ_zlFvuA/zh-cn_image_0000002370565472.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB626F87CF7CA7A543AC2C0C3598B4C5E8E83F120CE12E836A27DA42547A4B3)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。

   Details区域中显示此时间段内指定类型的内存分析统计信息：

   Memory泳道：

   * 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和以及各种内存页面状态的内存占用总和。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/6jJj3uC8R3u8r8nxMGnAyg/zh-cn_image_0000002404125145.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=B68BEDFD76C3E54C5DDC1584F7049C8F896243A932AFA8EEF22B806C902E4D72)

   * 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

   **须知** 

   Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/lDfMoWKcQVqLBhyAuHP7Ug/zh-cn_image_0000002370405592.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=351B8925299CB4425F98E89CC6CCECC109008F500771C8028F566EB27DC57483)

   ArkTS Allocation泳道：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。

   * “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/YP6MihdeQrS43iH9uu69wg/zh-cn_image_0000002404045305.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6DC21E5621FC0E2B5C78825B83CF695F55651D70B75802DCDFB749E883327D)标识的对象，表示其可以通过窗口访问。每个时段内已释放的内存大小在柱子上置灰，未释放的内存保持绿色。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/UTdQCAjuR9ekc2ws2RhFWQ/zh-cn_image_0000002370565476.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=6702EC0838A80F48DE29CC3571DDF68E1523958D25F5AE1511614D84E5CF0B26)Native Allocation泳道：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。

   * Statistics页签中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

     点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
   * Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
   * Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。

   **说明** 

   统计模式（Statistics Mode）下不存在Allocations List信息。

   选择任一对象，右侧会展示与该对象相关的所有库和调用者

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/5jXMX8ANSSW4ULIRbDVEjg/zh-cn_image_0000002404125149.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=D315324AD685388F22B529D9515A461539E0857E2FFAC0A37CF2029F30CDD008)
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   当前版本仅支持Debug版本应用跳转到用户侧Native代码。

## 分析数据筛选

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

### 通过内存状态筛选

在Allocation分析过程中，对“Native Allocation”泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在“Native Allocation”泳道的“Details”区域左下方的下拉框中，可以选择过滤内存状态：

* All Allocations：详情区域展示当前框选时间段内的所有内存分配信息。
* Created & Existing：详情区域展示当前框选时间段内分配未释放的内存。
* Created & Released：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/v--akF6cT8W2mL05s8txhA/zh-cn_image_0000002370405596.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=831F96C15F422ABCFF639413308930E2F45C2F94E71CEE57120BEB24BA962050)

### 通过统计方式筛选

在“Native Allocation”泳道的“Statistics”页签中，可以打开“Native Size”选择统计方式以过滤统计数据：

* Native Size：详情区域按照对象的Native内存进行展示。
* Native Library：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Ho0_lPvfQlCVAkS2fIFzJg/zh-cn_image_0000002404045309.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=81A2C59FA6902F4D2FCF1A66242583772095052AFE11A49B0736EBFFB20C1166)

### 通过so库名筛选

在“Native Allocation”泳道的“Allocations List”页签中，可以单击“Click to choose”选择要筛选的so库以过滤出与目标so库相关的数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/7RPVkLZlRkuzKfYuXofzqw/zh-cn_image_0000002370565480.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=999385D90FA75C7FD7D9C683C29D3062182F40A9397A768397F866A7E0B03A71)

### 通过搜索筛选

在**Native Allocation**泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的<、>按键可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/h98l9G9MRKqNwjbxJGYapw/zh-cn_image_0000002404125153.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=749F2A400238664798B3D8E084043704EDF1CF6F791EAD7DB7BDDEAF8EB738F5)

### 筛选内存分配堆栈

在Native Allocation泳道的Call Trees页签中，可以通过底部的“Call Trees”和“Constraints”选择框来过筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* Separate by Allocated Size：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；
* Hide System Libraries：隐藏内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/QohjXYEKRvq16C1QqF4ung/zh-cn_image_0000002370405600.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB23AC641C7045A66D309D7FCDA705D6A516DF3E35618DBFEE1A799457A9F116)

Constraints选择框也包含了两种过滤条件：

* Count：根据指定的内存申请次数过滤内存分配栈信息；
* Bytes：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/NYpbqhy9QnuqwXj8MItIVw/zh-cn_image_0000002404045313.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEFCA18F18CA1449AEB37858F9BEFD4591C77E7D90D3CC08B4E6D5999D90C1E2)

在Call Trees页签的More区域，单击“Heaviest Stack”旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/nJJBiG5mQC6di5bptuMZYA/zh-cn_image_0000002370565484.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8673C6436DBB5F109A9B171D717756300410A3AC0804F3F9DCAE3C0830641C4)

在Call Trees页签，可以通过底部的“Flame Chart”切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/wm8ZvcFOQzyRPswfFqvzCw/zh-cn_image_0000002404125157.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=93E1312AF60AAB4B3CD378F103BF086734E8D9DA2CCC576051C5FBCE948BEE31)

### 分析启动内存

应用/元服务在启动过程中对内存资源的占用情况，是开发者较为关心的问题。DevEco Profiler的Allocation分析任务，提供了启动内存分析能力，协助开发者优化启动过程的内存占用。

针对调测应用的当前运行情况，DevEco Profiler对其做如下处理：

* 如选择的是已安装但未启动的应用，在启动该分析任务时，会自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。
* 如选择的是正在运行的应用，在启动该分析任务时，会先将应用关停，再自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。

具体操作方法为：在任务列表中单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/aPa_HWdQSZKrenWbYQv_rA/zh-cn_image_0000002370405604.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9D049435458552D94060A450B9618BE9FDEFD776C17DE2ED16002F7F9ED4C2B)按钮

在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同。
