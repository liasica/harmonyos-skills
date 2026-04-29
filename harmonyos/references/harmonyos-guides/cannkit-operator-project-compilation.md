---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-project-compilation
title: 算子工程编译
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 算子编译安装 > 算子工程编译
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47378b9d838a9b870df6fa0d3703f98d454808502eac0fd12fed596f2c334c78
---

算子kernel侧和host侧实现开发完成后，需要对算子工程进行编译，将自定义算子部署到omg工具中，详细的编译操作包括：

* 编译AscendC算子kernel侧代码实现文件\*.cpp，分为源码发布和二进制发布两种方式。

  + **源码发布：** 不对算子kernel侧实现进行编译，保留算子kernel源码文件\*.cpp。该方式可以支持模型的离线编译场景。
  + **二进制发布：** 对算子kernel侧实现进行编译，生成描述算子相关信息的json文件\*.json和算子二进制文件\*.o。算子调用时，如果需要直接调用算子二进制，则使用该编译方式，当前暂不支持该方式进行部署。
* 编译AscendC算子host侧代码实现文件\*.cpp、\*.h。

  + 将原型定义和shape推导实现编译成算子原型定义动态库libcustom\_op.so，并生成算子原型对外接口op\_proto.h。
  + 将算子信息库定义编译成信息库定义文件\*.json。

上述编译过程示意图如下。

**图1** 算子工程编译示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/cJvP3relQsm_auCKkTK5ug/zh-cn_image_0000002558765750.png?HW-CC-KV=V1&HW-CC-Date=20260429T054109Z&HW-CC-Expire=86400&HW-CC-Sign=92939C22194D82CFB50C5310FFB13264D1760F9304D25D3CA6D5DFB53DA03786)

## 编译步骤

1. 完成工程编译相关配置。

   修改工程目录下的**CMakePresets.json** cacheVariables的配置项。**CMakePresets.json**文件内容如下。

   ```
   1. {
   2. "version": 1,
   3. "cmakeMinimumRequired": {
   4. "major": 3,
   5. "minor": 19,
   6. "patch": 0
   7. },
   8. "configurePresets": [
   9. {
   10. "name": "default",
   11. "displayName": "Default Config",
   12. "description": "Default build using Unix Makefiles generator",
   13. "generator": "Unix Makefiles",
   14. "binaryDir": "${sourceDir}/build_out",
   15. "cacheVariables": {
   16. "CMAKE_BUILD_TYPE": {
   17. "type": "STRING",
   18. "value": "Release"
   19. },
   20. "ASCEND_COMPUTE_UNIT": {
   21. "type": "STRING",
   22. "value": "kirin9020"
   23. },
   24. "vendor_name": {
   25. "type": "STRING",
   26. "value": "customize"
   27. },
   28. "ASCEND_PYTHON_EXECUTABLE": {
   29. "type": "STRING",
   30. "value": "python3"
   31. },
   32. "CMAKE_INSTALL_PREFIX": {
   33. "type": "PATH",
   34. "value": "${sourceDir}/build_out"
   35. }
   36. }
   37. }
   38. ]
   39. }
   ```

   **表1** 需要开发者配置的常用参数列表

   | 参数名称 | 参数描述 | 默认值 |
   | --- | --- | --- |
   | CMAKE\_BUILD\_TYPE | 编译模式选项，可配置为：  - “Release”，Release版本，不包含调试信息，编译最终发布的版本。  - “Debug”，“Debug”版本，包含调试信息，便于开发者开发和调试。 | Release |
2. 在算子工程目录下执行如下命令，进行算子工程编译。

   ```
   1. ./build.sh
   ```

   编译成功后，会在当前目录下创建build\_out目录，并将build\_out目录下生成的自定义算子交付件安装到tools\_omg中。

   如果想单独编译算子kernel，可以在算子工程下执行如下命令：

   ```
   1. ./build_devices.sh
   ```

   开发者如果需要该编译过程日志存盘，可以使用环境变量ASCENDC\_BUILD\_LOG\_DIR来控制存储路径。

   ```
   1. # 如希望编译日志存储在/home/build_log/，则可以按照如下设置，默认不打开日志存储
   2. export ASCENDC_BUILD_LOG_DIR=/home/build_log/
   ```

## 支持自定义编译选项

在算子工程中，如果开发者想对算子kernel侧代码增加一些自定义的编译选项，可以参考如下内容进行编译选项的定制。

修改算子工程op\_kernel目录下的CMakeLists.txt，使用add\_ops\_compile\_options来增加编译选项，方法如下。

```
1. add_ops_compile_options(OpType COMPUTE_UNIT soc_version1 soc_version2 ... OPTIONS option1 option2 ...)
```

**表2** 具体参数介绍

| 参数名称 | 可选/必选 | 参数描述 |
| --- | --- | --- |
| OpType（算子类型） | 必选 | 第一个参数应传入算子类型，如果需要对算子工程中的所有算子生效，需要配置为ALL。 |
| COMPUTE\_UNIT | 可选 | 标识编译选项在哪些AI处理器型号上生效，多个型号之间通过空格间隔。不配置时表示对所有AI处理器型号生效。  **说明：** COMPUTE\_UNIT具体配置如下。  - kirin9020  - kirinx90 |
| OPTIONS | 必选 | 自定义的编译选项。多个编译选项之间通过空格间隔。  - 增加-D编译选项，用于在编译时定义宏。  OPTIONS -Dname=definition  - 增加-g -O0等调试用编译选项。  - 增加AscendC框架提供的调试用编译选项-DASCENDC\_DUMP、-DASCENDC\_DEBUG  - -DASCENDC\_DUMP用于控制Dump开关，默认开关打开，开发者调用printf/DumpTensor/assert后会有信息打印；设置为0后，表示开关关闭。  OPTIONS -DASCENDC\_DUMP=0  - -DASCENDC\_DEBUG用于控制AscendC API的调测开关，默认开关关闭；增加该编译选项后，表示开关打开，此时接口内部的assert校验生效，校验不通过会有assert日志打屏。开启该功能会对算子实际运行的性能带来一定影响，通常在调测阶段使用。  OPTIONS -DASCENDC\_DEBUG  当前-DASCENDC\_DEBUG功能支持的产品型号为：Kirin9020/KirinX90。  - --tiling\_key，设置该选项后，只编译指定的[TilingKey](cannkit-tiling-implementation-on-the-host.md#tilingkey可选)相关的kernel代码，用于加速编译过程。若不指定TilingKey编译，则默认编译所有的TilingKey。配置多个TilingKey时，TilingKey之间不能有空格。示例如下，其中1、2为tiling\_key。  --tiling\_key=1,2 |

**简要说明：**

* 编译选项是基于“算子类型+AI处理器型号系列”进行配置的，也就是说不同的“算子类型+AI处理器型号系列”可以配置不同的编译选项。

  ```
  1. add_ops_compile_options(AddCustom COMPUTE_UNIT kirin9020 ... OPTIONS -DNEW_MACRO1=xx)
  2. add_ops_compile_options(AddCustom COMPUTE_UNIT kirin9020 ... OPTIONS -DNEW_MACRO2=xx)
  3. add_ops_compile_options(AddCustom COMPUTE_UNIT kirin9020 ... OPTIONS -DNEW_MACRO3=xx)
  ```
* 对相同算子类型+AI处理器型号系列，做多次编译选项配置，以后配置的为准。
* 对ALL生效的编译选项和对单一算子生效的编译选项如果没有冲突，同时生效，如果有冲突，以单一算子的编译选项为准。
